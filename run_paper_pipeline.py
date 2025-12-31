#!/usr/bin/env python3
"""
Paper Pipeline - Generate All Figures and Tables for Publication

This script orchestrates the complete pipeline for generating all figures
and tables needed for the paper:

1. Run experiments for all 3 tasks (Suicidal Ideation, Therapy Request, Therapy Engagement)
   - Uses cached results where available
   - Retries api_error entries automatically (include_errors=False in cache check)
2. Generate main figures (Figure 1, 2, 3)
3. Generate main table (Table 1 - regression with Bonferroni correction)
4. Generate supplementary figures (9 family×task facet plots)

Output Structure:
    results/FINETUNE_PAPER_FIGURES/[YYYYMMDD]/
        figure_1/
            model_coverage_facet.png
        figure_2/
            figure_2_f1_vs_params_overall_trend.png  (main)
            figure_2_f1_vs_params.png
            figure_2_f1_vs_version_*.png
            figure_2_regression_statistics.csv
        figure_3/
            delta_f1_facet_plot_across_all_models_and_tasks.png
        table_1/
            regression_table_combined.csv
            regression_table.jpg
        supplementary_figures/
            gemma_suicidal_ideation.png
            gemma_therapy_request.png
            gemma_therapy_engagement.png
            llama_*.png, qwen_*.png (9 total)
        data/
            all_models_all_tasks.csv
            comprehensive_metrics_*.csv
            raw_responses/*.tar.gz

Usage:
    python run_paper_pipeline.py [--skip-experiments] [--figures-only] [--table-only]
    
    Options:
        --skip-experiments    Skip running experiments, assume results exist
        --figures-only        Only generate figures, skip table
        --table-only          Only generate table, skip figures
        --dry-run             Show what would be done without executing

Author: Safety Simulations Team
"""

import subprocess
import sys
import logging
import argparse
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, List, Dict
import os

# =============================================================================
# Configuration
# =============================================================================

ROOT = Path(__file__).parent
RESULTS_DIR = ROOT / "results"

# Output directories with timestamp
RUN_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
PAPER_FIGURES_BASE = RESULTS_DIR / "FINETUNE_PAPER_FIGURES" / RUN_TIMESTAMP
MAIN_OUTPUT_DIR = PAPER_FIGURES_BASE
SUPP_OUTPUT_DIR = PAPER_FIGURES_BASE / "supplementary_figures"

# Task configurations
TASKS = {
    "suicidal_ideation": {
        "input_data": "data/inputs/finalized_input_data/SI_finalized_sentences.csv",
        "prompt_file": "data/prompts/system_suicide_detection_v2.txt",
        "prompt_name": "system_suicide_detection_v2",
        "short_name": "SI",
    },
    "therapy_request": {
        "input_data": "data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv",
        "prompt_file": "data/prompts/therapy_request_classifier_v3.txt",
        "prompt_name": "therapy_request_classifier_v3",
        "short_name": "TR",
    },
    "therapy_engagement": {
        "input_data": "data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv",
        "prompt_file": "data/prompts/therapy_engagement_conversation_prompt_v2.txt",
        "prompt_name": "therapy_engagement_conversation_prompt_v2",
        "short_name": "TE",
    },
}

# Model families for supplementary figures
MODEL_FAMILIES = ["gemma", "llama", "qwen"]


# =============================================================================
# Logging Setup
# =============================================================================

def setup_logging(log_file: Optional[Path] = None) -> logging.Logger:
    """Configure logging with both console and file handlers."""
    logger = logging.getLogger("paper_pipeline")
    logger.setLevel(logging.DEBUG)
    
    # Console handler (INFO level)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        "%(asctime)s │ %(levelname)-8s │ %(message)s",
        datefmt="%H:%M:%S"
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)
    
    # File handler (DEBUG level)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            "%(asctime)s │ %(levelname)-8s │ %(name)s │ %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
    
    return logger


