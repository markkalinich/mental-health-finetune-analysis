#!/usr/bin/env python3
"""
Rank fine-tuned models by mean ΔF1 and assign top/bottom 20% groups.

Produces per-class CSVs (Mental Health, Medical) with:
  - rank, group (Top 20% / Middle 60% / Bottom 20%)
  - lm_studio_id, Parameters (Bn), mean_base_f1, mean_ft_f1, mean_delta_f1
  - Fine-tune metadata from revised Table S2

Also prints summary statistics used in the reviewer response (mean base F1
and mean FT F1 for top/bottom groups).

Inputs:
  config/models_config.csv
  data/inputs/model_results/all_models_all_tasks.csv
  results/revision_experiments/fine_tune_subset_analysis/revised_table_s2.csv

Outputs:
  results/revision_experiments/fine_tune_subset_analysis/mental_health_ranked_models.csv
  results/revision_experiments/fine_tune_subset_analysis/medical_ranked_models.csv
"""

import math
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent.parent

CONFIG_PATH = ROOT / "config" / "models_config.csv"
RESULTS_PATH = ROOT / "data" / "inputs" / "model_results" / "all_models_all_tasks.csv"
TABLE_S2_PATH = ROOT / "results" / "revision_experiments" / "fine_tune_subset_analysis" / "revised_table_s2.csv"
OUTPUT_DIR = ROOT / "results" / "revision_experiments" / "fine_tune_subset_analysis"

FINETUNE_CLASSES = {
    "Mental Health": ["Mental Health"],
    "Medical": ["Medical", "MedGemma"],
}

TASKS = ["suicidal_ideation", "therapy_request", "therapy_engagement"]


def load_f1_by_lm_studio_id(cfg: pd.DataFrame, results: pd.DataFrame) -> pd.DataFrame:
    """Map (family, size) → lm_studio_id, then pivot F1 by task."""
    key_to_id = cfg.set_index(["family", "size"])["lm_studio_id"].to_dict()
    results = results.copy()
    results["lm_studio_id"] = results.apply(
        lambda r: key_to_id.get((r["model_family"], r["model_size"])), axis=1,
    )
    results = results.dropna(subset=["lm_studio_id"])
    pivot = results.pivot_table(
        index="lm_studio_id", columns="task", values="f1_score", aggfunc="first",
    )
    return pivot


def compute_ranked_table(
    ft_class_name: str,
    model_type_values: list,
    cfg: pd.DataFrame,
    f1_pivot: pd.DataFrame,
    table_s2: pd.DataFrame,
) -> pd.DataFrame:
    ft_models = cfg[cfg["model_type"].isin(model_type_values)].copy()
    ft_models = ft_models.dropna(subset=["Base_Model_LM_Studio_ID"])

    rows = []
    for _, m in ft_models.iterrows():
        ft_id = m["lm_studio_id"]
        base_id = m["Base_Model_LM_Studio_ID"]

        if ft_id not in f1_pivot.index or base_id not in f1_pivot.index:
            continue

        ft_f1s, base_f1s = [], []
        for task in TASKS:
            if task in f1_pivot.columns:
                ft_val = f1_pivot.loc[ft_id, task]
                base_val = f1_pivot.loc[base_id, task]
                if pd.notna(ft_val) and pd.notna(base_val):
                    ft_f1s.append(ft_val)
                    base_f1s.append(base_val)

        if not ft_f1s:
            continue

        rows.append({
            "lm_studio_id": ft_id,
            "Parameters (Bn)": m["param_billions"],
            "mean_base_f1": round(sum(base_f1s) / len(base_f1s), 4),
            "mean_ft_f1": round(sum(ft_f1s) / len(ft_f1s), 4),
            "mean_delta_f1": round(
                sum(f - b for f, b in zip(ft_f1s, base_f1s)) / len(ft_f1s), 4
            ),
            "Base Model Fine-Tune Type": m.get("Base_Model_Type", ""),
        })

    df = pd.DataFrame(rows).sort_values("mean_delta_f1", ascending=False).reset_index(drop=True)
    n = len(df)
    top_k = int(n * 0.2)
    bottom_k = int(n * 0.2)

    groups = []
    for i in range(n):
        if i < top_k:
            groups.append("Top 20%")
        elif i >= n - bottom_k:
            groups.append("Bottom 20%")
        else:
            groups.append("Middle 60%")
    df.insert(0, "group", groups)
    df.insert(0, "rank", range(1, n + 1))

    s2_cols = [
        "LM Studio ID", "Fine-Tune Method", "Data_Origin", "Data_Size_Reported",
        "Data_Size_Unit", "Data_Source_Platform", "Turn_Structure", "Is_MCQ",
        "Is_Preference_Pairs", "Is_Classification_Labels", "Has_Reasoning_Traces",
        "Content_Domain",
    ]
    existing_cols = [c for c in s2_cols if c in table_s2.columns]
    if existing_cols:
        s2_sub = table_s2[existing_cols].rename(columns={"LM Studio ID": "lm_studio_id"})
        df = df.merge(s2_sub, on="lm_studio_id", how="left")

    return df


