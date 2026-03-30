#!/usr/bin/env python3
"""
Read-only SQL aggregates on cache results.db. Writes facts only (no interpretation).

Usage:
  python utilities/cache_qc_report.py
  python utilities/cache_qc_report.py --db manuscript_paper_cache/results.db
  python utilities/cache_qc_report.py --output manuscript_paper_cache/qc_report_latest.txt
"""

from __future__ import annotations

import argparse
import io
import sqlite3
import sys
from pathlib import Path
from typing import TextIO

ROOT = Path(__file__).resolve().parent.parent


def connect(db: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{db.resolve()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


class TeeStdout:
    """Send stdout to console and optional file."""

    def __init__(self, file_obj: TextIO | None) -> None:
        self._file = file_obj
        self._stdout = sys.__stdout__

    def write(self, s: str) -> int:
        self._stdout.write(s)
        if self._file is not None:
            self._file.write(s)
        return len(s)

    def flush(self) -> None:
        self._stdout.flush()
        if self._file is not None:
            self._file.flush()


def section(out: TextIO, title: str) -> None:
    print(file=out)
    print("=" * 72, file=out)
    print(title, file=out)
    print("=" * 72, file=out)


def run_report(conn: sqlite3.Connection, out: TextIO) -> None:
    section(out, "0) Row counts and partition by prompt_name")
    ck = conn.execute("SELECT COUNT(*) FROM cache_keys").fetchone()[0]
    cr = conn.execute("SELECT COUNT(*) FROM cached_results").fetchone()[0]
    print(f"cache_keys:     {ck}", file=out)
    print(f"cached_results: {cr}", file=out)
    parts = conn.execute(
        """
        SELECT prompt_name, COUNT(*) AS n
        FROM cache_keys
        GROUP BY prompt_name
        ORDER BY prompt_name
        """
    ).fetchall()
    s = sum(r["n"] for r in parts)
    print("cache_keys by prompt_name:", file=out)
    for r in parts:
        print(f"  {r['prompt_name']}: {r['n']}", file=out)
    print(f"sum of above: {s}  (equals cache_keys: {s == ck})", file=out)

    section(out, "1) prompt_hash (content MD5); prompt_name (stored label)")
    n_distinct_hash = conn.execute(
        "SELECT COUNT(DISTINCT prompt_hash) FROM cache_keys"
    ).fetchone()[0]
    print(f"COUNT(DISTINCT prompt_hash): {n_distinct_hash}", file=out)
    print("", file=out)
    print("Per prompt_name: COUNT(DISTINCT prompt_hash), cache_keys:", file=out)
    by_name = conn.execute(
        """
        SELECT prompt_name, COUNT(DISTINCT prompt_hash) AS n_dh, COUNT(*) AS n_keys
        FROM cache_keys
        GROUP BY prompt_name
        ORDER BY prompt_name
        """
    ).fetchall()
    for r in by_name:
        print(f"  {r['prompt_name']}: {r['n_dh']}, {r['n_keys']}", file=out)

    print("", file=out)
    print("(prompt_name, prompt_hash, cache_keys):", file=out)
    rows = conn.execute(
        """
        SELECT prompt_name, prompt_hash, COUNT(*) AS n_keys
        FROM cache_keys
        GROUP BY prompt_name, prompt_hash
        ORDER BY prompt_name, prompt_hash
        """
    ).fetchall()
    for r in rows:
        print(f"  {r['prompt_name']}: {r['prompt_hash']}  {r['n_keys']}", file=out)

    print("", file=out)
    print(
        "prompt_hash values with COUNT(DISTINCT prompt_name) > 1:",
        file=out,
    )
    multi = conn.execute(
        """
        SELECT prompt_hash,
               COUNT(DISTINCT prompt_name) AS n_names,
               GROUP_CONCAT(DISTINCT prompt_name) AS names
        FROM cache_keys
        GROUP BY prompt_hash
        HAVING COUNT(DISTINCT prompt_name) > 1
        """
    ).fetchall()
    if not multi:
        print("  (none)", file=out)
    for r in multi:
        print(f"  hash={r['prompt_hash']}  prompt_names={r['n_names']}  {r['names']}", file=out)

    section(out, "2) input_hash per prompt_name (distinct input_hash, cache_keys)")
    per_prompt = conn.execute(
        """
        SELECT prompt_name, COUNT(DISTINCT input_hash) AS n_u, COUNT(*) AS n_ck
        FROM cache_keys
        GROUP BY prompt_name
        ORDER BY prompt_name
        """
    ).fetchall()
    for r in per_prompt:
        print(f"  {r['prompt_name']}: {r['n_u']}, {r['n_ck']}", file=out)

    section(out, "3) temperature, max_tokens, top_p")
    rows = conn.execute(
        """
        SELECT temperature, max_tokens, top_p, COUNT(*) AS n
        FROM cache_keys
        GROUP BY temperature, max_tokens, top_p
        ORDER BY n DESC
        """
    ).fetchall()
    print(f"distinct (temperature, max_tokens, top_p) rows: {len(rows)}", file=out)
    for r in rows:
        print(
            f"  {r['temperature']}, {r['max_tokens']}, {r['top_p']}: {r['n']}",
            file=out,
        )

    section(out, "4) cache_keys.created_at by calendar day")
    rows = conn.execute(
        """
        SELECT substr(created_at, 1, 10) AS day, COUNT(*) AS n
        FROM cache_keys
        GROUP BY day
        ORDER BY day
        """
    ).fetchall()
    max_n = max(r["n"] for r in rows) if rows else 1
    bar_w = 40
    for r in rows:
        bar_len = int(bar_w * r["n"] / max_n) if max_n else 0
        print(f"  {r['day']}  {r['n']:7}  {'#' * bar_len}", file=out)
    mm = conn.execute(
        "SELECT MIN(created_at), MAX(created_at) FROM cache_keys"
    ).fetchone()
    print(f"MIN(created_at): {mm[0]}", file=out)
    print(f"MAX(created_at): {mm[1]}", file=out)

    section(out, "5) cached_results: replicate_index, status, api_error breakdown")
    ck2 = conn.execute("SELECT COUNT(*) FROM cache_keys").fetchone()[0]
    cr2 = conn.execute("SELECT COUNT(*) FROM cached_results").fetchone()[0]
    it = conn.execute("SELECT COUNT(*) FROM input_texts").fetchone()[0]
    print(f"cache_keys: {ck2}", file=out)
    print(f"cached_results: {cr2}", file=out)
    print(f"input_texts: {it}", file=out)

    rep = conn.execute(
        """
        SELECT replicate_index, COUNT(*) AS n
        FROM cached_results
        GROUP BY replicate_index
        ORDER BY replicate_index
        """
    ).fetchall()
    print("replicate_index:", file=out)
    for r in rep:
        print(f"  {r['replicate_index']}: {r['n']}", file=out)

    n_ok = conn.execute(
        "SELECT COUNT(*) FROM cached_results WHERE status = 'ok'"
    ).fetchone()[0]
    n_pf = conn.execute(
        "SELECT COUNT(*) FROM cached_results WHERE status = 'parse_fail'"
    ).fetchone()[0]
    n_api = conn.execute(
        "SELECT COUNT(*) FROM cached_results WHERE status LIKE 'api_error%'"
    ).fetchone()[0]
    n_other = cr2 - n_ok - n_pf - n_api
    print("status:", file=out)
    print(f"  ok: {n_ok}", file=out)
    print(f"  parse_fail: {n_pf}", file=out)
    print(f"  api_error: {n_api}", file=out)
    if n_other:
        print(f"  other: {n_other}", file=out)
    if cr2:
        print(f"api_error / cached_results: {n_api / cr2:.6f}", file=out)

    n_to = conn.execute(
        """
        SELECT COUNT(*) FROM cached_results
        WHERE status LIKE 'api_error%' AND status LIKE '%timeout%'
        """
    ).fetchone()[0]
    n_400 = conn.execute(
        """
        SELECT COUNT(*) FROM cached_results
        WHERE status LIKE 'api_error%' AND status LIKE '%400%'
        """
    ).fetchone()[0]
    n_rest = n_api - n_to - n_400
    print("api_error substring counts on status field:", file=out)
    print(f"  LIKE '%timeout%': {n_to}", file=out)
    print(f"  LIKE '%400%': {n_400}", file=out)
    print(f"  remaining api_error: {n_rest}", file=out)

    rows = conn.execute(
        """
        SELECT status, COUNT(*) AS n
        FROM cached_results
        WHERE status LIKE 'api_error%'
        GROUP BY status
        ORDER BY n DESC
        LIMIT 20
        """
    ).fetchall()
    print("DISTINCT api_error status values (top 20 by count):", file=out)
    for r in rows:
        msg = (r["status"] or "")[:100]
        print(f"  n={r['n']}: {msg}", file=out)


def main() -> int:
    parser = argparse.ArgumentParser(description="QC report for results.db (facts only)")
    parser.add_argument(
        "--db",
        type=Path,
        default=ROOT / "manuscript_paper_cache" / "results.db",
        help="Path to results.db (read-only)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Also write the full report to this file (UTF-8)",
    )
    args = parser.parse_args()

    if not args.db.exists():
        print(f"ERROR: Database not found: {args.db}", file=sys.stderr)
        return 1

    file_obj = None
    old_stdout = sys.stdout
    try:
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            file_obj = open(args.output, "w", encoding="utf-8")
            sys.stdout = TeeStdout(file_obj)

        print("cache_qc_report.py")
        print(f"database: {args.db.resolve()}")
        conn = connect(args.db)
        try:
            run_report(conn, sys.stdout)
        finally:
            conn.close()
        section(sys.stdout, "end")
    finally:
        sys.stdout = old_stdout
        if file_obj is not None:
            file_obj.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
