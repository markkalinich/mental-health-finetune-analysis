#!/usr/bin/env python3
"""
Read-only SQL aggregates on cache results.db. Writes facts only (no interpretation).

Usage:
  python utilities/cache_qc_report.py
  python utilities/cache_qc_report.py --db manuscript_paper_cache/results.db
  python utilities/cache_qc_report.py --output manuscript_paper_cache/qc_report_latest.md
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Sequence, TextIO, Tuple

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MODELS_CONFIG = ROOT / "config" / "models_config.csv"

# Paper tasks (SI/TR/TE): two cache prompt_name labels map to TE (same prompt file hash in QC).
TASK_COLUMN: Dict[str, str] = {
    "system_suicide_detection_v2": "SI",
    "therapy_request_classifier_v3": "TR",
    "therapy_engagement_conversation_prompt_v2": "TE",
    "therapy_engagement_conversation_v2": "TE",
}

# Three paper tasks → prompt_name values present in manuscript cache (TE has two labels).
TASK_PROMPT_NAMES: Dict[str, List[str]] = {
    "SI": ["system_suicide_detection_v2"],
    "TR": ["therapy_request_classifier_v3"],
    "TE": [
        "therapy_engagement_conversation_prompt_v2",
        "therapy_engagement_conversation_v2",
    ],
}


def load_registry_lm_studio_qwen(models_config: Path) -> Tuple[Dict[str, bool], int]:
    """
    Single source of truth: enabled rows in `models_config.csv` only.

    Maps `lm_studio_id` → True iff `family` starts with `qwen`.
    Every enabled row must have a non-empty `lm_studio_id` (otherwise that row is skipped
    with a stderr warning — fix the CSV).
    """
    id_qwen: Dict[str, bool] = {}
    n_enabled = 0
    with models_config.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("enabled", "True").strip().lower() != "true":
                continue
            n_enabled += 1
            fam = (row.get("family") or "").strip()
            lid = (row.get("lm_studio_id") or "").strip()
            if not lid:
                print(
                    f"WARNING: enabled model row has empty lm_studio_id (family={fam!r}); "
                    f"fix {models_config}",
                    file=sys.stderr,
                )
                continue
            id_qwen[lid] = fam.startswith("qwen")
    return id_qwen, n_enabled


def normalize_version(version: str) -> str:
    """Match `orchestration/experiment_manager.py` / `MODEL_NAME_MAP` keying."""
    v = str(version)
    if v.endswith(".0"):
        v = v[:-2]
    return v


def load_config_triple_to_lm_studio(
    models_config: Path,
) -> Dict[Tuple[str, str, str], str]:
    """
    Enabled rows only: (family, size, normalized_version) -> lm_studio_id.
    Same key construction as `get_model_name_map()` in experiment_manager.py.
    """
    triple_map: Dict[Tuple[str, str, str], str] = {}
    with models_config.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("enabled", "True").strip().lower() != "true":
                continue
            fam = (row.get("family") or "").strip()
            size = (row.get("size") or "").strip()
            ver_raw = str(row.get("version") or "").strip()
            ver_key = ver_raw
            if ver_key.endswith(".0"):
                ver_key = ver_key[:-2]
            lid = (row.get("lm_studio_id") or "").strip()
            if not lid:
                continue
            triple_map[(fam, size, ver_key)] = lid
    return triple_map


def load_enabled_lm_studio_ids(models_config: Path) -> set[str]:
    """Set of enabled `lm_studio_id` values in `models_config.csv`."""
    ids: set[str] = set()
    with models_config.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("enabled", "True").strip().lower() != "true":
                continue
            lid = (row.get("lm_studio_id") or "").strip()
            if lid:
                ids.add(lid)
    return ids


def load_approved_crosswalk_csv(path: Path, enabled_lm_ids: set[str]) -> Dict[str, str]:
    """
    User-approved rows only: `model_full_name` (as in cache) → `lm_studio_id` (must be enabled).

    Missing file or header-only file → no overrides.
    """
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return {}
        fn_field = "model_full_name"
        lm_field = "lm_studio_id"
        if fn_field not in reader.fieldnames or lm_field not in reader.fieldnames:
            print(
                f"ERROR: {path} must have columns {fn_field!r} and {lm_field!r}.",
                file=sys.stderr,
            )
            raise SystemExit(1)
        out: Dict[str, str] = {}
        for i, row in enumerate(reader, start=2):
            k = (row.get(fn_field) or "").strip()
            v = (row.get(lm_field) or "").strip()
            if not k and not v:
                continue
            if not k or not v:
                print(f"ERROR: {path} line {i}: empty model_full_name or lm_studio_id.", file=sys.stderr)
                raise SystemExit(1)
            if k in out:
                print(f"ERROR: {path} duplicate model_full_name {k!r}.", file=sys.stderr)
                raise SystemExit(1)
            if v not in enabled_lm_ids:
                print(
                    f"ERROR: {path} line {i}: lm_studio_id {v!r} is not an enabled id in models_config.",
                    file=sys.stderr,
                )
                raise SystemExit(1)
            out[k] = v
        return out


@dataclass
class ModelResolutionResult:
    """Result of cache model → canonical `lm_studio_id` resolution."""

    resolved_lm_by_cache_name: Dict[str, str] = field(default_factory=dict)
    triple_direct: List[str] = field(default_factory=list)
    """Cache `model_full_name` where string equals triple-derived `lm_studio_id`."""
    label_drift_fixed_by_csv: List[Tuple[str, str, str, str, str]] = field(default_factory=list)
    """(family, size, version, cache name, registry lm_studio_id) — triple matched; strings differed."""
    triple_missing_fixed_by_csv: List[Tuple[str, str, str, str, str]] = field(default_factory=list)
    """(family, size, version, cache name, approved lm_studio_id) — no registry triple."""
    fixed_by_approved_csv: List[Tuple[str, str]] = field(default_factory=list)
    """(model_full_name, resolved lm_studio_id) — every row that used approved CSV."""
    conflicts: List[str] = field(default_factory=list)
    """Human-readable lines (approved row contradicts registry triple)."""
    unresolved: List[Tuple[str, str, str, str, str]] = field(default_factory=list)
    """(family, size, version, model_full_name, reason) — still broken after approved CSV."""


def resolve_cache_models(
    conn: sqlite3.Connection,
    triple_map: Dict[Tuple[str, str, str], str],
    enabled_lm_ids: set[str],
    approved: Dict[str, str],
) -> ModelResolutionResult:
    """
    (a) Map via `(family, size, normalized version)` → `lm_studio_id` (same as runtime).

    If `model_full_name` equals that id → done.

    If triple exists but strings differ → require `approved[model_full_name] == lm_studio_id`.

    If triple missing → require `approved[model_full_name]` in enabled ids.

    Contradictions (approved id ≠ triple when triple exists) are recorded as conflicts.
    """
    rows = conn.execute(
        """
        SELECT DISTINCT model_family, model_size, model_version, model_full_name
        FROM cache_keys
        ORDER BY model_family, model_size, model_version, model_full_name
        """
    ).fetchall()
    res = ModelResolutionResult()

    for r in rows:
        fam = (r["model_family"] or "").strip()
        size = (r["model_size"] or "").strip()
        ver_raw = str(r["model_version"] or "").strip()
        mfn = (r["model_full_name"] or "").strip()
        nv = normalize_version(ver_raw)
        lm_triple = triple_map.get((fam, size, nv))
        if lm_triple is None:
            lm_triple = triple_map.get((fam, size, ver_raw))

        if lm_triple is not None:
            if mfn == lm_triple:
                res.resolved_lm_by_cache_name[mfn] = lm_triple
                res.triple_direct.append(mfn)
                continue
            ap = approved.get(mfn)
            if ap == lm_triple:
                res.resolved_lm_by_cache_name[mfn] = lm_triple
                res.fixed_by_approved_csv.append((mfn, lm_triple))
                res.label_drift_fixed_by_csv.append((fam, size, ver_raw, mfn, lm_triple))
                continue
            if ap is None:
                res.unresolved.append(
                    (
                        fam,
                        size,
                        ver_raw,
                        mfn,
                        "label drift: add approved CSV row mapping model_full_name → "
                        f"{lm_triple!r} (registry triple)",
                    )
                )
                continue
            res.conflicts.append(
                f"{mfn!r}: approved lm_studio_id {ap!r} but registry triple requires {lm_triple!r}"
            )
            res.unresolved.append(
                (
                    fam,
                    size,
                    ver_raw,
                    mfn,
                    f"approved CSV contradicts registry triple (expected {lm_triple!r})",
                )
            )
            continue

        ap = approved.get(mfn)
        if ap in enabled_lm_ids:
            res.resolved_lm_by_cache_name[mfn] = ap
            res.fixed_by_approved_csv.append((mfn, ap))
            res.triple_missing_fixed_by_csv.append((fam, size, ver_raw, mfn, ap))
            continue
        if ap is None:
            res.unresolved.append(
                (
                    fam,
                    size,
                    ver_raw,
                    mfn,
                    "no registry triple for this (family, size, version); add approved CSV row",
                )
            )
            continue
        res.conflicts.append(f"{mfn!r}: approved lm_studio_id {ap!r} not in enabled registry")
        res.unresolved.append(
            (fam, size, ver_raw, mfn, "approved lm_studio_id invalid (should be caught at load)")
        )

    return res


def print_resolution_failure_stderr(rr: ModelResolutionResult) -> None:
    print("ERROR: QC aborted — not every cache model could be resolved to a canonical lm_studio_id.", file=sys.stderr)
    if rr.conflicts:
        print("Contradictions (fix approved CSV):", file=sys.stderr)
        for c in rr.conflicts:
            print(f"  {c}", file=sys.stderr)
    if rr.unresolved:
        print("Still unresolved:", file=sys.stderr)
        for fam, size, ver, mfn, reason in rr.unresolved:
            print(f"  {mfn!r} ({fam}/{size}/{ver}): {reason}", file=sys.stderr)


def emit_model_resolution_section(out: TextIO, rr: ModelResolutionResult, crosswalk_path: Path) -> None:
    print(
        "**(a)** Map each distinct cache row using **`(model_family, model_size, normalized "
        "model_version)`** → `lm_studio_id` in `models_config.csv` (same as "
        "`experiment_manager` / `MODEL_NAME_MAP`).",
        file=out,
    )
    print("", file=out)
    print(
        "**(b) Models not mapped by triple alone** (label drift, or no registry triple for that key):",
        file=out,
    )
    n_drift = len(rr.label_drift_fixed_by_csv)
    n_miss = len(rr.triple_missing_fixed_by_csv)
    if n_drift == 0 and n_miss == 0:
        print(
            "*(none — every `model_full_name` matched the triple-derived `lm_studio_id` "
            "without an approved crosswalk row.)*",
            file=out,
        )
    else:
        if n_drift:
            print("", file=out)
            print("*Label drift (triple matched; cache string ≠ registry id until approved CSV):*", file=out)
            print("", file=out)
            md_table(
                out,
                [
                    "model_family",
                    "model_size",
                    "model_version",
                    "model_full_name (cache)",
                    "lm_studio_id (registry triple)",
                ],
                [[a, b, c, d, e] for a, b, c, d, e in rr.label_drift_fixed_by_csv],
            )
        if n_miss:
            print("", file=out)
            print("*No registry triple; mapping from approved CSV only:*", file=out)
            print("", file=out)
            md_table(
                out,
                [
                    "model_family",
                    "model_size",
                    "model_version",
                    "model_full_name (cache)",
                    "lm_studio_id (approved)",
                ],
                [[a, b, c, d, e] for a, b, c, d, e in rr.triple_missing_fixed_by_csv],
            )
    print("", file=out)
    print(
        f"**(c)** Approved crosswalk file: `{crosswalk_path.resolve()}` "
        f"({len(rr.fixed_by_approved_csv)} row(s) applied).",
        file=out,
    )
    if rr.fixed_by_approved_csv:
        print("", file=out)
        md_table(
            out,
            ["model_full_name (cache)", "resolved lm_studio_id"],
            [[a, b] for a, b in rr.fixed_by_approved_csv],
        )
    print("", file=out)
    print(
        "**(d)** Resolution status: **complete** — every cache model maps to one enabled "
        "`lm_studio_id`. Metrics below use **`resolved_lm_studio_id`** for registry lookups "
        "(Qwen family, etc.) when it differs from `model_full_name`.",
        file=out,
    )


def connect(db: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{db.resolve()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


class TeeStdout:
    """Send stdout to console and optional file."""

    def __init__(self, file_obj: TextIO | None) -> None:
        self._file = file_obj
        self._stdout = sys.__stdout__

    def write(self, s: str) -> int:
        self._stdout.write(s)
        if self._file is not None:
            self._file.write(s)
        return len(s)

    def flush(self) -> None:
        self._stdout.flush()
        if self._file is not None:
            self._file.flush()


def md_escape_cell(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def md_h(out: TextIO, level: int, title: str) -> None:
    print(file=out)
    print(f"{'#' * level} {title}", file=out)
    print(file=out)


def md_table(out: TextIO, headers: Sequence[str], rows: Sequence[Sequence[str]]) -> None:
    h = [md_escape_cell(x) for x in headers]
    print("| " + " | ".join(h) + " |", file=out)
    print("| " + " | ".join("---" for _ in h) + " |", file=out)
    for row in rows:
        print("| " + " | ".join(md_escape_cell(str(c)) for c in row) + " |", file=out)


def _task_columns_ordered(prompt_names_in_db: List[str]) -> List[str]:
    labels = ["SI", "TR", "TE"]
    present = {TASK_COLUMN.get(p) for p in prompt_names_in_db}
    return [c for c in labels if c in present]


def build_model_task_matrix(
    conn: sqlite3.Connection,
    status_predicate: str,
    status_params: Tuple = (),
) -> Tuple[List[str], List[str], Dict[Tuple[str, str], int]]:
    """
    Rows: model_full_name. Columns: SI, TR, TE (prompt_name mapped via TASK_COLUMN).
    """
    models = [
        r[0]
        for r in conn.execute(
            "SELECT DISTINCT model_full_name FROM cache_keys ORDER BY model_full_name"
        ).fetchall()
    ]
    pnames = [
        r[0]
        for r in conn.execute(
            "SELECT DISTINCT prompt_name FROM cache_keys ORDER BY prompt_name"
        ).fetchall()
    ]
    cols = _task_columns_ordered(pnames)
    q = f"""
        SELECT ck.model_full_name, ck.prompt_name, COUNT(*) AS n
        FROM cached_results cr
        JOIN cache_keys ck ON cr.cache_id = ck.cache_id
        WHERE ({status_predicate})
        GROUP BY ck.model_full_name, ck.prompt_name
    """
    counts: Dict[Tuple[str, str], int] = {}
    for r in conn.execute(q, status_params):
        task = TASK_COLUMN.get(r["prompt_name"])
        if task is None:
            continue
        key = (r["model_full_name"], task)
        counts[key] = counts.get(key, 0) + int(r["n"])
    return models, cols, counts


def write_matrix_csv(
    path: Path,
    models: List[str],
    task_cols: List[str],
    counts: Dict[Tuple[str, str], int],
) -> None:
    """Write CSV with model, total (sum over tasks), task columns; rows sorted by total descending."""

    def row_total(m: str) -> int:
        return sum(counts.get((m, t), 0) for t in task_cols)

    models_sorted = sorted(models, key=row_total, reverse=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["model", "total"] + task_cols)
        for m in models_sorted:
            task_vals = [counts.get((m, t), 0) for t in task_cols]
            w.writerow([m, sum(task_vals)] + task_vals)


def _enabled_qwen_non_qwen_counts(id_qwen: Dict[str, bool]) -> Tuple[int, int]:
    """Counts of enabled models in registry with family qwen vs not."""
    n_q = sum(1 for v in id_qwen.values() if v)
    n_n = sum(1 for v in id_qwen.values() if not v)
    return n_q, n_n


def _slice_family_mode(
    conn: sqlite3.Connection,
    prompt_names: Tuple[str, ...],
    prompt_hash: str,
    resolved_lm: Dict[str, str],
    id_qwen: Dict[str, bool],
) -> str:
    """
    Whether cache_keys rows for this (task prompt set, hash) use only qwen, only non-qwen,
    or mixed resolved families (should be rare for one prompt_hash).
    """
    ph = ",".join("?" * len(prompt_names))
    rows = conn.execute(
        f"""
        SELECT DISTINCT model_full_name FROM cache_keys
        WHERE prompt_name IN ({ph}) AND prompt_hash = ?
        """,
        (*prompt_names, prompt_hash),
    ).fetchall()
    if not rows:
        return "empty"
    flags = [id_qwen[resolved_lm[r[0]]] for r in rows]
    if all(flags):
        return "qwen"
    if not any(flags):
        return "non_qwen"
    return "mixed"


def run_report(
    conn: sqlite3.Connection,
    out: TextIO,
    tables_dir: Path | None,
    models_config: Path,
    id_qwen: Dict[str, bool],
    n_enabled: int,
    resolution: ModelResolutionResult,
    crosswalk_path: Path,
) -> None:
    md_h(out, 2, "0) Row counts")
    ck = conn.execute("SELECT COUNT(*) FROM cache_keys").fetchone()[0]
    cr = conn.execute("SELECT COUNT(*) FROM cached_results").fetchone()[0]
    print(
        f"- `cache_keys`: **{ck}** — `cached_results`: **{cr}** "
        f"(equal: **{ck == cr}**).",
        file=out,
    )
    print(
        f"- Enabled models in `{models_config.name}`: **{n_enabled}** "
        f"(Qwen vs other use **resolved** `lm_studio_id`; see §1).",
        file=out,
    )

    md_h(out, 2, "1) Cache model → registry mapping")
    emit_model_resolution_section(out, resolution, crosswalk_path)

    resolved_lm = resolution.resolved_lm_by_cache_name
    n_qwen_enabled, n_non_qwen_enabled = _enabled_qwen_non_qwen_counts(id_qwen)

    md_h(out, 2, "2) Prompt content by `prompt_hash`")
    print(
        "One row per distinct `prompt_hash` (MD5 of stored prompt text). "
        "**`prompt_name(s)`** lists every label in `cache_keys` that maps to that hash. "
        "**% qwen family** = share of rows where the **resolved** `lm_studio_id` has `family` "
        "starting with `qwen` in the registry.",
        file=out,
    )
    hash_rows = conn.execute(
        """
        SELECT prompt_hash, model_full_name, COUNT(*) AS n
        FROM cache_keys
        GROUP BY prompt_hash, model_full_name
        ORDER BY prompt_hash, model_full_name
        """
    ).fetchall()
    by_ph: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
    for r in hash_rows:
        by_ph[r["prompt_hash"]].append((r["model_full_name"], int(r["n"])))

    names_by_ph = conn.execute(
        """
        SELECT prompt_hash, GROUP_CONCAT(DISTINCT prompt_name) AS prompt_names
        FROM cache_keys
        GROUP BY prompt_hash
        """
    ).fetchall()
    ph_to_names = {r["prompt_hash"]: r["prompt_names"] or "" for r in names_by_ph}

    detail_rows: List[List[str]] = []
    for ph in sorted(by_ph.keys()):
        nk = sum(t[1] for t in by_ph[ph])
        n_q = n_nq = 0
        for mfn, c in by_ph[ph]:
            lm = resolved_lm[mfn]
            if id_qwen[lm]:
                n_q += c
            else:
                n_nq += c
        pct_q = f"{100.0 * n_q / nk:.1f}%" if nk else "0.0%"
        raw = (ph_to_names.get(ph) or "").split(",")
        names_sorted = ", ".join(sorted({x.strip() for x in raw if x.strip()}))
        detail_rows.append([names_sorted, ph, str(nk), pct_q])

    print("", file=out)
    md_table(
        out,
        [
            "prompt_name(s)",
            "prompt_hash",
            "cache_keys",
            "% qwen family (registry)",
        ],
        detail_rows,
    )

    md_h(out, 2, "3) Per task check: prompt hash, coverage, balance")
    print(
        "One **row per `(task, prompt_hash)`** (same `prompt_name` may appear on multiple rows if "
        "it shares a hash with another label; each hash appears once per task). "
        "**Applicable enabled models** = registry count for **qwen** or **non-qwen** `family` when "
        "that slice is family-pure (typical when a task uses one hash for Qwen models and another "
        "for the rest). **Expected `cache_keys`** = applicable enabled models × distinct "
        "`input_hash` values in that slice. **`OK`** is **True** when that expected count equals "
        "**`cache_keys`** and **`cached_results`** equals **`cache_keys`** (always **False** / **n/a** "
        "when the slice mixes qwen and non-qwen models on the same `prompt_hash`).",
        file=out,
    )
    cov_rows: List[List[str]] = []
    for task_key in ("SI", "TR", "TE"):
        pnames = tuple(TASK_PROMPT_NAMES[task_key])
        ph_in = ",".join("?" * len(pnames))
        hash_list = [
            r[0]
            for r in conn.execute(
                f"""
                SELECT DISTINCT prompt_hash FROM cache_keys
                WHERE prompt_name IN ({ph_in})
                ORDER BY prompt_hash
                """,
                pnames,
            ).fetchall()
        ]
        for ph in hash_list:
            names_raw = conn.execute(
                f"""
                SELECT GROUP_CONCAT(DISTINCT prompt_name) AS pn FROM cache_keys
                WHERE prompt_name IN ({ph_in}) AND prompt_hash = ?
                """,
                (*pnames, ph),
            ).fetchone()[0]
            names_sorted = ", ".join(
                sorted({x.strip() for x in (names_raw or "").split(",") if x.strip()})
            )
            n_stmt = conn.execute(
                f"""
                SELECT COUNT(DISTINCT input_hash) FROM cache_keys
                WHERE prompt_name IN ({ph_in}) AND prompt_hash = ?
                """,
                (*pnames, ph),
            ).fetchone()[0]
            ck_n = conn.execute(
                f"""
                SELECT COUNT(*) FROM cache_keys
                WHERE prompt_name IN ({ph_in}) AND prompt_hash = ?
                """,
                (*pnames, ph),
            ).fetchone()[0]
            n_cr = conn.execute(
                f"""
                SELECT COUNT(*) FROM cached_results cr
                INNER JOIN cache_keys ck ON cr.cache_id = ck.cache_id
                WHERE ck.prompt_name IN ({ph_in}) AND ck.prompt_hash = ?
                """,
                (*pnames, ph),
            ).fetchone()[0]
            mode = _slice_family_mode(conn, pnames, ph, resolved_lm, id_qwen)
            if mode == "qwen":
                n_app = n_qwen_enabled
                app_label = f"{n_app} (qwen)"
                expected = n_app * int(n_stmt)
            elif mode == "non_qwen":
                n_app = n_non_qwen_enabled
                app_label = f"{n_app} (non-qwen)"
                expected = n_app * int(n_stmt)
            elif mode == "mixed":
                n_app = 0
                app_label = "mixed families in slice"
                expected = -1
            else:
                n_app = 0
                app_label = "0 (empty)"
                expected = 0
            if expected >= 0:
                ok = str(ck_n == expected and n_cr == ck_n)
                exp_cell = str(expected)
            else:
                ok = "n/a"
                exp_cell = "—"
            cov_rows.append(
                [
                    task_key,
                    ph,
                    names_sorted,
                    app_label,
                    str(n_stmt),
                    str(ck_n),
                    exp_cell,
                    ok,
                    str(n_cr),
                ]
            )
    print("", file=out)
    md_table(
        out,
        [
            "task",
            "prompt_hash",
            "prompt_name(s)",
            "enabled models (applicable)",
            "distinct statements",
            "cache_keys",
            "expected (n_enabled × n_stmt)",
            "OK",
            "cached_results",
        ],
        cov_rows,
    )

    md_h(out, 2, "4) temperature, max_tokens, top_p")
    rows = conn.execute(
        """
        SELECT temperature, max_tokens, top_p, COUNT(*) AS n
        FROM cache_keys
        GROUP BY temperature, max_tokens, top_p
        ORDER BY n DESC
        """
    ).fetchall()
    print(
        f"Distinct `(temperature, max_tokens, top_p)` rows: **{len(rows)}**",
        file=out,
    )
    md_table(
        out,
        ["temperature", "max_tokens", "top_p", "cache_keys"],
        [
            [str(r["temperature"]), str(r["max_tokens"]), str(r["top_p"]), str(r["n"])]
            for r in rows
        ],
    )

    md_h(out, 2, "5) cache_keys.created_at by calendar day")
    rows = conn.execute(
        """
        SELECT substr(created_at, 1, 10) AS day, COUNT(*) AS n
        FROM cache_keys
        GROUP BY day
        ORDER BY day
        """
    ).fetchall()
    md_table(out, ["calendar day", "cache_keys"], [[r["day"], str(r["n"])] for r in rows])
    mm = conn.execute(
        "SELECT MIN(created_at), MAX(created_at) FROM cache_keys"
    ).fetchone()
    print(f"- `MIN(created_at)`: `{mm[0]}`", file=out)
    print(f"- `MAX(created_at)`: `{mm[1]}`", file=out)

    md_h(out, 2, "6) cached_results: replicate_index, status, api_error breakdown")
    cr2 = conn.execute("SELECT COUNT(*) FROM cached_results").fetchone()[0]
    it = conn.execute("SELECT COUNT(*) FROM input_texts").fetchone()[0]
    print(
        f"`input_texts` rows (deduplicated input bodies): **{it}** "
        f"(row counts for `cache_keys` / `cached_results` are in **0) Row counts** above).",
        file=out,
    )
    print("", file=out)
    rep = conn.execute(
        """
        SELECT replicate_index, COUNT(*) AS n
        FROM cached_results
        GROUP BY replicate_index
        ORDER BY replicate_index
        """
    ).fetchall()
    print("`replicate_index`:", file=out)
    print("", file=out)
    md_table(
        out,
        ["replicate_index", "rows"],
        [[str(r["replicate_index"]), str(r["n"])] for r in rep],
    )

    print("", file=out)
    n_ok = conn.execute(
        "SELECT COUNT(*) FROM cached_results WHERE status = 'ok'"
    ).fetchone()[0]
    n_pf = conn.execute(
        "SELECT COUNT(*) FROM cached_results WHERE status = 'parse_fail'"
    ).fetchone()[0]
    n_api = conn.execute(
        "SELECT COUNT(*) FROM cached_results WHERE status LIKE 'api_error%'"
    ).fetchone()[0]
    n_other = cr2 - n_ok - n_pf - n_api
    print("`status`:", file=out)
    status_rows = [
        ["ok", str(n_ok)],
        ["parse_fail", str(n_pf)],
        ["api_error", str(n_api)],
    ]
    if n_other:
        status_rows.append(["other", str(n_other)])
    print("", file=out)
    md_table(out, ["status", "cached_results"], status_rows)
    if cr2:
        print(f"- `api_error` / `cached_results`: **{n_api / cr2:.6f}**", file=out)

    n_to = conn.execute(
        """
        SELECT COUNT(*) FROM cached_results
        WHERE status LIKE 'api_error%' AND status LIKE '%timeout%'
        """
    ).fetchone()[0]
    n_400 = conn.execute(
        """
        SELECT COUNT(*) FROM cached_results
        WHERE status LIKE 'api_error%' AND status LIKE '%400%'
        """
    ).fetchone()[0]
    n_rest = n_api - n_to - n_400
    print("", file=out)
    print("`api_error` substring counts on `status` field:", file=out)
    md_table(
        out,
        ["pattern", "count"],
        [
            ["`LIKE '%timeout%'`", str(n_to)],
            ["`LIKE '%400%'`", str(n_400)],
            ["remaining `api_error`", str(n_rest)],
        ],
    )

    if tables_dir is not None:
        pf_models, pf_cols, pf_counts = build_model_task_matrix(
            conn, "cr.status = 'parse_fail'"
        )
        api_models, api_cols, api_counts = build_model_task_matrix(
            conn, "cr.status LIKE 'api_error%'"
        )
        parse_path = tables_dir / "qc_parse_fail_matrix.csv"
        api_path = tables_dir / "qc_api_error_matrix.csv"
        write_matrix_csv(parse_path, pf_models, pf_cols, pf_counts)
        write_matrix_csv(api_path, api_models, api_cols, api_counts)
        print("", file=out)
        print("Model × task tables (CSV, same directory as this report):", file=out)
        print(f"- Parse failures: `{parse_path.name}`", file=out)
        print(f"- API errors: `{api_path.name}`", file=out)


def main() -> int:
    parser = argparse.ArgumentParser(description="QC report for results.db (facts only)")
    parser.add_argument(
        "--db",
        type=Path,
        default=ROOT / "manuscript_paper_cache" / "results.db",
        help="Path to results.db (read-only)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Also write the full report to this file (UTF-8 Markdown)",
    )
    parser.add_argument(
        "--tables-dir",
        type=Path,
        default=None,
        help="Directory for qc_parse_fail_matrix.csv and qc_api_error_matrix.csv "
        "(default: parent of --output, or omitted if --output unset)",
    )
    parser.add_argument(
        "--models-config",
        type=Path,
        default=DEFAULT_MODELS_CONFIG,
        help="Path to models_config.csv (registry triple + lm_studio_id for Qwen, etc.)",
    )
    parser.add_argument(
        "--crosswalk-csv",
        type=Path,
        default=None,
        help="Approved crosswalk: model_full_name,lm_studio_id (default: <db parent>/model_cache_crosswalk_approved.csv)",
    )
    args = parser.parse_args()

    if not args.db.exists():
        print(f"ERROR: Database not found: {args.db}", file=sys.stderr)
        return 1
    if not args.models_config.exists():
        print(f"ERROR: models_config not found: {args.models_config}", file=sys.stderr)
        return 1

    crosswalk_csv = (
        args.crosswalk_csv if args.crosswalk_csv is not None else args.db.parent / "model_cache_crosswalk_approved.csv"
    )

    triple_map = load_config_triple_to_lm_studio(args.models_config)
    enabled_ids = load_enabled_lm_studio_ids(args.models_config)
    id_qwen, n_enabled = load_registry_lm_studio_qwen(args.models_config)
    approved = load_approved_crosswalk_csv(crosswalk_csv, enabled_ids)

    conn = connect(args.db)
    try:
        resolution = resolve_cache_models(conn, triple_map, enabled_ids, approved)
    finally:
        conn.close()

    if resolution.unresolved:
        print_resolution_failure_stderr(resolution)
        return 1

    tables_dir: Path | None = None
    if args.tables_dir is not None:
        tables_dir = args.tables_dir
    elif args.output is not None:
        tables_dir = args.output.parent

    file_obj = None
    old_stdout = sys.stdout
    try:
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            file_obj = open(args.output, "w", encoding="utf-8")
            sys.stdout = TeeStdout(file_obj)

        print("# Cache QC report", file=sys.stdout)
        print("", file=sys.stdout)
        print(f"- **Script:** `cache_qc_report.py`", file=sys.stdout)
        print(f"- **Database:** `{args.db.resolve()}`", file=sys.stdout)
        conn = connect(args.db)
        try:
            run_report(
                conn,
                sys.stdout,
                tables_dir,
                args.models_config,
                id_qwen,
                n_enabled,
                resolution,
                crosswalk_csv,
            )
        finally:
            conn.close()
    finally:
        sys.stdout = old_stdout
        if file_obj is not None:
            file_obj.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
