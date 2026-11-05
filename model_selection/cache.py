"""Paths and read/write helpers for the dated Hub cache.

Layout (all under cache/):
  searches/{kind}__{term}__{YYYY-MM-DD}.csv   one file per Hub query per UTC date; single column hf_id
  cards/{YYYY-MM-DD}__{NNN}.csv               card rows whose screened_at falls on that UTC date, in
                                              chunks of CARD_CHUNK_ROWS so no file nears GitHub's 100 MB
  readmes/{repo_id}__{YYYY-MM-DD}.md          README text (or a FETCH_ERR line); each / in the repo id is __
  configs/{repo_id}__{YYYY-MM-DD}.json        config.json text (or a FETCH_ERR line)
  bin_headers/{repo_id}__{YYYY-MM-DD}.json    tensor storage types read from each root pytorch_model.bin
  datasets/{name}__{YYYY-MM-DD}.json          whether a dataset name a card gives exists on the Hub
  datasets/{name}__{YYYY-MM-DD}.md            the dataset's README text (or a FETCH_ERR line); fetched only when asked
                                              (JSON: name, status ok|gated|not_found|error:..., id)
  catalog/hub-public-ids__{YYYY-MM-DD}.txt.gz full public id list
  index.csv                                   one row per cache file: where it came from, hashes, dates

The cache is append-only. A new fetch adds a new dated file or new rows; nothing is overwritten.
"as_of" and "since" are ISO date strings. Lookups return the newest entry on or before as_of;
with since, only entries dated since or later count (used to force a fresh fetch of everything).
"""
from __future__ import annotations

import csv
import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

csv.field_size_limit(sys.maxsize)

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / "cache"
SEARCHES = CACHE / "searches"
CARDS = CACHE / "cards"
READMES = CACHE / "readmes"
CONFIGS = CACHE / "configs"
BIN_HEADERS = CACHE / "bin_headers"
DATASETS = CACHE / "datasets"
CATALOG = CACHE / "catalog"
CARD_CHUNK_ROWS = 2000  # ~8 MB per chunk at the observed ~4 KB per card row
INDEX = CACHE / "index.csv"
INDEX_FIELDS = [
    "cache_file", "kind", "n_rows", "fetched_at_min", "fetched_at_max",
    "date_source", "source_file", "source_sha256", "cache_sha256",
]


# Every timestamp written into the cache (card screened_at, index fetched_at) uses this form.
# Card files are named from screened_at[:10] and rows are deduplicated on (hf_id, screened_at),
# so the form must not change.
TIMESTAMP = "%Y-%m-%dT%H:%M:%SZ"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime(TIMESTAMP)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


_DATE_RE = re.compile(r"__(\d{4}-\d{2}-\d{2})\.(csv|md|json|txt\.gz)$")


def _date_of(path: Path) -> str:
    """Trailing __YYYY-MM-DD before the suffix. Terms and model names may themselves contain '.'."""
    m = _DATE_RE.search(path.name)
    if not m:
        raise ValueError(f"no date in cache file name: {path.name}")
    return m.group(1)


def _newest(paths: Iterable[Path], as_of: str, since: str = "") -> Optional[Path]:
    ok = [p for p in paths if since <= _date_of(p) <= as_of]
    return max(ok, key=_date_of) if ok else None


def _write_text_once(path: Path, text: str) -> Path:
    """Write a dated text entry. Append-only, with one exception added 10 Oct 2026 (approved by Mark):
    an entry that is a fetch error (``FETCH_ERR ...``) may be replaced on the same day by real content.
    An error is not data, so replacing it changes nothing about what ``--as-of`` means for any date;
    before this, a repo opened to the token after a 403 had been cached could not be re-read until the
    next UTC day.     Content never replaces content, and an error never replaces anything (a repeated error on the
    same day leaves the existing entry untouched)."""
    if path.exists():
        old = path.read_text(encoding="utf-8", errors="replace")
        if not old.startswith("FETCH_ERR"):
            raise FileExistsError(path)
        if text.startswith("FETCH_ERR"):
            return path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


# ------------------------------------------------------------------ searches
def term_slug(term: str) -> str:
    # Spaces become '+' so "self harm" and "self-harm" stay distinct file names.
    if "/" in term or "+" in term:
        raise ValueError(f"term cannot contain '/' or '+': {term!r}")
    return term.replace(" ", "+")


