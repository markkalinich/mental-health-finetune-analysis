"""Fill yes/no and MentalHealthBench columns on roster rows.

A short file leaves the task blank. A format failure with no Sonnet row counts
as unlabeled, and sensitivity, specificity, and F1 stay blank while any reply
is unlabeled. This does not append the locked Sonnet files.

A rewrite that would blank a filled si_f1, cssrs_f1, mhb_safety, or mhb_total
stops without writing. The manuscript draw refreshes the roster once from these
files, checks the written roster against a fresh fill once, then fits the
mixed models and draws the figures from that one file. The labeled-figure
filter is not applied to the file that is written.
"""

from __future__ import annotations

import csv
import os
import sqlite3
from collections import defaultdict
from pathlib import Path

import orchestration.plot_parse_rates as ppr

LABELS = ("answered_yes", "answered_no", "not_an_answer")
SCORE_COLUMNS = ("si_f1", "cssrs_f1", "mhb_safety", "mhb_total")


def _cell(row: dict, column: str) -> str:
    return (row.get(column) or "").strip()


def score_drops(old_rows: list[dict], new_rows: list[dict]) -> list[str]:
    """Filled score cells that the new rows would save as blank."""
    old = {row["hf_id"]: row for row in old_rows}
    drops = []
    for row in new_rows:
        previous = old.get(row["hf_id"])
        if previous is None:
            continue
        for column in SCORE_COLUMNS:
            if _cell(previous, column) and not _cell(row, column):
                drops.append(f"{row['hf_id']} {column}")
    return drops


def score_disagreements(old_rows: list[dict], new_rows: list[dict]) -> list[str]:
    """Roster cells whose si_f1, cssrs_f1, or mhb_safety differ from a fresh fill."""
    old = {row["hf_id"]: row for row in old_rows}
    found = []
    for row in new_rows:
        previous = old.get(row["hf_id"])
        if previous is None:
            found.append(f"{row['hf_id']} missing from roster")
            continue
        for column in SCORE_COLUMNS:
            before = _cell(previous, column)
            after = _cell(row, column)
            if before != after:
                found.append(
                    f"{row['hf_id']} {column} roster {before or 'blank'} fill {after or 'blank'}"
                )
    return found


def refuse_score_drops(old_rows: list[dict], new_rows: list[dict]) -> None:
    drops = score_drops(old_rows, new_rows)
    if drops:
        raise SystemExit("score fill would blank a filled cell:\n" + "\n".join(drops))


def require_same_scores(old_rows: list[dict], new_rows: list[dict]) -> None:
    found = score_disagreements(old_rows, new_rows)
    if found:
        raise SystemExit("roster scores disagree with a fresh fill:\n" + "\n".join(found))


def assert_roster_matches_fill() -> None:
    """Stop before a figure is drawn when the roster and a fresh fill differ."""
    from orchestration.study_roster import load_roster

    rows = load_roster()
    require_same_scores(rows, fill_scores(rows))


def _empty_scores() -> dict[str, str]:
    keys = [
        "si_n", "si_strict_parsed", "si_sonnet_answered_yes", "si_sonnet_answered_no",
        "si_sonnet_not_an_answer", "si_sonnet_unlabeled",
        "si_sensitivity", "si_specificity", "si_f1",
        "cssrs_n", "cssrs_strict_parsed", "cssrs_sonnet_answered_yes", "cssrs_sonnet_answered_no",
        "cssrs_sonnet_not_an_answer", "cssrs_sonnet_unlabeled",
        "cssrs_sensitivity", "cssrs_specificity", "cssrs_f1",
        "mhb_n", "mhb_n_parsed", "mhb_safety", "mhb_total",
    ]
    return {key: "" for key in keys}


def _fmt(value: float) -> str:
    return f"{value:.6f}"


