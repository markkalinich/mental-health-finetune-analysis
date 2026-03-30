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


def q0_totals(conn: sqlite3.Connection) -> None:
    section("0) Row accounting (nothing is “extra” beyond this total)")
    ck = conn.execute("SELECT COUNT(*) FROM cache_keys").fetchone()[0]
    cr = conn.execute("SELECT COUNT(*) FROM cached_results").fetchone()[0]
    print(f"  cache_keys:     {ck}")
    print(f"  cached_results: {cr}")
    print(
        "  Every cache_keys row is one (model × effective prompt × input × API defaults) cell; "
        "cached_results should match unless replicates split rows."
    )

    parts = conn.execute(
        """
        SELECT prompt_name, COUNT(*) AS n
        FROM cache_keys
        GROUP BY prompt_name
        ORDER BY prompt_name
        """
    ).fetchall()
    s = sum(r["n"] for r in parts)
    print("  Rows per prompt_name (these partition the total; they are NOT additive “on top of” 209,550):")
    for r in parts:
        print(f"    {r['prompt_name']}: {r['n']}")
    print(f"  Sum of parts: {s}  (should equal cache_keys={ck})")
    if s != ck:
        print("  *** WARNING: sum != cache_keys ***")


def q1_prompt_hashes(conn: sqlite3.Connection) -> None:
    section("1) Prompt hashes — expect ≤6 from (3 tasks × 2: base vs Qwen /no_think)")
    print(
        "  Design intent: for each task, at most TWO effective prompt texts — the base file, and the\n"
        "  same file plus model suffix for Qwen-family models (e.g. /no_think). That yields up to\n"
        "  3 tasks × 2 = 6 distinct prompt_hash values globally (if every task has both cohorts).\n"
    )
    print(
        "  **Undesired pattern:** MORE than two distinct prompt_hash values **for the same\n"
        "  prompt_name** usually means the **on-disk prompt file was edited** between runs\n"
        "  (old hash + new hash). That is separate from the Qwen suffix split.\n"
    )

    rows = conn.execute(
        """
        SELECT prompt_name, prompt_hash, COUNT(*) AS n_keys
        FROM cache_keys
        GROUP BY prompt_name, prompt_hash
        ORDER BY prompt_name, prompt_hash
        """
    ).fetchall()
    distinct_hashes = {r["prompt_hash"] for r in rows}
    print(f"  Distinct prompt_hash values (global): {len(distinct_hashes)}")
    print("  Per (prompt_name, prompt_hash):")
    for r in rows:
        print(f"    {r['prompt_name']:45}  hash={r['prompt_hash']}  cache_keys={r['n_keys']}")

    by_name = conn.execute(
        """
        SELECT prompt_name, COUNT(DISTINCT prompt_hash) AS n_hashes, COUNT(*) AS n_keys
        FROM cache_keys
        GROUP BY prompt_name
        ORDER BY prompt_name
        """
    ).fetchall()
    print("  Distinct prompt_hash count per prompt_name:")
    for r in by_name:
        flag = ""
        if r["n_hashes"] > 2:
            flag = "  *** >2: likely prompt FILE revision, not only Qwen suffix ***"
        elif r["n_hashes"] == 2:
            flag = "  (often = base + Qwen suffix for this task)"
        print(f"    {r['prompt_name']}: {r['n_hashes']} hash(es), {r['n_keys']} cache_keys{flag}")

    n_names = conn.execute("SELECT COUNT(DISTINCT prompt_name) FROM cache_keys").fetchone()[0]
    print(f"  Distinct prompt_name strings: {n_names} (expect 3 for SI/TR/TE only; >3 ⇒ legacy names).")


def q2_input_hashes(conn: sqlite3.Connection) -> None:
    section("2) Input hashes — per task and one global deduplication fact")
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
    print()
    print(
        f"  **Global DISTINCT input_hash = {global_distinct}** — meaning: if you listed every\n"
        "  distinct input *string* (by MD5) that appears **anywhere** in this database, you get\n"
        "  this many unique texts. It is NOT 450+780+420 = 1650 because that sum **double-counts**\n"
        "  any line that is **byte-identical** in two different task CSVs: it has one hash but\n"
        "  appears in two tasks, so the global unique count drops by one per such collision.\n"
    )
    print(
        f"  Here: 450 + 780 + 420 = 1650; 1650 − {global_distinct} = {1650 - global_distinct} "
        "shared hash(es) across tasks (usually duplicate line text in two files).\n"
    )
    print(
        "  Per task, distinct input_hash should match dataset row count (450 / 780 / 420) for the\n"
        "  main TE/TR/SI runs; a smaller count under a legacy prompt_name means a partial grid.\n"
    )


def q3_api_params(conn: sqlite3.Connection) -> None:
    section("3) temperature, max_tokens, top_p")
    rows = conn.execute(
        """
        SELECT temperature, max_tokens, top_p, COUNT(*) AS n
        FROM cache_keys
        GROUP BY temperature, max_tokens, top_p
        ORDER BY n DESC
        """
    ).fetchall()
    print(f"  Distinct combinations: {len(rows)}")
    for r in rows:
        print(
            f"    temp={r['temperature']}  max_tokens={r['max_tokens']}  top_p={r['top_p']}  rows={r['n']}"
        )
    if len(rows) != 1:
        print("  WARNING: More than one API-parameter combination.")


