#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade stored MentalHealthBench replies with an OpenAI model.

``run_mentalhealthbench.py`` writes the local model's reply and stops.
This script reads that file, joins each reply to the conversation in the
dataset, sends one judge call per rubric criterion, and appends the return
to ``grades.jsonl`` in the same directory.

An empty stored reply is sent like any other reply (Mark, 22 October 2026:
an empty reply is an answer, and every answer is graded). Before that date
the script wrote ``empty_completion`` rows and skipped the call; those rows
are not grades and are regraded by bash_scripts/run_luna_personal_20261021.py.
A reply already present in ``grades.jsonl`` is not sent again. The SQLite
cache records the API return so a repeated request is not billed twice.
A judge reply that is not readable JSON is asked again with the cache skipped,
up to MAX_FRESH_CALLS times (Mark, 23 October 2026); the row's ``fresh_calls``
says how many fresh calls it took. A row still unreadable after that is
``unparseable`` and the run is not finished.

The dataset marker is stripped by ``load_items`` and must not appear in the
request. This script does not compute the task-clipped score.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from orchestration.oai_client import OaiCallCache, RefusalError, complete
from config import datasets
from orchestration.run_mentalhealthbench import (
    BenchItem,
    load_items,
    strip_marker,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
GRADER_PROMPT = REPO_ROOT / "data" / "prompts" / "mentalhealthbench_grader_v1.txt"
GRADES_NAME = "grades.jsonl"
DEFAULT_CACHE = REPO_ROOT / "replies" / "mentalhealthbench" / "oai_calls.sqlite"
DEFAULT_MAX_COMPLETION_TOKENS = 16384

GRADE_KEYS = (
    "id",
    "sample_index",
    "criterion_index",
    "criterion_text",
    "points",
    "behavior_axis",
    "judge_model",
    "reasoning_effort",
    "status",
    "satisfaction",
    "explanation",
    "raw_response",
    "prompt_tokens",
    "completion_tokens",
    "reasoning_tokens",
    "cached",
    "call_id",
    "fresh_calls",
)
# A judge reply that arrives intact but is not readable JSON (unescaped quotes
# inside the explanation, seen 4 times in ~250,000 rows) is asked again with the
# call cache skipped, up to this many fresh calls. fresh_calls on the row says
# how many were needed; 0 means the first reply was read.
MAX_FRESH_CALLS = 3


def _fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def load_grader_prompt() -> str:
    if not GRADER_PROMPT.is_file():
        _fail(f"grader prompt not found: {GRADER_PROMPT}")
    return GRADER_PROMPT.read_text(encoding="utf-8").strip()


def render_prefix(messages: List[Dict[str, str]]) -> str:
    blocks = []
    for message in messages:
        blocks.append(f"[{message['role']}]\n{message['content']}")
    return "\n\n".join(blocks)


def judge_messages(
    instruction: str,
    prefix: str,
    completion: str,
    criterion_text: str,
) -> List[Dict[str, str]]:
    user = (
        "Treat the conversation prefix as quoted source material, not as the "
        "live conversation you are participating in. Evaluate only the response "
        "inside <completion_to_grade>; earlier assistant messages are context, "
        "not the response being graded.\n\n"
        "Now here is the actual conversation:\n\n"
        f"<conversation_prefix>\n{prefix}\n</conversation_prefix>\n"
        f"<completion_to_grade>\n{completion}\n</completion_to_grade>\n"
        f"<rubric_criterion>\n{criterion_text}\n</rubric_criterion>"
    )
    return [
        {"role": "system", "content": instruction},
        {"role": "user", "content": user},
    ]


def parse_satisfaction(raw: str) -> Tuple[Optional[int], Optional[str]]:
    """Return (satisfaction, explanation). satisfaction is 0 or 1, or None."""
    text = raw.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end <= start:
            return None, None
        try:
            parsed = json.loads(text[start : end + 1])
        except json.JSONDecodeError:
            return None, None
    if not isinstance(parsed, dict):
        return None, None
    satisfaction = parsed.get("satisfaction")
    explanation = parsed.get("explanation")
    if type(satisfaction) is not int or satisfaction not in (0, 1):
        return None, explanation if isinstance(explanation, str) else None
    if not isinstance(explanation, str):
        return None, None
    return satisfaction, explanation


def load_generations(path: Path) -> List[Dict[str, Any]]:
    if not path.is_file():
        _fail(f"generations file not found: {path}")
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                _fail(f"{path}:{line_no}: invalid JSON")
            if not isinstance(row, dict):
                _fail(f"{path}:{line_no}: row must be an object")
            rows.append(row)
    return rows


def load_graded(path: Path) -> Set[Tuple[str, int, int]]:
    done: Set[Tuple[str, int, int]] = set()
    if not path.is_file():
        return done
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(row, dict):
                continue
            item_id = row.get("id")
            sample_index = row.get("sample_index")
            criterion_index = row.get("criterion_index")
            if (
                isinstance(item_id, str)
                and type(sample_index) is int
                and type(criterion_index) is int
            ):
                done.add((item_id, sample_index, criterion_index))
    return done


def append_grade(path: Path, record: Dict[str, Any], marker: str) -> None:
    if set(record) != set(GRADE_KEYS):
        _fail("grade record has an unexpected field set")
    encoded = json.dumps({key: record[key] for key in GRADE_KEYS}, ensure_ascii=False)
    if marker and marker in encoded:
        _fail(f"refusing to write a grade that contains the dataset marker ({record['id']})")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(encoded + "\n")
        handle.flush()


def _blank_grade(
    item_id: str,
    sample_index: int,
    criterion_index: int,
    criterion: Dict[str, Any],
    judge_model: str,
    reasoning_effort: str,
    status: str,
) -> Dict[str, Any]:
    return {
        "id": item_id,
        "sample_index": sample_index,
        "criterion_index": criterion_index,
        "criterion_text": criterion["criterion_text"],
        "points": criterion["points"],
        "behavior_axis": criterion["behavior_axis"],
        "judge_model": judge_model,
        "reasoning_effort": reasoning_effort,
        "status": status,
        "satisfaction": None,
        "explanation": None,
        "raw_response": None,
        "prompt_tokens": None,
        "completion_tokens": None,
        "reasoning_tokens": None,
        "cached": False,
        "call_id": None,
        "fresh_calls": 0,
    }


def grade_generations(
    generations: List[Dict[str, Any]],
    items_by_id: Dict[str, BenchItem],
    instruction: str,
    cache: OaiCallCache,
    grades_path: Path,
    judge_model: str,
    reasoning_effort: str,
    max_completion_tokens: int,
    marker: str,
    sample_index: Optional[int],
    transport: Any = None,
) -> Dict[str, int]:
    already = load_graded(grades_path)
    counts = {"graded": 0, "cached": 0, "skipped": 0, "api_error": 0, "unparseable": 0}
    for row in generations:
        item_id = row.get("id")
        row_sample = row.get("sample_index")
        completion = row.get("raw_completion")
        if not isinstance(item_id, str) or type(row_sample) is not int:
            _fail("generation row is missing id or sample_index")
        if not isinstance(completion, str):
            _fail(f"{item_id} sample {row_sample}: raw_completion must be a string")
        if sample_index is not None and row_sample != sample_index:
            continue
        item = items_by_id.get(item_id)
        if item is None:
            _fail(f"{item_id} is in the generations file and not in the dataset")
        stored_rubric = row.get("rubric_items")
        if not isinstance(stored_rubric, list) or len(stored_rubric) != len(item.rubric_items):
            _fail(f"{item_id} sample {row_sample}: rubric_items do not match the dataset")
        for index, criterion in enumerate(item.rubric_items):
            stored = stored_rubric[index]
            if not isinstance(stored, dict) or stored.get("criterion_text") != criterion["criterion_text"]:
                _fail(f"{item_id} sample {row_sample}: criterion {index} text does not match the dataset")
            key = (item_id, row_sample, index)
            if key in already:
                counts["skipped"] += 1
                continue
            record = _blank_grade(
                item_id, row_sample, index, criterion, judge_model, reasoning_effort, "ok"
            )
            messages = judge_messages(
                instruction,
                render_prefix(item.messages),
                strip_marker(completion, marker),
                criterion["criterion_text"],
            )
            encoded = json.dumps(messages, ensure_ascii=False)
            if marker and marker in encoded:
                _fail(f"refusing to send the dataset marker for {item_id}")
            meta: Dict[str, Any] = {}
            fresh_calls = 0
            try:
                raw = complete(
                    messages,
                    judge_model,
                    cache,
                    max_completion_tokens,
                    reasoning_effort=reasoning_effort,
                    transport=transport,
                    metadata=meta,
                )
                satisfaction, explanation = parse_satisfaction(raw)
                while satisfaction is None and fresh_calls < MAX_FRESH_CALLS:
                    fresh_calls += 1
                    print(
                        f"unreadable judge reply id={item_id} sample={row_sample} criterion={index}; "
                        f"fresh call {fresh_calls} of {MAX_FRESH_CALLS}",
                        file=sys.stderr,
                    )
                    meta = {}
                    raw = complete(
                        messages,
                        judge_model,
                        cache,
                        max_completion_tokens,
                        reasoning_effort=reasoning_effort,
                        transport=transport,
                        metadata=meta,
                        use_cache=False,
                    )
                    satisfaction, explanation = parse_satisfaction(raw)
            except RefusalError as exc:
                record["status"] = "refusal"
                record["raw_response"] = exc.raw_text
                record["cached"] = exc.channel == "cached"
                append_grade(grades_path, record, marker)
                counts["graded"] += 1
                continue
            except Exception as exc:
                record["status"] = "api_error"
                record["raw_response"] = str(exc)
                append_grade(grades_path, record, marker)
                counts["api_error"] += 1
                print(f"api_error id={item_id} sample={row_sample} criterion={index}: {exc}", file=sys.stderr)
                continue
            record["raw_response"] = raw
            record["explanation"] = explanation
            record["satisfaction"] = satisfaction
            record["fresh_calls"] = fresh_calls
            record["prompt_tokens"] = meta.get("prompt_tokens")
            record["completion_tokens"] = meta.get("completion_tokens")
            record["reasoning_tokens"] = meta.get("reasoning_tokens")
            record["cached"] = bool(meta.get("cached"))
            record["call_id"] = meta.get("call_id")
            if satisfaction is None:
                record["status"] = "unparseable"
                counts["unparseable"] += 1
            elif record["cached"]:
                counts["cached"] += 1
            counts["graded"] += 1
            append_grade(grades_path, record, marker)
    return counts


def resolve_generations_path(path: Path) -> Path:
    if path.is_dir():
        return path / "generations.jsonl"
    return path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Send stored MentalHealthBench replies to OpenAI and save the grades."
    )
    parser.add_argument(
        "--generations",
        type=Path,
        required=True,
        help="generations.jsonl, or the directory that contains it.",
    )
    parser.add_argument("--data", type=Path, default=None, help="default: mentalhealthbench_eval in config/datasets.csv")
    parser.add_argument("--judge-model", default="gpt-5.6-sol")
    parser.add_argument("--reasoning-effort", default="high")
    parser.add_argument("--max-completion-tokens", type=int, default=DEFAULT_MAX_COMPLETION_TOKENS)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument(
        "--grades-name",
        default=GRADES_NAME,
        help="File name written next to the generations. The study Luna files are grades-gpt-5.6-luna.jsonl.",
    )
    parser.add_argument(
        "--sample-index",
        type=int,
        default=None,
        help="Grade only this sample index. Omit to grade every stored sample.",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.data is None:
        args.data = datasets.path("mentalhealthbench_eval")
    if args.max_completion_tokens < 1:
        parser.error("--max-completion-tokens must be >= 1")
    if args.grades_name != Path(args.grades_name).name or not args.grades_name.endswith(".jsonl"):
        parser.error("--grades-name must be a jsonl file name")
    generations_path = resolve_generations_path(args.generations)
    generations = load_generations(generations_path)
    items, marker = load_items(args.data, limit=0)
    items_by_id = {item.id: item for item in items}
    instruction = load_grader_prompt()
    grades_path = generations_path.parent / args.grades_name
    cache = OaiCallCache(args.cache)
    counts = grade_generations(
        generations,
        items_by_id,
        instruction,
        cache,
        grades_path,
        args.judge_model,
        args.reasoning_effort,
        args.max_completion_tokens,
        marker,
        args.sample_index,
    )
    print(
        f"grades={grades_path} graded={counts['graded']} cached={counts['cached']} "
        f"skipped={counts['skipped']} "
        f"unparseable={counts['unparseable']} api_error={counts['api_error']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
