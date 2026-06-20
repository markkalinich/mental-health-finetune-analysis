#!/usr/bin/env python3
"""Parse-filter sensitivity outputs: Table S2, Figure S11, Figure S12.

Merged entry point for filter + Table 1 regression + Figure 2 + Figure 3.
Writes under results/parse{pct}pct_per_task/ (separate folder per cutoff).

Top-level deliverables only; intermediates go to supplemental_tables/ or supplemental/.

Usage:
  .venv/bin/python reviewer_2_experiments/scripts/run_parse_filtered_outputs.py --target all
  .venv/bin/python reviewer_2_experiments/scripts/run_parse_filtered_outputs.py --min-parse 0.50 --target all
  MPLBACKEND=Agg .venv/bin/python reviewer_2_experiments/scripts/run_parse_filtered_outputs.py --target figure3
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import pandas as pd

from filter_models_config_by_parse import artifact_tag
from r2_paths import ROOT, SCRIPTS, parse_run_dirs

FILTER_SCRIPT = SCRIPTS / "filter_models_config_by_parse.py"
FIG2_SCRIPT = ROOT / "analysis" / "comparative_analysis" / "compact_unified_facet_plot.py"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Parse-filtered Table 1 + Figures 2–3")
    p.add_argument("--min-parse", type=float, default=0.50)
    p.add_argument(
        "--tasks",
        nargs="+",
        choices=["all", "any", "per_task", "SI", "TR", "TE"],
        default=["per_task"],
    )
    p.add_argument(
        "--target",
        choices=["all", "filter", "table1", "figure2", "figure3"],
        default="all",
        help="Which outputs to run (default: all)",
    )
    return p.parse_args()


def run_filter(args: argparse.Namespace, tag: str, dirs: dict[str, Path]) -> tuple[Path, Path]:
    config_csv = dirs["cohort"] / f"models_config_{tag}.csv"
    results_csv = dirs["cohort"] / f"all_models_all_tasks_{tag}.csv"
    py = ROOT / ".venv/bin/python"
    rc = subprocess.run(
        [
            str(py),
            str(FILTER_SCRIPT),
            "--min-parse",
            str(args.min_parse),
            "--tasks",
            *args.tasks,
            "--output",
            str(config_csv),
            "--results-output",
            str(results_csv),
        ],
        cwd=str(ROOT),
    )
    if rc.returncode != 0:
        raise SystemExit(rc.returncode)
    for path in (config_csv, results_csv):
        if not path.exists():
            print(f"Missing: {path}", file=sys.stderr)
            raise SystemExit(1)
    return config_csv, results_csv


def build_f1_bonferroni_table(all_coeff_path: Path) -> pd.DataFrame | None:
    df = pd.read_csv(all_coeff_path)
    f1 = df[df["DV"] == "F1 Score"].copy()
    if f1.empty:
        return None

    task_order = ["Suicidal Ideation", "Therapy Request", "Therapy Engagement"]
    task_short = {"Suicidal Ideation": "SI", "Therapy Request": "TR", "Therapy Engagement": "TE"}
    var_order = [
        "Intercept",
        "Version: 2",
        "Version: 3",
        "Version: 4",
        "Parameter Size (B)",
        "Fine-Tune Type: Instruction-Tuned",
        "Fine-Tune Type: Mental Health Tuned",
        "Fine-Tune Type: Medical-Tuned",
        "Fine-Tune Type: Safety-Tuned",
        "Family: LLaMA",
        "Family: Qwen",
    ]

    def stars(p: float) -> str:
        if p < 0.001:
            return "***"
        if p < 0.01:
            return "**"
        if p < 0.05:
            return "*"
        return ""

    rows = []
    for var in var_order:
        row = {"Variable": var}
        for task in task_order:
            t = task_short[task]
            sub = f1[(f1["Task"] == task) & (f1["Variable"] == var)]
            if sub.empty:
                row[f"{t}-β"] = ""
                row[f"{t}-95% CI"] = ""
                continue
            r = sub.iloc[0]
            row[f"{t}-β"] = f"{r['β']:.3f}{stars(r['p_bonferroni'])}"
            row[f"{t}-95% CI"] = f"[{r['Bonf CI Lower']:.3f}, {r['Bonf CI Upper']:.3f}]"
        rows.append(row)

    for stat_name, col_name in [("R²", "R²"), ("Adj R²", "Adj R²"), ("N", "N")]:
        row = {"Variable": stat_name}
        for task in task_order:
            t = task_short[task]
            sub = f1[f1["Task"] == task].iloc[0]
            if stat_name == "N":
                row[f"{t}-β"] = f"{int(sub[col_name])}"
            else:
                row[f"{t}-β"] = f"{sub[col_name]:.3f}"
            row[f"{t}-95% CI"] = ""
        rows.append(row)

    col_order = ["Variable"] + [c for t in task_short.values() for c in (f"{t}-β", f"{t}-95% CI")]
    return pd.DataFrame(rows)[col_order]


def write_paste_deliverables(out_df: pd.DataFrame, out_dir: Path, tag: str) -> None:
    csv_path = out_dir / f"multivariable_regression_f1_bonferroni_{tag}.csv"
    tsv_path = out_dir / "table_1_f1_bonferroni_paste_format.tsv"
    out_df.to_csv(csv_path, index=False)
    header1 = ["", "Suicidal Ideation", "", "Therapy Request", "", "Therapy Engagement", ""]
    header2 = ["Variable", "β", "95% CI", "β", "95% CI", "β", "95% CI"]
    with tsv_path.open("w") as f:
        f.write("\t".join(header1) + "\n")
        f.write("\t".join(header2) + "\n")
        for _, row in out_df.iterrows():
            f.write("\t".join(str(row[c]) for c in out_df.columns) + "\n")
    print(f"Table 1 CSV: {csv_path}")
    print(f"Table 1 TSV (paste): {tsv_path}")


def run_table1(config_csv: Path, results_csv: Path, tag: str, out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    supp = out_dir / "supplemental_tables"
    supp.mkdir(parents=True, exist_ok=True)

    sys.path.insert(0, str(ROOT))
    import analysis.statistics.regression_analysis as ra
    from analysis.statistics.create_combined_tables import (
        create_combined_html_table,
        generate_per_task_files,
    )
    from analysis.statistics.create_regression_tables import (
        create_regression_table,
        create_regression_table_bonferroni,
    )

    ra.CONFIG_PATH = config_csv
    ra.ALL_MODELS_PATH = results_csv

    print(f"Table 1 config: {config_csv}")
    print(f"Table 1 results: {results_csv}")
    print(f"Deliverables: {out_dir}")
    print(f"Supplemental: {supp}")

    results = ra.run_all_regressions()
    ra.save_all_coefficient_tables(results, supp)
    summary = ra.create_summary_table(results)
    summary.to_csv(supp / "regression_summary.csv", index=False)
    print("\nModel fit summary:")
    print(summary.to_string(index=False))

    create_regression_table(supp, supp / "regression_table_combined.csv")
    create_regression_table_bonferroni(supp, supp / "regression_table_combined_bonferroni.csv")
    generate_per_task_files(supp)

    html_name = f"combined_regression_f1_score_bonferroni_{tag}.html"
    create_combined_html_table(
        supp,
        dv="f1_score",
        title=f"Regression Results: F1 Score (Bonferroni) — {tag}",
        output_file=html_name,
        correction_type="bonferroni",
    )

    paste_df = build_f1_bonferroni_table(supp / "all_coefficients.csv")
    if paste_df is None:
        print("Missing F1 coefficients for paste table", file=sys.stderr)
        return 1
    write_paste_deliverables(paste_df, out_dir, tag)
    return 0


def run_figure2(results_csv: Path, tag: str, out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    py = ROOT / ".venv/bin/python"
    rc = subprocess.run(
        [
            str(py),
            str(FIG2_SCRIPT),
            "--unified-csv",
            str(results_csv),
            "--output-dir",
            str(out_dir),
            "--prefix",
            "fig2",
            "--plots",
            "f1_vs_params_overall_trend",
        ],
        cwd=str(ROOT),
    )
    if rc.returncode != 0:
        return rc.returncode

    generated = out_dir / "fig2_f1_vs_params_overall_trend.png"
    final = out_dir / f"fig2_f1_vs_params_overall_trend_{tag}.png"
    if not generated.exists():
        print(f"Missing: {generated}", file=sys.stderr)
        return 1
    generated.rename(final)
    print(f"Figure 2: {final}")
    return 0


def run_figure3(config_csv: Path, results_csv: Path, tag: str, out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    supp = out_dir / "supplemental"
    supp.mkdir(parents=True, exist_ok=True)

    sys.path.insert(0, str(ROOT))
    import analysis.combined_finetune_facet_plot as cffp

    def load_filtered() -> tuple[pd.DataFrame, pd.DataFrame]:
        cfg = pd.read_csv(config_csv)
        cfg = cfg[cfg["enabled"] == True].copy()
        res = pd.read_csv(results_csv)
        return cfg, res

    cffp.load_data = load_filtered

    all_data = {}
    for ft_config in cffp.FINETUNE_TYPES:
        config, results = load_filtered()
        df = cffp.compute_deltas(config, results, ft_config["filter"], "f1_score", "f1")
        all_data[ft_config["name"]] = df
        print(f"{ft_config['label']}: {len(df)} data points")

    main_png = out_dir / f"delta_f1_facet_plot_{tag}.png"
    data_csv = supp / f"delta_f1_facet_plot_{tag}_data.csv"
    stats_csv = out_dir / f"delta_f1_facet_plot_{tag}_stats.csv"

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

    total_pts = sum(len(v) for v in all_data.values())
    print(f"Figure 3: {main_png}")
    print(f"Figure 3 stats: {stats_csv}")
    print(f"Figure 3 pair data (supplemental): {data_csv}")
    print(f"Total fine-tune/base pairs plotted: {total_pts}")
    return 0


def main() -> int:
    args = parse_args()
    tag = artifact_tag(args.min_parse, args.tasks)
    dirs = parse_run_dirs(args.min_parse, args.tasks)
    need_filter = args.target in ("all", "filter", "table1", "figure2", "figure3")

    print(f"Output root: {dirs['root']}")

    config_csv = dirs["cohort"] / f"models_config_{tag}.csv"
    results_csv = dirs["cohort"] / f"all_models_all_tasks_{tag}.csv"

    if need_filter:
        config_csv, results_csv = run_filter(args, tag, dirs)
        if args.target == "filter":
            return 0

    if args.target in ("all", "table1"):
        rc = run_table1(config_csv, results_csv, tag, dirs["table1"])
        if rc != 0:
            return rc

    if args.target in ("all", "figure2"):
        rc = run_figure2(results_csv, tag, dirs["fig2"])
        if rc != 0:
            return rc

    if args.target in ("all", "figure3"):
        rc = run_figure3(config_csv, results_csv, tag, dirs["fig3"])
        if rc != 0:
            return rc

    print(f"\nDone: min_parse={args.min_parse}, tasks={args.tasks}, target={args.target}")
    print(f"Artifacts: {dirs['root']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
