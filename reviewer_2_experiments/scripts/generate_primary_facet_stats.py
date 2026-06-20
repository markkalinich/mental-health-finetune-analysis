#!/usr/bin/env python3
"""Primary (N=127) Figure 3 paired-ΔF1 facet stats.

Produces the primary-cohort counterpart to the parse-filtered Figure S12 stats
(`results/parse50pct_per_task/figure_3/delta_f1_facet_plot_parse50pct_per_task_stats.csv`)
using the *identical* stats logic (`combined_finetune_facet_plot._generate_facet_grid`)
so the two CSVs are directly comparable cell-for-cell.

Cohort: canonical primary config (enabled==True) + primary results — the same
inputs `audit_all_claims.py` uses for its primary-side facet computation, which
asserts 9 Bonferroni-significant cells.

Usage:
  MPLBACKEND=Agg .venv/bin/python reviewer_2_experiments/scripts/generate_primary_facet_stats.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

import pandas as pd

from r2_paths import ROOT, RESULTS

PRIMARY_CONFIG = ROOT / "config" / "models_config.csv"
PRIMARY_RESULTS = ROOT / "data" / "inputs" / "model_results" / "all_models_all_tasks.csv"
OUT_DIR = RESULTS / "primary_n127" / "figure_3"


def main() -> int:
    if not PRIMARY_CONFIG.exists():
        print(f"Missing primary config: {PRIMARY_CONFIG}", file=sys.stderr)
        return 1
    if not PRIMARY_RESULTS.exists():
        print(f"Missing primary results: {PRIMARY_RESULTS}", file=sys.stderr)
        return 1

    sys.path.insert(0, str(ROOT))
    import analysis.combined_finetune_facet_plot as cffp

    def load_primary() -> tuple[pd.DataFrame, pd.DataFrame]:
        cfg = pd.read_csv(PRIMARY_CONFIG)
        cfg = cfg[cfg["enabled"] == True].copy()  # noqa: E712
        res = pd.read_csv(PRIMARY_RESULTS)
        return cfg, res

    cffp.load_data = load_primary

    all_data = {}
    for ft_config in cffp.FINETUNE_TYPES:
        config, results = load_primary()
        df = cffp.compute_deltas(config, results, ft_config["filter"], "f1_score", "f1")
        all_data[ft_config["name"]] = df
        print(f"{ft_config['label']}: {len(df)} data points")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    supp = OUT_DIR / "supplemental"
    supp.mkdir(parents=True, exist_ok=True)

    stats_csv = OUT_DIR / "delta_f1_facet_plot_primary_n127_stats.csv"
    data_csv = supp / "delta_f1_facet_plot_primary_n127_data.csv"
    main_png = OUT_DIR / "delta_f1_facet_plot_primary_n127.png"

    cffp._generate_facet_grid(
        all_data,
        delta_col="delta_f1",
        ft_col="ft_f1",
        base_col="base_f1",
        y_label="Δ F1 Score",
        stats_mean_key="mean_delta_f1",
        stats_std_key="std_delta_f1",
        stats_median_key="median_delta_f1",
        paired_test_description="fine-tune F1 vs base F1",
        out_png=main_png,
        out_csv=data_csv,
        out_stats=stats_csv,
    )

    stats = pd.read_csv(stats_csv)
    n_sig = int((stats["significant"] == True).sum())  # noqa: E712
    total_pairs = int(stats["n_pairs"].sum())
    print(f"\nPrimary N=127 facet cells: {len(stats)} rows, {total_pairs} pairs, {n_sig} Bonferroni-significant")
    sig = stats[stats["significant"] == True]  # noqa: E712
    for _, r in sig.iterrows():
        print(
            f"  SIG: {r['finetune_type']:<18} {r['task']:<20} {r['model_family']:<6} "
            f"n={int(r['n_pairs'])} mean ΔF1={r['mean_delta_f1']:+.4f} p_adj={r['p_adjusted']:.4g}"
        )
    if n_sig != 9:
        print(f"\nWARNING: expected 9 significant cells (audit invariant), got {n_sig}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
