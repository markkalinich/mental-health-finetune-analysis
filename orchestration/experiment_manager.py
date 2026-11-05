#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced configuration and experiment management system for multi-model evaluations.

This system handles:
- Multiple model families (Gemma, LLaMA, Mistral, etc.)
- Multiple model sizes within families
- Multiple prompt variations
- Structured result storage and organization
- Experiment tracking and metadata management
"""


import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
import pandas as pd


def load_models_config() -> pd.DataFrame:
    """Load model configuration from CSV (single source of truth)."""
    config_path = Path(__file__).parent.parent / "config" / "models_config.csv"
    if not config_path.exists():
        raise FileNotFoundError(f"Models config not found: {config_path}")
    return pd.read_csv(config_path)


def get_model_name_map() -> Dict[Tuple[str, str, str], str]:
    """Build MODEL_NAME_MAP from CSV config."""
    df = load_models_config()
    result = {}
    for _, row in df.iterrows():
        if row.get('enabled', True):
            # Ensure version is string without trailing .0
            version = str(row['version'])
            if version.endswith('.0'):
                version = version[:-2]
            result[(row['family'], row['size'], version)] = row['lm_studio_id']
    return result



# Load MODEL_NAME_MAP from CSV (single source of truth)
MODEL_NAME_MAP = get_model_name_map()

# Note: MODEL_NAME_MAP is now loaded from config/models_config.csv
# To add a new model, just add a row to that CSV file.


def normalize_version(version: str) -> str:
    """Normalize version string for consistent lookup (e.g., '1.0' -> '1', '3.0' -> '3')."""
    version = str(version)
    if version.endswith('.0'):
        version = version[:-2]
    return version


@dataclass
class ModelConfig:
    """Configuration for a specific model."""
    family: str  # e.g., "gemma", "llama", "mistral"
    size: str    # e.g., "270m", "4b", "12b", "27b"
    version: str = "latest"  # e.g., "3", "3.1", "2.5"
    full_name: str = ""  # Full model name as used by LM Studio
    
    def __post_init__(self):
        if not self.full_name:
            # Normalize version for consistent lookup
            normalized_version = normalize_version(self.version)
            
            # Look up the model name in our mapping table
            key = (self.family, self.size, normalized_version)
            if key in MODEL_NAME_MAP:
                self.full_name = MODEL_NAME_MAP[key]
            else:
                # Also try with original version in case it's something like "1.1"
                key_original = (self.family, self.size, self.version)
                if key_original in MODEL_NAME_MAP:
                    self.full_name = MODEL_NAME_MAP[key_original]
                else:
                    # FAIL LOUDLY instead of using a bad fallback
                    # This prevents silent failures with invalid model identifiers
                    available_keys = [k for k in MODEL_NAME_MAP.keys() if k[0] == self.family]
                    raise ValueError(
                        f"Model ({self.family}, {self.size}, {self.version}) not found in MODEL_NAME_MAP. "
                        f"Available models for family '{self.family}': {available_keys}. "
                        f"Please add this model to config/models_config.csv with the correct lm_studio_id."
                    )


@dataclass
class PromptConfig:
    """Configuration for a specific prompt."""
    name: str  # e.g., "system_suicide_detection", "enhanced_safety_prompt"
    description: str
    file_path: str
    version: str = "1.0"


@dataclass
class ExperimentConfig:
    """Complete experiment configuration."""
    experiment_name: str
    model: ModelConfig
    prompt: PromptConfig
    input_dataset: str
    
    # API settings
    base_url: str = "http://localhost:1234/v1"
    temperature: float = 0.0
    max_tokens: int = 256
    top_p: float = 1.0
    request_timeout: int = 60
    request_delay: float = 0.02
    
    # Metadata
    created_at: str = ""
    description: str = ""
    
    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
    
    def get_experiment_id(self) -> str:
        """Generate unique experiment ID based on key parameters."""
        key_components = [
            self.model.family,
            self.model.size,
            self.model.version,
            self.prompt.name,
            self.prompt.version,
            Path(self.input_dataset).stem
        ]
        key_string = "_".join(str(c) for c in key_components)
        # Add hash for uniqueness while keeping readability
        hash_suffix = hashlib.md5(key_string.encode()).hexdigest()[:8]
        return f"{key_string}_{hash_suffix}"


class ExperimentManager:
    """Manages experiment configurations and result storage."""
    
    def __init__(self, base_dir: Path):
        self.base_dir = Path(base_dir)
        self.configs_dir = self.base_dir / "data" / "model_outputs" / "configs"
        self.results_dir = self.base_dir / "data" / "model_outputs"  # Fixed: was "results"
        
        # Directory creation DISABLED - no longer writing configs or results to data/model_outputs
        # Create directory structure
        # for dir_path in [self.configs_dir, self.results_dir]:
        #     dir_path.mkdir(parents=True, exist_ok=True)
    
    def create_experiment_config(self, 
                               experiment_name: str,
                               model_family: str,
                               model_size: str,
                               model_version: str,
                               prompt_name: str,
                               prompt_file: str,
                               input_dataset: str,
                               description: str = "",
                               model_name: str = "",
                               **api_kwargs) -> ExperimentConfig:
        """Create a new experiment configuration.

        model_name is the id sent to the API. When it is set, models_config.csv
        is not consulted. family/size/version still form the result-cache key
        and must be unique per checkpoint.
        """
        
        model = ModelConfig(
            family=model_family,
            size=model_size,
            version=model_version,
            full_name=model_name or "",
        )
        
        prompt = PromptConfig(
            name=prompt_name,
            description=f"Prompt configuration: {prompt_name}",
            file_path=prompt_file
        )
        
        config = ExperimentConfig(
            experiment_name=experiment_name,
            model=model,
            prompt=prompt,
            input_dataset=input_dataset,
            description=description,
            **api_kwargs
        )
        
        return config
    
    def get_result_paths(self, config: ExperimentConfig) -> Dict[str, Path]:
        """Get standardized paths for experiment results."""
        exp_id = config.get_experiment_id()
        
        # Directory creation DISABLED - no longer writing results to data/model_outputs
        # Results go directly to data/model_outputs (not in a subdirectory)
        # self.results_dir.mkdir(parents=True, exist_ok=True)
        
        # Define paths for analysis and visualizations (created on demand)
        analysis_dir = self.base_dir / "replies" / "analysis_reports"
        viz_dir = self.base_dir / "replies" / "visualizations"
        
        return {
            'csv': self.results_dir / f"{exp_id}_results.csv",
            'jsonl': self.results_dir / f"{exp_id}_results.jsonl",
            'analysis': analysis_dir / f"{exp_id}_analysis.txt",
            'visualizations': viz_dir / f"{exp_id}_visualizations"
        }
    