def log_section(logger: logging.Logger, title: str, char: str = "═") -> None:
    """Log a section header."""
    width = 70
    logger.info("")
    logger.info(char * width)
    logger.info(f"  {title}")
    logger.info(char * width)


def log_subsection(logger: logging.Logger, title: str) -> None:
    """Log a subsection header."""
    logger.info("")
    logger.info(f"─── {title} ───")


# =============================================================================
# Experiment Running
# =============================================================================

def run_experiments_for_task(
    task_name: str, 
    task_config: Dict, 
    logger: logging.Logger,
    dry_run: bool = False
) -> Tuple[bool, Optional[Path]]:
    """
    Run experiments for a single task using run_all_models.sh.
    
    Returns:
        Tuple of (success, output_dir_path)
    """
    log_subsection(logger, f"Task: {task_name.replace('_', ' ').title()}")
    
    input_data = ROOT / task_config["input_data"]
    prompt_file = ROOT / task_config["prompt_file"]
    prompt_name = task_config["prompt_name"]
    
    logger.info(f"  Input data:  {input_data}")
    logger.info(f"  Prompt:      {prompt_file}")
    logger.info(f"  Prompt name: {prompt_name}")
    
    if dry_run:
        logger.info("  [DRY RUN] Would execute run_all_models.sh")
        return True, None
    
    # Build command
    cmd = [
        str(ROOT / "bash_scripts" / "run_all_models.sh"),
        str(input_data),
        str(prompt_file),
        prompt_name,
    ]
    
    logger.info(f"  Executing: {' '.join(cmd[:1])} ...")
    logger.debug(f"  Full command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(
            cmd,
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=7200,  # 2 hour timeout per task
        )
        
        if result.returncode != 0:
            logger.error(f"  ✗ Experiment failed with exit code {result.returncode}")
            logger.debug(f"  STDOUT: {result.stdout[-2000:] if result.stdout else 'None'}")
            logger.debug(f"  STDERR: {result.stderr[-2000:] if result.stderr else 'None'}")
            return False, None
        
        logger.info(f"  ✓ Experiments completed successfully")
        
        # Find the output directory from stdout (look for "Output:" line)
        output_dir = None
        for line in result.stdout.split('\n'):
            if 'Output:' in line and 'results/individual_prediction_performance' in line:
                output_dir = Path(line.split('Output:')[-1].strip())
                break
        
        if output_dir:
            logger.info(f"  Output dir: {output_dir}")
        
        return True, output_dir
        
    except subprocess.TimeoutExpired:
        logger.error(f"  ✗ Experiment timed out after 2 hours")
        return False, None
    except Exception as e:
        logger.error(f"  ✗ Experiment failed with exception: {e}")
        return False, None


def run_all_experiments(logger: logging.Logger, dry_run: bool = False) -> Dict[str, Path]:
    """
    Run experiments for all tasks.
    
    Returns:
        Dict mapping task_name -> output_dir
    """
    log_section(logger, "PHASE 1: RUNNING EXPERIMENTS (FROM CACHE)")
    
    results = {}
    all_success = True
    
    for task_name, task_config in TASKS.items():
        success, output_dir = run_experiments_for_task(
            task_name, task_config, logger, dry_run
        )
        if success:
            results[task_name] = output_dir
        else:
            all_success = False
            logger.warning(f"  ⚠ Task {task_name} failed, continuing with others...")
    
    if all_success:
        logger.info("")
        logger.info("✓ All experiments completed successfully")
    else:
        logger.warning("")
        logger.warning("⚠ Some experiments failed - check logs for details")
    
    return results


# =============================================================================
# Figure Generation
# =============================================================================

