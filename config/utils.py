#!/usr/bin/env python3
"""
Configuration utilities and classes for experiment management.
"""

import yaml
from dataclasses import dataclass
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


def load_system_prompt(path: str, model_config=None) -> str:
    """
    Load system prompt from text file and apply model-specific modifications.
    
    Some models require special prompt suffixes to control their behavior:
    - Qwen models need '/no_think' suffix to disable chain-of-thought reasoning
      Without this, Qwen outputs verbose reasoning steps before the JSON response,
      which breaks JSON parsing. This is a documented Qwen feature.
    
    Args:
        path: Path to system prompt text file
        model_config: Optional model configuration with 'family' attribute
        
    Returns:
        System prompt string, potentially modified for specific model families
    """
    from config.constants import MODEL_SPECIFIC_PROMPT_SUFFIXES
    
    with open(path, "r", encoding="utf-8") as f:
        prompt = f.read().strip()
    
    # Apply model-specific prompt modifications
    if model_config and hasattr(model_config, 'family'):
        model_family = model_config.family
        # Check for exact match first, then prefix match (e.g., 'qwen_mental_health' matches 'qwen')
        suffix = None
        if model_family in MODEL_SPECIFIC_PROMPT_SUFFIXES:
            suffix = MODEL_SPECIFIC_PROMPT_SUFFIXES[model_family]
        else:
            # Check if family starts with any known prefix
            for prefix, prefix_suffix in MODEL_SPECIFIC_PROMPT_SUFFIXES.items():
                if model_family.startswith(prefix):
                    suffix = prefix_suffix
                    break
        
        if suffix:
            prompt += f'\n\n{suffix}'
            print(f"  ℹ️  Applied model-specific modification for {model_family}: added '{suffix}' suffix")
    
    return prompt