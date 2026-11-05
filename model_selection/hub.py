"""Hub client: the only module in this package that talks to huggingface.co.

Used by funnel.py --fetch through fill(missing, date). Every answer is written into cache/
under ``date``; nothing is returned to the caller. The calls, one kind per missing row:

  search:search / search:filter  GET /api/models?search=|filter=, every page (list_models_all_pages)
  card                           GET /api/models/{id}?expand=...   one request (first_pass_one)
  readme / config                GET /{id}/raw/main/README.md | config.json  (fetch_raw_text)
  bin_header                     three ranged GETs per root pytorch_model.bin shard (bin_storage_types)

Every request goes through hub_get -> huggingface_hub.utils.http_backoff, which on a 429
reads the RateLimit headers and waits until the reset plus one second. A token is required
(HF_TOKEN or HUGGING_FACE_HUB_TOKEN): no anonymous access, no gated-license accept, no
weight download. The helpers that shape a card row (FIRST_PASS_EXPAND, _serialize_*) were
copied from reviewer_2_experiments/hf_inventory/throughput.py on 5 Oct 2026 so this module
has no import outside the package and huggingface_hub.
"""
from __future__ import annotations

import json
import os
import re
import struct
import sys
from datetime import timezone
from pathlib import Path
from typing import Any

from huggingface_hub import HfApi, ModelInfo
from huggingface_hub.errors import GatedRepoError, RepositoryNotFoundError, HfHubHTTPError, HFValidationError
from huggingface_hub.utils import hf_raise_for_status, http_backoff

import cache

DEFAULT_SEARCH_PAGE_SIZE = 100  # per-request page size for /api/models, not a cap on hits
RAW_TEXT_MAX_BYTES = 5_000_000
RAW_FILES = ("README.md", "config.json")
LFS_POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1"  # the only files fetch_raw_text will GET
_LINK_NEXT_RE = re.compile(r"<([^>]+)>\s*;\s*rel=\"next\"", re.I)

# The expand= list for one card GET. ``id`` is always on the payload and is not an expand key.
FIRST_PASS_EXPAND = (
    "downloadsAllTime", "downloads", "likes", "createdAt", "lastModified", "gated", "disabled",
    "private", "library_name", "pipeline_tag", "tags", "cardData", "baseModels",
    "childrenModelCount", "safetensors", "spaces", "siblings",
)

# Columns of a card row (cache/cards/*.csv). The names and order are what the seeded September
# cards already use; changing them needs a cache migration.
FIRST_PASS_FIELDS = [
    "hf_id", "id", "repo_url", "wave_id", "screened_at", "downloads", "downloads_last_30_days",
    "likes", "createdAt", "lastModified", "gated", "disabled", "private", "library_name",
    "pipeline_tag", "tags", "cardData", "baseModels", "childrenModelCount", "safetensors",
    "spaces", "siblings", "sibling_count", "fetch_err", "http_status",
]


