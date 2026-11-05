#!/usr/bin/env python3
"""Write the one Sonnet label file every score reader uses.

Output: replies/lenient-parse-pilot/labels-current.jsonl, one row per labeled
reply: {"id", "label", "source"}. ``id`` is ``si|<model>|<cache hash>`` or
``cssrs|<model>|<row index>``; ``label`` is answered_yes, answered_no, or
not_an_answer; ``source`` is the stored file the label came from, relative to
replies/lenient-parse-pilot.

Inputs are the stored label files listed in SOURCES, in that order. They are
read, never written. Every (id, label) pair found is kept; an id that two
files label differently stops the run and names both files. The one known
exception is written down here, not discovered at run time:

  sonnet-full.jsonl labeled the 17 October draft prompts. Its ``si|`` rows are
  the study synthetic-SI prompt (v2) and are used. Its ``cssrs|`` rows are the
  v4 C-SSRS replies; the same ``cssrs|<model>|<index>`` id names a different
  reply under v5, so those rows are not read.

Readers (fill_roster_scores, plot_sonnet_recovery) read labels-current.jsonl
and nothing else. refresh_roster() rewrites it first, so a new label file
dropped into one of the SOURCES folders is picked up on the next fill and a
conflicting one stops the fill.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

PILOT = REPO / "replies/lenient-parse-pilot"
OUTPUT = PILOT / "labels-current.jsonl"
LABELS = ("answered_yes", "answered_no", "not_an_answer")

# (path or glob relative to PILOT, id prefixes read from it)
SOURCES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("sonnet-full.jsonl", ("si|",)),
    ("sonnet-cssrs-v5.jsonl", ("cssrs|",)),
    ("sonnet-pretrained-20261018.jsonl", ("si|", "cssrs|")),
    ("sonnet-si-unlabeled-20261020.jsonl", ("si|",)),
    ("firstline-sample-20261019/sonnet-*.jsonl", ("si|", "cssrs|")),
    ("firstline-20pct-20261019/sonnet-*.jsonl", ("si|", "cssrs|")),
    ("firstline-30pct-20261019/sonnet-*.jsonl", ("si|", "cssrs|")),
    ("firstline-30pct-b-20261019/sonnet-*.jsonl", ("si|", "cssrs|")),
    ("firstline-rest-20261019/sonnet-*.jsonl", ("si|", "cssrs|")),
    ("unlabeled-medical-20261020/*/sonnet.jsonl", ("si|", "cssrs|")),
    ("sonnet-three-parents-20261021/labels/*/*.jsonl", ("si|", "cssrs|")),
    ("sonnet-bases-20261022/labels/*/*.jsonl", ("si|", "cssrs|")),
)


def _source_files() -> list[tuple[Path, tuple[str, ...]]]:
    found = []
    for pattern, prefixes in SOURCES:
        paths = sorted(PILOT.glob(pattern)) if any(ch in pattern for ch in "*?[") else [PILOT / pattern]
        if not paths:
            raise SystemExit(f"no label files match {PILOT / pattern}")
        for path in paths:
            if not path.is_file():
                raise SystemExit(f"missing label file {path}")
            found.append((path, prefixes))
    return found


def consolidate() -> dict[str, str]:
    """Merge the stored files. Returns id -> label and writes OUTPUT."""
    labels: dict[str, str] = {}
    origin: dict[str, str] = {}
    for path, prefixes in _source_files():
        rel = str(path.relative_to(PILOT))
        with path.open(encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                row = json.loads(line)
                rid = row.get("id")
                label = row.get("label")
                if not isinstance(rid, str) or not rid:
                    raise SystemExit(f"{rel} line {line_no}: no id")
                if not rid.startswith(prefixes):
                    continue
                if label not in LABELS:
                    raise SystemExit(f"{rel} line {line_no}: {rid} has label {label!r}, not one of {LABELS}")
                previous = labels.get(rid)
                if previous is not None and previous != label:
                    raise SystemExit(
                        f"{rid} is {previous} in {origin[rid]} and {label} in {rel}. "
                        "Two stored files disagree; decide which is right before any score is filled."
                    )
                if previous is None:
                    labels[rid] = label
                    origin[rid] = rel
    tmp = OUTPUT.with_suffix(".jsonl.tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        for rid in sorted(labels):
            handle.write(json.dumps({"id": rid, "label": labels[rid], "source": origin[rid]}, ensure_ascii=False) + "\n")
    tmp.replace(OUTPUT)
    return labels


def read_current() -> dict[str, str]:
    """id -> label from labels-current.jsonl. Missing file stops the run."""
    if not OUTPUT.is_file():
        raise SystemExit(f"{OUTPUT} does not exist; run orchestration/consolidate_sonnet_labels.py")
    labels: dict[str, str] = {}
    with OUTPUT.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            rid, label = row["id"], row["label"]
            if label not in LABELS:
                raise SystemExit(f"{OUTPUT} line {line_no}: {rid} has label {label!r}")
            if rid in labels:
                raise SystemExit(f"{OUTPUT} line {line_no}: {rid} appears twice")
            labels[rid] = label
    return labels


def main() -> int:
    labels = consolidate()
    si = sum(1 for rid in labels if rid.startswith("si|"))
    print(f"wrote {OUTPUT}: {len(labels)} labels (si {si}, cssrs {len(labels) - si})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