def run_python_script(
    script_path: Path, 
    args: List[str], 
    logger: logging.Logger,
    cwd: Optional[Path] = None,
    dry_run: bool = False
) -> bool:
    """Run a Python script and return success status."""
    if cwd is None:
        cwd = ROOT
    
    cmd = [sys.executable, str(script_path)] + args
    
    logger.debug(f"  Command: {' '.join(cmd)}")
    
    if dry_run:
        logger.info(f"  [DRY RUN] Would run: {script_path.name}")
        return True
    
    try:
        result = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=600,  # 10 min timeout
        )
        
        if result.returncode != 0:
            logger.error(f"  ✗ Script failed: {script_path.name}")
            logger.debug(f"  STDERR: {result.stderr[-1000:] if result.stderr else 'None'}")
            return False
        
        # Log any output
        if result.stdout:
            for line in result.stdout.strip().split('\n')[-5:]:
                logger.debug(f"    {line}")
        
        return True
        
    except subprocess.TimeoutExpired:
        logger.error(f"  ✗ Script timed out: {script_path.name}")
        return False
    except Exception as e:
        logger.error(f"  ✗ Script failed with exception: {e}")
        return False


def generate_figure_1(logger: logging.Logger, dry_run: bool = False) -> bool:
    """Generate Figure 1: Model Coverage Heatmap."""
    log_subsection(logger, "Figure 1: Model Coverage Heatmap")
    
    script = ROOT / "analysis" / "model_coverage_heatmap.py"
    output_dir = MAIN_OUTPUT_DIR / "figure_1"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if dry_run:
        logger.info(f"  [DRY RUN] Would run: {script.name}")
        return True
    
    # Run the script
    success = run_python_script(script, [], logger, dry_run=dry_run)
    
    if success:
        # Copy output to figure_1 subdirectory
        src = RESULTS_DIR / "model_coverage" / "model_coverage_facet.png"
        dst = output_dir / "model_coverage_heatmap.png"
        
        if src.exists():
            shutil.copy(src, dst)
            logger.info(f"  ✓ Saved: figure_1/{dst.name}")
            return True
        else:
            logger.warning(f"  ⚠ Output not found: {src}")
            return False
    
    return False


def generate_figure_2(logger: logging.Logger, dry_run: bool = False) -> bool:
    """Generate Figure 2: F1 vs Parameters with Overall Trend."""
    log_subsection(logger, "Figure 2: F1 vs Parameters (Overall Trend)")
    
    script = ROOT / "analysis" / "comparative_analysis" / "compact_unified_facet_plot.py"
    output_dir = MAIN_OUTPUT_DIR / "figure_2"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # The script generates multiple plots with prefix_<metric>_<type>.png format
    args = [
        "--output-dir", str(output_dir),
        "--prefix", "fig2",  # Prefix for figure 2 plots
    ]
    
    if dry_run:
        logger.info(f"  [DRY RUN] Would run: {script.name}")
        return True
    
    success = run_python_script(script, args, logger, dry_run=dry_run)
    
    if success:
        # Check for any generated plots
        plots = list(output_dir.glob("*.png"))
        
        if plots:
            main_plot = output_dir / "f1_vs_params_overall_trend.png"
            if main_plot.exists():
                logger.info(f"  ✓ Saved: figure_2/{main_plot.name}")
            
            # Also note that other variants were generated
            logger.info("  ✓ Additional variants generated:")
            for f in plots:
                if f != main_plot:
                    logger.info(f"      {f.name}")
            
            return True
        else:
            logger.warning(f"  ⚠ No plots generated")
            return False
    
    return False


