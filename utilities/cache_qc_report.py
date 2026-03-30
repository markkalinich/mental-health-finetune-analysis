#!/usr/bin/env python3
"""
Quality-control report for a results.db (full cache or manuscript subset).

Read-only; uses SQL aggregates only (no per-row JSON parsing) — typically
seconds to ~1–2 minutes on ~200k–300k rows.

Usage (from repo root, with pandas venv if needed):
  python utilities/cache_qc_report.py
  python utilities/cache_qc_report.py --db manuscript_paper_cache/results.db
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def connect(db: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{db.resolve()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def section(title: str) -> None:
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def q1_prompt_hashes(conn: sqlite3.Connection) -> None:
    section("1) Prompt hashes (task prompts + revisions / suffixes)")
    rows = conn.execute(
        """
        SELECT prompt_name, prompt_hash, COUNT(*) AS n_keys
        FROM cache_keys
        GROUP BY prompt_name, prompt_hash
        ORDER BY prompt_name, prompt_hash
        """
    ).fetchall()
    distinct_hashes = {r["prompt_hash"] for r in rows}
    print(f"Distinct prompt_hash values (global): {len(distinct_hashes)}")
    print("Per (prompt_name, prompt_hash):")
    for r in rows:
        print(f"  {r['prompt_name']:45}  hash={r['prompt_hash']}  cache_keys={r['n_keys']}")
    by_name = conn.execute(
        """
        SELECT prompt_name, COUNT(DISTINCT prompt_hash) AS n_hashes, COUNT(*) AS n_keys
        FROM cache_keys
        GROUP BY prompt_name
        ORDER BY prompt_name
        """
    ).fetchall()
    print("Distinct prompt_hash count per prompt_name:")
    for r in by_name:
        print(f"  {r['prompt_name']}: {r['n_hashes']} distinct hash(es), {r['n_keys']} cache_keys")
    print(
        "Interpretation: You will usually see MORE than 3 global hashes because:\n"
        "  • Model-specific prompt suffixes (e.g. Qwen /no_think) change prompt text → new hash.\n"
        "  • If the same prompt file was edited and re-run, old + new hashes can coexist.\n"
        "  • Legacy prompt_name strings may differ (e.g. TE) — see distinct prompt_name count."
    )
    n_names = conn.execute("SELECT COUNT(DISTINCT prompt_name) FROM cache_keys").fetchone()[0]
    print(f"Distinct prompt_name values: {n_names}")


def q2_input_hashes(conn: sqlite3.Connection) -> None:
    section("2) Input hashes — counts per task and global uniqueness")
    # Per prompt_name (task proxy)
    per_prompt = conn.execute(
        """
        SELECT prompt_name, COUNT(DISTINCT input_hash) AS n_unique_input_hash,
               COUNT(*) AS n_cache_keys
        FROM cache_keys
        GROUP BY prompt_name
        ORDER BY prompt_name
        """
    ).fetchall()
    for r in per_prompt:
        print(
            f"  {r['prompt_name']}: distinct input_hash={r['n_unique_input_hash']}, "
            f"cache_keys={r['n_cache_keys']}"
        )
    global_distinct = conn.execute(
        "SELECT COUNT(DISTINCT input_hash) FROM cache_keys"
    ).fetchone()[0]
    print(f"  Global DISTINCT input_hash (across all tasks): {global_distinct}")
    print("  Expected rows per task: SI=450, TR=780, TE=420 (if one row per input per model).")
    print("  Distinct input texts per task should match row counts above / n_models.")


def q3_api_params(conn: sqlite3.Connection) -> None:
    section("3) temperature, max_tokens, top_p (expect a single triple)")
    rows = conn.execute(
        """
        SELECT temperature, max_tokens, top_p, COUNT(*) AS n
        FROM cache_keys
        GROUP BY temperature, max_tokens, top_p
        ORDER BY n DESC
        """
    ).fetchall()
    print(f"Distinct (temperature, max_tokens, top_p) combinations: {len(rows)}")
    for r in rows:
        print(
            f"  temp={r['temperature']}  max_tokens={r['max_tokens']}  top_p={r['top_p']}  rows={r['n']}"
        )
    if len(rows) != 1:
        print("  WARNING: More than one API-parameter combination present.")


def q4_created_histogram(conn: sqlite3.Connection) -> None:
    section("4) created_at distribution (cache_keys.created_at)")
    # SQLite: substring day for bucketing without Python load
    rows = conn.execute(
        """
        SELECT substr(created_at, 1, 10) AS day, COUNT(*) AS n
        FROM cache_keys
        GROUP BY day
        ORDER BY day
        """
    ).fetchall()
    if not rows:
        print("No created_at data.")
        return
    print("Counts by calendar day (cache_keys):")
    max_n = max(r["n"] for r in rows) if rows else 1
    bar_width = 40
    for r in rows:
        day = r["day"] or "?"
        n = r["n"]
        bar_len = int(bar_width * n / max_n) if max_n else 0
        bar = "#" * bar_len
        print(f"  {day}  {n:7}  {bar}")

    # Min/max
    mm = conn.execute(
        "SELECT MIN(created_at), MAX(created_at) FROM cache_keys"
    ).fetchone()
    print(f"  MIN(created_at): {mm[0]}")
    print(f"  MAX(created_at): {mm[1]}")

    # Optional: cached_results created_at span
    mm2 = conn.execute(
        "SELECT MIN(created_at), MAX(created_at) FROM cached_results"
    ).fetchone()
    print(f"  cached_results MIN: {mm2[0]}")
    print(f"  cached_results MAX: {mm2[1]}")


def q5_extra(conn: sqlite3.Connection) -> None:
    section("5) Extra checks (recommended)")
    # Status mix — collapsed
    rows = conn.execute(
        """
        SELECT
          CASE
            WHEN status = 'ok' THEN 'ok'
            WHEN status = 'parse_fail' THEN 'parse_fail'
            WHEN status LIKE 'api_error%' THEN 'api_error (any)'
            ELSE status
          END AS bucket,
          COUNT(*) AS n
        FROM cached_results
        GROUP BY bucket
        ORDER BY n DESC
        """
    ).fetchall()
    print("cached_results status (collapsed):")
    for r in rows:
        print(f"  {r['bucket']}: {r['n']}")

    rows = conn.execute(
        """
        SELECT status, COUNT(*) AS n
        FROM cached_results
        WHERE status LIKE 'api_error%'
        GROUP BY status
        ORDER BY n DESC
        LIMIT 15
        """
    ).fetchall()
    if rows:
        print("Top api_error status strings (detail):")
        for r in rows:
            msg = (r["status"] or "")[:70]
            print(f"  n={r['n']:5}  {msg}")

    rep = conn.execute(
        """
        SELECT replicate_index, COUNT(*) AS n
        FROM cached_results
        GROUP BY replicate_index
        ORDER BY replicate_index
        """
    ).fetchall()
    print("replicate_index distribution:")
    for r in rep:
        print(f"  replicate_index={r['replicate_index']}: {r['n']}")

    ck = conn.execute("SELECT COUNT(*) FROM cache_keys").fetchone()[0]
    cr = conn.execute("SELECT COUNT(*) FROM cached_results").fetchone()[0]
    it = conn.execute("SELECT COUNT(*) FROM input_texts").fetchone()[0]
    print(f"Row counts: cache_keys={ck}, cached_results={cr}, input_texts={it}")
    if ck != cr:
        print("  NOTE: cache_keys != cached_results → multiple replicates or orphan rows; investigate.")


def main() -> int:
    parser = argparse.ArgumentParser(description="QC report for results.db")
    parser.add_argument(
        "--db",
        type=Path,
        default=ROOT / "manuscript_paper_cache" / "results.db",
        help="Path to results.db (read-only)",
    )
    args = parser.parse_args()

    if not args.db.exists():
        print(f"ERROR: Database not found: {args.db}", file=sys.stderr)
        return 1

    print("cache_qc_report.py — read-only SQL aggregates")
    print(f"Database: {args.db.resolve()}")
    print("Expected runtime: typically seconds to ~1–2 minutes on ~200k–300k rows (no JSON parsing).")

    conn = connect(args.db)
    try:
        q1_prompt_hashes(conn)
        q2_input_hashes(conn)
        q3_api_params(conn)
        q4_created_histogram(conn)
        q5_extra(conn)
    finally:
        conn.close()

    section("Done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
