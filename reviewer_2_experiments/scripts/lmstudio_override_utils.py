"""Shared helpers for LM Studio override JSON scan (127 enabled models)."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from lm_studio_load_crosswalk import LM_STUDIO_LOAD_CROSSWALK, resolve_lms_load_id

OVERRIDE_DIR = Path.home() / ".lmstudio/.internal/user-concrete-model-default-config"
INDEX_CACHE_PATH = Path.home() / ".lmstudio/.internal/model-index-cache.json"
MODELS_ROOT = Path.home() / ".lmstudio/models"


def load_enabled_models(models_csv: Path) -> List[dict]:
    return [
        r
        for r in csv.DictReader(models_csv.open(newline=""))
        if str(r.get("enabled", "")).lower() in ("true", "1", "yes")
    ]


def load_index_by_id(index_cache: Path) -> Dict[str, dict]:
    data = json.loads(index_cache.read_text())
    return {
        m["defaultIdentifier"]: m
        for m in data.get("models", [])
        if m.get("defaultIdentifier")
    }


def resolve_gguf_rel_path(lm_studio_id: str, by_id: Dict[str, dict]) -> Tuple[Optional[str], Optional[str]]:
    """Return (gguf_rel_path, resolved_index_id)."""
    index_id = resolve_lms_load_id(lm_studio_id)
    model = by_id.get(index_id)
    if not model:
        return None, None
    ep = model.get("entryPoint") or {}
    rel = ep.get("relPath")
    if rel:
        return rel, index_id
    abs_path = ep.get("absPath")
    if abs_path:
        try:
            return str(Path(abs_path).relative_to(MODELS_ROOT)), index_id
        except ValueError:
            return None, index_id
    return None, index_id


def override_config_path(gguf_rel_path: str) -> Path:
    return OVERRIDE_DIR / f"{gguf_rel_path}.json"


def extract_jinja_override(doc: Optional[dict]) -> Tuple[bool, Optional[str], Optional[str], list]:
    """Return (has_override, template_text, override_type, stop_strings)."""
    if not doc:
        return False, None, None, []
    for field in doc.get("operation", {}).get("fields", []):
        value = field.get("value") or {}
        if value.get("type") != "jinja":
            continue
        tmpl = (value.get("jinjaPromptTemplate") or {}).get("template")
        if tmpl:
            stops = value.get("stopStrings") or []
            return True, tmpl, "jinja", stops
    return False, None, None, []


def scan_model_row(row: dict, by_id: Dict[str, dict]) -> dict[str, Any]:
    lid = row["lm_studio_id"]
    out: dict[str, Any] = {
        "lm_studio_id": lid,
        "family": row["family"],
        "size": row["size"],
    }
    rel, index_id = resolve_gguf_rel_path(lid, by_id)
    if index_id and index_id != lid:
        out["index_id_resolved"] = index_id
    if not rel:
        out["status"] = "SKIP_no_index_entry"
        return out

    out["gguf_rel_path"] = rel
    cfg_path = override_config_path(rel)
    out["override_file"] = str(cfg_path)

    if not cfg_path.exists():
        out["lmstudio_jinja_override"] = False
        out["status"] = "ok_no_config_file"
        return out

    has_override, tmpl, otype, stops = extract_jinja_override(json.loads(cfg_path.read_text()))
    out["lmstudio_jinja_override"] = has_override
    if has_override:
        out["override_type"] = otype
        out["stopStrings"] = stops
        out["jinja_override_template"] = tmpl
        out["jinja_override_sha256"] = hashlib.sha256(tmpl.encode()).hexdigest()
    out["status"] = "ok"
    return out


def index_entry_failures(rows: List[dict]) -> List[str]:
    return sorted(
        m["lm_studio_id"]
        for m in rows
        if m.get("status") == "SKIP_no_index_entry"
    )


def build_override_scan(
    models_csv: Path,
    index_cache: Path = INDEX_CACHE_PATH,
    source_directory: Path = OVERRIDE_DIR,
) -> dict[str, Any]:
    if not index_cache.exists():
        raise FileNotFoundError(f"LM Studio index cache missing: {index_cache}")

    enabled = load_enabled_models(models_csv)
    by_id = load_index_by_id(index_cache)
    rows = [scan_model_row(r, by_id) for r in enabled]
    override_ids = sorted(m["lm_studio_id"] for m in rows if m.get("lmstudio_jinja_override"))
    return {
        "source_directory": str(source_directory),
        "enabled_model_count": len(enabled),
        "models_with_jinja_override_count": len(override_ids),
        "models_with_jinja_override": override_ids,
        "models": rows,
    }