def generate_figure_3(logger: logging.Logger, dry_run: bool = False) -> bool:
    """Generate Figure 3: Delta F1 Fine-tune Facet Plot."""
    log_subsection(logger, "Figure 3: Delta F1 Fine-tune Facet Plot")
    
    script = ROOT / "analysis" / "combined_finetune_facet_plot.py"
    output_dir = MAIN_OUTPUT_DIR / "figure_3"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if dry_run:
        logger.info(f"  [DRY RUN] Would run: {script.name}")
        return True
    
    success = run_python_script(script, [], logger, dry_run=dry_run)
    
    if success:
        src_dir = RESULTS_DIR / "fine_tune_figures"
        
        # Copy the main figure
        src_png = src_dir / "delta_f1_facet_plot_across_all_models_and_tasks.png"
        if src_png.exists():
            shutil.copy(src_png, output_dir / "delta_f1_finetune_facet.png")
            logger.info(f"  ✓ Saved: figure_3/delta_f1_finetune_facet.png")
        else:
            logger.warning(f"  ⚠ Output not found: {src_png}")
            return False
        
        # Copy the data CSV
        src_data = src_dir / "delta_f1_facet_plot_across_all_models_and_tasks_data.csv"
        if src_data.exists():
            shutil.copy(src_data, output_dir / "delta_f1_data.csv")
            logger.info(f"  ✓ Saved: figure_3/delta_f1_data.csv")
        
        # Copy the statistical summary CSV (p-values, etc.)
        src_stats = src_dir / "delta_f1_statistical_analysis_summary.csv"
        if src_stats.exists():
            shutil.copy(src_stats, output_dir / "delta_f1_statistics.csv")
            logger.info(f"  ✓ Saved: figure_3/delta_f1_statistics.csv")
        
        return True
    
    return False


def generate_all_main_figures(logger: logging.Logger, dry_run: bool = False) -> bool:
    """Generate all main figures."""
    log_section(logger, "PHASE 2: GENERATING MAIN FIGURES")
    
    MAIN_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    results = []
    results.append(("Figure 1", generate_figure_1(logger, dry_run)))
    results.append(("Figure 2", generate_figure_2(logger, dry_run)))
    results.append(("Figure 3", generate_figure_3(logger, dry_run)))
    
    # Summary
    logger.info("")
    success_count = sum(1 for _, s in results if s)
    logger.info(f"Main figures: {success_count}/{len(results)} generated successfully")
    
    return all(s for _, s in results)


# =============================================================================
# Table Generation
# =============================================================================

def generate_table_1(logger: logging.Logger, dry_run: bool = False) -> bool:
    """Generate Table 1: Regression Analysis (F1 only)."""
    log_section(logger, "PHASE 3: GENERATING TABLE 1 (REGRESSION)")
    
    output_dir = MAIN_OUTPUT_DIR / "table_1"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Run regression analysis
    log_subsection(logger, "Running regression analysis")
    regression_script = ROOT / "analysis" / "statistics" / "regression_analysis.py"
    
    if not dry_run:
        success = run_python_script(regression_script, [], logger, dry_run=dry_run)
        if not success:
            logger.error("  ✗ Regression analysis failed")
            return False
    else:
        logger.info(f"  [DRY RUN] Would run: {regression_script.name}")
    
    # Step 2: Create formatted table (CSV)
    log_subsection(logger, "Creating formatted regression table")
    table_script = ROOT / "analysis" / "statistics" / "create_regression_tables.py"
    
    if not dry_run:
        success = run_python_script(table_script, [], logger, dry_run=dry_run)
        if not success:
            logger.error("  ✗ Table formatting failed")
            return False
    else:
        logger.info(f"  [DRY RUN] Would run: {table_script.name}")
    
    # Step 3: Create combined HTML table
    log_subsection(logger, "Creating HTML regression table")
    combined_script = ROOT / "analysis" / "statistics" / "create_combined_tables.py"
    
    if not dry_run:
        success = run_python_script(combined_script, [], logger, dry_run=dry_run)
        if not success:
            logger.warning("  ⚠ HTML table generation failed (non-critical)")
    else:
        logger.info(f"  [DRY RUN] Would run: {combined_script.name}")
    
    # Copy files to table_1 subdirectory
    if dry_run:
        logger.info(f"  [DRY RUN] Would copy regression files to table_1/")
        return True
    
    # Copy CSV files
    csv_src = RESULTS_DIR / "statistics" / "regression_table_combined.csv"
    if csv_src.exists():
        shutil.copy(csv_src, output_dir / "regression_f1.csv")
        logger.info(f"  ✓ Saved: table_1/regression_f1.csv")
    
    bonf_csv_src = RESULTS_DIR / "statistics" / "all_coefficients_bonferroni.csv"
    if bonf_csv_src.exists():
        shutil.copy(bonf_csv_src, output_dir / "regression_f1_bonferroni.csv")
        logger.info(f"  ✓ Saved: table_1/regression_f1_bonferroni.csv")
    
    # Copy HTML file (the main visual table)
    html_src = RESULTS_DIR / "statistics" / "combined_regression_f1_score_bonferroni.html"
    if html_src.exists():
        shutil.copy(html_src, output_dir / "regression_f1_bonferroni.html")
        logger.info(f"  ✓ Saved: table_1/regression_f1_bonferroni.html")
    else:
        logger.warning(f"  ⚠ HTML table not found: {html_src}")
    
    return True


