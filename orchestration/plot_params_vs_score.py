#!/usr/bin/env python3
"""Parameters against the three study scores.

The family figure has one row for Qwen, Gemma, Llama, and the other families.
The combined figure puts every model on one row. Columns are synthetic SI F1,
Reddit C-SSRS F1, and the MentalHealthBench score. F1 is drawn from 0 to 1.
MentalHealthBench keeps the 0–40 range.

Color is the fine-tune on both figures. On the family figure, marker shape is
the version bucket from analysis/comparative_analysis/compact_unified_facet_plot.py:
v1, v2, v3, and the fourth bucket that plot labeled v3.1+ (drawn here as v4).
On the combined figure, marker shape is the model family. A line is the score
against log2(parameters), the same scale as Table 1. R² and the Benjamini-Hochberg q-value for that
figure's panels are printed in the upper left of each panel.

The scores are the parse-rate figure: SI v2 and C-SSRS v5, with a card label
counted for the nine safety models and with Sonnet's yes or no counted when
the format check failed. F1 is blank when a format failure has no Sonnet label.
The third column
is the MentalHealthBench safety subset (the English user suicide or self-harm
questions), stored on the percent scale used by that figure. Safety models
have no point in that column. Pretrained checkpoints are drawn when
orchestration.study_roster.DRAW_PRETRAINED is true.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator
from scipy import stats

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from orchestration.plot_parse_rates import _param_billions

DIR = REPO / "outputs/cross-grouping/model_performance"
OUT = DIR / "params-vs-score.png"
OUT_ALL = DIR / "params-vs-score-all.png"
OUT_TYPE = DIR / "params-vs-score-by-type.png"
OUT_HEAT = DIR / "scores-by-family.png"
STATS = DIR / "params-vs-score-regressions.csv"

ROWS = ("Qwen", "Gemma", "Llama", "Other")
COLUMNS = (
    ("synthetic_si", "Synthetic SI (F1)"),
    ("cssrs", "Reddit C-SSRS (F1)"),
    ("mentalhealthbench", "MHB-Safety"),
)
COLORS = {
    "parent": "#2E86AB",
    "pretrained": "#115E59",
    "mental-health": "#C73E1D",
    "safety": "#7B2D8E",
    "medical": "#F18F01",
}
LEGEND = (
    ("parent", "Instruction-tuned"),
    ("mental-health", "Mental health"),
    ("medical", "Medical"),
    ("safety", "Safety"),
    ("pretrained", "Pretrained"),
)
# Same four buckets as normalize_version_for_plotting in
# compact_unified_facet_plot.py. Gemma 3n and Llama 3.1/3.2 are the fourth
# bucket (that file's internal 3.5, legend text "v3.1+"). Qwen uses the major
# version, so Qwen3.5 stays with Qwen3. Mistral and SmolLM were not on that
# figure: the two Mistral instruct releases are v1 and v2, and SmolLM2 is v2.
VERSION_BUCKET = {
    "Gemma 1": 1,
    "Gemma 3": 3,
    "Gemma 3n": 4,
    "Llama 3": 3,
    "Llama 3.1": 4,
    "Llama 3.2": 4,
    "Qwen2.5": 2,
    "Qwen3": 3,
    "Qwen3.5": 3,
    "Mistral 7B v0.2": 1,
    "Mistral 7B v0.3": 2,
    "SmolLM2": 2,
}
VERSION_MARKERS = {1: "o", 2: "s", 3: "^", 4: "D"}
VERSION_SIZE = {1: 60, 2: 100, 3: 140, 4: 180}
VERSION_LABELS = {1: "v1", 2: "v2", 3: "v3", 4: "v4"}
FAMILY_MARKERS = {
    "Qwen": "o",
    "Gemma": "s",
    "Llama": "^",
    "Mistral": "D",
    "SmolLM": "P",
}
# Same colors as the fine-tune-versus-parent figure. plot_figure3_delta imports this dict.
FAMILY_COLORS = {
    "Qwen": "#54A24B",
    "Gemma": "#E45756",
    "Llama": "#4C78A8",
    "Mistral": "#B279A2",
    "SmolLM": "#9D755D",
}
FAMILY_LABELS = {"Llama": "LLaMA"}
# "training" colors a point by fine-tune type. "family" colors it by model family.
# Marker shape is the model family either way. Figure 3 uses "family".
POINT_COLOR = "family"
FDR_ALPHA = 0.05
STAT_FIELDS = ["layout", "family", "task", "n", "slope", "r_squared", "p_value", "q_value", "significant"]


def _family_row(family: str) -> str:
    if family in ("Qwen", "Gemma", "Llama"):
        return family
    return "Other"


def _fdr_bh(p_values: list[float]) -> list[float]:
    """Benjamini-Hochberg q-values, clipped to 1, monotone in rank."""
    m = len(p_values)
    order = np.argsort(p_values)
    ranked = np.asarray(p_values, dtype=float)[order]
    adjusted = ranked * m / np.arange(1, m + 1)
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    adjusted = np.clip(adjusted, 0, 1)
    out = np.empty(m)
    out[order] = adjusted
    return out.tolist()


def _points(rows: list[dict] | None = None) -> list[dict]:
    """One point per roster row. rows replaces the roster read; None reads it.

    A caller that passes rows has already chosen the si_f1 and cssrs_f1 values.
    """
    from orchestration.study_roster import DRAW_PRETRAINED, for_analysis, load_roster, mhb_safety_ids

    if rows is None:
        rows = load_roster()
    rows = for_analysis(rows)
    on_mhb = mhb_safety_ids(rows)
    points = []
    for row in rows:
        if row["role"] == "pretrained" and not DRAW_PRETRAINED:
            continue
        if row["family"] not in FAMILY_MARKERS or row["family"] not in FAMILY_COLORS:
            raise SystemExit(f"{row['hf_id']} family {row['family']!r} has no marker or color")
        if row["version"] not in VERSION_BUCKET:
            raise SystemExit(f"{row['hf_id']} version {row['version']!r} has no v1–v4 bucket")
        if row["role"] == "pretrained":
            kind = "pretrained"
        elif row["role"] == "instruction parent":
            kind = "parent"
        else:
            kind = row["grouping"]
        if kind not in COLORS:
            raise SystemExit(f"{row['hf_id']} has no color for {kind}")
        slot = {
            "hf_id": row["hf_id"],
            "role": "parent" if row["role"] == "instruction parent" else row["role"],
            "grouping": row["grouping"],
            "family": row["family"],
            "row": _family_row(row["family"]),
            "version": row["version"],
            "size": row["size"],
            "kind": kind,
            "version_bucket": VERSION_BUCKET[row["version"]],
            "scores": {
                "synthetic_si": float(row["si_f1"]) if row["si_f1"] else None,
                "cssrs": float(row["cssrs_f1"]) if row["cssrs_f1"] else None,
                "mentalhealthbench": (
                    float(row["mhb_safety"]) * 100
                    if row["hf_id"] in on_mhb and row["mhb_safety"]
                    else None
                ),
            },
        }
        slot["billions"], _effective = _param_billions(slot)
        points.append(slot)
    return points


def _fit(xs: np.ndarray, ys: np.ndarray) -> dict | None:
    mask = np.isfinite(xs) & np.isfinite(ys) & (xs > 0)
    x = xs[mask]
    y = ys[mask]
    if len(x) < 3 or np.allclose(np.log2(x), np.log2(x)[0]):
        return None
    logx = np.log2(x)
    slope, intercept, r_value, p_value, _std_err = stats.linregress(logx, y)
    n = len(x)
    y_hat = slope * logx + intercept
    se = np.sqrt(np.sum((y - y_hat) ** 2) / (n - 2))
    grid = np.linspace(logx.min(), logx.max(), 100)
    y_line = slope * grid + intercept
    x_mean = float(np.mean(logx))
    x_var = float(np.sum((logx - x_mean) ** 2))
    se_pred = se * np.sqrt(1 / n + (grid - x_mean) ** 2 / x_var)
    t_critical = stats.t.ppf(0.975, n - 2)
    return {
        "x": 2 ** grid,
        "y": y_line,
        "lo": y_line - t_critical * se_pred,
        "hi": y_line + t_critical * se_pred,
        "n": n,
        "slope": slope,
        "r_squared": r_value ** 2,
        "p_value": p_value,
    }


# Doubling ticks from 135 million through 32 billion, the study range.
PARAM_TICKS = (0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32)


def _param_tick(value: float, _pos: int) -> str:
    if value >= 1:
        return f"{value:.0f}"
    return f"{value:g}"


def _style_panel(ax, task: str, title: str | None, ylabel: str | None) -> None:
    ax.set_xscale("log", base=2)
    ax.set_xlim(0.1, 40)
    ax.xaxis.set_major_locator(FixedLocator(PARAM_TICKS))
    ax.xaxis.set_major_formatter(FuncFormatter(_param_tick))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.set_ylim(0, 40 if task == "mentalhealthbench" else 1)
    if title:
        ax.set_title(title, fontsize=12, fontweight="bold")
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=11, fontweight="bold")
    ax.grid(True, alpha=0.3, linewidth=0.5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def _point_color(point: dict, color_by: str) -> str:
    if color_by == "training":
        return COLORS[point["kind"]]
    if color_by == "family":
        return FAMILY_COLORS[point["family"]]
    raise SystemExit(f"unknown point color {color_by}")


def _scatter(ax, drawn: list[dict], task: str, by_version: bool, marker_size: float = 46, color_by: str = "training") -> None:
    for point in drawn:
        bucket = point["version_bucket"]
        ax.scatter(
            [point["billions"]],
            [point["scores"][task]],
            s=VERSION_SIZE[bucket] if by_version else marker_size,
            marker=VERSION_MARKERS[bucket] if by_version else FAMILY_MARKERS[point["family"]],
            color=_point_color(point, color_by),
            alpha=0.85 if color_by == "family" else 0.35,
            linewidths=0,
            edgecolors="none",
            zorder=3,
        )


def _draw_lines(pending: list[tuple], layout: str) -> list[dict]:
    q_values = _fdr_bh([fit["p_value"] for _ax, _family, _task, fit in pending])
    records = []
    for (ax, family, task, fit), q_value in zip(pending, q_values):
        significant = q_value < FDR_ALPHA
        ax.fill_between(fit["x"], fit["lo"], fit["hi"], color="#333333", alpha=0.12, linewidth=0, zorder=1)
        ax.plot(
            fit["x"],
            fit["y"],
            color="#333333",
            linewidth=1.8,
            linestyle="-" if significant else ":",
            alpha=0.75,
            zorder=2,
        )
        q_text = "q < 0.0001" if q_value < 0.0001 else f"q = {q_value:.4f}"
        ax.text(
            0.05,
            0.95,
            f"R² = {fit['r_squared']:.3f}\n{q_text}",
            transform=ax.transAxes,
            fontsize=11,
            verticalalignment="top",
            horizontalalignment="left",
        )
        records.append(
            {
                "layout": layout,
                "family": family,
                "task": task,
                "n": fit["n"],
                "slope": fit["slope"],
                "r_squared": fit["r_squared"],
                "p_value": fit["p_value"],
                "q_value": q_value,
                "significant": significant,
            }
        )
    return records


def legend_entries() -> tuple[tuple[str, str], ...]:
    """Legend rows actually drawn. The pretrained entry returns with DRAW_PRETRAINED."""
    from orchestration.study_roster import DRAW_PRETRAINED

    if DRAW_PRETRAINED:
        return LEGEND
    return tuple(item for item in LEGEND if item[0] != "pretrained")


def _type_handles() -> list[Line2D]:
    return [
        Line2D([0], [0], marker="o", color=COLORS[key], linestyle="None", markersize=8, label=label)
        for key, label in legend_entries()
    ]


def _line_handles() -> list[Line2D]:
    return [
        Line2D([0], [0], color="#333333", linewidth=1.8, linestyle="-", label="q < 0.05"),
        Line2D([0], [0], color="#333333", linewidth=1.8, linestyle=":", label="q ≥ 0.05"),
    ]


def _family_figure(points: list[dict]) -> list[dict]:
    fig, axes = plt.subplots(len(ROWS), len(COLUMNS), figsize=(11.2, 11.2), sharex=True)
    pending = []
    for i, family in enumerate(ROWS):
        block = [p for p in points if p["row"] == family]
        for j, (task, title) in enumerate(COLUMNS):
            ax = axes[i, j]
            drawn = [p for p in block if p["scores"].get(task) is not None]
            _scatter(ax, drawn, task, by_version=True)
            fit = _fit(
                np.array([p["billions"] for p in drawn], dtype=float),
                np.array([p["scores"][task] for p in drawn], dtype=float),
            )
            if fit:
                pending.append((ax, family, task, fit))
            _style_panel(ax, task, title if i == 0 else None, family if j == 0 else None)
    for ax in axes[-1]:
        ax.set_xlabel("Parameters (billions)", fontweight="bold")
    records = _draw_lines(pending, "by_family")
    version_handles = [
        Line2D(
            [0],
            [0],
            marker=VERSION_MARKERS[bucket],
            color="gray",
            linestyle="None",
            markersize=np.sqrt(VERSION_SIZE[bucket]) * 0.55,
            label=VERSION_LABELS[bucket],
        )
        for bucket in (1, 2, 3, 4)
    ]
    fig.tight_layout(rect=(0, 0.10, 1, 1))
    fig.legend(handles=_type_handles(), loc="upper center", ncol=5, frameon=False, bbox_to_anchor=(0.5, 0.075))
    fig.legend(
        handles=version_handles,
        title="Model version",
        loc="upper center",
        ncol=4,
        frameon=False,
        bbox_to_anchor=(0.5, 0.035),
    )
    fig.savefig(OUT, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {OUT}")
    return records


def _combined_figure(points: list[dict]) -> list[dict]:
    fig, axes = plt.subplots(1, len(COLUMNS), figsize=(11.2, 4.6), sharex=True)
    pending = []
    for j, (task, title) in enumerate(COLUMNS):
        ax = axes[j]
        drawn = [p for p in points if p["scores"].get(task) is not None]
        _scatter(ax, drawn, task, by_version=False, marker_size=32)
        fit = _fit(
            np.array([p["billions"] for p in drawn], dtype=float),
            np.array([p["scores"][task] for p in drawn], dtype=float),
        )
        if fit:
            pending.append((ax, "all", task, fit))
        _style_panel(ax, task, title, None)
        ax.set_xlabel("Parameters (billions)", fontweight="bold")
    records = _draw_lines(pending, "all")
    family_handles = [
        Line2D(
            [0],
            [0],
            marker=FAMILY_MARKERS[name],
            color="gray",
            linestyle="None",
            markersize=8,
            label=name,
        )
        for name in FAMILY_MARKERS
    ]
    fig.tight_layout(rect=(0, 0.16, 1, 1))
    fig.legend(handles=_type_handles(), loc="upper center", ncol=5, frameon=False, bbox_to_anchor=(0.5, 0.12))
    fig.legend(
        handles=family_handles,
        title="Model family",
        loc="upper center",
        ncol=5,
        frameon=False,
        bbox_to_anchor=(0.5, 0.055),
    )
    fig.savefig(OUT_ALL, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {OUT_ALL}")
    return records


def _family_handles(colored: bool = False) -> list[Line2D]:
    return [
        Line2D(
            [0],
            [0],
            marker=FAMILY_MARKERS[name],
            color=FAMILY_COLORS[name] if colored else "gray",
            linestyle="None",
            markersize=8,
            label=FAMILY_LABELS.get(name, name),
        )
        for name in FAMILY_MARKERS
    ]


def _place_type_legends(ax, color_by: str) -> None:
    """Legends in the empty Safety × MHB-Safety panel.

    Training-type color keeps the type key and a gray family-shape key.
    Family color drops the type key: the row label already names the type.
    """
    ax.set_axis_off()
    style = dict(frameon=False, fontsize=10, title_fontsize=11, borderaxespad=0.0)
    if color_by == "training":
        training = ax.legend(
            handles=_type_handles(),
            title="Training type",
            loc="upper left",
            bbox_to_anchor=(0.0, 1.02),
            **style,
        )
        ax.add_artist(training)
        family = ax.legend(
            handles=_family_handles(False),
            title="Model family",
            loc="upper left",
            bbox_to_anchor=(0.50, 1.02),
            **style,
        )
        ax.add_artist(family)
    elif color_by == "family":
        family = ax.legend(
            handles=_family_handles(True),
            title="Model family",
            loc="upper left",
            bbox_to_anchor=(0.0, 1.02),
            **style,
        )
        ax.add_artist(family)
        ax.legend(
            handles=_line_handles(),
            title="Line",
            loc="upper left",
            bbox_to_anchor=(0.55, 1.02),
            **style,
        )
        return
    else:
        raise SystemExit(f"unknown point color {color_by}")
    ax.legend(
        handles=_line_handles(),
        title="Line",
        loc="lower left",
        bbox_to_anchor=(0.0, -0.02),
        **style,
    )


def _type_figure(points: list[dict], dest: Path | None = None, color_by: str | None = None) -> list[dict]:
    """One row per training type. Marker shape is the model family.

    Color follows color_by, or POINT_COLOR when that argument is omitted.
    Safety has no MHB-Safety score, so that panel holds the legends.
    """
    color_by = POINT_COLOR if color_by is None else color_by
    legend = legend_entries()
    fig, axes = plt.subplots(len(legend), len(COLUMNS), figsize=(11.2, 2.35 * len(legend)), sharex=True)
    pending = []
    legend_ax = None
    for i, (kind, label) in enumerate(legend):
        block = [p for p in points if p["kind"] == kind]
        for j, (task, title) in enumerate(COLUMNS):
            ax = axes[i, j]
            if kind == "safety" and task == "mentalhealthbench":
                legend_ax = ax
                continue
            drawn = [p for p in block if p["scores"].get(task) is not None]
            _scatter(ax, drawn, task, by_version=False, color_by=color_by)
            if not drawn:
                ax.text(0.5, 0.5, "Not run", transform=ax.transAxes, ha="center", va="center", color="#666666")
            fit = _fit(
                np.array([p["billions"] for p in drawn], dtype=float),
                np.array([p["scores"][task] for p in drawn], dtype=float),
            )
            if fit:
                pending.append((ax, label, task, fit))
            _style_panel(ax, task, title if i == 0 else None, label if j == 0 else None)
    if legend_ax is None:
        raise SystemExit("the training-type figure has no Safety × MHB-Safety panel for the legends")
    for ax in axes[-1]:
        if ax is legend_ax:
            continue
        ax.set_xlabel("Parameters (billions)", fontweight="bold")
    records = _draw_lines(pending, "by_type")
    _place_type_legends(legend_ax, color_by)
    fig.tight_layout()
    out = dest or OUT_TYPE
    fig.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {out}")
    return records


# Named releases on the version figure. Gemma 3n is drawn in the next slot
# after Gemma 3. Mistral and SmolLM are omitted: v0.3 extends the v0.2
# vocabulary from 32,000 to 32,768 tokens, and SmolLM2 is the only SmolLM release.
# "violin" or "box". The median line for a release with two models stays either way.
VERSION_SUMMARY = "violin"
VERSION_FACET = (
    ("Gemma", (("Gemma 1", "v1"), ("Gemma 3", "v3"), ("Gemma 3n", "v3n"))),
    ("Llama", (("Llama 3", "v3"), ("Llama 3.1", "v3.1"), ("Llama 3.2", "v3.2"))),
    ("Qwen", (("Qwen2.5", "v2.5"), ("Qwen3", "v3"), ("Qwen3.5", "v3.5"))),
)


KIND_MARKERS = {"parent": "o", "mental-health": "s", "medical": "^", "safety": "D"}


def _version_groups(block: list[dict], family: str, versions, task: str) -> list[list[float]]:
    groups = []
    for version, _tick in versions:
        scores = [p["scores"][task] for p in block if p["version"] == version]
        if scores:
            groups.append(scores)
    return groups


def _version_marks(kept: list[dict]) -> dict[tuple[str, str], str]:
    """Kruskal-Wallis q across the nine family-by-task panels, as on Figure 2."""
    pending = []
    for task, _title in COLUMNS:
        for family, versions in VERSION_FACET:
            block = [p for p in kept if p["family"] == family and p["scores"].get(task) is not None]
            if task == "mentalhealthbench":
                block = [p for p in block if p["kind"] != "safety"]
            groups = _version_groups(block, family, versions, task)
            if len(groups) < 2:
                raise SystemExit(f"{family} {task}: fewer than two versions to compare")
            _h, p_value = stats.kruskal(*groups)
            pending.append((family, task, p_value))
    q_values = _fdr_bh([p_value for _family, _task, p_value in pending])
    marks = {}
    for (family, task, _p), q_value in zip(pending, q_values):
        if q_value < 0.001:
            marks[(family, task)] = "***"
        elif q_value < 0.01:
            marks[(family, task)] = "**"
        elif q_value < 0.05:
            marks[(family, task)] = "*"
        else:
            marks[(family, task)] = "ns"
    return marks


def _version_bracket(ax, label: str, x0: float, x1: float) -> None:
    from matplotlib.transforms import blended_transform_factory

    transform = blended_transform_factory(ax.transData, ax.transAxes)
    y = 0.90
    drop = 0.035
    ax.plot(
        [x0, x0, x1, x1],
        [y - drop, y, y, y - drop],
        transform=transform,
        color="#333333",
        linewidth=1.05,
        solid_capstyle="butt",
        zorder=4,
        clip_on=False,
    )
    notable = label != "ns"
    ax.text(
        (x0 + x1) / 2,
        y + 0.012,
        label,
        transform=transform,
        ha="center",
        va="bottom",
        fontsize=14 if notable else 11,
        fontweight="bold" if notable else "regular",
        fontstyle="normal" if notable else "italic",
        color="#222222" if notable else "#666666",
        zorder=4,
        clip_on=False,
    )


def version_review_figure(points: list[dict], dest: Path) -> None:
    """One column per family and one row per task.

    The box or median line summarizes every model at that release. Color and
    marker are the training type. F1 and MHB-Safety stay on separate rows
    because they are not on the same scale.
    """
    families = [family for family, _versions in VERSION_FACET]
    shown = {"Llama": "LLaMA"}
    slots = {
        (family, version): index
        for family, versions in VERSION_FACET
        for index, (version, _label) in enumerate(versions)
    }
    kept = [p for p in points if p["family"] in families]
    missing = sorted({(p["family"], p["version"]) for p in kept if (p["family"], p["version"]) not in slots})
    if missing:
        raise SystemExit("no version slot for: " + "; ".join(f"{family} {version}" for family, version in missing))
    marks = _version_marks(kept)
    kinds = legend_entries()
    fig, axes = plt.subplots(len(COLUMNS), len(VERSION_FACET), figsize=(11.2, 8.4), sharey="row")
    rng = np.random.default_rng(0)
    for i, (task, title) in enumerate(COLUMNS):
        for j, (family, versions) in enumerate(VERSION_FACET):
            ax = axes[i, j]
            block = [p for p in kept if p["family"] == family and p["scores"].get(task) is not None]
            if task == "mentalhealthbench":
                block = [p for p in block if p["kind"] != "safety"]
            for version, _tick in versions:
                chosen = [p for p in block if p["version"] == version]
                if len(chosen) >= 3 and VERSION_SUMMARY == "box":
                    drawn = ax.boxplot(
                        [[p["scores"][task] for p in chosen]],
                        positions=[slots[(family, version)]],
                        widths=0.45,
                        patch_artist=True,
                        showfliers=False,
                        medianprops={"color": "black", "linewidth": 1.2},
                        whiskerprops={"color": "#666666"},
                        capprops={"color": "#666666"},
                        boxprops={"facecolor": "#dddddd", "edgecolor": "#666666"},
                    )
                    for box in drawn["boxes"]:
                        box.set_alpha(0.8)
                elif len(chosen) >= 3:
                    drawn = ax.violinplot(
                        [[p["scores"][task] for p in chosen]],
                        positions=[slots[(family, version)]],
                        widths=0.55,
                        showmeans=False,
                        showmedians=True,
                        showextrema=False,
                    )
                    for body in drawn["bodies"]:
                        body.set_facecolor((0.54, 0.54, 0.54, 0.35))
                        body.set_edgecolor((0.33, 0.33, 0.33, 0.75))
                        body.set_linewidth(0.8)
                        body.set_zorder(0)
                    drawn["cmedians"].set_color("#222222")
                    drawn["cmedians"].set_linewidth(1.4)
                    drawn["cmedians"].set_zorder(2)
                elif len(chosen) == 2:
                    median = float(np.median([p["scores"][task] for p in chosen]))
                    center = slots[(family, version)]
                    ax.plot([center - 0.18, center + 0.18], [median, median], color="black", linewidth=1.4, zorder=2)
            for version, _tick in versions:
                at_version = [p for p in block if p["version"] == version]
                # Tight when a release has a few models; wider, but still inside the box, when it has many.
                half = 0.08 if len(at_version) <= 3 else min(0.18, 0.08 + 0.012 * (len(at_version) - 3))
                for point in at_version:
                    ax.scatter(
                        [slots[(point["family"], point["version"])] + float(rng.uniform(-half, half))],
                        [point["scores"][task]],
                        s=28,
                        marker=KIND_MARKERS[point["kind"]],
                        color=COLORS[point["kind"]],
                        alpha=0.9,
                        linewidths=0,
                        zorder=3,
                    )
            _style_panel(ax, task, shown.get(family, family) if i == 0 else None, title if j == 0 else None)
            ax.set_xscale("linear")
            ax.set_xticks(range(len(versions)))
            ax.set_xticklabels([label for _version, label in versions], fontsize=10)
            ax.set_xlim(-0.7, len(versions) - 0.3)
            _version_bracket(ax, marks[(family, task)], 0, len(versions) - 1)
        top = 40 if task == "mentalhealthbench" else 1
        axes[i, 0].set_ylim(0, top / 0.90)
        axes[i, 0].set_yticks([0, 10, 20, 30, 40] if task == "mentalhealthbench" else [0, 0.2, 0.4, 0.6, 0.8, 1.0])
    handles = [
        Line2D([0], [0], marker=KIND_MARKERS[kind], color=COLORS[kind], linestyle="None", markersize=8, label=label)
        for kind, label in kinds
    ]
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False, fontsize=11, bbox_to_anchor=(0.5, 0.0))
    dest.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(dest, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {dest}")


def _score_heatmap() -> None:
    """Four family panels, cut to the three scores. Version stays inside a family."""
    import orchestration.plot_parse_rates as ppr

    saved = (ppr.COLUMNS, ppr.DATA_IN)
    ppr.COLUMNS = (
        ("si_f1", "F1", "Synthetic SI"),
        ("cssrs_f1", "F1", "Reddit C-SSRS"),
        ("mhb86", "Score", "MHB-Safety"),
    )
    ppr.DATA_IN = 1.45
    try:
        from orchestration.study_roster import plot_records

        records = plot_records()
        ppr._attach_objectives(records)
        ppr._attach_scope(records)
        by_family: dict[str, list[dict]] = {}
        for row in records:
            by_family.setdefault(row["family"], []).append(row)
        panels = [
            ("Qwen", ppr._one_parent_block(by_family["Qwen"])),
            ("Gemma", ppr._one_parent_block(by_family["Gemma"])),
            ("Llama", ppr._one_parent_block(by_family["Llama"])),
            (
                "Mistral and SmolLM",
                ppr._one_parent_block(by_family["Mistral"]) + ppr._one_parent_block(by_family["SmolLM"]),
            ),
        ]
        clashes = ppr._collisions([row for _name, block in panels for row in block])
        param_max = max(ppr._param_billions(row)[0] for _name, block in panels for row in block)
        mhb_max = ppr._mhb_scale_max(records)
        cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm = ppr._cmaps(param_max, mhb_max)
        grid = [panels[0:2], panels[2:4]]
        label_in = 4.05
        axes_w = 2 * ppr.META_IN + len(ppr.COLUMNS) * ppr.DATA_IN
        col_gap = 0.45
        top_in = 0.2
        title_in = 0.48
        row_gap = 0.4
        bot_in = 1.2
        right_in = 1.45
        row_slot = [max(len(block) for _name, block in row) * ppr.ROW_IN for row in grid]
        fig_w = 2 * (label_in + axes_w) + col_gap + right_in
        fig_h = top_in + sum(title_in + slot for slot in row_slot) + row_gap + bot_in
        fig = plt.figure(figsize=(fig_w, fig_h))
        axes = []
        blocks = []
        y_top = fig_h - top_in
        for row_index, row in enumerate(grid):
            y_top -= title_in
            for col_index, (name, block) in enumerate(row):
                height = len(block) * ppr.ROW_IN
                x = col_index * (label_in + axes_w + col_gap) + label_in
                y = y_top - height
                ax = fig.add_axes((x / fig_w, y / fig_h, axes_w / fig_w, height / fig_h))
                ppr._paint(ax, block, clashes, cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm)
                n_ft = sum(1 for item in block if item["role"] == "fine-tune")
                ax.set_title(f"{name}    {n_ft} fine-tunes", fontsize=13, loc="left", pad=8, fontweight="bold")
                axes.append(ax)
                blocks.append(block)
            y_top -= row_slot[row_index] + row_gap
        ppr._place_version_labels(fig, axes, blocks)
        span_y0 = min(ax.get_position().y0 for ax in axes)
        span_y1 = max(ax.get_position().y1 for ax in axes)
        span = span_y1 - span_y0
        bar_h = span * 0.28
        right = max(ax.get_position().x1 for ax in axes)
        cax = fig.add_axes([right + 0.012, span_y0 + bar_h + span * 0.06, 0.012, bar_h])
        f1_bar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax)
        f1_bar.set_label("F1, percent", fontsize=9)
        mhb_ax = fig.add_axes([right + 0.012, span_y0, 0.012, bar_h])
        mhb_bar = fig.colorbar(plt.cm.ScalarMappable(norm=mhb_norm, cmap=mhb_cmap), cax=mhb_ax)
        mhb_bar.set_label("MentalHealthBench", fontsize=9)
        handles = [
            plt.Rectangle((0, 0), 1, 1, facecolor=ppr.TYPE_COLOR[key], edgecolor="none", label=label)
            for key, label in ppr.type_legend()
        ]
        handles.append(
            plt.Rectangle((0, 0), 1, 1, facecolor="#f3f3f3", edgecolor="#8d8d8d", hatch="///", label="Not run")
        )
        fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.45, 0.012))
        fig.savefig(OUT_HEAT, dpi=120, facecolor="white")
        plt.close(fig)
        print(f"wrote {OUT_HEAT}")
    finally:
        ppr.COLUMNS, ppr.DATA_IN = saved


def main() -> None:
    points = _points()
    records = _family_figure(points) + _type_figure(points)
    _score_heatmap()
    with STATS.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=STAT_FIELDS)
        writer.writeheader()
        writer.writerows(records)
    print(f"wrote {STATS}")
    for row in records:
        print(
            f"  {row['layout']:<10} {row['family']:<8} {row['task']:<20} n={row['n']:<3} "
            f"R²={row['r_squared']:.3f} p={row['p_value']:.4f} q={row['q_value']:.4f}"
        )


if __name__ == "__main__":
    main()
