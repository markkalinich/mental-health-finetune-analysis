#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare the Gaur et al. 2019 Reddit C-SSRS user-level gold-standard CSV.

Reads the Zenodo 500-user psychiatrist labels from /shared, writes a scoring
table with stable item ids, and writes schema/counts only (no post text).

Do not print User, Post, or other cell values. Gold-standard labels attach to users.
If Post is a Python list of that user's posts, join them with blank lines.
That is the paper's user-level unit, not a new aggregation.
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import sys
from collections import Counter
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))
from config import datasets  # noqa: E402



# Exact Label strings in 500_Reddit_users_posts_labels.csv (Gaur et al. WWW 2019).
CANONICAL_LABELS = ("Supportive", "Indicator", "Ideation", "Behavior", "Attempt")


def _posts_to_user_text(raw_post: str) -> tuple[str, str]:
    """Return (text, post_shape) without inventing a different unit."""
    s = "" if raw_post is None else str(raw_post)
    stripped = s.strip()
    if stripped.startswith("[") and stripped.endswith("]"):
        try:
            parsed = ast.literal_eval(stripped)
        except (ValueError, SyntaxError):
            parsed = None
        if isinstance(parsed, (list, tuple)):
            parts = [str(p) for p in parsed if str(p).strip()]
            return "\n\n".join(parts), "list"
    return s, "string"


def prepare(raw_path: Path, prepared_path: Path, schema_path: Path) -> dict:
    if not raw_path.is_file():
        raise FileNotFoundError(f"raw psychiatrist-label CSV not found: {raw_path}")

    with raw_path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols = list(reader.fieldnames or [])
        if cols != ["User", "Post", "Label"]:
            raise ValueError(f"unexpected raw columns {cols}; expected User, Post, Label")
        rows = list(reader)

    if len(rows) != 500:
        raise ValueError(f"expected 500 user rows, got {len(rows)}")

    out_rows = []
    shapes = Counter()
    empty_text = 0
    labels = []
    for i, row in enumerate(rows):
        label = (row.get("Label") or "").strip()
        if label not in CANONICAL_LABELS:
            raise ValueError(f"unexpected gold-standard label {label!r} at row {i}")
        text, shape = _posts_to_user_text(row.get("Post") or "")
        shapes[shape] += 1
        if not text.strip():
            empty_text += 1
        labels.append(label)
        out_rows.append({
            "item_id": f"u{i:03d}",
            "text": text,
            "standard_label": label,
        })

    if empty_text:
        raise SystemExit(
            f"STOP: {empty_text}/{len(out_rows)} prepared rows have empty text. "
            "Do not scrape Reddit; the Zenodo file must already contain posts."
        )

    prepared_path.parent.mkdir(parents=True, exist_ok=True)
    with prepared_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["item_id", "text", "standard_label"])
        writer.writeheader()
        writer.writerows(out_rows)

    counts = {lab: labels.count(lab) for lab in CANONICAL_LABELS}
    schema = {
        "source_doi": "10.5281/zenodo.2667859",
        "paper": "Gaur et al. WWW 2019; Knowledge-aware Assessment of Severity of Suicide Risk for Early Intervention",
        "unit": "user",
        "n_items": len(out_rows),
        "raw_columns": ["User", "Post", "Label"],
        "prepared_columns": ["item_id", "text", "standard_label"],
        "prepared_path": str(prepared_path),
        "raw_path": str(raw_path),
        "label_set": list(CANONICAL_LABELS),
        "label_counts": counts,
        "post_cell_shape": dict(shapes),
        "notes": (
            "One gold-standard label per user.  Post is a Python-list of that user's posts "
            "for list-shaped rows; remaining rows are a single string.  Prepared "
            "text joins list items with blank lines.  Default eval is this 2019 "
            "user-level file, not the optional 2021 post-level Zenodo record."
        ),
    }
    schema_path.parent.mkdir(parents=True, exist_ok=True)
    schema_path.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")
    return schema


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare Reddit C-SSRS user-level gold standard (no text printed).")
    # Defaults are config/datasets.csv: cssrs_raw (checked), cssrs_users and cssrs_schema (written here;
    # update their checksums in the manifest after a rewrite).
    parser.add_argument("--raw", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--schema", type=Path, default=None)
    args = parser.parse_args()
    if args.raw is None:
        args.raw = datasets.path("cssrs_raw")
    if args.out is None:
        args.out = datasets.location("cssrs_users")
    if args.schema is None:
        args.schema = datasets.location("cssrs_schema")
    schema = prepare(args.raw, args.out, args.schema)
    print("prepared_ok")
    print("n_items", schema["n_items"])
    print("label_set", ",".join(schema["label_set"]))
    for lab in schema["label_set"]:
        print(f"count\t{lab}\t{schema['label_counts'][lab]}")
    print("post_cell_shape", json.dumps(schema["post_cell_shape"], sort_keys=True))
    print("prepared_path", schema["prepared_path"])
    print("schema_path", args.schema)
    return 0


if __name__ == "__main__":
    sys.exit(main())
