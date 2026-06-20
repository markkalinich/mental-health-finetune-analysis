#!/usr/bin/env python3
"""Analyze shieldgemma-2-4b-it SG-2 arm: paper generic vs SG-2 multimodal patched (+ Yes/No reparse).

Three arms (when patched cache exists):
  1. generic_override_LM_STUDIO_GEMMA — paper cache
  2. sg2_multimodal_before_reparse — SG-2 patched run cache
  3. sg2_multimodal_after_yesno_reparse — jerry-rig Yes/No on SG-2 parse_fail rows

Usage:
  .venv/bin/python reviewer_2_experiments/analyze_shieldgemma_24b_sg2.py --yesno-only-on-paper --full --task all
  .venv/bin/python reviewer_2_experiments/analyze_shieldgemma_24b_sg2.py --full --task all
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(SCRIPT_DIR))
from r2_paths import R2, SG2_RESULTS, SG2_RUN

LM_ID = "shieldgemma-2-4b-it"
SIZE = "4b-it"
PAPER_CACHE = ROOT / "cache"
SMOKE_ROOT = R2 / "zArchive" / "tier_a_smoke_runs"
FULL_SG2_DIR = SG2_RUN
FULL_SG2_RESULTS = SG2_RESULTS

TASK_CFG = {
    "SI": {
        "experiment_type": "suicidal_ideation",
        "config_key": "suicidal_ideation",
        "pred_field": "safety_type",
        "pred_pos": "passive_si",
        "pred_neg": "no_SI",
        "prompt": ROOT / "data/prompts/system_suicide_detection_v2.txt",
        "prompt_name": "system_suicide_detection_v2",
        "full_input": ROOT / "data/inputs/finalized_input_data/SI_finalized_sentences.csv",
        "smoke_input": SMOKE_ROOT / "shieldgemma_24b_sg2_si_10pct_smoke/data/SI_finalized_sentences_10pct.csv",
        "smoke_cache": SMOKE_ROOT / "shieldgemma_24b_sg2_si_10pct_smoke/cache",
    },
    "TR": {
        "experiment_type": "therapy_request",
        "config_key": "therapy_request",
        "pred_field": "therapy_request",
        "pred_pos": "explicit_therapy_request",
        "pred_neg": "declarative",
        "prompt": ROOT / "data/prompts/therapy_request_classifier_v3.txt",
        "prompt_name": "therapy_request_classifier_v3",
        "full_input": ROOT / "data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv",
        "smoke_input": SMOKE_ROOT / "shieldgemma_24b_sg2_tr_10pct_smoke/data/therapy_request_finalized_sentences_10pct.csv",
        "smoke_cache": SMOKE_ROOT / "shieldgemma_24b_sg2_tr_10pct_smoke/cache",
    },
    "TE": {
        "experiment_type": "therapy_engagement",
        "config_key": "therapy_engagement",
        "pred_field": "therapy_engagement",
        "pred_pos": "simulated_therapy",
        "pred_neg": "non_therapeutic",
        "prompt": ROOT / "data/prompts/therapy_engagement_conversation_prompt_v2.txt",
        "prompt_name": "therapy_engagement_conversation_prompt_v2",
        "full_input": ROOT / "data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv",
        "smoke_input": SMOKE_ROOT / "shieldgemma_24b_sg2_te_10pct_smoke/data/therapy_engagement_finalized_sentences_10pct.csv",
        "smoke_cache": SMOKE_ROOT / "shieldgemma_24b_sg2_te_10pct_smoke/cache",
    },
}


def parse_yes_no_from_content(content: str) -> int:
    if not content:
        return -1
    stripped = content.strip().lower()
    if stripped == "yes" or stripped.startswith("yes\n") or stripped.startswith("yes "):
        return 1
    if stripped == "no" or stripped.startswith("no\n") or stripped.startswith("no "):
        return 0
    return -1


def fetch_raw_by_input_text(cache_dir: Path, prompt_name: str) -> dict:
    db = cache_dir / "results.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT it.input_text, cr.raw_response
        FROM cached_results cr
        JOIN cache_keys ck ON cr.cache_id = ck.cache_id
        JOIN input_texts it ON ck.input_hash = it.input_hash
        WHERE ck.model_full_name = ? AND ck.prompt_name = ?
        """,
        (LM_ID, prompt_name),
    )
    out = {}
    for input_text, raw in cur.fetchall():
        try:
            data = json.loads(raw)
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except (json.JSONDecodeError, TypeError, IndexError):
            content = raw or ""
        out[input_text] = content
    conn.close()
    return out


def jerry_rig_yesno_reparse(df, raw_by_text, pred_field, pred_pos, pred_neg):
    df = df.copy()
    text_col = "text" if "text" in df.columns else "input_text"
    mask = (df["model_family"] == "shieldgemma") & (df["model_size"] == SIZE) & (df["status"] == "parse_fail")
    n = mask.sum()
    recovered = 0
    still_fail = 0
    for idx in df.index[mask]:
        text = df.at[idx, text_col]
        content = raw_by_text.get(text, "")
        binary = parse_yes_no_from_content(content)
        if binary == 1:
            df.at[idx, "status"] = "ok"
            df.at[idx, pred_field] = pred_pos
            recovered += 1
        elif binary == 0:
            df.at[idx, "status"] = "ok"
            df.at[idx, pred_field] = pred_neg
            recovered += 1
        else:
            still_fail += 1
    print(f"  Jerry-rig Yes/No: {recovered}/{n} recovered, {still_fail} still parse_fail")
    return df


