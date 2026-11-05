#!/usr/bin/env python3
"""Fit the manuscript's mixed models from the current roster.

Runs orchestration/joint_and_paired.py (the Table 1 mixed model and the
fine-tune-minus-parent fits in category-deltas.csv) and then
orchestration/mhb_variance_retry.py (the MentalHealthBench inference
decision) into one folder:

    outputs/mixed-models/<day of the run>/

and writes outputs/mixed-models/CURRENT last. Table 1 in
publish_manuscript_figures.py reads the folder CURRENT names. An older dated
folder is a previous fit.

    .venv/bin/python orchestration/fit_mixed_models.py [--date YYYY-MM-DD]
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

MIXED_ROOT = REPO / "outputs/mixed-models"
POINTER = MIXED_ROOT / "CURRENT"
SOURCE_NAME = "roster-source.txt"


def mixed_dir(day: str | None = None) -> Path:
    return MIXED_ROOT / (day or date.today().isoformat())


def current_mixed_dir() -> Path:
    if not POINTER.is_file():
        raise SystemExit(f"{POINTER} does not exist; run orchestration/fit_mixed_models.py")
    text = POINTER.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit(f"{POINTER} is empty")
    return MIXED_ROOT / text


def source_sha256(folder: Path) -> str:
    """The sha256 of the roster a fit folder was made from, as recorded by the fit."""
    path = folder / SOURCE_NAME
    if not path.is_file():
        raise SystemExit(f"{path} is missing; the folder is not a complete fit")
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("sha256: "):
            return line.split(": ", 1)[1].strip()
    raise SystemExit(f"{path} has no sha256 line")


def main(day: str | None = None) -> Path:
    from orchestration import joint_and_paired, mhb_variance_retry

    out = mixed_dir(day)
    joint_and_paired.main(out)
    mhb_variance_retry.main(out)
    POINTER.write_text(out.name + "\n", encoding="utf-8")
    print(f"{POINTER} = {out.name}")
    return out


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--date", help="folder name under mixed-models/ (default: today, YYYY-MM-DD)")
    main(parser.parse_args().date)
