#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MentalHealthBench generation only. No judge and no score.

Posts each item's conversation.messages unchanged to an OpenAI-compatible
/v1/chat/completions endpoint, four times by default. A leading system
message stays in the list. has_prior_context does not drop it.

Temperature defaults to 0 and top_p defaults to 1, matching the other
local tasks. Qwen 3 and Qwen 3.5 send chat_template_kwargs
enable_thinking false. No prompt suffix is applied. max_tokens defaults
to 2048. --samples defaults to 4, which is the paper's count; this
study's run passes --samples 1.

The dataset marker field is read only so it can be removed from text that
would be sent or written. It is not stored.

summary.json keys:
  n_items       items used for this invocation (after --limit)
  n_samples     completions requested per item (--samples)
  n_api_errors  completion calls that failed in this invocation
  api_errors    one entry per failed call: id, sample_index, message (the server's error text)
  elapsed       wall-clock seconds for this invocation

Replies are stored in cache/results.db. A rerun returns those rows and
does not call the model. An api_error row is not a hit. The generations
file is a copy of rows from this invocation; it is not what decides a hit.

An empty model reply is stored as an empty string. Failed calls are not
written to the generations file, so a rerun retries those pairs.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

_REPO = Path(__file__).resolve().parents[1]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))
from config import datasets  # noqa: E402

GENERATIONS_NAME = "generations.jsonl"
SUMMARY_NAME = "summary.json"
RECORD_KEYS = (
    "id",
    "sample_index",
    "raw_completion",
    "acuity",
    "user_profile",
    "language",
    "has_prior_context",
    "rubric_items",
)


@dataclass
class BenchItem:
    id: str
    messages: List[Dict[str, str]]
    acuity: str
    user_profile: str
    language: str
    has_prior_context: bool
    rubric_items: List[Dict[str, Any]]


def strip_marker(text: str, marker: str) -> str:
    if not text or not marker or marker not in text:
        return text
    return text.replace(marker, "")


def _fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def prepare_messages(raw_messages: Any, marker: str, item_id: str) -> List[Dict[str, str]]:
    if not isinstance(raw_messages, list) or not raw_messages:
        _fail(f"item {item_id}: conversation.messages must be a non-empty list")
    prepared: List[Dict[str, str]] = []
    for index, message in enumerate(raw_messages):
        if not isinstance(message, dict):
            _fail(f"item {item_id}: message {index} must be an object")
        role = message.get("role")
        content = message.get("content")
        if role not in ("system", "user", "assistant"):
            _fail(f"item {item_id}: message {index} has an unsupported role")
        if not isinstance(content, str):
            _fail(f"item {item_id}: message {index} content must be a string")
        prepared.append({"role": role, "content": strip_marker(content, marker)})
    if prepared[-1]["role"] != "user":
        _fail(f"item {item_id}: conversation does not end on a user turn")
    return prepared


def copy_rubric(raw: Any, marker: str, item_id: str) -> List[Dict[str, Any]]:
    if not isinstance(raw, list) or not raw:
        _fail(f"item {item_id}: rubric_items must be a non-empty list")
    copied: List[Dict[str, Any]] = []
    for index, item in enumerate(raw):
        if not isinstance(item, dict):
            _fail(f"item {item_id}: rubric item {index} must be an object")
        for key in ("criterion_text", "points", "behavior_axis"):
            if key not in item:
                _fail(f"item {item_id}: rubric item {index} missing {key}")
        points = item["points"]
        text = item["criterion_text"]
        axis = item["behavior_axis"]
        if isinstance(points, bool) or not isinstance(points, int):
            _fail(f"item {item_id}: rubric item {index} points must be an int")
        if not isinstance(text, str) or not isinstance(axis, str):
            _fail(f"item {item_id}: rubric item {index} text fields must be strings")
        copied.append(
            {
                "criterion_text": strip_marker(text, marker),
                "points": points,
                "behavior_axis": axis,
            }
        )
    return copied


