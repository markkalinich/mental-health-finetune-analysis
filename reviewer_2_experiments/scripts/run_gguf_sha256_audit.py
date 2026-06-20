#!/usr/bin/env python3
"""SHA256 audit: local GGUF vs HuggingFace x-linked-etag for enabled models.

Writes reviewer_2_experiments/data/provenance/all_models_gguf_sha256_audit.json
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from lm_studio_load_crosswalk import LM_STUDIO_LOAD_CROSSWALK
from r2_paths import PROVENANCE, ROOT

ART = PROVENANCE
MODELS_CSV = ROOT / "config/models_config.csv"
CACHE_PATH = Path.home() / ".lmstudio/.internal/model-index-cache.json"
OUT_PATH = PROVENANCE / "all_models_gguf_sha256_audit.json"

# Split-shard layouts on HF (examples):
#   bartowski/.../Meta-Llama-3.1-70B-Instruct-Q8_0/Meta-Llama-3.1-70B-Instruct-Q8_0-00001-of-00002.gguf
#   RichardErkhov/.../Q4_K_M/Llama3-Med42-70B_Q4_K_M-00001-of-00002.gguf
SPLIT_SHARD_SUFFIX = re.compile(r"-\d+-of-\d+\.gguf$", re.IGNORECASE)
BARTOWSKI_STYLE_QUANT = re.compile(r"^(.+-Q\d+(?:_[A-Z0-9]+)?)-\d+-of-\d+\.gguf$", re.IGNORECASE)
RICHARDERKHOV_STYLE_QUANT = re.compile(
    r"_((?:Q|IQ)\d+(?:_[A-Z0-9]+)*)-\d+-of-\d+\.gguf$", re.IGNORECASE
)


def local_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            block = f.read(8 * 1024 * 1024)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def hf_head(repo: str, fname: str) -> Tuple[str, Optional[str], Optional[str]]:
    url = f"https://huggingface.co/{repo}/resolve/main/{fname}"
    proc = subprocess.run(
        ["curl", "-sI", url],
        capture_output=True,
        text=True,
        timeout=45,
    )
    headers: Dict[str, str] = {}
    status = proc.stdout.splitlines()[0] if proc.stdout else ""
    for line in proc.stdout.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip().lower()] = value.strip()
    etag = headers.get("x-linked-etag", "").strip('"') or None
    size = headers.get("x-linked-size") or headers.get("content-length")
    return status, etag, size


def derive_hf_repo(rel_path: str) -> str:
    parts = Path(rel_path).parts
    return f"{parts[0]}/{parts[1]}"


def hf_path_candidates(rel_path: str) -> List[Tuple[str, str]]:
    """Return (repo, filename) pairs to try, most specific first."""
    repo = derive_hf_repo(rel_path)
    fname = Path(rel_path).name
    seen: set[Tuple[str, str]] = set()
    ordered: List[Tuple[str, str]] = []

    def add(r: str, f: str) -> None:
        key = (r, f)
        if key not in seen:
            seen.add(key)
            ordered.append(key)

    add(repo, fname)

    if SPLIT_SHARD_SUFFIX.search(fname):
        m = BARTOWSKI_STYLE_QUANT.match(fname)
        if m:
            add(repo, f"{m.group(1)}/{fname}")
        m = RICHARDERKHOV_STYLE_QUANT.search(fname)
        if m:
            add(repo, f"{m.group(1)}/{fname}")

    return ordered


def resolve_index_entry(
    lm_studio_id: str, by_id: Dict[str, dict]
) -> Tuple[Optional[dict], Optional[str]]:
    """Return (index model dict, resolved_index_id)."""
    index_id = LM_STUDIO_LOAD_CROSSWALK.get(lm_studio_id, lm_studio_id)
    model = by_id.get(index_id)
    if model:
        return model, index_id
    return None, None


def audit_model(row: dict, by_id: Dict[str, dict]) -> dict:
    lid = row["lm_studio_id"]
    base: dict[str, Any] = {
        "lm_studio_id": lid,
        "family": row["family"],
        "size": row["size"],
        "publisher_csv": row.get("publisher", ""),
    }

    model, index_id = resolve_index_entry(lid, by_id)
    if not model or not (model.get("entryPoint") or {}).get("relPath"):
        note = "lm_studio_id not in model-index-cache or no entryPoint"
        if lid in LM_STUDIO_LOAD_CROSSWALK:
            note += f" (crosswalk target {LM_STUDIO_LOAD_CROSSWALK[lid]} also missing)"
        return {**base, "status": "SKIP_no_index_entry", "detail": note}

    if index_id != lid:
        base["index_id_resolved"] = index_id

    ep = model["entryPoint"]
    gguf_path = Path(ep["absPath"])
    rel_path = ep.get("relPath") or str(
        gguf_path.relative_to(Path.home() / ".lmstudio/models")
    )
    base.update({"gguf_path": str(gguf_path), "rel_path": rel_path})

    if not gguf_path.exists():
        return {**base, "status": "SKIP_local_missing", "detail": "GGUF not on disk"}

    if not str(rel_path).endswith(".gguf"):
        return {
            **base,
            "status": "SKIP_not_gguf",
            "detail": f"format={model.get('format')}",
        }

    local_bytes = gguf_path.stat().st_size
    base["local_bytes"] = local_bytes

    tried: List[dict] = []
    for repo, fname in hf_path_candidates(rel_path):
        status, etag, hsize = hf_head(repo, fname)
        tried.append(
            {
                "huggingface_repo": repo,
                "huggingface_filename": fname,
                "http_status": status.split()[1] if status else None,
                "x_linked_etag": etag,
                "x_linked_size": int(hsize) if hsize and str(hsize).isdigit() else hsize,
            }
        )
        if "404" in status:
            continue
        if not etag:
            continue

        print(f"  hashing {lid} ({local_bytes / 1e9:.2f} GB)...", flush=True)
        lsha = local_sha256(gguf_path)
        match = lsha == etag
        size_match = str(local_bytes) == str(hsize)
        result = {
            **base,
            "huggingface_repo": repo,
            "huggingface_filename": fname,
            "huggingface_x_linked_size": tried[-1]["x_linked_size"],
            "local_sha256": lsha,
            "huggingface_x_linked_etag": etag,
            "size_match": size_match,
            "sha256_match": match,
            "embedded_template_matches_hf": match,
            "hf_paths_tried": tried,
        }
        if match:
            result["status"] = "VERIFIED_match"
            result["detail"] = "Full-file SHA256 equals HF x-linked-etag"
        else:
            result["status"] = "FLAG_mismatch"
            result["detail"] = "Local GGUF bytes differ from HF-published blob"
        return result

    # No candidate returned etag
    last = tried[-1] if tried else {}
    if any(t.get("http_status") == "404" for t in tried):
        st = "SKIP_hf_404"
        detail = "No HF path candidate returned x-linked-etag (all 404 or missing etag)"
    else:
        st = "SKIP_no_x_linked_etag"
        detail = "HF HEAD returned no x-linked-etag on any candidate path"
    return {
        **base,
        "status": st,
        "detail": detail,
        "hf_paths_tried": tried,
        **{k: last[k] for k in ("huggingface_repo", "huggingface_filename") if k in last},
    }


def load_enabled() -> List[dict]:
    return [
        r
        for r in csv.DictReader(open(MODELS_CSV, newline=""))
        if str(r.get("enabled", "")).lower() in ("true", "1", "yes")
    ]


def run_audit(
    only_ids: Optional[List[str]] = None,
    index_cache: Path = CACHE_PATH,
) -> dict:
    if not index_cache.exists():
        raise SystemExit(f"LM Studio model index not found: {index_cache}")
    cache = json.loads(index_cache.read_text())
    by_id = {
        m.get("defaultIdentifier"): m
        for m in cache["models"]
        if m.get("defaultIdentifier")
    }
    enabled = load_enabled()
    if only_ids:
        only_set = set(only_ids)
        enabled = [r for r in enabled if r["lm_studio_id"] in only_set]

    rows: List[dict] = []
    for i, row in enumerate(enabled, 1):
        lid = row["lm_studio_id"]
        print(f"[{i}/{len(enabled)}] {lid}", flush=True)
        rows.append(audit_model(row, by_id))

    out = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "enabled_model_count": len(load_enabled()),
        "audited_count": len(rows),
        "crosswalk": LM_STUDIO_LOAD_CROSSWALK,
        "summary": dict(Counter(r["status"] for r in rows)),
        "models": rows,
    }
    return out


def merge_into_full(partial: dict) -> None:
    """Update existing full audit JSON with re-audited rows."""
    if not OUT_PATH.exists():
        OUT_PATH.write_text(json.dumps(partial, indent=2))
        return
    full = json.loads(OUT_PATH.read_text())
    by_id = {r["lm_studio_id"]: r for r in full.get("models", [])}
    for row in partial["models"]:
        by_id[row["lm_studio_id"]] = row
    full["models"] = sorted(by_id.values(), key=lambda r: r["lm_studio_id"])
    full["generated_at"] = partial["generated_at"]
    full["crosswalk"] = LM_STUDIO_LOAD_CROSSWALK
    full["summary"] = dict(Counter(r["status"] for r in full["models"]))
    OUT_PATH.write_text(json.dumps(full, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description="GGUF SHA256 audit vs HuggingFace")
    parser.add_argument(
        "--only",
        nargs="+",
        help="Re-audit only these lm_studio_id values and merge into existing JSON",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Re-audit all enabled models (overwrites output)",
    )
    parser.add_argument(
        "--index-cache",
        type=Path,
        default=CACHE_PATH,
        help="LM Studio model-index-cache.json (default: ~/.lmstudio/.internal/model-index-cache.json)",
    )
    args = parser.parse_args()

    ART.mkdir(parents=True, exist_ok=True)
    index_cache = args.index_cache

    if args.full:
        result = run_audit(index_cache=index_cache)
        OUT_PATH.write_text(json.dumps(result, indent=2))
    elif args.only:
        result = run_audit(only_ids=args.only, index_cache=index_cache)
        merge_into_full(result)
    else:
        # Default: re-audit the five previously fixable skips only
        fix_ids = [
            "m42-health_-_llama3-med42-70b",
            "qwen/qwen3-1.7b",
            "qwen/qwen3-4b",
            "llama-3.2-1b-instruct",
            "lmstudio-community/meta-llama-3.1-70b-instruct",
        ]
        result = run_audit(only_ids=fix_ids, index_cache=index_cache)
        merge_into_full(result)

    print("\nSUMMARY", result["summary"], flush=True)
    flags = [r for r in result["models"] if r["status"] == "FLAG_mismatch"]
    if flags:
        print("MISMATCHES", len(flags), file=sys.stderr)
        for r in flags:
            print(
                " ",
                r["lm_studio_id"],
                r.get("local_sha256"),
                r.get("huggingface_x_linked_etag"),
                file=sys.stderr,
            )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