# =============================================================================
# Supplementary Figures
# =============================================================================

def generate_supplementary_figures(
    experiment_results: Dict[str, Path],
    logger: logging.Logger,
    dry_run: bool = False
) -> bool:
    """Generate all 9 supplementary figures (3 families × 3 tasks)."""
    log_section(logger, "PHASE 4: GENERATING SUPPLEMENTARY FIGURES")
    
    SUPP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Family-specific scripts
    family_scripts = {
        "gemma": ROOT / "analysis" / "comparative_analysis" / "gemma_version_facet_plot.py",
        "llama": ROOT / "analysis" / "comparative_analysis" / "llama_version_facet_plot.py",
        "qwen": ROOT / "analysis" / "comparative_analysis" / "qwen_version_facet_plot.py",
    }
    
    results = []
    
    for task_name, task_config in TASKS.items():
        for family in MODEL_FAMILIES:
            log_subsection(logger, f"{family.title()} - {task_name.replace('_', ' ').title()}")
            
            # Find the comprehensive_metrics.csv for this task
            # Look in the most recent experiment output directory
            task_type = task_name
            results_base = RESULTS_DIR / "individual_prediction_performance" / task_type
            
            if not results_base.exists():
                logger.warning(f"  ⚠ Results directory not found: {results_base}")
                results.append(False)
                continue
            
            # Find most recent timestamped directory
            task_dirs = sorted(results_base.glob("*"), reverse=True)
            metrics_csv = None
            
            for task_dir in task_dirs:
                candidate = task_dir / "tables" / "comprehensive_metrics.csv"
                if candidate.exists():
                    metrics_csv = candidate
                    break
            
            if metrics_csv is None:
                logger.warning(f"  ⚠ comprehensive_metrics.csv not found for {task_name}")
                results.append(False)
                continue
            
            logger.info(f"  Using: {metrics_csv.parent.parent.name}/tables/comprehensive_metrics.csv")
            
            # Output path
            output_path = SUPP_OUTPUT_DIR / f"supp_fig_{family}_{task_name}.png"
            
            # Run family-specific script
            script = family_scripts[family]
            args = [
                "--metrics-csv", str(metrics_csv),
                "--output", str(output_path),
                "--title", f"{family.title()} Family - {task_name.replace('_', ' ').title()}"
            ]
            
            if dry_run:
                logger.info(f"  [DRY RUN] Would generate: {output_path.name}")
                results.append(True)
            else:
                success = run_python_script(script, args, logger, dry_run=dry_run)
                if success and output_path.exists():
                    logger.info(f"  ✓ Saved: {output_path.name}")
                    results.append(True)
                else:
                    logger.warning(f"  ⚠ Failed to generate: {output_path.name}")
                    results.append(False)
    
    # Summary
    logger.info("")
    success_count = sum(results)
    total_count = len(results)
    logger.info(f"Supplementary figures: {success_count}/{total_count} generated successfully")
    
    return all(results)


# =============================================================================
# Update Combined Results CSV
# =============================================================================

