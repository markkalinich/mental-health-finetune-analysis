#!/usr/bin/env python3
"""
Build a SQLite subset of cache/results.db containing only rows needed for the
paper experiment grid: all enabled models in config/models_config.csv × three
tasks (SI, TR, TE) × each input row × default API params.

Uses the same cache-key rules as cache/result_cache.py (including
load_system_prompt model-specific suffixes).

Outputs:
  - New database file (default: manuscript_paper_cache/results.db)
  - JSON report: expected vs found cache_ids, missing keys, SHA-256 of output

Verification limits (read the report footer):
  - Proves internal consistency between enumeration and the source DB.
  - Does NOT by itself prove identity with "original submission" unless you
    compare against a frozen DB from submission time OR recompute metrics and
    match the pinned all_models_all_tasks.csv (see docs/PROVENANCE_PLAN.md).
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

# Project root on sys.path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from config import load_system_prompt  # noqa: E402
from config.models_registry import ModelsRegistry  # noqa: E402
from orchestration.data_processor import DataProcessor  # noqa: E402
from orchestration.experiment_manager import ExperimentManager  # noqa: E402
from cache.result_cache import ResultCache  # noqa: E402

TASKS: Dict[str, Dict[str, str]] = {
    "suicidal_ideation": {
        "input_data": "data/inputs/finalized_input_data/SI_finalized_sentences.csv",
        "prompt_file": "data/prompts/system_suicide_detection_v2.txt",
        "prompt_name": "system_suicide_detection_v2",
    },
    "therapy_request": {
        "input_data": "data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv",
        "prompt_file": "data/prompts/therapy_request_classifier_v3.txt",
        "prompt_name": "therapy_request_classifier_v3",
    },
    "therapy_engagement": {
        "input_data": "data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv",
        "prompt_file": "data/prompts/therapy_engagement_conversation_prompt_v2.txt",
        "prompt_name": "therapy_engagement_conversation_prompt_v2",
    },
}


def _create_db_schema(conn: sqlite3.Connection) -> None:
    """Same DDL as cache/result_cache.py _init_database."""
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS cache_keys (
            cache_id TEXT PRIMARY KEY,
            model_family TEXT NOT NULL,
            model_size TEXT NOT NULL,
            model_version TEXT NOT NULL,
            model_full_name TEXT NOT NULL,
            prompt_name TEXT NOT NULL,
            prompt_version TEXT NOT NULL,
            prompt_hash TEXT NOT NULL,
            input_hash TEXT NOT NULL,
            temperature REAL NOT NULL,
            max_tokens INTEGER NOT NULL,
            top_p REAL NOT NULL,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS input_texts (
            input_hash TEXT PRIMARY KEY,
            input_text TEXT NOT NULL,
            first_seen TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS cached_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cache_id TEXT NOT NULL,
            raw_response TEXT NOT NULL,
            parsed_result TEXT,
            status TEXT NOT NULL,
            processing_time REAL NOT NULL,
            created_at TEXT NOT NULL,
            replicate_index INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (cache_id) REFERENCES cache_keys (cache_id)
        );
        CREATE INDEX IF NOT EXISTS idx_cache_id ON cached_results (cache_id);
        CREATE INDEX IF NOT EXISTS idx_input_hash ON cache_keys (input_hash);
        CREATE INDEX IF NOT EXISTS idx_model_prompt ON cache_keys (model_family, model_size, prompt_name);
        """
    )


def enumerate_expected_cache_ids(
    registry: ModelsRegistry,
    manager: ExperimentManager,
    processor: DataProcessor,
    quiet: bool = False,
) -> Tuple[Set[str], Dict[str, Any]]:
    """Return set of cache_id hex strings and summary counts."""
    expected_list: List[str] = []
    per_task_counts: Dict[str, int] = {}
    models = registry.get_enabled_models()
    # Isolated temp cache dir so we never touch the real results.db while computing keys
    _stdout = io.StringIO() if quiet else None
    with tempfile.TemporaryDirectory() as tmp:
        rc_logic = ResultCache(tmp)
        for task_key, tcfg in TASKS.items():
            input_path = ROOT / tcfg["input_data"]
            prompt_path = ROOT / tcfg["prompt_file"]
            df = processor.load_input_data(str(input_path))
            n_rows = len(df)
            per_task_counts[task_key] = n_rows

            for spec in models:
                config = manager.create_experiment_config(
                    experiment_name=f"enum_{spec.family}_{spec.size}_{tcfg['prompt_name']}",
                    model_family=spec.family,
                    model_size=spec.size,
                    model_version=str(spec.version),
                    prompt_name=tcfg["prompt_name"],
                    prompt_file=str(prompt_path),
                    input_dataset=str(input_path),
                )
                cm = contextlib.redirect_stdout(_stdout) if quiet else contextlib.nullcontext()
                with cm:
                    prompt_content = load_system_prompt(str(prompt_path), config.model)
                for _, row in df.iterrows():
                    text = str(row["text"])
                    ck = rc_logic._create_cache_key(config, text, prompt_content)
                    expected_list.append(ck.get_cache_id())

    return set(expected_list), {
        "enabled_models": len(models),
        "rows_per_task": per_task_counts,
        "expected_unique_cache_ids": len(set(expected_list)),
        "expected_total_enumerations": len(expected_list),
    }


