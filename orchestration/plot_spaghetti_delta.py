#!/usr/bin/env python3
"""Parent on the left, fine-tune on the right, one line per fine-tune.

Rows are mental health, medical, and safety. The first two columns are the
full study scores. The MentalHealthBench column is the safety subset: the
task-clipped score on the English questions whose user message is suicide or
self-harm. The safety row has no point in that column.
Color is the model family. A transparent violin summarizes the scores at
each side. The left-hand points are the parents of the fine-tunes in that
cell, each parent once. A bracket over the two sides is the paired t-test of each fine-tune
against its parent. The label on the bracket is the Benjamini-Hochberg
q-value across the cells that have a test: *** below 0.001, ** below 0.01, * below 0.05,
and ns otherwise.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.transforms import blended_transform_factory
from scipy import stats

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

import orchestration.plot_parse_rates as ppr
from orchestration.plot_figure3_delta import COLUMNS, FAMILY_COLORS
from orchestration.plot_params_vs_score import FAMILY_MARKERS, _fdr_bh


OUT = REPO / "outputs/cross-grouping/model_performance/spaghetti-by-type.png"
TESTS = OUT.with_name("spaghetti-by-type-tests.csv")
ROWS = (("mental-health", "Mental health"), ("medical", "Medical"), ("safety", "Safety"))
SCOPE_MARKER = {"Q/LoRA": "^", "Full": "s", "Unstated": "D"}
SCOPE_LABEL = {"Q/LoRA": "Q/LoRA", "Full": "Full", "Unstated": "Unstated"}


# The top labeled tick sits at this fraction of every panel, and the bracket
# sits at one fraction above that, so the six brackets share a height.
# The 1.0 and 40 ticks sit at this fraction of the axes. The spine stops there.
# The bracket sits just above that tick, in the band the spine does not draw.
TOP_TICK_FRACTION = 0.90
BRACKET_AXES_Y = 0.945


def _bracket(ax, label: str) -> None:
    transform = blended_transform_factory(ax.transData, ax.transAxes)
    drop = 0.035
    ax.plot(
        [0, 0, 1, 1],
        [BRACKET_AXES_Y - drop, BRACKET_AXES_Y, BRACKET_AXES_Y, BRACKET_AXES_Y - drop],
        transform=transform,
        color="#333333",
        linewidth=1.05,
        solid_capstyle="butt",
        zorder=4,
        clip_on=False,
    )
    notable = label != "ns"
    ax.text(
        0.5,
        BRACKET_AXES_Y + 0.012,
        label,
        transform=transform,
        ha="center",
        va="bottom",
        fontsize=14 if notable else 12,
        fontweight="bold" if notable else "regular",
        fontstyle="normal" if notable else "italic",
        color="#222222" if notable else "#666666",
        zorder=4,
        clip_on=False,
    )


def _violin(ax, parent_scores: list[float], child_scores: list[float]) -> None:
    drawn = ax.violinplot(
        [parent_scores, child_scores],
        positions=[0, 1],
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



def _saved_pairs(rows: list[dict] | None = None) -> list[dict]:
    """Fine-tune versus the parent id on the roster.

    The listed parent_id is the parent. When that id is an Unsloth copy of a
    Google model, the copy is the same checkpoint as the Google model, and the
    score is the Google score. A missing score skips that point. F1 is stored
    as a proportion. The MentalHealthBench value is the 86-question subset,
    drawn on the 0–100 scale. rows replaces the roster read; None reads it.
    A caller that passes rows has already chosen the si_f1 and cssrs_f1 values.
    """
    from orchestration.joint_and_paired import canonical_checkpoint
    from orchestration.study_roster import load_roster

    if rows is None:
        rows = load_roster()
    ancestors = {row["hf_id"]: row for row in rows if row["role"] != "fine-tune"}
    score_of = {
        "synthetic_si": ("si_f1", 1.0),
        "cssrs": ("cssrs_f1", 1.0),
        "mentalhealthbench": ("mhb_safety", 100.0),
    }
    pairs = []
    for row in rows:
        if row["role"] != "fine-tune":
            continue
        listed = row["parent_id"]
        if listed not in ancestors:
            raise SystemExit(f"{row['hf_id']} parent {listed} is not on the roster")
        parent = ancestors.get(canonical_checkpoint(listed))
        if parent is None:
            raise SystemExit(
                f"{row['hf_id']} parent {listed} is the same checkpoint as "
                f"{canonical_checkpoint(listed)}, which is not on the roster"
            )
        for task, _title, _ylabel in COLUMNS:
            if row["grouping"] == "safety" and task == "mentalhealthbench":
                continue
            field, scale = score_of[task]
            if not row[field] or not parent[field]:
                continue
            child_score = float(row[field]) * scale
            parent_score = float(parent[field]) * scale
            pairs.append(
                {
                    "hf_id": row["hf_id"],
                    "parent": listed,
                    "checkpoint": parent["hf_id"],
                    "family": row["family"],
                    "kind": row["grouping"],
                    "task": task,
                    "child": child_score,
                    "parent_score": parent_score,
                    "delta": child_score - parent_score,
                }
            )
    return pairs


def _fine_tune_scope() -> dict[str, str]:
    """Weight-update code for every fine-tune on the roster."""
    from orchestration.study_roster import load_roster, scope_marker

    found: dict[str, str] = {}
    for row in load_roster():
        if row["role"] != "fine-tune":
            continue
        code = scope_marker(row["training_method"], row["hf_id"])
        if code is None:
            raise SystemExit(f"{row['hf_id']} training_method {row['training_method']!r} has no marker")
        previous = found.get(row["hf_id"])
        if previous is not None and previous != code:
            raise SystemExit(f"{row['hf_id']} has two weight-update codes")
        found[row["hf_id"]] = code
    return found


def main(rows: list[dict] | None = None) -> None:
    pairs = _saved_pairs(rows)
    scopes = _fine_tune_scope()
    for row in pairs:
        scope = scopes.get(row["hf_id"])
        if scope not in SCOPE_MARKER:
            raise SystemExit(f"{row['hf_id']} has no weight-update marker")
        row["scope"] = scope
    fig, axes = plt.subplots(3, 3, figsize=(11.6, 10.4), sharex=True, sharey="col")
    pending = []
    for i, (kind, row_label) in enumerate(ROWS):
        for j, (task, title, _ylabel) in enumerate(COLUMNS):
            ax = axes[i, j]
            block = [row for row in pairs if row["kind"] == kind and row["task"] == task]
            parents: dict[str, float] = {}
            families: dict[str, str] = {}
            for row in block:
                parents.setdefault(row["checkpoint"], row["parent_score"])
                families.setdefault(row["checkpoint"], row["family"])
            parent_scores = list(parents.values())
            child_scores = [row["child"] for row in block]
            if parent_scores and child_scores:
                _violin(ax, parent_scores, child_scores)
            if len(block) >= 2:
                _stat, p_value = stats.ttest_rel(
                    [row["child"] for row in block],
                    [row["parent_score"] for row in block],
                )
                pending.append(
                    (ax, task, kind, len(block), float(p_value), float(np.mean([row["delta"] for row in block])))
                )
            for row in block:
                color = FAMILY_COLORS[row["family"]]
                ax.plot(
                    [0, 1],
                    [row["parent_score"], row["delta"] + row["parent_score"]],
                    color=color,
                    alpha=0.35,
                    linewidth=1.0,
                    zorder=1,
                )
                ax.scatter(
                    [1],
                    [row["delta"] + row["parent_score"]],
                    s=42,
                    marker="o",
                    color=color,
                    edgecolors="white",
                    linewidths=0.3,
                    zorder=3,
                )
            for parent, score in parents.items():
                ax.scatter(
                    [0],
                    [score],
                    s=36,
                    marker="o",
                    color=FAMILY_COLORS[families[parent]],
                    edgecolors="white",
                    linewidths=0.3,
                    zorder=3,
                )
            ax.set_xlim(-0.55, 1.55)
            ax.set_xticks([0, 1])
            ax.set_xticklabels(["Instruction-tuned\n(Parent model)", "Fine-tune"], fontsize=13)
            ax.tick_params(axis="y", labelsize=12)
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            if i == 0:
                shown = "MHB-Safety" if task == "mentalhealthbench" else title
                ax.set_title(shown, fontsize=12, fontweight="bold", pad=18)
            if j == 0:
                ax.set_ylabel(row_label, fontsize=13)
    for column in range(3):
        if COLUMNS[column][0] == "mentalhealthbench":
            axes[0, column].set_ylim(0, 40 / TOP_TICK_FRACTION)
            axes[0, column].set_yticks([0, 10, 20, 30, 40])
            spine_top = 40
        else:
            axes[0, column].set_ylim(0, 1 / TOP_TICK_FRACTION)
            axes[0, column].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
            spine_top = 1
        for row in range(len(ROWS)):
            axes[row, column].set_ylim(axes[0, column].get_ylim())
            axes[row, column].spines["left"].set_bounds(0, spine_top)
    axes[ROWS.index(("safety", "Safety")), COLUMNS.index(("mentalhealthbench", "MentalHealthBench Score", "Change in score"))].set_visible(False)
    q_values = _fdr_bh([item[4] for item in pending])
    tests = []
    for (ax, task, kind, n, p_value, mean), q_value in zip(pending, q_values):
        significant = q_value < 0.05
        if q_value < 0.001:
            mark = "***"
        elif q_value < 0.01:
            mark = "**"
        elif q_value < 0.05:
            mark = "*"
        else:
            mark = "ns"
        _bracket(ax, mark)
        tests.append(
            {
                "task": task,
                "kind": kind,
                "n": n,
                "mean_delta": mean,
                "p_value": p_value,
                "q_value": q_value,
                "significant": significant,
            }
        )
    family_handles = [
        Line2D([0], [0], marker="o", color=FAMILY_COLORS[name], linestyle="None", markersize=8, label=name)
        for name in FAMILY_MARKERS
    ]
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.legend(
        handles=family_handles,
        loc="lower center",
        ncol=5,
        frameon=False,
        fontsize=13,
        bbox_to_anchor=(0.5, 0.02),
    )
    method_tests = []
    grouped: dict[tuple[str, str, str], list[dict]] = {}
    for row in pairs:
        grouped.setdefault((row["task"], row["kind"], row["scope"]), []).append(row)
    pending_method = []
    for key in sorted(grouped):
        block = grouped[key]
        if len(block) < 2:
            continue
        _stat, p_value = stats.ttest_rel(
            [row["child"] for row in block],
            [row["parent_score"] for row in block],
        )
        pending_method.append((key, len(block), float(p_value), float(np.mean([row["delta"] for row in block]))))
    method_q = _fdr_bh([item[2] for item in pending_method]) if pending_method else []
    for ((task, kind, scope), n, p_value, mean), q_value in zip(pending_method, method_q):
        method_tests.append(
            {
                "task": task,
                "kind": kind,
                "scope": scope,
                "n": n,
                "mean_delta": mean,
                "p_value": p_value,
                "q_value": q_value,
                "significant": q_value < 0.05,
            }
        )
    method_path = OUT.with_name(f"{OUT.stem}-method-tests.csv")
    with method_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["task", "kind", "scope", "n", "mean_delta", "p_value", "q_value", "significant"],
        )
        writer.writeheader()
        writer.writerows(method_tests)
    print(f"wrote {method_path}")
    contrasts = []
    pending_contrast = []
    for task, _title, _ylabel in COLUMNS:
        for kind, _label in ROWS:
            full = [row["delta"] for row in pairs if row["task"] == task and row["kind"] == kind and row["scope"] == "Full"]
            lora = [row["delta"] for row in pairs if row["task"] == task and row["kind"] == kind and row["scope"] == "Q/LoRA"]
            if len(full) < 2 or len(lora) < 2:
                continue
            _stat, p_value = stats.ttest_ind(full, lora, equal_var=False)
            pending_contrast.append(
                (task, kind, len(full), len(lora), float(np.mean(full) - np.mean(lora)), float(p_value))
            )
    contrast_q = _fdr_bh([item[5] for item in pending_contrast]) if pending_contrast else []
    for (task, kind, n_full, n_lora, mean, p_value), q_value in zip(pending_contrast, contrast_q):
        contrasts.append(
            {
                "task": task,
                "kind": kind,
                "n_full": n_full,
                "n_qlora": n_lora,
                "mean_full_minus_qlora": mean,
                "p_value": p_value,
                "q_value": q_value,
                "significant": q_value < 0.05,
            }
        )
    contrast_path = OUT.with_name(f"{OUT.stem}-method-contrast.csv")
    with contrast_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["task", "kind", "n_full", "n_qlora", "mean_full_minus_qlora", "p_value", "q_value", "significant"],
        )
        writer.writeheader()
        writer.writerows(contrasts)
    print(f"wrote {contrast_path}")
    for row in contrasts:
        print(
            f"  contrast {row['task']:<20} {row['kind']:<16} full {row['n_full']} qlora {row['n_qlora']} "
            f"mean={row['mean_full_minus_qlora']:+.3f} p={row['p_value']:.4f} q={row['q_value']:.4f}"
        )
    for row in method_tests:
        print(
            f"  {row['task']:<20} {row['kind']:<16} {row['scope']:<10} n={row['n']:<3} "
            f"mean={row['mean_delta']:+.3f} p={row['p_value']:.4f} q={row['q_value']:.4f}"
        )
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)
    with TESTS.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["task", "kind", "n", "mean_delta", "p_value", "q_value", "significant"],
        )
        writer.writeheader()
        writer.writerows(tests)
    print(f"wrote {OUT}")
    print(f"wrote {TESTS}")
    for row in tests:
        mark = "marked" if row["significant"] else "unmarked"
        print(
            f"  {row['task']:<20} {row['kind']:<16} n={row['n']:<3} "
            f"mean={row['mean_delta']:+.3f} p={row['p_value']:.4f} q={row['q_value']:.4f} {mark}"
        )


QLORA_FACE = "#1B4F72"
FULL_FACE = "#8C4A2F"
SFT_FACE = "#335C67"
OTHER_FACE = "#6D597A"


def _half_violin(ax, values: list[float], side: int, color: str) -> None:
    """One side of a split violin. side is -1 for the left half and +1 for the right."""
    if len(values) < 2:
        return
    drawn = ax.violinplot(
        [values],
        positions=[0],
        widths=0.85,
        showmeans=False,
        showmedians=False,
        showextrema=False,
    )
    lo, hi = min(values), max(values)
    body = drawn["bodies"][0]
    vertices = body.get_paths()[0].vertices
    if side < 0:
        vertices[:, 0] = np.minimum(vertices[:, 0], 0)
    else:
        vertices[:, 0] = np.maximum(vertices[:, 0], 0)
    if hi > lo:
        vertices[:, 1] = np.clip(vertices[:, 1], lo, hi)
    body.set_facecolor(color)
    body.set_edgecolor(color)
    body.set_alpha(0.38)
    body.set_linewidth(0.9)
    body.set_zorder(1)
    median = float(np.median(values))
    half = 0.20 * side
    ax.plot(
        [0, half],
        [median, median],
        color="#222222",
        linewidth=1.5,
        solid_capstyle="butt",
        zorder=3,
        clip_on=False,
    )


def _method_bracket(ax, label: str) -> None:
    transform = blended_transform_factory(ax.transData, ax.transAxes)
    drop = 0.035
    y = 0.90
    ax.plot(
        [-0.46, -0.46, 0.46, 0.46],
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
        0,
        y + 0.015,
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


OBJECTIVE_MARKER = {"SFT": "o", "GRPO": "^", "DPO": "s", "DIST": "D", "MULT": "P"}


def draw_split_delta(
    pairs: list[dict],
    out: Path,
    field: str,
    left: str,
    right: str,
    left_color: str,
    right_color: str,
    marker_field: str,
    markers: dict[str, str],
) -> None:
    """Fine-tune minus parent, one split violin per grouping and score.

    The left half is `left` and the right half is `right`, read from `field`.
    The bracket is the Welch test of the right half minus the left, with the
    Benjamini-Hochberg q across the panels that have at least two models on
    each side. A panel with fewer than two on a side has points and no bracket.
    """
    kept = []
    for row in pairs:
        side = row.get(field)
        if side not in (left, right):
            continue
        copied = dict(row)
        copied["side"] = side
        kept.append(copied)
    fig, axes = plt.subplots(3, 3, figsize=(11.2, 8.6))
    pending = []
    for i, (kind, row_label) in enumerate(ROWS):
        for j, (task, title, _ylabel) in enumerate(COLUMNS):
            ax = axes[i, j]
            block = [row for row in kept if row["kind"] == kind and row["task"] == task]
            halves = {
                name: sorted((row for row in block if row["side"] == name), key=lambda row: row["hf_id"])
                for name in (left, right)
            }
            _half_violin(ax, [row["delta"] for row in halves[left]], -1, left_color)
            _half_violin(ax, [row["delta"] for row in halves[right]], 1, right_color)
            ax.axhline(0, color="#888888", linewidth=0.8, zorder=0)
            ax.axvline(0, color="#dddddd", linewidth=0.6, zorder=0)
            for name, side in ((left, -1), (right, 1)):
                for index, row in enumerate(halves[name]):
                    frac = (index + 0.5) / max(len(halves[name]), 1)
                    code = row.get(marker_field)
                    if code not in markers:
                        raise SystemExit(f"{row['hf_id']} {marker_field} {code!r} has no shape")
                    ax.scatter(
                        [side * (0.08 + 0.20 * frac)],
                        [row["delta"]],
                        s=36,
                        marker=markers[code],
                        color=FAMILY_COLORS[row["family"]],
                        edgecolors="white",
                        linewidths=0.3,
                        zorder=4,
                    )
                ax.text(
                    0.22 if side < 0 else 0.78,
                    0.03,
                    f"n={len(halves[name])}",
                    transform=ax.transAxes,
                    ha="center",
                    va="bottom",
                    fontsize=9,
                    color="#444444",
                )
            if len(halves[left]) >= 2 and len(halves[right]) >= 2:
                left_delta = [row["delta"] for row in halves[left]]
                right_delta = [row["delta"] for row in halves[right]]
                _stat, p_value = stats.ttest_ind(right_delta, left_delta, equal_var=False)
                pending.append(
                    (
                        ax,
                        task,
                        kind,
                        len(left_delta),
                        len(right_delta),
                        float(np.mean(right_delta) - np.mean(left_delta)),
                        float(p_value),
                    )
                )
            ax.set_xlim(-0.7, 0.7)
            ax.set_xticks([])
            ax.tick_params(axis="y", labelsize=11)
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            if i == 0:
                shown = "MHB-Safety" if task == "mentalhealthbench" else title
                ax.set_title(shown + "\nFine-tune − parent", fontsize=12, fontweight="bold", pad=16)
            if j == 0:
                ax.set_ylabel(row_label, fontsize=12)
    q_values = _fdr_bh([item[6] for item in pending]) if pending else []
    contrasts = []
    for (ax, task, kind, n_left, n_right, mean, p_value), q_value in zip(pending, q_values):
        if q_value < 0.001:
            mark = "***"
        elif q_value < 0.01:
            mark = "**"
        elif q_value < 0.05:
            mark = "*"
        else:
            mark = "ns"
        _method_bracket(ax, mark)
        contrasts.append(
            {
                "task": task,
                "kind": kind,
                "left": left,
                "right": right,
                "n_left": n_left,
                "n_right": n_right,
                "mean_right_minus_left": mean,
                "p_value": p_value,
                "q_value": q_value,
                "significant": q_value < 0.05,
            }
        )
    for column, (task, _title, _ylabel) in enumerate(COLUMNS):
        deltas = [row["delta"] for row in kept if row["task"] == task]
        if not deltas:
            continue
        lo = min(0.0, min(deltas))
        hi = max(0.0, max(deltas))
        span = (hi - lo) or 1.0
        for row in range(len(ROWS)):
            axes[row, column].set_ylim(lo - 0.16 * span, hi + 0.38 * span)
    hidden = axes[
        ROWS.index(("safety", "Safety")),
        COLUMNS.index(("mentalhealthbench", "MentalHealthBench Score", "Change in score")),
    ]
    hidden.set_visible(False)
    split_handles = [
        Line2D([0], [0], marker="s", color=left_color, linestyle="None", markersize=10, label=left),
        Line2D([0], [0], marker="s", color=right_color, linestyle="None", markersize=10, label=right),
    ]
    used_markers = [code for code in markers if any(row.get(marker_field) == code for row in kept)]
    shape_handles = [
        Line2D([0], [0], marker=markers[code], color="#333333", linestyle="None", markersize=8, label=code)
        for code in used_markers
    ]
    family_handles = [
        Line2D([0], [0], marker="o", color=FAMILY_COLORS[name], linestyle="None", markersize=8, label=name)
        for name in FAMILY_MARKERS
    ]
    fig.tight_layout(rect=(0, 0.16, 1, 1))
    fig.legend(handles=split_handles, loc="lower center", ncol=2, frameon=False, fontsize=11, bbox_to_anchor=(0.28, 0.075))
    fig.legend(handles=shape_handles, loc="lower center", ncol=len(shape_handles), frameon=False, fontsize=11, bbox_to_anchor=(0.68, 0.075))
    fig.legend(handles=family_handles, loc="lower center", ncol=5, frameon=False, fontsize=11, bbox_to_anchor=(0.5, 0.015))
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=300, facecolor="white")
    plt.close(fig)
    stem = out.stem
    points_path = out.with_name(f"{stem}-points.csv")
    point_fields = ["hf_id", "parent", "family", "kind", "task", "side", "scope", "objective", "parent_score", "child", "delta"]
    if field not in point_fields:
        point_fields.insert(5, field)
    if marker_field not in point_fields:
        point_fields.insert(6, marker_field)
    with points_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=point_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(sorted(kept, key=lambda row: (row["task"], row["kind"], row["side"], row["hf_id"])))
    contrast_path = out.with_name(f"{stem}-tests.csv")
    with contrast_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "task", "kind", "left", "right", "n_left", "n_right",
                "mean_right_minus_left", "p_value", "q_value", "significant",
            ],
        )
        writer.writeheader()
        writer.writerows(contrasts)
    print(f"wrote {out}")
    print(f"wrote {points_path}")
    print(f"wrote {contrast_path}")
    for row in contrasts:
        print(
            f"  {row['task']:<20} {row['kind']:<16} {row['right']}−{row['left']} "
            f"n={row['n_left']}/{row['n_right']} mean={row['mean_right_minus_left']:+.3f} "
            f"p={row['p_value']:.4f} q={row['q_value']:.4f}"
        )


def write_method_objective_figures(dest: Path) -> None:
    """Figure S10 splits Q/LoRA from full. Figure S11 splits SFT from every other objective.

    Both use the roster the process just loaded, including the labeled filter
    when MANUSCRIPT_LABELED=1. The marker on S9 is the objective. The marker on
    S10 is the weight-update method.
    """
    from orchestration.study_roster import load_roster, objective_code

    figure_code = {
        "SFT": "SFT",
        "GRPO": "GRPO",
        "DPO": "DPO",
        "Distillation": "DIST",
        "More than one stage": "MULT",
    }
    codes = {
        row["hf_id"]: objective_code(row)
        for row in load_roster()
        if row["role"] == "fine-tune"
    }
    scopes = _fine_tune_scope()
    pairs = []
    for row in _saved_pairs():
        code = codes.get(row["hf_id"], "")
        if code not in figure_code:
            continue
        scope = scopes.get(row["hf_id"])
        if scope not in SCOPE_MARKER:
            raise SystemExit(f"{row['hf_id']} has no weight-update marker")
        copied = dict(row)
        copied["scope"] = scope
        copied["objective"] = figure_code[code]
        copied["objective_group"] = "SFT" if code == "SFT" else "Other"
        pairs.append(copied)
    dest.mkdir(parents=True, exist_ok=True)
    draw_split_delta(
        pairs, dest / "figure-s10.png", "scope", "Q/LoRA", "Full",
        QLORA_FACE, FULL_FACE, "objective", OBJECTIVE_MARKER,
    )
    draw_split_delta(
        pairs, dest / "figure-s11.png", "objective_group", "SFT", "Other",
        SFT_FACE, OTHER_FACE, "scope", SCOPE_MARKER,
    )


if __name__ == "__main__":
    main()
