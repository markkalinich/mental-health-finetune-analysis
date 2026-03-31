#!/usr/bin/env python3
"""
Experiment Data Loader for Safety Simulations

Loads experiment data from the CACHE DATABASE (single source of truth).
Combines cached LLM results with ground truth labels from input CSV files.

Key Functions:
- load_and_validate_results(): Load from cache + join with ground truth
- Data validation and error checking for analysis pipeline

CRITICAL: This module ALWAYS loads LLM results from cache, never from CSV files.
CSV files in data/model_outputs/ are for provenance only and are NOT data sources.
"""

import json
import pandas as pd
from pathlib import Path
from typing import List, Tuple
from .metrics_calculator import determine_multiclass_labels
from cache.result_cache import ResultCache
from orchestration.experiment_manager import ExperimentConfig, ModelConfig, PromptConfig
from config.utils import load_system_prompt, EvaluationConfig
from config.experiment_config import get_experiment_config
from utilities.category_validator import validate_prompt_config_match, CategoryValidationError

GUARD_FAMILIES = frozenset(["llama_guard", "qwen_guard"])

_GUARD_POSITIVE = {
    "suicidal_ideation": ("safety_type", "passive_si"),
    "therapy_request": ("therapy_request", "explicit_therapy_request"),
    "therapy_engagement": ("therapy_engagement", "simulated_therapy"),
}
_GUARD_NEGATIVE = {
    "suicidal_ideation": ("safety_type", "no_SI"),
    "therapy_request": ("therapy_request", "declarative"),
    "therapy_engagement": ("therapy_engagement", "non_therapeutic"),
}


def _parse_guard_binary(raw_response: str) -> int:
    """Extract binary safe(0)/unsafe(1) from a guard model's raw API response."""
    try:
        data = json.loads(raw_response)
        content = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )
    except (json.JSONDecodeError, TypeError):
        return -1

    lower = content.lower()

    # Llama Guard: literal "safe" or "unsafe\n..."
    if lower == "safe":
        return 0
    if lower.startswith("unsafe"):
        return 1

    # Qwen Guard: "Safety: Safe" / "Safety: Unsafe"
    for line in content.split("\n"):
        if line.startswith("Safety:"):
            return 0 if "Safe" == line.replace("Safety:", "").strip() else 1

    return -1


def _reparse_guard_models(df: pd.DataFrame, experiment_type: str) -> pd.DataFrame:
    """Re-parse guard model rows in-place using their native output format.

    Guard models (Llama Guard, Qwen Guard) rigidly output plain text
    (safe/unsafe) regardless of the task prompt, so standard JSON
    validation marks them as parse_fail.  This function extracts the
    binary prediction from raw_response and maps it to the task's
    positive/negative category so metrics_calculator can score them
    like any other model.
    """
    guard_mask = (
        df["model_family"].isin(GUARD_FAMILIES) & (df["status"] == "parse_fail")
    )
    n_guard = guard_mask.sum()
    if n_guard == 0:
        return df

    pred_field, pos_val = _GUARD_POSITIVE[experiment_type]
    _, neg_val = _GUARD_NEGATIVE[experiment_type]

    parsed = df.loc[guard_mask, "raw_response"].apply(_parse_guard_binary)

    successful = parsed.isin([0, 1])
    success_idx = parsed[successful].index

    df.loc[success_idx, "status"] = "ok"
    df.loc[success_idx, pred_field] = parsed[successful].map(
        {1: pos_val, 0: neg_val}
    )

    n_ok = successful.sum()
    n_fail = n_guard - n_ok
    families = df.loc[guard_mask, "model_family"].unique().tolist()
    print(
        f"  Guard re-parse ({', '.join(families)}): "
        f"{n_ok}/{n_guard} rows recovered, {n_fail} still failed"
    )
    return df


