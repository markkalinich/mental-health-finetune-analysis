"""
Correction-note panel for Figure 3 (ΔF1 for safety-tuned models).

Generates a 2×3 panel matching the box-plot style of Figure 3 Row C:
  - Top row: Original (buggy) ΔF1 for safety models
  - Bottom row: Corrected ΔF1 for safety models
  - Columns: SI, TR, TE
  - Box plots with jittered points, grouped by architecture family

Output: results/FINETUNE_PAPER_FIGURES/<run>/correction_note/
            figure3_correction_panel.png
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from scipy import stats as scipy_stats

ROOT = Path(__file__).resolve().parent.parent.parent

OLD_DELTA = Path("/home/mkalinich/safety_simulations/results/FINETUNE_PAPER_FIGURES/20251231_004214/figure_3/delta_f1_data.csv")
NEW_DELTA = ROOT / "results" / "FINETUNE_PAPER_FIGURES" / "20260330_233116" / "figure_3" / "delta_f1_data.csv"

TASKS = ["suicidal_ideation", "therapy_request", "therapy_engagement"]
TASK_LABELS = {
    "suicidal_ideation": "Suicidal Ideation",
    "therapy_request": "Therapy Request",
    "therapy_engagement": "Therapy Engagement",
}
FAMILIES = ["gemma", "llama", "qwen"]
FAMILY_LABELS = {"gemma": "Gemma", "llama": "Llama", "qwen": "Qwen"}
FAMILY_COLORS = {"gemma": "#E74C3C", "llama": "#3498DB", "qwen": "#2ECC71"}


def _load_safety(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df[df["finetune_type"] == "safety"].copy()


def _ensure_family_col(old_sf: pd.DataFrame, new_sf: pd.DataFrame) -> pd.DataFrame:
    """Old file lacks detail columns; copy from new (same row order)."""
    if "ft_family" not in old_sf.columns:
        assert (old_sf["family"].values == new_sf["family"].values).all()
        assert (old_sf["task"].values == new_sf["task"].values).all()
        old_sf = old_sf.copy()
        old_sf["ft_family"] = new_sf["ft_family"].values
        old_sf["ft_size"] = new_sf["ft_size"].values
        old_sf["ft_param_billions"] = new_sf["ft_param_billions"].values
    return old_sf


def _plot_row(axes_row, data, row_label):
    for col_idx, task in enumerate(TASKS):
        ax = axes_row[col_idx]
        task_data = data[data["task"] == task]

        n_testable = sum(
            1 for fam in FAMILIES
            if len(task_data[task_data["family"] == fam]) >= 2
        )

        row_max_y = 0.0
        for fam in FAMILIES:
            fam_data = task_data[task_data["family"] == fam]
            if len(fam_data) > 0:
                row_max_y = max(row_max_y, float(fam_data["delta_f1"].max()))

        box_data, positions, colors = [], [], []
        for i, fam in enumerate(FAMILIES):
            fam_data = task_data[task_data["family"] == fam]
            if len(fam_data) > 0:
                box_data.append(fam_data["delta_f1"].values)
                positions.append(i)
                colors.append(FAMILY_COLORS[fam])

        if box_data:
            bp = ax.boxplot(
                box_data, positions=positions, widths=0.6, patch_artist=True,
                showfliers=False, medianprops=dict(color="black", linewidth=2),
            )
            for patch, color in zip(bp["boxes"], colors):
                patch.set_facecolor(color)
                patch.set_alpha(0.6)
                patch.set_edgecolor(color)

            for i, fam in enumerate(FAMILIES):
                fam_data = task_data[task_data["family"] == fam]
                if len(fam_data) > 0:
                    x_jitter = i + np.random.uniform(-0.2, 0.2, len(fam_data))
                    ax.scatter(
                        x_jitter, fam_data["delta_f1"].values, s=50, alpha=0.5,
                        color=FAMILY_COLORS[fam], edgecolors="black", linewidth=0.5, zorder=10,
                    )

            if n_testable > 0:
                for i, fam in enumerate(FAMILIES):
                    fam_data = task_data[task_data["family"] == fam]
                    if len(fam_data) >= 2:
                        _, p = scipy_stats.ttest_rel(
                            fam_data["ft_f1"].values, fam_data["base_f1"].values
                        )
                        p_adj = min(p * n_testable, 1.0)
                        if p_adj < 0.001:
                            sig = "***"
                        elif p_adj < 0.01:
                            sig = "**"
                        elif p_adj < 0.05:
                            sig = "*"
                        else:
                            sig = None
                        if sig:
                            y_pos = row_max_y + 0.08
                            ax.text(i, y_pos, sig, ha="center", fontsize=18, fontweight="bold")

        ax.axhline(0, color="gray", ls="--", lw=0.8, alpha=0.5, zorder=1)
        ax.set_xticks(range(len(FAMILIES)))
        ax.set_xticklabels([FAMILY_LABELS[f] for f in FAMILIES], fontsize=14)
        ax.grid(True, axis="y", alpha=0.15, zorder=0)

        if col_idx == 0:
            ax.set_ylabel(f"{row_label}\nΔF1 Score", fontsize=18, fontweight="bold")


def main():
    np.random.seed(42)

    old_sf = _load_safety(OLD_DELTA)
    new_sf = _load_safety(NEW_DELTA)
    old_sf = _ensure_family_col(old_sf, new_sf)

    fig, axes = plt.subplots(2, 3, figsize=(18, 10), sharey=True)

    _plot_row(axes[0], old_sf, "Original")
    _plot_row(axes[1], new_sf, "Corrected")

    for col_idx, task in enumerate(TASKS):
        axes[0, col_idx].set_title(TASK_LABELS[task], fontsize=21, fontweight="bold", pad=10)

    legend_handles = [
        mpatches.Patch(facecolor=FAMILY_COLORS[f], edgecolor=FAMILY_COLORS[f],
                       alpha=0.6, label=FAMILY_LABELS[f])
        for f in FAMILIES
    ]
    fig.legend(handles=legend_handles, loc="lower center", ncol=3,
               fontsize=14, framealpha=0.95, bbox_to_anchor=(0.5, -0.02),
               title="Architecture Family", title_fontsize=15)

    plt.suptitle("Figure 3 Correction: Safety-Tuned ΔF1 (Original vs Corrected)",
                 fontsize=22, fontweight="bold", y=1.01)
    plt.tight_layout(rect=[0, 0.03, 1, 1.0])

    results_root = ROOT / "results" / "FINETUNE_PAPER_FIGURES"
    runs = sorted(results_root.iterdir()) if results_root.exists() else []
    out_dir = (runs[-1] if runs else results_root) / "correction_note"
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "figure3_correction_panel.png"
    plt.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
