#!/usr/bin/env python3
"""Compare embedded chat_template for Q8-orphan models vs smaller HF quant.

For models whose local Q8_0 GGUF cannot be HEAD-verified on HuggingFace (404),
fetch only the GGUF metadata/header region (~8 MB) from an available quant in the
same repo and compare tokenizer.chat_template SHA256 to the local Q8 file.

Default output:
  reviewer_2_experiments/data/provenance/hf_template_compare/q8_vs_smaller_quant_template_compare.json

Use --output for safe regeneration; --compare-to for read-only verification.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from gguf_template_utils import extract_chat_template, extract_hf_chat_template, template_sha256
from r2_paths import PROVENANCE, ROOT

DEFAULT_OUT = PROVENANCE / "hf_template_compare/q8_vs_smaller_quant_template_compare.json"
AUDIT_PATH = PROVENANCE / "all_models_gguf_sha256_audit.json"
MODELS_ROOT = Path.home() / ".lmstudio/models"

# Explicit mapping recovered from committed artifact + EXPERIMENT_LOG §4.
CASES = [
    {
        "lm_studio_id": "gemma-2-27b",
        "local_quant_file": "gemma-2-27b-Q8_0.gguf",
        "hf_quant_file_compared": "gemma-2-27b-Q3_K_M.gguf",
    },
    {
        "lm_studio_id": "klyang_mentallama-chat-13b",
        "local_quant_file": "MentaLLaMA-chat-13B-Q8_0.gguf",
        "hf_quant_file_compared": "MentaLLaMA-chat-13B-Q2_K.gguf",
    },
    {
        "lm_studio_id": "llama-3.1-8b-instruct-mental-health-classification",
        "local_quant_file": "Llama-3.1-8B-Instruct-Mental-Health-Classification-Q8_0.gguf",
        "hf_quant_file_compared": "Llama-3.1-8B-Instruct-Mental-Health-Classification-Q2_K.gguf",
    },
]


def load_audit_index() -> Dict[str, dict]:
    audit = json.loads(AUDIT_PATH.read_text())
    return {m["lm_studio_id"]: m for m in audit["models"]}


def compare_row(case: dict, audit_by_id: Dict[str, dict]) -> dict[str, Any]:
    lid = case["lm_studio_id"]
    audit = audit_by_id.get(lid)
    if not audit:
        raise KeyError(f"{lid}: missing from {AUDIT_PATH}")

    rel = audit.get("rel_path")
    if not rel:
        raise KeyError(f"{lid}: no rel_path in audit JSON")

    local_path = MODELS_ROOT / rel
    if not local_path.exists():
        raise FileNotFoundError(f"{lid}: local GGUF missing: {local_path}")

    repo = audit.get("huggingface_repo")
    if not repo:
        parts = Path(rel).parts
        repo = f"{parts[0]}/{parts[1]}"

    local_present, local_tmpl = extract_chat_template(local_path)
    hf_present, hf_tmpl = extract_hf_chat_template(repo, case["hf_quant_file_compared"])

    row: dict[str, Any] = {
        "lm_studio_id": lid,
        "local_quant_file": case["local_quant_file"],
        "hf_quant_file_compared": case["hf_quant_file_compared"],
        "huggingface_repo": repo,
        "local_gguf_path": str(local_path),
        "local_embedded_chat_template_present": local_present,
        "hf_embedded_chat_template_present": hf_present,
    }

    if local_present and hf_present:
        local_sha = template_sha256(local_tmpl)
        hf_sha = template_sha256(hf_tmpl)
        row["local_template_sha256"] = local_sha
        row["hf_template_sha256"] = hf_sha
        row["embedded_chat_template_match"] = local_sha == hf_sha
        if local_sha != hf_sha:
            row["note"] = "Template strings differ between local Q8 and HF smaller quant."
    elif not local_present and not hf_present:
        row["embedded_chat_template_match"] = True
        row["note"] = (
            "Neither local Q8 nor HF smaller quant has tokenizer.chat_template in GGUF metadata."
        )
    else:
        row["embedded_chat_template_match"] = False
        row["note"] = (
            f"Presence mismatch: local={local_present} hf={hf_present}"
        )

    return row


def build_compare(audit_by_id: Optional[Dict[str, dict]] = None) -> List[dict]:
    audit_by_id = audit_by_id or load_audit_index()
    return [compare_row(case, audit_by_id) for case in CASES]


def compare_to_committed(live: List[dict], committed: List[dict]) -> list[str]:
    errors: list[str] = []
    committed_by_id = {r["lm_studio_id"]: r for r in committed}

    for row in live:
        lid = row["lm_studio_id"]
        old = committed_by_id.get(lid)
        if not old:
            errors.append(f"{lid}: missing from committed JSON")
            continue
        for key in (
            "local_embedded_chat_template_present",
            "hf_embedded_chat_template_present",
            "embedded_chat_template_match",
        ):
            if row.get(key) != old.get(key):
                errors.append(f"{lid}: {key} live={row.get(key)} committed={old.get(key)}")
        for key in ("local_template_sha256", "hf_template_sha256"):
            if key in old and row.get(key) != old.get(key):
                errors.append(f"{lid}: {key} mismatch")

    if len(live) != len(committed):
        errors.append(f"row count live={len(live)} committed={len(committed)}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Q8-orphan HF template compare (3 models)")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUT,
        help="Write compare JSON here",
    )
    parser.add_argument(
        "--compare-to",
        type=Path,
        help="Read-only verify against committed JSON (requires network for HF Range fetch)",
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="Write verification report JSON (with --compare-to)",
    )
    parser.add_argument(
        "--audit",
        type=Path,
        default=AUDIT_PATH,
        help="GGUF audit JSON for rel_path / huggingface_repo",
    )
    args = parser.parse_args()

    audit_by_id = {m["lm_studio_id"]: m for m in json.loads(args.audit.read_text())["models"]}
    live = build_compare(audit_by_id)

    if args.compare_to:
        if not args.compare_to.exists():
            print(f"ERROR: compare target missing: {args.compare_to}", file=sys.stderr)
            return 1
        committed = json.loads(args.compare_to.read_text())
        errors = compare_to_committed(live, committed)
        report = {
            "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "compare_to": str(args.compare_to),
            "rows": live,
            "errors": errors,
            "ok": len(errors) == 0,
        }
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, indent=2))
        print(f"Template compare verify: {'PASS' if report['ok'] else 'FAIL'}")
        for row in live:
            print(
                f"  {row['lm_studio_id']}: match={row['embedded_chat_template_match']} "
                f"local_present={row['local_embedded_chat_template_present']} "
                f"hf_present={row['hf_embedded_chat_template_present']}"
            )
        if errors:
            for e in errors:
                print(f"  ERROR: {e}", file=sys.stderr)
        return 0 if report["ok"] else 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(live, indent=2))
    print(f"Wrote {args.output} ({len(live)} models)")
    for row in live:
        print(f"  {row['lm_studio_id']}: match={row['embedded_chat_template_match']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
