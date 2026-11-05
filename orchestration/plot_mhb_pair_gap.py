#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Forest plot of mental-health fine-tune versus its instruction-tuned parent.

Reads Luna grades for the 100 English questions and kept.csv. Writes
pair-gap-forest.png, pair-gap-forest.pdf, and pair-gap-forest.csv under
replies/mentalhealthbench-english100/.

The task-clipped score is equation (2) in the MentalHealthBench paper: points
of criteria marked met, including penalties, divided by that question's
positive points, floored at 0. Axis rows are equation (4): positive points
earned on that axis, and penalty burden on that axis, each divided by the
question's total positive points and averaged over every question in the
acuity, including questions with no line on that axis.

On the figure, left of zero means the mental-health fine-tune is better and
right of zero means the instruction-tuned parent is better. For the score and
for positive points, better means a higher value. For penalty burden, better
means a lower burden.
"""
from __future__ import annotations

import csv
import math
import random
import statistics
import zlib
from collections import defaultdict
from pathlib import Path

import matplotlib
import sys

_REPO = Path(__file__).resolve().parents[1]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))
from config import datasets  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
_MH_RESULTS = ROOT / "outputs/funnel/mental-health"
KEPT = _MH_RESULTS / _MH_RESULTS.joinpath("CURRENT").read_text(encoding="utf-8").strip() / "kept.csv"
QUESTIONS = ROOT / "data/benchmarks/mentalhealthbench/english_100_fewest_criteria.csv"
EVAL = datasets.path("mentalhealthbench_eval")
GRADES = ROOT / "replies/mentalhealthbench-english100"
OUT_DIR = GRADES

# In kept.csv, and it serves, but this 100-question figure has no grade file for it yet.
SKIP_CHILDREN = {
    "SoufianeDahimi/child_trauma_gemma_finetune",
}

AXIS_LABEL = {
    "context_seeking_and_assessment": "Context seeking",
    "actionable_guidance_and_coping_strategies": "Actionable guidance",
    "empathy_emotional_attunement_and_support": "Empathy",
    "clinical_reasoning_and_health_accuracy": "Clinical accuracy",
    "over_alarmism_and_under_response": "Over-alarm / under-response",
    "interpretation_and_cognitive_reframing": "Reframing",
    "dual_use_refusals_and_harm_avoidance": "Harm avoidance",
    "unsupported_belief_and_reality_testing_calibration": "Reality testing",
    "collaboration_and_user_agency": "Agency",
    "communication_and_writing": "Communication",
}
# A row is drawn in a column only when that acuity has at least this many
# criteria of that sign. Fewer than two is one line, not an axis estimate.
MIN_CRITERIA = 2

ACUITY_ORDER = (
    ("high_acuity", "High acuity"),
    ("emergent", "Emergent"),
    ("non_acute", "Non-acute"),
)

BOOTSTRAP_DRAWS = 10000
SUMMARY_PANELS = {"score", "summary_positive", "summary_penalty"}


def t_crit(df: int) -> float:
    try:
        from scipy.stats import t
    except ImportError:
        if df != 20:
            raise SystemExit(f"scipy is required for a t interval with df={df}")
        return 2.086
    return float(t.ppf(0.975, df))


def mean_ci(values: list[float]) -> tuple[float, float, float, int]:
    n = len(values)
    if n == 0:
        raise SystemExit("a forest row has no pairs")
    mean = statistics.mean(values)
    if n < 2:
        return mean, mean, mean, n
    se = statistics.stdev(values) / math.sqrt(n)
    half = t_crit(n - 1) * se
    return mean, mean - half, mean + half, n


def load_jsonl(path: Path) -> list[dict]:
    import json

    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def question_parts(criteria: list[dict]) -> dict:
    """Task-clipped score and equation-(4) pieces for one graded reply."""
    positive = sum(row["points"] for row in criteria if row["points"] > 0)
    if positive <= 0:
        raise SystemExit("a question has no positive points")
    met_points = sum(row["points"] for row in criteria if row["satisfaction"] == 1)
    signed = met_points / positive
    pos: dict[str, float] = defaultdict(float)
    burden: dict[str, float] = defaultdict(float)
    for row in criteria:
        if row["satisfaction"] != 1:
            continue
        if row["points"] > 0:
            pos[row["behavior_axis"]] += row["points"] / positive
        elif row["points"] < 0:
            burden[row["behavior_axis"]] += abs(row["points"]) / positive
    recovered = sum(pos.values()) - sum(burden.values())
    if abs(recovered - signed) > 1e-9:
        raise SystemExit("axis pieces do not add up to the signed score")
    return {
        "clipped": max(signed, 0.0),
        "positive_credit": sum(pos.values()),
        "penalty_burden": sum(burden.values()),
        "pos": pos,
        "burden": burden,
    }


def grades_by_question(hub: str) -> dict[str, list[dict]]:
    path = GRADES / hub.replace("/", "__") / "grades-gpt-5.6-luna.jsonl"
    if not path.is_file():
        raise SystemExit(f"missing Luna grades for {hub}")
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in load_jsonl(path):
        grouped[row["id"]].append(row)
    return grouped


def load_questions() -> tuple[list[str], dict[str, dict]]:
    import json

    with QUESTIONS.open(encoding="utf-8") as handle:
        selected = list(csv.DictReader(handle))
    if len(selected) != 100:
        raise SystemExit(f"expected 100 questions, found {len(selected)}")
    wanted = {row["id"] for row in selected}
    meta = {}
    for line in EVAL.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("id") in wanted:
            meta[row["id"]] = row
    if set(meta) != wanted:
        raise SystemExit("the 100-question file and the eval file do not match")
    order = [row["id"] for row in selected]
    return order, meta


def pairs() -> list[tuple[str, str]]:
    found = []
    with KEPT.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["hf_id"] in SKIP_CHILDREN:
                continue
            found.append((row["hf_id"], row["parent"]))
    if len(found) != 21:
        raise SystemExit(f"expected 21 pairs with replies, found {len(found)}")
    return found


def criterion_count(meta: dict[str, dict], question_ids: list[str], axis: str, positive: bool) -> int:
    count = 0
    for qid in question_ids:
        for criterion in meta[qid]["rubric_items"]:
            if criterion["behavior_axis"] != axis:
                continue
            if positive and criterion["points"] > 0:
                count += 1
            elif not positive and criterion["points"] < 0:
                count += 1
    return count


def model_means(grouped: dict[str, list[dict]], question_ids: list[str]) -> dict[str, dict]:
    parts = [question_parts(grouped[qid]) for qid in question_ids]
    pos = {}
    burden = {}
    for axis in AXIS_LABEL:
        pos[axis] = statistics.mean(part["pos"].get(axis, 0.0) for part in parts)
        burden[axis] = statistics.mean(part["burden"].get(axis, 0.0) for part in parts)
    return {
        "clipped": statistics.mean(part["clipped"] for part in parts),
        "positive_credit": statistics.mean(part["positive_credit"] for part in parts),
        "penalty_burden": statistics.mean(part["penalty_burden"] for part in parts),
        "pos": pos,
        "burden": burden,
    }


def cluster_ci(values: list[float], parents: list[str], seed: int) -> tuple[float, float, float]:
    """95% interval for the mean gap. Parents are resampled, and a drawn parent brings every fine-tune that uses it."""
    if len(values) != len(parents):
        raise SystemExit("each pair gap needs its parent")
    mean = statistics.mean(values)
    groups: dict[str, list[float]] = defaultdict(list)
    for value, parent in zip(values, parents):
        groups[parent].append(value)
    keys = list(groups)
    if len(keys) < 2 or all(abs(value - mean) < 1e-12 for value in values):
        return mean, mean, mean
    rng = random.Random(seed)
    draws = []
    for _ in range(BOOTSTRAP_DRAWS):
        chosen = [keys[rng.randrange(len(keys))] for _ in keys]
        sample = [value for key in chosen for value in groups[key]]
        draws.append(statistics.mean(sample))
    draws.sort()
    low = draws[int(0.025 * BOOTSTRAP_DRAWS)]
    high = draws[int(0.975 * BOOTSTRAP_DRAWS) - 1]
    return mean, low, high


def row_from_plotted(
    acuity: str,
    panel: str,
    label: str,
    plotted: list[float],
    raw_ft_minus_parent: list[float],
    parents: list[str],
    n_criteria: int,
    n_questions: int,
) -> dict:
    t_mean, t_low, t_high, n = mean_ci(plotted)
    seed = zlib.adler32(f"{acuity}|{panel}|{label}".encode())
    mean, low, high = cluster_ci(plotted, parents, seed)
    if abs(mean - t_mean) > 1e-9:
        raise SystemExit("the bootstrap mean and the pair mean disagree")
    raw_mean = statistics.mean(raw_ft_minus_parent)
    return {
        "acuity": acuity,
        "panel": panel,
        "label": label,
        "mean": mean,
        "low": low,
        "high": high,
        "t_low": t_low,
        "t_high": t_high,
        "values": plotted,
        "raw_ft_minus_parent": raw_mean,
        "n_pairs": n,
        "n_parents": len(set(parents)),
        "n_criteria": n_criteria,
        "n_questions": n_questions,
        "draw": panel in SUMMARY_PANELS or n_criteria >= MIN_CRITERIA,
    }


def build_rows() -> tuple[list[dict], list[dict]]:
    order, meta = load_questions()
    pair_list = pairs()
    child = {hub: grades_by_question(hub) for hub, _ in pair_list}
    parent = {hub: grades_by_question(hub) for _, hub in pair_list}
    slices = [("all", "All", order)] + [
        (key, label, [qid for qid in order if meta[qid]["acuity"] == key])
        for key, label in ACUITY_ORDER
    ]
    rows = []
    summaries = []
    for acuity_key, _label, question_ids in slices:
        child_means = {hub: model_means(grouped, question_ids) for hub, grouped in child.items()}
        parent_means = {hub: model_means(grouped, question_ids) for hub, grouped in parent.items()}

        parent_ids = [base for _fine, base in pair_list]

        def paired(pick) -> list[float]:
            return [
                pick(child_means[fine]) - pick(parent_means[base])
                for fine, base in pair_list
            ]

        score_raw = paired(lambda item: item["clipped"])
        # Left is the fine-tune better, so a higher fine-tune score is negative on the plot.
        score_plot = [-value for value in score_raw]
        rows.append(
            row_from_plotted(
                acuity_key,
                "score",
                "Task-clipped score",
                score_plot,
                score_raw,
                parent_ids,
                n_criteria=0,
                n_questions=len(question_ids),
            )
        )
        credit_raw = paired(lambda item: item["positive_credit"])
        burden_raw = paired(lambda item: item["penalty_burden"])
        n_positive = sum(
            1
            for qid in question_ids
            for criterion in meta[qid]["rubric_items"]
            if criterion["points"] > 0
        )
        n_penalty = sum(
            1
            for qid in question_ids
            for criterion in meta[qid]["rubric_items"]
            if criterion["points"] < 0
        )
        rows.append(
            row_from_plotted(
                acuity_key,
                "summary_positive",
                "Positive points",
                [-value for value in credit_raw],
                credit_raw,
                parent_ids,
                n_positive,
                len(question_ids),
            )
        )
        rows.append(
            row_from_plotted(
                acuity_key,
                "summary_penalty",
                "Penalties",
                burden_raw,
                burden_raw,
                parent_ids,
                n_penalty,
                len(question_ids),
            )
        )
        summaries.append(
            {
                "acuity": acuity_key,
                "n_questions": len(question_ids),
                "clipped": statistics.mean(score_raw),
                "positive_credit": statistics.mean(credit_raw),
                "penalty_burden": statistics.mean(burden_raw),
            }
        )
        for axis, label in AXIS_LABEL.items():
            n_pos = criterion_count(meta, question_ids, axis, True)
            pos_raw = paired(lambda item, axis=axis: item["pos"][axis])
            rows.append(
                row_from_plotted(
                    acuity_key,
                    "positive",
                    label,
                    [-value for value in pos_raw],
                    pos_raw,
                    parent_ids,
                    n_pos,
                    len(question_ids),
                )
            )
            n_neg = criterion_count(meta, question_ids, axis, False)
            bur_raw = paired(lambda item, axis=axis: item["burden"][axis])
            # A smaller burden is better, so fine-tune minus parent is already
            # negative when the fine-tune is better.
            rows.append(
                row_from_plotted(
                    acuity_key,
                    "penalty",
                    label,
                    bur_raw,
                    bur_raw,
                    parent_ids,
                    n_neg,
                    len(question_ids),
                )
            )
    return rows, summaries


def slots(rows: list[dict]) -> list[dict]:
    """Shared vertical order. An axis is listed if any acuity has enough criteria."""
    by_acuity: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        if row["acuity"] != "all":
            by_acuity[row["acuity"]].append(row)
    ordered = []
    ordered.append({"kind": "header", "panel": "summary", "label": "Summary"})
    ordered.append({"kind": "point", "panel": "score", "label": "Task-clipped score"})
    ordered.append({"kind": "point", "panel": "summary_positive", "label": "Positive points"})
    ordered.append({"kind": "point", "panel": "summary_penalty", "label": "Penalties"})
    ordered.append({"kind": "header", "panel": "positive", "label": "Positive points, by kind"})
    for axis, label in AXIS_LABEL.items():
        if any(
            row["panel"] == "positive" and row["label"] == label and row["draw"]
            for row in rows
            if row["acuity"] != "all"
        ):
            ordered.append({"kind": "point", "panel": "positive", "label": label, "axis": axis})
    ordered.append({"kind": "header", "panel": "penalty", "label": "Penalties, by kind"})
    for axis, label in AXIS_LABEL.items():
        if any(
            row["panel"] == "penalty" and row["label"] == label and row["draw"]
            for row in rows
            if row["acuity"] != "all"
        ):
            ordered.append({"kind": "point", "panel": "penalty", "label": label, "axis": axis})
    return ordered


def write_csv(rows: list[dict], path: Path) -> None:
    fields = [
        "acuity",
        "panel",
        "label",
        "plotted_mean",
        "low",
        "high",
        "t_low",
        "t_high",
        "raw_ft_minus_parent",
        "n_pairs",
        "n_parents",
        "n_criteria",
        "n_questions",
        "drawn",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "acuity": row["acuity"],
                    "panel": row["panel"],
                    "label": row["label"],
                    "plotted_mean": f"{row['mean']:.6f}",
                    "low": f"{row['low']:.6f}",
                    "high": f"{row['high']:.6f}",
                    "t_low": f"{row['t_low']:.6f}",
                    "t_high": f"{row['t_high']:.6f}",
                    "raw_ft_minus_parent": f"{row['raw_ft_minus_parent']:.6f}",
                    "n_pairs": row["n_pairs"],
                    "n_parents": row["n_parents"],
                    "n_criteria": row["n_criteria"],
                    "n_questions": row["n_questions"],
                    "drawn": int(row["draw"] and row["acuity"] != "all"),
                }
            )


def y_offsets(values: list[float]) -> list[float]:
    """Spread pairs that land on the same gap so a stack of zeros is a column, not one dot."""
    counts: dict[float, int] = defaultdict(int)
    for value in values:
        counts[round(value, 5)] += 1
    seen: dict[float, int] = defaultdict(int)
    offsets = []
    for value in values:
        key = round(value, 5)
        index = seen[key]
        seen[key] += 1
        count = counts[key]
        if count == 1:
            offsets.append(0.0)
            continue
        span = min(0.62, max(0.14, 0.045 * (count - 1)))
        offsets.append((index - (count - 1) / 2) * (span / (count - 1)))
    return offsets


# Plotted value is parent-better to the right. Blue is a negative gap, red a positive one.
BLUE = "#1d4e89"
RED = "#b42318"


def draw_diamond(ax, y: float, low: float, mean: float, high: float) -> None:
    color = BLUE if mean < 0 else RED if mean > 0 else "#555555"
    if high - low < 1e-6:
        ax.plot([mean, mean], [y - 0.18, y + 0.18], color=color, lw=2.0, zorder=5)
        return
    height = 0.22
    xs = [low, mean, high, mean]
    ys = [y, y + height, y, y - height]
    ax.fill(xs, ys, facecolor=color, edgecolor=color, alpha=0.9, lw=0.6, zorder=5)


def axis_limit(drawn: list[dict]) -> tuple[float, int]:
    """Scale the axis to the diamonds. A few extreme pairs are left off the edge."""
    abs_ci = max(max(abs(row["low"]), abs(row["high"])) for row in drawn)
    outside = 0
    limit = max(abs_ci, 0.02) * 1.25
    for row in drawn:
        outside += sum(1 for value in row["values"] if abs(value) > limit)
    return limit, outside


def paint(ax, rows_for_ax: list[dict], order: list[dict], annotate_n: bool = True) -> None:
    lookup = {(row["panel"], row["label"]): row for row in rows_for_ax}
    ys = list(range(len(order)))
    bottom_to_top = list(reversed(order))
    for y, slot in zip(ys, bottom_to_top):
        if slot["kind"] != "point":
            continue
        row = lookup.get((slot["panel"], slot["label"]))
        if row is None or not row["draw"]:
            continue
        for value, offset in zip(row["values"], y_offsets(row["values"])):
            ax.plot(
                value,
                y + offset,
                "o",
                color="#4a4a4a",
                alpha=0.28,
                ms=3.2,
                zorder=2,
                markeredgewidth=0,
            )
        draw_diamond(ax, y, row["low"], row["mean"], row["high"])
        if annotate_n and slot["panel"] != "score":
            ax.annotate(
                str(row["n_criteria"]),
                xy=(1.01, y),
                xycoords=("axes fraction", "data"),
                fontsize=7,
                color="#666666",
                va="center",
                ha="left",
                annotation_clip=False,
            )
    ax.axvline(0, color="#888888", lw=0.8, zorder=1)
    ax.set_xlabel("←  fine-tune better          parent better  →", fontsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", labelsize=8)


def y_labels(order: list[dict]):
    bottom_to_top = list(reversed(order))
    labels = [slot["label"] for slot in bottom_to_top]
    return bottom_to_top, labels


def draw(rows: list[dict], png: Path, pdf: Path) -> int:
    order = slots(rows)
    by_acuity = {
        acuity: [row for row in rows if row["acuity"] == acuity]
        for acuity, _title in ACUITY_ORDER
    }
    fig, axes = plt.subplots(
        1,
        3,
        figsize=(13.6, 10.2),
        sharex=True,
        sharey=True,
    )
    fig.subplots_adjust(left=0.22, right=0.96, top=0.90, bottom=0.08, wspace=0.16)
    drawn = [
        row
        for acuity, _title in ACUITY_ORDER
        for row in by_acuity[acuity]
        if row["draw"] and any(slot["panel"] == row["panel"] and slot["label"] == row["label"] and slot["kind"] == "point" for slot in order)
    ]
    if not drawn:
        raise SystemExit("no rows to draw")
    limit, outside = axis_limit(drawn)
    for ax, (acuity_key, title) in zip(axes, ACUITY_ORDER):
        n_questions = next(row["n_questions"] for row in by_acuity[acuity_key] if row["panel"] == "score")
        paint(ax, by_acuity[acuity_key], order)
        ax.set_title(f"{title}\n{n_questions} questions", loc="center", fontsize=12, pad=8)
        ax.set_xlim(-limit, limit)
    bottom_to_top, labels = y_labels(order)
    axes[0].set_yticks(list(range(len(order))))
    axes[0].set_yticklabels(labels, fontsize=8.5)
    for tick, slot in zip(axes[0].get_yticklabels(), bottom_to_top):
        if slot["kind"] == "header":
            tick.set_fontstyle("italic")
            tick.set_color("#555555")
            tick.set_fontsize(8)
    fig.suptitle(
        "Mental-health fine-tune versus its instruction-tuned parent",
        fontsize=14,
        x=0.22,
        ha="left",
        y=0.98,
    )
    fig.savefig(png, dpi=160)
    fig.savefig(pdf)
    plt.close(fig)
    return outside


def overall_slots(rows: list[dict]) -> list[dict]:
    """Same groups as the acuity figure, including a kind of line only when the full 100 has at least two criteria."""
    present = {
        (row["panel"], row["label"])
        for row in rows
        if row["acuity"] == "all" and row["draw"]
    }
    return [
        slot
        for slot in slots(rows)
        if slot["kind"] == "header" or (slot["panel"], slot["label"]) in present
    ]


def draw_overall(rows: list[dict], png: Path, pdf: Path) -> int:
    order = overall_slots(rows)
    block = [row for row in rows if row["acuity"] == "all"]
    drawn = [row for row in block if row["draw"] and any(
        slot["kind"] == "point" and slot["panel"] == row["panel"] and slot["label"] == row["label"]
        for slot in order
    )]
    if not drawn:
        raise SystemExit("no overall rows to draw")
    limit, outside = axis_limit(drawn)
    fig, ax = plt.subplots(figsize=(8.4, 10.2))
    fig.subplots_adjust(left=0.34, right=0.94, top=0.92, bottom=0.07)
    paint(ax, block, order)
    n_questions = next(row["n_questions"] for row in block if row["panel"] == "score")
    ax.set_title(f"All {n_questions} questions", loc="center", fontsize=12, pad=8)
    ax.set_xlim(-limit, limit)
    bottom_to_top, labels = y_labels(order)
    ax.set_yticks(list(range(len(order))))
    ax.set_yticklabels(labels, fontsize=8.5)
    for tick, slot in zip(ax.get_yticklabels(), bottom_to_top):
        if slot["kind"] == "header":
            tick.set_fontstyle("italic")
            tick.set_color("#555555")
            tick.set_fontsize(8)
    fig.suptitle(
        "Mental-health fine-tune versus its instruction-tuned parent",
        fontsize=13,
        x=0.34,
        ha="left",
        y=0.98,
    )
    fig.savefig(png, dpi=160)
    fig.savefig(pdf)
    plt.close(fig)
    return outside


def main() -> None:
    rows, summaries = build_rows()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(rows, OUT_DIR / "pair-gap-forest.csv")
    outside = draw(rows, OUT_DIR / "pair-gap-forest.png", OUT_DIR / "pair-gap-forest.pdf")
    draw(rows, OUT_DIR / "pair-gap-by-acuity.png", OUT_DIR / "pair-gap-by-acuity.pdf")
    outside_all = draw_overall(rows, OUT_DIR / "pair-gap-overall.png", OUT_DIR / "pair-gap-overall.pdf")
    print(f"pair dots past the axis edge: acuity figure {outside}, overall figure {outside_all}")
    print("fine-tune minus parent")
    for item in summaries:
        print(
            f"{item['acuity']:12} questions {item['n_questions']:3}  "
            f"clipped {item['clipped']:+.4f}  "
            f"positive credit {item['positive_credit']:+.4f}  "
            f"penalty burden {item['penalty_burden']:+.4f}"
        )
    for row in rows:
        if row["acuity"] == "all" or not row["draw"]:
            continue
        print(
            f"{row['acuity']:12} {row['panel']:9} {row['label']:32} "
            f"plot {row['mean']:+.3f} parent-boot [{row['low']:+.3f}, {row['high']:+.3f}]  "
            f"pair-t [{row['t_low']:+.3f}, {row['t_high']:+.3f}]  "
            f"ft-parent {row['raw_ft_minus_parent']:+.3f}  lines={row['n_criteria']}"
        )


if __name__ == "__main__":
    main()
