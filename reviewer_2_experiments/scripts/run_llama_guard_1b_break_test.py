#!/usr/bin/env python3
"""Formal LM Studio break test for meta-llama_-_llama-guard-3-1b embedded Jinja.

Mirrors run_embedded_template_break_test.py (ShieldGemma) for the only other
non-ShieldGemma Jinja override in the study. Demonstrates that the GGUF-embedded
multimodal Llama-Guard-3-1B template cannot render our pipeline {system, user}
string payload, while the LM Studio text-only Guard override can.

Protocol (override JSON backed up + SHA256-verified restore):
  1. baseline_override         -> current text-only Guard override (from backup)
  2. embedded_as_override      -> inject embedded GGUF multimodal template as override
  3. no_override_gguf_embedded -> remove override file, fall back to GGUF embedded

Requires LM Studio on localhost:1234. Touches ONLY the llama-guard-3-1b override
JSON; restores it from backup in a finally block and verifies SHA256.
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
from r2_paths import BREAK_TESTS, ROOT, TEMPLATE_BACKUPS, TEMPLATES

BACKUP = TEMPLATE_BACKUPS / "embedded_template_break_test_backups"
OUT = BREAK_TESTS / "llama_guard_3_1b_break_test.json"
OVERRIDE_DIR = Path.home() / ".lmstudio/.internal/user-concrete-model-default-config"
OVERRIDE_REL = "RichardErkhov/meta-llama_-_Llama-Guard-3-1B-gguf/Llama-Guard-3-1B.Q8_0.gguf.json"
EMBEDDED_JINJA = TEMPLATES / "llama_guard_3_1b_templates" / "embedded_gguf_real.jinja"

MODEL_ID = "meta-llama_-_llama-guard-3-1b"
EMBEDDED_SHA256 = "df3965ba586f628bed4f3bb122cda2cc7502d5fdd87b525d4a3fea37831905f7"
OVERRIDE_JINJA_SHA256 = "3652a68adfcb5fc2a54a3aa52750b64d124a05901c07aaff67d1c1b5b300a857"


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def make_override_config(template: str) -> dict:
    """Match the existing llama-guard override structure (stopStrings: [])."""
    return {
        "preset": "",
        "operation": {
            "fields": [
                {
                    "key": "llm.prediction.promptTemplate",
                    "value": {
                        "type": "jinja",
                        "jinjaPromptTemplate": {"template": template},
                        "stopStrings": [],
                    },
                }
            ]
        },
        "load": {"fields": []},
    }


def override_jinja_sha256(override_path: Path) -> str:
    data = json.loads(override_path.read_text())
    template = (
        data["operation"]["fields"][0]["value"]["jinjaPromptTemplate"]["template"]
    )
    return sha256_text(template)


def classify(mode: str, attempt: dict) -> str:
    status = attempt.get("http_status")
    err = (attempt.get("error_text") or "")
    log = (attempt.get("log_stream_excerpt") or "")
    combined = (err + " " + log).lower()
    content = attempt.get("response_content") or ""

    if attempt.get("model_mismatch"):
        return "wrong_model_loaded"
    if status is None:
        return "connection_failed"
    if isinstance(status, int) and status >= 500:
        return "server_error"
    if isinstance(status, int) and status >= 400:
        if "jinja" in combined or "raise_exception" in combined or "alternate" in combined \
           or "iterable" in combined or "undefined" in combined or "selectattr" in combined:
            return "jinja_render_error_http400"
        return f"http_error_{status}"
    if status == 200:
        if mode == "baseline_override":
            low = content.strip().lower()
            if low.startswith("safe") or low.startswith("unsafe"):
                return "ok_guard_safe_unsafe"
            return "ok_unexpected_content"
        # 200 under the embedded template would itself be notable
        return "unexpected_200_under_embedded"
    return "unknown"


def run() -> dict:
    override_path = OVERRIDE_DIR / OVERRIDE_REL
    backup_path = BACKUP / OVERRIDE_REL
    backup_path.parent.mkdir(parents=True, exist_ok=True)

    if not override_path.exists():
        raise FileNotFoundError(f"Override JSON not found: {override_path}")

    embedded_template = EMBEDDED_JINJA.read_text()
    embedded_actual_sha = sha256_text(embedded_template)

    original_sha = sha256_file(override_path)
    override_jinja_sha = override_jinja_sha256(override_path)
    shutil.copy2(override_path, backup_path)

    system_prompt = (ROOT / "data/prompts/system_suicide_detection_v2.txt").read_text()
    user_text = str(
        pd.read_csv(ROOT / "data/inputs/finalized_input_data/SI_finalized_sentences.csv").iloc[0]["statement"]
    )

    report: Dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "lm_studio_id": MODEL_ID,
        "override_file": str(override_path),
        "embedded_jinja_source": str(EMBEDDED_JINJA),
        "embedded_jinja_sha256": embedded_actual_sha,
        "embedded_jinja_sha256_expected": EMBEDDED_SHA256,
        "embedded_jinja_sha256_match": embedded_actual_sha == EMBEDDED_SHA256,
        "original_override_sha256": original_sha,
        "override_jinja_sha256": override_jinja_sha,
        "override_jinja_sha256_expected": OVERRIDE_JINJA_SHA256,
        "override_jinja_sha256_match": override_jinja_sha == OVERRIDE_JINJA_SHA256,
        "method": "Backup override -> {baseline override, embedded-as-override, no-override GGUF} -> restore",
        "api_shape": "POST /v1/chat/completions: {system, user} string content, temperature=0",
        "user_text": user_text,
        "tests": [],
    }

    try:
        # 1. Baseline: current text-only Guard override
        shutil.copy2(backup_path, override_path)
        code, load_out, loaded_ids = load_model(MODEL_ID)
        a = try_completion(MODEL_ID, system_prompt, user_text)
        report["tests"].append({
            "mode": "baseline_override",
            "load_returncode": code,
            "loaded_model_ids": loaded_ids,
            "load_output_tail": load_out[-500:] if load_out else "",
            "outcome": classify("baseline_override", a),
            **a,
        })
        unload_all()

        # 2. Embedded GGUF multimodal template as override
        override_path.write_text(json.dumps(make_override_config(embedded_template), indent=2) + "\n")
        code, load_out, loaded_ids = load_model(MODEL_ID)
        b = try_completion(MODEL_ID, system_prompt, user_text)
        report["tests"].append({
            "mode": "embedded_as_override",
            "load_returncode": code,
            "loaded_model_ids": loaded_ids,
            "load_output_tail": load_out[-500:] if load_out else "",
            "outcome": classify("embedded_as_override", b),
            **b,
        })
        unload_all()

        # 3. No override file -> GGUF embedded template
        sidecar = override_path.with_suffix(".json.off")
        override_path.rename(sidecar)
        code, load_out, loaded_ids = load_model(MODEL_ID)
        c = try_completion(MODEL_ID, system_prompt, user_text)
        report["tests"].append({
            "mode": "no_override_gguf_embedded",
            "load_returncode": code,
            "loaded_model_ids": loaded_ids,
            "load_output_tail": load_out[-500:] if load_out else "",
            "outcome": classify("no_override_gguf_embedded", c),
            **c,
        })
        unload_all()
        sidecar.rename(override_path)

    finally:
        shutil.copy2(backup_path, override_path)
        restored_sha = sha256_file(override_path)
        report["restored_override_sha256"] = restored_sha
        report["restore_match"] = restored_sha == original_sha

    return report


def main() -> None:
    report = run()
    OUT.write_text(json.dumps(report, indent=2))
    print(f"Wrote {OUT}")
    print(f"embedded_jinja_sha256_match={report['embedded_jinja_sha256_match']}")
    print(f"override_jinja_sha256_match={report['override_jinja_sha256_match']}")
    print(f"restore_match={report['restore_match']}")
    errors: list[str] = []
    if not report["embedded_jinja_sha256_match"]:
        errors.append("embedded jinja SHA256 mismatch")
    if not report["override_jinja_sha256_match"]:
        errors.append("override jinja SHA256 mismatch")
    if not report["restore_match"]:
        errors.append("override file restore SHA256 mismatch")
    expected = {
        "baseline_override": "ok_guard_safe_unsafe",
        "embedded_as_override": "jinja_render_error_http400",
        "no_override_gguf_embedded": "jinja_render_error_http400",
    }
    for t in report["tests"]:
        print(f"  {t['mode']}: http={t['http_status']} outcome={t['outcome']}")
        if t.get("model_mismatch"):
            errors.append(
                f"{t['mode']}: API responded as {t.get('response_model')!r}, "
                f"expected {MODEL_ID!r}"
            )
        exp = expected.get(t["mode"])
        if exp and t["outcome"] != exp:
            errors.append(f"{t['mode']}: outcome={t['outcome']!r}, expected {exp!r}")
    if errors:
        for msg in errors:
            print(f"ERROR: {msg}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
