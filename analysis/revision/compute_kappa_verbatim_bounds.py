#!/usr/bin/env python3
"""
Cohen's kappa — optimistic vs pessimistic bounds for "parallel verbatim evaluation".

**Scale:** Both psychiatrists coded as endorsing (or not) the **model text verbatim**.

- R1 = True iff Psychiatrist_01 == KEPT_exact_match, else False.

**P2 "kept without changes" (verbatim OK):**
  - SI & therapy request: Psychiatrist_02 == KEPT (only non-NA labels are KEPT / REMOVED).
  - Therapy engagement: Psychiatrist_02 == KEPT_exact_match.

**Optimistic (best-case κ):**
  - P1 == KEPT_exact_match: compare to P2; concord if P2 is verbatim OK; discord otherwise.
    Missing P2 → impute verbatim OK (concord).
  - P1 in {REMOVED, KEPT_with_changes}: **automatic concordance** — impute R2 = R1 (both False).

**Pessimistic (worst-case κ):**
  - P1 == KEPT_exact_match: concord only if P2 verbatim OK; missing P2 → impute not OK (discord).
  - P1 in {REMOVED, KEPT_with_changes}: **automatic discord** — impute R2 = not R1 (R1 False → R2 True).

Then Cohen's κ is computed on the paired binary vectors (R1, R2) over all rows.

**Complete cases:** Rows where P2 is not NA — same verbatim R1/R2 from observed data only (no imputation, no auto win/lose rules).

**Therapy engagement:** spreadsheet rows are turns; review is per **conversation** — dedupe by `Example_ID` before any count (labels are constant across turns).

Outputs:

- `results/revision_experiments/kappa_verbatim_optimistic_pessimistic.csv`
- `results/revision_experiments/kappa_verbatim_complete_cases.csv`

Usage (from repository root):
    python analysis/revision/compute_kappa_verbatim_bounds.py
"""

from __future__ import annotations

import csv
import importlib.util
import math
import random
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
_te_mod = importlib.util.spec_from_file_location(
    "therapy_engagement_conversations",
    Path(__file__).resolve().parent / "therapy_engagement_conversations.py",
)
_te = importlib.util.module_from_spec(_te_mod)
assert _te_mod.loader is not None
_te_mod.loader.exec_module(_te)
dedupe_by_conversation = _te.dedupe_by_conversation
INTERMEDIATE = REPO_ROOT / "data" / "inputs" / "intermediate_files"
DEFAULT_OUT = REPO_ROOT / "results" / "revision_experiments" / "kappa_verbatim_optimistic_pessimistic.csv"
COMPLETE_OUT = REPO_ROOT / "results" / "revision_experiments" / "kappa_verbatim_complete_cases.csv"
BOOTSTRAP_REPS = 5000
BOOTSTRAP_SEED = 42


def is_p2_missing(val: str | None) -> bool:
    if val is None:
        return True
    s = str(val).strip()
    return s in ("", "NA", "N/A", "nan")


def r1_verbatim_ok(row: dict[str, str]) -> bool:
    return row.get("Psychiatrist_01") == "KEPT_exact_match"


def p2_verbatim_ok_observed(row: dict[str, str], *, engagement: bool) -> bool | None:
    """Whether P2 endorsed verbatim; None if P2 not rated."""
    v = row.get("Psychiatrist_02")
    if is_p2_missing(v):
        return None
    v = str(v).strip()
    if not engagement:
        if v == "KEPT":
            return True
        if v == "REMOVED":
            return False
    else:
        if v == "KEPT_exact_match":
            return True
        if v in ("KEPT_with_changes", "REMOVED"):
            return False
    raise ValueError(f"Unknown Psychiatrist_02: {v!r}")


def r2_optimistic(row: dict[str, str], *, engagement: bool) -> bool:
    p1 = row.get("Psychiatrist_01")
    r1 = p1 == "KEPT_exact_match"
    if p1 in ("REMOVED", "KEPT_with_changes"):
        return r1  # False — forced agreement with R1 (auto win)
    if p1 == "KEPT_exact_match":
        obs = p2_verbatim_ok_observed(row, engagement=engagement)
        if obs is None:
            return True  # missing P2: assume verbatim OK
        return obs
    raise ValueError(f"Unknown Psychiatrist_01: {p1!r}")