def search_path(kind: str, term: str, date: str) -> Path:
    return SEARCHES / f"{kind}__{term_slug(term)}__{date}.csv"


def newest_search(kind: str, term: str, as_of: str, since: str = "") -> Optional[Path]:
    return _newest(SEARCHES.glob(f"{kind}__{term_slug(term)}__*.csv"), as_of, since)


def write_search(kind: str, term: str, date: str, ids: Iterable[str]) -> Path:
    path = search_path(kind, term, date)
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["hf_id"])
        for hf_id in ids:
            w.writerow([hf_id])
    return path


def read_ids(path: Path) -> list:
    with path.open(newline="") as fh:
        return [r["hf_id"] for r in csv.DictReader(fh)]


# ------------------------------------------------------------------ cards
def card_path(date: str, chunk: int) -> Path:
    return CARDS / f"{date}__{chunk:03d}.csv"


def _card_date(path: Path) -> str:
    return path.stem[:10]


def card_files(date: str) -> list:
    """Chunk files for one date, in chunk order."""
    return sorted(CARDS.glob(f"{date}__*.csv"))


def _count_rows(path: Path) -> int:
    with path.open(newline="") as fh:
        return sum(1 for _ in csv.DictReader(fh))


def load_cards(as_of: str, since: str = "") -> dict:
    """hf_id.lower() -> newest card row with since <= screened_at date <= as_of."""
    files = sorted((p for p in CARDS.glob("*.csv") if since <= _card_date(p) <= as_of), key=lambda p: p.name)
    out: dict = {}
    for path in files:
        with path.open(newline="") as fh:
            for row in csv.DictReader(fh):
                key = row["hf_id"].lower()
                prev = out.get(key)
                if prev is None or row["screened_at"] >= prev["screened_at"]:
                    out[key] = row
    return out


def append_cards(rows: list) -> dict:
    """Append rows into cards/{date}__{NNN}.csv by screened_at date, filling the last chunk of that
    date up to CARD_CHUNK_ROWS and then starting a new one. Skips exact (hf_id, screened_at)
    duplicates already stored for that date. Returns {path: n_written}."""
    by_date: dict = {}
    for row in rows:
        ts = row.get("screened_at") or ""
        if len(ts) < 10:
            raise ValueError(f"card row without screened_at: {row.get('hf_id')}")
        by_date.setdefault(ts[:10], []).append(row)
    written: dict = {}
    CARDS.mkdir(parents=True, exist_ok=True)
    for date, batch in sorted(by_date.items()):
        fields = list(batch[0].keys())
        existing = card_files(date)
        seen: set = set()
        for path in existing:
            with path.open(newline="") as fh:
                reader = csv.DictReader(fh)
                if reader.fieldnames != fields:
                    raise ValueError(f"{path}: header differs from rows being appended")
                seen |= {(r["hf_id"], r["screened_at"]) for r in reader}
        new = [r for r in batch if (r["hf_id"], r["screened_at"]) not in seen]
        new.sort(key=lambda r: (r["screened_at"], r["hf_id"]))
        chunk = len(existing) - 1 if existing else 0
        room = CARD_CHUNK_ROWS - _count_rows(existing[-1]) if existing else CARD_CHUNK_ROWS
        if room <= 0:
            chunk, room = chunk + 1, CARD_CHUNK_ROWS
        while new:
            path = card_path(date, chunk)
            part, new = new[:room], new[room:]
            with path.open("a", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=fields)
                if fh.tell() == 0:
                    w.writeheader()
                w.writerows(part)
            written[path] = written.get(path, 0) + len(part)
            chunk, room = chunk + 1, CARD_CHUNK_ROWS
    return written


# ------------------------------------------------------------------ readmes
def readme_name(hf_id: str) -> str:
    return hf_id.replace("/", "__")


def readme_path(hf_id: str, date: str) -> Path:
    return READMES / f"{readme_name(hf_id)}__{date}.md"


def newest_readme(hf_id: str, as_of: str, since: str = "") -> Optional[Path]:
    return _newest(READMES.glob(f"{readme_name(hf_id)}__*.md"), as_of, since)


def write_readme(hf_id: str, date: str, text: str) -> Path:
    return _write_text_once(readme_path(hf_id, date), text)


# ------------------------------------------------------------------ configs
def config_path(hf_id: str, date: str) -> Path:
    return CONFIGS / f"{readme_name(hf_id)}__{date}.json"