def load_items(path: Path, limit: int) -> Tuple[List[BenchItem], str]:
    if not path.is_file():
        _fail(f"data file not found: {path}")
    items: List[BenchItem] = []
    seen: Set[str] = set()
    marker: Optional[str] = None
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                _fail(f"line {line_no}: invalid JSON")
            if not isinstance(row, dict):
                _fail(f"line {line_no}: item must be an object")
            item_id = row.get("id")
            if not isinstance(item_id, str) or not item_id:
                _fail(f"line {line_no}: missing id")
            if item_id in seen:
                _fail(f"duplicate id {item_id}")
            seen.add(item_id)
            row_marker = row.get("canary_string")
            if not isinstance(row_marker, str) or not row_marker:
                _fail(f"item {item_id}: missing canary_string")
            if marker is None:
                marker = row_marker
            elif row_marker != marker:
                _fail("canary_string is not uniform across items")
            conversation = row.get("conversation")
            if not isinstance(conversation, dict) or "messages" not in conversation:
                _fail(f"item {item_id}: conversation.messages is missing")
            acuity = row.get("acuity")
            user_profile = row.get("user_profile")
            language = row.get("language")
            has_prior_context = row.get("has_prior_context")
            if not isinstance(acuity, str) or not acuity:
                _fail(f"item {item_id}: acuity must be a string")
            if not isinstance(user_profile, str) or not user_profile:
                _fail(f"item {item_id}: user_profile must be a string")
            if not isinstance(language, str) or not language:
                _fail(f"item {item_id}: language must be a string")
            if not isinstance(has_prior_context, bool):
                _fail(f"item {item_id}: has_prior_context must be a bool")
            items.append(
                BenchItem(
                    id=item_id,
                    messages=prepare_messages(conversation["messages"], marker, item_id),
                    acuity=acuity,
                    user_profile=user_profile,
                    language=language,
                    has_prior_context=has_prior_context,
                    rubric_items=copy_rubric(row.get("rubric_items"), marker, item_id),
                )
            )
    if not items or marker is None:
        _fail(f"no items in {path}")
    if limit < 0:
        _fail("--limit must be >= 0")
    if limit:
        items = items[:limit]
    return items, marker


def generations_path(output_dir: Path) -> Path:
    return output_dir / GENERATIONS_NAME


def load_completed(output_dir: Path) -> Set[Tuple[str, int]]:
    path = generations_path(output_dir)
    done: Set[Tuple[str, int]] = set()
    if not path.is_file():
        return done
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(row, dict):
                continue
            item_id = row.get("id")
            sample_index = row.get("sample_index")
            completion = row.get("raw_completion")
            if not isinstance(item_id, str) or not item_id:
                continue
            if isinstance(sample_index, bool) or not isinstance(sample_index, int):
                continue
            if not isinstance(completion, str):
                continue
            done.add((item_id, sample_index))
    return done


def append_generation(output_dir: Path, record: Dict[str, Any], marker: str) -> None:
    if set(record) != set(RECORD_KEYS):
        _fail("generation record has an unexpected field set")
    record = {key: record[key] for key in RECORD_KEYS}
    if "canary_string" in record:
        _fail("refusing to write canary_string")
    encoded = json.dumps(record, ensure_ascii=False)
    if marker and marker in encoded:
        _fail(
            f"refusing to write item {record.get('id')} sample {record.get('sample_index')}"
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    with generations_path(output_dir).open("a", encoding="utf-8") as handle:
        handle.write(encoded + "\n")
        handle.flush()


def record_for(item: BenchItem, sample_index: int, completion: str) -> Dict[str, Any]:
    return {
        "id": item.id,
        "sample_index": sample_index,
        "raw_completion": completion,
        "acuity": item.acuity,
        "user_profile": item.user_profile,
        "language": item.language,
        "has_prior_context": item.has_prior_context,
        "rubric_items": item.rubric_items,
    }


def write_summary(
    output_dir: Path,
    n_items: int,
    n_samples: int,
    api_errors: List[Dict[str, Any]],
    elapsed: float,
) -> None:
    payload = {
        "n_items": n_items,
        "n_samples": n_samples,
        "n_api_errors": len(api_errors),
        "api_errors": api_errors,
        "elapsed": elapsed,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / SUMMARY_NAME).write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )


