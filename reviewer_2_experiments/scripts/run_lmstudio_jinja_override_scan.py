#!/usr/bin/env python3
"""Scan LM Studio per-model override JSON for all enabled models (127).

Reads ~/.lmstudio/.internal/user-concrete-model-default-config and flags
llm.prediction.promptTemplate entries with type=jinja.

Default output: reviewer_2_experiments/data/provenance/all_models_lmstudio_jinja_overrides.json
Use --output to write elsewhere (safe regeneration).
Use --compare-to for read-only verification against a committed snapshot.

Exits non-zero if any enabled model lacks an LM Studio index entry (fail loud).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from lmstudio_override_utils import INDEX_CACHE_PATH, build_override_scan, index_entry_failures
from r2_paths import PROVENANCE, ROOT

DEFAULT_OUT = PROVENANCE / "all_models_lmstudio_jinja_overrides.json"

REQUIRED_COMMITTED_FIELDS = ("gguf_rel_path", "override_file", "lmstudio_jinja_override")


def committed_row_complete(old: dict) -> bool:
    if old.get("note") == "no_index_entry":
        return False
    for key in REQUIRED_COMMITTED_FIELDS:
        if key not in old or old.get(key) is None:
            return False
    return True


def compare_scans(live: dict, committed: dict) -> list[str]:
    errors: list[str] = []

    if live["enabled_model_count"] != committed.get("enabled_model_count"):
        errors.append(
            f"enabled_model_count live={live['enabled_model_count']} "
            f"committed={committed.get('enabled_model_count')}"
        )

    live_ids = live["models_with_jinja_override"]
    committed_ids = committed.get("models_with_jinja_override", [])
    if sorted(live_ids) != sorted(committed_ids):
        errors.append(f"override id list differs: live={live_ids} committed={committed_ids}")

    live_by_id = {m["lm_studio_id"]: m for m in live["models"]}
    committed_by_id = {m["lm_studio_id"]: m for m in committed.get("models", [])}

    for lid in sorted(set(live_by_id) | set(committed_by_id)):
        live_row = live_by_id.get(lid)
        old = committed_by_id.get(lid)

        if live_row is None:
            errors.append(f"{lid}: in committed JSON but missing from live scan")
            continue
        if old is None:
            errors.append(f"{lid}: in live scan but missing from committed JSON")
            continue
        if live_row.get("status") == "SKIP_no_index_entry":
            errors.append(f"{lid}: live scan has no LM Studio index entry")
            continue
        if not committed_row_complete(old):
            errors.append(
                f"{lid}: committed row incomplete "
                f"(note={old.get('note')!r}, missing required fields "
                f"{[k for k in REQUIRED_COMMITTED_FIELDS if k not in old or old.get(k) is None]})"
            )
            continue

        if live_row.get("lmstudio_jinja_override") != old.get("lmstudio_jinja_override"):
            errors.append(
                f"{lid}: override flag live={live_row.get('lmstudio_jinja_override')} "
                f"committed={old.get('lmstudio_jinja_override')}"
            )
        if live_row.get("gguf_rel_path") != old.get("gguf_rel_path"):
            errors.append(
                f"{lid}: gguf_rel_path live={live_row.get('gguf_rel_path')} "
                f"committed={old.get('gguf_rel_path')}"
            )
        if live_row.get("override_file") != old.get("override_file"):
            errors.append(
                f"{lid}: override_file live={live_row.get('override_file')} "
                f"committed={old.get('override_file')}"
            )
        if live_row.get("lmstudio_jinja_override"):
            live_sha = live_row.get("jinja_override_sha256")
            old_sha = old.get("jinja_override_sha256")
            if live_sha != old_sha:
                errors.append(f"{lid}: jinja_override_sha256 mismatch")
            elif live_row.get("jinja_override_template") != old.get("jinja_override_template"):
                errors.append(f"{lid}: jinja_override_template text mismatch")

    return errors


def fail_on_index_gaps(scan: dict) -> list[str]:
    failures = index_entry_failures(scan["models"])
    if failures:
        print("ERROR: enabled model(s) missing LM Studio index entry:", file=sys.stderr)
        for lid in failures:
            print(f"  {lid}", file=sys.stderr)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="LM Studio Jinja override scan (127 models)")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUT,
        help=f"Write scan JSON here (default: {DEFAULT_OUT.relative_to(ROOT.parent)})",
    )
    parser.add_argument(
        "--compare-to",
        type=Path,
        help="Read-only: compare live scan to this committed JSON (does not write --output)",
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="Write verification report JSON (used with --compare-to)",
    )
    parser.add_argument(
        "--index-cache",
        type=Path,
        default=INDEX_CACHE_PATH,
        help="LM Studio model-index-cache.json",
    )
    parser.add_argument(
        "--models-csv",
        type=Path,
        default=ROOT / "config/models_config.csv",
    )
    args = parser.parse_args()

    live = build_override_scan(args.models_csv, index_cache=args.index_cache)
    live["generated_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    index_failures = fail_on_index_gaps(live)
    if index_failures and not args.compare_to:
        return 1

    if args.compare_to:
        if not args.compare_to.exists():
            print(f"ERROR: compare target missing: {args.compare_to}", file=sys.stderr)
            return 1
        committed = json.loads(args.compare_to.read_text())
        errors = compare_scans(live, committed)
        if index_failures:
            for lid in index_failures:
                errors.append(f"{lid}: live scan has no LM Studio index entry")
        report = {
            "generated_at": live["generated_at"],
            "compare_to": str(args.compare_to),
            "live_override_count": live["models_with_jinja_override_count"],
            "committed_override_count": committed.get("models_with_jinja_override_count"),
            "live_override_ids": live["models_with_jinja_override"],
            "committed_override_ids": committed.get("models_with_jinja_override"),
            "index_entry_failures": index_failures,
            "errors": errors,
            "ok": len(errors) == 0 and len(index_failures) == 0,
        }
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, indent=2))
        print(f"Override scan verify: {'PASS' if report['ok'] else 'FAIL'}")
        print(f"  live overrides: {live['models_with_jinja_override_count']} {live['models_with_jinja_override']}")
        if errors:
            for e in errors:
                print(f"  ERROR: {e}", file=sys.stderr)
        return 0 if report["ok"] else 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(live, indent=2))
    print(f"Wrote {args.output}")
    print(
        f"  enabled={live['enabled_model_count']} "
        f"overrides={live['models_with_jinja_override_count']} "
        f"ids={live['models_with_jinja_override']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
