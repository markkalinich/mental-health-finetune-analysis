#!/usr/bin/env python3
"""Ad-hoc analysis: SG-1 patched ShieldGemma smoke test vs generic-override baseline.

Jerry-rigged Yes/No re-parse for the patched cache ONLY. Does NOT modify data_loader.py.

Usage:
  .venv/bin/python reviewer_2_experiments/analyze_sg1_patched_smoke_test.py --task SI
  .venv/bin/python reviewer_2_experiments/analyze_sg1_patched_smoke_test.py --task TR
  .venv/bin/python reviewer_2_experiments/analyze_sg1_patched_smoke_test.py --full --task all
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any, Dict

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from r2_paths import CACHE, R2, SG1_RESULTS, SG1_RUN

SMOKE_ROOT = R2 / "zArchive" / "tier_a_smoke_runs"

SIZES_SMOKE = ["2b"]
SIZES_FULL = ["2b", "9b", "27b"]

# Yes/No -> task pred fields (same as data_loader._GUARD_POSITIVE/_NEGATIVE)
TASK_REPARSE = {
    "SI": {
        "experiment_type": "suicidal_ideation",
        "config_key": "suicidal_ideation",
        "pred_field": "safety_type",
        "prior_field": "prior_safety_type",
        "pred_pos": "passive_si",
        "pred_neg": "no_SI",
        "prompt": ROOT / "data/prompts/system_suicide_detection_v2.txt",
        "prompt_name": "system_suicide_detection_v2",
        "full_input": ROOT / "data/inputs/finalized_input_data/SI_finalized_sentences.csv",
        "smoke_dir": "shieldgemma_sg1_patched_si_10pct_smoke",
        "subset_file": "data/SI_finalized_sentences_10pct.csv",
        "generic_cache": R2 / "zArchive/tier_a_pilots/shieldgemma_9b_rerun_subset/shieldgemma_9b_rerun/cache",
        "generic_cache_full": ROOT / "cache",
    },
    "TR": {
        "experiment_type": "therapy_request",
        "config_key": "therapy_request",
        "pred_field": "therapy_request",
        "prior_field": "prior_therapy_request",
        "pred_pos": "explicit_therapy_request",
        "pred_neg": "declarative",
        "prompt": ROOT / "data/prompts/therapy_request_classifier_v3.txt",
        "prompt_name": "therapy_request_classifier_v3",
        "full_input": ROOT / "data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv",
        "smoke_dir": "shieldgemma_sg1_patched_tr_10pct_smoke",
        "subset_file": "data/therapy_request_finalized_sentences_10pct.csv",
        "generic_cache": CACHE / "shieldgemma_9b_rerun_full" / "cache",
        "generic_cache_full": ROOT / "cache",
    },
    "TE": {
        "experiment_type": "therapy_engagement",
        "config_key": "therapy_engagement",
        "pred_field": "therapy_engagement",
        "prior_field": "prior_therapy_engagement",
        "pred_pos": "simulated_therapy",
        "pred_neg": "non_therapeutic",
        "prompt": ROOT / "data/prompts/therapy_engagement_conversation_prompt_v2.txt",
        "prompt_name": "therapy_engagement_conversation_v2",
        "full_input": ROOT / "data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv",
        "smoke_dir": "shieldgemma_sg1_patched_te_10pct_smoke",
        "subset_file": "data/therapy_engagement_finalized_sentences_10pct.csv",
        "generic_cache": CACHE / "shieldgemma_9b_rerun_te_10pct" / "cache",
        "generic_cache_full": ROOT / "cache",
    },
}

FULL_PATCHED_DIR = SG1_RUN
FULL_PATCHED_RESULTS = SG1_RESULTS


def parse_yes_no_from_content(content: str) -> int:
    if not content:
        return -1
    stripped = content.strip().lower()
    if stripped == "yes" or stripped.startswith("yes\n") or stripped.startswith("yes "):
        return 1
    if stripped == "no" or stripped.startswith("no\n") or stripped.startswith("no "):
        return 0
    return -1


def fetch_raw_by_input_text(
    cache_dir: Path, prompt_name: str, lm_studio_id: str = "shieldgemma-2b"
) -> Dict[str, str]:
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
        (lm_studio_id, prompt_name),
    )
    out: Dict[str, str] = {}
    for input_text, raw in cur.fetchall():
        try:
            data = json.loads(raw)
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except (json.JSONDecodeError, TypeError, IndexError):
            content = raw or ""
        out[input_text] = content
    conn.close()
    return out


def jerry_rig_yesno_reparse(
    df: pd.DataFrame, raw_by_text: Dict[str, str], pred_field: str, pred_pos: str, pred_neg: str
) -> pd.DataFrame:
    df = df.copy()
    text_col = "text" if "text" in df.columns else "input_text"
    mask = (df["model_family"] == "shieldgemma") & (df["status"] == "parse_fail")
    n = mask.sum()
    if n == 0:
        return df

    recovered = 0
    still_fail = 0
    content_counts: Dict[str, int] = {}

    for idx in df.index[mask]:
        text = df.at[idx, text_col]
        content = raw_by_text.get(text, "")
        key = repr(content.strip()[:40]) if content else "<empty>"
        content_counts[key] = content_counts.get(key, 0) + 1
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

    print(
        f"  Jerry-rig Yes/No re-parse: {recovered}/{n} recovered, {still_fail} still parse_fail"
    )
    print(f"  Raw content distribution: {content_counts}")
    return df


def load_df(
    input_csv: Path,
    prompt: Path,
    experiment_type: str,
    cache_dir: Path,
    sizes: list[str],
) -> pd.DataFrame:
    from analysis.model_performance.data_loader import load_experiment_results

    models = {"shieldgemma": sizes}
    df, _ = load_experiment_results(
        str(input_csv),
        str(prompt),
        models,
        experiment_type,
        cache_dir=str(cache_dir),
    )
    return df


def metrics_row(
    df: pd.DataFrame,
    label: str,
    experiment_type: str,
    config_key: str,
    size: str,
) -> dict:
    from analysis.model_performance.metrics_calculator import calculate_model_metrics
    from config.experiment_config import get_experiment_config

    cfg = get_experiment_config(config_key)
    m = calculate_model_metrics(
        df,
        "shieldgemma",
        size,
        experiment_type,
        cfg.binary_positive_categories,
        cfg.ground_truth_positive_categories,
    )
    if m is None:
        return {
            "label": label,
            "model_size": size,
            "n_rows": 0,
            "parse_success_rate": None,
            "sensitivity": None,
            "specificity": None,
            "f1_score": None,
        }
    return {
        "label": label,
        "model_size": size,
        "n_rows": len(df[df["model_size"] == size]),
        "parse_success_rate": round(m["parse_success_rate"], 6),
        "sensitivity": round(m["sensitivity"], 6),
        "specificity": round(m["specificity"], 6),
        "f1_score": round(m["f1_score"], 6),
    }


def row_level_compare(
    generic_df: pd.DataFrame,
    patched_df: pd.DataFrame,
    pred_field: str,
    binary_pos_cats: list,
    size: str,
) -> dict:
    text_col = "text"
    g = generic_df[generic_df["model_size"] == size][[text_col, "status", pred_field]].copy()
    p = patched_df[patched_df["model_size"] == size][[text_col, "status", pred_field]].copy()
    g = g.rename(columns={pred_field: "pred_generic", "status": "status_generic"})
    p = p.rename(columns={pred_field: "pred_patched", "status": "status_patched"})
    m = g.merge(p, on=text_col, how="inner")

    both_ok = m[(m.status_generic == "ok") & (m.status_patched == "ok")]

    def bin_pos(series):
        return series.isin(binary_pos_cats)

    binary_agree = (bin_pos(both_ok["pred_generic"]) == bin_pos(both_ok["pred_patched"])).sum()

    return {
        "model_size": size,
        "rows_joined": len(m),
        "both_ok": len(both_ok),
        "inter_arm_binary_agree": int(binary_agree),
        "inter_arm_binary_disagree": len(both_ok) - int(binary_agree),
        "note": "Compares generic_override vs patched_SG1 predictions; not ground truth.",
    }


def analyze_task(task: str, full: bool) -> dict:
    cfg = TASK_REPARSE[task]
    sizes = SIZES_FULL if full else SIZES_SMOKE
    if full:
        input_csv = cfg["full_input"]
        patched_cache = FULL_PATCHED_DIR / "cache"
        generic_cache = cfg["generic_cache_full"]
        out_json = FULL_PATCHED_RESULTS / f"sg1_patched_full_analysis_{task.lower()}.json"
        mode = "full"
    else:
        smoke_dir = SMOKE_ROOT / cfg["smoke_dir"]
        input_csv = smoke_dir / cfg["subset_file"]
        patched_cache = smoke_dir / "cache"
        generic_cache = cfg["generic_cache"]
        out_json = smoke_dir / f"sg1_patched_smoke_analysis_{task.lower()}.json"
        mode = "smoke"

    for path, label in [
        (input_csv, "input CSV"),
        (generic_cache / "results.db", "generic cache"),
        (patched_cache / "results.db", "patched cache"),
    ]:
        if not path.exists():
            raise FileNotFoundError(f"Missing {label}: {path}")

    print(f"\n=== {task} {mode} analysis ===")
    print("Loading generic-override baseline…")
    generic_df = load_df(input_csv, cfg["prompt"], cfg["experiment_type"], generic_cache, sizes)

    print("Loading patched SG-1 cache…")
    patched_raw_df = load_df(input_csv, cfg["prompt"], cfg["experiment_type"], patched_cache, sizes)

    from config.experiment_config import get_experiment_config

    exp_cfg = get_experiment_config(cfg["config_key"])

    all_metrics = []
    all_compare = []
    patched_reparsed_parts = []
    for size in sizes:
        lm_id = f"shieldgemma-{size}"
        print(f"\n--- shieldgemma-{size} ---")
        raw_by_text = fetch_raw_by_input_text(patched_cache, cfg["prompt_name"], lm_id)
        size_raw = patched_raw_df[patched_raw_df["model_size"] == size].copy()
        print("Applying jerry-rig Yes/No re-parse…")
        size_patched = jerry_rig_yesno_reparse(
            size_raw,
            raw_by_text,
            cfg["pred_field"],
            cfg["pred_pos"],
            cfg["pred_neg"],
        )
        patched_reparsed_parts.append(size_patched)

        generic_size = generic_df[generic_df["model_size"] == size]
        patched_size = patched_raw_df[patched_raw_df["model_size"] == size]

        rows = [
            metrics_row(
                generic_size,
                "generic_override_LM_STUDIO_GEMMA",
                cfg["experiment_type"],
                cfg["config_key"],
                size,
            ),
            metrics_row(
                patched_size,
                "patched_SG1_before_reparse",
                cfg["experiment_type"],
                cfg["config_key"],
                size,
            ),
            metrics_row(
                size_patched,
                "patched_SG1_after_yesno_reparse",
                cfg["experiment_type"],
                cfg["config_key"],
                size,
            ),
        ]
        for row in rows:
            if row["parse_success_rate"] is None:
                print(f"  {row['label']}: no data")
            else:
                print(
                    f"  {row['label']}: parse={row['parse_success_rate']:.3f} "
                    f"sens={row['sensitivity']:.3f} spec={row['specificity']:.3f} "
                    f"f1={row['f1_score']:.3f}"
                )
        all_metrics.extend(rows)

    patched_df = pd.concat(patched_reparsed_parts, ignore_index=True)
    for size in sizes:
        compare = row_level_compare(
            generic_df,
            patched_df,
            cfg["pred_field"],
            exp_cfg.binary_positive_categories,
            size,
        )
        print(
            f"  [{size}] inter_arm_binary_agree: {compare['inter_arm_binary_agree']}/"
            f"{compare['both_ok']} (both_ok={compare['both_ok']}/{compare['rows_joined']})"
        )
        all_compare.append(compare)

    report = {
        "task": task,
        "mode": mode,
        "model_sizes": sizes,
        "input_csv": str(input_csv),
        "generic_cache": str(generic_cache),
        "patched_cache": str(patched_cache),
        "metrics": all_metrics,
        "metrics_note": (
            "sens/spec/f1/parse: each arm vs CSV ground truth. "
            "inter_arm_binary_agree: generic vs patched prediction match only."
        ),
        "row_level_by_size": all_compare,
        "caveat": "Yes/No = policy violation under classifier-as-guideline; sensitivity check only.",
    }
    out_json.write_text(json.dumps(report, indent=2))
    print(f"Wrote {out_json}")
    return report


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--task", choices=["SI", "TR", "TE", "all"], default="SI")
    p.add_argument("--full", action="store_true", help="Full datasets; 2b/9b/27b; patched full cache")
    args = p.parse_args()

    tasks = ["SI", "TR", "TE"] if args.task == "all" else [args.task]
    reports = []
    try:
        for task in tasks:
            reports.append(analyze_task(task, args.full))
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return 1

    if args.full and len(tasks) == 3:
        summary_path = FULL_PATCHED_RESULTS / "sg1_patched_full_analysis_summary.json"
        summary_path.write_text(json.dumps({"tasks": reports}, indent=2))
        print(f"\nWrote {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
