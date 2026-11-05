"""Every filter note must quote the current counts.csv, not an older pass.

For each grouping with a CURRENT file, doc_counts.py --check compares the generated block in
docs/<grouping>_FT_funnel/how-models-are-filtered.md with outputs/funnel/<grouping>/<CURRENT>/counts.csv.
A grouping whose note has no marker block is skipped with a message.

    .venv/bin/python model_selection/tests/test_docs_match_counts.py
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(PKG))
import cache  # noqa: E402
import doc_counts  # noqa: E402


def test_docs_match_counts() -> None:
    failures = []
    for grouping, doc in doc_counts.DOC.items():
        if not cache.current_path(grouping).exists():
            print(f"skip {grouping}: no CURRENT file")
            continue
        if doc_counts.BEGIN not in doc.read_text():
            print(f"skip {grouping}: {doc.name} has no {doc_counts.BEGIN} block yet")
            continue
        proc = subprocess.run([sys.executable, str(PKG / "doc_counts.py"), "--grouping", grouping, "--check"],
                              capture_output=True, text=True)
        print((proc.stdout + proc.stderr).strip())
        if proc.returncode:
            failures.append(grouping)
    assert not failures, f"stale count table in: {failures}"


if __name__ == "__main__":
    test_docs_match_counts()
    print("OK")
