#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OpenAI chat-completions calls with a local SQLite cache.

Adapted from conversation-trajectory-multiturn-benchmark ``src/clients/openai.py``
and ``src/cache.py``. This copy talks to api.openai.com with ``requests``
because this project's venv does not have the OpenAI SDK. It does not use
``cache/result_cache.py``: that database is the local sentence-task cache.

A cached ``ok`` or ``refusal`` is returned without a new request. A cached
``api_error`` is returned only when the error is a context-length or other
invalid request, so a rerun does not pay for the same rejection. Other errors
are tried again.

``reasoning_effort`` is part of the cache key. The trajectory lookup omitted it.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import random
import sqlite3
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

import requests

logger = logging.getLogger(__name__)

API_URL = "https://api.openai.com/v1/chat/completions"
MAX_RETRIES = 1
RETRY_BACKOFF_BASE_SEC = 2.0
DEFAULT_TIMEOUT_SECONDS = 600.0
TERMINAL_ERROR_MARKERS = (
    "context_length_exceeded",
    "context_length",
    "invalid_request_error",
    "maximum context length",
)

Transport = Callable[[str, Dict[str, str], Dict[str, Any], float], requests.Response]


class RefusalError(RuntimeError):
    """The API declined the request or filtered the completion."""

    def __init__(self, channel: str, raw_text: str, finish_reason: Optional[str]):
        super().__init__(f"refusal[{channel}] finish_reason={finish_reason!r}")
        self.channel = channel
        self.raw_text = raw_text
        self.finish_reason = finish_reason


