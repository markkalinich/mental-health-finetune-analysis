#!/usr/bin/env python3
"""4×3 facet paired bars: rows = metrics, cols = model; task pairs inside each cell.

Reads sg1_patched_full_analysis_summary.json (or per-task JSONs).

Usage:
  MPLBACKEND=Agg .venv/bin/python reviewer_2_experiments/plot_sg1_template_delta_grid.py
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress, t as t_dist

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from r2_paths import SG1_RESULTS, SG2_RESULTS

DEFAULT_SUMMARY = SG1_RESULTS / "sg1_patched_full_analysis_summary.json"
DEFAULT_SG2_SUMMARY = SG2_RESULTS / "shieldgemma_24b_sg2_analysis_summary.json"
FIGURES_DIR = SG1_RESULTS / "figures"

TASK_ORDER = ["SI", "TR", "TE"]
TASK_LABELS = {"SI": "SI", "TR": "TR", "TE": "TE"}
TASK_COLORS = {
    "SI": "#C73E1D",
    "TR": "#2E86AB",
    "TE": "#52B788",
}
SIZES = ["2b", "4b-it", "9b", "27b"]
SIZE_TITLES = {
    "2b": "ShieldGemma-2b",
    "4b-it": "ShieldGemma-2-4b-it",
    "9b": "ShieldGemma-9b",
    "27b": "ShieldGemma-27b",
}
METRICS = [
    ("parse_success_rate", "Parse success rate"),
    ("sensitivity", "Sensitivity"),
    ("specificity", "Specificity"),
    ("f1_score", "F1 score"),
]
GENERIC = "generic_override_LM_STUDIO_GEMMA"
PATCHED = "patched_SG1_after_yesno_reparse"
SG2_GENERIC = "generic_override_LM_STUDIO_GEMMA_as_scored"
SG2_PATCHED = "sg2_multimodal_after_yesno_reparse"

BAR_WIDTH = 0.22
PAIR_GAP = 0.06
SIZE_MARKERS = {"2b": "o", "9b": "s", "4b-it": "D", "27b": "^"}
SIZE_MS = {"2b": 70, "9b": 90, "4b-it": 85, "27b": 110}
JITTER_SEED = 42


def _jitter_x(x: float, task: str, size: str) -> float:
    rng = np.random.default_rng(JITTER_SEED)
    key = sum(ord(c) for c in task + size) % 97
    return x + (rng.random() - 0.5) * 0.012 + key * 1e-5


def load_metrics_table(summary_path: Path, sg2_summary_path: Path | None = None) -> pd.DataFrame:
    data = json.loads(summary_path.read_text())
    tasks = data["tasks"] if "tasks" in data else [data]
    rows = []
    for block in tasks:
        task = block["task"]
        by_size_label = {}
        for m in block["metrics"]:
            by_size_label.setdefault(m["model_size"], {})[m["label"]] = m
        for size in ("2b", "9b", "27b"):
            rec = by_size_label.get(size, {})
            g = rec.get(GENERIC)
            p = rec.get(PATCHED)
            if not g or not p:
                continue
            for key, _ in METRICS:
                gv = g.get(key)
                pv = p.get(key)
                delta = np.nan
                if gv is not None and pv is not None:
                    delta = float(pv) - float(gv)
                rows.append(
                    {
                        "task": task,
                        "model_size": size,
                        "metric": key,
                        "delta": delta,
                        "generic": gv,
                        "patched": pv,
                    }
                )

    if sg2_summary_path and sg2_summary_path.exists():
        sg2 = json.loads(sg2_summary_path.read_text())
        for block in sg2["tasks"]:
            task = block["task"]
            by_label = {m["label"]: m for m in block["metrics"]}
            g = by_label.get(SG2_GENERIC)
            p = by_label.get(SG2_PATCHED)
            if not g or not p:
                continue
            for key, _ in METRICS:
                gv = g.get(key)
                pv = p.get(key)
                delta = np.nan
                if gv is not None and pv is not None:
                    delta = float(pv) - float(gv)
                rows.append(
                    {
                        "task": task,
                        "model_size": "4b-it",
                        "metric": key,
                        "delta": delta,
                        "generic": gv,
                        "patched": pv,
                    }
                )
    return pd.DataFrame(rows)


def _pair_positions(task_idx: int) -> tuple[float, float]:
    center = float(task_idx)
    half = BAR_WIDTH / 2 + PAIR_GAP / 2
    return center - half, center + half


def _draw_cell(ax, sub: pd.DataFrame, size: str) -> None:
    task_centers = np.arange(len(TASK_ORDER))
    for ti, task in enumerate(TASK_ORDER):
        row = sub[(sub["model_size"] == size) & (sub["task"] == task)]
        if row.empty:
            continue
        row = row.iloc[0]
        x_gen, x_pat = _pair_positions(ti)
        color = TASK_COLORS[task]
        gv = float(row["generic"])
        pv = float(row["patched"])

        ax.bar(
            x_gen,
            gv,
            width=BAR_WIDTH,
            color=color,
            alpha=0.35,
            edgecolor="black",
            linewidth=0.6,
            hatch="//",
            zorder=2,
        )
        ax.bar(
            x_pat,
            pv,
            width=BAR_WIDTH,
            color=color,
            alpha=0.95,
            edgecolor="black",
            linewidth=0.6,
            zorder=3,
        )

    ax.set_xticks(task_centers)
    ax.set_xticklabels([TASK_LABELS[t] for t in TASK_ORDER], fontsize=12)
    ax.set_ylim(0, 1.05)
    ax.grid(axis="y", alpha=0.25, linestyle=":")


def plot_paired_bars_facet(df: pd.DataFrame, out_png: Path, out_csv: Path) -> None:
    n_rows = len(METRICS)
    n_cols = len(SIZES)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15.5, 14), sharey="row")

    for row_idx, (metric_key, metric_title) in enumerate(METRICS):
        sub = df[df["metric"] == metric_key]
        for col_idx, size in enumerate(SIZES):
            ax = axes[row_idx, col_idx]
            _draw_cell(ax, sub, size)

            if row_idx == 0:
                ax.set_title(SIZE_TITLES.get(size, f"ShieldGemma-{size}"), fontsize=11, fontweight="bold", pad=6)
            if col_idx == 0:
                ax.set_ylabel(metric_title, fontsize=13, fontweight="bold")

    task_handles = [
        mpatches.Patch(facecolor=TASK_COLORS[t], edgecolor="black", label=TASK_LABELS[t])
        for t in TASK_ORDER
    ]
    template_handles = [
        mpatches.Patch(facecolor="0.85", edgecolor="black", hatch="//", label="Generic"),
        mpatches.Patch(facecolor="0.55", edgecolor="black", label="Patched"),
    ]
    leg1 = fig.legend(
        handles=task_handles,
        loc="upper left",
        bbox_to_anchor=(0.06, 1.01),
        ncol=3,
        fontsize=10,
        title="Task",
        framealpha=0.95,
    )
    fig.add_artist(leg1)
    fig.legend(
        handles=template_handles,
        loc="upper right",
        bbox_to_anchor=(0.94, 1.01),
        ncol=2,
        fontsize=10,
        title="Template",
        framealpha=0.95,
    )
    fig.suptitle(
        "Template sensitivity: generic vs patched (SG-1: 2b/9b/27b; SG-2: 2-4b-it)",
        fontsize=14,
        fontweight="bold",
        y=1.04,
    )
    plt.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    df.to_csv(out_csv, index=False)
    print(f"Saved: {out_png}")
    print(f"Saved: {out_csv}")


def _draw_delta_scatter_ax(ax, sub: pd.DataFrame, metric_title: str, xlabel: str, ylabel: str) -> None:
    for task in TASK_ORDER:
        for size in SIZES:
            row = sub[(sub["task"] == task) & (sub["model_size"] == size)]
            if row.empty:
                continue
            row = row.iloc[0]
            x = float(row["generic"])
            y = float(row["delta"])
            ax.scatter(
                _jitter_x(x, task, size),
                y,
                c=TASK_COLORS[task],
                marker=SIZE_MARKERS[size],
                s=SIZE_MS[size],
                edgecolors="black",
                linewidths=0.6,
                alpha=0.9,
                zorder=3,
            )
    ax.axhline(0, color="0.45", linestyle="--", linewidth=1, zorder=1)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.set_title(metric_title, fontsize=11, fontweight="bold")
    ax.grid(alpha=0.25, linestyle=":")
    ax.set_xlim(-0.05, 1.05)


def _add_ols_line(ax, xs: np.ndarray, ys: np.ndarray) -> dict[str, float]:
    xs = np.asarray(xs, dtype=float)
    ys = np.asarray(ys, dtype=float)
    slope, intercept, r, p, stderr = linregress(xs, ys)
    n = len(xs)
    x_line = np.linspace(xs.min(), xs.max(), 100)
    y_line = slope * x_line + intercept

    if n >= 3 and np.ptp(xs) > 1e-12:
        y_pred = slope * xs + intercept
        residuals = ys - y_pred
        dof = n - 2
        s_err = float(np.sqrt(np.sum(residuals**2) / dof))
        x_mean = float(np.mean(xs))
        sxx = float(np.sum((xs - x_mean) ** 2))
        if sxx > 0:
            se_mean = s_err * np.sqrt(1.0 / n + (x_line - x_mean) ** 2 / sxx)
            t_crit = float(t_dist.ppf(0.975, dof))
            ci_lower = y_line - t_crit * se_mean
            ci_upper = y_line + t_crit * se_mean
            ax.fill_between(
                x_line,
                ci_lower,
                ci_upper,
                color="#CCCCCC",
                alpha=0.35,
                zorder=1,
                linewidth=0,
            )

    ax.plot(x_line, y_line, color="0.25", linestyle="-", linewidth=1.8, zorder=2)
    p_str = f"{p:.3g}" if p < 0.001 else f"{p:.3f}"
    ax.text(
        0.03,
        0.08,
        f"slope = {slope:.3f}\np = {p_str}",
        transform=ax.transAxes,
        fontsize=9,
        va="bottom",
        ha="left",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.9, "edgecolor": "0.7"},
        zorder=4,
    )
    return {"slope": float(slope), "intercept": float(intercept), "r": float(r), "p": float(p), "stderr": float(stderr)}


def plot_delta_scatter_2x2(df: pd.DataFrame, out_png: Path, out_csv: Path) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11, 9))
    xlabel = "Generic baseline"
    ylabel = "Δ (patched − generic)"
    for ax, (metric_key, metric_title) in zip(axes.flatten(), METRICS):
        _draw_delta_scatter_ax(ax, df[df["metric"] == metric_key], metric_title, xlabel, ylabel)

    task_handles = [
        plt.Line2D(
            [0], [0], marker="o", color="w", markerfacecolor=TASK_COLORS[t],
            markeredgecolor="black", markersize=8, label=TASK_LABELS[t],
        )
        for t in TASK_ORDER
    ]
    size_handles = [
        plt.Line2D(
            [0], [0], marker=SIZE_MARKERS[s], color="w", markerfacecolor="0.55",
            markeredgecolor="black", markersize={70: 8, 85: 8, 90: 9, 110: 10}[SIZE_MS[s]],
            label=SIZE_TITLES[s],
        )
        for s in SIZES
    ]
    leg1 = fig.legend(handles=task_handles, loc="upper left", bbox_to_anchor=(0.02, 1.02), ncol=3, title="Task")
    fig.add_artist(leg1)
    fig.legend(handles=size_handles, loc="upper right", bbox_to_anchor=(0.98, 1.02), ncol=2, title="Model")
    fig.suptitle(
        "Template sensitivity: baseline vs Δ (SG-1: 2b/9b/27b; SG-2: 2-4b-it)",
        fontsize=13, fontweight="bold", y=1.06,
    )
    plt.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    df.to_csv(out_csv, index=False)
    print(f"Saved: {out_png}")
    print(f"Saved: {out_csv}")


def plot_f1_delta_scatter(df: pd.DataFrame, out_png: Path, out_csv: Path) -> None:
    sub = df[df["metric"] == "f1_score"].copy()
    fig, ax = plt.subplots(figsize=(7.5, 6))
    _draw_delta_scatter_ax(
        ax, sub, "F1 score", "Generic F1 (baseline)", "ΔF1 (patched − generic)",
    )
    ols = _add_ols_line(ax, sub["generic"].to_numpy(dtype=float), sub["delta"].to_numpy(dtype=float))
    task_handles = [
        plt.Line2D(
            [0], [0], marker="o", color="w", markerfacecolor=TASK_COLORS[t],
            markeredgecolor="black", markersize=8, label=TASK_LABELS[t],
        )
        for t in TASK_ORDER
    ]
    size_handles = [
        plt.Line2D(
            [0], [0], marker=SIZE_MARKERS[s], color="w", markerfacecolor="0.55",
            markeredgecolor="black", markersize={70: 8, 85: 8, 90: 9, 110: 10}[SIZE_MS[s]],
            label=SIZE_TITLES[s],
        )
        for s in SIZES
    ]
    leg1 = ax.legend(
        handles=task_handles,
        loc="upper right",
        bbox_to_anchor=(0.56, 0.98),
        title="Task",
        framealpha=0.95,
        fontsize=9,
        title_fontsize=9,
    )
    ax.add_artist(leg1)
    ax.legend(
        handles=size_handles,
        loc="upper right",
        bbox_to_anchor=(0.98, 0.98),
        title="Model",
        framealpha=0.95,
        fontsize=8,
        title_fontsize=9,
    )
    ax.set_title(
        "F1 vs ΔF1: generic baseline vs template patch effect",
        fontsize=12, fontweight="bold", pad=10,
    )
    plt.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    sub = sub.assign(**{f"ols_{k}": v for k, v in ols.items()})
    sub.to_csv(out_csv, index=False)
    print(f"Saved: {out_png}")
    print(f"Saved: {out_csv}")
    print(f"OLS: slope={ols['slope']:.4f}, p={ols['p']:.4g}")


def plot_f1_oldnew_scatter(df: pd.DataFrame, out_png: Path, out_csv: Path) -> None:
    sub = df[df["metric"] == "f1_score"].copy()
    fig, ax = plt.subplots(figsize=(7.5, 6))
    for task in TASK_ORDER:
        for size in SIZES:
            row = sub[(sub["task"] == task) & (sub["model_size"] == size)]
            if row.empty:
                continue
            row = row.iloc[0]
            ax.scatter(
                float(row["generic"]),
                float(row["patched"]),
                c=TASK_COLORS[task],
                marker=SIZE_MARKERS[size],
                s=SIZE_MS[size],
                edgecolors="black",
                linewidths=0.6,
                alpha=0.9,
                zorder=3,
            )
    ax.plot([0, 1], [0, 1], color="0.45", linestyle="--", linewidth=1, zorder=1)
    ols = _add_ols_line(ax, sub["generic"].to_numpy(dtype=float), sub["patched"].to_numpy(dtype=float))
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("Generic F1 (old)", fontsize=10)
    ax.set_ylabel("Patched F1 (new)", fontsize=10)
    ax.grid(alpha=0.25, linestyle=":")
    task_handles = [
        plt.Line2D(
            [0], [0], marker="o", color="w", markerfacecolor=TASK_COLORS[t],
            markeredgecolor="black", markersize=8, label=TASK_LABELS[t],
        )
        for t in TASK_ORDER
    ]
    size_handles = [
        plt.Line2D(
            [0], [0], marker=SIZE_MARKERS[s], color="w", markerfacecolor="0.55",
            markeredgecolor="black", markersize={70: 8, 85: 8, 90: 9, 110: 10}[SIZE_MS[s]],
            label=SIZE_TITLES[s],
        )
        for s in SIZES
    ]
    leg1 = ax.legend(
        handles=task_handles, loc="lower right", bbox_to_anchor=(0.56, 0.02),
        title="Task", framealpha=0.95, fontsize=9, title_fontsize=9,
    )
    ax.add_artist(leg1)
    ax.legend(
        handles=size_handles, loc="lower right", bbox_to_anchor=(0.98, 0.02),
        title="Model", framealpha=0.95, fontsize=8, title_fontsize=9,
    )
    ax.set_title(
        "Old vs new F1: generic baseline vs patched template\n(points below y=x: generic better)",
        fontsize=12, fontweight="bold", pad=10,
    )
    plt.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    sub = sub.assign(**{f"ols_{k}": v for k, v in ols.items()})
    sub.to_csv(out_csv, index=False)
    print(f"Saved: {out_png}")
    print(f"Saved: {out_csv}")
    print(f"OLS (patched~generic): slope={ols['slope']:.4f}, r={ols['r']:.4f}, p={ols['p']:.4g}")


def plot_f1_paired_bars_by_task(df: pd.DataFrame, out_png: Path, out_csv: Path, layout: str = "rows") -> None:
    sub = df[df["metric"] == "f1_score"].copy()
    full_task_titles = {"SI": "Suicidal Ideation", "TR": "Therapy Request", "TE": "Therapy Engagement"}
    if layout == "grid":
        fig, axes = plt.subplots(2, 2, figsize=(13, 9))
        axlist = axes.flatten()
        axlist[3].axis("off")
        task_axes = list(zip(axlist[:3], TASK_ORDER))
        legend_ax = axlist[0]
    else:
        fig, axes = plt.subplots(1, len(TASK_ORDER), figsize=(19, 6))
        task_axes = list(zip(axes, TASK_ORDER))
        legend_ax = axes[0]
    rows_out = []
    w = 0.38
    for ax, task in task_axes:
        t = sub[sub["task"] == task].copy()
        t = t.sort_values("generic", ascending=True)
        models = t["model_size"].tolist()
        gen = t["generic"].astype(float).to_numpy()
        pat = t["patched"].astype(float).to_numpy()
        x = np.arange(len(models))
        color = TASK_COLORS[task]
        ax.bar(
            x - w / 2, gen, width=w, color=color, alpha=0.95, edgecolor="black",
            linewidth=0.6, zorder=2,
        )
        ax.bar(
            x + w / 2, pat, width=w, color=color, alpha=0.35, edgecolor="black",
            linewidth=0.6, hatch="//", zorder=2,
        )
        for xi, gv, pv in zip(x, gen, pat):
            ax.text(xi - w / 2, gv + 0.02, f"{gv:.2f}", ha="center", va="bottom", fontsize=7)
            ax.text(xi + w / 2, pv + 0.02, f"{pv:.2f}", ha="center", va="bottom", fontsize=7)
        ax.set_xticks(x)
        ax.set_xticklabels([SIZE_TITLES.get(m, m) for m in models], fontsize=13, rotation=45, ha="right")
        ax.tick_params(axis="y", labelsize=13)
        ax.set_ylim(0, 1.08)
        ax.set_ylabel("F1 score", fontsize=15)
        ax.set_title(full_task_titles[task], fontsize=18, fontweight="bold")
        ax.grid(axis="y", alpha=0.25, linestyle=":")
        for m, gv, pv in zip(models, gen, pat):
            rows_out.append({"task": task, "model_size": m, "generic": gv, "patched": pv})
    template_handles = [
        mpatches.Patch(facecolor="0.55", edgecolor="black", label="Generic"),
        mpatches.Patch(facecolor="0.85", edgecolor="black", hatch="//", label="Patched"),
    ]
    legend_ax.legend(handles=template_handles, loc="upper left", fontsize=10, framealpha=0.95, title="Template")
    plt.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    pd.DataFrame(rows_out).to_csv(out_csv, index=False)
    print(f"Saved: {out_png}")
    print(f"Saved: {out_csv}")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    p.add_argument(
        "--sg2-summary",
        type=Path,
        default=DEFAULT_SG2_SUMMARY,
        help="SG-2 analysis for shieldgemma-2-4b-it (4b-it column)",
    )
    p.add_argument(
        "--output-dir",
        type=Path,
        default=FIGURES_DIR,
    )
    p.add_argument(
        "--plots",
        nargs="+",
        choices=["facet", "scatter", "f1-scatter", "f1-oldnew", "f1-bars-bytask", "f1-bars-grid", "all"],
        default=["all"],
        help="Which figures to emit (default: all)",
    )
    args = p.parse_args()
    if not args.summary.exists():
        print(f"Missing: {args.summary}", flush=True)
        return 1
    df = load_metrics_table(args.summary, args.sg2_summary)
    want = set(args.plots)
    if "all" in want:
        want = {"facet", "scatter", "f1-scatter", "f1-oldnew", "f1-bars-bytask"}
    if "facet" in want:
        plot_paired_bars_facet(
            df,
            args.output_dir / "sg1_template_paired_bars_facet.png",
            args.output_dir / "sg1_template_paired_bars_facet.csv",
        )
    if "scatter" in want:
        plot_delta_scatter_2x2(
            df,
            args.output_dir / "sg1_template_delta_scatter_2x2.png",
            args.output_dir / "sg1_template_delta_scatter_2x2.csv",
        )
    if "f1-scatter" in want:
        plot_f1_delta_scatter(
            df,
            args.output_dir / "sg1_template_f1_delta_scatter.png",
            args.output_dir / "sg1_template_f1_delta_scatter.csv",
        )
    if "f1-oldnew" in want:
        plot_f1_oldnew_scatter(
            df,
            args.output_dir / "sg1_template_f1_oldnew_scatter.png",
            args.output_dir / "sg1_template_f1_oldnew_scatter.csv",
        )
    if "f1-bars-bytask" in want:
        plot_f1_paired_bars_by_task(
            df,
            args.output_dir / "sg1_template_f1_paired_bars_by_task.png",
            args.output_dir / "sg1_template_f1_paired_bars_by_task.csv",
        )
    if "f1-bars-grid" in want:
        plot_f1_paired_bars_by_task(
            df,
            args.output_dir / "sg1_template_f1_paired_bars_grid.png",
            args.output_dir / "sg1_template_f1_paired_bars_grid.csv",
            layout="grid",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