def newest_config(hf_id: str, as_of: str, since: str = "") -> Optional[Path]:
    return _newest(CONFIGS.glob(f"{readme_name(hf_id)}__*.json"), as_of, since)


def write_config(hf_id: str, date: str, text: str) -> Path:
    return _write_text_once(config_path(hf_id, date), text)


# ------------------------------------------------------------------ bin headers
# For a repo whose weights are pytorch_model.bin (no safetensors): the tensor storage types read
# from each root .bin file's pickle header, as JSON {"files": {name: [types] | "ERR <reason>"}}.
def bin_header_path(hf_id: str, date: str) -> Path:
    return BIN_HEADERS / f"{readme_name(hf_id)}__{date}.json"


def newest_bin_header(hf_id: str, as_of: str, since: str = "") -> Optional[Path]:
    return _newest(BIN_HEADERS.glob(f"{readme_name(hf_id)}__*.json"), as_of, since)


def write_bin_header(hf_id: str, date: str, text: str) -> Path:
    path = bin_header_path(hf_id, date)
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


# ------------------------------------------------------------------ datasets
# For a dataset name taken from a model card: the Hub's answer to "does a dataset repo with this
# name exist". Bare names ('empathetic_dialogues') are looked up as given; the Hub resolves the
# old canonical names and 404s the rest.
_UNSAFE = re.compile(r"[^A-Za-z0-9._-]")


def dataset_name(name: str) -> str:
    return _UNSAFE.sub("_", name.replace("/", "__"))


def dataset_path(name: str, date: str) -> Path:
    return DATASETS / f"{dataset_name(name)}__{date}.json"


def newest_dataset(name: str, as_of: str, since: str = "") -> Optional[Path]:
    return _newest(DATASETS.glob(f"{dataset_name(name)}__*.json"), as_of, since)


def write_dataset(name: str, date: str, text: str) -> Path:
    path = dataset_path(name, date)
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def dataset_readme_path(name: str, date: str) -> Path:
    return DATASETS / f"{dataset_name(name)}__{date}.md"


def newest_dataset_readme(name: str, as_of: str, since: str = "") -> Optional[Path]:
    return _newest(DATASETS.glob(f"{dataset_name(name)}__*.md"), as_of, since)


def write_dataset_readme(name: str, date: str, text: str) -> Path:
    return _write_text_once(dataset_readme_path(name, date), text)


# ------------------------------------------------------------------ catalog
def newest_catalog(as_of: str) -> Optional[Path]:
    return _newest(CATALOG.glob("hub-public-ids__*.txt.gz"), as_of)


# ------------------------------------------------------------------ current view
# outputs/funnel/<grouping>/CURRENT holds one line: the --as-of date of the run that is the grouping's
# current funnel. funnel.py writes it after a complete normal run (no cache misses, no --relax)
# whose date is not older than the one already there. Every script and document that quotes a
# count reads this file instead of naming a date, so there is one place to look.
RESULTS = ROOT.parent / "outputs" / "funnel"
_DATE_ONLY = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def current_path(grouping: str) -> Path:
    return RESULTS / grouping / "CURRENT"


def current_view(grouping: str) -> str:
    """The date in outputs/funnel/<grouping>/CURRENT. Raises FileNotFoundError when no run has set it."""
    path = current_path(grouping)
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist; run funnel.py --grouping {grouping} first")
    text = path.read_text().strip()
    if not _DATE_ONLY.match(text):
        raise ValueError(f"{path} must hold one ISO date, found {text!r}")
    return text


def current_dir(grouping: str) -> Path:
    return RESULTS / grouping / current_view(grouping)


def set_current(grouping: str, as_of: str) -> bool:
    """Write CURRENT when as_of is not older than what is there. Returns True when written."""
    path = current_path(grouping)
    if path.exists() and current_view(grouping) > as_of:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(as_of + "\n")
    return True


# ------------------------------------------------------------------ index
def index_append(record: dict) -> None:
    missing = set(INDEX_FIELDS) - set(record)
    if missing:
        raise ValueError(f"index record missing {sorted(missing)}")
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    new_file = not INDEX.exists()
    with INDEX.open("a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=INDEX_FIELDS)
        if new_file:
            w.writeheader()
        w.writerow({k: record[k] for k in INDEX_FIELDS})


def rel(path: Path) -> str:
    """Path relative to the repo root, for index rows. A source outside the repo (downloaded
    weights) is recorded by its absolute path."""
    repo = ROOT.parent
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(repo))
    except ValueError:
        return str(resolved)
