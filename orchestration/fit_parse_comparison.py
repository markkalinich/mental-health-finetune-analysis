#!/usr/bin/env python3
"""Refit the current mixed model on strict F1 and on Sonnet-recovered F1.

Writes two folders next to the dated fits. Does not change mixed-models/CURRENT.

    outputs/mixed-models/strict_parsing/
    outputs/mixed-models/sonnet_parsing/

MentalHealthBench scores are the roster scores in both. Strict F1 ignores
Sonnet labels. Sonnet F1 is checked against the roster before the fit.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from orchestration.fit_mixed_models import MIXED_ROOT
from orchestration import joint_and_paired, mhb_variance_retry


def main() -> None:
    for mode in ("sonnet", "strict"):
        dest = MIXED_ROOT / f"{mode}_parsing"
        joint_and_paired.main(dest, parse_mode=mode)
        mhb_variance_retry.main(dest)
        print(f"wrote {dest}")


if __name__ == "__main__":
    main()
