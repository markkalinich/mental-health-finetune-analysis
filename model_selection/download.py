"""Download the weights of the current kept models and their parents, with a log.

    export HF_TOKEN="$(cat ~/.cache/huggingface/token)"
    .venv/bin/python model_selection/download.py --grouping mental-health            # kept + parents
    .venv/bin/python model_selection/download.py --grouping mental-health --dry-run  # list only

Reads outputs/funnel/<grouping>/<CURRENT>/kept.csv (the date in outputs/funnel/<grouping>/CURRENT), adds the
distinct parents, and for each repo not yet complete on disk runs

    hf download <repo> --local-dir <dest>/<org>__<name> --max-workers 1 --exclude "*.gguf" --exclude "mlx-int4/*"

the same call the 2 to 9 October downloads used (scripts and logs in /home/mkalinich/hf_models/). A repo is
complete when every weight file named in its index (or the single model.safetensors / pytorch_model.bin)
is present and no .incomplete part remains. One log line per repo with the Hub commit sha the
download pinned (read from <dest>/<repo>/.cache/huggingface or the API), to outputs/funnel/<grouping>/<CURRENT>/download_log.csv.
Stops before starting a repo when the destination disk has under --min-free-gib free. Exits 1 if any
repo failed; the log says which.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cache  # noqa: E402

DEFAULT_DEST = Path("/home/mkalinich/hf_models")
DEFAULT_HF = Path("/home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/hf")
WEIGHT = re.compile(
    r"^(?:model(?:-\d+-of-\d+)?\.safetensors|model\.safetensors(?:-\d+-of-\d+\.safetensors)?|pytorch_model(?:-\d+-of-\d+)?\.bin)$"
)
LOG_FIELDS = ["repo", "role", "dest", "status", "commit", "started", "ended", "detail"]


def folder(dest: Path, repo: str) -> Path:
    return dest / repo.replace("/", "__")


def complete(d: Path) -> tuple[bool, str]:
    if not d.is_dir():
        return False, "no folder"
    files = [p.name for p in d.iterdir() if p.is_file()]
    weights = [f for f in files if WEIGHT.match(f)]
    if not weights:
        return False, "no root weights"
    if list(d.glob(".cache/huggingface/download/**/*.incomplete")):
        return False, "incomplete parts"
    for idx in ("model.safetensors.index.json", "pytorch_model.bin.index.json"):
        p = d / idx
        if p.exists():
            try:
                need = sorted(set(json.load(p.open())["weight_map"].values()))
            except Exception as e:  # noqa: BLE001
                return False, f"bad index: {e}"
            missing = [s for s in need if not (d / s).exists()]
            if missing:
                return False, f"missing shards {missing[:3]}"
    return True, f"{len(weights)} weight files"


def pinned_commit(d: Path) -> str:
    """The Hub commit the files came from, as hf download records it under .cache/huggingface."""
    for meta in d.glob(".cache/huggingface/download/*.metadata"):
        try:
            lines = meta.read_text().splitlines()
            if len(lines) >= 1 and re.fullmatch(r"[0-9a-f]{40}", lines[0].strip()):
                return lines[0].strip()
        except OSError:
            pass
    return ""


def free_gib(path: Path) -> float:
    return shutil.disk_usage(path).free / 2**30


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grouping", required=True)
    ap.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    ap.add_argument("--hf-bin", type=Path, default=DEFAULT_HF)
    ap.add_argument("--min-free-gib", type=float, default=80.0)
    ap.add_argument("--no-parents", action="store_true", help="kept models only")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not (os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")) and not args.dry_run:
        print("ERROR: HF_TOKEN or HUGGING_FACE_HUB_TOKEN must be set.", file=sys.stderr)
        return 2
    if not args.hf_bin.exists() and not args.dry_run:
        print(f"ERROR: hf binary not found at {args.hf_bin}", file=sys.stderr)
        return 2

    current = cache.current_dir(args.grouping)
    kept = list(csv.DictReader((current / "kept.csv").open(newline="")))
    todo = [(r["hf_id"], "kept") for r in kept]
    if not args.no_parents:
        seen = {r["hf_id"].lower() for r in kept}
        for r in kept:
            if r["parent"] and r["parent"].lower() not in seen:
                seen.add(r["parent"].lower())
                todo.append((r["parent"], "parent"))
    print(f"{len(kept)} kept models, {len(todo) - len(kept)} distinct parents, from {current}")

    log_path = current / "download_log.csv"
    new_file = not log_path.exists()
    failed = 0
    with log_path.open("a", newline="") as fh:
        log = csv.DictWriter(fh, fieldnames=LOG_FIELDS)
        if new_file:
            log.writeheader()
        for repo, role in todo:
            d = folder(args.dest, repo)
            ok, why = complete(d)
            if ok:
                print(f"  have  {repo}  ({why})")
                log.writerow({"repo": repo, "role": role, "dest": str(d), "status": "present", "commit": pinned_commit(d),
                              "started": "", "ended": datetime.now(timezone.utc).isoformat(timespec="seconds"), "detail": why})
                continue
            if args.dry_run:
                print(f"  NEED  {repo}  ({why})")
                continue
            if free_gib(args.dest) < args.min_free_gib:
                print(f"STOP: {free_gib(args.dest):.0f} GiB free under {args.min_free_gib} GiB; not starting {repo}", file=sys.stderr)
                return 1
            d.mkdir(parents=True, exist_ok=True)
            started = datetime.now(timezone.utc).isoformat(timespec="seconds")
            print(f"  get   {repo} -> {d}")
            proc = subprocess.run([str(args.hf_bin), "download", repo, "--local-dir", str(d), "--max-workers", "1",
                                   "--exclude", "*.gguf", "--exclude", "mlx-int4/*"],
                                  capture_output=True, text=True)
            ok, why = complete(d)
            status = "downloaded" if proc.returncode == 0 and ok else "failed"
            failed += status == "failed"
            log.writerow({"repo": repo, "role": role, "dest": str(d), "status": status, "commit": pinned_commit(d),
                          "started": started, "ended": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                          "detail": why if status == "downloaded" else (proc.stderr or proc.stdout).strip()[-300:]})
            fh.flush()
            print(f"  {status}  {repo}  ({why})")
    print(f"log: {log_path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