def r2_pessimistic(row: dict[str, str], *, engagement: bool) -> bool:
    p1 = row.get("Psychiatrist_01")
    r1 = p1 == "KEPT_exact_match"
    if p1 in ("REMOVED", "KEPT_with_changes"):
        return not r1  # True — forced disagreement (auto lose)
    if p1 == "KEPT_exact_match":
        obs = p2_verbatim_ok_observed(row, engagement=engagement)
        if obs is None:
            return False  # missing P2: assume not verbatim OK
        return obs
    raise ValueError(f"Unknown Psychiatrist_01: {p1!r}")


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


def bootstrap_kappa_ci(
    rows: list[dict[str, str]],
    *,
    engagement: bool,
    r2_fn,
    n_boot: int = BOOTSTRAP_REPS,
    seed: int = BOOTSTRAP_SEED,
) -> tuple[float, float]:
    """Percentile 95% CI from row resampling with replacement (same construction rules each draw)."""
    rng = random.Random(seed)
    n = len(rows)
    if n < 2:
        return (float("nan"), float("nan"))
    vals: list[float] = []
    for _ in range(n_boot):
        sample = [rows[rng.randrange(n)] for _ in range(n)]
        r1 = [r1_verbatim_ok(r) for r in sample]
        r2 = [r2_fn(r, engagement=engagement) for r in sample]
        k = cohen_kappa_binary(r1, r2)
        if not math.isnan(k):
            vals.append(k)
    if len(vals) < 50:
        return (float("nan"), float("nan"))
    vals.sort()
    lo = vals[int(0.025 * (len(vals) - 1))]
    hi = vals[int(0.975 * (len(vals) - 1))]
    return (lo, hi)


def bootstrap_kappa_complete_cases_only(
    cc_rows: list[dict[str, str]],
    *,
    engagement: bool,
    n_boot: int = BOOTSTRAP_REPS,
    seed: int = BOOTSTRAP_SEED,
) -> tuple[float, float]:
    """Bootstrap CI when only rows with observed P2 are used."""
    rng = random.Random(seed)
    n = len(cc_rows)
    if n < 2:
        return (float("nan"), float("nan"))
    vals: list[float] = []
    for _ in range(n_boot):
        sample = [cc_rows[rng.randrange(n)] for _ in range(n)]
        r1 = [r1_verbatim_ok(r) for r in sample]
        r2: list[bool] = []
        for r in sample:
            v = p2_verbatim_ok_observed(r, engagement=engagement)
            assert v is not None
            r2.append(v)
        k = cohen_kappa_binary(r1, r2)
        if not math.isnan(k):
            vals.append(k)
    if len(vals) < 50:
        return (float("nan"), float("nan"))
    vals.sort()
    lo = vals[int(0.025 * (len(vals) - 1))]
    hi = vals[int(0.975 * (len(vals) - 1))]
    return (lo, hi)


def run_complete_cases(rows: list[dict[str, str]], *, engagement: bool) -> dict[str, object]:
    """Verbatim κ on rows where Psychiatrist_02 is present (not NA)."""
    cc = [r for r in rows if not is_p2_missing(r.get("Psychiatrist_02"))]
    n_all = len(rows)
    r1 = [r1_verbatim_ok(r) for r in cc]
    r2: list[bool] = []
    for r in cc:
        v = p2_verbatim_ok_observed(r, engagement=engagement)
        if v is None:
            raise RuntimeError("complete-case row unexpectedly missing P2")
        r2.append(v)
    k = cohen_kappa_binary(r1, r2)
    lo, hi = bootstrap_kappa_complete_cases_only(cc, engagement=engagement)
    ci_note = (
        f"Bootstrap percentile on row resampling, n={BOOTSTRAP_REPS}, seed={BOOTSTRAP_SEED}. "
        "Quantifies resampling uncertainty of κ given fixed rules; not a population CI unless rows are i.i.d. samples."
    )
    r1_varies = len(set(r1)) > 1
    r2_varies = len(set(r2)) > 1
    note = ""
    if not r1_varies or not r2_varies:
        note = "Degenerate: R1 or R2 has no variance on this subset; κ is not informative."
    return {
        "scale": "R1=R2=True iff psychiatrist endorses model text verbatim (task-specific P2 mapping).",
        "n_rows_in_file": n_all,
        "n_complete_pairs": len(cc),
        "n_excluded_missing_p2": n_all - len(cc),
        "n_p1_verbatim_ok_in_complete": sum(1 for x in r1 if x),
        "r1_binary_varies": r1_varies,
        "r2_binary_varies": r2_varies,
        "cohens_kappa": round(k, 6),
        "ci95_lower": round(lo, 6),
        "ci95_upper": round(hi, 6),
        "ci_method": ci_note,
        "notes": note,
    }