def load_experiment_results(input_data_path: str, prompt_file_path: str, 
                           model_families: dict, experiment_type: str,
                           cache_dir: str = "cache") -> Tuple[pd.DataFrame, List[str]]:
    """
    Load experiment results from CACHE DATABASE (single source of truth).
    Joins cached LLM results with ground truth labels from input CSV.
    
    CRITICAL: This function ALWAYS loads from cache, never from CSV result files.
    
    Args:
        input_data_path: Path to input CSV with ground truth labels
        prompt_file_path: Path to prompt file
        model_families: Dictionary of model family configurations
        experiment_type: 'suicidal_ideation', 'therapy_request', or 'therapy_engagement'
        cache_dir: Path to cache directory
        
    Returns:
        Tuple of (combined_results_df, multiclass_labels_list)
        
    Raises:
        ValueError: If input data not found or cache query fails
    """
    print("Loading experiment results from CACHE...")
    
    # 1. Load input CSV to get input texts + ground truth labels
    input_df = pd.read_csv(input_data_path)
    print(f"Loaded {len(input_df)} inputs from {input_data_path}")
    
    # Determine ground truth column names based on experiment type
    if experiment_type == 'suicidal_ideation':
        ground_truth_col = 'Safety type'  # Note: capitalized in CSV
        # Input CSV uses 'statement' column for text
        text_col = 'statement' if 'statement' in input_df.columns else 'text'
    elif experiment_type == 'therapy_request':
        ground_truth_col = 'therapy_request'
        text_col = 'statement' if 'statement' in input_df.columns else 'text'
    elif experiment_type == 'therapy_engagement':
        ground_truth_col = 'therapy_engagement'
        text_col = 'statement' if 'statement' in input_df.columns else 'conversation'
    else:
        raise ValueError(f"Unknown experiment type: {experiment_type}")
    
    if text_col not in input_df.columns:
        raise ValueError(f"Input CSV must have '{text_col}' column")
    if ground_truth_col not in input_df.columns:
        raise ValueError(f"Input CSV must have '{ground_truth_col}' column for ground truth labels")
    
    # Check for duplicate texts with conflicting ground truth labels
    duplicates = input_df[input_df.duplicated(subset=[text_col], keep=False)]
    if len(duplicates) > 0:
        dup_conflicts = duplicates.groupby(text_col)[ground_truth_col].nunique()
        conflicts = dup_conflicts[dup_conflicts > 1]
        if len(conflicts) > 0:
            conflict_examples = conflicts.head(3).index.tolist()
            raise ValueError(
                f"Found {len(conflicts)} duplicate texts with conflicting ground truth labels! "
                f"Examples: {conflict_examples[:3]}... "
                f"Fix input data before running analysis."
            )
        else:
            print(f"  Note: {len(duplicates)} duplicate texts found, but all have consistent labels.")
    
    input_texts = input_df[text_col].tolist()
    
    # 2. Read prompt file and get prompt name
    prompt_name = Path(prompt_file_path).stem
    print(f"Loaded prompt: {prompt_name}")
    
    # 2.5. Validate prompt categories match config (DESIGN-11 protection)
    print(f"\nValidating prompt categories for {experiment_type}...")
    try:
        analysis_config = get_experiment_config(experiment_type)
        validation_result = validate_prompt_config_match(
            prompt_file_path,
            analysis_config,
            strict=False  # Warn but don't fail for analysis (data might be old)
        )
        
        if not validation_result['valid']:
            print(f"⚠️  WARNING: Category validation issues detected:")
            for mismatch in validation_result['mismatches']:
                print(f"   - {mismatch}")
            print(f"   Continuing analysis, but results may be incorrect if categories don't align.")
        else:
            print(f"✅ Category validation passed")
        
        if validation_result['warnings']:
            for warning in validation_result['warnings']:
                print(f"   ⚠️  {warning}")
    except CategoryValidationError as e:
        print(f"⚠️  WARNING: Could not validate categories: {e}")
        print(f"   Continuing analysis, but verify prompt/config alignment manually.")
    print()
    
    # 3. Initialize cache
    cache = ResultCache(cache_dir)
    stats = cache.get_statistics()
    print(f"Cache contains {stats['unique_entries']} unique entries, {stats['total_results']} total results")
    
    # 4. Query cache for each model
    all_model_results = []
    
    # Load models_config.csv (single source of truth for model metadata)
    from config.experiment_config import load_models_config
    models_config_df = load_models_config()
    
    eval_defaults = EvaluationConfig()
    
    for family_name, model_sizes in model_families.items():
        for model_size in model_sizes:
            # Look up version from models_config.csv (single source of truth)
            config_match = models_config_df[
                (models_config_df['family'] == family_name) & 
                (models_config_df['size'] == model_size)
            ]
            
            if len(config_match) > 0:
                # Use version from CSV, ensuring it's a string
                model_version = str(config_match.iloc[0]['version'])
            else:
                # Fail loudly - model must be in config for correct cache lookup
                raise ValueError(
                    f"Model {family_name} {model_size} not found in models_config.csv. "
                    f"Cannot determine correct version for cache lookup. "
                    f"Add this model to the config or remove it from model_families."
                )
            
            print(f"Loading cached results for {family_name} {model_size}...")
            
            # Create a simple model config object for load_system_prompt
            class SimpleModelConfig:
                def __init__(self, family):
                    self.family = family
            
            # Load prompt using the same function experiments use
            # This handles model-specific modifications (e.g., /no_think for qwen)
            model_config = SimpleModelConfig(family_name)
            prompt_content = load_system_prompt(prompt_file_path, model_config)
            
            config = ExperimentConfig(
                experiment_name=f"{family_name}_{model_size}_{prompt_name}_analysis",
                model=ModelConfig(
                    family=family_name,
                    size=model_size,
                    version=model_version,
                ),
                prompt=PromptConfig(
                    name=prompt_name,
                    description=f"Prompt: {prompt_name}",
                    file_path=prompt_file_path,
                    version="1.0",
                ),
                input_dataset=input_data_path,
                temperature=eval_defaults.temperature,
                max_tokens=eval_defaults.max_tokens,
                top_p=eval_defaults.top_p,
            )
            
            # Query cache for this model
            try:
                model_df = cache.load_results_for_analysis(config, input_texts, prompt_content)
                
                if len(model_df) == 0:
                    print(f"  WARNING: No cached results found for {family_name} {model_size}")
                    continue
                
                print(f"  Loaded {len(model_df)} cached results")
                all_model_results.append(model_df)
                
            except Exception as e:
                print(f"  ERROR loading cache for {family_name} {model_size}: {e}")
                continue
    
    if not all_model_results:
        raise ValueError("No cached results found for any models! Run experiments first to populate cache.")
    
    # 5. Combine all model results
    results_df = pd.concat(all_model_results, ignore_index=True)
    print(f"Combined {len(results_df)} total results from {len(all_model_results)} models")

    # 5b. Re-parse guard models (Llama Guard, Qwen Guard) from raw_response
    results_df = _reparse_guard_models(results_df, experiment_type)
    results_df.drop(columns=["raw_response"], inplace=True, errors="ignore")
    
    # 6. Join with ground truth labels
    # Create a mapping from input_text to ground truth
    ground_truth_map = dict(zip(input_df[text_col], input_df[ground_truth_col]))
    
    # Add ground truth column based on input_text
    if experiment_type == 'suicidal_ideation':
        results_df['prior_safety_type'] = results_df['input_text'].map(ground_truth_map)
    elif experiment_type == 'therapy_request':
        results_df['prior_therapy_request'] = results_df['input_text'].map(ground_truth_map)
    elif experiment_type == 'therapy_engagement':
        results_df['prior_therapy_engagement'] = results_df['input_text'].map(ground_truth_map)
    
    # Add other prior columns if they exist in input_df
    for col in input_df.columns:
        if col.startswith('prior_') or col in ['therapy_request', 'therapy_engagement', 'safety_type']:
            if col != ground_truth_col and col not in results_df.columns:
                col_map = dict(zip(input_df[text_col], input_df[col]))
                results_df[f'prior_{col}'] = results_df['input_text'].map(col_map)
    
    # Rename input_text to text for consistency with old format
    results_df.rename(columns={'input_text': 'text'}, inplace=True)
    
    # Add row IDs
    results_df.insert(0, 'id', range(1, len(results_df) + 1))
    
    # Determine multi-class label ordering
    multiclass_labels = determine_multiclass_labels(results_df, experiment_type)
    
    print(f"✓ Successfully loaded {len(results_df)} results from cache")
    return results_df, multiclass_labels