def load_df(input_csv, prompt, experiment_type, cache_dir):
    from analysis.model_performance.data_loader import load_experiment_results

    df, _ = load_experiment_results(
        str(input_csv),
        str(prompt),
        {"shieldgemma": [SIZE]},
        experiment_type,
        cache_dir=str(cache_dir),
    )
    return df


def metrics_row(df, label, experiment_type, config_key):
    from analysis.model_performance.metrics_calculator import calculate_model_metrics
    from config.experiment_config import get_experiment_config

    cfg = get_experiment_config(config_key)
    m = calculate_model_metrics(
        df,
        "shieldgemma",
        SIZE,
        experiment_type,
        cfg.binary_positive_categories,
        cfg.ground_truth_positive_categories,
    )
    if m is None:
        return {
            "label": label,
            "model_size": SIZE,
            "n_rows": 0,
            "parse_success_rate": None,
            "sensitivity": None,
            "specificity": None,
            "f1_score": None,
        }
    n = len(df[(df["model_family"] == "shieldgemma") & (df["model_size"] == SIZE)])
    return {
        "label": label,
        "model_size": SIZE,
        "n_rows": n,
        "parse_success_rate": round(m["parse_success_rate"], 6),
        "sensitivity": round(m["sensitivity"], 6),
        "specificity": round(m["specificity"], 6),
        "f1_score": round(m["f1_score"], 6),
    }


def print_row(row):
    if row["parse_success_rate"] is None:
        print(f"  {row['label']}: no data")
    else:
        print(
            f"  {row['label']}: parse={row['parse_success_rate']:.3f} "
            f"sens={row['sensitivity']:.3f} spec={row['specificity']:.3f} "
            f"f1={row['f1_score']:.3f}"
        )


def analyze_task(task, full, yesno_only):
    cfg = TASK_CFG[task]
    input_csv = cfg["full_input"] if full else cfg["smoke_input"]
    sg2_cache = FULL_SG2_DIR / "cache" if full else cfg["smoke_cache"]
    out_json = (
        FULL_SG2_RESULTS if full else cfg["smoke_cache"].parent
    ) / f"shieldgemma_24b_sg2_analysis_{task.lower()}.json"

    print(f"\n=== {task} {'full' if full else 'smoke'} (SG-2 arm) ===")
    generic_df = load_df(input_csv, cfg["prompt"], cfg["experiment_type"], PAPER_CACHE)
    metrics = [
        metrics_row(
            generic_df,
            "generic_override_LM_STUDIO_GEMMA_as_scored",
            cfg["experiment_type"],
            cfg["config_key"],
        )
    ]
    print_row(metrics[-1])

    if yesno_only:
        raw = fetch_raw_by_input_text(PAPER_CACHE, cfg["prompt_name"])
        yesno_df = jerry_rig_yesno_reparse(
            generic_df, raw, cfg["pred_field"], cfg["pred_pos"], cfg["pred_neg"]
        )
        metrics.append(
            metrics_row(
                yesno_df,
                "generic_override_after_yesno_reparse",
                cfg["experiment_type"],
                cfg["config_key"],
            )
        )
        print_row(metrics[-1])
    else:
        if not (sg2_cache / "results.db").exists():
            raise FileNotFoundError(
                f"Missing SG-2 cache: {sg2_cache / 'results.db'} "
                f"(run run_shieldgemma_24b_sg2_sensitivity.py first)"
            )
        sg2_df = load_df(input_csv, cfg["prompt"], cfg["experiment_type"], sg2_cache)
        metrics.append(
            metrics_row(
                sg2_df,
                "sg2_multimodal_before_reparse",
                cfg["experiment_type"],
                cfg["config_key"],
            )
        )
        print_row(metrics[-1])
        raw = fetch_raw_by_input_text(sg2_cache, cfg["prompt_name"])
        sg2_yesno = jerry_rig_yesno_reparse(
            sg2_df, raw, cfg["pred_field"], cfg["pred_pos"], cfg["pred_neg"]
        )
        metrics.append(
            metrics_row(
                sg2_yesno,
                "sg2_multimodal_after_yesno_reparse",
                cfg["experiment_type"],
                cfg["config_key"],
            )
        )
        print_row(metrics[-1])

    report = {
        "task": task,
        "mode": "full" if full else "smoke",
        "arm": "sg2_multimodal_patched",
        "lm_studio_id": LM_ID,
        "input_csv": str(input_csv),
        "paper_cache": str(PAPER_CACHE),
        "sg2_cache": None if yesno_only else str(sg2_cache),
        "metrics": metrics,
        "caveat": (
            "SG-2 arm uses patched native multimodal framing (image placeholder + policy block). "
            "Yes/No reparse maps leading Yes/No only; off-label for SI/TR/TE text tasks."
        ),
    }
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2))
    print(f"Wrote {out_json}")
    return report


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--task", choices=["SI", "TR", "TE", "all"], default="all")
    p.add_argument("--full", action="store_true")
    p.add_argument("--yesno-only-on-paper", action="store_true")
    args = p.parse_args()
    tasks = ["SI", "TR", "TE"] if args.task == "all" else [args.task]
    reports = [analyze_task(t, args.full, args.yesno_only_on_paper) for t in tasks]
    if len(reports) > 1:
        summary = FULL_SG2_RESULTS / "shieldgemma_24b_sg2_analysis_summary.json"
        summary.parent.mkdir(parents=True, exist_ok=True)
        summary.write_text(json.dumps({"tasks": reports}, indent=2))
        print(f"\nWrote {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
