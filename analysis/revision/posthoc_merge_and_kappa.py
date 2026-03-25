#!/usr/bin/env python3
"""
Merge psychiatrist 2 post-hoc ratings into intermediate score tables and compute
Cohen's kappa on the full sample (no missing P2 after merge).

Revision CSVs (lowercase keep / remove / change) live under:
    data/revision_data/psychiatrist02_review/

Merged tables:
    data/revision_data/merged/

Results:
    data/revision_data/results/posthoc_kappa_merged.csv
    data/revision_data/results/posthoc_merge_validation.csv

Cohen's κ uses one binary per rater: **as-is OK** (keep the model wording) vs **not as-is OK**
(change or remove). P1: `KEPT_exact_match` vs (`KEPT_with_changes` | `REMOVED`). P2 (SI/TR):
`KEPT` vs (`KEPT_with_changes` | `REMOVED`). P2 (therapy engagement): `KEPT_exact_match` vs
(`KEPT_with_changes` | `REMOVED`). Agreement = both on the same side of that split.

Usage (from repository root):
    python analysis/revision/posthoc_merge_and_kappa.py
"""

from __future__ import annotations

import csv
import importlib.util
import math
import random
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
INTERMEDIATE = REPO_ROOT / "data" / "inputs" / "intermediate_files"
REVIEW = REPO_ROOT / "data" / "revision_data" / "psychiatrist02_review"
MERGED_DIR = REPO_ROOT / "data" / "revision_data" / "merged"
RESULTS_DIR = REPO_ROOT / "data" / "revision_data" / "results"

_te_mod = importlib.util.spec_from_file_location(
    "therapy_engagement_conversations",
    Path(__file__).resolve().parent / "therapy_engagement_conversations.py",
)
_te = importlib.util.module_from_spec(_te_mod)
assert _te_mod.loader is not None
_te_mod.loader.exec_module(_te)
dedupe_by_conversation = _te.dedupe_by_conversation

BOOTSTRAP_REPS = 5000
BOOTSTRAP_SEED = 42


def cohen_kappa_binary(r1: list[bool], r2: list[bool]) -> float:
    n = len(r1)
    if n == 0:
        return float("nan")
    p_o = sum(1 for a, b in zip(r1, r2) if a == b) / n
    p1_pos = sum(r1) / n
    p2_pos = sum(r2) / n
    p_e = p1_pos * p2_pos + (1 - p1_pos) * (1 - p2_pos)
    if abs(1.0 - p_e) < 1e-15:
        return 1.0 if abs(1.0 - p_o) < 1e-15 else 0.0
    return (p_o - p_e) / (1.0 - p_e)


def bootstrap_kappa(
    r1: list[bool],
    r2: list[bool],
    *,
    n_boot: int = BOOTSTRAP_REPS,
    seed: int = BOOTSTRAP_SEED,
) -> tuple[float, float]:
    rng = random.Random(seed)
    n = len(r1)
    if n < 2:
        return (float("nan"), float("nan"))
    vals: list[float] = []
    for _ in range(n_boot):
        idx = [rng.randrange(n) for _ in range(n)]
        k = cohen_kappa_binary([r1[i] for i in idx], [r2[i] for i in idx])
        if not math.isnan(k):
            vals.append(k)
    if len(vals) < 50:
        return (float("nan"), float("nan"))
    vals.sort()
    return (vals[int(0.025 * (len(vals) - 1))], vals[int(0.975 * (len(vals) - 1))])


def norm_key(safety: str, counseling: str, original: str) -> tuple[str, str, str]:
    return (safety.strip(), counseling.strip(), original.strip())


def map_short_to_si_tr(s: str) -> str:
    s = s.strip().lower()
    if s == "keep":
        return "KEPT"
    if s == "remove":
        return "REMOVED"
    if s == "change":
        return "KEPT_with_changes"
    raise ValueError(f"Unknown P2 short label: {s!r}")


def map_short_to_te(s: str) -> str:
    s = s.strip().lower()
    if s == "keep":
        return "KEPT_exact_match"
    if s == "remove":
        return "REMOVED"
    if s == "change":
        return "KEPT_with_changes"
    raise ValueError(f"Unknown P2 short label: {s!r}")


