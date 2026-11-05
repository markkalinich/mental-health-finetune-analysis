#!/usr/bin/env python3
"""MentalHealthBench on the English questions whose user message is suicide or self-harm.

Homicide-only user messages are not included. A mention that appears only in
an earlier assistant or system turn is not included. Non-English conversations
are not included. The score is the usual task-clipped MentalHealthBench score,
averaged over these questions only. Every rubric line on those questions counts.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from scipy import stats

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
from config import datasets  # noqa: E402

import orchestration.plot_parse_rates as ppr
from orchestration.plot_figure3_delta import FAMILY_COLORS
from orchestration.plot_mhb_pair_gap import question_parts
from orchestration.plot_params_vs_score import FAMILY_MARKERS, _fdr_bh
from orchestration.plot_spaghetti_delta import TOP_TICK_FRACTION, _bracket, _violin

EVAL = datasets.path("mentalhealthbench_eval")
OUT = REPO / "outputs/cross-grouping/model_performance/spaghetti-mhb-si-hi-selfharm.png"
TESTS = OUT.with_name("spaghetti-mhb-si-hi-selfharm-tests.csv")
GRADES = REPO / "replies/mentalhealthbench-1215-temp0"
ROWS = (("mental-health", "Mental health"), ("medical", "Medical"))

_SI = re.compile(
    r"suicid|\bkill myself\b|\bkilling myself\b|\bend (?:my|his|her|their) life\b"
    r"|\bwant to die\b|\bwanna die\b|\btake my (?:own )?life\b",
    re.IGNORECASE,
)
_SELF_HARM = re.compile(
    r"self[-\s]?harm|\bhurt(?:ing)? myself\b|\bharm(?:ing)? myself\b|\bcut(?:ting)? myself\b",
    re.IGNORECASE,
)
_HI = re.compile(
    r"homicid|\bkill (?:him|her|them|someone|people)\b|\bmurder\b",
    re.IGNORECASE,
)


def _labels(text: str) -> set[str]:
    found = set()
    if _SI.search(text):
        found.add("SI")
    if _SELF_HARM.search(text):
        found.add("self-harm")
    if _HI.search(text):
        found.add("HI")
    return found


# English suicide/self-harm user messages in the released 1,215. The 7
# non-English matches (4 Hindi, 2 Spanish, 1 Portuguese) are left out.
MHB_SAFETY_N = 79


def safety_questions() -> tuple[dict[str, int], dict[str, set[str]]]:
    """English questions whose user message matches suicide or self-harm.

    The count is checked against MHB_SAFETY_N. A user message that matches
    only homicide or murder is left out. A conversation whose language is
    not English is left out.
    """
    rubric_n = {}
    labels = {}
    with EVAL.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            if "language" not in row:
                raise SystemExit(f"{row.get('id')}: MentalHealthBench row has no language")
            user_text = "\n".join(
                message.get("content") or ""
                for message in row["conversation"]["messages"]
                if message.get("role") == "user"
            )
            found = _labels(user_text)
            found.discard("HI")
            rubric_n[row["id"]] = len(row["rubric_items"])
            if found and row["language"] == "en":
                labels[row["id"]] = found
    if len(rubric_n) != 1215:
        raise SystemExit(f"expected 1,215 questions, found {len(rubric_n)}")
    if len(labels) != MHB_SAFETY_N:
        raise SystemExit(
            f"expected {MHB_SAFETY_N} English user SI/self-harm questions, found {len(labels)}"
        )
    return rubric_n, labels


def subset_scores(question_ids: set[str], rubric_n: dict[str, int]) -> dict[str, float]:
    found = {}
    for path in GRADES.iterdir():
        grades = path / "grades-gpt-5.6-luna.jsonl"
        if not grades.is_file():
            continue
        grouped: dict[str, list[dict]] = defaultdict(list)
        seen = set()
        ids = set()
        n_lines = 0
        broken = False
        with grades.open(encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    broken = True
                    break
                n_lines += 1
                ids.add(row.get("id"))
                key = (row.get("id"), row.get("criterion_index"))
                if key in seen:
                    broken = True
                    break
                seen.add(key)
                if row.get("status") != "ok" or row.get("satisfaction") not in (0, 1):
                    broken = True
                    break
                if row.get("id") not in question_ids:
                    continue
                grouped[row["id"]].append(row)
        if broken or n_lines != 5262 or len(ids) != 1215 or set(grouped) != question_ids:
            continue
        if any(len(grouped[qid]) != rubric_n[qid] for qid in question_ids):
            continue
        parts = [question_parts(grouped[qid]) for qid in question_ids]
        found[ppr._hub(path.name)] = 100.0 * float(np.mean([part["clipped"] for part in parts]))
    return found


def pairs(scores: dict[str, float]) -> list[dict]:
    from orchestration.study_roster import plot_records

    records = plot_records()
    parents = {record["hf_id"]: record for record in records if record["role"] == "parent"}
    rows = []
    for record in records:
        if record["role"] != "fine-tune" or record["grouping"] not in ("mental-health", "medical"):
            continue
        child = scores.get(record["hf_id"])
        parent = parents.get(record["parent"])
        base = None if parent is None else scores.get(record["parent"])
        if child is None or base is None:
            continue
        rows.append(
            {
                "hf_id": record["hf_id"],
                "parent": record["parent"],
                "family": record["family"],
                "kind": record["grouping"],
                "child": child,
                "parent_score": base,
                "delta": child - base,
            }
        )
    return rows


def main() -> None:
    rubric_n, labels = safety_questions()
    print(f"questions whose user message is SI or self-harm: {len(labels)} of {len(rubric_n)}")
    mix: dict[str, int] = defaultdict(int)
    for found in labels.values():
        mix["+".join(sorted(found))] += 1
    for name, count in sorted(mix.items(), key=lambda item: -item[1]):
        print(f"  {name}: {count}")
    scores = subset_scores(set(labels), rubric_n)
    block_rows = pairs(scores)
    fig, axes = plt.subplots(2, 1, figsize=(4.8, 7.2), sharex=True, sharey=True)
    pending = []
    for ax, (kind, row_label) in zip(axes, ROWS):
        block = [row for row in block_rows if row["kind"] == kind]
        parents: dict[str, float] = {}
        families: dict[str, str] = {}
        for row in block:
            parents.setdefault(row["parent"], row["parent_score"])
            families.setdefault(row["parent"], row["family"])
        parent_scores = list(parents.values())
        child_scores = [row["child"] for row in block]
        if parent_scores and child_scores:
            _violin(ax, parent_scores, child_scores)
        if len(block) >= 2:
            _stat, p_value = stats.ttest_rel(child_scores, [row["parent_score"] for row in block])
            pending.append((ax, kind, len(block), float(p_value), float(np.mean([row["delta"] for row in block]))))
        for row in block:
            color = FAMILY_COLORS[row["family"]]
            ax.plot([0, 1], [row["parent_score"], row["child"]], color=color, alpha=0.35, linewidth=1.0, zorder=1)
            ax.scatter([1], [row["child"]], s=36, marker="o", color=color, edgecolors="white", linewidths=0.3, zorder=3)
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
        ax.set_xticklabels(["Instruction-tuned", "Fine-tune"])
        ax.set_ylabel(row_label)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    axes[0].set_title(f"User SI / self-harm questions\n(n = {len(labels)})", fontsize=12, fontweight="bold")
    axes[0].set_ylim(0, 40 / TOP_TICK_FRACTION)
    axes[0].set_yticks([0, 10, 20, 30, 40])
    q_values = _fdr_bh([item[3] for item in pending]) if pending else []
    tests = []
    for (ax, kind, n, p_value, mean), q_value in zip(pending, q_values):
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
                "kind": kind,
                "n_questions": len(labels),
                "n_pairs": n,
                "mean_delta": mean,
                "p_value": p_value,
                "q_value": q_value,
                "significant": q_value < 0.05,
            }
        )
    handles = [
        Line2D([0], [0], marker="o", color=FAMILY_COLORS[name], linestyle="None", markersize=8, label=name)
        for name in FAMILY_MARKERS
    ]
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.01))
    fig.savefig(OUT, dpi=170, facecolor="white")
    plt.close(fig)
    with TESTS.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["kind", "n_questions", "n_pairs", "mean_delta", "p_value", "q_value", "significant"],
        )
        writer.writeheader()
        writer.writerows(tests)
    print(f"wrote {OUT}")
    print(f"wrote {TESTS}")
    for row in tests:
        mark = "marked" if row["significant"] else "unmarked"
        print(
            f"  {row['kind']:<16} pairs={row['n_pairs']:<3} "
            f"mean={row['mean_delta']:+.3f} p={row['p_value']:.4f} q={row['q_value']:.4f} {mark}"
        )


if __name__ == "__main__":
    main()