def q4_created_histogram(conn: sqlite3.Connection) -> None:
    section("4) created_at (when keys were inserted)")
    rows = conn.execute(
        """
        SELECT substr(created_at, 1, 10) AS day, COUNT(*) AS n
        FROM cache_keys
        GROUP BY day
        ORDER BY day
        """
    ).fetchall()
    if not rows:
        print("  No created_at data.")
        return
    print("  Counts by calendar day (cache_keys):")
    max_n = max(r["n"] for r in rows) if rows else 1
    bar_width = 40
    for r in rows:
        day = r["day"] or "?"
        n = r["n"]
        bar_len = int(bar_width * n / max_n) if max_n else 0
        bar = "#" * bar_len
        print(f"    {day}  {n:7}  {bar}")

    mm = conn.execute(
        "SELECT MIN(created_at), MAX(created_at) FROM cache_keys"
    ).fetchone()
    print(f"  MIN: {mm[0]}")
    print(f"  MAX: {mm[1]}")
    print()
    print(
        "  **Note:** Sparse late days (e.g. a handful of rows on a new date) often correspond to\n"
        "  **re-runs / fill-ins** after bulk collection. Heavy **api_error:Request timeout** in\n"
        "  the status section is consistent with **LM Studio overload** when many parallel calls\n"
        "  hit the server — retries may land on a later calendar day.\n"
    )


def q5_status_and_errors(conn: sqlite3.Connection) -> None:
    section("5) Row alignment, replicate index, status & API errors")

    ck = conn.execute("SELECT COUNT(*) FROM cache_keys").fetchone()[0]
    cr = conn.execute("SELECT COUNT(*) FROM cached_results").fetchone()[0]
    it = conn.execute("SELECT COUNT(*) FROM input_texts").fetchone()[0]
    print("  **Core row counts**")
    print(f"    cache_keys:      {ck}")
    print(f"    cached_results:  {cr}")
    print(f"    input_texts:     {it}  (one row per distinct input_hash text)")
    if ck == cr:
        print("    → cache_keys == cached_results: one stored result per cache_id (replicate_index 0 only).")
    else:
        print("    → mismatch: check replicates or orphans.")

    rep = conn.execute(
        """
        SELECT replicate_index, COUNT(*) AS n
        FROM cached_results
        GROUP BY replicate_index
        ORDER BY replicate_index
        """
    ).fetchall()
    print("  **replicate_index**")
    for r in rep:
        print(f"    replicate_index={r['replicate_index']}: {r['n']}")

    n_ok = conn.execute(
        "SELECT COUNT(*) FROM cached_results WHERE status = 'ok'"
    ).fetchone()[0]
    n_pf = conn.execute(
        "SELECT COUNT(*) FROM cached_results WHERE status = 'parse_fail'"
    ).fetchone()[0]
    n_api = conn.execute(
        "SELECT COUNT(*) FROM cached_results WHERE status LIKE 'api_error%'"
    ).fetchone()[0]
    n_other = cr - n_ok - n_pf - n_api

    print("  **Status (collapsed)**")
    print(f"    ok:          {n_ok}")
    print(f"    parse_fail:  {n_pf}")
    print(f"    api_error:   {n_api}")
    if n_other:
        print(f"    other:       {n_other}")

    pct_api = (100.0 * n_api / cr) if cr else 0.0
    print()
    print("  *** API errors (highlight) ***")
    print(
        f"    Total api_error rows: {n_api}  ({pct_api:.2f}% of all cached_results)\n"
        "    These are failed API calls (timeouts, 400s, etc.); metrics pipelines treat them\n"
        "    differently from parse_fail — review downstream handling for manuscript claims.\n"
    )

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
    rest_api = n_api - n_to - n_400
    print("    Approximate split (string match on status):")
    print(f"      contains 'timeout':  {n_to}")
    print(f"      contains '400':      {n_400}")
    print(f"      other api_error:     {rest_api}")

    rows = conn.execute(
        """
        SELECT status, COUNT(*) AS n
        FROM cached_results
        WHERE status LIKE 'api_error%'
        GROUP BY status
        ORDER BY n DESC
        LIMIT 12
        """
    ).fetchall()
    if rows:
        print("    Top distinct api_error strings:")
        for r in rows:
            msg = (r["status"] or "")[:75]
            print(f"      n={r['n']:5}  {msg}")


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
    print("Expected runtime: typically seconds (~1–2 min worst case); no per-row JSON parsing.")

    conn = connect(args.db)
    try:
        q0_totals(conn)
        q1_prompt_hashes(conn)
        q2_input_hashes(conn)
        q3_api_params(conn)
        q4_created_histogram(conn)
        q5_status_and_errors(conn)
    finally:
        conn.close()

    section("Done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
