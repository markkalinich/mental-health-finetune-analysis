#!/usr/bin/env python3
"""Strict first-line parse rate against replies Sonnet has already labeled.

One point is one model. The x-axis is the share of replies whose first line is
yes or no, with the safety-card labels counted for the nine usable safety
models. The y-axis is the permissive rate: that strict share, plus replies
that fail it and that an existing Sonnet file labels answered_yes or
answered_no. A strict failure with no Sonnet label stays out of the y-axis,
so the permissive rate is at least the strict rate and is short of the rate
a full Sonnet read would give. The labels are replies/lenient-parse-pilot/labels-current.jsonl,
written by orchestration/consolidate_sonnet_labels.py.
"""
from __future__ import annotations

import csv
import sqlite3
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from scipy import stats

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from orchestration.plot_params_vs_score import (
    COLORS,
    FAMILY_MARKERS,
    legend_entries,
    _fdr_bh,
    _points,
)
from orchestration.plot_parse_rates import CACHE_DB
from orchestration.plot_spaghetti_delta import _violin
from orchestration.yesno_decision_review import failure_id, format_parsed, _message_text

# The 1.0 tick sits lower than on figure 3, and the bracket sits higher,
# because almost every model is piled on 1.0 and a tight bracket touches that pile.
S4_TOP_TICK_FRACTION = 0.78
S4_BRACKET_Y = 0.97

SI_PROMPT = "suicide_ideation_yesno_v2"
CSSRS_DIR = REPO / "replies/cssrs-yesno-v5"
# Standalone default. publish_manuscript_figures sets OUT into the dated figure folder.
OUT = REPO / "outputs/cross-grouping/model_performance/sonnet-recovery.png"
OUT_TESTS = OUT.with_name("figure-s4-tests.csv")
OUT_CSV = OUT.with_name("figure-s4-points.csv")
TASKS = (
    ("si", "Synthetic SI"),
    ("cssrs", "Reddit C-SSRS"),
)
ANSWERED = {"answered_yes", "answered_no"}



def _type_only_handles() -> list[Line2D]:
    return [
        Line2D([0], [0], marker="o", color=COLORS[key], linestyle="None", markersize=8, label=label)
        for key, label in legend_entries()
    ]


def _labels() -> dict[str, str]:
    """Sonnet labels, from replies/lenient-parse-pilot/labels-current.jsonl only.

    orchestration/consolidate_sonnet_labels.py writes that file and names the
    stored files it merges. This figure and the roster fill read the same file.
    """
    from orchestration.consolidate_sonnet_labels import read_current

    return read_current()



def _rates(models: set[str], labels: dict[str, str]) -> dict[str, dict[str, dict]]:
    tallies: dict[str, dict[str, dict]] = {
        model: {
            task: {"n": 0, "strict": 0, "recovered": 0, "unlabeled": 0}
            for task, _title in TASKS
        }
        for model in models
    }
    seen: set[tuple[str, str]] = set()
    with sqlite3.connect(f"file:{CACHE_DB}?mode=ro", uri=True) as conn:
        rows = conn.execute(
            """
            SELECT ck.model_full_name, ck.input_hash, cr.raw_response
            FROM cache_keys ck
            JOIN cached_results cr ON ck.cache_id = cr.cache_id
            WHERE ck.prompt_name = ? AND cr.replicate_index = 0
            """,
            (SI_PROMPT,),
        )
        for name, digest, raw in rows:
            if name not in models:
                continue
            key = (name, digest)
            if key in seen:
                raise SystemExit(f"duplicate v2 cache row {name} {digest}")
            seen.add(key)
            _add(tallies[name]["si"], name, failure_id("si", name, digest), _message_text(raw), labels)
    for model in sorted(models):
        path = CSSRS_DIR / model.replace("/", "__") / "predictions.csv"
        if not path.is_file():
            raise SystemExit(f"{model} has no C-SSRS file {path}")
        with path.open(encoding="utf-8", newline="") as handle:
            for index, record in enumerate(csv.DictReader(handle)):
                _add(
                    tallies[model]["cssrs"],
                    model,
                    failure_id("cssrs", model, str(index)),
                    record.get("raw_response") or "",
                    labels,
                )
    for model, tasks in tallies.items():
        if tasks["si"]["n"] != 450:
            raise SystemExit(f"{model} synthetic SI has n={tasks['si']['n']}")
        if tasks["cssrs"]["n"] != 500:
            raise SystemExit(f"{model} C-SSRS has n={tasks['cssrs']['n']}")
    return tallies


def _add(tally: dict, model: str, rid: str, text: str, labels: dict[str, str]) -> None:
    tally["n"] += 1
    if format_parsed(model, text):
        tally["strict"] += 1
        return
    label = labels.get(rid)
    if label in ANSWERED:
        tally["recovered"] += 1
    elif label is None:
        tally["unlabeled"] += 1


