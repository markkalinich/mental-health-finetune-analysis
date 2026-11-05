"""Seed cache/ once from the files saved under zArchive/reviewer_2_experiments/hf_inventory/persisted/.

No Hub calls. Each cache file is hashed and recorded in cache/index.csv. Byte copies
(READMEs, catalog) must hash-match their source. A README already present with the
same hash (the same model in the child and parent dirs) is not recorded twice.
Reshaped files must round-trip: searches, the set of ids; cards, the set of
(hf_id, screened_at) rows.

Dates are UTC. Where a source carries its own timestamp (query-log started_at, card
screened_at) that is used. README files carry no fetch log; their mtime is used and the
index says so (date_source=mtime). The 4 Oct safety searches have no timestamps in
their logs; the folder date is used (date_source=folder_name).

Run from the repo root:
    .venv/bin/python model_selection/seed_cache.py
Refuses to run if cache/ already has content.
"""
from __future__ import annotations

import csv
import shutil
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import cache

PERSISTED = cache.ROOT.parent / "zArchive" / "reviewer_2_experiments" / "hf_inventory" / "persisted"
HARVEST = PERSISTED / "harvest"
ROWS = HARVEST / "2026-09-23-model-rows"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def rows(path: Path) -> list:
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def utc_date_of_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%d")


def record(cache_file: Path, kind: str, n: int, lo: str, hi: str, date_source: str, sources: list) -> None:
    cache.index_append({
        "cache_file": cache.rel(cache_file),
        "kind": kind,
        "n_rows": n,
        "fetched_at_min": lo,
        "fetched_at_max": hi,
        "date_source": date_source,
        "source_file": ";".join(cache.rel(s) for s in sources),
        "source_sha256": ";".join(cache.sha256_file(s) for s in sources),
        "cache_sha256": cache.sha256_file(cache_file),
    })


# ------------------------------------------------------------------ searches
def seed_queries(kind: str, hits: Path, log: Path, term_col: str, hit_term_col: str,
                 started_col: str, date_source: str, fixed_date: str = "") -> None:
    """One cache file per term in the query log, including terms with zero hits."""
    by_term = defaultdict(list)
    for r in rows(hits):
        # 4 Oct safety hits: one row per model, terms joined with ';'.
        # A 23 Sep row names one term. '|' is split the same way.
        for t in r[hit_term_col].replace("|", ";").split(";"):
            by_term[t].append(r["hf_id"])
    log_rows = rows(log)
    log_terms = [r[term_col] for r in log_rows]
    extra = set(by_term) - set(log_terms)
    if extra:
        fail(f"{hits}: terms with hits but no log row: {sorted(extra)}")
    if len(log_terms) != len(set(log_terms)):
        fail(f"{log}: duplicate terms")
    for r in log_rows:
        term = r[term_col]
        ids = by_term.get(term, [])
        if str(r["hit_count"]) != str(len(ids)):
            fail(f"{log}: {term!r} hit_count {r['hit_count']} but {len(ids)} hits in {hits.name}")
        ts = fixed_date or r[started_col]
        path = cache.write_search(kind, term, ts[:10], ids)
        if set(cache.read_ids(path)) != set(ids):
            fail(f"{path}: round-trip mismatch")
        record(path, f"search:{kind}", len(ids), ts, ts, date_source, [hits, log])
    print(f"searches {kind:6s} {hits.parent.name}: {len(log_terms)} terms, {sum(len(v) for v in by_term.values())} hit rows")


# ------------------------------------------------------------------ cards
def seed_cards(sources: list) -> None:
    all_rows = []
    for src in sources:
        all_rows.extend(rows(src))
    expected = {(r["hf_id"], r["screened_at"]) for r in all_rows}
    written = cache.append_cards(all_rows)
    got = set()
    for path in cache.CARDS.glob("*.csv"):
        got |= {(r["hf_id"], r["screened_at"]) for r in rows(path)}
    if got != expected:
        fail(f"cards round-trip mismatch: {len(got)} in cache vs {len(expected)} in sources")
    for date, n in sorted(written.items()):
        path = cache.card_path(date)
        ts = sorted(r["screened_at"] for r in rows(path))
        record(path, "card", len(ts), ts[0], ts[-1], "screened_at", sources)
    print(f"cards: {len(expected)} (hf_id, screened_at) rows across {len(written)} dates: {written}")


