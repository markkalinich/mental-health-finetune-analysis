"""Fetch config.json for the models listed in <dataset-search folder>/configs-to-fetch.txt into the cache (dated by UTC day).
Needs HF_TOKEN: export HF_TOKEN="$(cat ~/.cache/huggingface/token)" in the foreground."""
import sys, datetime
from _common import parser, resolve, INV
sys.path.insert(0, str(INV))
import cache, hub
a = resolve(parser(__doc__).parse_args())
token = hub.require_hub_token()
date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
todo = [l.strip() for l in open(a.searches / f"{a.date}-dataset-search" / "configs-to-fetch.txt") if l.strip()]
print(len(todo), "configs to fetch", flush=True)
ok = err = 0
for i, hf in enumerate(todo, 1):
    text, e = hub.fetch_raw_text(hf, "config.json", token)
    path = cache.write_config(hf, date, text if text is not None else f"FETCH_ERR {e}\n")
    cache.index_append({"cache_file": cache.rel(path), "kind": "config", "n_rows": 1, "fetched_at_min": cache.now_iso(),
                        "fetched_at_max": cache.now_iso(), "date_source": "fetched", "source_file": f"hub:{hf}/config.json",
                        "source_sha256": "", "cache_sha256": cache.sha256_file(path)})
    ok += text is not None; err += text is None
    if i % 50 == 0: print(i, "done", ok, "ok", err, "err", flush=True)
print("finished", ok, "ok", err, "err")