def get_experiment_result_files(results_pattern: str) -> List[str]:
    """
    DEPRECATED: This function is no longer used.
    Analysis loads directly from cache, not from CSV files.
    Kept for backward compatibility only.
    """
    import glob
    return glob.glob(results_pattern)


def validate_results_dataframe(results_df: pd.DataFrame, experiment_type: str) -> bool:
    """
    Validate that the results DataFrame has required columns for the experiment type.
    
    Args:
        results_df: Combined experiment results DataFrame
        experiment_type: 'suicide_detection', 'therapy_request', or 'therapy_engagement'
        
    Returns:
        True if valid, raises ValueError if invalid
        
    Raises:
        ValueError: If required columns are missing
    """
    required_base_columns = ['model_family', 'model_size', 'status']
    
    if experiment_type == 'therapy_request':
        # Therapy request experiments
        required_columns = required_base_columns + ['prior_therapy_request', 'therapy_request']
        missing_columns = [col for col in required_columns if col not in results_df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns for {experiment_type}: {missing_columns}")
    elif experiment_type == 'therapy_engagement':
        # Therapy engagement experiments
        required_columns = required_base_columns + ['prior_therapy_engagement', 'therapy_engagement']
        missing_columns = [col for col in required_columns if col not in results_df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns for {experiment_type}: {missing_columns}")
    else:  # suicidal_ideation
        required_columns = required_base_columns + ['prior_safety_type', 'safety_type']
        missing_columns = [col for col in required_columns if col not in results_df.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns for {experiment_type}: {missing_columns}")
    
    return True


def load_and_validate_results(input_data_path: str, prompt_file_path: str,
                             model_families: dict, experiment_type: str,
                             cache_dir: str = "cache") -> Tuple[pd.DataFrame, List[str]]:
    """
    Load experiment results from cache and validate they have required columns.
    
    Args:
        input_data_path: Path to input CSV with ground truth labels
        prompt_file_path: Path to prompt file
        model_families: Dictionary of model family configurations
        experiment_type: 'suicidal_ideation', 'therapy_request', or 'therapy_engagement'
        cache_dir: Path to cache directory
        
    Returns:
        Tuple of (validated_results_df, multiclass_labels_list)
        
    Raises:
        ValueError: If no results found or required columns missing
    """
    results_df, multiclass_labels = load_experiment_results(
        input_data_path, prompt_file_path, model_families, experiment_type, cache_dir
    )
    validate_results_dataframe(results_df, experiment_type)
    return results_df, multiclass_labels