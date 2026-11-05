#!/usr/bin/env python3
"""GPT-5.6 Sol versus GPT-5.6 Luna on the 25-question MentalHealthBench subset.

One point is one model's mean score. Sol is the x-axis. The grades are the
paired files under replies/mentalhealthbench-english100/.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

GRADES = REPO / "replies/mentalhealthbench-english100"
SOL_NAME = "grades-gpt-5.6-sol.jsonl"
LUNA_NAME = "grades-gpt-5.6-luna.jsonl"
N_QUESTIONS = 25
N_MODELS = 37
TITLE = (
    "GPT-5.6 Sol versus GPT-5.6 Luna scoring on a 25-question subset "
    "of MentalHealthBench"
)


def _load(path: Path) -> list[dict]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    bad = [row["status"] for row in rows if row["status"] != "ok"]
    if bad:
        raise SystemExit(f"{path} has a grade that is not ok")
    return rows


def _question_scores(rows: list[dict], judge: str) -> dict[str, float]:
    by: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        if row["judge_model"] != judge:
            raise SystemExit(f"expected judge {judge}, found {row['judge_model']}")
        by[row["id"]].append(row)
    scores = {}
    for qid, criteria in by.items():
        positive = sum(item["points"] for item in criteria if item["points"] > 0)
        if positive <= 0:
            raise SystemExit(f"{qid} has no positive points")
        met = sum(item["points"] for item in criteria if item["satisfaction"] == 1)
        scores[qid] = max(met / positive, 0.0)
    return scores


def model_means() -> tuple[np.ndarray, np.ndarray]:
    """Return Sol means and Luna means, one pair per model, same order."""
    sol_paths = sorted(GRADES.glob(f"*/{SOL_NAME}"))
    if len(sol_paths) != N_MODELS:
        raise SystemExit(f"expected {N_MODELS} Sol grade files, found {len(sol_paths)}")
    sol_means = []
    luna_means = []
    for sol_path in sol_paths:
        luna_path = sol_path.with_name(LUNA_NAME)
        if not luna_path.is_file():
            raise SystemExit(f"no Luna grades beside {sol_path}")
        sol = _question_scores(_load(sol_path), "gpt-5.6-sol")
        luna = _question_scores(_load(luna_path), "gpt-5.6-luna")
        shared = sorted(set(sol) & set(luna))
        if len(shared) != N_QUESTIONS:
            raise SystemExit(f"{sol_path.parent.name}: {len(shared)} shared questions, expected {N_QUESTIONS}")
        sol_means.append(float(np.mean([sol[qid] for qid in shared])))
        luna_means.append(float(np.mean([luna[qid] for qid in shared])))
    return np.array(sol_means), np.array(luna_means)


def draw(dest: Path) -> None:
    sol, luna = model_means()
    r_value, p_value = stats.pearsonr(sol, luna)
    r_squared = float(r_value) ** 2
    p_text = "p < 0.0001" if p_value < 0.0001 else f"p = {p_value:.4f}"
    fig, ax = plt.subplots(figsize=(6.4, 6.6))
    hi = max(float(sol.max()), float(luna.max())) * 1.08
    ax.plot([0, hi], [0, hi], color="#bbbbbb", linewidth=1, zorder=1)
    ax.scatter(sol, luna, s=36, color="#222222", zorder=2)
    ax.set_xlim(-0.01, hi)
    ax.set_ylim(-0.01, hi)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("GPT-5.6 Sol")
    ax.set_ylabel("GPT-5.6 Luna")
    ax.set_title(TITLE, fontsize=11)
    ax.text(
        0.05,
        0.95,
        f"R² = {r_squared:.3f}\n{p_text}",
        transform=ax.transAxes,
        fontsize=11,
        verticalalignment="top",
        horizontalalignment="left",
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    dest.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(dest, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {dest}")
    print(f"  n={len(sol)} R²={r_squared:.3f} {p_text}")


if __name__ == "__main__":
    draw(GRADES / "sol-vs-luna-model-means.png")
