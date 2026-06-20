"""Shared LM Studio load/unload helpers for reviewer break tests."""
from __future__ import annotations

import subprocess
import time
from typing import Any, Dict, List, Tuple

import requests

DEFAULT_CONTEXT = "4096"
UNLOAD_SETTLE_SEC = 2.0
LOAD_SETTLE_SEC = 1.0
PS_RETRIES = 10
PS_RETRY_SEC = 0.5


def _run_lms(args: List[str], *, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["lms", *args],
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def list_loaded_model_ids() -> List[str]:
    proc = _run_lms(["ps"])
    if proc.returncode != 0:
        raise RuntimeError(
            f"lms ps failed (exit {proc.returncode}): {(proc.stderr or proc.stdout or '').strip()}"
        )
    out = proc.stdout or ""
    if "No models are currently loaded" in out:
        return []
    ids: List[str] = []
    for line in out.splitlines():
        line = line.strip()
        if not line or line.startswith("IDENTIFIER") or line.startswith("To load"):
            continue
        parts = line.split()
        if parts:
            ids.append(parts[0])
    return ids


def unload_all(*, settle_sec: float = UNLOAD_SETTLE_SEC) -> None:
    proc = _run_lms(["unload", "--all"], timeout=120)
    if proc.returncode != 0:
        tail = (proc.stderr or proc.stdout or "").strip()[-500:]
        raise RuntimeError(f"lms unload --all failed (exit {proc.returncode}): {tail}")
    if settle_sec > 0:
        time.sleep(settle_sec)
    for attempt in range(PS_RETRIES):
        loaded = list_loaded_model_ids()
        if not loaded:
            return
        if attempt == PS_RETRIES - 1:
            raise RuntimeError(f"models still loaded after unload --all: {loaded}")
        time.sleep(PS_RETRY_SEC)


def load_model(
    model_id: str,
    *,
    context_length: str = DEFAULT_CONTEXT,
    settle_sec: float = LOAD_SETTLE_SEC,
) -> Tuple[int, str, List[str]]:
    unload_all()
    proc = _run_lms(
        ["load", model_id, "-y", "-c", context_length],
        timeout=900,
    )
    load_out = (proc.stderr or "") + (proc.stdout or "")
    if proc.returncode != 0:
        raise RuntimeError(
            f"lms load {model_id!r} failed (exit {proc.returncode}): {load_out[-500:]}"
        )
    if settle_sec > 0:
        time.sleep(settle_sec)
    loaded: List[str] = []
    for attempt in range(PS_RETRIES):
        loaded = list_loaded_model_ids()
        if model_id in loaded:
            if len(loaded) == 1:
                return proc.returncode, load_out, loaded
            raise RuntimeError(
                f"expected only {model_id!r} loaded, but lms ps shows: {loaded}"
            )
        if attempt == PS_RETRIES - 1:
            raise RuntimeError(
                f"{model_id!r} not listed in lms ps after load; loaded={loaded or '(none)'}"
            )
        time.sleep(PS_RETRY_SEC)
    return proc.returncode, load_out, loaded


def pipeline_payload(model_id: str, system_prompt: str, user_text: str) -> dict:
    return {
        "model": model_id,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text},
        ],
        "temperature": 0.0,
        "max_tokens": 128,
        "stream": False,
    }


def response_model_ids(body: Any) -> List[str]:
    ids: List[str] = []
    if not isinstance(body, dict):
        return ids
    model = body.get("model")
    if isinstance(model, str) and model:
        ids.append(model)
    fp = body.get("system_fingerprint")
    if isinstance(fp, str) and fp and fp not in ids:
        ids.append(fp)
    return ids


def try_completion(model_id: str, system_prompt: str, user_text: str) -> dict:
    proc = subprocess.Popen(
        ["lms", "log", "stream", "-s", "model", "--filter", "input"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    time.sleep(1)
    result: Dict[str, Any] = {
        "http_status": None,
        "response_body": None,
        "error_text": None,
        "response_content": None,
        "response_model": None,
        "response_system_fingerprint": None,
        "model_mismatch": False,
        "log_stream_excerpt": "",
    }
    try:
        r = requests.post(
            "http://localhost:1234/v1/chat/completions",
            json=pipeline_payload(model_id, system_prompt, user_text),
            timeout=180,
        )
        result["http_status"] = r.status_code
        try:
            body = r.json()
            result["response_body"] = body
            if isinstance(body, dict):
                result["response_model"] = body.get("model")
                result["response_system_fingerprint"] = body.get("system_fingerprint")
                result["response_content"] = (
                    body.get("choices", [{}])[0].get("message", {}).get("content")
                )
                seen = response_model_ids(body)
                if seen and model_id not in seen:
                    result["model_mismatch"] = True
        except Exception:
            result["response_body"] = r.text[:2000]
        if not r.ok:
            result["error_text"] = r.text[:2000]
    except requests.RequestException as e:
        result["error_text"] = str(e)
    time.sleep(2)
    proc.terminate()
    try:
        out, _ = proc.communicate(timeout=5)
        result["log_stream_excerpt"] = (out or "")[:4000]
    except Exception:
        pass
    return result