async def warmup(client: Any, temperature: float, top_p: float) -> None:
    await client.call_chat_completion_messages_async(
        [{"role": "user", "content": "Reply with the word ready."}],
        max_tokens=16,
        temperature=temperature,
        top_p=top_p,
    )


async def generate_pending(
    client: Any,
    pending: List[Tuple[BenchItem, int, str]],
    output_dir: Path,
    marker: str,
    max_tokens: int,
    max_concurrent: int,
    temperature: float,
    top_p: float,
    cache: Any,
    config: Any,
    already_written: Set[Tuple[str, int]],
) -> List[Dict[str, Any]]:
    from orchestration.api_client import ChatAPIError

    sem = asyncio.Semaphore(max(1, max_concurrent))
    write_lock = asyncio.Lock()
    total = len(pending)
    done = 0
    api_errors: List[Dict[str, Any]] = []

    async def one(item: BenchItem, sample_index: int, input_text: str) -> None:
        nonlocal done
        error_name: Optional[str] = None
        error_text = ""
        completion = ""
        raw: Dict[str, Any] = {}
        started = time.perf_counter()
        async with sem:
            try:
                raw = await client.call_chat_completion_messages_async(
                    item.messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                )
                content = client.extract_content(raw)
                completion = content if isinstance(content, str) else ""
                completion = strip_marker(completion, marker)
            except ChatAPIError as exc:
                error_name = "ChatAPIError"
                error_text = strip_marker(str(exc), marker)
        elapsed = time.perf_counter() - started
        async with write_lock:
            if error_name is not None:
                api_errors.append({"id": item.id, "sample_index": sample_index, "message": error_text})
                cache.store_result(
                    config, input_text, "mentalhealthbench",
                    {"error": error_name}, None, "api_error:ChatAPIError",
                    elapsed, sample_index,
                )
                print(
                    strip_marker(
                        f"api_error id={item.id} sample={sample_index} {error_name}",
                        marker,
                    ),
                    flush=True,
                )
            else:
                cache.store_result(
                    config, input_text, "mentalhealthbench",
                    raw, {"content": completion}, "ok", elapsed, sample_index,
                )
                if (item.id, sample_index) not in already_written:
                    append_generation(
                        output_dir,
                        record_for(item, sample_index, completion),
                        marker,
                    )
                    already_written.add((item.id, sample_index))
            done += 1
            if done % 50 == 0 or done == total:
                print(
                    f"Progress: {done}/{total} ({100.0 * done / total:.1f}%)",
                    flush=True,
                )

    print(
        f"Processing {total} completions with up to {max_concurrent} concurrent connections..."
    )
    await asyncio.gather(*[one(item, sample_index, input_text) for item, sample_index, input_text in pending])
    return api_errors


def default_output_dir(model_name: str) -> Path:
    safe = model_name.replace("/", "__")
    return Path("replies/mentalhealthbench") / safe


def message_input(messages: List[Dict[str, str]]) -> str:
    return json.dumps(messages, ensure_ascii=False, separators=(",", ":"))


