#!/usr/bin/env python3
"""
Compute P2 agreement (with 95% Wilson CIs) conditional on P1 == KEPT_exact_match.

Reads dual-psychiatrist score CSVs from data/inputs/intermediate_files/ and writes
a summary table to results/revision_experiments/p2_agreement_given_p1_exact_match.csv

Therapy engagement: one row per conversation (Example_ID); labels repeat per turn in the CSV.

Usage (from repository root):
    python analysis/revision/compute_p2_agreement.py
"""

from __future__ import annotations

import csv
import importlib.util
import math
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
DEFAULT_OUT = REPO_ROOT / "results" / "revision_experiments" / "interrater_reliability" / "p2_agreement_given_p1_exact_match.csv"


def wilson_ci(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion."""
    if n == 0:
        return (float("nan"), float("nan"))
    p = successes / n
    z2 = z * z
    denom = 1 + z2 / n
    center = (p + z2 / (2 * n)) / denom
    margin = (z / denom) * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n))
    return (max(0.0, center - margin), min(1.0, center + margin))


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    rows_out: list[dict[str, str | int | float]] = []

    # SI & therapy request: P2 positive == KEPT
    for dataset, fname in [
        ("Suicidal ideation (SI)", "SI_psychiatrist_01_and_02_scores.csv"),
        ("Therapy request", "therapy_request_psychiatrist_01_and_02_scores.csv"),
    ]:
        path = INTERMEDIATE / fname
        rows = load_rows(path)
        sub = [r for r in rows if r.get("Psychiatrist_01") == "KEPT_exact_match"]
        n = len(sub)
        agree = sum(1 for r in sub if r.get("Psychiatrist_02") == "KEPT")
        lo, hi = wilson_ci(agree, n)
        rows_out.append(
            {
                "dataset": dataset,
                "subset": "Psychiatrist_01 == KEPT_exact_match",
                "n": n,
                "definition_positive_P2": "Psychiatrist_02 == KEPT",
                "n_positive": agree,
                "proportion": round(agree / n, 6) if n else 0.0,
                "ci95_lower": round(lo, 6),
                "ci95_upper": round(hi, 6),
                "method": "Wilson score interval, z=1.96",
            }
        )

    # Therapy engagement: conversation-level (not turn-level)
    path = INTERMEDIATE / "therapy_engagement_psychiatrist_01_and_02_scores.csv"
    rows = dedupe_by_conversation(load_rows(path))
    sub = [r for r in rows if r.get("Psychiatrist_01") == "KEPT_exact_match"]
    n = len(sub)

    # Stringent criterion only: P2 == KEPT_exact_match, parallel to SI/TR
    agree = sum(1 for r in sub if r.get("Psychiatrist_02") == "KEPT_exact_match")
    lo, hi = wilson_ci(agree, n)
    rows_out.append(
        {
            "dataset": "Therapy engagement",
            "subset": "Psychiatrist_01 == KEPT_exact_match; analysis unit = conversation (deduped by Example_ID)",
            "n": n,
            "definition_positive_P2": "Psychiatrist_02 == KEPT_exact_match",
            "n_positive": agree,
            "proportion": round(agree / n, 6) if n else 0.0,
            "ci95_lower": round(lo, 6),
            "ci95_upper": round(hi, 6),
            "method": "Wilson score interval, z=1.96",
        }
    )

    DEFAULT_OUT.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows_out[0].keys())
    with DEFAULT_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_out)

    print(f"Wrote {DEFAULT_OUT.relative_to(REPO_ROOT)} ({len(rows_out)} rows)")


if __name__ == "__main__":
    main()