def fetch_existing_cache_ids(
    src_db: Path, expected: Set[str]
) -> Tuple[Set[str], Set[str]]:
    """Return (found, missing) among expected ids."""
    conn = sqlite3.connect(str(src_db))
    cur = conn.cursor()
    found: Set[str] = set()
    missing: Set[str] = set()
    # Batch query to avoid huge IN clauses
    exp_list = list(expected)
    chunk = 500
    for i in range(0, len(exp_list), chunk):
        part = exp_list[i : i + chunk]
        q = "SELECT cache_id FROM cache_keys WHERE cache_id IN (%s)" % (
            ",".join("?" * len(part))
        )
        for (cid,) in cur.execute(q, part):
            found.add(cid)
    missing = set(expected) - found
    conn.close()
    return found, missing


def copy_rows_for_ids(src_db: Path, dst_db: Path, cache_ids: Set[str]) -> Dict[str, int]:
    """Copy cache_keys, input_texts, cached_results for given cache_ids."""
    if dst_db.exists():
        dst_db.unlink()
    dst_db.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(dst_db))
    _create_db_schema(conn)

    src = sqlite3.connect(str(src_db))
    src.row_factory = sqlite3.Row

    ids_list = list(cache_ids)
    counts = {"cache_keys": 0, "input_texts": 0, "cached_results": 0}

    chunk = 300
    input_hashes_needed: Set[str] = set()

    for i in range(0, len(ids_list), chunk):
        part = ids_list[i : i + chunk]
        ph = ",".join("?" * len(part))
        rows = src.execute(f"SELECT * FROM cache_keys WHERE cache_id IN ({ph})", part).fetchall()
        for r in rows:
            input_hashes_needed.add(r["input_hash"])
            conn.execute(
                """
                INSERT OR REPLACE INTO cache_keys (
                    cache_id, model_family, model_size, model_version, model_full_name,
                    prompt_name, prompt_version, prompt_hash, input_hash,
                    temperature, max_tokens, top_p, created_at
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                tuple(r[k] for k in r.keys()),
            )
            counts["cache_keys"] += 1

    for ih in input_hashes_needed:
        r = src.execute("SELECT * FROM input_texts WHERE input_hash = ?", (ih,)).fetchone()
        if r:
            conn.execute(
                "INSERT OR REPLACE INTO input_texts VALUES (?,?,?)",
                (r["input_hash"], r["input_text"], r["first_seen"]),
            )
            counts["input_texts"] += 1

    for i in range(0, len(ids_list), chunk):
        part = ids_list[i : i + chunk]
        ph = ",".join("?" * len(part))
        rows = src.execute(f"SELECT * FROM cached_results WHERE cache_id IN ({ph})", part).fetchall()
        for r in rows:
            conn.execute(
                """
                INSERT INTO cached_results (
                    cache_id, raw_response, parsed_result, status, processing_time,
                    created_at, replicate_index
                ) VALUES (?,?,?,?,?,?,?)
                """,
                (
                    r["cache_id"],
                    r["raw_response"],
                    r["parsed_result"],
                    r["status"],
                    r["processing_time"],
                    r["created_at"],
                    r["replicate_index"],
                ),
            )
            counts["cached_results"] += 1

    conn.commit()
    conn.execute("VACUUM")
    conn.close()
    src.close()
    return counts


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def git_info() -> Dict[str, Any]:
    try:
        commit = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=str(ROOT), stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
        dirty = bool(
            subprocess.check_output(
                ["git", "status", "--porcelain"], cwd=str(ROOT), stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
        return {"commit": commit, "dirty": dirty}
    except Exception as e:
        return {"commit": None, "dirty": None, "error": str(e)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Build manuscript-only cache subset SQLite")
    parser.add_argument(
        "--source",
        type=Path,
        default=ROOT / "cache" / "results.db",
        help="Source results.db (symlinks resolved by open())",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "manuscript_paper_cache" / "results.db",
        help="Output SQLite path",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=ROOT / "manuscript_paper_cache" / "subset_report.json",
        help="JSON report path",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only enumerate and compare; do not write output DB",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress prompt-suffix messages during enumeration",
    )
    args = parser.parse_args()

    if not args.source.exists():
        print(f"ERROR: Source database not found: {args.source}", file=sys.stderr)
        return 1

    registry = ModelsRegistry()
    manager = ExperimentManager(ROOT)
    processor = DataProcessor()

    expected_ids, enum_summary = enumerate_expected_cache_ids(
        registry, manager, processor, quiet=args.quiet
    )
    found_ids, missing_ids = fetch_existing_cache_ids(args.source, expected_ids)

    report: Dict[str, Any] = {
        "git": git_info(),
        "source_db": str(args.source.resolve()),
        "source_db_sha256": sha256_file(args.source),
        "enumeration": enum_summary,
        "expected_cache_ids": len(expected_ids),
        "found_in_source": len(found_ids),
        "missing_in_source": len(missing_ids),
        "missing_sample": sorted(missing_ids)[:50],
        "verification_notes": [
            "Found/missing refer to whether each expected cache_id exists in the SOURCE db.",
            "If missing_in_source > 0, the large cache is incomplete for current models_config + inputs.",
            "This script does NOT prove byte-identity with the original journal submission unless you "
            "also hold a contemporaneous DB snapshot or regenerate metrics and match pinned CSVs.",
        ],
    }

    if not args.dry_run and found_ids:
        counts = copy_rows_for_ids(args.source, args.output, found_ids)
        report["output_db"] = str(args.output.resolve())
        report["output_counts"] = counts
        report["output_db_sha256"] = sha256_file(args.output)

    args.report.parent.mkdir(parents=True, exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(json.dumps(report, indent=2))
    if missing_ids:
        print(
            f"\nWARNING: {len(missing_ids)} expected cache_ids missing from source.",
            file=sys.stderr,
        )
    return 0 if not missing_ids else 2


if __name__ == "__main__":
    sys.exit(main())
