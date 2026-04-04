"""
Correction-note overlay for Figure 2 (F1 vs Parameters, overall trendline).

Generates a 3×3 panel (families × tasks) showing:
  - All non-safety points at moderate alpha (ghost layer)
  - Safety-model points with RED arrows from old → new position
  - Old overall trendline (dashed) vs new overall trendline (solid)
  - Version-based marker shapes matching the original Figure 2

The OLD safety F1 values come from safety_model_f1_before_after.csv (the
runtime-corrected buggy values), NOT from the raw old CSV (which had zeros
for guard models and un-corrected ShieldGemma values).

Output: results/FINETUNE_PAPER_FIGURES/<run>/correction_note/
            figure2_correction_overlay.png
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
import pandas as pd
from scipy import stats as scipy_stats

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "analysis" / "comparative_analysis"))

from compact_unified_facet_plot import (
    FAMILIES,
    FAMILY_LABELS,
    TASKS,
    TASK_LABELS,
    TYPE_COLORS,
    VERSION_MARKERS,
    load_unified_data,
    normalize_version_for_plotting,
)

NEW_CSV = ROOT / "data" / "inputs" / "model_results" / "all_models_all_tasks.csv"
BEFORE_AFTER_CSV = (
    ROOT / "results" / "FINETUNE_PAPER_FIGURES" / "20260330_233116"
    / "correction_note" / "safety_model_f1_before_after.csv"
)

TASK_SHORT_TO_LONG = {"SI": "suicidal_ideation", "TR": "therapy_request", "TE": "therapy_engagement"}
SAFETY_MODEL_TYPES = {"Safety", "ShieldGemma", "Guard"}
BONF_ALPHA = 0.05 / 9


def _is_safety(model_type: str) -> bool:
    return model_type in SAFETY_MODEL_TYPES


def _ols_on_log(x: np.ndarray, y: np.ndarray):
    mask = np.isfinite(x) & np.isfinite(y) & (x > 0)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return None, None, None, None, len(x)
    lx = np.log10(x)
    slope, intercept, r, p, _ = scipy_stats.linregress(lx, y)
    return slope, intercept, r**2, p, len(x)


def _draw_ols_line(ax, x_range, slope, intercept, *, color, ls, lw, alpha, label, zorder=5):
    xs = np.linspace(np.log10(x_range[0]), np.log10(x_range[1]), 200)
    ys = slope * xs + intercept
    ax.plot(10**xs, ys, color=color, ls=ls, lw=lw, alpha=alpha, label=label, zorder=zorder)


def _build_old_df(df_new: pd.DataFrame, before_after: pd.DataFrame) -> pd.DataFrame:
    """Build the 'old' dataset: new data with safety F1s swapped to buggy values."""
    df_old = df_new.copy()
    ba = before_after.copy()
    ba["task"] = ba["Task"].map(TASK_SHORT_TO_LONG)
    ba["model_key"] = ba["Model"]

    df_old["model_key"] = df_old["model_family"] + " " + df_old["model_size"]

    for _, ba_row in ba.iterrows():
        mask = (df_old["task"] == ba_row["task"]) & (df_old["model_key"] == ba_row["model_key"])
        df_old.loc[mask, "f1_score"] = float(ba_row["Old F1"])

    df_old.drop(columns=["model_key"], inplace=True)
    return df_old


def main(out_dir: Path | None = None):
    if not BEFORE_AFTER_CSV.exists():
        sys.exit(f"Missing before/after CSV: {BEFORE_AFTER_CSV}")

    df_new = load_unified_data(str(NEW_CSV))
    df_new = normalize_version_for_plotting(df_new)
    before_after = pd.read_csv(BEFORE_AFTER_CSV)
    df_old = _build_old_df(df_new, before_after)

    if out_dir is None:
        results_root = ROOT / "results" / "FINETUNE_PAPER_FIGURES"
        runs = sorted(results_root.iterdir()) if results_root.exists() else []
        out_dir = (runs[-1] if runs else results_root) / "correction_note"
    out_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(3, 3, figsize=(16, 13), sharex="col", sharey=True)

    for fam_idx, (family, fam_label) in enumerate(zip(FAMILIES, FAMILY_LABELS)):
        for task_idx, (task, task_label) in enumerate(zip(TASKS, TASK_LABELS)):
            ax = axes[fam_idx, task_idx]

            cell_new = df_new[(df_new["base_family"] == family) & (df_new["task"] == task)].copy()
            cell_old = df_old[(df_old["base_family"] == family) & (df_old["task"] == task)].copy()

            nonsafety = cell_new[~cell_new["model_type"].apply(_is_safety)]
            safety_new = cell_new[cell_new["model_type"].apply(_is_safety)].copy()
            safety_old = cell_old[cell_old["model_type"].apply(_is_safety)].copy()

            # Ghost layer: non-safety points with version shapes
            if len(nonsafety) > 0:
                for _, row in nonsafety.iterrows():
                    marker = VERSION_MARKERS.get(row.get("version_ordinal", 1), "o")
                    ax.scatter(
                        row["size_billions"], row["f1_score"],
                        c=TYPE_COLORS.get(row["model_type"], "#888888"),
                        marker=marker, s=70, alpha=0.15, edgecolors="none", zorder=2,
                    )

            # Safety: old (open) → new (filled) with red arrows
            if len(safety_new) > 0 and len(safety_old) > 0:
                s_new = safety_new.sort_values(["model_family", "model_size"]).reset_index(drop=True)
                s_old = safety_old.sort_values(["model_family", "model_size"]).reset_index(drop=True)

                for i in range(min(len(s_old), len(s_new))):
                    xo = s_old.loc[i, "size_billions"]
                    yo = s_old.loc[i, "f1_score"]
                    xn = s_new.loc[i, "size_billions"]
                    yn = s_new.loc[i, "f1_score"]
                    vo = s_new.loc[i].get("version_ordinal", 1)
                    marker = VERSION_MARKERS.get(vo, "o")

                    if abs(yn - yo) > 0.005 or abs((xn - xo) / max(xo, 0.01)) > 0.05:
                        ax.annotate(
                            "", xy=(xn, yn), xytext=(xo, yo),
                            arrowprops=dict(
                                arrowstyle="-|>", color="#CC0000",
                                lw=1.6, mutation_scale=13, shrinkA=4, shrinkB=4,
                            ),
                            zorder=6,
                        )

                    # Old position (open)
                    ax.scatter(xo, yo, s=80, facecolors="none", edgecolors="#7B2D8E",
                               linewidths=1.3, zorder=7, marker=marker)
                    # New position (filled)
                    ax.scatter(xn, yn, s=80, c="#7B2D8E", edgecolors="black",
                               linewidths=0.6, zorder=8, marker=marker)

            # Overall trendlines (all models in family, old vs new)
            all_x = cell_new["size_billions"].values
            x_range = (max(all_x.min(), 0.1), all_x.max()) if len(all_x) > 0 else (0.1, 80)

            sl_o, int_o, _, p_o, _ = _ols_on_log(
                cell_old["size_billions"].values, cell_old["f1_score"].values
            )
            sl_n, int_n, _, p_n, _ = _ols_on_log(
                cell_new["size_billions"].values, cell_new["f1_score"].values
            )

            # Trendlines: solid=significant, dashed=NS (matching Figure 2 convention)
            # Color distinguishes old (orange) vs new (dark gray)
            if sl_o is not None:
                ls_old = "-" if (p_o is not None and p_o < BONF_ALPHA) else "--"
                _draw_ols_line(ax, x_range, sl_o, int_o,
                               color="#E08B00", ls=ls_old, lw=2.0, alpha=0.75,
                               label="Original", zorder=4)
            if sl_n is not None:
                ls_new = "-" if (p_n is not None and p_n < BONF_ALPHA) else "--"
                _draw_ols_line(ax, x_range, sl_n, int_n,
                               color="#333333", ls=ls_new, lw=2.2, alpha=0.9,
                               label="Corrected", zorder=5)

            ax.set_xscale("log")
            ax.set_ylim(-0.05, 1.05)
            ax.grid(True, alpha=0.2, zorder=0)

            if fam_idx == 0:
                ax.set_title(task_label, fontsize=21, fontweight="bold", pad=10)
            if task_idx == 0:
                ax.set_ylabel(f"{fam_label}\nF1 Score", fontsize=18, fontweight="bold")
            if fam_idx == 2:
                ax.set_xlabel("Parameters (B)", fontsize=18)

    VERSION_LABELS = {1: "v1", 2: "v2", 3: "v3", 4: "3.1+"}

    # Row 1: trendlines
    trend_handles = [
        mlines.Line2D([], [], color="#E08B00", ls="-", lw=2, label="Original (sig)"),
        mlines.Line2D([], [], color="#E08B00", ls="--", lw=2, label="Original (NS)"),
        mlines.Line2D([], [], color="#333333", ls="-", lw=2.2, label="Corrected (sig)"),
        mlines.Line2D([], [], color="#333333", ls="--", lw=2.2, label="Corrected (NS)"),
    ]
    # Row 2: safety markers + arrows
    marker_handles = [
        mlines.Line2D([], [], color="none", marker="o", markerfacecolor="none",
                       markeredgecolor="#7B2D8E", markersize=8, markeredgewidth=1.3,
                       label="Safety (original)"),
        mlines.Line2D([], [], color="none", marker="o", markerfacecolor="#7B2D8E",
                       markeredgecolor="black", markersize=8, markeredgewidth=0.6,
                       label="Safety (corrected)"),
        mlines.Line2D([], [], color="#CC0000", ls="-", lw=1.6,
                       marker=">", markersize=6, label="Direction of change"),
    ]
    # Row 3: version shapes
    version_handles = [
        mlines.Line2D([], [], color="none", marker=VERSION_MARKERS[v],
                       markerfacecolor="#888888", markeredgecolor="none",
                       markersize=8, label=VERSION_LABELS[v])
        for v in sorted(VERSION_MARKERS.keys())
    ]

    leg1 = fig.legend(handles=trend_handles, loc="lower center", ncol=4,
                      fontsize=14, framealpha=0.95, bbox_to_anchor=(0.5, -0.005),
                      title="Trendlines", title_fontsize=15)
    fig.add_artist(leg1)
    leg2 = fig.legend(handles=marker_handles, loc="lower center", ncol=3,
                      fontsize=14, framealpha=0.95, bbox_to_anchor=(0.5, -0.065),
                      title="Markers", title_fontsize=15)
    fig.add_artist(leg2)
    fig.legend(handles=version_handles, loc="lower center", ncol=4,
               fontsize=14, framealpha=0.95, bbox_to_anchor=(0.5, -0.125),
               title="Version (shape)", title_fontsize=15)

    plt.suptitle("Figure 2 Correction Overlay: Safety Model F1 vs Parameters",
                 fontsize=22, fontweight="bold", y=1.01)
    plt.tight_layout(rect=[0, 0.04, 1, 1.0])

    out_path = out_dir / "figure2_correction_overlay.png"
    plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out_path}")
    return out_path


if __name__ == "__main__":
    main()
