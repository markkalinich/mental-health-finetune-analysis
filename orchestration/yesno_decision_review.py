#!/usr/bin/env python3
"""Second score for yes/no replies the format parser rejected.

The format score is unchanged. This step lists the replies that score
rejects and checks that a finished review has one label for each of them.
The review label is not written back into the cache or into metrics.json.

The reviewer is Claude Sonnet. The codebook is docs/yesno-decision-review.md.
"""

from __future__ import annotations

import argparse
import csv
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable, List, Mapping, Optional, Sequence

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from safety_labels.cohort import BY_ID, USABLE_IDS
from safety_labels.parse import parse_reply
from safety_labels.score import predicted_yes
from utilities.schemas import parse_one_word

LABELS = ("answered_yes", "answered_no", "not_an_answer")
_USABLE = frozenset(USABLE_IDS)


def format_parsed(model_id: str, text: str) -> bool:
    """True when the format score already has a yes or a no.

    The one-word ladder is the score. For a safety model in USABLE_IDS, a
    card label that maps to yes or no is also a format success. The Chat
    Doctor paragraph rule is not applied here.
    """
    parsed = parse_one_word(text or "", "suicidal_ideation", "x_yesno")
    if parsed and parsed.get("safety_type") in ("yes", "no"):
        return True
    if model_id not in _USABLE:
        return False
    kind = BY_ID[model_id].kind
    card = parse_reply(kind, text or "")
    return predicted_yes(kind, "synthetic_si", card["status"], card["label"]) is not None


def failure_id(task: str, model_id: str, key: str) -> str:
    return f"{task}|{model_id}|{key}"


def check_labels(
    failures: Sequence[Mapping[str, str]],
    labels: Sequence[Mapping[str, str]],
) -> List[str]:
    """Return every problem. An empty list means the review covers the failures."""
    problems: List[str] = []
    allowed = set(LABELS)
    want = [row["id"] for row in failures]
    if len(want) != len(set(want)):
        problems.append("failure list has duplicate ids")
    got: List[str] = []
    for i, row in enumerate(labels, 1):
        rid = row.get("id", "")
        label = row.get("label", "")
        if not rid:
            problems.append(f"label row {i} has no id")
            continue
        if label not in allowed:
            problems.append(f"{rid}: label {label!r} is not one of {LABELS}")
        got.append(rid)
    if len(got) != len(set(got)):
        problems.append("label file has duplicate ids")
    missing = [rid for rid in want if rid not in set(got)]
    extra = [rid for rid in got if rid not in set(want)]
    if missing:
        problems.append(f"missing {len(missing)} labels")
        problems.extend(missing)
    if extra:
        problems.append(f"extra {len(extra)} labels")
        problems.extend(extra)
    return problems


def summarize(failures: Sequence[Mapping[str, str]], labels: Mapping[str, str]) -> str:
    lines = []
    groups = {"both": list(failures)}
    for task in ("si", "cssrs"):
        groups[task] = [row for row in failures if row.get("task") == task]
    for name, rows in groups.items():
        counts = Counter(labels[row["id"]] for row in rows)
        lines.append(
            f"{name} n={len(rows)} "
            + " ".join(f"{label}={counts[label]}" for label in LABELS)
        )
    return "\n".join(lines)


def _read_jsonl(path: Path) -> List[dict]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _cohort_ids(path: Path) -> List[str]:
    ids = []
    with path.open(encoding="utf-8") as handle:
        next(handle)
        for line in handle:
            hf_id = line.split("\t", 1)[0].strip()
            if hf_id:
                ids.append(hf_id)
    return ids


def _message_text(raw: str) -> str:
    """Chat message, or the completion text when that message is empty.

    A non-empty message.content is the reply, which is how the instruction-tuned
    runs are stored. A one-string completion has no message, so choices[0].text
    is the reply. An empty message does not hide that text.
    """
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError:
        return ""
    choices = obj.get("choices") or [{}]
    choice = choices[0] or {}
    message = choice.get("message") or {}
    content = message.get("content") or ""
    if content:
        return content
    completion = choice.get("text")
    return completion if isinstance(completion, str) else ""


