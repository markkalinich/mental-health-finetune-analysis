"""
Delta–delta plot: Δ parse success (x) vs Δ F1 (y) for each Figure-3 fine-tune/base pair.

Uses the same load_data / compute_deltas pipeline as Figure 3. F1 and parse
deltas are merged on the
fine-tune identity (task, architecture family, ft_family, ft_size) so x and y
refer to the identical pair.

Convention (fine-tune − base):
  positive Δ parse  → fine-tune has higher parse success than its base
  positive Δ F1   → fine-tune has higher F1 than its base

Encoding: color = model family (Gemma/Llama/Qwen); marker area scales with
fine-tune parameter count (log mapping, same spirit as compact F1 vs params).

All panels share the same x/y limits. Each panel with n>=3 and varying x gets OLS +
95% CI for the mean response. Inset shows R² and the OLS slope p-value
(Bonferroni-adjusted within each fine-tune type row by number of testable tasks,
matching Figure 3's within-cell correction); trendline solid if p_adj < 0.05,
dashed otherwise.

Output: results/revision_experiments/delta_parse_vs_delta_f1_scatter.png (+ CSV)
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from scipy import stats as scipy_stats

ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from analysis.combined_finetune_facet_plot import (
    FAMILIES,
    FAMILY_COLORS,
    FAMILY_LABELS,
    FINETUNE_TYPES,
    TASKS,
    TASK_TITLES,
    compute_deltas,
    load_data,
)

OUT_DIR = ROOT / "results" / "revision_experiments"
MERGE_KEYS = ["task", "family", "ft_family", "ft_size"]


def format_p_scientific_2sf(p: float) -> str:
    """Format p in scientific notation with two significant figures (mantissa one decimal)."""
    if not np.isfinite(p) or p < 0:
        return "NA"
    p = float(min(p, 1.0))
    if p == 0.0:
        return "0.0e+00"
    exp = int(np.floor(np.log10(p)))
    mantissa = p / (10.0**exp)
    mantissa = float(np.round(mantissa, 1))
    if mantissa >= 10 - 1e-9:
        mantissa /= 10.0
        exp += 1
    return f"{mantissa:.1f}e{exp:+d}"


def _ols_raw_p_and_fit(
    x_pct: np.ndarray, y_f1: np.ndarray
) -> tuple[float | None, float | None, float | None, float | None]:
    """Return (p-value for slope!=0, slope, intercept, pearson_r) or all None."""
    x_pct = np.asarray(x_pct, dtype=float)
    y_f1 = np.asarray(y_f1, dtype=float)
    mask = np.isfinite(x_pct) & np.isfinite(y_f1)
    x_pct, y_f1 = x_pct[mask], y_f1[mask]
    n = len(x_pct)
    if n < 3 or np.ptp(x_pct) <= 1e-12:
        return None, None, None, None
    slope, intercept, r_val, p_val, _se = scipy_stats.linregress(x_pct, y_f1)
    return float(p_val), float(slope), float(intercept), float(r_val)


def _scatter_area_from_param_billions(param_billions) -> float:
    """Map parameter count (billions) to matplotlib scatter `s` (area), log-scaled."""
    if pd.isna(param_billions) or float(param_billions) <= 0:
        return 55.0
    size_b = float(param_billions)
    min_size, max_size = 0.3, 80.0
    min_marker, max_marker = 40.0, 320.0
    log_ratio = (np.log10(size_b) - np.log10(min_size)) / (
        np.log10(max_size) - np.log10(min_size)
    )
    log_ratio = float(np.clip(log_ratio, 0.0, 1.0))
    return min_marker + log_ratio * (max_marker - min_marker)


# Reference sizes for legend (billions → display label)
SIZE_LEGEND_REFS = [(0.3, "~0.3B"), (3.0, "~3B"), (30.0, "~30B"), (70.0, "~70B")]


def _global_xy_limits(merged_frames: list[pd.DataFrame]) -> tuple[tuple[float, float], tuple[float, float]]:
    """Shared x/y limits (Δ parse %, Δ F1) across all facets for comparison."""
    if not merged_frames:
        return ((-100.0, 100.0), (-1.05, 1.05))
    big = pd.concat(merged_frames, ignore_index=True)
    x = (big["delta_parse"].values * 100.0).astype(float)
    y = big["delta_f1"].values.astype(float)
    x = x[np.isfinite(x)]
    y = y[np.isfinite(y)]
    if len(x) == 0:
        return ((-100.0, 100.0), (-1.05, 1.05))

    def padded(lo: float, hi: float, min_pad: float) -> tuple[float, float]:
        span = hi - lo
        pad = max(span * 0.06, min_pad)
        return (lo - pad, hi + pad)

    xlim = padded(float(np.min(x)), float(np.max(x)), 2.0)
    ylim = padded(float(np.min(y)), float(np.max(y)), 0.05)
    return (xlim, ylim)


def _add_ols_trend_and_ci(
    ax,
    x_pct: np.ndarray,
    y_f1: np.ndarray,
    color: str = "#333333",
    line_alpha: float = 0.9,
    band_alpha: float = 0.2,
    linestyle: str = "-",
    linewidth: float = 2.4,
) -> None:
    """OLS line + 95% CI for mean response (shaded); points on top (higher zorder)."""
    x_pct = np.asarray(x_pct, dtype=float)
    y_f1 = np.asarray(y_f1, dtype=float)
    mask = np.isfinite(x_pct) & np.isfinite(y_f1)
    x_pct, y_f1 = x_pct[mask], y_f1[mask]
    n = len(x_pct)
    if n < 3 or np.ptp(x_pct) <= 1e-12:
        return

    slope, intercept, _, _, _ = scipy_stats.linregress(x_pct, y_f1)
    x_line = np.linspace(float(np.min(x_pct)), float(np.max(x_pct)), 100)
    y_line = slope * x_line + intercept

    y_pred = slope * x_pct + intercept
    residuals = y_f1 - y_pred
    dof = n - 2
    if dof < 1:
        return
    s_err = float(np.sqrt(np.sum(residuals**2) / dof))
    x_mean = float(np.mean(x_pct))
    Sxx = float(np.sum((x_pct - x_mean) ** 2))
    if Sxx <= 0:
        return
    se_mean = s_err * np.sqrt(1.0 / n + (x_line - x_mean) ** 2 / Sxx)
    t_crit = float(scipy_stats.t.ppf(0.975, dof))
    lo = y_line - t_crit * se_mean
    hi = y_line + t_crit * se_mean

    ax.fill_between(x_line, lo, hi, color=color, alpha=band_alpha, zorder=2, linewidth=0)
    ax.plot(
        x_line,
        y_line,
        color=color,
        linewidth=linewidth,
        alpha=line_alpha,
        linestyle=linestyle,
        zorder=2,
    )


def merged_f1_and_parse_for_facet(ft_config: dict) -> pd.DataFrame:
    """Same results table and filters as Figure 3 for this facet row."""
    config, results = load_data()
    df_f1 = compute_deltas(config, results, ft_config["filter"], "f1_score", "f1")
    df_p = compute_deltas(
        config, results, ft_config["filter"], "parse_success_rate", "parse"
    )
    if df_f1.empty or df_p.empty:
        return pd.DataFrame()
    drop_overlap = [
        c
        for c in ("base_family", "base_size", "ft_model_type", "ft_param_billions")
        if c in df_p.columns
    ]
    df_p = df_p.drop(columns=drop_overlap, errors="ignore")
    merged = df_f1.merge(df_p, on=MERGE_KEYS, how="inner", validate="one_to_one")
    return merged


def plot_delta_delta_facets(
    out_png: Path | None = None,
    out_csv: Path | None = None,
) -> tuple[Path, Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if out_png is None:
        out_png = OUT_DIR / "delta_parse_vs_delta_f1_scatter.png"
    if out_csv is None:
        out_csv = OUT_DIR / "delta_parse_vs_delta_f1_merged.csv"

    all_merged = []
    panel_subs: dict[tuple[int, int], tuple[dict, pd.DataFrame]] = {}

    for row_idx, ft_config in enumerate(FINETUNE_TYPES):
        merged = merged_f1_and_parse_for_facet(ft_config)
        if len(merged) > 0:
            merged = merged.assign(finetune_type=ft_config["name"])
            all_merged.append(merged)
        for col_idx, task in enumerate(TASKS):
            sub = merged[merged["task"] == task] if len(merged) else pd.DataFrame()
            panel_subs[(row_idx, col_idx)] = (ft_config, sub)

    xlim, ylim = _global_xy_limits(all_merged)

    panel_ols_p_raw: dict[tuple[int, int], float | None] = {}
    panel_pearson_r: dict[tuple[int, int], float | None] = {}
    for row_idx in range(len(FINETUNE_TYPES)):
        for col_idx in range(len(TASKS)):
            _, sub = panel_subs[(row_idx, col_idx)]
            p_raw, r_val = None, None
            if len(sub) >= 3:
                x_arr = sub["delta_parse"].values * 100.0
                y_arr = sub["delta_f1"].values
                p_raw, _, _, r_val = _ols_raw_p_and_fit(x_arr, y_arr)
            panel_ols_p_raw[(row_idx, col_idx)] = p_raw
            panel_pearson_r[(row_idx, col_idx)] = r_val

    # Bonferroni within each row (fine-tune type) by testable tasks — matches Figure 3
    n_testable_per_row: dict[int, int] = {}
    for row_idx in range(len(FINETUNE_TYPES)):
        n_testable = sum(
            1 for col_idx in range(len(TASKS))
            if panel_ols_p_raw[(row_idx, col_idx)] is not None
        )
        n_testable_per_row[row_idx] = max(n_testable, 1)

    fig, axes = plt.subplots(4, 3, figsize=(18, 20), sharex=True, sharey=True)

    FS_AXIS_LABEL = 18  # −25% from 24
    FS_TITLE_COL = 21  # was 14 → +50%
    FS_SUPTITLE = 26
    FS_TICK = 15  # −25% from 20
    FS_INSET = 13.5  # −25% from 18 (r / p / n box)
    # Match Figure 3 facet plot panel letters (combined_finetune_facet_plot.py)
    FS_PANEL = 26
    FS_LEGEND = 22.5  # +25% from 18
    FS_LEGEND_SMALL = 20  # +25% from 16
    FS_LEGEND_TITLE = 23.75  # +25% from 19

    for row_idx, ft_config in enumerate(FINETUNE_TYPES):
        for col_idx, task in enumerate(TASKS):
            ax = axes[row_idx, col_idx]
            _, sub = panel_subs[(row_idx, col_idx)]

            ax.axhline(0, color="gray", linestyle="--", linewidth=1.2, alpha=0.75, zorder=1)
            ax.axvline(0, color="gray", linestyle="--", linewidth=1.2, alpha=0.75, zorder=1)
            ax.grid(True, alpha=0.28, zorder=0)
            ax.tick_params(axis="both", which="major", labelsize=FS_TICK)

            p_raw = panel_ols_p_raw[(row_idx, col_idx)]
            n_comparisons = n_testable_per_row[row_idx]
            p_adj = min(p_raw * n_comparisons, 1.0) if p_raw is not None else None
            sig = p_adj is not None and p_adj < 0.05
            trend_style = "-" if sig else "--"

            if len(sub) >= 3 and p_raw is not None:
                x_arr = sub["delta_parse"].values * 100.0
                y_arr = sub["delta_f1"].values
                _add_ols_trend_and_ci(ax, x_arr, y_arr, linestyle=trend_style)

            for _, pt in sub.iterrows():
                fam = pt["family"]
                c = FAMILY_COLORS.get(fam, "#888888")
                s_area = _scatter_area_from_param_billions(pt["ft_param_billions"])
                ax.scatter(
                    pt["delta_parse"] * 100.0,
                    pt["delta_f1"],
                    s=s_area,
                    alpha=0.72,
                    c=c,
                    marker="o",
                    edgecolors="black",
                    linewidths=0.45,
                    zorder=3,
                )

            if len(sub) >= 3:
                r_pearson = panel_pearson_r[(row_idx, col_idx)]
                if r_pearson is not None and p_adj is not None:
                    r2 = r_pearson ** 2
                    p_str = format_p_scientific_2sf(p_adj)
                    stat_block = f"R² = {r2:.2f}\np = {p_str}\nn = {len(sub)}"
                elif r_pearson is not None:
                    r2 = r_pearson ** 2
                    stat_block = f"R² = {r2:.2f}\np = NA\nn = {len(sub)}"
                else:
                    stat_block = f"n = {len(sub)}"
                ax.text(
                    0.02,
                    0.98,
                    stat_block,
                    transform=ax.transAxes,
                    fontsize=FS_INSET,
                    va="top",
                    ha="left",
                    bbox=dict(boxstyle="round,pad=0.35", facecolor="white", alpha=0.88, edgecolor="none"),
                )

            ax.set_xlim(xlim)
            ax.set_ylim(ylim)

            if col_idx == 0:
                ax.set_ylabel(f'{ft_config["label"]}\nΔ(F1)', fontsize=FS_AXIS_LABEL, fontweight="bold")
                panel = chr(65 + row_idx)
                ax.text(
                    -0.18,
                    1.08,
                    panel,
                    transform=ax.transAxes,
                    fontsize=FS_PANEL,
                    fontweight="bold",
                    va="top",
                    ha="left",
                )

            if row_idx == 0:
                ax.set_title(TASK_TITLES[task], fontsize=FS_TITLE_COL, fontweight="bold", pad=12)

            if row_idx == 3:
                ax.set_xlabel("Δ(Parse success) (%)", fontsize=FS_AXIS_LABEL, fontweight="bold")

    family_handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor=FAMILY_COLORS[f],
            markeredgecolor="black",
            markeredgewidth=0.5,
            markersize=18,
            linestyle="None",
            label=FAMILY_LABELS[f],
        )
        for f in FAMILIES
    ]
    leg_fam = fig.legend(
        handles=family_handles,
        title="Model family (color)",
        loc="upper center",
        bbox_to_anchor=(0.30, 0.01),
        ncol=3,
        fontsize=FS_LEGEND,
        framealpha=0.95,
    )
    leg_fam.get_title().set_fontsize(FS_LEGEND_TITLE)
    fig.add_artist(leg_fam)

    size_handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="gray",
            linestyle="None",
            markersize=max(5.0, np.sqrt(_scatter_area_from_param_billions(b)) * 0.69),
            markeredgecolor="black",
            markeredgewidth=0.45,
            alpha=0.75,
            label=lab,
        )
        for b, lab in SIZE_LEGEND_REFS
    ]
    leg_size = fig.legend(
        handles=size_handles,
        title=r"Fine-tune params (marker area, $\log_{10}$ scale)",
        loc="upper center",
        bbox_to_anchor=(0.72, 0.01),
        ncol=4,
        fontsize=FS_LEGEND_SMALL,
        framealpha=0.95,
    )
    leg_size.get_title().set_fontsize(FS_LEGEND_TITLE)
    fig.add_artist(leg_size)

    plt.suptitle(
        "Δ(F1) versus Δ(Parse Success Rate) for Fine-Tune versus Base Models",
        fontsize=FS_SUPTITLE,
        fontweight="bold",
        y=0.995,
    )
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.35, wspace=0.22, top=0.94, bottom=0.10)
    plt.savefig(out_png, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    if all_merged:
        pd.concat(all_merged, ignore_index=True).to_csv(out_csv, index=False)
    else:
        pd.DataFrame().to_csv(out_csv, index=False)

    print(f"Saved: {out_png}")
    print(f"Saved: {out_csv}")
    return out_png, out_csv


if __name__ == "__main__":
    plot_delta_delta_facets()
