#!/usr/bin/env python3
"""Empirical chat-template audit for reviewer comment #2 (safety models only).

Writes raw command outputs under reviewer_2_experiments/data/provenance/.
Does NOT modify cache/results.db or committed results CSVs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import requests
from gguf import GGUFReader

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from lmstudio_override_utils import extract_jinja_override
from r2_paths import PROVENANCE

ART = PROVENANCE
AUDIT_PATH = PROVENANCE / "all_models_gguf_sha256_audit.json"
ART.mkdir(parents=True, exist_ok=True)

MODELS = [
    {
        "lm_studio_id": "shieldgemma-2b",
        "family": "shieldgemma",
        "size": "2b",
        "gguf": Path.home() / ".lmstudio/models/QuantFactory/shieldgemma-2b-GGUF/shieldgemma-2b.Q8_0.gguf",
        "arch": "gemma",
        "control_token": "<start_of_turn>",
        "override_rel": "QuantFactory/shieldgemma-2b-GGUF/shieldgemma-2b.Q8_0.gguf.json",
    },
    {
        "lm_studio_id": "shieldgemma-2-4b-it",
        "family": "shieldgemma",
        "size": "4b-it",
        "gguf": Path.home() / ".lmstudio/models/infil00p/shieldgemma-2-4b-it-GGUF/shieldgemma-2-4b-it.gguf",
        "arch": "gemma",
        "control_token": "<start_of_turn>",
        "override_rel": "infil00p/shieldgemma-2-4b-it-GGUF/shieldgemma-2-4b-it.gguf.json",
        "failure_model": True,
    },
    {
        "lm_studio_id": "shieldgemma-9b",
        "family": "shieldgemma",
        "size": "9b",
        "gguf": Path.home() / ".lmstudio/models/QuantFactory/shieldgemma-9b-GGUF/shieldgemma-9b.Q8_0.gguf",
        "arch": "gemma",
        "control_token": "<start_of_turn>",
        "override_rel": "QuantFactory/shieldgemma-9b-GGUF/shieldgemma-9b.Q8_0.gguf.json",
        "failure_model": True,
    },
    {
        "lm_studio_id": "shieldgemma-27b",
        "family": "shieldgemma",
        "size": "27b",
        "gguf": Path.home() / ".lmstudio/models/mradermacher/shieldgemma-27b-GGUF/shieldgemma-27b.Q8_0.gguf",
        "arch": "gemma",
        "control_token": "<start_of_turn>",
        "override_rel": "mradermacher/shieldgemma-27b-GGUF/shieldgemma-27b.Q8_0.gguf.json",
    },
    {
        "lm_studio_id": "meta-llama_-_llama-guard-3-1b",
        "family": "llama_guard",
        "size": "1b",
        "gguf": Path.home() / ".lmstudio/models/RichardErkhov/meta-llama_-_Llama-Guard-3-1B-gguf/Llama-Guard-3-1B.Q8_0.gguf",
        "arch": "llama",
        "control_token": "<|start_header_id|>",
        "override_rel": "RichardErkhov/meta-llama_-_Llama-Guard-3-1B-gguf/Llama-Guard-3-1B.Q8_0.gguf.json",
    },
    {
        "lm_studio_id": "llama-guard-3-8b",
        "family": "llama_guard",
        "size": "8b",
        "gguf": Path.home() / ".lmstudio/models/Mungert/Llama-Guard-3-8B-GGUF/Llama-Guard-3-8B-q8_0.gguf",
        "arch": "llama",
        "control_token": "<|start_header_id|>",
        "override_rel": None,
    },
    {
        "lm_studio_id": "qwen3guard-gen-0.6b",
        "family": "qwen_guard",
        "size": "0.6b",
        "gguf": Path.home() / ".lmstudio/models/QuantFactory/Qwen3Guard-Gen-0.6B-GGUF/Qwen3Guard-Gen-0.6B.Q8_0.gguf",
        "arch": "qwen",
        "control_token": "<|im_start|>",
        "override_rel": None,
    },
    {
        "lm_studio_id": "qwen3guard-gen-4b",
        "family": "qwen_guard",
        "size": "4b",
        "gguf": Path.home() / ".lmstudio/models/mradermacher/Qwen3Guard-Gen-4B-GGUF/Qwen3Guard-Gen-4B.Q8_0.gguf",
        "arch": "qwen",
        "control_token": "<|im_start|>",
        "override_rel": None,
    },
    {
        "lm_studio_id": "qwen3guard-gen-8b",
        "family": "qwen_guard",
        "size": "8b",
        "gguf": Path.home() / ".lmstudio/models/ShahzebKhoso/Qwen3Guard-Gen-8B-GGUF/Qwen3Guard-Gen-8B-Q8_0.gguf",
        "arch": "qwen",
        "control_token": "<|im_start|>",
        "override_rel": None,
    },
]

OVERRIDE_DIR = Path.home() / ".lmstudio/.internal/user-concrete-model-default-config"
HTTP_CFG = Path.home() / ".lmstudio/.internal/http-server-config.json"
LOG_DIR = Path.home() / ".lmstudio/server-logs"
PROMPTS = {
    "SI": ROOT / "data/prompts/system_suicide_detection_v2.txt",
    "TR": ROOT / "data/prompts/therapy_request_classifier_v3.txt",
    "TE": ROOT / "data/prompts/therapy_engagement_conversation_prompt_v2.txt",
}
INPUTS = {
    "SI": ROOT / "data/inputs/finalized_input_data/SI_finalized_sentences.csv",
    "TR": ROOT / "data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv",
    "TE": ROOT / "data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv",
}
TEXT_COL = {
    "SI": "statement",
    "TR": "statement",
    "TE": "statement",
}


def run(cmd: List[str], timeout: int = 600) -> Tuple[int, str, str]:
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def capture_rendered_input(model_id: str, system_prompt: str, user_text: str) -> Tuple[str, dict]:
    """Return (rendered_prompt, api_response) using lms log stream input filter."""
    proc = subprocess.Popen(
        ["lms", "log", "stream", "-s", "model", "--filter", "input"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    time.sleep(1)
    resp = api_chat(model_id, system_prompt, user_text)
    time.sleep(2)
    proc.terminate()
    stream_out, _ = proc.communicate(timeout=5)
    rendered = ""
    if "input:" in stream_out:
        rendered = stream_out.split("input:", 1)[1].strip()
    return rendered, resp


def dump_gguf_template(gguf_path: Path) -> Tuple[bool, str]:
    reader = GGUFReader(str(gguf_path))
    for field in reader.fields.values():
        if field.name == "tokenizer.chat_template":
            val = field.parts[field.data[0]]
            if hasattr(val, "tobytes"):
                val = val.tobytes().decode("utf-8", errors="replace")
            elif isinstance(val, bytes):
                val = val.decode("utf-8", errors="replace")
            else:
                val = str(val)
            return True, val
    return False, ""


def load_override(rel: Optional[str]) -> Optional[dict]:
    if not rel:
        return None
    p = OVERRIDE_DIR / rel
    if not p.exists():
        return None
    return json.loads(p.read_text())


def current_parse_rates() -> Dict[Tuple[str, str], float]:
    p = ROOT / "data/inputs/model_results/all_models_all_tasks.csv"
    df = pd.read_csv(p)
    out = {}
    for m in MODELS:
        sub = df[(df["model_family"] == m["family"]) & (df["model_size"] == m["size"])]
        for _, r in sub.iterrows():
            out[(m["lm_studio_id"], r["task"])] = float(r["parse_success_rate"])
    return out


def sample_text(task: str, n: int = 20) -> str:
    df = pd.read_csv(INPUTS[task])
    col = TEXT_COL[task]
    row = df.iloc[0]
    return str(row[col])


def latest_log_file() -> Path:
    files = sorted(LOG_DIR.rglob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        raise FileNotFoundError("No LM Studio server logs found")
    return files[0]


def log_byte_offset() -> int:
    return latest_log_file().stat().st_size


def read_log_since(offset: int) -> str:
    p = latest_log_file()
    with p.open("rb") as f:
        f.seek(offset)
        return f.read().decode("utf-8", errors="replace")


def api_chat(model: str, system_prompt: str, user_text: str) -> dict:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text},
        ],
        "temperature": 0.0,
        "max_tokens": 512,
        "stream": False,
    }
    r = requests.post("http://localhost:1234/v1/chat/completions", json=payload, timeout=300)
    r.raise_for_status()
    return r.json()


def load_model(model_id: str) -> None:
    run(["lms", "unload", "--all"], timeout=120)
    code, out, err = run(["lms", "load", model_id, "-y", "-c", "4096"], timeout=900)
    if code != 0:
        raise RuntimeError(f"lms load {model_id} failed: {err or out}")


def extract_rendered_prompt(log_text: str) -> Optional[str]:
    # LM Studio verbose + logSensitiveData may log detokenized prompt fragments
    patterns = [
        r"Formatted prompt:\s*(.+)",
        r"Rendered prompt:\s*(.+)",
        r"prompt text:\s*(.+)",
        r"slot prompt:\s*(.+)",
    ]
    for pat in patterns:
        m = re.search(pat, log_text, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    # Fallback: capture Received request body (API messages, not rendered)
    m = re.search(r"Received request: POST to /v1/chat/completions with body (\{[\s\S]*?\})\n", log_text)
    if m:
        return "[API request body, not fully rendered] " + m.group(1)[:500]
    return None


def parse_response_content(resp: dict) -> Tuple[str, str]:
    content = resp.get("choices", [{}])[0].get("message", {}).get("content", "")
    finish = resp.get("choices", [{}])[0].get("finish_reason", "")
    return content, finish


def load_audit_by_id() -> Dict[str, dict]:
    if not AUDIT_PATH.exists():
        return {}
    audit = json.loads(AUDIT_PATH.read_text())
    return {m["lm_studio_id"]: m for m in audit.get("models", [])}


def build_subtask1_rows(audit_by_id: Dict[str, dict]) -> List[dict]:
    rows: List[dict] = []
    for m in MODELS:
        present, tmpl = dump_gguf_template(m["gguf"])
        ov = load_override(m["override_rel"])
        has_override, override_tmpl, _, _ = extract_jinja_override(ov)
        audit = audit_by_id.get(m["lm_studio_id"], {})
        row: dict = {
            "lm_studio_id": m["lm_studio_id"],
            "gguf_path": str(m["gguf"]),
            "embedded_chat_template": tmpl if present else "",
            "local_sha256": audit.get("local_sha256", ""),
            "sha256_match": bool(audit.get("sha256_match") or audit.get("status") == "VERIFIED_match"),
            "jinja_override": has_override,
        }
        if has_override and override_tmpl:
            row["jinja_override_template"] = override_tmpl
            row["jinja_override_sha256"] = hashlib.sha256(override_tmpl.encode()).hexdigest()
        rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="9 safety-model chat template audit")
    parser.add_argument(
        "--write-subtask1",
        type=Path,
        help="Optional: write subtask1_embedded_templates.json schema to this path",
    )
    args = parser.parse_args()

    sys.path.insert(0, str(ROOT))
    from utilities.schemas import extract_first_json_object, validate_and_coerce

    embedded_rows = []
    for m in MODELS:
        present, tmpl = dump_gguf_template(m["gguf"])
        row = {
            "lm_studio_id": m["lm_studio_id"],
            "gguf_path": str(m["gguf"]),
            "embedded_present": "Y" if present else "N",
            "embedded_first_200": tmpl[:200] if present else "",
        }
        embedded_rows.append(row)
        (ART / f"embedded_{m['lm_studio_id']}.txt").write_text(tmpl if present else "<none>")
    (ART / "embedded_templates.json").write_text(json.dumps(embedded_rows, indent=2))

    # Confirm verbose logging config (empirical read, no assumptions)
    http_cfg = json.loads(HTTP_CFG.read_text())
    (ART / "http_server_config_snapshot.json").write_text(json.dumps(http_cfg, indent=2))

    override_audit = []
    for m in MODELS:
        ov = load_override(m["override_rel"])
        override_audit.append(
            {
                "lm_studio_id": m["lm_studio_id"],
                "override_file": str(OVERRIDE_DIR / m["override_rel"]) if m["override_rel"] else None,
                "override_present": "Y" if ov else "N",
                "override_type": (ov or {}).get("operation", {}).get("fields", [{}])[0].get("value", {}).get("type")
                if ov
                else None,
            }
        )
    (ART / "override_audit.json").write_text(json.dumps(override_audit, indent=2))

    si_prompt = PROMPTS["SI"].read_text()
    user_text = sample_text("SI", 1)

    rendered_rows = []
    live_rows = []
    for m in MODELS:
        print(f"Loading {m['lm_studio_id']}...", flush=True)
        load_model(m["lm_studio_id"])
        time.sleep(2)
        try:
            rendered, resp = capture_rendered_input(m["lm_studio_id"], si_prompt, user_text)
        except Exception as e:
            live_rows.append({"model": m["lm_studio_id"], "error": str(e)})
            continue
        (ART / f"rendered_{m['lm_studio_id']}.txt").write_text(rendered or "<no input captured>")
        content, finish = parse_response_content(resp)
        parsed = validate_and_coerce(extract_first_json_object(content) if content else None)
        rendered_rows.append(
            {
                "lm_studio_id": m["lm_studio_id"],
                "expected_control_token": m["control_token"],
                "control_in_rendered": "Y" if rendered and m["control_token"] in rendered else "N",
                "rendered_first_200": rendered[:200] if rendered else "",
                "assistant_content_first_200": content[:200],
                "finish_reason": finish,
                "parse_ok_live": parsed is not None,
            }
        )
        live_rows.append(
            {
                "model": m["lm_studio_id"],
                "content_len": len(content),
                "finish_reason": finish,
                "parse_ok": parsed is not None,
            }
        )
    (ART / "rendered_prompt_audit.json").write_text(json.dumps(rendered_rows, indent=2))
    (ART / "live_single_request.json").write_text(json.dumps(live_rows, indent=2))

    # Failure diagnosis from committed cache (read-only)
    db = ROOT / "cache/results.db"
    diag = {}
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    for mid in ["shieldgemma-9b", "shieldgemma-2-4b-it"]:
        rows = conn.execute(
            """
            SELECT cr.status, cr.raw_response, ck.prompt_name
            FROM cached_results cr JOIN cache_keys ck ON cr.cache_id = ck.cache_id
            WHERE ck.model_full_name = ?
            """,
            (mid,),
        ).fetchall()
        st = Counter(r["status"] for r in rows)
        empty = 0
        wrong_schema = 0
        jinja_err = 0
        for r in rows:
            if r["status"] != "ok":
                try:
                    data = json.loads(r["raw_response"])
                    content = data["choices"][0]["message"]["content"]
                except Exception:
                    content = ""
                if "jinja" in (r["raw_response"] or "").lower() or "template" in (r["raw_response"] or "").lower():
                    jinja_err += 1
                elif not content or not str(content).strip():
                    empty += 1
                elif "is_si" in content or "Safety:" in content or content.strip().lower() in ("safe", "unsafe"):
                    wrong_schema += 1
                else:
                    wrong_schema += 1
        diag[mid] = {
            "status_counts": dict(st),
            "failure_empty_content": empty,
            "failure_wrong_schema_or_non_json": wrong_schema,
            "failure_jinja_in_response": jinja_err,
        }
    (ART / "failure_diagnosis.json").write_text(json.dumps(diag, indent=2))

    if args.write_subtask1:
        subtask1 = build_subtask1_rows(load_audit_by_id())
        args.write_subtask1.parent.mkdir(parents=True, exist_ok=True)
        args.write_subtask1.write_text(json.dumps(subtask1, indent=2))
        print(f"Wrote subtask1 schema -> {args.write_subtask1}")

    print("Done. Artifacts in", ART)


if __name__ == "__main__":
    main()