def extract_failures(
    cohort: Sequence[str],
    *,
    db_path: Path,
    si_prompt_name: str,
    cssrs_dir: Optional[Path],
    tasks: Sequence[str] = ("si", "cssrs"),
) -> List[dict]:
    """Replies the format score rejected, in cohort order."""
    rows: List[dict] = []
    if "si" in tasks:
        rows.extend(_si_failures(cohort, db_path=db_path, si_prompt_name=si_prompt_name))
    if "cssrs" in tasks:
        if cssrs_dir is None:
            raise ValueError("cssrs_dir is required when extracting C-SSRS failures")
        rows.extend(_cssrs_failures(cohort, cssrs_dir))
    return rows


def _si_failures(cohort: Sequence[str], *, db_path: Path, si_prompt_name: str) -> List[dict]:
    rows: List[dict] = []
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        for model_id in cohort:
            found = conn.execute(
                """
                SELECT ck.input_hash, cr.raw_response
                FROM cache_keys ck
                JOIN cached_results cr ON ck.cache_id = cr.cache_id
                WHERE ck.prompt_name = ?
                  AND cr.replicate_index = 0
                  AND ck.model_full_name = ?
                """,
                (si_prompt_name, model_id),
            ).fetchall()
            for input_hash, raw in found:
                text = _message_text(raw)
                if format_parsed(model_id, text):
                    continue
                rows.append({
                    "id": failure_id("si", model_id, input_hash),
                    "task": "si",
                    "model": model_id,
                    "key": input_hash,
                    "reply": text,
                })
    finally:
        conn.close()
    return rows


def _cssrs_failures(cohort: Sequence[str], cssrs_dir: Path) -> List[dict]:
    rows: List[dict] = []
    for model_id in cohort:
        path = cssrs_dir / model_id.replace("/", "__") / "predictions.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            for index, record in enumerate(csv.DictReader(handle)):
                text = record.get("raw_response") or ""
                if format_parsed(model_id, text):
                    continue
                rows.append({
                    "id": failure_id("cssrs", model_id, str(index)),
                    "task": "cssrs",
                    "model": model_id,
                    "key": str(index),
                    "reply": text,
                })
    return rows


def _cmd_check(args: argparse.Namespace) -> int:
    failures = _read_jsonl(Path(args.failures))
    labels = _read_jsonl(Path(args.labels))
    problems = check_labels(failures, labels)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    by_id = {row["id"]: row["label"] for row in labels}
    print(summarize(failures, by_id))
    print(f"labels {args.labels}")
    print(f"failures {args.failures}")
    return 0


def _cmd_extract(args: argparse.Namespace) -> int:
    tasks = tuple(args.task) if args.task else ("si", "cssrs")
    if "si" in tasks and not args.si_prompt_name:
        print("extract --task si needs --si-prompt-name", file=sys.stderr)
        return 1
    cohort = _cohort_ids(Path(args.cohort))
    rows = extract_failures(
        cohort,
        db_path=Path(args.db),
        si_prompt_name=args.si_prompt_name,
        cssrs_dir=Path(args.cssrs_dir) if args.cssrs_dir else None,
        tasks=tasks,
    )
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    counts = Counter(row["task"] for row in rows)
    print(f"wrote {len(rows)} failures si={counts['si']} cssrs={counts['cssrs']} {out}")
    return 0


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    check = sub.add_parser("check", help="fail unless every format failure has one review label")
    check.add_argument("--failures", required=True)
    check.add_argument("--labels", required=True)
    check.set_defaults(func=_cmd_check)

    extract = sub.add_parser("extract", help="write the replies the format score rejected")
    extract.add_argument("--cohort", required=True)
    extract.add_argument("--db", default="cache/results.db")
    extract.add_argument("--si-prompt-name", default="")
    extract.add_argument("--cssrs-dir", default="")
    extract.add_argument("--task", action="append", choices=("si", "cssrs"), dest="task")
    extract.add_argument("--out", required=True)
    extract.set_defaults(func=_cmd_extract)

    args = parser.parse_args(list(argv) if argv is not None else None)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
