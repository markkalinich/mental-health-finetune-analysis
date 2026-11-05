"""Grade every roster model's MentalHealthBench replies with Luna.

The key is an argument, --key mark or --key torous. There is no default.
The key is read from /home/mkalinich/.openai_keys/openai_<name> and is not
printed. When the queue finishes, this script refreshes the roster.

Which models, and when a run is finished, come from one place:
orchestration/mhb_status.py (Mark, 22 October 2026). This script

  * reads the study roster and takes every row except safety fine-tunes,
    which are not drawn on the MentalHealthBench column (plot_parse_rates
    ``_not_run``);
  * stops if any of those rows has no generations file at all;
  * skips a row whose generations file is short only when that id is in
    KNOWN_NEEDS_GPU with a written reason, and stops otherwise;
  * removes every grade row that is not a finished grade (``api_error``,
    ``empty_completion``, ``unparseable``, ``refusal``) into
    replies/luna-personal-20261021/stripped-rows/<safe>.jsonl, then runs the
    grader, which regrades those criteria;
  * refreshes the roster when the queue is done.

One grader process per model, all started at once (Mark, 23 Oct 2026); each
process sends one judge call at a time.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from queue import Empty, Queue

ROOT = Path("/home/mkalinich/main")
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.mhb_status import (  # noqa: E402
    GRADES_NAME,
    dataset_rubric,
    grade_file_status,
    grade_row_ok,
    read_grades,
    run_directory,
    safe_name,
)

KEYS = {
    "mark": Path("/home/mkalinich/.openai_keys/openai_mark"),
    "torous": Path("/home/mkalinich/.openai_keys/openai_torous"),
}
RUN = ROOT / "replies" / "luna-personal-20261021"
STRIPPED = RUN / "stripped-rows"
PY = ROOT / ".venv" / "bin" / "python"
# A short generations file is a GPU gap, not a grading gap. Only these ids may
# be skipped, each with the decision that says so.
KNOWN_NEEDS_GPU = {
    "Qwen/Qwen2.5-Math-1.5B": "docs/DECISIONS-PENDING.md, decided 22 Oct 2026: one conversation exceeds the 4,096-token context; cell stays blank",
}


def _key_from(path: Path) -> str:
    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("export "):
            line = line[len("export ") :]
        if line.startswith("OPENAI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit(f"{path} has no OPENAI_API_KEY")


def load_key(name: str) -> None:
    path = KEYS.get(name)
    if path is None:
        raise SystemExit(f"key must be one of {', '.join(sorted(KEYS))}, not {name!r}")
    if not path.is_file():
        raise SystemExit(f"{path} does not exist")
    key = _key_from(path)
    if not key:
        raise SystemExit(f"{path} has an empty key")
    os.environ["OPENAI_API_KEY"] = key
    print(f"key_source={path.name}", flush=True)


def roster_models() -> list[dict]:
    """Every roster row that is drawn on the MentalHealthBench column."""
    from orchestration.study_roster import load_roster

    rows = load_roster()
    kept = [row for row in rows if not (row["role"] == "fine-tune" and row["grouping"] == "safety")]
    skipped = len(rows) - len(kept)
    if skipped != 10:
        raise SystemExit(f"expected 10 safety fine-tunes on the roster, found {skipped}")
    print(f"roster rows {len(rows)}; safety fine-tunes not graded {skipped}", flush=True)
    return kept


def plan() -> list[tuple[str, int]]:
    """(hf_id, criteria still to grade), shortest first."""
    rubric = dataset_rubric()
    todo: list[tuple[int, str]] = []
    not_run: list[str] = []
    for row in roster_models():
        hf_id = row["hf_id"]
        status = grade_file_status(hf_id, rubric)
        if status.status == "processed":
            continue
        if status.status == "not_run":
            not_run.append(hf_id)
            continue
        if status.status == "needs_gpu":
            reason = KNOWN_NEEDS_GPU.get(hf_id)
            if reason is None:
                raise SystemExit(f"{hf_id} has a short generations file and no decision: {status.note}")
            print(f"needs_gpu\t{hf_id}\t{status.note}\t{reason}", flush=True)
            continue
        gap = status.missing_criteria + (status.grade_rows - status.ok_rows)
        todo.append((gap, hf_id))
        print(f"plan\t{hf_id}\tremaining={gap}\t{dict(status.row_status)}", flush=True)
    if not_run:
        raise SystemExit("roster models with no MentalHealthBench generations file:\n  " + "\n  ".join(not_run))
    todo.sort()
    return [(hf_id, gap) for gap, hf_id in todo]


def strip_unfinished_rows(hf_id: str) -> int:
    """Remove every grade row that is not a finished grade so the grader redoes it."""
    path = run_directory(hf_id) / GRADES_NAME
    if not path.is_file():
        return 0
    rows = read_grades(path)
    kept = [row for row in rows if grade_row_ok(row)]
    removed = [row for row in rows if not grade_row_ok(row)]
    if not removed:
        return 0
    STRIPPED.mkdir(parents=True, exist_ok=True)
    with (STRIPPED / f"{safe_name(hf_id)}.jsonl").open("a", encoding="utf-8") as handle:
        for row in removed:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    tmp = path.with_suffix(".jsonl.tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        for row in kept:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    tmp.replace(path)
    print(f"stripped\t{hf_id}\tremoved={len(removed)}\tkept={len(kept)}", flush=True)
    return len(removed)


def grader_running(hf_id: str) -> bool:
    needle = f"mentalhealthbench-1215-temp0/{safe_name(hf_id)}"
    for proc in Path("/proc").iterdir():
        if not proc.name.isdigit():
            continue
        try:
            command = (proc / "cmdline").read_bytes().replace(b"\x00", b" ").decode(errors="replace")
        except OSError:
            continue
        # The directory name has to end the path. Qwen__Qwen3.5-4B is a prefix of
        # Qwen__Qwen3.5-4B-Base, and a prefix match skips the shorter one.
        if "grade_mentalhealthbench" in command and f"{needle} " in command:
            return True
    return False


def grade(hf_id: str) -> int:
    log = RUN / f"{safe_name(hf_id)}.log"
    cmd = [
        str(PY),
        "-u",
        "-m",
        "orchestration.grade_mentalhealthbench",
        "--generations",
        str(run_directory(hf_id)),
        "--judge-model",
        "gpt-5.6-luna",
        "--reasoning-effort",
        "high",
        "--grades-name",
        GRADES_NAME,
    ]
    print(f"start\t{hf_id}\t{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}", flush=True)
    with log.open("w", encoding="utf-8") as handle:
        proc = subprocess.run(cmd, cwd=ROOT, stdout=handle, stderr=subprocess.STDOUT)
    text = log.read_text(encoding="utf-8", errors="replace")
    if "credit_balance_exhausted" in text:
        print(f"stop\t{hf_id}\tcredit_balance_exhausted", flush=True)
        return 2
    tail = text.strip().splitlines()[-1] if text.strip() else ""
    status = grade_file_status(hf_id)
    print(f"done\t{hf_id}\texit={proc.returncode}\tstatus={status.status}\t{tail}", flush=True)
    return proc.returncode


def _grade_one(hf_id: str, stop: threading.Event) -> int:
    if grader_running(hf_id):
        print(f"already-running\t{hf_id}", flush=True)
        while grader_running(hf_id) and not stop.is_set():
            time.sleep(20)
        if grade_file_status(hf_id).processed:
            print(f"finished-elsewhere\t{hf_id}", flush=True)
            return 0
    if stop.is_set():
        print(f"not-started\t{hf_id}", flush=True)
        return 0
    strip_unfinished_rows(hf_id)
    return grade(hf_id)


def _refresh_roster() -> int:
    """Copy finished grades into the roster. A blanked score stops the pass."""
    from orchestration.fill_roster_scores import refresh_roster

    try:
        path = refresh_roster()
    except SystemExit as exc:
        print(exc, flush=True)
        return 1
    print(f"roster refreshed\t{path}", flush=True)
    return 0


def main(key_name: str) -> int:
    load_key(key_name)
    RUN.mkdir(parents=True, exist_ok=True)
    models = plan()
    if not models:
        print("nothing to grade", flush=True)
        return _refresh_roster()
    work: Queue = Queue()
    for item in models:
        work.put(item)
    stop = threading.Event()
    codes: list[int] = []
    lock = threading.Lock()

    def worker() -> None:
        while not stop.is_set():
            try:
                hf_id, _gap = work.get_nowait()
            except Empty:
                return
            code = _grade_one(hf_id, stop)
            with lock:
                codes.append(code)
            if code == 2:
                stop.set()
                return

    # One worker per model: every grader process starts now.
    threads = [threading.Thread(target=worker, name=f"luna-{i}") for i in range(len(models))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    refresh_code = _refresh_roster()
    if stop.is_set():
        return 2
    if refresh_code:
        return refresh_code
    failed = [code for code in codes if code]
    if failed:
        print(f"{len(failed)} grader runs exited non-zero; see the per-model logs", flush=True)
        return 1
    print("luna pass finished", flush=True)
    return 0


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--key", required=True, choices=sorted(KEYS), help="which key file to read")
    raise SystemExit(main(parser.parse_args().key))