def run_dataset(rows: list[dict[str, str]], *, engagement: bool) -> tuple[dict[str, object], dict[str, object]]:
    r1 = [r1_verbatim_ok(r) for r in rows]
    r2_opt = [r2_optimistic(r, engagement=engagement) for r in rows]
    r2_pes = [r2_pessimistic(r, engagement=engagement) for r in rows]

    n = len(rows)
    n_exact = sum(1 for x in r1 if x)
    n_miss_on_exact = sum(
        1
        for r in rows
        if r.get("Psychiatrist_01") == "KEPT_exact_match" and p2_verbatim_ok_observed(r, engagement=engagement) is None
    )

    k_opt = cohen_kappa_binary(r1, r2_opt)
    k_pes = cohen_kappa_binary(r1, r2_pes)

    ci_opt_lo, ci_opt_hi = bootstrap_kappa_ci(rows, engagement=engagement, r2_fn=r2_optimistic)
    ci_pes_lo, ci_pes_hi = bootstrap_kappa_ci(rows, engagement=engagement, r2_fn=r2_pessimistic)

    ci_note = (
        f"Bootstrap percentile on row resampling, n={BOOTSTRAP_REPS}, seed={BOOTSTRAP_SEED}. "
        "Quantifies resampling uncertainty of κ given fixed rules; not a population CI unless rows are i.i.d. samples."
    )

    base = {
        "scale": "R1=R2=True iff psychiatrist endorses model text verbatim (task-specific P2 mapping).",
        "n_rows": n,
        "n_p1_verbatim_ok": n_exact,
        "n_p2_missing_where_p1_verbatim": n_miss_on_exact,
        "ci_method": ci_note,
    }

    return (
        {
            **base,
            "scenario": "optimistic",
            "cohens_kappa": round(k_opt, 6),
            "ci95_lower": round(ci_opt_lo, 6),
            "ci95_upper": round(ci_opt_hi, 6),
        },
        {
            **base,
            "scenario": "pessimistic",
            "cohens_kappa": round(k_pes, 6),
            "ci95_lower": round(ci_pes_lo, 6),
            "ci95_upper": round(ci_pes_hi, 6),
        },
    )


def main() -> None:
    datasets: list[tuple[str, str, bool]] = [
        ("Suicidal ideation (SI)", "SI_psychiatrist_01_and_02_scores.csv", False),
        ("Therapy request", "therapy_request_psychiatrist_01_and_02_scores.csv", False),
        ("Therapy engagement", "therapy_engagement_psychiatrist_01_and_02_scores.csv", True),
    ]

    out_rows: list[dict[str, str | int | float]] = []
    complete_rows: list[dict[str, str | int | float]] = []

    for label, fname, engagement in datasets:
        path = INTERMEDIATE / fname
        with path.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        if engagement:
            rows = dedupe_by_conversation(rows)
        for block in run_dataset(rows, engagement=engagement):
            out_rows.append({"dataset": label, "source_file": fname, **block})
        complete_rows.append({"dataset": label, "source_file": fname, **run_complete_cases(rows, engagement=engagement)})

    DEFAULT_OUT.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "dataset",
        "source_file",
        "scale",
        "n_rows",
        "n_p1_verbatim_ok",
        "n_p2_missing_where_p1_verbatim",
        "scenario",
        "cohens_kappa",
        "ci95_lower",
        "ci95_upper",
        "ci_method",
    ]
    with DEFAULT_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    cc_fields = [
        "dataset",
        "source_file",
        "scale",
        "n_rows_in_file",
        "n_complete_pairs",
        "n_excluded_missing_p2",
        "n_p1_verbatim_ok_in_complete",
        "r1_binary_varies",
        "r2_binary_varies",
        "cohens_kappa",
        "ci95_lower",
        "ci95_upper",
        "ci_method",
        "notes",
    ]
    with COMPLETE_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cc_fields)
        w.writeheader()
        w.writerows(complete_rows)

    print(f"Wrote {DEFAULT_OUT.relative_to(REPO_ROOT)} ({len(out_rows)} rows)")
    print(f"Wrote {COMPLETE_OUT.relative_to(REPO_ROOT)} ({len(complete_rows)} rows)")


if __name__ == "__main__":
    main()