class OaiCallCache:
    """One row per distinct judge request. The key includes reasoning_effort."""

    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS calls (
                    call_id TEXT PRIMARY KEY,
                    model TEXT NOT NULL,
                    reasoning_effort TEXT NOT NULL,
                    temperature REAL,
                    top_p REAL,
                    max_completion_tokens INTEGER NOT NULL,
                    messages_json TEXT NOT NULL,
                    status_type TEXT NOT NULL,
                    response_raw TEXT,
                    error_details TEXT,
                    prompt_tokens INTEGER,
                    completion_tokens INTEGER,
                    reasoning_tokens INTEGER,
                    elapsed_ms REAL,
                    created_at TEXT NOT NULL
                )
                """
            )

    def _connect(self) -> sqlite3.Connection:
        # WAL and a 30s busy wait match the trajectory cache, so several
        # grading processes can write this file at the same time.
        conn = sqlite3.connect(self.path, timeout=30)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA busy_timeout=30000")
        return conn

    @staticmethod
    def call_id(
        model: str,
        messages: List[Dict[str, str]],
        max_completion_tokens: int,
        reasoning_effort: Optional[str],
        temperature: Optional[float],
        top_p: Optional[float],
    ) -> str:
        payload = {
            "model": model,
            "messages": messages,
            "max_completion_tokens": max_completion_tokens,
            "reasoning_effort": reasoning_effort or "",
            "temperature": temperature,
            "top_p": top_p,
        }
        encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()

    def lookup(
        self,
        model: str,
        messages: List[Dict[str, str]],
        max_completion_tokens: int,
        reasoning_effort: Optional[str],
        temperature: Optional[float],
        top_p: Optional[float],
    ) -> Optional[Dict[str, Any]]:
        call_id = self.call_id(
            model, messages, max_completion_tokens, reasoning_effort, temperature, top_p
        )
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM calls WHERE call_id = ?", (call_id,)
            ).fetchone()
        if row is None:
            return None
        return dict(row)

    def log_call(
        self,
        model: str,
        messages: List[Dict[str, str]],
        max_completion_tokens: int,
        reasoning_effort: Optional[str],
        temperature: Optional[float],
        top_p: Optional[float],
        status_type: str,
        response_raw: Optional[str],
        error_details: Optional[str],
        prompt_tokens: Optional[int],
        completion_tokens: Optional[int],
        reasoning_tokens: Optional[int],
        elapsed_ms: Optional[float],
    ) -> str:
        call_id = self.call_id(
            model, messages, max_completion_tokens, reasoning_effort, temperature, top_p
        )
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO calls (
                    call_id, model, reasoning_effort, temperature, top_p,
                    max_completion_tokens, messages_json, status_type, response_raw,
                    error_details, prompt_tokens, completion_tokens, reasoning_tokens,
                    elapsed_ms, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    call_id,
                    model,
                    reasoning_effort or "",
                    temperature,
                    top_p,
                    max_completion_tokens,
                    json.dumps(messages, ensure_ascii=False),
                    status_type,
                    response_raw,
                    error_details,
                    prompt_tokens,
                    completion_tokens,
                    reasoning_tokens,
                    elapsed_ms,
                    time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                ),
            )
        return call_id


def _api_key() -> str:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    return key


def _post(url: str, headers: Dict[str, str], payload: Dict[str, Any], timeout: float) -> requests.Response:
    return requests.post(url, headers=headers, json=payload, timeout=timeout)


def _usage_ints(usage: Any) -> tuple:
    if not isinstance(usage, dict):
        return None, None, None
    details = usage.get("completion_tokens_details") or {}
    reasoning = details.get("reasoning_tokens") if isinstance(details, dict) else None
    return usage.get("prompt_tokens"), usage.get("completion_tokens"), reasoning


def _is_refusal_body(body: Any) -> bool:
    if not isinstance(body, dict):
        return False
    error = body.get("error") if isinstance(body.get("error"), dict) else body
    code = error.get("code") if isinstance(error, dict) else None
    if isinstance(code, str) and (
        code.startswith("content_policy") or code.startswith("moderation")
    ):
        return True
    return False


def _terminal_api_error(error_details: Optional[str]) -> bool:
    text = (error_details or "").lower()
    return any(marker in text for marker in TERMINAL_ERROR_MARKERS)


def complete(
    messages: List[Dict[str, str]],
    model: str,
    cache: OaiCallCache,
    max_completion_tokens: int,
    reasoning_effort: Optional[str] = None,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
    transport: Optional[Transport] = None,
    metadata: Optional[Dict[str, Any]] = None,
    use_cache: bool = True,
) -> str:
    """Return the assistant text. Raises RefusalError or the last API error.

    Temperature and top_p are omitted from the request when None, so the API
    uses its own default. Reasoning models often reject an explicit temperature.

    use_cache=False skips the stored reply and calls the API; the new reply
    replaces the stored one (same call_id). A caller uses it when the stored
    reply arrived intact but cannot be read, so asking again is the only way to
    get a different answer.
    """
    cached = None
    if use_cache:
        cached = cache.lookup(
            model, messages, max_completion_tokens, reasoning_effort, temperature, top_p
        )
    if cached and cached["status_type"] in ("ok", "refusal"):
        if metadata is not None:
            metadata["cached"] = True
            metadata["prompt_tokens"] = cached["prompt_tokens"]
            metadata["completion_tokens"] = cached["completion_tokens"]
            metadata["reasoning_tokens"] = cached["reasoning_tokens"]
            metadata["raw_text"] = cached["response_raw"] or ""
            metadata["call_id"] = cached["call_id"]
        if cached["status_type"] == "refusal":
            raise RefusalError("cached", cached["response_raw"] or "", None)
        return cached["response_raw"] or ""
    if cached and cached["status_type"] == "api_error" and _terminal_api_error(cached["error_details"]):
        raise RuntimeError(cached["error_details"] or "cached terminal api_error")

    payload: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "max_completion_tokens": max_completion_tokens,
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if top_p is not None:
        payload["top_p"] = top_p
    if reasoning_effort:
        payload["reasoning_effort"] = reasoning_effort

    headers = {
        "Authorization": f"Bearer {_api_key()}",
        "Content-Type": "application/json",
    }
    send = transport or _post
    last_error: Optional[BaseException] = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            started = time.time()
            response = send(API_URL, headers, payload, timeout)
            elapsed_ms = round((time.time() - started) * 1000, 1)
            try:
                body = response.json()
            except ValueError:
                body = {"error": {"message": response.text[:500], "code": "bad_json"}}
            if response.status_code == 400 and _is_refusal_body(body):
                raw = json.dumps(body, ensure_ascii=False)
                cache.log_call(
                    model, messages, max_completion_tokens, reasoning_effort,
                    temperature, top_p, "refusal", raw, raw[:500],
                    None, None, None, elapsed_ms,
                )
                raise RefusalError("http", raw, None)
            if response.status_code in (429, 500, 502, 503, 504):
                raise requests.HTTPError(
                    f"HTTP {response.status_code}: {json.dumps(body)[:300]}",
                    response=response,
                )
            if response.status_code >= 400:
                message = json.dumps(body, ensure_ascii=False)[:500]
                cache.log_call(
                    model, messages, max_completion_tokens, reasoning_effort,
                    temperature, top_p, "api_error", None,
                    f"HTTP {response.status_code}: {message}",
                    None, None, None, elapsed_ms,
                )
                raise RuntimeError(f"HTTP {response.status_code}: {message}")

            choices = body.get("choices") if isinstance(body, dict) else None
            if not choices:
                raise RuntimeError("Empty choices in completion response")
            choice = choices[0]
            message = choice.get("message") or {}
            finish_reason = choice.get("finish_reason")
            prompt_tok, completion_tok, reasoning_tok = _usage_ints(body.get("usage"))
            served = body.get("model")
            if served and served != model and not str(served).startswith(model):
                raise RuntimeError(
                    f"OpenAI substituted model: requested={model!r} served={served!r}"
                )
            structured = message.get("refusal")
            if structured:
                cache.log_call(
                    model, messages, max_completion_tokens, reasoning_effort,
                    temperature, top_p, "refusal", structured, str(structured)[:200],
                    prompt_tok, completion_tok, reasoning_tok, elapsed_ms,
                )
                raise RefusalError("structured", structured, finish_reason)
            if finish_reason == "content_filter":
                content = message.get("content") or ""
                cache.log_call(
                    model, messages, max_completion_tokens, reasoning_effort,
                    temperature, top_p, "refusal", content, "content_filter",
                    prompt_tok, completion_tok, reasoning_tok, elapsed_ms,
                )
                raise RefusalError("content_filter", content, finish_reason)
            content = (message.get("content") or "").strip()
            call_id = cache.log_call(
                model, messages, max_completion_tokens, reasoning_effort,
                temperature, top_p, "ok", content, None,
                prompt_tok, completion_tok, reasoning_tok, elapsed_ms,
            )
            if metadata is not None:
                metadata["cached"] = False
                metadata["prompt_tokens"] = prompt_tok
                metadata["completion_tokens"] = completion_tok
                metadata["reasoning_tokens"] = reasoning_tok
                metadata["raw_text"] = content
                metadata["finish_reason"] = finish_reason
                metadata["served_model"] = served
                metadata["call_id"] = call_id
                metadata["elapsed_ms"] = elapsed_ms
            return content
        except RefusalError:
            raise
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as exc:
            last_error = exc
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_BACKOFF_BASE_SEC * (2 ** attempt) + random.uniform(0, 1))
                continue
            break
        except Exception as exc:
            last_error = exc
            break

    detail = f"[{type(last_error).__name__}] {last_error}"
    cache.log_call(
        model, messages, max_completion_tokens, reasoning_effort,
        temperature, top_p, "api_error", None, detail,
        None, None, None, None,
    )
    if last_error is not None:
        raise last_error
    raise RuntimeError("OpenAI completion failed without an exception")
