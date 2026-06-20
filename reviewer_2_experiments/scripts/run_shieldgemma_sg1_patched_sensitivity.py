#!/usr/bin/env python3
"""ShieldGemma SG-1 patched-Jinja sensitivity test (reviewer response).

Minimal change to Google's embedded SG-1 template: supply missing `guideline`
from the pipeline's system message. Does NOT permanently edit LM Studio configs.

Safety protocol:
  1. Golden snapshot of live override JSON(s) under artifacts/sg1_patched_sensitivity_backups/
  2. Temporarily swap override to patched SG-1 Jinja for the run
  3. try/finally: always restore from golden snapshot + SHA256 verify

Requires LM Studio on localhost:1234.

Examples:
  .venv/bin/python reviewer_2_experiments/run_shieldgemma_sg1_patched_sensitivity.py --task SI --smoke-test
  .venv/bin/python reviewer_2_experiments/run_shieldgemma_sg1_patched_sensitivity.py --task TR --smoke-test
  .venv/bin/python reviewer_2_experiments/run_shieldgemma_sg1_patched_sensitivity.py --full --task all
  .venv/bin/python reviewer_2_experiments/run_shieldgemma_sg1_patched_sensitivity.py --snapshot-only
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from r2_paths import R2, SG1_RUN, TEMPLATE_BACKUPS, TEMPLATES

OVERRIDE_DIR = Path.home() / ".lmstudio/.internal/user-concrete-model-default-config"
PATCHED_JINJA = TEMPLATES / "shieldgemma_sg1_patched_guideline.jinja"
GOLDEN_ROOT = TEMPLATE_BACKUPS / "sg1_patched_sensitivity_backups"

SEED = 42
PER_CATEGORY = 5
TE_FRAC = 0.10

TASKS = {
    "SI": {
        "source": ROOT / "data/inputs/finalized_input_data/SI_finalized_sentences.csv",
        "system": ROOT / "data/prompts/system_suicide_detection_v2.txt",
        "prompt_name": "system_suicide_detection_v2",
        "subset_file": "SI_finalized_sentences_10pct.csv",
        "group_col": "Safety type",
        "spot_col": "statement",
        "smoke_dir": "shieldgemma_sg1_patched_si_10pct_smoke",
    },
    "TR": {
        "source": ROOT / "data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv",
        "system": ROOT / "data/prompts/therapy_request_classifier_v3.txt",
        "prompt_name": "therapy_request_classifier_v3",
        "subset_file": "therapy_request_finalized_sentences_10pct.csv",
        "group_col": "therapy_request",
        "spot_col": "statement",
        "smoke_dir": "shieldgemma_sg1_patched_tr_10pct_smoke",
    },
    "TE": {
        "source": ROOT / "data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv",
        "system": ROOT / "data/prompts/therapy_engagement_conversation_prompt_v2.txt",
        "prompt_name": "therapy_engagement_conversation_v2",
        "subset_file": "therapy_engagement_finalized_sentences_10pct.csv",
        "group_col": "therapy_engagement",
        "spot_col": "statement",
        "smoke_dir": "shieldgemma_sg1_patched_te_10pct_smoke",
    },
}

SG1_SIZES = ["2b", "9b", "27b"]

SG1_CASES = [
    {
        "lm_studio_id": "shieldgemma-2b",
        "override_rel": "QuantFactory/shieldgemma-2b-GGUF/shieldgemma-2b.Q8_0.gguf.json",
    },
    {
        "lm_studio_id": "shieldgemma-9b",
        "override_rel": "QuantFactory/shieldgemma-9b-GGUF/shieldgemma-9b.Q8_0.gguf.json",
    },
    {
        "lm_studio_id": "shieldgemma-27b",
        "override_rel": "mradermacher/shieldgemma-27b-GGUF/shieldgemma-27b.Q8_0.gguf.json",
    },
]


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def case_by_id(lm_id: str) -> dict:
    for c in SG1_CASES:
        if c["lm_studio_id"] == lm_id:
            return c
    raise KeyError(lm_id)


def override_path(case: dict) -> Path:
    return OVERRIDE_DIR / case["override_rel"]


def make_override_config(template: str) -> dict:
    return {
        "preset": "",
        "operation": {
            "fields": [
                {
                    "key": "llm.prediction.promptTemplate",
                    "value": {
                        "type": "jinja",
                        "jinjaPromptTemplate": {"template": template},
                        "stopStrings": ["<end_of_turn>"],
                    },
                }
            ]
        },
        "load": {"fields": []},
    }


def snapshot_golden(cases: List[dict], run_id: str) -> Dict[str, dict]:
    records: Dict[str, dict] = {}
    for case in cases:
        live = override_path(case)
        if not live.exists():
            raise FileNotFoundError(f"Live override missing: {live}")
        golden = GOLDEN_ROOT / run_id / case["override_rel"]
        golden.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(live, golden)
        sha = sha256_file(golden)
        records[case["lm_studio_id"]] = {
            "live_path": str(live),
            "golden_path": str(golden),
            "golden_sha256": sha,
        }
        print(f"  golden snapshot {case['lm_studio_id']}: {golden} ({sha[:16]}…)")
    return records


def restore_from_record(case: dict, record: dict) -> bool:
    live = override_path(case)
    golden = Path(record["golden_path"])
    if not golden.exists():
        raise FileNotFoundError(f"Golden backup missing: {golden}")
    shutil.copy2(golden, live)
    restored = sha256_file(live)
    ok = restored == record["golden_sha256"]
    print(f"  restore {case['lm_studio_id']}: match={ok} sha={restored[:16]}…")
    return ok


def apply_patched(case: dict, template: str) -> None:
    live = override_path(case)
    live.write_text(json.dumps(make_override_config(template), indent=2) + "\n")
    print(f"  applied patched SG-1 override -> {live}")


def unload_all() -> None:
    subprocess.run(["lms", "unload", "--all"], capture_output=True, text=True, timeout=120)


def lms_load(model_id: str) -> None:
    unload_all()
    p = subprocess.run(
        ["lms", "load", model_id, "-y", "-c", "4096"],
        capture_output=True,
        text=True,
        timeout=900,
    )
    if p.returncode != 0:
        raise RuntimeError(f"lms load {model_id} failed:\n{p.stderr or p.stdout}")


def break_test_http(model_id: str, system_prompt: str, user_text: str) -> dict:
    payload = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text},
        ],
        "temperature": 0.0,
        "max_tokens": 128,
        "stream": False,
    }
    result: Dict[str, Any] = {"http_status": None, "response_content": None, "error_text": None}
    try:
        r = requests.post("http://localhost:1234/v1/chat/completions", json=payload, timeout=180)
        result["http_status"] = r.status_code
        if r.ok:
            body = r.json()
            result["response_content"] = (
                body.get("choices", [{}])[0].get("message", {}).get("content")
            )
        else:
            result["error_text"] = r.text[:2000]
    except requests.RequestException as e:
        result["error_text"] = str(e)
    return result


def subset_10pct_csv(task: str, out_dir: Path) -> Path:
    spec = TASKS[task]
    subset_path = out_dir / "data" / spec["subset_file"]
    df = pd.read_csv(spec["source"])
    parts = []
    if task == "TE":
        for _, grp in df.groupby(spec["group_col"], sort=True):
            n = max(1, min(len(grp), round(len(grp) * TE_FRAC)))
            parts.append(grp.sample(n=n, random_state=SEED))
    else:
        for _, grp in df.groupby(spec["group_col"], sort=True):
            n = max(1, min(len(grp), PER_CATEGORY))
            parts.append(grp.sample(n=n, random_state=SEED))
    out = pd.concat(parts).sort_index()
    subset_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(subset_path, index=False)
    return subset_path


def resolve_tasks(task_args: List[str]) -> List[str]:
    if "all" in task_args:
        return ["SI", "TR", "TE"]
    return task_args


def resolve_models(model_args: List[str], full: bool) -> List[str]:
    if full or "all" in model_args:
        return list(SG1_SIZES)
    return model_args


def resolve_out_dir(full: bool, task: str, override: Path | None) -> Path:
    if override is not None:
        return override
    if full:
        return SG1_RUN
    return R2 / TASKS[task]["smoke_dir"]


def resolve_input_path(task: str, full: bool, out_dir: Path) -> Path:
    spec = TASKS[task]
    if full:
        return spec["source"]
    return subset_10pct_csv(task, out_dir)


def run_experiment(
    out_dir: Path,
    task: str,
    lm_id: str,
    family: str,
    size: str,
    input_path: Path,
    full: bool,
) -> dict:
    spec = TASKS[task]
    suffix = "full" if full else "10pct"
    cmd = [
        str(ROOT / ".venv/bin/python"),
        "-m",
        "orchestration.run_experiment",
        "--base-dir",
        str(out_dir),
        "--experiment-name",
        f"shieldgemma_{size}_{task.lower()}_sg1_patched_{suffix}",
        "--model-family",
        family,
        "--model-size",
        size,
        "--model-version",
        "2.0",
        "--prompt-name",
        spec["prompt_name"],
        "--system",
        str(spec["system"]),
        "--input",
        str(input_path),
        "--temperature",
        "0",
        "--max-tokens",
        "256",
        "--num-replicates",
        "1",
    ]
    print("Running:", " ".join(cmd))
    p = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    print(p.stdout)
    if p.stderr:
        print(p.stderr, file=sys.stderr)
    return {"exit_code": p.returncode, "stdout_tail": (p.stdout or "")[-4000:]}


def summarize_cache(out_dir: Path, task: str, lm_id: str) -> dict:
    import sqlite3

    prompt_name = TASKS[task]["prompt_name"]
    db = out_dir / "cache/results.db"
    if not db.exists():
        return {"error": "no cache db"}
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT cr.status, COUNT(*),
               AVG(json_extract(cr.raw_response, '$.usage.completion_tokens'))
        FROM cached_results cr
        JOIN cache_keys ck ON cr.cache_id = ck.cache_id
        WHERE ck.model_full_name = ? AND ck.prompt_name = ?
        GROUP BY cr.status
        """,
        (lm_id, prompt_name),
    )
    summary = {
        row[0]: {"count": row[1], "avg_completion_tokens": row[2]} for row in cur.fetchall()
    }
    conn.close()
    return summary


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="ShieldGemma SG-1 patched-Jinja sensitivity")
    p.add_argument(
        "--task",
        nargs="+",
        choices=["SI", "TR", "TE", "all"],
        default=["SI"],
        help="Task(s). Use 'all' for SI+TR+TE.",
    )
    p.add_argument(
        "--smoke-test",
        action="store_true",
        help="10%% stratified subset on shieldgemma-2b (default when neither --full nor --snapshot-only)",
    )
    p.add_argument(
        "--full",
        action="store_true",
        help="Full finalized CSVs; all three models (2b, 9b, 27b) unless --models set",
    )
    p.add_argument(
        "--models",
        nargs="+",
        choices=["2b", "9b", "27b", "all"],
        default=["2b"],
        help="Model sizes to run (default 2b for smoke; all three when --full)",
    )
    p.add_argument(
        "--snapshot-only",
        action="store_true",
        help="Golden-backup live overrides only; no patch or inference",
    )
    p.add_argument("--out-dir", type=Path, default=None)
    p.add_argument("--run-id", default=None)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if not args.snapshot_only and not args.smoke_test and not args.full:
        args.smoke_test = True

    if not PATCHED_JINJA.exists():
        print(f"Missing patched template: {PATCHED_JINJA}", file=sys.stderr)
        return 1

    tasks = resolve_tasks(args.task)
    models = resolve_models(args.models, args.full)
    if args.full and len(tasks) > 1:
        out_dir = args.out_dir or SG1_RUN
    elif args.full:
        out_dir = args.out_dir or resolve_out_dir(True, tasks[0], None)
    else:
        if len(tasks) != 1:
            print("Smoke test supports one task at a time.", file=sys.stderr)
            return 1
        out_dir = args.out_dir or resolve_out_dir(False, tasks[0], None)

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    patched_template = PATCHED_JINJA.read_text()
    first_task = tasks[0]
    system_prompt = TASKS[first_task]["system"].read_text()
    spot_user = str(pd.read_csv(TASKS[first_task]["source"]).iloc[0][TASKS[first_task]["spot_col"]])

    manifest: Dict[str, Any] = {
        "mode": "full" if args.full else "smoke_test",
        "tasks": tasks,
        "models": models,
        "run_id": run_id,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "patched_jinja": str(PATCHED_JINJA),
        "patched_jinja_sha256": sha256_file(PATCHED_JINJA),
        "patch_description": "SG-1 embedded template + preamble mapping system message -> guideline",
        "golden_snapshots": {},
        "restore_verified": {},
        "experiments": [],
    }

    print(f"\n=== Step 1: golden snapshot (tasks={tasks}, run_id={run_id}) ===")
    manifest["golden_snapshots"] = snapshot_golden(SG1_CASES, run_id)

    manifest_path = GOLDEN_ROOT / run_id / "manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2))

    if args.snapshot_only:
        print(f"\nSnapshot only — wrote {manifest_path}")
        return 0

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "cache").mkdir(parents=True, exist_ok=True)

    failed = False
    break_tested: set[str] = set()

    try:
        for task in tasks:
            spec = TASKS[task]
            input_path = resolve_input_path(task, args.full, out_dir)
            n_rows = len(pd.read_csv(input_path))
            print(f"\n=== Task {task}: {input_path} ({n_rows} rows) ===")

            for size in models:
                lm_id = f"shieldgemma-{size}"
                case = case_by_id(lm_id)

                print(f"\n=== Apply patched SG-1 to {lm_id} ({task}) ===")
                apply_patched(case, patched_template)

                if lm_id not in break_tested:
                    print(f"\n=== Break test ({lm_id}, {task}) ===")
                    task_system = spec["system"].read_text()
                    spot = str(pd.read_csv(spec["source"]).iloc[0][spec["spot_col"]])
                    lms_load(lm_id)
                    bt = break_test_http(lm_id, task_system, spot)
                    manifest.setdefault("break_tests", {})[lm_id] = bt
                    print(
                        f"  http={bt['http_status']} content_preview="
                        f"{repr((bt.get('response_content') or '')[:120])}"
                    )
                    if bt.get("http_status") != 200:
                        print("Break test failed (HTTP != 200); aborting.", file=sys.stderr)
                        failed = True
                        return 1
                    break_tested.add(lm_id)

                print(f"\n=== Run {task} ({'full' if args.full else '10pct'}) on {lm_id} ===")
                lms_load(lm_id)
                run_info = run_experiment(
                    out_dir, task, lm_id, "shieldgemma", size, input_path, args.full
                )
                exp_record = {
                    "task": task,
                    "lm_studio_id": lm_id,
                    "input_csv": str(input_path),
                    "input_rows": n_rows,
                    **run_info,
                    "cache_summary": summarize_cache(out_dir, task, lm_id),
                }
                manifest["experiments"].append(exp_record)
                if run_info["exit_code"] != 0:
                    failed = True

    finally:
        print("\n=== Restore live overrides from golden snapshot ===")
        all_ok = True
        for case in SG1_CASES:
            rec = manifest["golden_snapshots"][case["lm_studio_id"]]
            ok = restore_from_record(case, rec)
            manifest["restore_verified"][case["lm_studio_id"]] = ok
            all_ok = all_ok and ok
        if not all_ok:
            print(
                "\n*** RESTORE MISMATCH — manually restore from:\n"
                f"    {GOLDEN_ROOT / run_id}\n",
                file=sys.stderr,
            )
            failed = True

    out_manifest = out_dir / "run_manifest.json"
    manifest["updated_at"] = datetime.now(timezone.utc).isoformat()
    out_manifest.write_text(json.dumps(manifest, indent=2))
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"\nManifest: {out_manifest}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
