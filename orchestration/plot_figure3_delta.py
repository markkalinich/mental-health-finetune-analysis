#!/usr/bin/env python3
"""Change from each fine-tune to its instruction-tuned parent.

One panel per study score. Inside a panel, one box for mental-health,
medical, and safety fine-tunes. Every fine-tune of that type is a point,
including Mistral and SmolLM. The point is the fine-tune's score minus its
parent's score. A mark above a box means the paired t-test has a
Benjamini-Hochberg q-value below 0.05 across the boxes in this figure.
Safety models have no MentalHealthBench score.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from scipy import stats

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

import orchestration.plot_parse_rates as ppr
from orchestration.plot_params_vs_score import COLORS, FAMILY_COLORS, FAMILY_MARKERS, _fdr_bh
OUT = REPO / "outputs/cross-grouping/model_performance/delta-by-type.png"
PAIRS = OUT.with_name("delta-by-type-pairs.csv")
TESTS = OUT.with_name("delta-by-type-tests.csv")

TYPES = (
    ("mental-health", "Mental health"),
    ("medical", "Medical"),
    ("safety", "Safety"),
)
COLUMNS = (
    ("synthetic_si", "Synthetic SI (F1)", "Change in F1"),
    ("cssrs", "Reddit C-SSRS (F1)", "Change in F1"),
    ("mentalhealthbench", "MentalHealthBench Score", "Change in score"),
)
def _value(record: dict, task: str) -> float | None:
    if task == "mentalhealthbench":
        score = record["scores"]["mhb"]
        if not score:
            return None
        return 100.0 * float(score["total"])
    score = record["scores"][task]
    if not score:
        return None
    return float(score["f1"])


def _pairs() -> list[dict]:
    from orchestration.study_roster import plot_records

    records = plot_records()
    parents = {record["hf_id"]: record for record in records if record["role"] == "parent"}
    rows = []
    for record in records:
        if record["role"] != "fine-tune":
            continue
        parent = parents.get(record["parent"])
        if parent is None:
            raise SystemExit(f"{record['hf_id']} has no parent row for {record['parent']}")
        if record["grouping"] not in COLORS:
            raise SystemExit(f"{record['hf_id']} grouping {record['grouping']!r} is not a fine-tune type")
        for task, _title, _ylabel in COLUMNS:
            child = _value(record, task)
            base = _value(parent, task)
            if child is None or base is None:
                continue
            rows.append(
                {
                    "hf_id": record["hf_id"],
                    "parent": record["parent"],
                    "family": record["family"],
                    "kind": record["grouping"],
                    "task": task,
                    "child": child,
                    "parent_score": base,
                    "delta": child - base,
                }
            )
    return rows


def main() -> None:
    pairs = _pairs()
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 5.2))
    pending = []
    rng = np.random.default_rng(42)
    for index, (task, title, ylabel) in enumerate(COLUMNS):
        ax = axes[index]
        ax.axhline(0, color="#888888", linestyle="--", linewidth=1.2, zorder=1)
        drawn_any = False
        for position, (kind, _label) in enumerate(TYPES):
            block = [row for row in pairs if row["task"] == task and row["kind"] == kind]
            if not block:
                continue
            drawn_any = True
            values = [row["delta"] for row in block]
            box = ax.boxplot(
                [values],
                positions=[position],
                widths=0.62,
                patch_artist=True,
                showfliers=False,
                medianprops={"color": "black", "linewidth": 1.6},
            )
            patch = box["boxes"][0]
            patch.set_facecolor(COLORS[kind])
            patch.set_alpha(0.35)
            patch.set_edgecolor(COLORS[kind])
            for row in block:
                ax.scatter(
                    [position + float(rng.uniform(-0.16, 0.16))],
                    [row["delta"]],
                    s=42,
                    marker=FAMILY_MARKERS[row["family"]],
                    color=FAMILY_COLORS[row["family"]],
                    edgecolors="white",
                    linewidths=0.4,
                    zorder=3,
                )
            if len(block) >= 2:
                _stat, p_value = stats.ttest_rel(
                    [row["child"] for row in block],
                    [row["parent_score"] for row in block],
                )
                pending.append((ax, position, max(values), task, kind, len(block), p_value, float(np.mean(values))))
        if not drawn_any:
            ax.text(0.5, 0.5, "Not run", transform=ax.transAxes, ha="center", va="center", color="#666666")
        ax.set_xlim(-0.6, 2.6)
        ax.set_xticks(range(len(TYPES)))
        tick_labels = []
        for kind, label in TYPES:
            n = sum(1 for row in pairs if row["task"] == task and row["kind"] == kind)
            tick_labels.append(f"{label}\nn = {n}" if n else f"{label}\nNot run")
        ax.set_xticklabels(tick_labels, fontsize=11)
        ax.set_title(title, fontsize=12, fontweight="bold")
        ax.set_ylabel(ylabel)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(True, axis="y", color="#eeeeee")
    q_values = _fdr_bh([item[6] for item in pending]) if pending else []
    tests = []
    for (ax, position, top, task, kind, n, p_value, mean), q_value in zip(pending, q_values):
        significant = q_value < 0.05
        if significant:
            mark = "***" if q_value < 0.001 else "**" if q_value < 0.01 else "*"
            span = ax.get_ylim()[1] - ax.get_ylim()[0]
            ax.text(position, top + 0.04 * span, mark, ha="center", va="bottom", fontsize=14, fontweight="bold")
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
    f1_deltas = [row["delta"] for row in pairs if row["task"] != "mentalhealthbench"]
    f1_pad = 0.14 * (max(f1_deltas) - min(f1_deltas))
    axes[0].set_ylim(min(f1_deltas) - f1_pad, max(f1_deltas) + f1_pad)
    axes[1].sharey(axes[0])
    mhb_deltas = [row["delta"] for row in pairs if row["task"] == "mentalhealthbench"]
    mhb_pad = 0.14 * (max(mhb_deltas) - min(mhb_deltas))
    axes[2].set_ylim(min(mhb_deltas) - mhb_pad, max(mhb_deltas) + mhb_pad)
    handles = [
        Line2D(
            [0],
            [0],
            marker=FAMILY_MARKERS[name],
            color=FAMILY_COLORS[name],
            linestyle="None",
            markersize=8,
            label=name,
        )
        for name in FAMILY_MARKERS
    ]
    fig.legend(handles=handles, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout()
    fig.savefig(OUT, dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    with PAIRS.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["hf_id", "parent", "family", "kind", "task", "child", "parent_score", "delta"],
        )
        writer.writeheader()
        writer.writerows(pairs)
    with TESTS.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["task", "kind", "n", "mean_delta", "p_value", "q_value", "significant"],
        )
        writer.writeheader()
        writer.writerows(tests)
    print(f"wrote {OUT}")
    print(f"wrote {PAIRS}")
    print(f"wrote {TESTS}")
    for row in tests:
        mark = "marked" if row["significant"] else "unmarked"
        print(
            f"  {row['task']:<20} {row['kind']:<16} n={row['n']:<3} "
            f"mean={row['mean_delta']:+.3f} p={row['p_value']:.4f} q={row['q_value']:.4f} {mark}"
        )


if __name__ == "__main__":
    main()
