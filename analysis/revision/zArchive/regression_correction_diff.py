"""
Compare original (pre-fix) and corrected (post-fix) Bonferroni-corrected
regression coefficients for the safety-model scoring bug correction note.

Reads two Bonferroni-corrected regression CSVs (original submission vs
corrected), filters to F1 Score DVs only, and produces one diff CSV per task
(SI, TR, TE) with columns: Variable, Original β, Corrected β, Δ, and
Significance Change.

Input:  data/revision_data/correction_note/regression_f1_bonferroni_ORIGINAL_20251231.csv
        data/revision_data/correction_note/regression_f1_bonferroni_CORRECTED_20260330.csv

Output: results/FINETUNE_PAPER_FIGURES/<run>/correction_note/
            table1_diff_SI_F1.csv
            table1_diff_TR_F1.csv
            table1_diff_TE_F1.csv
            table1_significance_changes_F1.csv
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

DATA_DIR = ROOT / "data" / "revision_data" / "correction_note"
ORIGINAL_CSV = DATA_DIR / "regression_f1_bonferroni_ORIGINAL_20251231.csv"
CORRECTED_CSV = DATA_DIR / "regression_f1_bonferroni_CORRECTED_20260330.csv"

TASKS = {
    "Suicidal Ideation": "SI",
    "Therapy Request": "TR",
    "Therapy Engagement": "TE",
}

BONF_SIG_THRESHOLDS = [
    (0.001, "***"),
    (0.01, "**"),
    (0.05, "*"),
]


def _sig_label(bonf_p: float | None) -> str:
    if bonf_p is None or pd.isna(bonf_p):
        return ""
    for threshold, label in BONF_SIG_THRESHOLDS:
        if bonf_p < threshold:
            return label
    return ""


def _significance_change(orig_sig: str, fix_sig: str) -> str:
    """Describe the direction of any significance change."""
    orig_is_sig = orig_sig != ""
    fix_is_sig = fix_sig != ""
    if orig_is_sig and not fix_is_sig:
        return f"{orig_sig} → NS"
    if not orig_is_sig and fix_is_sig:
        return f"NS → {fix_sig}"
    if orig_is_sig and fix_is_sig and orig_sig != fix_sig:
        return f"{orig_sig} → {fix_sig}"
    return ""


def load_f1_by_task(csv_path: Path) -> dict[str, pd.DataFrame]:
    """Load Bonferroni CSV and return {task_full_name: df} filtered to F1 Score."""
    df = pd.read_csv(csv_path)
    df = df[df["DV"] == "F1 Score"].copy()
    return {task: df[df["Task"] == task].copy() for task in TASKS}


def build_diff_table(orig_task_df: pd.DataFrame, fix_task_df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, orig_row in orig_task_df.iterrows():
        var = orig_row["Variable"]
        fix_matches = fix_task_df[fix_task_df["Variable"] == var]
        if fix_matches.empty:
            continue
        fix_row = fix_matches.iloc[0]

        orig_beta = orig_row["β"]
        fix_beta = fix_row["β"]
        delta = fix_beta - orig_beta

        orig_sig = _sig_label(orig_row["p (Bonferroni-corrected)"])
        fix_sig = _sig_label(fix_row["p (Bonferroni-corrected)"])
        sig_change = _significance_change(orig_sig, fix_sig)

        rows.append({
            "Variable": var,
            "Original β": round(orig_beta, 4),
            "Corrected β": round(fix_beta, 4),
            "Δ": round(delta, 4),
            "Original Sig": orig_sig,
            "Corrected Sig": fix_sig,
            "Significance Change": sig_change,
        })

    r2_orig = orig_task_df.iloc[0]["R²"] if len(orig_task_df) > 0 else None
    r2_fix = fix_task_df.iloc[0]["R²"] if len(fix_task_df) > 0 else None
    if r2_orig is not None and r2_fix is not None:
        rows.append({
            "Variable": "R²",
            "Original β": round(r2_orig, 4),
            "Corrected β": round(r2_fix, 4),
            "Δ": round(r2_fix - r2_orig, 4),
            "Original Sig": "",
            "Corrected Sig": "",
            "Significance Change": "",
        })

    return pd.DataFrame(rows)


def main(out_dir: Path | None = None) -> list[Path]:
    if not ORIGINAL_CSV.exists():
        sys.exit(f"Missing original CSV: {ORIGINAL_CSV}")
    if not CORRECTED_CSV.exists():
        sys.exit(f"Missing corrected CSV: {CORRECTED_CSV}")

    orig_by_task = load_f1_by_task(ORIGINAL_CSV)
    fix_by_task = load_f1_by_task(CORRECTED_CSV)

    if out_dir is None:
        results_root = ROOT / "results" / "FINETUNE_PAPER_FIGURES"
        runs = sorted(results_root.iterdir()) if results_root.exists() else []
        if runs:
            out_dir = runs[-1] / "correction_note"
        else:
            out_dir = results_root / "correction_note"

    out_dir.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []
    sig_change_rows: list[pd.DataFrame] = []

    for task_full, task_short in TASKS.items():
        diff = build_diff_table(orig_by_task[task_full], fix_by_task[task_full])
        out_path = out_dir / f"table1_diff_{task_short}_F1.csv"
        diff.to_csv(out_path, index=False)
        saved.append(out_path)
        print(f"Saved: {out_path}")

        n_sig_changes = (diff["Significance Change"] != "").sum()
        print(f"  {task_short} F1: {len(diff)} rows, {n_sig_changes} significance change(s)")

        changed = diff[diff["Significance Change"] != ""].copy()
        if not changed.empty:
            changed.insert(0, "Task", task_short)
            sig_change_rows.append(changed)

    if sig_change_rows:
        sig_df = pd.concat(sig_change_rows, ignore_index=True)
    else:
        sig_df = pd.DataFrame(columns=["Task", "Variable", "Original β", "Corrected β",
                                        "Δ", "Original Sig", "Corrected Sig",
                                        "Significance Change"])
    sig_path = out_dir / "table1_significance_changes_F1.csv"
    sig_df.to_csv(sig_path, index=False)
    saved.append(sig_path)
    print(f"\nSaved: {sig_path}  ({len(sig_df)} row(s) with significance changes)")

    return saved


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Diff original vs corrected Table 1 regressions")
    parser.add_argument("--out-dir", type=Path, default=None,
                        help="Output directory (default: latest results run / correction_note)")
    args = parser.parse_args()
    main(out_dir=args.out_dir)
