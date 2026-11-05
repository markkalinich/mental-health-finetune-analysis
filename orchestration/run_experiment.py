#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Single Model Experiment Runner for Safety Simulations

Runs safety simulation experiments on a single specified model with:
- Single model/prompt/dataset configuration per run
- Caching to avoid duplicate API calls
- Parallel processing with configurable concurrency
- Experiment metadata tracking
- Result storage with JSON and CSV outputs
- Replication support for statistical reliability

Use this for running individual experiments. For multi-model batch analysis,
use the bash_scripts/run_all_models.sh script instead.
"""

import argparse
import time
import json
import logging
import asyncio
from pathlib import Path
from typing import List, Dict, Any
from dataclasses import asdict

import sys
sys.path.append('..')

from config import load_system_prompt, EvaluationConfig
from config.utils import qwen_chat_template_kwargs
from config.experiment_config import get_experiment_config
from utilities.model_output_rules import parse_study_reply
from utilities.schemas import is_one_word_prompt, one_word_field_and_labels
from utilities.category_validator import validate_prompt_config_match, CategoryValidationError
from orchestration.api_client import ChatCompletionsClient, ChatAPIError
from orchestration.data_processor import DataProcessor
from orchestration.experiment_manager import ExperimentManager, ExperimentConfig
from cache.result_cache import ResultCache, CachedResult
from utilities.model_validator import ModelValidator, validate_experiment_model


def infer_experiment_type(prompt_name: str) -> str:
    """
    Infer experiment type from prompt name.
    
    Args:
        prompt_name: Name of the prompt (from PromptConfig.name)
        
    Returns:
        Experiment type string: 'suicidal_ideation', 'therapy_request', or 'therapy_engagement'
    """
    prompt_lower = prompt_name.lower()
    
    if 'suicide' in prompt_lower or 'si_' in prompt_lower or 'safety' in prompt_lower:
        return 'suicidal_ideation'
    elif 'engagement' in prompt_lower:
        return 'therapy_engagement'
    elif 'therapy' in prompt_lower or 'request' in prompt_lower or 'counseling' in prompt_lower:
        return 'therapy_request'
    else:
        # Default to therapy_request for unknown prompts
        print(f"⚠️  Warning: Could not infer experiment type from prompt name '{prompt_name}', defaulting to 'therapy_request'")
        return 'therapy_request'


def enhance_results_with_metadata(results: List[Dict[str, Any]], 
                                config: ExperimentConfig) -> List[Dict[str, Any]]:
    """Add experiment metadata to each result row."""
    
    enhanced_results = []
    for result in results:
        enhanced_result = result.copy()
        enhanced_result.update({
            'experiment_id': config.get_experiment_id(),
            'experiment_name': config.experiment_name,
            'model_family': config.model.family,
            'model_size': config.model.size,
            'model_version': config.model.version,
            'model_full_name': config.model.full_name,
            'prompt_name': config.prompt.name,
            'prompt_version': config.prompt.version,
            'temperature': config.temperature,
            'max_tokens': config.max_tokens,
            'created_at': config.created_at
        })
        enhanced_results.append(enhanced_result)
    
    return enhanced_results


def enhance_jsonl_with_metadata(jsonl_entries: List[Dict[str, Any]], 
                               config: ExperimentConfig) -> List[Dict[str, Any]]:
    """Add experiment metadata to each JSONL entry."""
    
    enhanced_entries = []
    for entry in jsonl_entries:
        enhanced_entry = entry.copy()
        enhanced_entry['experiment_metadata'] = {
            'experiment_id': config.get_experiment_id(),
            'experiment_name': config.experiment_name,
            'model': asdict(config.model),
            'prompt': asdict(config.prompt),
            'api_settings': {
                'temperature': config.temperature,
                'max_tokens': config.max_tokens,
                'top_p': config.top_p
            },
            'created_at': config.created_at
        }
        enhanced_entries.append(enhanced_entry)
    
    return enhanced_entries



async def process_batch_async(client: ChatCompletionsClient, 
                             system_prompt: str,
                             texts_to_process: List[tuple],  # (text, row_index, replicate_idx)
                             config: ExperimentConfig,
                             cache: ResultCache,
                             max_concurrent: int = 5) -> List[tuple]:
    """
    Process multiple texts concurrently using async API calls.
    
    Args:
        client: chat-completions client (vLLM or any OpenAI-compatible server)
        system_prompt: System prompt for the model
        texts_to_process: List of (text, row_index, replicate_idx) tuples
        config: Experiment configuration
        cache: Result cache instance
        max_concurrent: Maximum number of concurrent requests
        
    Returns:
        List of (raw_response, parsed_result, status, row_index) tuples
    """
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def process_single_async(text: str, row_index: int, replicate_idx: int):
        """Process a single text with concurrency control."""
        async with semaphore:
            start_time = time.time()
            try:
                # Make async API call
                raw_response = await client.call_chat_completion_async(system_prompt, text)
                processing_time = time.time() - start_time
                
                # Add timing information
                raw_response['processing_time_seconds'] = processing_time
                
                # Extract and parse content
                content = client.extract_content(raw_response)
                parsed_result = parse_study_reply(
                    content,
                    config.prompt.name,
                    infer_experiment_type(config.prompt.name),
                    config.model.full_name,
                )
                status = "ok" if parsed_result is not None else "parse_fail"
                
                # Store in cache (cache is None when --no-cache is set)
                if cache is not None:
                    cache.store_result(
                        config, text, system_prompt, raw_response, parsed_result, 
                        status, processing_time, replicate_idx
                    )
                
                return (raw_response, parsed_result, status, row_index)
                
            except ChatAPIError as e:
                processing_time = time.time() - start_time
                
                # Return error information
                error_response = {
                    "error": str(e),
                    "processing_time_seconds": processing_time
                }
                
                # Store error in cache (cache is None when --no-cache is set)
                if cache is not None:
                    cache.store_result(
                        config, text, system_prompt, error_response, None,
                        f"api_error:{str(e)[:200]}", processing_time, replicate_idx
                    )
                
                return (error_response, None, f"api_error:{str(e)[:200]}", row_index)
    
    # Create a progress tracking wrapper
    async def track_progress(task, task_index, total_tasks):
        result = await task
        # Print progress every 50 completions or at the end
        if (task_index + 1) % 50 == 0 or (task_index + 1) == total_tasks:
            progress_pct = ((task_index + 1) / total_tasks) * 100
            print(f"Progress: {task_index + 1}/{total_tasks} ({progress_pct:.1f}%) completed")
        return result
    
    # Create tasks for all texts to process
    tasks = [
        process_single_async(text, row_index, replicate_idx)
        for text, row_index, replicate_idx in texts_to_process
    ]
    
    # Process all tasks concurrently
    print(f"Processing {len(tasks)} requests with up to {max_concurrent} concurrent connections...")
    
    # Process with progress tracking - simpler approach
    completed_tasks = []
    total_tasks = len(tasks)
    
    # Use gather with return_exceptions to handle errors gracefully
    for i, task in enumerate(asyncio.as_completed(tasks)):
        try:
            result = await task
            completed_tasks.append(result)
            
            # Show progress every 50 items or at the end
            if len(completed_tasks) % 50 == 0 or len(completed_tasks) == total_tasks:
                progress_pct = (len(completed_tasks) / total_tasks) * 100
                print(f"Progress: {len(completed_tasks)}/{total_tasks} ({progress_pct:.1f}%) completed", flush=True)
                
        except Exception as e:
            completed_tasks.append(e)
    
    results = completed_tasks
    
    # Handle any exceptions that weren't caught
    processed_results = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            text, row_index, replicate_idx = texts_to_process[i]
            error_response = {"error": str(result), "processing_time_seconds": 0.0}
            processed_results.append((error_response, None, f"error:{str(result)[:200]}", row_index))
        else:
            processed_results.append(result)
    
    return processed_results


def _input_gold_column(experiment_type: str) -> str:
    if experiment_type == "therapy_request":
        return "therapy_request"
    if experiment_type == "therapy_engagement":
        return "therapy_engagement"
    return "prior_safety_type"


def _output_gold_column(experiment_type: str) -> str:
    if experiment_type == "therapy_request":
        return "prior_therapy_request"
    if experiment_type == "therapy_engagement":
        return "prior_therapy_engagement"
    return "prior_safety_type"


def _pred_column_for_type(experiment_type: str) -> str:
    if experiment_type == "therapy_request":
        return "therapy_request"
    if experiment_type == "therapy_engagement":
        return "therapy_engagement"
    return "safety_type"


def _user_message(text: str, prefix: str, suffix: str) -> str:
    """Put the sentence between the approved lines. Empty prefix and suffix leave the sentence unchanged."""
    if not prefix and not suffix:
        return text
    chunks = []
    if prefix:
        chunks.append(prefix)
    chunks.append(text.rstrip())
    if suffix:
        chunks.append(suffix)
    return "\n\n".join(chunks)


def run_experiment(config: ExperimentConfig, 
                  manager: ExperimentManager,
                  num_replicates: int = 1,
                  use_cache: bool = True,
                  max_concurrent: int = 1,
                  limit: int = 0,
                  output_summary: str = "",
                  user_prefix: str = "",
                  user_suffix: str = "") -> Dict[str, Any]:
    """
    Run a complete experiment with the given configuration.
    
    Args:
        config: Experiment configuration
        manager: Experiment manager instance
        
    Returns:
        Dictionary with experiment results summary
    """
    
    # Get result paths
    paths = manager.get_result_paths(config)
    
    # Cache is the single source of truth - CSV files are output logs only
    print(f"Running experiment {config.get_experiment_id()}")
    print(f"Cache-only approach: CSV files will be generated from cache + new API results")
    
    # Create evaluation config from experiment config
    eval_config = EvaluationConfig(
        base_url=config.base_url,
        model=config.model.full_name,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        top_p=config.top_p,
        request_timeout=config.request_timeout,
        request_delay=config.request_delay,
        chat_template_kwargs=qwen_chat_template_kwargs(
            config.model.family, model_id=config.model.full_name
        ),
    )
    
    # Load system prompt
    system_prompt = load_system_prompt(config.prompt.file_path, config.model)
    
    # Validate prompt categories match config expectations
    # This prevents expensive experiment failures due to taxonomy mismatches (DESIGN-11)
    print(f"\n{'='*70}")
    print(f"Validating prompt categories against config...")
    print(f"{'='*70}")
    try:
        experiment_type = infer_experiment_type(config.prompt.name)
        analysis_config = get_experiment_config(experiment_type)
        
        if is_one_word_prompt(config.prompt.name):
            # One-word prompts carry no JSON category block. Check that every label word the
            # parser accepts is written in the prompt file, and nothing else is parsed.
            spec = one_word_field_and_labels(config.prompt.name, experiment_type)
            if spec is None:
                raise CategoryValidationError(
                    f"No one-word labels for {config.prompt.name} ({experiment_type})")
            field, labels = spec
            prompt_text = Path(config.prompt.file_path).read_text()
            missing = [l for l in labels if l not in prompt_text]
            if missing:
                raise CategoryValidationError(
                    f"One-word prompt {config.prompt.file_path} does not contain label(s) {missing}")
            print(f"✅ One-word prompt: field {field}, labels {list(labels)} all present in prompt")
            print(f"   Experiment type: {experiment_type}")
            print(f"{'='*70}\n")
        else:
            validation_result = validate_prompt_config_match(
                config.prompt.file_path,
                analysis_config,
                strict=True  # Fail fast on mismatch
            )
            
            print(f"✅ Category validation passed!")
            print(f"   Experiment type: {experiment_type}")
            print(f"   Prompt declares: {list(validation_result['prompt_categories'].keys())}")
            if validation_result['warnings']:
                for warning in validation_result['warnings']:
                    print(f"   ⚠️  {warning}")
            print(f"{'='*70}\n")
        
    except CategoryValidationError as e:
        print(f"\n{'='*70}")
        print(f"❌ CATEGORY VALIDATION FAILED")
        print(f"{'='*70}")
        print(str(e))
        print(f"Aborting experiment to prevent incorrect results.")
        print(f"Fix the prompt or config, then try again.")
        print(f"{'='*70}\n")
        return {
            'status': 'validation_failed',
            'error': str(e),
            'experiment_id': config.get_experiment_id()
        }
    
    # Initialize components
    client = ChatCompletionsClient(eval_config)
    processor = DataProcessor()
    
    # Initialize cache
    cache = None
    if use_cache:
        cache_dir = manager.base_dir / "cache"
        cache = ResultCache(cache_dir)
        print(f"Cache initialized at: {cache_dir}")
    
    # Load and validate input data
    print(f"Loading input data from {config.input_dataset}")
    df = processor.load_input_data(config.input_dataset)
    if limit and limit > 0:
        from orchestration.pilot_sample import dataframe_stratified_take
        gold_col = _input_gold_column(experiment_type)
        if gold_col not in df.columns:
            raise ValueError(
                f"--limit needs gold column {gold_col!r} on {config.input_dataset}; "
                f"have {list(df.columns)}"
            )
        before = len(df)
        df = dataframe_stratified_take(df, gold_col, limit, seed=0)
        print(f"Pilot limit={limit}: kept {len(df)}/{before} rows stratified on {gold_col}")
    n_total = len(df)
    print(f"Loaded {n_total} rows for processing")
    print(f"Replicates per item: {num_replicates}")
    
    # Process each row
    output_rows: List[Dict[str, Any]] = []
    jsonl_entries: List[Dict[str, Any]] = []
    
    total_api_calls = 0
    cache_hits = 0
    
    print(f"Starting batch processing for experiment: {config.experiment_name}")
    
    # Phase 1: Collect all cache information and identify items to process
    all_results = {}  # row_idx -> [(raw_response, parsed_result, status), ...]
    texts_to_process = []  # [(text, row_idx, replicate_idx), ...]
    
    print("Phase 1: Checking cache...")
    for idx, row in df.iterrows():
        uid = row["id"]
        text = _user_message(str(row["text"]), user_prefix, user_suffix)
        
        if use_cache and cache:
            # Check cache for this text
            cached_results, missing_count = cache.check_cache(config, text, system_prompt, num_replicates)
            
            # Store cached results
            replicate_results = []
            for cached_result in cached_results:
                replicate_results.append((
                    cached_result.raw_response,
                    cached_result.parsed_result,
                    cached_result.status
                ))
            
            all_results[idx] = replicate_results
            cache_hits += len(cached_results)
            
            # Add missing items to processing queue
            for rep_idx in range(len(cached_results), num_replicates):
                texts_to_process.append((text, idx, rep_idx))
                total_api_calls += 1
        else:
            # No cache - process all replicates
            all_results[idx] = []
            for rep_idx in range(num_replicates):
                texts_to_process.append((text, idx, rep_idx))
                total_api_calls += 1
    
    print(f"Cache: {cache_hits} hits, {len(texts_to_process)} to process")
    
    # Phase 2: Process uncached items in parallel batches
    if texts_to_process:
        # Warmup: Ensure model is loaded before sending batch requests
        print(f"Warming up model...")
        if not client.warmup_model(max_retries=5, retry_delay=3.0):
            print("⚠️  Warning: Model warmup failed, proceeding anyway...")
        
        print(f"Processing {len(texts_to_process)} items...")
        
        batch_results = asyncio.run(process_batch_async(
            client, system_prompt, texts_to_process, config, cache,
            max_concurrent=max_concurrent
        ))
        
        # Organize batch results back into all_results
        for (raw_response, parsed_result, status, row_idx) in batch_results:
            if row_idx not in all_results:
                all_results[row_idx] = []
            all_results[row_idx].append((raw_response, parsed_result, status))
    
    print("Organizing results...")
    
    # Phase 3: Create output rows from all results
    for idx, row in df.iterrows():
        uid = row["id"]
        text = str(row["text"])
        
        # Disabled verbose progress output
        # if (idx + 1) % 10 == 0:  # Progress every 10 items
        #     print(f"Organizing {idx + 1}/{n_total}: ID={uid}")
        
        replicate_results = all_results.get(idx, [])
        
        try:
            
            # Create output entries for each replicate
            for rep_idx, (raw_response, parsed_result, status) in enumerate(replicate_results):
                # Add replicate information to the row
                rep_uid = f"{uid}_rep{rep_idx}" if num_replicates > 1 else uid
                
                output_row = processor.create_output_row(
                    rep_uid, text, parsed_result, status, row, df.columns.tolist()
                )
                # Add replicate metadata
                output_row['replicate_index'] = rep_idx
                output_row['total_replicates'] = num_replicates
                
                jsonl_entry = processor.create_jsonl_entry(
                    rep_uid, text, raw_response, parsed_result, status, row, df.columns.tolist()
                )
                # Add replicate metadata
                jsonl_entry['replicate_index'] = rep_idx
                jsonl_entry['total_replicates'] = num_replicates
                
                output_rows.append(output_row)
                jsonl_entries.append(jsonl_entry)
            
        except Exception as e:
            print(f"Error processing ID={uid}: {e}")
            # Create error rows for each intended replicate
            for rep_idx in range(num_replicates):
                rep_uid = f"{uid}_rep{rep_idx}" if num_replicates > 1 else uid
                
                error_row = processor.create_error_row(
                    rep_uid, text, e, row, df.columns.tolist()
                )
                error_row['replicate_index'] = rep_idx
                error_row['total_replicates'] = num_replicates
                output_rows.append(error_row)
                
                error_jsonl = processor.create_jsonl_entry(
                    rep_uid, text, {"error": str(e)}, None, f"error:{type(e).__name__}", 
                    row, df.columns.tolist()
                )
                error_jsonl['replicate_index'] = rep_idx
                error_jsonl['total_replicates'] = num_replicates
                jsonl_entries.append(error_jsonl)
    
    # Enhance results with experiment metadata
    enhanced_rows = enhance_results_with_metadata(output_rows, config)
    enhanced_jsonl = enhance_jsonl_with_metadata(jsonl_entries, config)
    
    # Results live only in the cache; no CSV or JSONL copy is written here.

    # Calculate summary statistics
    total_results = len(enhanced_rows)
    success_count = sum(1 for row in enhanced_rows if row["status"] == "ok")
    parse_fail_count = sum(1 for row in enhanced_rows if row["status"] == "parse_fail")
    error_count = sum(1 for row in enhanced_rows if row["status"].startswith("error") or row["status"].startswith("api_error"))
    
    summary = {
        'status': 'completed',
        'experiment_id': config.get_experiment_id(),
        'input_samples': n_total,
        'replicates_per_sample': num_replicates,
        'total_results': total_results,
        'successful': success_count,
        'parse_failures': parse_fail_count,
        'errors': error_count,
        'success_rate': success_count / total_results if total_results > 0 else 0,
        'total_api_calls': total_api_calls,
        'cache_hits': cache_hits,
        'cache_hit_rate': cache_hits / (cache_hits + total_api_calls) if (cache_hits + total_api_calls) > 0 else 0,
        'csv_output': str(paths['csv']),
        'jsonl_output': str(paths['jsonl'])
    }
    
    print(f"\nExperiment complete!")
    print(f"Experiment ID: {config.get_experiment_id()}")
    print(f"Input samples: {n_total}")
    print(f"Replicates per sample: {num_replicates}")
    print(f"Total results generated: {total_results}")
    print(f"Successful: {success_count}")
    print(f"Parse failures: {parse_fail_count}")
    print(f"Errors: {error_count}")
    print(f"Success rate: {summary['success_rate']:.1%}")
    if use_cache:
        print(f"API calls made: {total_api_calls}")
        print(f"Cache hits: {cache_hits}")
        print(f"Cache hit rate: {summary['cache_hit_rate']:.1%}")

    gold_col = _output_gold_column(experiment_type)
    pred_col = _pred_column_for_type(experiment_type)
    gold_vals = [row.get(gold_col) for row in enhanced_rows]
    pred_vals = [row.get(pred_col) for row in enhanced_rows]
    gold_present = sum(1 for g in gold_vals if g not in (None, ""))
    correct = sum(
        1 for g, p, row in zip(gold_vals, pred_vals, enhanced_rows)
        if row.get("status") == "ok" and g not in (None, "") and p == g
    )
    summary["standard_column"] = gold_col
    summary["pred_column"] = pred_col
    summary["standard_n"] = gold_present
    summary["standard_exact_match"] = (
        correct / gold_present if gold_present else None
    )
    summary["limit"] = limit
    if output_summary:
        out = Path(output_summary)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        print(f"Pilot summary: {out}")
    
    return summary


def main():
    """
    Execute a single model safety simulation experiment.
    
    Runs a complete experiment on one specified model with intelligent caching,
    parallel processing, and comprehensive result tracking. Processes all samples
    in the input dataset through the specified model and prompt configuration.
    """
    parser = argparse.ArgumentParser(
        description="Single model safety simulation experiment runner"
    )
    
    # Experiment definition
    parser.add_argument("--experiment-name", required=True,
                       help="Name for this experiment")
    parser.add_argument("--model-family", required=True,
                       help="Model family (gemma, llama, mistral, etc.)")
    parser.add_argument("--model-size", required=True,
                       help="Model size (270m, 4b, 12b, etc.)")
    parser.add_argument("--model-version", default="latest",
                       help="Model version (3, 3.1, etc.)")
    parser.add_argument("--model-name", default="",
                       help="API model id. When set, skip models_config.csv lookup.")
    parser.add_argument("--prompt-name", required=True,
                       help="Prompt configuration name")
    parser.add_argument("--input", required=True,
                       help="Path to input CSV file")
    
    # File paths
    parser.add_argument("--system", required=True,
                       help="Path to system prompt text file")
    parser.add_argument("--base-dir", default="./",
                       help="Base directory for experiment management")
    
    # API settings (optional, will use defaults if not specified)
    parser.add_argument("--base-url", default="http://localhost:1234/v1",
                       help="OpenAI-compatible server base URL, e.g. http://127.0.0.1:8000/v1 for vLLM")
    parser.add_argument("--temperature", type=float, default=0.0,
                       help="Sampling temperature")
    parser.add_argument("--max-tokens", type=int, default=256,
                       help="Maximum response tokens")
    parser.add_argument("--max-concurrent", type=int, default=1,
                       help="In-flight chat completions against one server. Keep 1 for LM Studio. vLLM can take more.")
    
    # Execution options
    parser.add_argument("--description", default="",
                       help="Description of this experiment")
    parser.add_argument("--num-replicates", type=int, default=1,
                       help="Number of replicates to run for each input (default: 1)")
    parser.add_argument("--no-cache", action="store_true",
                       help="Disable caching (force recomputation)")
    parser.add_argument("--force-recompute", action="store_true",
                       help="Skip cache and recompute all results")
    parser.add_argument("--retry-errors", action="store_true",
                       help="Retry API errors by deleting them from cache and re-running (default: False)")
    parser.add_argument("--limit", type=int, default=0,
                       help="Stratified subsample size for a smoke/pilot run (0 = all)")
    parser.add_argument("--output-summary", default="",
                       help="Write parse/gold smoke JSON here (pilot checker)")
    parser.add_argument("--user-prefix", default="",
                       help="Text placed before each sentence. The sentence itself is unchanged.")
    parser.add_argument("--user-suffix", default="",
                       help="Text placed after each sentence. The sentence itself is unchanged.")
    
    args = parser.parse_args()
    
    # Initialize experiment manager
    manager = ExperimentManager(Path(args.base_dir))
    
    # Create experiment configuration
    config = manager.create_experiment_config(
        experiment_name=args.experiment_name,
        model_family=args.model_family,
        model_size=args.model_size,
        model_version=args.model_version,
        prompt_name=args.prompt_name,
        prompt_file=args.system,
        input_dataset=args.input,
        description=args.description,
        model_name=args.model_name,
        base_url=args.base_url,
        temperature=args.temperature,
        max_tokens=args.max_tokens
    )
    
    # Run experiment
    use_cache = not args.no_cache
    summary = run_experiment(
        config, manager,
        num_replicates=args.num_replicates,
        use_cache=use_cache,
        max_concurrent=args.max_concurrent,
        limit=args.limit,
        output_summary=args.output_summary,
        user_prefix=args.user_prefix.strip(),
        user_suffix=args.user_suffix.strip(),
    )
    
    # API Error Retry Step (only if --retry-errors flag is set)
    if args.retry_errors and use_cache and summary.get('errors', 0) > 0:
        from cache.result_cache import ResultCache
        cache = ResultCache()
        
        api_error_count = cache.count_api_errors(
            model_family=args.model_family,
            model_size=args.model_size,
            prompt_name=args.prompt_name
        )
        
        if api_error_count > 0:
            print(f"\n{'='*60}")
            print(f"⚠️  Found {api_error_count} API errors - attempting retry...")
            print(f"{'='*60}")
            
            # Delete API errors to allow retry
            deleted = cache.delete_api_errors(
                model_family=args.model_family,
                model_size=args.model_size,
                prompt_name=args.prompt_name
            )
            print(f"Cleared {deleted} API error cache entries")
            
            # Re-run experiment (will only process the deleted items due to cache)
            print(f"\n--- Retry Run ---")
            retry_summary = run_experiment(
                config, manager,
                num_replicates=args.num_replicates,
                use_cache=True,  # Must use cache for retry to work
                max_concurrent=args.max_concurrent,
            )
            
            # Update summary with retry results
            summary['retry_performed'] = True
            summary['retry_api_errors_cleared'] = deleted
            summary['retry_errors'] = retry_summary.get('errors', 0)
            
            if retry_summary.get('errors', 0) > 0:
                print(f"\n⚠️  {retry_summary['errors']} errors remain after retry (not retrying again)")
            else:
                print(f"\n✓ All API errors resolved on retry!")
    
    # Summary JSON writing DISABLED - all experiment info is captured in comprehensive analysis reports
    # manager.results_dir.mkdir(parents=True, exist_ok=True)
    # summary_path = manager.results_dir / f"{config.get_experiment_id()}_summary.json"
    # with open(summary_path, 'w') as f:
    #     json.dump(summary, f, indent=2)
    # print(f"\nExperiment summary saved to: {summary_path}")


if __name__ == "__main__":
    main()