"""One answer to "is this MentalHealthBench run processed?"

Decided by Mark on 22 October 2026 (docs/DECISIONS-PENDING.md):

  A model is processed when (a) it answered all 1,215 conversations and no
  call returned an API error, an empty reply being an answer, and (b) every
  answer was graded by Luna on every rubric criterion.

Every reader of a grade file calls ``grade_file_status`` and nothing else
decides. The plotting code, the roster fill, and the Luna launcher do not
carry their own rule.

Files, under replies/mentalhealthbench-1215-temp0/<hf_id with / as __>/:

  generations.jsonl        one record per conversation answered without an
                           API error; a failed call is not written
  grades-gpt-5.6-luna.jsonl one record per (conversation, criterion)

Status values:

  not_run        no generations.jsonl
  needs_gpu      generations.jsonl does not hold every one of the 1,215
                 conversation ids exactly once
  needs_grading  the grade file is missing, or is short of one row per
                 criterion, or holds a row whose status is not ``ok`` or
                 whose satisfaction is not 0 or 1
  processed      every criterion of every conversation has an ``ok`` row

A duplicate (id, criterion_index), a JSON line that does not parse, or an
id that is not in the dataset stops the run. Those are not states a file
can be in; they are something a person has to look at.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

MHB_ROOT = REPO / "replies/mentalhealthbench-1215-temp0"
GRADES_NAME = "grades-gpt-5.6-luna.jsonl"
GENERATIONS_NAME = "generations.jsonl"
N_CONVERSATIONS = 1215
N_CRITERIA = 5262

STATUSES = ("not_run", "needs_gpu", "needs_grading", "processed")


@dataclass
class RunStatus:
    hf_id: str
    directory: Path
    status: str
    n_answered: int = 0
    n_nonempty: int = 0
    grade_rows: int = 0
    ok_rows: int = 0
    row_status: Counter = field(default_factory=Counter)
    missing_criteria: int = 0
    note: str = ""

    @property
    def processed(self) -> bool:
        return self.status == "processed"


def safe_name(hf_id: str) -> str:
    return hf_id.replace("/", "__")


def run_directory(hf_id: str) -> Path:
    return MHB_ROOT / safe_name(hf_id)


def dataset_rubric() -> dict[str, int]:
    """Criterion count for each of the 1,215 conversations, from the dataset file."""
    from config import datasets

    data = datasets.path("mentalhealthbench_eval")
    rubric: dict[str, int] = {}
    with data.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            qid = row["id"]
            if qid in rubric:
                raise SystemExit(f"{data} line {line_no}: conversation {qid} appears twice")
            rubric[qid] = len(row["rubric_items"])
    if len(rubric) != N_CONVERSATIONS:
        raise SystemExit(f"{data} has {len(rubric)} conversations, not {N_CONVERSATIONS}")
    if sum(rubric.values()) != N_CRITERIA:
        raise SystemExit(f"{data} has {sum(rubric.values())} criteria, not {N_CRITERIA}")
    return rubric


def read_generations(path: Path) -> dict[str, str]:
    """Conversation id -> reply text. Records are JSON objects, not always one per line."""
    decoder = json.JSONDecoder()
    text = path.read_text(encoding="utf-8")
    replies: dict[str, str] = {}
    index = 0
    length = len(text)
    while index < length:
        while index < length and text[index].isspace():
            index += 1
        if index >= length:
            break
        try:
            row, index = decoder.raw_decode(text, index)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}: unreadable JSON at offset {index}: {exc}")
        if not isinstance(row, dict) or "id" not in row:
            raise SystemExit(f"{path}: a record has no id")
        qid = row["id"]
        if qid in replies:
            raise SystemExit(f"{path}: conversation {qid} appears twice")
        reply = row.get("raw_completion")
        if not isinstance(reply, str):
            raise SystemExit(f"{path}: conversation {qid} raw_completion is not a string")
        replies[qid] = reply
    return replies


def read_grades(path: Path) -> list[dict]:
    """Every grade row. A line that is not JSON stops the run."""
    rows: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path} line {line_no}: not JSON ({exc}). Fix or remove the line.")
            if not isinstance(row, dict):
                raise SystemExit(f"{path} line {line_no}: not a JSON object")
            rows.append(row)
    return rows


def grade_row_ok(row: dict) -> bool:
    return row.get("status") == "ok" and row.get("satisfaction") in (0, 1)


def grade_file_status(hf_id: str, rubric: dict[str, int] | None = None) -> RunStatus:
    """The one status for a model's MentalHealthBench run."""
    if rubric is None:
        rubric = dataset_rubric()
    directory = run_directory(hf_id)
    generations = directory / GENERATIONS_NAME
    if not generations.is_file():
        return RunStatus(hf_id, directory, "not_run")
    replies = read_generations(generations)
    unknown = sorted(set(replies) - set(rubric))
    if unknown:
        raise SystemExit(f"{generations}: {len(unknown)} ids are not in the dataset, first {unknown[0]}")
    result = RunStatus(
        hf_id,
        directory,
        "needs_gpu",
        n_answered=len(replies),
        n_nonempty=sum(1 for reply in replies.values() if reply.strip()),
    )
    if set(replies) != set(rubric):
        missing = sorted(set(rubric) - set(replies))
        result.note = f"{len(missing)} conversations unanswered, first {missing[0]}"
        return result
    grades = directory / GRADES_NAME
    result.status = "needs_grading"
    if not grades.is_file():
        result.missing_criteria = N_CRITERIA
        result.note = "no grade file"
        return result
    rows = read_grades(grades)
    seen: set[tuple[str, int]] = set()
    for row in rows:
        key = (row.get("id"), row.get("criterion_index"))
        if key[0] not in rubric:
            raise SystemExit(f"{grades}: grade for {key[0]}, which is not in the dataset")
        if not isinstance(key[1], int) or not 0 <= key[1] < rubric[key[0]]:
            raise SystemExit(f"{grades}: {key[0]} criterion_index {key[1]!r} is out of range")
        if key in seen:
            raise SystemExit(f"{grades}: {key[0]} criterion {key[1]} graded twice")
        seen.add(key)
        result.row_status[str(row.get("status"))] += 1
        if grade_row_ok(row):
            result.ok_rows += 1
    result.grade_rows = len(rows)
    result.missing_criteria = N_CRITERIA - len(seen)
    if result.ok_rows == N_CRITERIA:
        result.status = "processed"
    else:
        not_ok = {k: v for k, v in result.row_status.items() if k != "ok"}
        result.note = f"{result.missing_criteria} criteria ungraded; non-ok rows {dict(not_ok)}"
    return result


def main(argv: list[str] | None = None) -> int:
    """Print the status of every roster model, or of the ids given."""
    from orchestration.study_roster import load_roster

    ids = list(argv) if argv else [row["hf_id"] for row in load_roster()]
    rubric = dataset_rubric()
    counts: Counter = Counter()
    for hf_id in ids:
        status = grade_file_status(hf_id, rubric)
        counts[status.status] += 1
        print(f"{status.status:14} {hf_id:60} answered={status.n_answered:4} ok_rows={status.ok_rows:4} {status.note}")
    print(dict(counts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
