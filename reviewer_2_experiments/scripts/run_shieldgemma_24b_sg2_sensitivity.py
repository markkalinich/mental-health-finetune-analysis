#!/usr/bin/env python3
"""ShieldGemma 2-4b-it SG-2 multimodal-template sensitivity (reviewer response).

Applies patched embedded SG-2 Jinja (shieldgemma_sg2_patched_multimodal.jinja): maps pipeline
{system, user} to native image-moderation framing (<start_of_image>, BEGIN_SAFETY_POLICY, Yes/No).

Complements the SG-1 text patched arm (run_shieldgemma_24b_patched_sensitivity.py).

Safety: golden snapshot -> patch only 2-4b-it override -> try/finally restore.

Examples:
  .venv/bin/python reviewer_2_experiments/run_shieldgemma_24b_sg2_sensitivity.py --task SI --smoke-test
  .venv/bin/python reviewer_2_experiments/run_shieldgemma_24b_sg2_sensitivity.py --full --task all
  .venv/bin/python reviewer_2_experiments/run_shieldgemma_24b_sg2_sensitivity.py --snapshot-only
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
from r2_paths import R2, SG2_RUN, TEMPLATE_BACKUPS, TEMPLATES

OVERRIDE_DIR = Path.home() / ".lmstudio/.internal/user-concrete-model-default-config"
PATCHED_JINJA = TEMPLATES / "shieldgemma_sg2_patched_multimodal.jinja"
GOLDEN_ROOT = TEMPLATE_BACKUPS / "sg2_patched_sensitivity_backups"

LM_STUDIO_ID = "shieldgemma-2-4b-it"
MODEL_FAMILY = "shieldgemma"
MODEL_SIZE = "4b-it"
MODEL_VERSION = "3.0"
CASE = {
    "lm_studio_id": LM_STUDIO_ID,
    "override_rel": "infil00p/shieldgemma-2-4b-it-GGUF/shieldgemma-2-4b-it.gguf.json",
}

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
        "smoke_dir": "shieldgemma_24b_sg2_si_10pct_smoke",
    },
    "TR": {
        "source": ROOT / "data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv",
        "system": ROOT / "data/prompts/therapy_request_classifier_v3.txt",
        "prompt_name": "therapy_request_classifier_v3",
        "subset_file": "therapy_request_finalized_sentences_10pct.csv",
        "group_col": "therapy_request",
        "spot_col": "statement",
        "smoke_dir": "shieldgemma_24b_sg2_tr_10pct_smoke",
    },
    "TE": {
        "source": ROOT / "data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv",
        "system": ROOT / "data/prompts/therapy_engagement_conversation_prompt_v2.txt",
        "prompt_name": "therapy_engagement_conversation_prompt_v2",
        "subset_file": "therapy_engagement_finalized_sentences_10pct.csv",
        "group_col": "therapy_engagement",
        "spot_col": "statement",
        "smoke_dir": "shieldgemma_24b_sg2_te_10pct_smoke",
    },
}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def override_path() -> Path:
    return OVERRIDE_DIR / CASE["override_rel"]


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


def snapshot_golden(run_id: str) -> dict:
    live = override_path()
    if not live.exists():
        raise FileNotFoundError(f"Live override missing: {live}")
    golden = GOLDEN_ROOT / run_id / CASE["override_rel"]
    golden.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(live, golden)
    sha = sha256_file(golden)
    record = {
        "live_path": str(live),
        "golden_path": str(golden),
        "golden_sha256": sha,
    }
    print(f"  golden snapshot {LM_STUDIO_ID}: {golden} ({sha[:16]}…)")
    return record


def restore_from_record(record: dict) -> bool:
    live = override_path()
    golden = Path(record["golden_path"])
    shutil.copy2(golden, live)
    restored = sha256_file(live)
    ok = restored == record["golden_sha256"]
    print(f"  restore {LM_STUDIO_ID}: match={ok} sha={restored[:16]}…")
    return ok


def apply_patched(template: str) -> None:
    live = override_path()
    live.write_text(json.dumps(make_override_config(template), indent=2) + "\n")
    print(f"  applied SG-2 patched multimodal override -> {live}")


def lms_load() -> None:
    subprocess.run(["lms", "unload", "--all"], capture_output=True, text=True, timeout=120)
    p = subprocess.run(
        ["lms", "load", LM_STUDIO_ID, "-y", "-c", "4096"],
        capture_output=True,
        text=True,
        timeout=900,
    )
    if p.returncode != 0:
        raise RuntimeError(f"lms load {LM_STUDIO_ID} failed:\n{p.stderr or p.stdout}")


def break_test_http(system_prompt: str, user_text: str) -> dict:
    payload = {
        "model": LM_STUDIO_ID,
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
    return ["SI", "TR", "TE"] if "all" in task_args else task_args


def resolve_out_dir(full: bool, task: str, override: Path | None) -> Path:
    if override is not None:
        return override
    if full:
        return SG2_RUN
    return R2 / TASKS[task]["smoke_dir"]


def resolve_input_path(task: str, full: bool, out_dir: Path) -> Path:
    spec = TASKS[task]
    return spec["source"] if full else subset_10pct_csv(task, out_dir)


def run_experiment(out_dir: Path, task: str, input_path: Path, full: bool) -> dict:
    spec = TASKS[task]
    suffix = "full" if full else "10pct"
    cmd = [
        str(ROOT / ".venv/bin/python"),
        "-m",
        "orchestration.run_experiment",
        "--base-dir",
        str(out_dir),
        "--experiment-name",
        f"shieldgemma_24b_{task.lower()}_sg2_multimodal_{suffix}",
        "--model-family",
        MODEL_FAMILY,
        "--model-size",
        MODEL_SIZE,
        "--model-version",
        MODEL_VERSION,
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


def summarize_cache(out_dir: Path, task: str) -> dict:
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
        (LM_STUDIO_ID, prompt_name),
    )
    summary = {
        row[0]: {"count": row[1], "avg_completion_tokens": row[2]} for row in cur.fetchall()
    }
    conn.close()
    return summary


def main() -> int:
    p = argparse.ArgumentParser(description="ShieldGemma 2-4b-it SG-2 multimodal sensitivity")
    p.add_argument("--task", nargs="+", choices=["SI", "TR", "TE", "all"], default=["SI"])
    p.add_argument("--smoke-test", action="store_true")
    p.add_argument("--full", action="store_true")
    p.add_argument("--snapshot-only", action="store_true")
    p.add_argument("--out-dir", type=Path, default=None)
    p.add_argument("--run-id", default=None)
    args = p.parse_args()

    if not args.snapshot_only and not args.smoke_test and not args.full:
        args.smoke_test = True

    if not PATCHED_JINJA.exists():
        print(f"Missing patched template: {PATCHED_JINJA}", file=sys.stderr)
        return 1

    tasks = resolve_tasks(args.task)
    if args.full and len(tasks) > 1:
        out_dir = args.out_dir or SG2_RUN
    elif args.full:
        out_dir = args.out_dir or resolve_out_dir(True, tasks[0], None)
    else:
        if len(tasks) != 1:
            print("Smoke test supports one task at a time.", file=sys.stderr)
            return 1
        out_dir = args.out_dir or resolve_out_dir(False, tasks[0], None)

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    patched_template = PATCHED_JINJA.read_text()

    manifest: Dict[str, Any] = {
        "model": LM_STUDIO_ID,
        "model_size": MODEL_SIZE,
        "model_version": MODEL_VERSION,
        "mode": "full" if args.full else "smoke_test",
        "tasks": tasks,
        "run_id": run_id,
        "patched_jinja": str(PATCHED_JINJA),
        "patched_jinja_sha256": sha256_file(PATCHED_JINJA),
        "patch_description": (
            "Patched embedded SG-2 multimodal template: system+user -> "
            "<start_of_image> + BEGIN_SAFETY_POLICY + Yes/No question. "
            "Off-label text probe; image slot is placeholder only."
        ),
        "golden_snapshot": {},
        "restore_verified": False,
        "experiments": [],
    }

    print(f"\n=== Step 1: golden snapshot (run_id={run_id}) ===")
    manifest["golden_snapshot"] = snapshot_golden(run_id)
    manifest_path = GOLDEN_ROOT / run_id / f"manifest_sg2_{run_id}.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2))

    if args.snapshot_only:
        print(f"Snapshot only — wrote {manifest_path}")
        return 0

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "cache").mkdir(parents=True, exist_ok=True)
    failed = False
    break_tested = False

    try:
        for task in tasks:
            spec = TASKS[task]
            input_path = resolve_input_path(task, args.full, out_dir)
            n_rows = len(pd.read_csv(input_path))
            print(f"\n=== Task {task}: {input_path} ({n_rows} rows) ===")

            print(f"\n=== Apply SG-2 patched multimodal template to {LM_STUDIO_ID} ({task}) ===")
            apply_patched(patched_template)

            if not break_tested:
                print(f"\n=== Break test ({LM_STUDIO_ID}, {task}) ===")
                task_system = spec["system"].read_text()
                spot = str(pd.read_csv(spec["source"]).iloc[0][spec["spot_col"]])
                lms_load()
                bt = break_test_http(task_system, spot)
                manifest["break_test"] = bt
                print(
                    f"  http={bt['http_status']} content_preview="
                    f"{repr((bt.get('response_content') or '')[:120])}"
                )
                if bt.get("http_status") != 200:
                    print("Break test failed (HTTP != 200); aborting.", file=sys.stderr)
                    return 1
                break_tested = True

            print(f"\n=== Run {task} ({'full' if args.full else '10pct'}) on {LM_STUDIO_ID} ===")
            lms_load()
            run_info = run_experiment(out_dir, task, input_path, args.full)
            exp_record = {
                "task": task,
                "lm_studio_id": LM_STUDIO_ID,
                "input_csv": str(input_path),
                "input_rows": n_rows,
                **run_info,
                "cache_summary": summarize_cache(out_dir, task),
            }
            manifest["experiments"].append(exp_record)
            if run_info["exit_code"] != 0:
                failed = True

    finally:
        print("\n=== Restore live override from golden snapshot ===")
        ok = restore_from_record(manifest["golden_snapshot"])
        manifest["restore_verified"] = ok
        if not ok:
            print(
                f"\n*** RESTORE MISMATCH — manually restore from:\n    {manifest['golden_snapshot']['golden_path']}\n",
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