def _task_f1(triples: list[tuple[bool, bool | None, str | None]], expected: int, mode: str) -> float | None:
    """F1 for one task. None leaves the roster cell blank, as _apply_yesno does.

    strict uses only the format check. sonnet fills a format failure with
    answered_yes or answered_no and leaves not_an_answer unparsed. A short
    file, or a sonnet file with an unlabeled failure, returns None.
    """
    if mode not in {"strict", "sonnet"}:
        raise SystemExit(f"parse mode must be strict or sonnet, not {mode!r}")
    if len(triples) != expected:
        return None
    unlabeled = 0
    pairs = []
    for gold, pred, label in triples:
        use = pred
        if mode == "sonnet" and use is None:
            if label == "answered_yes":
                use = True
            elif label == "answered_no":
                use = False
            elif label == "not_an_answer":
                use = None
            else:
                unlabeled += 1
                use = None
        pairs.append((gold, use))
    if mode == "sonnet" and unlabeled:
        return None
    return ppr._binary(pairs)["f1"]


def f1_by_model(model_ids: set[str], mode: str) -> dict[str, dict[str, float | None]]:
    """si_f1 and cssrs_f1 for each id. The readers are the roster fill."""
    si = _si_triples(model_ids)
    cssrs = _cssrs_triples(model_ids)
    found = {}
    for name in model_ids:
        found[name] = {
            "si_f1": _task_f1(si.get(name, []), 450, mode),
            "cssrs_f1": _task_f1(cssrs.get(name, []), 500, mode),
        }
    return found


def _apply_yesno(row: dict, prefix: str, triples: list[tuple[bool, bool | None, str | None]], expected: int) -> None:
    if len(triples) != expected:
        return
    n_parsed = sum(pred is not None for _gold, pred, _label in triples)
    counts = {label: 0 for label in LABELS}
    unlabeled = 0
    for _gold, pred, label in triples:
        if pred is not None:
            continue
        if label in counts:
            counts[label] += 1
        else:
            unlabeled += 1
    row[f"{prefix}n"] = str(expected)
    row[f"{prefix}strict_parsed"] = str(n_parsed)
    row[f"{prefix}sonnet_answered_yes"] = str(counts["answered_yes"])
    row[f"{prefix}sonnet_answered_no"] = str(counts["answered_no"])
    row[f"{prefix}sonnet_not_an_answer"] = str(counts["not_an_answer"])
    row[f"{prefix}sonnet_unlabeled"] = str(unlabeled)
    if unlabeled:
        return
    pairs = []
    for gold, pred, label in triples:
        if pred is None:
            if label == "answered_yes":
                pred = True
            elif label == "answered_no":
                pred = False
            else:
                pred = None
        pairs.append((gold, pred))
    metrics = ppr._binary(pairs)
    row[f"{prefix}sensitivity"] = _fmt(metrics["sens"])
    row[f"{prefix}specificity"] = _fmt(metrics["spec"])
    row[f"{prefix}f1"] = _fmt(metrics["f1"])


def _study_labels() -> dict[str, str]:
    """Sonnet labels, from replies/lenient-parse-pilot/labels-current.jsonl only.

    orchestration/consolidate_sonnet_labels.py writes that file from the stored
    label files and stops when two of them disagree. refresh_roster() rewrites
    it before every fill.
    """
    from orchestration.consolidate_sonnet_labels import read_current

    return read_current()


def _si_triples(model_ids: set[str]) -> dict[str, list[tuple[bool, bool | None, str | None]]]:
    gold = ppr._gold_si_v2()
    labels = _study_labels()
    found: dict[str, list] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    with sqlite3.connect(f"file:{ppr.CACHE_DB}?mode=ro", uri=True) as conn:
        rows = conn.execute(
            """
            SELECT ck.model_full_name, ck.input_hash, cr.raw_response
            FROM cache_keys ck
            JOIN cached_results cr ON ck.cache_id = cr.cache_id
            WHERE ck.prompt_name = 'suicide_ideation_yesno_v2' AND cr.replicate_index = 0
            """
        )
        for name, digest, raw in rows:
            if name not in model_ids or digest not in gold:
                continue
            key = (name, digest)
            if key in seen:
                continue
            seen.add(key)
            text = ppr._message_text(raw or "")
            label_id = f"si|{name}|{digest}"
            found[name].append((gold[digest], ppr._format_yes(name, text), labels.get(label_id)))
    return found