def update_combined_results(logger: logging.Logger, dry_run: bool = False) -> bool:
    """Update the all_models_all_tasks.csv with latest results."""
    log_subsection(logger, "Updating combined results CSV")
    
    script = ROOT / "analysis" / "combine_results.py"
    
    if dry_run:
        logger.info(f"  [DRY RUN] Would run: {script.name}")
        return True
    
    # We need to update combine_results.py with the latest paths first
    # For now, just run it and hope the paths are correct
    success = run_python_script(script, [], logger, dry_run=dry_run)
    
    if success:
        logger.info("  ✓ Updated: data/inputs/model_results/all_models_all_tasks.csv")
    else:
        logger.warning("  ⚠ Failed to update combined results")
    
    return success


# =============================================================================
# Main Pipeline
# =============================================================================

def run_pipeline(args: argparse.Namespace) -> int:
    """Run the complete paper pipeline."""
    
    # Setup - put log in the output directory
    MAIN_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    log_file = MAIN_OUTPUT_DIR / "pipeline.log"
    
    logger = setup_logging(log_file)
    
    # Header
    logger.info("")
    logger.info("╔══════════════════════════════════════════════════════════════════════╗")
    logger.info("║                    PAPER PIPELINE - FIGURE & TABLE GENERATION        ║")
    logger.info("╚══════════════════════════════════════════════════════════════════════╝")
    logger.info("")
    logger.info(f"  Timestamp:  {RUN_TIMESTAMP}")
    logger.info(f"  Log file:   {log_file}")
    logger.info(f"  Dry run:    {args.dry_run}")
    logger.info(f"  Output:     {MAIN_OUTPUT_DIR}")
    logger.info("")
    
    if args.dry_run:
        logger.info("  *** DRY RUN MODE - No changes will be made ***")
    
    success = True
    experiment_results = {}
    
    # Phase 1: Run experiments (unless skipped)
    if not args.skip_experiments:
        experiment_results = run_all_experiments(logger, args.dry_run)
        if not experiment_results and not args.dry_run:
            logger.error("No experiments completed successfully")
            success = False
    else:
        logger.info("")
        logger.info("⏭  Skipping experiments (--skip-experiments)")
    
    # Phase 2 & 3: Generate figures and table
    if not args.table_only:
        if not generate_all_main_figures(logger, args.dry_run):
            success = False
    else:
        logger.info("")
        logger.info("⏭  Skipping figures (--table-only)")
    
    if not args.figures_only:
        if not generate_table_1(logger, args.dry_run):
            success = False
    else:
        logger.info("")
        logger.info("⏭  Skipping table (--figures-only)")
    
    # Phase 4: Supplementary figures
    if not args.table_only and not args.skip_supplementary:
        if not generate_supplementary_figures(experiment_results, logger, args.dry_run):
            success = False
    else:
        logger.info("")
        logger.info("⏭  Skipping supplementary figures")
    
    # Summary
    log_section(logger, "PIPELINE COMPLETE")
    
    logger.info("")
    logger.info(f"  Main figures:   {MAIN_OUTPUT_DIR}")
    logger.info(f"  Supplementary:  {SUPP_OUTPUT_DIR}")
    logger.info(f"  Log file:       {log_file}")
    logger.info("")
    
    if success:
        logger.info("✓ Pipeline completed successfully")
        return 0
    else:
        logger.warning("⚠ Pipeline completed with some failures - check logs")
        return 1


def main():
    parser = argparse.ArgumentParser(
        description="Generate all figures and tables for paper publication",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "--skip-experiments", 
        action="store_true",
        help="Skip running experiments, assume results exist"
    )
    parser.add_argument(
        "--skip-supplementary",
        action="store_true", 
        help="Skip generating supplementary figures"
    )
    parser.add_argument(
        "--figures-only",
        action="store_true",
        help="Only generate figures, skip table"
    )
    parser.add_argument(
        "--table-only",
        action="store_true",
        help="Only generate table, skip figures"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without executing"
    )
    
    args = parser.parse_args()
    
    return run_pipeline(args)


if __name__ == "__main__":
    sys.exit(main())

