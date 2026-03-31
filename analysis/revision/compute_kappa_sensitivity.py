#!/usr/bin/env python3
"""
Cohen's kappa sensitivity bounds for missing Psychiatrist_2 ratings.

Harmonizes P1 and P2 to a binary **keep** vs **remove** decision, then:
  - **complete_cases**: kappa on rows where P2 is observed (not NA).
  - **worst_case**: all rows; missing P2 imputed to **disagree** with P1 on binary keep/remove.
  - **best_case**: all rows; missing P2 imputed to **agree** with P1 on binary keep/remove.

Therapy engagement rows in the CSV are turns; review is per **conversation** — the script
dedupes by `Example_ID` before computing κ. Therapy engagement has no missing P2 in the
current files; worst and best match the full-sample kappa.

Usage (from repository root):
    python analysis/revision/compute_kappa_sensitivity.py
"""

from __future__ import annotations

import csv
import importlib.util
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
DEFAULT_OUT = REPO_ROOT / "results" / "revision_experiments" / "kappa_sensitivity_binary_keep_remove.csv"


def is_p2_missing(val: str | None) -> bool:
    if val is None:
        return True
    s = str(val).strip()
    return s in ("", "NA", "N/A", "nan")


def p1_keep_remove(row: dict[str, str]) -> bool:
    """True = keep (any form), False = removed."""
    v = row.get("Psychiatrist_01", "")
    if v in ("KEPT_exact_match", "KEPT_with_changes"):
        return True
    if v == "REMOVED":
        return False
    raise ValueError(f"Unknown Psychiatrist_01: {v!r}")


def p2_keep_remove_observed(row: dict[str, str], *, engagement: bool) -> bool | None:
    """None if P2 not yet rated."""
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
        if v in ("KEPT_exact_match", "KEPT_with_changes"):
            return True
        if v == "REMOVED":
            return False
    raise ValueError(f"Unknown Psychiatrist_02: {v!r}")


def cohen_kappa_binary(r1: list[bool], r2: list[bool]) -> float:
    """Cohen's kappa for two raters on binary labels (True=keep, False=remove)."""
    n = len(r1)
    if n == 0:
        return float("nan")
    if len(r2) != n:
        raise ValueError("Length mismatch")
    p_o = sum(1 for a, b in zip(r1, r2) if a == b) / n
    p1_keep = sum(r1) / n
    p2_keep = sum(r2) / n
    p_e = p1_keep * p2_keep + (1 - p1_keep) * (1 - p2_keep)
    if abs(1.0 - p_e) < 1e-15:
        return 1.0 if abs(1.0 - p_o) < 1e-15 else 0.0
    return (p_o - p_e) / (1.0 - p_e)


def run_dataset(
    rows: list[dict[str, str]],
    *,
    engagement: bool,
) -> tuple[dict[str, float | int | str], ...]:
    """Returns dicts for complete_cases, worst_case, best_case rows."""
    p1 = [p1_keep_remove(r) for r in rows]

    p2_obs = [p2_keep_remove_observed(r, engagement=engagement) for r in rows]
    n_total = len(rows)
    n_missing = sum(1 for x in p2_obs if x is None)

    # Complete-case kappa (only rows where P2 is observed)
    idx_cc = [i for i, x in enumerate(p2_obs) if x is not None]
    if idx_cc:
        p1_cc = [p1[i] for i in idx_cc]
        p2_cc = [p2_obs[i] for i in idx_cc]  # type: ignore[misc]
        k_cc = cohen_kappa_binary(p1_cc, p2_cc)
        p1_binary_varies = len(set(p1_cc)) > 1
    else:
        k_cc = float("nan")
        p1_binary_varies = False

    # Worst / best imputation for missing P2
    p2_worst: list[bool] = []
    p2_best: list[bool] = []
    for i in range(n_total):
        if p2_obs[i] is not None:
            v = p2_obs[i]
            assert v is not None
            p2_worst.append(v)
            p2_best.append(v)
        else:
            p2_worst.append(not p1[i])  # disagree on keep/remove
            p2_best.append(p1[i])  # agree

    k_worst = cohen_kappa_binary(p1, p2_worst)
    k_best = cohen_kappa_binary(p1, p2_best)

    base = {
        "harmonization": "binary keep vs remove: P1 keep = KEPT_exact_match|KEPT_with_changes; "
        "P1 remove = REMOVED. P2 keep/remove mapped from task-specific labels (see ANALYSIS_SUMMARY.md).",
        "n_rows_total": n_total,
        "n_p2_missing": n_missing,
        "n_complete_pairs": n_total - n_missing,
        "complete_cases_p1_binary_varies": bool(p1_binary_varies) if idx_cc else False,
    }

    cc_note = ""
    if idx_cc and not p1_binary_varies:
        cc_note = (
            "Degenerate: on rows with observed P2, P1 is always 'keep' "
            "(P1=REMOVED rows have P2=NA). Cohen's kappa is 0 by construction."
        )

    return (
        {
            **base,
            "scenario": "complete_cases_only",
            "cohens_kappa": round(k_cc, 6),
            "notes": cc_note,
        },
        {
            **base,
            "scenario": "worst_case_imputation",
            "cohens_kappa": round(k_worst, 6),
            "notes": "Missing P2 imputed to disagree with P1 on binary keep/remove.",
        },
        {
            **base,
            "scenario": "best_case_imputation",
            "cohens_kappa": round(k_best, 6),
            "notes": "Missing P2 imputed to agree with P1 on binary keep/remove.",
        },
    )


def main() -> None:
    datasets: list[tuple[str, str, bool]] = [
        ("Suicidal ideation (SI)", "SI_psychiatrist_01_and_02_scores.csv", False),
        ("Therapy request", "therapy_request_psychiatrist_01_and_02_scores.csv", False),
        ("Therapy engagement", "therapy_engagement_psychiatrist_01_and_02_scores.csv", True),
    ]

    out_rows: list[dict[str, str | int | float]] = []

    for label, fname, engagement in datasets:
        path = INTERMEDIATE / fname
        with path.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        if engagement:
            rows = dedupe_by_conversation(rows)
        for block in run_dataset(rows, engagement=engagement):
            out_rows.append(
                {
                    "dataset": label,
                    "source_file": fname,
                    **block,
                }
            )

    DEFAULT_OUT.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "dataset",
        "source_file",
        "harmonization",
        "n_rows_total",
        "n_p2_missing",
        "n_complete_pairs",
        "complete_cases_p1_binary_varies",
        "scenario",
        "cohens_kappa",
        "notes",
    ]
    with DEFAULT_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    print(f"Wrote {DEFAULT_OUT.relative_to(REPO_ROOT)} ({len(out_rows)} rows)")


if __name__ == "__main__":
    main()