def load_si_revision(path: Path) -> dict[tuple[str, str, str], str]:
    out: dict[tuple[str, str, str], str] = {}
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) < 4:
                continue
            raw = row[-1].strip().lower()
            if raw not in ("keep", "remove", "change"):
                continue
            out[norm_key(row[0], row[1], row[2])] = map_short_to_si_tr(raw)
    return out


def load_tr_revision(path: Path) -> dict[tuple[str, str, str], str]:
    return load_si_revision(path)  # same schema


def load_te_revision(path: Path) -> dict[str, str]:
    """Example_ID -> canonical P2 (one rating per conversation)."""
    out: dict[str, str] = {}
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) < 2:
                continue
            ex = row[1].strip()
            raw = row[-1].strip().lower()
            if raw not in ("keep", "remove", "change"):
                continue
            out[ex] = map_short_to_te(raw)
    return out


def is_p2_missing(val: str | None) -> bool:
    if val is None:
        return True
    s = str(val).strip()
    return s in ("", "NA", "N/A", "nan")


def merge_si_tr(
    intermediate_rows: list[dict[str, str]],
    rev: dict[tuple[str, str, str], str],
) -> tuple[list[dict[str, str]], dict[str, int]]:
    stats = {"n_rows": 0, "n_from_revision": 0, "n_keep_original": 0, "n_missing_after": 0}
    out: list[dict[str, str]] = []
    for row in intermediate_rows:
        stats["n_rows"] += 1
        key = norm_key(row["Safety type"], row["Counseling Request"], row["original_statement"])
        p2_orig = row.get("Psychiatrist_02", "")
        merged = dict(row)
        if key in rev:
            merged["Psychiatrist_02"] = rev[key]
            merged["Psychiatrist_02_source"] = "revision_posthoc"
            stats["n_from_revision"] += 1
        else:
            merged["Psychiatrist_02_source"] = "original"
            stats["n_keep_original"] += 1
        if is_p2_missing(merged.get("Psychiatrist_02")):
            stats["n_missing_after"] += 1
        out.append(merged)
    return out, stats


def merge_te(
    conv_rows: list[dict[str, str]],
    rev: dict[str, str],
) -> tuple[list[dict[str, str]], dict[str, int]]:
    stats = {"n_rows": 0, "n_from_revision": 0, "n_keep_original": 0, "n_missing_after": 0}
    out: list[dict[str, str]] = []
    for row in conv_rows:
        stats["n_rows"] += 1
        ex = (row.get("Example_ID") or "").strip()
        merged = dict(row)
        if ex in rev:
            merged["Psychiatrist_02"] = rev[ex]
            merged["Psychiatrist_02_source"] = "revision_posthoc"
            stats["n_from_revision"] += 1
        else:
            merged["Psychiatrist_02_source"] = "original"
            stats["n_keep_original"] += 1
        if is_p2_missing(merged.get("Psychiatrist_02")):
            stats["n_missing_after"] += 1
        out.append(merged)
    return out, stats


# --- kappa: "as-is OK" vs "not as-is" (change or remove) ---


def r1_as_is_ok(row: dict[str, str]) -> bool:
    """True = P1 kept model wording unchanged (good as-is)."""
    return row.get("Psychiatrist_01") == "KEPT_exact_match"


def r2_as_is_ok(row: dict[str, str], *, engagement: bool) -> bool:
    """True = P2 would keep as-is; False = change or remove."""
    v = (row.get("Psychiatrist_02") or "").strip()
    if engagement:
        return v == "KEPT_exact_match"
    return v == "KEPT"


def kappa_as_is_agreement(rows: list[dict[str, str]], *, engagement: bool) -> tuple[float, float, float]:
    r1 = [r1_as_is_ok(r) for r in rows]
    r2 = [r2_as_is_ok(r, engagement=engagement) for r in rows]
    k = cohen_kappa_binary(r1, r2)
    lo, hi = bootstrap_kappa(r1, r2)
    return (k, lo, hi)


