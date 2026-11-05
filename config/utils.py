#!/usr/bin/env python3
"""
Configuration utilities and classes for experiment management.
"""

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class EvaluationConfig:
    """Configuration for the evaluation run."""
    base_url: str = "http://localhost:1234/v1"
    model: str = "gemma-3-12b-instruct"
    temperature: float = 0.0
    max_tokens: int = 256
    top_p: float = 1.0
    request_timeout: int = 120
    request_delay: float = 0.02  # Delay between requests to be gentle on server
    # Qwen3 only. None for every other family.
    chat_template_kwargs: Optional[dict] = None


def load_config(path: str) -> EvaluationConfig:
    """Load configuration from YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        config_dict = yaml.safe_load(f)
    
    return EvaluationConfig(
        base_url=config_dict.get("base_url", "http://localhost:1234/v1"),
        model=config_dict.get("model", "gemma-3-12b-instruct"),
        temperature=float(config_dict.get("temperature", 0.0)),
        max_tokens=int(config_dict.get("max_tokens", 256)),
        top_p=float(config_dict.get("top_p", 1.0)),
        request_timeout=int(config_dict.get("request_timeout", 120)),
        request_delay=float(config_dict.get("request_delay", 0.02))
    )


def qwen_generation(model_id: Optional[str]) -> Optional[str]:
    """'qwen3' or 'qwen3.5' when this id is that generation. Otherwise None.

    The repo name is checked first. Qwen 3.5 is checked before Qwen 3
    because that string contains 'qwen3'. A hyphenated 'qwen-3' name counts
    as Qwen 3; 'qwen-32' does not. Qwen 2 and Qwen 2.5 return None from the
    name. If the name does not say, the local config.json model_type is
    used: qwen3, or qwen3_5. The family name is not used: the runner labels
    all three generations family qwen.
    """
    text = (model_id or "").lower()
    if "qwen3.5" in text or "qwen3-5" in text or "qwen-3.5" in text:
        return "qwen3.5"
    if "qwen3" in text or re.search(r"qwen-3([^0-9]|$)", text):
        return "qwen3"
    return _model_type_generation(model_id)


def _model_type_generation(model_id: Optional[str]) -> Optional[str]:
    """Qwen generation from the weights' config.json, when the repo name omits it."""
    if not model_id or "/" not in model_id:
        return None
    root = Path(os.environ.get("HF_MODELS_DIR", "/home/mkalinich/hf_models"))
    cfg_path = root / model_id.replace("/", "__") / "config.json"
    if not cfg_path.is_file():
        return None
    try:
        model_type = json.loads(cfg_path.read_text(encoding="utf-8")).get("model_type")
    except (OSError, json.JSONDecodeError):
        return None
    if model_type == "qwen3":
        return "qwen3"
    if model_type in ("qwen3_5", "qwen3_5_text"):
        return "qwen3.5"
    return None


def qwen_chat_template_kwargs(
    model_family: Optional[str] = None,
    model_id: Optional[str] = None,
) -> Optional[dict]:
    """Request field that turns Qwen 3 and Qwen 3.5 thinking off.

    Those templates prefill an empty think block only when enable_thinking
    is false. Qwen 2.5 has no such branch. When model_id is set, the id
    decides, including a local config.json whose model_type is qwen3 or
    qwen3_5 when the repo name does not say so. A call that passes only a
    family name keeps the old behavior.
    """
    if model_id:
        if qwen_generation(model_id) in ("qwen3", "qwen3.5"):
            return {"enable_thinking": False}
        return None
    if model_family and str(model_family).startswith("qwen"):
        return {"enable_thinking": False}
    return None


def _configured_model_id(model_config) -> str:
    if model_config is None:
        return ""
    return str(
        getattr(model_config, "full_name", "")
        or getattr(model_config, "model_id", "")
        or ""
    )


def apply_model_prompt_suffix(prompt: str, model_config=None) -> str:
    """Leave the prompt unchanged when the caller passes a model id.

    Thinking is turned off with chat_template_kwargs, not with /no_think.
    When the caller passes no model id, a family name of qwen still gets
    the suffix, so an old cache lookup that rebuilds the prompt from the
    family alone still matches rows stored that way.
    """
    from config.constants import MODEL_SPECIFIC_PROMPT_SUFFIXES

    model_id = _configured_model_id(model_config)
    if model_id:
        return prompt

    if not (model_config and hasattr(model_config, "family") and model_config.family):
        return prompt
    model_family = model_config.family
    suffix = None
    if model_family in MODEL_SPECIFIC_PROMPT_SUFFIXES:
        suffix = MODEL_SPECIFIC_PROMPT_SUFFIXES[model_family]
    else:
        for prefix, prefix_suffix in MODEL_SPECIFIC_PROMPT_SUFFIXES.items():
            if model_family.startswith(prefix):
                suffix = prefix_suffix
                break
    if not suffix:
        return prompt
    print(f"  ℹ️  Applied model-specific modification for {model_family}: added '{suffix}' suffix")
    return prompt.rstrip() + f"\n\n{suffix}"


def load_system_prompt(path: str, model_config=None) -> str:
    """
    Load system prompt from text file and apply model-specific modifications.
    
    A model id does not change the prompt text. Thinking-off is the request field.
    
    Args:
        path: Path to system prompt text file
        model_config: Optional model configuration with full_name or family
        
    Returns:
        System prompt string, potentially modified for specific model families
    """
    with open(path, "r", encoding="utf-8") as f:
        prompt = f.read().strip()
    return apply_model_prompt_suffix(prompt, model_config)