def _s4_bracket(ax, label: str) -> None:
    from matplotlib.transforms import blended_transform_factory

    transform = blended_transform_factory(ax.transData, ax.transAxes)
    drop = 0.028
    ax.plot(
        [0, 0, 1, 1],
        [S4_BRACKET_Y - drop, S4_BRACKET_Y, S4_BRACKET_Y, S4_BRACKET_Y - drop],
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
        S4_BRACKET_Y + 0.012,
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


def _s4_violin(ax, left: list[float], right: list[float]) -> None:
    """Same violin as figure 3, with the density cut off at 0 and 1.

    The kernel estimate otherwise runs past 1.0 and into the bracket.
    """
    _violin(ax, left, right)
    for body in ax.collections:
        if body.get_zorder() != 0:
            continue
        for path in body.get_paths():
            path.vertices[:, 1] = np.clip(path.vertices[:, 1], 0.0, 1.0)


def _spaghetti(points: list[dict]) -> None:
    """One line per model, strict yes/no on the left and the Sonnet read on the right.

    The violin is the distribution at each side. The bracket is a paired t-test
    of the two rates, with a Benjamini-Hochberg q-value across the two tasks.
    """
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.4), sharey=True)
    pending = []
    for ax, (task, title) in zip(axes, TASKS):
        strict = [point["rates"][task]["strict"] for point in points]
        permissive = [point["rates"][task]["permissive"] for point in points]
        _s4_violin(ax, strict, permissive)
        if len(points) >= 2:
            _stat, p_value = stats.ttest_rel(permissive, strict)
            pending.append(
                (
                    ax,
                    task,
                    len(points),
                    float(p_value),
                    float(np.mean(np.asarray(permissive) - np.asarray(strict))),
                )
            )
        for point in points:
            rate = point["rates"][task]
            moved = rate["permissive"] > rate["strict"] + 1e-12
            ax.plot(
                [0, 1],
                [rate["strict"], rate["permissive"]],
                color=COLORS[point["kind"]],
                alpha=0.55 if moved else 0.18,
                linewidth=1.15 if moved else 0.8,
                zorder=3 if moved else 1,
            )
            ax.scatter(
                [0, 1],
                [rate["strict"], rate["permissive"]],
                s=18,
                color=COLORS[point["kind"]],
                alpha=0.55 if moved else 0.25,
                linewidths=0,
                edgecolors="none",
                zorder=4 if moved else 2,
            )
        ax.set_xlim(-0.7, 1.7)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Strict yes/no", "Sonnet-interpreted"], fontsize=12)
        ax.tick_params(axis="y", labelsize=11, labelleft=True)
        ax.set_title(title, fontsize=12, fontweight="bold", pad=28)
        ax.grid(True, axis="y", alpha=0.3, linewidth=0.5)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    for ax in axes:
        ax.set_ylim(0, 1 / S4_TOP_TICK_FRACTION)
        ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
        ax.spines["left"].set_bounds(0, 1)
    axes[0].set_ylabel("Parse success", fontsize=12)
    q_values = _fdr_bh([item[3] for item in pending])
    tests = []
    for (ax, task, n, p_value, mean), q_value in zip(pending, q_values):
        if q_value < 0.001:
            mark = "***"
        elif q_value < 0.01:
            mark = "**"
        elif q_value < 0.05:
            mark = "*"
        else:
            mark = "ns"
        _s4_bracket(ax, mark)
        tests.append(
            {
                "task": task,
                "n": n,
                "mean_delta": mean,
                "p_value": p_value,
                "q_value": q_value,
                "significant": q_value < 0.05,
            }
        )
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.legend(
        handles=_type_only_handles(),
        loc="lower center",
        ncol=5,
        frameon=False,
        fontsize=11,
        bbox_to_anchor=(0.5, 0.0),
    )
    fig.savefig(OUT, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    with OUT_TESTS.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["task", "n", "mean_delta", "p_value", "q_value", "significant"],
        )
        writer.writeheader()
        writer.writerows(tests)
    print(f"wrote {OUT}")
    print(f"wrote {OUT_TESTS}")
    for row in tests:
        print(
            f"  {row['task']} n={row['n']} mean={row['mean_delta']:+.4f} "
            f"p={row['p_value']:.4g} q={row['q_value']:.4g}"
        )


def main(keep: set[str] | None = None) -> None:
    meta = {
        point["hf_id"]: point
        for point in _points()
        if keep is None or point["hf_id"] in keep
    }
    labels = _labels()
    tallies = _rates(set(meta), labels)
    points = []
    for model, point in meta.items():
        rates = {}
        for task, _title in TASKS:
            tally = tallies[model][task]
            rates[task] = {
                "strict": tally["strict"] / tally["n"],
                "permissive": (tally["strict"] + tally["recovered"]) / tally["n"],
                "unlabeled": tally["unlabeled"],
                "n": tally["n"],
            }
        points.append({**point, "rates": rates})
    _spaghetti(points)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["hf_id", "kind", "family", "task", "n", "strict", "permissive", "unlabeled_failures"]
        )
        for point in points:
            for task, _title in TASKS:
                rate = point["rates"][task]
                if rate["permissive"] + 1e-9 < rate["strict"]:
                    raise SystemExit(f"{point['hf_id']} {task} permissive is below strict")
                writer.writerow(
                    [
                        point["hf_id"],
                        point["kind"],
                        point["family"],
                        task,
                        rate["n"],
                        f"{rate['strict']:.6f}",
                        f"{rate['permissive']:.6f}",
                        rate["unlabeled"],
                    ]
                )
    unlabeled = sum(point["rates"][task]["unlabeled"] for point in points for task, _title in TASKS)
    print(f"wrote {OUT_CSV}")
    print(f"models {len(points)}  unlabeled strict failures {unlabeled}")


if __name__ == "__main__":
    main()