def _cssrs_triples(model_ids: set[str]) -> dict[str, list[tuple[bool, bool | None, str | None]]]:
    labels = _study_labels()
    found: dict[str, list] = {}
    for name in model_ids:
        path = ppr.CSSRS_YESNO / name.replace("/", "__") / "predictions.csv"
        if not path.is_file():
            continue
        triples = []
        with path.open(encoding="utf-8", newline="") as handle:
            for index, record in enumerate(csv.DictReader(handle)):
                text = record.get("raw_response") or ""
                triples.append(
                    (
                        ppr._gold_flag(record["gold_yes"], path),
                        ppr._format_yes(name, text),
                        labels.get(f"cssrs|{name}|{index}"),
                    )
                )
        found[name] = triples
    return found


def _apply_mhb(row: dict, item: dict | None) -> None:
    """MentalHealthBench columns.

    mhb_n and mhb_n_parsed are the 1,215 conversations: answered, and answered
    with a non-empty reply. They are filled when the reply file is complete.
    mhb_safety is the English suicide and self-harm score (orchestration.plot_spaghetti_mhb_safety.MHB_SAFETY_N conversations) and mhb_total is
    the full-bench score; both are filled only when the run is processed
    (orchestration.mhb_status). An empty reply counts in mhb_n, not mhb_n_parsed.
    """
    if item is None:
        return
    row["mhb_n"] = str(item["n"])
    row["mhb_n_parsed"] = str(item["n_parsed"])
    if "safety86" in item:
        row["mhb_safety"] = _fmt(item["safety86"])
        row["mhb_total"] = _fmt(item["total"])


def _mhb_items(model_ids: set[str]) -> dict[str, dict]:
    """Per model: 1,215-conversation counts, and the two scores when processed."""
    from orchestration.mhb_status import N_CONVERSATIONS, dataset_rubric, grade_file_status

    rubric = dataset_rubric()
    graded = ppr._mhb_scores(model_ids)
    found = {}
    for name in model_ids:
        status = grade_file_status(name, rubric)
        if status.status in ("not_run", "needs_gpu"):
            continue
        item = {"n": N_CONVERSATIONS, "n_parsed": status.n_nonempty}
        if status.processed:
            if name not in graded:
                raise SystemExit(f"{name} is processed and has no MentalHealthBench score")
            item["safety86"] = graded[name]["safety86"]
            item["total"] = graded[name]["total"]
        found[name] = item
    return found


def fill_scores(rows: list[dict]) -> list[dict]:
    model_ids = {row["hf_id"] for row in rows}
    si = _si_triples(model_ids)
    cssrs = _cssrs_triples(model_ids)
    mhb = _mhb_items(model_ids)
    filled = []
    for row in rows:
        out = dict(row)
        out.update(_empty_scores())
        name = row["hf_id"]
        _apply_yesno(out, "si_", si.get(name, []), 450)
        _apply_yesno(out, "cssrs_", cssrs.get(name, []), 500)
        _apply_mhb(out, mhb.get(name))
        filled.append(out)
    return filled


def _load_for_rewrite(path: Path) -> list[dict]:
    """Every roster row. The labeled-figure filter must not shrink the file."""
    saved = os.environ.pop("MANUSCRIPT_LABELED", None)
    try:
        from orchestration.study_roster import load_roster

        return load_roster(path)
    finally:
        if saved is not None:
            os.environ["MANUSCRIPT_LABELED"] = saved


