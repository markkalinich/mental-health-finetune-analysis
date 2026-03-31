#!/usr/bin/env python3
"""
Shared utilities for facet plot generation.

This module contains common functionality used across all facet plot scripts:
- Model configuration loading
- Metadata helpers
- Color/marker definitions
"""

import pandas as pd
from pathlib import Path
from typing import Optional


# =============================================================================
# Configuration Loading
# =============================================================================

def load_models_config() -> Optional[pd.DataFrame]:
    """Load model configuration from CSV (single source of truth).
    
    Note: LM Studio has metadata bugs for some Qwen2 models:
      - qwen2-0.5b-instruct: Reports 5B, actually 0.5B
      - qwen2-1.5b: Reports 7B, actually 1.5B
      - qwen2-1.5b-instruct: Reports 5B, actually 1.5B
    These are manually corrected in models_config.csv.
    """
    config_path = Path(__file__).parent.parent.parent / "config" / "models_config.csv"
    if config_path.exists():
        return pd.read_csv(config_path)
    return None


# Module-level config cache
_MODELS_CONFIG: Optional[pd.DataFrame] = None


def get_models_config() -> Optional[pd.DataFrame]:
    """Get cached models config, loading if necessary."""
    global _MODELS_CONFIG
    if _MODELS_CONFIG is None:
        _MODELS_CONFIG = load_models_config()
    return _MODELS_CONFIG


def get_model_metadata(family: str, size: str) -> Optional[pd.Series]:
    """Get model metadata from CSV config."""
    config = get_models_config()
    if config is None:
        return None
    match = config[(config['family'] == family) & (config['size'] == size)]
    if len(match) > 0:
        return match.iloc[0]
    return None


def get_param_billions_from_config(family: str, size: str) -> float:
    """Get param_billions directly from models_config.csv."""
    config = get_models_config()
    if config is None:
        return float('nan')
    
    match = config[(config['family'] == family) & (config['size'] == size)]
    if len(match) > 0 and pd.notna(match.iloc[0].get('param_billions')):
        return float(match.iloc[0]['param_billions'])
    
    return float('nan')


# =============================================================================
# Color and Marker Definitions
# =============================================================================

# Consistent colors across all plots
# Base models = cool colors (blue/green), Fine-tunes = warm colors (red/orange/purple)
MODEL_TYPE_COLORS = {
    'IT': '#2E86AB',           # Blue (base instruct)
    'PT': '#52B788',           # Sea Green (base pretrain)
    'MedGemma': '#F18F01',     # Orange (medical fine-tune)
    'Medical': '#F18F01',      # Orange (medical fine-tune)
    'ShieldGemma': '#7B2D8E',  # Dark Purple (safety fine-tune)
    'Safety': '#7B2D8E',       # Dark Purple (safety fine-tune)
    'Guard': '#7B2D8E',        # Dark Purple (safety fine-tune)
    'Mental Health': '#C73E1D', # Red (mental health fine-tune)
}

# Consistent markers across all plots
MODEL_TYPE_MARKERS = {
    'IT': 'o',              # Circle
    'PT': 's',              # Square
    'MedGemma': 'D',        # Diamond
    'Medical': 'h',         # Hexagon (or 'D' for diamond)
    'ShieldGemma': '^',     # Triangle up
    'Safety': '^',          # Triangle up
    'Guard': '^',           # Triangle up
    'Mental Health': 'P',   # Plus (filled)
}

# Display labels for legend
MODEL_TYPE_DISPLAY_LABELS = {
    'IT': 'Instruct Tune',
    'PT': 'Base Model',
    'MedGemma': 'MedGemma',
    'Medical': 'Medical',
    'ShieldGemma': 'ShieldGemma',
    'Safety': 'Safety*',     # Asterisk indicates modified parsing
    'Guard': 'Guard*',       # Asterisk indicates modified parsing
    'Mental Health': 'Mental Health',
}
