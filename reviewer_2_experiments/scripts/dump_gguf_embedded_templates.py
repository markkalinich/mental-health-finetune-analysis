#!/usr/bin/env python3
"""Dump the embedded jinja chat template (tokenizer.chat_template) from every enabled model's GGUF.

For each model this records the VERBATIM template only (NOT the system prompt,
NOT a rendered prompt):
  - template_base64:     base64 of the RAW template bytes (bitwise-faithful source of truth)
  - template_utf8:       decoded text (errors='replace'), for human reading only
  - template_sha256_raw: sha256 of the RAW bytes
  - has_template / status: ok | no_template | error

When a GGUF has no tokenizer.chat_template key the content is recorded as empty
(b"") with status="no_template", so template_sha256_raw is the sha256 of empty
input and the invariant sha256==sha256(b64decode(base64)) holds for every row.
status/has_template record the absence. NOTHING is invented or substituted.
Read/parse failures use status="error" with null content + null hash.

Crash-safe: writes atomically (temp file + os.replace) after EACH model, so an
interruption never loses completed work. Use --resume to skip models already
captured with status in {ok, no_template}.

Output: reviewer_2_experiments/data/provenance/all_models_gguf_embedded_templates.json
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Tuple

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from gguf_template_utils import PARTIAL_BYTE_SIZES, _kv_fields_only
from r2_paths import PROVENANCE

AUDIT = PROVENANCE / "all_models_gguf_sha256_audit.json"
OUT = PROVENANCE / "all_models_gguf_embedded_templates.json"


def raw_template_bytes(path: Path) -> Tuple[bool, bytes]:
    """Return (found, raw_bytes) for tokenizer.chat_template, trying growing header windows.

    (False, b"") means the GGUF parsed but has no chat_template key.
    Raises RuntimeError only if the metadata could not be parsed at any window size.
    """
    last_err = None
    for size in PARTIAL_BYTE_SIZES:
        try:
            fields = _kv_fields_only(path, max_bytes=size)
            field = fields.get("tokenizer.chat_template")
            if field is None:
                return False, b""
            val = field.parts[field.data[0]]
            if hasattr(val, "tobytes"):
                return True, val.tobytes()
            if isinstance(val, bytes):
                return True, val
            return True, str(val).encode("utf-8")
        except Exception as exc:  # noqa: BLE001 - retry at a larger window
            last_err = exc
    raise RuntimeError(f"GGUF metadata parse failed for {path}: {last_err}")


def atomic_write_json(path: Path, obj: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2))
    os.replace(tmp, path)


def now_z() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def build_report(records: dict, total: int) -> dict:
    rows = list(records.values())
    status_counts: dict = {}
    for r in rows:
        status_counts[r["status"]] = status_counts.get(r["status"], 0) + 1
    return {
        "generated_at": now_z(),
        "source": "tokenizer.chat_template extracted directly from each model's GGUF",
        "gguf_paths_from": "all_models_gguf_sha256_audit.json",
        "content_note": (
            "Verbatim embedded jinja chat template only. template_base64 is the "
            "bitwise source of truth; template_utf8 is decoded for reading. "
            "Invariant for ok/no_template rows: template_sha256_raw == "
            "sha256(base64_decode(template_base64)). no_template = GGUF has no "
            "tokenizer.chat_template; content is empty (b''), so its hash is the "
            "sha256 of empty input. status/has_template records absence; nothing invented. "
            "error rows (parse/read failure) keep null content + null hash (content unknown)."
        ),
        "models_total": total,
        "models_captured": len(rows),
        "status_summary": status_counts,
        "models": [records[k] for k in sorted(records)],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--resume", action="store_true", help="Skip models already captured (ok/no_template)")
    ap.add_argument("--only", nargs="+", help="Only these lm_studio_id values")
    ap.add_argument("--limit", type=int, help="Only the first N models (in audit order)")
    args = ap.parse_args()

    audit = json.loads(AUDIT.read_text())["models"]
    if args.only:
        keep = set(args.only)
        audit = [m for m in audit if m["lm_studio_id"] in keep]
    if args.limit is not None:
        audit = audit[: args.limit]

    records: dict = {}
    if OUT.exists():
        for r in json.loads(OUT.read_text()).get("models", []):
            records[r["lm_studio_id"]] = r

    total = len(json.loads(AUDIT.read_text())["models"])
    skip_ok = {"ok", "no_template"}

    for i, m in enumerate(audit, 1):
        lid = m["lm_studio_id"]
        if args.resume and lid in records and records[lid].get("status") in skip_ok:
            print(f"[{i}/{len(audit)}] SKIP {lid} ({records[lid]['status']})", flush=True)
            continue

        gguf_path = m.get("gguf_path", "")
        rec = {
            "lm_studio_id": lid,
            "publisher": m.get("publisher_csv"),
            "huggingface_repo": m.get("huggingface_repo"),
            "gguf_path": gguf_path,
            "captured_at": now_z(),
        }
        t0 = time.time()
        try:
            if not gguf_path or not os.path.exists(gguf_path):
                raise FileNotFoundError(f"gguf_path missing on disk: {gguf_path!r}")
            rec["gguf_file_size_bytes"] = os.path.getsize(gguf_path)
            found, raw = raw_template_bytes(Path(gguf_path))
            if not found:
                rec.update(
                    {
                        "has_template": False,
                        "status": "no_template",
                        "template_base64": "",
                        "template_utf8": "",
                        "template_sha256_raw": hashlib.sha256(b"").hexdigest(),
                        "error": None,
                    }
                )
            else:
                rec.update(
                    {
                        "has_template": True,
                        "status": "ok",
                        "template_base64": base64.b64encode(raw).decode("ascii"),
                        "template_utf8": raw.decode("utf-8", errors="replace"),
                        "template_sha256_raw": hashlib.sha256(raw).hexdigest(),
                        "error": None,
                    }
                )
        except Exception as exc:  # noqa: BLE001 - record, never silently drop
            rec.update(
                {
                    "has_template": None,
                    "status": "error",
                    "template_base64": None,
                    "template_utf8": None,
                    "template_sha256_raw": None,
                    "error": str(exc)[:2000],
                }
            )
        rec["extract_seconds"] = round(time.time() - t0, 3)
        records[lid] = rec
        atomic_write_json(OUT, build_report(records, total))
        print(
            f"[{i}/{len(audit)}] {lid} -> {rec['status']} "
            f"sha={(rec.get('template_sha256_raw') or '')[:12]} "
            f"({rec['extract_seconds']}s)",
            flush=True,
        )

    atomic_write_json(OUT, build_report(records, total))
    rep = build_report(records, total)
    print(f"\nWrote {OUT}", flush=True)
    print(json.dumps(rep["status_summary"], indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
