"""CSV lm_studio_id -> LM Studio CLI defaultIdentifier for lms load.

Same mapping as run_gguf_sha256_audit.py LM_STUDIO_ID_CROSSWALK.
"""
from __future__ import annotations

from typing import Dict

# Explicit human-approved crosswalk only — no guessing.
LM_STUDIO_LOAD_CROSSWALK: Dict[str, str] = {
    "qwen/qwen3-1.7b": "qwen3-1.7b",
    "qwen/qwen3-4b": "qwen3-4b",
    "llama-3.2-1b-instruct": "lmstudio-community/llama-3.2-1b-instruct",
    "lmstudio-community/meta-llama-3.1-70b-instruct": "meta-llama-3.1-70b-instruct",
}


def resolve_lms_load_id(lm_studio_id: str) -> str:
    return LM_STUDIO_LOAD_CROSSWALK.get(lm_studio_id, lm_studio_id)