# ------------------------------------------------------------------ readmes
def seed_readmes(dirs: list) -> None:
    n = 0
    for d in dirs:
        for src in sorted(d.glob("*.md")):
            hf_id = src.stem.replace("__", "/", 1)
            date = utc_date_of_mtime(src)
            dest = cache.readme_path(hf_id, date)
            if dest.exists():
                if cache.sha256_file(dest) == cache.sha256_file(src):
                    continue  # same model in child and parent dirs, same text
                fail(f"{dest} exists with different content than {src}")
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dest)
            if cache.sha256_file(dest) != cache.sha256_file(src):
                fail(f"{dest}: copy hash differs from source")
            record(dest, "readme", 1, date, date, "mtime", [src])
            n += 1
    print(f"readmes: {n} files from {[d.name for d in dirs]}")


# ------------------------------------------------------------------ catalog
def seed_catalog(gz: Path, status_json: Path) -> None:
    import json
    status = json.loads(status_json.read_text())
    date = status["ended_utc"][:10]
    dest = cache.CATALOG / f"hub-public-ids__{date}.txt.gz"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(gz, dest)
    if cache.sha256_file(dest) != cache.sha256_file(gz):
        fail(f"{dest}: copy hash differs from source")
    record(dest, "catalog", status["id_count_unique"], status["started_utc"], status["ended_utc"],
           "walk-status.json", [gz, status_json])
    print(f"catalog: {status['id_count_unique']} ids, walk ended {status['ended_utc']}")


# ------------------------------------------------------------------ configs (from downloaded weights)
def seed_configs(weights_root: Path) -> None:
    """config.json of every model whose weights were downloaded, dated by the file's mtime (the
    download date). Lets the config check run for the locked view without a Hub call. Skips a
    model whose config for that date is already cached with the same hash."""
    n = 0
    for src in sorted(weights_root.glob("*/config.json")):
        hf_id = src.parent.name.replace("__", "/", 1)
        date = utc_date_of_mtime(src)
        dest = cache.config_path(hf_id, date)
        if dest.exists():
            if cache.sha256_file(dest) == cache.sha256_file(src):
                continue
            fail(f"{dest} exists with different content than {src}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
        if cache.sha256_file(dest) != cache.sha256_file(src):
            fail(f"{dest}: copy hash differs from source")
        record(dest, "config", 1, date, date, "mtime", [src])
        n += 1
    print(f"configs: {n} files from {weights_root}")


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "configs":
        seed_configs(Path(sys.argv[2]))
        return
    if len(sys.argv) != 1:
        fail("usage: seed_cache.py            (first seed, cache/ must be empty)\n"
             "       seed_cache.py configs /path/to/hf_models   (add config.json files from downloaded weights)")
    if cache.CACHE.exists() and any(cache.CACHE.iterdir()):
        fail(f"{cache.CACHE} already has content. Delete it to reseed.")
    cache.CACHE.mkdir(parents=True, exist_ok=True)

    seed_queries("search", HARVEST / "2026-09-23-search" / "hits.csv",
                 HARVEST / "2026-09-23-search" / "query-log.csv",
                 term_col="term", hit_term_col="term", started_col="started_at", date_source="query_log")
    seed_queries("filter", HARVEST / "2026-09-23-funnel" / "filter-hits.csv",
                 HARVEST / "2026-09-23-funnel" / "filter-query-log.csv",
                 term_col="tag", hit_term_col="tag", started_col="started_at", date_source="query_log")
    for sub in ("2026-10-04-safety-words", "2026-10-04-safety-search"):
        seed_queries("search", HARVEST / sub / "hits.csv", HARVEST / sub / "query-log.csv",
                     term_col="query_string", hit_term_col="terms", started_col="",
                     date_source="folder_name", fixed_date="2026-10-04")

    seed_cards([
        ROWS / "first-pass.csv",
        ROWS / "parent-first-pass.csv",
        HARVEST / "2026-10-04-safety-first-pass" / "first-pass-inventory.csv",
    ])
    seed_readmes([ROWS / "child-readmes", ROWS / "parent-readmes"])
    seed_catalog(PERSISTED / "catalog" / "hub-public-ids.txt.gz", PERSISTED / "catalog" / "walk-status.json")
    print(f"index: {cache.INDEX}")


if __name__ == "__main__":
    main()
