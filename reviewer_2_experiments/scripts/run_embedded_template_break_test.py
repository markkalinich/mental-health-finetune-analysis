#!/usr/bin/env python3
"""Demonstrate LM Studio failure/wrong behavior with embedded ShieldGemma Jinja templates.

Temporarily swaps override JSON to embedded GGUF template, sends pipeline-style API
request, captures outcome, restores originals. Writes artifact JSON + restores verified by sha256.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from lmstudio_runtime_utils import load_model, try_completion, unload_all
from r2_paths import BREAK_TESTS, PROVENANCE, ROOT, TEMPLATE_BACKUPS, TEMPLATES

BACKUP = TEMPLATE_BACKUPS / "embedded_template_break_test_backups"
OUT = BREAK_TESTS / "shieldgemma_embedded_template_break_test.json"
OVERRIDE_DIR = Path.home() / ".lmstudio/.internal/user-concrete-model-default-config"
SUBTASK1 = PROVENANCE / "subtask1_embedded_templates.json"

CASES = [
    {
        "lm_studio_id": "shieldgemma-2b",
        "override_rel": "QuantFactory/shieldgemma-2b-GGUF/shieldgemma-2b.Q8_0.gguf.json",
        "embedded_key": "shieldgemma-2b",
        "template_label": "Template A (text ShieldGemma)",
    },
    {
        "lm_studio_id": "shieldgemma-9b",
        "override_rel": "QuantFactory/shieldgemma-9b-GGUF/shieldgemma-9b.Q8_0.gguf.json",
        "embedded_key": "shieldgemma-9b",
        "template_label": "Template A (text ShieldGemma)",
    },
    {
        "lm_studio_id": "shieldgemma-27b",
        "override_rel": "mradermacher/shieldgemma-27b-GGUF/shieldgemma-27b.Q8_0.gguf.json",
        "embedded_key": "shieldgemma-27b",
        "template_label": "Template A (text ShieldGemma)",
    },
    {
        "lm_studio_id": "shieldgemma-2-4b-it",
        "override_rel": "infil00p/shieldgemma-2-4b-it-GGUF/shieldgemma-2-4b-it.gguf.json",
        "embedded_key": "shieldgemma-2-4b-it",
        "template_label": "Template B (multimodal ShieldGemma)",
    },
]


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_embedded_templates() -> Dict[str, str]:
    rows = json.loads(SUBTASK1.read_text())
    return {r["lm_studio_id"]: r["embedded_chat_template"] for r in rows if r["lm_studio_id"].startswith("shieldgemma")}


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


def classify_outcome(case: dict, mode: str, attempt: dict) -> str:
    if attempt.get("model_mismatch"):
        return "wrong_model_loaded"
    status = attempt.get("http_status")
    body = attempt.get("response_body")
    err = attempt.get("error_text") or ""
    log = attempt.get("log_stream_excerpt") or ""
    combined = err + log + json.dumps(body, default=str) if body is not None else err + log

    if status is None or (isinstance(status, int) and status >= 500):
        return "server_error"
    if isinstance(status, int) and status >= 400:
        return "http_error"
    if "raise_exception" in combined.lower() or "jinja" in combined.lower() and "error" in combined.lower():
        return "jinja_render_error"
    if "error" in log.lower() and "input" not in log.lower():
        return "logged_error"

    if mode == "embedded_original":
        if case["template_label"].startswith("Template B"):
            if status == 200 and isinstance(body, dict):
                content = body.get("choices", [{}])[0].get("message", {}).get("content", "")
                if content:
                    return "wrong_success_or_nonsense"
            return "broken_or_empty"
        # Template A: missing guideline — policy not wired; may still return 200
        if "Human Question:" in log and "<start_of_turn>system" not in log:
            return "renders_wrong_shape"
        if status == 200 and isinstance(body, dict):
            content = body.get("choices", [{}])[0].get("message", {}).get("content", "")
            if "* \n" in log or "guideline" in combined.lower():
                return "missing_guideline_empty_policy"
            if "Human Question:" in log:
                return "ignores_system_policy"
        if status == 200:
            return "http_ok_but_wrong_prompt"

    if status == 200:
        return "success"
    return "unknown"


def run_case(case: dict, embedded: str, system_prompt: str, user_text: str) -> Dict[str, Any]:
    override_path = OVERRIDE_DIR / case["override_rel"]
    backup_path = BACKUP / case["override_rel"]
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    original_sha = sha256_file(override_path)
    shutil.copy2(override_path, backup_path)

    results: Dict[str, Any] = {
        "lm_studio_id": case["lm_studio_id"],
        "template_label": case["template_label"],
        "override_file": str(override_path),
        "original_override_sha256": original_sha,
        "tests": [],
    }

    try:
        # Baseline: current generic override (restore from backup first)
        shutil.copy2(backup_path, override_path)
        code, load_out, loaded_ids = load_model(case["lm_studio_id"])
        baseline = try_completion(case["lm_studio_id"], system_prompt, user_text)
        results["tests"].append(
            {
                "mode": "baseline_generic_override",
                "load_returncode": code,
                "loaded_model_ids": loaded_ids,
                "load_output_tail": load_out[-500:] if load_out else "",
                "outcome": classify_outcome(case, "baseline", baseline),
                **baseline,
            }
        )
        unload_all()

        # Embedded original as override
        override_path.write_text(json.dumps(make_override_config(embedded), indent=2) + "\n")
        code, load_out, loaded_ids = load_model(case["lm_studio_id"])
        embedded_attempt = try_completion(case["lm_studio_id"], system_prompt, user_text)
        results["tests"].append(
            {
                "mode": "embedded_original_as_override",
                "load_returncode": code,
                "loaded_model_ids": loaded_ids,
                "load_output_tail": load_out[-500:] if load_out else "",
                "outcome": classify_outcome(case, "embedded_original", embedded_attempt),
                **embedded_attempt,
            }
        )
        unload_all()

        # No override file — fall back to GGUF embedded template
        sidecar = override_path.with_suffix(".json.off")
        override_path.rename(sidecar)
        code, load_out, loaded_ids = load_model(case["lm_studio_id"])
        no_ov = try_completion(case["lm_studio_id"], system_prompt, user_text)
        results["tests"].append(
            {
                "mode": "no_override_gguf_embedded",
                "load_returncode": code,
                "loaded_model_ids": loaded_ids,
                "load_output_tail": load_out[-500:] if load_out else "",
                "outcome": classify_outcome(case, "embedded_original", no_ov),
                **no_ov,
            }
        )
        unload_all()
        sidecar.rename(override_path)

    finally:
        shutil.copy2(backup_path, override_path)
        restored_sha = sha256_file(override_path)
        results["restored_override_sha256"] = restored_sha
        results["restore_match"] = restored_sha == original_sha

    return results


def main() -> None:
    embedded_map = load_embedded_templates()
    system_prompt = (ROOT / "data/prompts/system_suicide_detection_v2.txt").read_text()
    user_text = str(
        pd.read_csv(ROOT / "data/inputs/finalized_input_data/SI_finalized_sentences.csv").iloc[0]["statement"]
    )

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "method": "Backup override JSON -> swap to embedded tokenizer.chat_template -> pipeline {system,user} API -> restore",
        "api_shape": "orchestration/api_client.py: system + user messages, no guideline, no multimodal content",
        "cases": [],
    }

    for case in CASES:
        print(f"Testing {case['lm_studio_id']}...", flush=True)
        report["cases"].append(
            run_case(case, embedded_map[case["embedded_key"]], system_prompt, user_text)
        )

    OUT.write_text(json.dumps(report, indent=2))
    print(f"Wrote {OUT}")
    for c in report["cases"]:
        print(f"\n=== {c['lm_studio_id']} restore_match={c['restore_match']} ===")
        for t in c["tests"]:
            print(f"  {t['mode']}: http={t['http_status']} outcome={t['outcome']}")


if __name__ == "__main__":
    main()