def cached_ok(cache: Any, config: Any, input_text: str, replicate_index: int) -> Optional[Dict[str, Any]]:
    """One non-error cache row for this sample, or None."""
    existing, _missing = cache.check_cache(
        config, input_text, "mentalhealthbench", num_replicates=1, include_errors=False
    )
    for row in existing:
        if row.replicate_index == replicate_index:
            return row.raw_response
    return None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate MentalHealthBench replies. Does not score."
    )
    parser.add_argument("--base-url", default="", help="OpenAI-compatible base, e.g. http://127.0.0.1:8000/v1")
    parser.add_argument("--model-name", default="", help="Served model id. '/' is stored as '__'.")
    parser.add_argument("--model-family", default="", help="Cache key family. Default: qwen if the id contains qwen, otherwise other.")
    parser.add_argument("--model-size", default="", help="Cache key size. Default: the model id with '/' replaced by '__'.")
    parser.add_argument("--model-version", default="20261007", help="Cache key version. Same value the ideation runs use.")
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--data", type=Path, default=None, help="default: mentalhealthbench_eval in config/datasets.csv")
    parser.add_argument("--limit", type=int, default=0, help="First N items in file order. 0 means all.")
    parser.add_argument("--max-tokens", type=int, default=2048)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=1.0)
    parser.add_argument(
        "--samples",
        type=int,
        default=4,
        help="Completions per item. summary.json n_samples is this value.",
    )
    parser.add_argument("--max-concurrent", type=int, default=128)
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="HTTP timeout in seconds for each completion.",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.data is None:
        args.data = datasets.path("mentalhealthbench_eval")
    if not args.base_url or not args.model_name:
        parser.error("--base-url and --model-name are required")
    if args.limit < 0:
        parser.error("--limit must be >= 0")
    if args.samples < 1:
        parser.error("--samples must be >= 1")
    if args.max_tokens < 1:
        parser.error("--max-tokens must be >= 1")
    if args.max_concurrent < 1:
        parser.error("--max-concurrent must be >= 1")
    if args.timeout < 1:
        parser.error("--timeout must be >= 1")

    from types import SimpleNamespace

    from cache.result_cache import ResultCache
    from config.utils import qwen_chat_template_kwargs
    from orchestration.api_client import ChatAPIError, ChatCompletionsClient
    from orchestration.experiment_manager import ExperimentManager

    started = time.perf_counter()
    items, marker = load_items(args.data, args.limit)
    output_dir = args.output_dir or default_output_dir(args.model_name)
    already_written = load_completed(output_dir)
    family = args.model_family or ("qwen" if "qwen" in args.model_name.lower() else "other")
    size = args.model_size or args.model_name.replace("/", "__")
    cache = ResultCache()
    config = ExperimentManager(Path(".")).create_experiment_config(
        experiment_name=f"mhb_{size}",
        model_family=family,
        model_size=size,
        model_version=args.model_version,
        prompt_name="mentalhealthbench",
        prompt_file=str(args.data),
        input_dataset=str(args.data),
        model_name=args.model_name,
        base_url=args.base_url,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        top_p=args.top_p,
        request_timeout=args.timeout,
    )
    client = ChatCompletionsClient(
        SimpleNamespace(
            base_url=args.base_url,
            model=args.model_name,
            request_timeout=args.timeout,
            chat_template_kwargs=qwen_chat_template_kwargs(model_id=args.model_name),
        )
    )
    pending: List[Tuple[BenchItem, int, str]] = []
    n_hits = 0
    for item in items:
        sent = client._messages(item.messages)
        input_text = message_input(sent)
        for sample_index in range(args.samples):
            raw = cached_ok(cache, config, input_text, sample_index)
            if raw is None:
                pending.append((item, sample_index, input_text))
                continue
            n_hits += 1
            if (item.id, sample_index) in already_written:
                continue
            content = client.extract_content(raw)
            completion = content if isinstance(content, str) else ""
            append_generation(
                output_dir,
                record_for(item, sample_index, strip_marker(completion, marker)),
                marker,
            )
            already_written.add((item.id, sample_index))
    print(
        f"items {len(items)} samples_per_item {args.samples} "
        f"cache_hits {n_hits} pending {len(pending)} dir {output_dir}"
    )

    api_errors: List[Dict[str, Any]] = []
    if pending:
        print(
            f"Warming up {args.model_name} at {args.base_url} "
            f"temperature={args.temperature} top_p={args.top_p}"
        )
        try:
            asyncio.run(warmup(client, args.temperature, args.top_p))
        except ChatAPIError:
            print("warmup failed: ChatAPIError", file=sys.stderr)
            return 1
        api_errors = asyncio.run(
            generate_pending(
                client,
                pending,
                output_dir,
                marker,
                args.max_tokens,
                args.max_concurrent,
                args.temperature,
                args.top_p,
                cache,
                config,
                already_written,
            )
        )

    elapsed = round(time.perf_counter() - started, 3)
    write_summary(output_dir, len(items), args.samples, api_errors, elapsed)
    print(f"generations {generations_path(output_dir)}")
    print(f"summary {output_dir / SUMMARY_NAME}")
    print(
        f"n_items={len(items)} n_samples={args.samples} "
        f"n_api_errors={len(api_errors)} elapsed={elapsed}"
    )
    return 1 if api_errors else 0


if __name__ == "__main__":
    sys.exit(main())