def require_hub_token() -> str:
    """Fail loud if HF_TOKEN and HUGGING_FACE_HUB_TOKEN are both unset."""
    token = (os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN") or "").strip()
    if not token:
        print("ERROR: HF_TOKEN or HUGGING_FACE_HUB_TOKEN must be set. Refusing anonymous Hub access.",
              file=sys.stderr)
        raise SystemExit(2)
    return token


def hub_get(url: str, *, headers: dict | None = None, params: dict | None = None, timeout: float = 60):
    """One Hub GET through http_backoff (waits out a 429). Tests patch this name."""
    kwargs: dict[str, Any] = {"timeout": timeout}
    if headers is not None:
        kwargs["headers"] = headers
    if params is not None:
        kwargs["params"] = params
    return http_backoff("GET", url, **kwargs)


def _next_link_url(response: Any) -> str | None:
    """The URL in the response's ``Link: <...>; rel="next"`` header, or None on the last page."""
    links = getattr(response, "links", None)
    if isinstance(links, dict):
        nxt = links.get("next")
        if isinstance(nxt, dict) and nxt.get("url"):
            return str(nxt["url"])
        if isinstance(nxt, str) and nxt:
            return nxt
    headers = getattr(response, "headers", None)
    raw = headers.get("link") or headers.get("Link") if headers is not None else None
    if not raw:
        return None
    m = _LINK_NEXT_RE.search(str(raw))
    return m.group(1) if m else None


def _raw_get_error_for_status(status: int) -> str | None:
    """404 -> MISSING, 401/403 -> INACCESSIBLE_<status>; none of these is retried."""
    if status == 404:
        return "MISSING"
    if status in (401, 403):
        return f"INACCESSIBLE_{status}"
    return None


def model_info_or_err(api: HfApi, repo_id: str, token: str, *, expand: list[str]) -> tuple[Any | None, str]:
    """GET /api/models/{repo_id}?expand=... -> (ModelInfo, "") or (None, reason).

    Built by hand rather than HfApi.model_info because the SDK method does not wait on a 429.
    """
    try:
        headers = api._build_hf_headers(token=token)
        r = hub_get(f"{api.endpoint.rstrip('/')}/api/models/{repo_id}", headers=headers,
                    params={"expand": list(expand)})
        hf_raise_for_status(r)
        return ModelInfo(**r.json()), ""
    except GatedRepoError as e:
        return None, f"GATED:{e}"
    except RepositoryNotFoundError:
        return None, "NOT_FOUND"
    except HfHubHTTPError as e:
        status = getattr(e.response, "status_code", None)
        if status in (401, 403):
            return None, f"INACCESSIBLE_{status}"
        return None, f"HTTP_{status}:{e}"
    except Exception as e:
        return None, f"ERROR:{type(e).__name__}:{e}"


def fetch_raw_text(repo_id: str, filename: str, token: str, *,
                   endpoint: str = "https://huggingface.co") -> tuple[str | None, str]:
    """GET /{repo_id}/raw/main/{filename} -> (text, "") or (None, reason). Only README.md and
    config.json are allowed; a 404 is MISSING and is not retried. When the file is stored in
    Git LFS, /raw/ returns a three-line pointer ("version https://git-lfs.github.com/spec/v1",
    oid, size) instead of the file; the function then re-reads it through /resolve/, which
    follows the redirect to the real bytes (nvidia/Nemotron-Content-Safety-Reasoning-4B keeps
    its config.json in LFS)."""
    if filename not in RAW_FILES:
        return None, "REFUSED_FILE"
    url = f"{endpoint.rstrip('/')}/{repo_id}/raw/main/{filename}"
    try:
        r = hub_get(url, headers={"Authorization": f"Bearer {token}"})
        status = getattr(r, "status_code", None)
        mapped = _raw_get_error_for_status(int(status)) if status is not None else None
        if mapped:
            return None, mapped
        hf_raise_for_status(r)
        data = r.content or b""
        if data.startswith(LFS_POINTER_PREFIX):
            r = hub_get(f"{endpoint.rstrip('/')}/{repo_id}/resolve/main/{filename}",
                        headers={"Authorization": f"Bearer {token}"})
            hf_raise_for_status(r)
            data = r.content or b""
            if data.startswith(LFS_POINTER_PREFIX):
                return None, "LFS_POINTER"
        if len(data) > RAW_TEXT_MAX_BYTES:
            return None, "TOO_LARGE"
        if b"\x00" in data[:1024]:
            return None, "BINARY_REFUSED"
        return data.decode("utf-8", errors="replace"), ""
    except GatedRepoError as e:
        return None, f"GATED:{e}"
    except RepositoryNotFoundError:
        return None, "NOT_FOUND"
    except HfHubHTTPError as e:
        status = getattr(e.response, "status_code", None)
        mapped = _raw_get_error_for_status(int(status)) if status is not None else None
        return None, mapped or f"HTTP_{status}"
    except Exception as e:
        return None, f"ERROR:{type(e).__name__}:{e}"


def safetensors_dtypes(repo_id: str, filename: str, token: str, *, endpoint: str = "https://huggingface.co") -> tuple:
    """(sorted dtype codes, "") or (None, reason) for one root safetensors shard, from the file's own
    header: the first 8 bytes give the header length, the header is JSON with one "dtype" per tensor
    (F32, BF16, F16, I64, ...). Two ranged GETs; no weights downloaded. Used when the Hub's dtype
    summary on the card is blank (added 9 Oct 2026)."""
    url = f"{endpoint.rstrip('/')}/{repo_id}/resolve/main/{filename}"
    auth = {"Authorization": f"Bearer {token}"}

    def ranged(spec: str) -> bytes:
        r = http_backoff("GET", url, headers={**auth, "Range": f"bytes={spec}"}, timeout=120, follow_redirects=True)
        if r.status_code == 404:
            raise FileNotFoundError("NOT_FOUND")
        if r.status_code in (401, 403):
            raise PermissionError(f"HTTP_{r.status_code}")
        hf_raise_for_status(r)
        if r.status_code != 206:
            raise ValueError(f"no range support (HTTP {r.status_code})")
        return r.content

    try:
        n = struct.unpack("<Q", ranged("0-7"))[0]
        if n <= 0 or n > 100_000_000:
            return None, f"NOT_SAFETENSORS:header_len_{n}"
        header = json.loads(ranged(f"8-{8 + n - 1}").decode("utf-8"))
        dtypes = sorted({v["dtype"] for k, v in header.items() if k != "__metadata__" and isinstance(v, dict) and "dtype" in v})
        if not dtypes:
            return None, "NO_TENSORS"
        return dtypes, ""
    except FileNotFoundError:
        return None, "NOT_FOUND"
    except PermissionError as e:
        return None, f"GATED:{e}"
    except Exception as e:  # noqa: BLE001  — recorded in the cache, never hidden
        return None, f"ERROR:{type(e).__name__}:{e}"


def bin_storage_types(repo_id: str, filename: str, token: str, *, endpoint: str = "https://huggingface.co") -> tuple:
    """(sorted storage type names, "") or (None, reason) for one root pytorch_model.bin shard.

    A .bin written by torch.save is a zip archive whose small data.pkl member lists every tensor's
    storage class (torch.FloatStorage, HalfStorage, BFloat16Storage, ByteStorage, ...). Three ranged
    GETs read it without downloading the weights: the zip end-of-central-directory (tail), the
    central directory (to locate data.pkl), then data.pkl itself. The pickle is scanned for
    storage class names, never unpickled. A pre-1.6 (non-zip) torch file is reported unreadable.
    """
    url = f"{endpoint.rstrip('/')}/{repo_id}/resolve/main/{filename}"
    auth = {"Authorization": f"Bearer {token}"}

    def ranged(spec: str) -> bytes:
        r = http_backoff("GET", url, headers={**auth, "Range": f"bytes={spec}"}, timeout=120, follow_redirects=True)
        if r.status_code == 404:
            raise FileNotFoundError("NOT_FOUND")
        if r.status_code in (401, 403):
            raise PermissionError(f"HTTP_{r.status_code}")
        hf_raise_for_status(r)
        if r.status_code != 206:
            raise ValueError(f"no range support (HTTP {r.status_code})")
        return r.content

    try:
        tail = ranged("-65536")
        i = tail.rfind(b"PK\x05\x06")
        if i < 0:
            return None, "NOT_ZIP"
        cd_size, cd_off = struct.unpack("<II", tail[i + 12:i + 20])
        if 0xFFFFFFFF in (cd_size, cd_off):
            j = tail.rfind(b"PK\x06\x06")
            if j < 0:
                return None, "ZIP64_EOCD_MISSING"
            cd_size, cd_off = struct.unpack("<QQ", tail[j + 40:j + 56])
        cd = ranged(f"{cd_off}-{cd_off + cd_size - 1}")
        p, pkl = 0, None
        while p + 46 <= len(cd) and cd[p:p + 4] == b"PK\x01\x02":
            n, m, k = struct.unpack("<HHH", cd[p + 28:p + 34])
            name = cd[p + 46:p + 46 + n].decode("utf-8", "replace")
            csize, usize = struct.unpack("<II", cd[p + 20:p + 28])
            lho = struct.unpack("<I", cd[p + 42:p + 46])[0]
            extra, q = cd[p + 46 + n:p + 46 + n + m], 0
            while q + 4 <= len(extra):  # zip64 extra field: 8-byte values for each 0xFFFFFFFF field, in order
                hid, hl = struct.unpack("<HH", extra[q:q + 4])
                if hid == 1:
                    vals = iter(struct.unpack("<" + "Q" * (hl // 8), extra[q + 4:q + 4 + (hl // 8) * 8]))
                    if usize == 0xFFFFFFFF:
                        usize = next(vals)
                    if csize == 0xFFFFFFFF:
                        csize = next(vals)
                    if lho == 0xFFFFFFFF:
                        lho = next(vals)
                q += 4 + hl
            if name.endswith("/data.pkl") or name == "data.pkl":
                pkl = (lho, csize)
                break
            p += 46 + n + m + k
        if pkl is None:
            return None, "NO_DATA_PKL"
        lho, csize = pkl
        lh = ranged(f"{lho}-{lho + 29}")
        n, m = struct.unpack("<HH", lh[26:30])
        start = lho + 30 + n + m
        data = ranged(f"{start}-{start + csize - 1}")
        types = sorted({t.decode() for t in re.findall(rb"\b([A-Za-z0-9]+Storage)\b", data)})
        return types, ""
    except FileNotFoundError:
        return None, "NOT_FOUND"
    except PermissionError as e:
        return None, f"GATED:{e}"
    except Exception as e:  # noqa: BLE001  — recorded in the cache, never hidden
        return None, f"ERROR:{type(e).__name__}:{e}"


def list_models_all_pages(api: HfApi, *, search: str | None = None, filter: str | None = None,
                          sort: str = "downloads", token: str,
                          page_size: int = DEFAULT_SEARCH_PAGE_SIZE) -> tuple[list[ModelInfo], int]:
    """Every Hub hit for one ``search=`` string or one exact ``filter=`` tag -> (models, pages).

    Follows the ``Link: rel="next"`` header until the last page; ``page_size`` is the per-request
    page size, not a cap. A 429 waits inside http_backoff; there is no sleep between pages.
    """
    if (search is None) == (filter is None):
        raise ValueError("pass exactly one of search= or filter=")
    label = search if search is not None else filter
    params: dict[str, Any] = {"sort": sort, "limit": page_size}
    params["search" if search is not None else "filter"] = label
    headers = api._build_hf_headers(token=token)
    url: str | None = f"{api.endpoint.rstrip('/')}/api/models"
    models: list[ModelInfo] = []
    pages = 0
    while url:
        pages += 1
        r = hub_get(url, headers=headers, params=params if pages == 1 else None)  # the next link carries its own params
        hf_raise_for_status(r)
        items = r.json()
        if not isinstance(items, list):
            raise TypeError(f"Hub /api/models expected a JSON list, got {type(items).__name__}")
        print(f"[search-page] q={label!r} page={pages} page_hits={len(items)}", flush=True)
        models.extend(ModelInfo(**item) for item in items)
        url = _next_link_url(r)
        if url and not items:
            print(f"[search-page] q={label!r} empty page with next link; stopping", file=sys.stderr)
            break
    return models, pages


# ---------------------------------------------------------------------------- one card row
def _json(val: Any) -> str:
    """JSON text with sorted keys, or str(val) when something inside is not serializable."""
    try:
        return json.dumps(val, sort_keys=True, default=str)
    except TypeError:
        return str(val)


def _hub_dt_iso(val: Any) -> str:
    if val is None or val == "":
        return ""
    if hasattr(val, "astimezone"):
        return val.astimezone(timezone.utc).strftime(cache.TIMESTAMP)
    return str(val)


def _serialize_card_data(val: Any) -> str:
    """The card's YAML front matter as JSON. ModelCardData has to_dict(); a plain dict is kept as is."""
    if val is None:
        return ""
    data = val.to_dict() if hasattr(val, "to_dict") else val
    return _json(data) if isinstance(data, dict) and data else ""


def _serialize_base_models(val: Any) -> str:
    """The Hub's baseModels lineage field, as JSON."""
    if val is None or val == "":
        return ""
    return val if isinstance(val, str) else _json(val)


def _serialize_safetensors(val: Any) -> str:
    """Parameter count by dtype and total, from the Hub's safetensors metadata; no weight bytes."""
    if val is None or val == "":
        return ""
    total = getattr(val, "total", None)
    params = getattr(val, "parameters", None)
    if total is None and params is None and isinstance(val, dict):
        total, params = val.get("total"), val.get("parameters")
    if total is None and params is None:
        return ""
    payload: dict[str, Any] = {}
    if total is not None:
        payload["total"] = total
    if params is not None:
        payload["parameters"] = dict(params) if hasattr(params, "items") else params
    return _json(payload)


def _spaces_count(val: Any) -> str:
    if val is None or val == "":
        return ""
    if isinstance(val, int):
        return str(val)
    return str(len(list(val))) if hasattr(val, "__iter__") else ""


def _serialize_siblings(val: Any) -> tuple[str, int]:
    """Repo file names and sizes as JSON, plus the count."""
    listing = []
    for s in list(val or []):
        if isinstance(s, dict):
            listing.append({"rfilename": s.get("rfilename"), "size": s.get("size")})
        else:
            listing.append({"rfilename": getattr(s, "rfilename", None), "size": getattr(s, "size", None)})
    return _json(listing), len(listing)


def first_pass_one(api: HfApi, hf_id: str, token: str, *, wave_id: str = "") -> dict[str, Any]:
    """One card row (FIRST_PASS_FIELDS) from exactly one GET /api/models/{id}?expand=FIRST_PASS_EXPAND.
    A model the Hub cannot serve still gets a row, with fetch_err set."""
    row: dict[str, Any] = {k: "" for k in FIRST_PASS_FIELDS}
    row.update({"hf_id": hf_id, "repo_url": f"https://huggingface.co/{hf_id}", "wave_id": wave_id,
                "screened_at": cache.now_iso()})
    info, err = model_info_or_err(api, hf_id, token, expand=list(FIRST_PASS_EXPAND))
    if err or info is None:
        row["fetch_err"] = err or "NO_INFO"
        return row

    def get(*names: str, default: Any = None) -> Any:
        for n in names:
            v = getattr(info, n, None)
            if v is not None:
                return v
        return default

    payload_id = get("id")
    if not payload_id:
        print(f"ERROR: card payload for {hf_id} has no id", file=sys.stderr)
        raise SystemExit(2)
    row["id"] = row["hf_id"] = str(payload_id)
    row["repo_url"] = f"https://huggingface.co/{payload_id}"
    lifetime = get("downloads_all_time", "downloadsAllTime")
    row["downloads"] = "" if lifetime is None else int(lifetime)
    last30 = get("downloads")
    row["downloads_last_30_days"] = "" if last30 is None else int(last30)
    likes = get("likes")
    row["likes"] = "" if likes is None else int(likes)
    row["createdAt"] = _hub_dt_iso(get("created_at", "createdAt"))
    row["lastModified"] = _hub_dt_iso(get("last_modified", "lastModified"))
    for field in ("gated", "disabled", "private"):
        row[field] = "yes" if get(field, default=False) else "no"
    row["library_name"] = get("library_name", default="") or ""
    row["pipeline_tag"] = get("pipeline_tag", default="") or ""
    row["tags"] = "|".join(str(t) for t in get("tags", default=[]) or [])
    row["cardData"] = _serialize_card_data(get("card_data", "cardData"))
    row["baseModels"] = _serialize_base_models(get("base_models", "baseModels"))
    children = get("children_model_count", "childrenModelCount")
    row["childrenModelCount"] = "" if children is None else children
    row["safetensors"] = _serialize_safetensors(get("safetensors"))
    row["spaces"] = _spaces_count(get("spaces"))
    row["siblings"], row["sibling_count"] = _serialize_siblings(get("siblings"))
    row["fetch_err"] = ""
    row["http_status"] = "200"
    return row


# ---------------------------------------------------------------------------- cache-miss fill
def _record(path: Path, kind: str, n: int, ts: str) -> None:
    cache.index_append({
        "cache_file": cache.rel(path), "kind": kind, "n_rows": n,
        "fetched_at_min": ts, "fetched_at_max": ts, "date_source": "fetched",
        "source_file": "huggingface.co", "source_sha256": "", "cache_sha256": cache.sha256_file(path),
    })


def dataset_status(api: HfApi, name: str, token: str) -> tuple[str, str]:
    """(status, resolved id). status: ok (public dataset repo), gated (exists; access controlled),
    not_found (404), or invalid_name (the string is not a Hub repo id, e.g. a card whose
    ``datasets:`` entry is the text ``['tasksource/bigbench', 'suicide_risk']``).
    Any other failure (network, 5xx) is raised so nothing wrong is cached. No files are downloaded."""
    try:
        info = api.dataset_info(name, token=token)
        return "ok", getattr(info, "id", name)
    except GatedRepoError:
        return "gated", name
    except RepositoryNotFoundError:
        return "not_found", ""
    except HFValidationError:
        return "invalid_name", ""
    except HfHubHTTPError as e:
        status = getattr(getattr(e, "response", None), "status_code", None)
        if status == 404:
            return "not_found", ""
        if status in (401, 403):
            return "gated", name
        raise


def fill(missing: list, date: str, *, page_size: int = DEFAULT_SEARCH_PAGE_SIZE) -> None:
    """Run the matching Hub call for each distinct missing row and write it into cache/ dated ``date``.

    kinds: search:search (term), search:filter (tag), card (hf_id), readme (hf_id), config (hf_id),
    bin_header (hf_id; the row's ``detail`` lists the root .bin shards, '|'-joined),
    dataset (a dataset name from a card; one dataset_info call -> ok | gated | not_found | error),
    dataset_readme (a dataset name; one raw GET of its README.md, written next to the status file).
    A search follows every page; a card is one expand GET; a README or config.json is one raw GET;
    a bin header is three ranged GETs per shard.
    A card the Hub cannot serve is still written, with fetch_err set, so the next
    pass treats it as unreadable (row_unreadable on the model, parent_unreadable
    on a parent) instead of missing. A README that cannot be fetched is written
    as a ``FETCH_ERR <reason>`` line, the form already stored in the seeded READMEs.
    """
    token = require_hub_token()
    api = HfApi()
    todo = sorted({(m["kind"], m["key"], m.get("detail", "")) for m in missing})
    cards: list = []

    def flush_cards() -> None:
        # Cards are appended in batches so a killed run keeps what it already fetched.
        if cards:
            written = cache.append_cards(cards)
            for path, n in written.items():
                _record(path, "card", n, cache.now_iso())
            print(f"[fill] cards: {sum(written.values())} rows appended")
            cards.clear()

    for kind, key, detail in todo:
        if kind in ("search:search", "search:filter"):
            which = kind.split(":", 1)[1]
            models, pages = list_models_all_pages(
                api, token=token, page_size=page_size, **{which: key}
            )
            ids = [m.id for m in models]
            path = cache.write_search(which, key, date, ids)
            _record(path, kind, len(ids), cache.now_iso())
            print(f"[fill] {kind} {key!r}: {len(ids)} ids, {pages} pages")
        elif kind == "card":
            cards.append(first_pass_one(api, key, token))
            if len(cards) >= 200:
                flush_cards()
        elif kind == "config":
            text, err = fetch_raw_text(key, "config.json", token)
            body = text if text is not None else f"FETCH_ERR {err}\n"
            path = cache.write_config(key, date, body)
            _record(path, kind, 1, cache.now_iso())
            print(f"[fill] config {key}: {'ok' if text is not None else err}")
        elif kind == "readme":
            text, err = fetch_raw_text(key, "README.md", token)
            body = text if text is not None else f"FETCH_ERR {err}\n"
            path = cache.write_readme(key, date, body)
            _record(path, kind, 1, cache.now_iso())
            print(f"[fill] readme {key}: {'ok' if text is not None else err}")
        elif kind == "dataset_readme":
            # The dataset's card text. Same raw GET as a model README, on the datasets/ namespace.
            text, err = fetch_raw_text(f"datasets/{key}", "README.md", token)
            body = text if text is not None else f"FETCH_ERR {err}\n"
            path = cache.write_dataset_readme(key, date, body)
            _record(path, kind, 1, cache.now_iso())
            print(f"[fill] dataset_readme {key}: {'ok' if text is not None else err}")
        elif kind == "dataset":
            status, resolved = dataset_status(api, key, token)
            path = cache.write_dataset(key, date, json.dumps({"name": key, "status": status, "id": resolved}) + "\n")
            _record(path, kind, 1, cache.now_iso())
            print(f"[fill] dataset {key!r}: {status}")
        elif kind == "bin_header":
            files = {}
            for fname in [f for f in detail.split("|") if f]:
                reader = safetensors_dtypes if fname.endswith(".safetensors") else bin_storage_types
                types, err = reader(key, fname, token)
                files[fname] = types if types is not None else f"ERR {err}"
            path = cache.write_bin_header(key, date, json.dumps({"files": files}, indent=1) + "\n")
            _record(path, kind, len(files), cache.now_iso())
            print(f"[fill] bin_header {key}: " + "; ".join(f"{f}={v}" for f, v in files.items()))
        else:
            raise ValueError(f"unknown missing kind {kind!r}")
    flush_cards()