def rewrite(path: Path) -> None:
    """Fill scores in the existing roster file. The directory name stays."""
    path = Path(path)
    rows = _load_for_rewrite(path)
    _write_filled(path, rows, fill_scores(rows))


def _write_filled(path: Path, rows: list[dict], filled: list[dict]) -> None:
    from orchestration.study_roster import COLUMNS

    refuse_score_drops(rows, filled)
    if len(filled) != len(rows):
        raise SystemExit(f"score fill changed the roster from {len(rows)} rows to {len(filled)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        for row in filled:
            writer.writerow({key: row.get(key, "") for key in COLUMNS})


def score_input_files(model_ids: set[str]) -> list[tuple[Path, str | None]]:
    """Every file whose content decides a score cell on the roster, with the
    model id for a MentalHealthBench grade file (None for every other file).

    The synthetic-SI database, each model's C-SSRS predictions file, each
    model's MentalHealthBench replies and grades, and the stored Sonnet label
    files that consolidate_sonnet_labels merges.
    """
    from orchestration.consolidate_sonnet_labels import _source_files
    from orchestration.mhb_status import GENERATIONS_NAME, GRADES_NAME, run_directory

    files: list[tuple[Path, str | None]] = [(ppr.CACHE_DB.resolve(), None)]
    for name in sorted(model_ids):
        files.append((ppr.CSSRS_YESNO / name.replace("/", "__") / "predictions.csv", None))
        files.append((run_directory(name) / GENERATIONS_NAME, None))
        files.append((run_directory(name) / GRADES_NAME, name))
    files.extend((path, None) for path, _prefixes in _source_files())
    return files


def input_snapshot(model_ids: set[str]) -> dict[str, tuple]:
    """What each score input contributed at this moment.

    For every file: ("file", size, mtime), or ("missing",). For a
    MentalHealthBench grade file: ("processed", size, mtime) when the run is
    processed, else ("not processed",). A grade file that is still being
    appended feeds no cell until it is complete (mhb_safety and mhb_total come
    only from processed runs; mhb_n and mhb_n_parsed come from the replies
    file), so an append to an unfinished file is not a change; a file that
    becomes processed, or a processed file that changes, is.
    """
    from orchestration.mhb_status import dataset_rubric, grade_file_status

    rubric = dataset_rubric()
    snapshot: dict[str, tuple] = {}
    for path, hf_id in score_input_files(model_ids):
        if hf_id is not None:
            status = grade_file_status(hf_id, rubric)
            if not status.processed:
                snapshot[str(path)] = ("not processed",)
                continue
            stat = path.stat()
            snapshot[str(path)] = ("processed", stat.st_size, stat.st_mtime_ns)
            continue
        try:
            stat = path.stat()
        except FileNotFoundError:
            snapshot[str(path)] = ("missing",)
            continue
        snapshot[str(path)] = ("file", stat.st_size, stat.st_mtime_ns)
    return snapshot


def refresh_roster() -> Path:
    """Copy scores from the reply, grade, and label files into the current roster.

    The Sonnet label file is consolidated first. The score inputs are
    snapshotted (input_snapshot) before the fill and again after it; an input
    that changed what it contributes in between (a labeler appending, a grade
    file becoming complete) stops the run before the roster is written. Rerun
    when the writer has finished.
    """
    from orchestration.consolidate_sonnet_labels import consolidate
    from orchestration.study_roster import roster_csv

    consolidate()
    path = roster_csv()
    rows = _load_for_rewrite(path)
    model_ids = {row["hf_id"] for row in rows}
    before = input_snapshot(model_ids)
    filled = fill_scores(rows)
    after = input_snapshot(model_ids)
    changed = sorted(key for key in before if before[key] != after.get(key))
    if changed:
        raise SystemExit(
            "score inputs changed while the roster was being filled; rerun when the writer is done:\n"
            + "\n".join(changed)
        )
    _write_filled(path, rows, filled)
    return path
