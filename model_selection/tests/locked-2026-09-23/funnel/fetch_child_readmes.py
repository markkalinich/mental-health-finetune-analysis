"""Fetch child READMEs for every full-precision keyword model, resuming from files on disk.

Uses run_pilot.fetch_raw_text, which waits on Hub RateLimit 429 headers via http_backoff.
Skips a file that already holds README text. Retries a previous FETCH_ERR once.
Does not print the token.

Run from the repo root:
    HF_TOKEN is read from ~/.cache/huggingface/token inside this process.
    python3 reviewer_2_experiments/hf_inventory/persisted/harvest/2026-09-23-funnel/fetch_child_readmes.py
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "reviewer_2_experiments" / "hf_inventory"))

TOKEN_PATH = Path.home() / ".cache" / "huggingface" / "token"
os.environ["HF_TOKEN"] = TOKEN_PATH.read_text().strip()

from run_pilot import fetch_raw_text  # noqa: E402

README_DIR = HERE.parent / "2026-09-23-model-rows" / "child-readmes"
README_DIR.mkdir(parents=True, exist_ok=True)
IDS = [ln.strip() for ln in (HERE / "fp-kept.txt").read_text().splitlines() if ln.strip()]


def path_for(hf_id: str) -> Path:
    return README_DIR / (hf_id.replace("/", "__") + ".md")


def already_ok(path: Path) -> bool:
    if not path.exists() or path.stat().st_size == 0:
        return False
    with path.open(errors="replace") as fh:
        return not fh.read(12).startswith("FETCH_ERR")


def main() -> None:
    todo = [h for h in IDS if not already_ok(path_for(h))]
    print(f"fp-kept {len(IDS)} | to fetch {len(todo)} | dir {README_DIR}", flush=True)
    ok = err = 0
    t0 = time.time()
    for i, hf_id in enumerate(todo, 1):
        text, status = fetch_raw_text(hf_id, "README.md", os.environ["HF_TOKEN"])
        dest = path_for(hf_id)
        if text is not None and status == "":
            dest.write_text(text)
            ok += 1
        else:
            dest.write_text(f"FETCH_ERR {status or 'EMPTY'}\n")
            err += 1
        if i % 25 == 0 or i == len(todo):
            rate = i / max(time.time() - t0, 0.1)
            print(f"{i}/{len(todo)} ok {ok} err {err} ({rate:.1f}/s) last {hf_id} {status or 'ok'}", flush=True)
    print(f"done ok {ok} err {err}", flush=True)


if __name__ == "__main__":
    main()