def main() -> None:
    MERGED_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    validation_rows: list[dict[str, str | int]] = []

    # --- SI ---
    si_path = INTERMEDIATE / "SI_psychiatrist_01_and_02_scores.csv"
    si_rev = load_si_revision(REVIEW / "SI_revisions_psychiatrist02.csv")
    with si_path.open(newline="", encoding="utf-8") as f:
        si_rows = list(csv.DictReader(f))
    si_merged, si_stats = merge_si_tr(si_rows, si_rev)
    validation_rows.append({"dataset": "SI", **{k: str(v) for k, v in si_stats.items()}})
    fieldnames_si = list(si_merged[0].keys())
    with (MERGED_DIR / "SI_psychiatrist_01_and_02_scores_merged.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames_si)
        w.writeheader()
        w.writerows(si_merged)

    # --- Therapy request ---
    tr_path = INTERMEDIATE / "therapy_request_psychiatrist_01_and_02_scores.csv"
    tr_rev = load_tr_revision(REVIEW / "therapy_request_psychiatrist02.csv")
    with tr_path.open(newline="", encoding="utf-8") as f:
        tr_rows = list(csv.DictReader(f))
    tr_merged, tr_stats = merge_si_tr(tr_rows, tr_rev)
    validation_rows.append({"dataset": "Therapy request", **{k: str(v) for k, v in tr_stats.items()}})
    fieldnames_tr = list(tr_merged[0].keys())
    with (MERGED_DIR / "therapy_request_psychiatrist_01_and_02_scores_merged.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames_tr)
        w.writeheader()
        w.writerows(tr_merged)

    # --- Therapy engagement (conversation-level) ---
    te_path = INTERMEDIATE / "therapy_engagement_psychiatrist_01_and_02_scores.csv"
    te_rev = load_te_revision(REVIEW / "therapy_engagement_conversations_revision_psychiatrist02.csv")
    with te_path.open(newline="", encoding="utf-8") as f:
        te_rows_full = list(csv.DictReader(f))
    te_conv = dedupe_by_conversation(te_rows_full)
    te_merged, te_stats = merge_te(te_conv, te_rev)
    validation_rows.append({"dataset": "Therapy engagement (conversations)", **{k: str(v) for k, v in te_stats.items()}})
    fieldnames_te = list(te_merged[0].keys())
    with (MERGED_DIR / "therapy_engagement_psychiatrist_01_and_02_scores_merged.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames_te)
        w.writeheader()
        w.writerows(te_merged)

    with (RESULTS_DIR / "posthoc_merge_validation.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(validation_rows[0].keys()))
        w.writeheader()
        w.writerows(validation_rows)

    # --- Kappa results ---
    kappa_rows: list[dict[str, str | float]] = []
    specs = [
        ("Suicidal ideation (SI)", si_merged, False),
        ("Therapy request", tr_merged, False),
        ("Therapy engagement", te_merged, True),
    ]
    desc = (
        "Binary per rater: as-is OK (keep) vs not as-is (change OR remove). "
        "P1 as-is=KEPT_exact_match; not as-is=KEPT_with_changes|REMOVED. "
        "P2 as-is=KEPT (SI/TR) or KEPT_exact_match (TE); not as-is=KEPT_with_changes|REMOVED."
    )
    for label, rows, engagement in specs:
        kv, klo, khi = kappa_as_is_agreement(rows, engagement=engagement)
        n = len(rows)
        kappa_rows.append(
            {
                "dataset": label,
                "n_units": n,
                "analysis_unit": "statement" if not engagement else "conversation",
                "metric": "as_is_agreement",
                "description": desc,
                "cohens_kappa": round(kv, 6),
                "ci95_lower": round(klo, 6),
                "ci95_upper": round(khi, 6),
                "bootstrap_reps": BOOTSTRAP_REPS,
                "bootstrap_seed": BOOTSTRAP_SEED,
            }
        )

    with (RESULTS_DIR / "posthoc_kappa_merged.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(kappa_rows[0].keys()))
        w.writeheader()
        w.writerows(kappa_rows)

    print(f"Wrote merged tables under {MERGED_DIR.relative_to(REPO_ROOT)}")
    print(f"Wrote {RESULTS_DIR.relative_to(REPO_ROOT)}/posthoc_merge_validation.csv")
    print(f"Wrote {RESULTS_DIR.relative_to(REPO_ROOT)}/posthoc_kappa_merged.csv")


if __name__ == "__main__":
    main()