def build_group_summary(df: pd.DataFrame, class_name: str) -> pd.DataFrame:
    """Build a summary DataFrame with group-level statistics."""
    summary_rows = []
    for grp in ["Top 20%", "Bottom 20%"]:
        sub = df[df["group"] == grp]
        if sub.empty:
            continue
        no_desc = sub["Data_Origin"].isna() | (sub["Data_Origin"] == "No FT data description available")
        base_type_counts = sub["Base Model Fine-Tune Type"].value_counts()
        n_pt = int(base_type_counts.get("PT", 0))
        n_it = int(base_type_counts.get("IT", 0))
        summary_rows.append({
            "fine_tune_class": class_name,
            "group": grp,
            "n": len(sub),
            "n_total": len(df),
            "n_pt_base": n_pt,
            "n_it_base": n_it,
            "mean_base_f1": round(sub["mean_base_f1"].mean(), 4),
            "base_f1_min": round(sub["mean_base_f1"].min(), 4),
            "base_f1_max": round(sub["mean_base_f1"].max(), 4),
            "mean_ft_f1": round(sub["mean_ft_f1"].mean(), 4),
            "ft_f1_min": round(sub["mean_ft_f1"].min(), 4),
            "ft_f1_max": round(sub["mean_ft_f1"].max(), 4),
            "mean_delta_f1": round(sub["mean_delta_f1"].mean(), 4),
            "missing_ft_data_description": int(no_desc.sum()),
        })

    # Add a row for the full class (all models)
    no_desc_all = df["Data_Origin"].isna() | (df["Data_Origin"] == "No FT data description available")
    all_base_counts = df["Base Model Fine-Tune Type"].value_counts()
    summary_rows.append({
        "fine_tune_class": class_name,
        "group": "All",
        "n": len(df),
        "n_total": len(df),
        "n_pt_base": int(all_base_counts.get("PT", 0)),
        "n_it_base": int(all_base_counts.get("IT", 0)),
        "mean_base_f1": round(df["mean_base_f1"].mean(), 4),
        "base_f1_min": round(df["mean_base_f1"].min(), 4),
        "base_f1_max": round(df["mean_base_f1"].max(), 4),
        "mean_ft_f1": round(df["mean_ft_f1"].mean(), 4),
        "ft_f1_min": round(df["mean_ft_f1"].min(), 4),
        "ft_f1_max": round(df["mean_ft_f1"].max(), 4),
        "mean_delta_f1": round(df["mean_delta_f1"].mean(), 4),
        "missing_ft_data_description": int(no_desc_all.sum()),
    })

    return pd.DataFrame(summary_rows)


def print_group_summary(df: pd.DataFrame, class_name: str) -> None:
    """Print summary statistics matching reviewer response claims."""
    print(f"\n{'='*70}")
    print(f"  {class_name} — {len(df)} paired models")
    print(f"{'='*70}")

    for grp in ["Top 20%", "Bottom 20%"]:
        sub = df[df["group"] == grp]
        if sub.empty:
            continue
        n = len(sub)
        mean_base = sub["mean_base_f1"].mean()
        mean_ft = sub["mean_ft_f1"].mean()
        mean_delta = sub["mean_delta_f1"].mean()
        base_range = f"{sub['mean_base_f1'].min():.2f}–{sub['mean_base_f1'].max():.2f}"
        ft_range = f"{sub['mean_ft_f1'].min():.2f}–{sub['mean_ft_f1'].max():.2f}"

        print(f"\n  {grp} (n={n}):")
        print(f"    Mean base F1:  {mean_base:.2f}  (range {base_range})")
        print(f"    Mean FT F1:    {mean_ft:.2f}  (range {ft_range})")
        print(f"    Mean ΔF1:      {mean_delta:+.4f}")

        no_desc = sub["Data_Origin"].isna() | (sub["Data_Origin"] == "No FT data description available")
        print(f"    Missing FT data description: {no_desc.sum()}/{n}")

    print()


def main() -> int:
    cfg = pd.read_csv(CONFIG_PATH)
    cfg = cfg[cfg["enabled"] == True]
    results = pd.read_csv(RESULTS_PATH)
    table_s2 = pd.read_csv(TABLE_S2_PATH)

    f1_pivot = load_f1_by_lm_studio_id(cfg, results)

    all_summaries = []

    for class_name, type_values in FINETUNE_CLASSES.items():
        df = compute_ranked_table(class_name, type_values, cfg, f1_pivot, table_s2)
        if df.empty:
            print(f"WARNING: No paired models found for {class_name}", file=sys.stderr)
            continue

        ranked_dir = OUTPUT_DIR / "supplemental_data"
        ranked_dir.mkdir(parents=True, exist_ok=True)
        out_path = ranked_dir / f"{class_name.lower().replace(' ', '_')}_ranked_models.csv"
        df.to_csv(out_path, index=False)
        print(f"Saved: {out_path}  ({len(df)} models)")

        all_summaries.append(build_group_summary(df, class_name))
        print_group_summary(df, class_name)

    if all_summaries:
        summary_df = pd.concat(all_summaries, ignore_index=True)
        summary_path = OUTPUT_DIR / "top_bottom_20pct_summary.csv"
        summary_df.to_csv(summary_path, index=False)
        print(f"Saved: {summary_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
