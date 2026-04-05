#!/usr/bin/env python3
"""
Paper Pipeline - Generate All Figures and Tables for Manuscript Revisions

This script orchestrates the complete pipeline for generating all figures
and tables needed for the paper: Evaluating the effect of mental health 
fine-tuning relative to other model characteristics on LLM safety performance

1. Run experiments for all 3 tasks (Suicidal Ideation, Therapy Request, Therapy Engagement)
   - Uses cached results where available
   - Retries api_error entries automatically (include_errors=False in cache check)
2. Generate main figures (Figure 1, 2, 3)
3. Generate main table (Table 1 - Multivariable Regression with Bonferroni correction)
4. Generate supplementary figures (9 family×task facet plots; ΔF1 vs ΔParse Success (1))
5. Generate revision outputs (Figure S10 scatter, delta-parse facet, P2 agreement, revised Table S2)

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
        revision_figures/
            figure_s10_delta_parse_vs_delta_f1.png
            delta_parse_facet_plot.png
        revision_data/
            p2_agreement_given_p1_exact_match.csv
            revised_table_s2.csv
        data/
            all_models_all_tasks.csv
            comprehensive_metrics_*.csv
            raw_responses/*.tar.gz

Usage:
    python run_paper_pipeline.py [--skip-experiments] [--figures-only] [--table-only]
        [--dry-run] [--si-dir DIR --tr-dir DIR --te-dir DIR]
        [--use-latest-experiment-dirs]

    Options:
        --skip-experiments    Skip running experiments; then require explicit dirs or
                              --use-latest-experiment-dirs (non-dry-run).
        --si-dir, --tr-dir, --te-dir   Per-task experiment output dirs (contain tables/).
        --use-latest-experiment-dirs   Opt-in: newest run per task under results/.
        --figures-only        Only generate figures, skip table
        --table-only          Only generate table, skip figures
        --dry-run             Show what would be done without executing

Author: Mark Kalinich (with significant assistance from Cursor models)
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
import csv

from analysis.combine_results import get_latest_experiment_dir
from utilities.paper_run_provenance import write_paper_run_provenance

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


def resolve_task_experiment_dirs(
    args: argparse.Namespace,
    experiment_results: Dict[str, Path],
    logger: logging.Logger,
) -> Optional[Dict[str, Path]]:
    """
    Map each task name to its experiment output directory (contains tables/).

    Resolution order: Phase 1 outputs → explicit --si-dir/--tr-dir/--te-dir →
    --use-latest-experiment-dirs → in dry-run only, newest dir per task for logging.
    """
    base = RESULTS_DIR / "individual_prediction_performance"
    task_keys = list(TASKS.keys())

    if experiment_results and all(experiment_results.get(k) is not None for k in task_keys):
        out: Dict[str, Path] = {}
        for k in task_keys:
            p = experiment_results[k]
            if not p.is_absolute():
                p = ROOT / p
            out[k] = p.resolve()
        return out

    si, tr, te = getattr(args, "si_dir", None), getattr(args, "tr_dir", None), getattr(args, "te_dir", None)
    if si and tr and te:
        return {
            "suicidal_ideation": Path(si).resolve(),
            "therapy_request": Path(tr).resolve(),
            "therapy_engagement": Path(te).resolve(),
        }

    if getattr(args, "use_latest_experiment_dirs", False):
        return {
            "suicidal_ideation": get_latest_experiment_dir(base, "suicidal_ideation"),
            "therapy_request": get_latest_experiment_dir(base, "therapy_request"),
            "therapy_engagement": get_latest_experiment_dir(base, "therapy_engagement"),
        }

    if args.dry_run:
        try:
            return {
                "suicidal_ideation": get_latest_experiment_dir(base, "suicidal_ideation"),
                "therapy_request": get_latest_experiment_dir(base, "therapy_request"),
                "therapy_engagement": get_latest_experiment_dir(base, "therapy_engagement"),
            }
        except FileNotFoundError:
            logger.warning("  [DRY RUN] No experiment directories found under results/")
            return None

    return None


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
        else:
            logger.warning(f"  ⚠ Output not found: {src}")
            return False
        
        # Include the source data CSV used to generate Figure 1
        config_csv = ROOT / "config" / "models_config.csv"
        if config_csv.exists():
            shutil.copy(config_csv, output_dir / "models_config.csv")
            logger.info(f"  ✓ Saved: figure_1/models_config.csv (source data)")
        
        return True
    
    return False


def _build_figure2_params_summary(
    supp_dir: Path, output_dir: Path, logger: logging.Logger,
) -> None:
    """Extract F1-vs-params regression rows with ×9 Bonferroni into a summary CSV."""
    import pandas as pd
    src = supp_dir / "fig2_regression_statistics.csv"
    if not src.exists():
        logger.warning("  ⚠ fig2_regression_statistics.csv not found; skipping summary")
        return
    df = pd.read_csv(src)
    sub = df[(df["plot_type"] == "f1_vs_params_overall_trend") &
             (df["trendline_type"] == "overall")].copy()
    if sub.empty:
        return
    N_BONF = 9
    sub["p_adjusted"] = (sub["p_value"] * N_BONF).clip(upper=1.0)
    sub["significant_bonferroni"] = sub["p_adjusted"] < 0.05
    out = sub[["family", "task", "n_points", "r_squared", "slope",
               "p_value", "p_adjusted", "significant_bonferroni"]].copy()
    out["r_squared"] = out["r_squared"].round(4)
    out["slope"] = out["slope"].round(4)
    dst = output_dir / "figure_2_f1_vs_params_summary.csv"
    out.to_csv(dst, index=False)
    logger.info(f"  ✓ Saved: figure_2/{dst.name}")


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
        plots = list(output_dir.glob("*.png"))
        
        if plots:
            # The main figure stays in figure_2/; everything else moves to supplemental_plots/
            main_plot_name = "fig2_f1_vs_params_overall_trend.png"
            main_plot = output_dir / main_plot_name
            if main_plot.exists():
                logger.info(f"  ✓ Main figure: figure_2/{main_plot.name}")
            
            supp_dir = output_dir / "supplemental_plots"
            supp_dir.mkdir(exist_ok=True)
            for f in sorted(output_dir.iterdir()):
                if f.is_file() and f.name != main_plot_name:
                    shutil.move(str(f), supp_dir / f.name)
                    logger.info(f"      → supplemental_plots/{f.name}")
            
            _build_figure2_params_summary(supp_dir, output_dir, logger)
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

def _build_f1_bonferroni_table(all_coeff_path: Path, output_path: Path,
                               logger: logging.Logger) -> bool:
    """Build the main Table 1 CSV: F1-only, Bonferroni-corrected.

    Output columns: Variable, SI-β, SI-95% CI, TR-β, TR-95% CI, TE-β, TE-95% CI
    Asterisks on β only; CI as [lower, upper] in a single cell.
    Fit statistics (R², Adj R², N) appended as bottom rows.
    """
    import pandas as pd

    df = pd.read_csv(all_coeff_path)
    f1 = df[df["DV"] == "F1 Score"].copy()
    if f1.empty:
        logger.error("  ✗ No F1 Score rows in all_coefficients.csv")
        return False

    TASK_ORDER = ["Suicidal Ideation", "Therapy Request", "Therapy Engagement"]
    TASK_SHORT = {"Suicidal Ideation": "SI", "Therapy Request": "TR",
                  "Therapy Engagement": "TE"}
    VAR_ORDER = [
        "Intercept", "Version: 2", "Version: 3", "Version: 4",
        "Parameter Size (B)",
        "Fine-Tune Type: Instruction-Tuned",
        "Fine-Tune Type: Mental Health Tuned",
        "Fine-Tune Type: Medical-Tuned",
        "Fine-Tune Type: Safety-Tuned",
        "Family: LLaMA", "Family: Qwen",
    ]

    def _stars(p: float) -> str:
        if p < 0.001:
            return "***"
        if p < 0.01:
            return "**"
        if p < 0.05:
            return "*"
        return ""

    rows = []
    for var in VAR_ORDER:
        row = {"Variable": var}
        for task in TASK_ORDER:
            t = TASK_SHORT[task]
            sub = f1[(f1["Task"] == task) & (f1["Variable"] == var)]
            if sub.empty:
                row[f"{t}-β"] = ""
                row[f"{t}-95% CI"] = ""
                continue
            r = sub.iloc[0]
            stars = _stars(r["p_bonferroni"])
            row[f"{t}-β"] = f"{r['β']:.3f}{stars}"
            row[f"{t}-95% CI"] = f"[{r['Bonf CI Lower']:.3f}, {r['Bonf CI Upper']:.3f}]"
        rows.append(row)

    for stat_name, col_name in [("R²", "R²"), ("Adj R²", "Adj R²"), ("N", "N")]:
        row = {"Variable": stat_name}
        for task in TASK_ORDER:
            t = TASK_SHORT[task]
            sub = f1[f1["Task"] == task].iloc[0]
            if stat_name == "N":
                row[f"{t}-β"] = f"{int(sub[col_name])}"
            else:
                row[f"{t}-β"] = f"{sub[col_name]:.3f}"
            row[f"{t}-95% CI"] = ""
        rows.append(row)

    out_df = pd.DataFrame(rows)
    col_order = ["Variable"]
    for t in TASK_SHORT.values():
        col_order += [f"{t}-β", f"{t}-95% CI"]
    out_df = out_df[col_order]
    out_df.to_csv(output_path, index=False)
    return True


def generate_table_1(logger: logging.Logger, dry_run: bool = False) -> bool:
    """Generate Table 1: Regression Analysis (F1 only)."""
    log_section(logger, "PHASE 3: GENERATING TABLE 1 (REGRESSION)")
    
    output_dir = MAIN_OUTPUT_DIR / "table_1"
    output_dir.mkdir(parents=True, exist_ok=True)
    supp_data_dir = output_dir / "supplemental_data"
    supp_data_dir.mkdir(exist_ok=True)
    
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
    
    # Step 2: Create formatted tables (CSV + HTML)
    log_subsection(logger, "Creating formatted regression tables")
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
    
    if dry_run:
        logger.info(f"  [DRY RUN] Would copy regression files to table_1/")
        return True
    
    # ── Main table: F1-only, Bonferroni-corrected, split columns ──
    log_subsection(logger, "Building F1 Bonferroni table (split columns)")
    all_coeff_src = RESULTS_DIR / "statistics" / "all_coefficients.csv"
    if all_coeff_src.exists():
        main_csv = output_dir / "multivariable_regression_f1_bonferroni.csv"
        ok = _build_f1_bonferroni_table(all_coeff_src, main_csv, logger)
        if ok:
            logger.info(f"  ✓ Saved: table_1/{main_csv.name}")
        else:
            logger.warning(f"  ⚠ Failed to build F1 Bonferroni table")
    else:
        logger.warning(f"  ⚠ Source not found: {all_coeff_src}")
    
    # ── Supplemental data ──
    # Full Bonferroni long-form results (all DVs) → supplemental_data/
    bonf_src = RESULTS_DIR / "statistics" / "regression_table_combined_bonferroni.csv"
    if bonf_src.exists():
        shutil.copy(bonf_src, supp_data_dir / "all_regressions_all_results.csv")
        logger.info(f"  ✓ Saved: table_1/supplemental_data/all_regressions_all_results.csv")
    else:
        alt_src = RESULTS_DIR / "statistics" / "all_coefficients_bonferroni.csv"
        if alt_src.exists():
            shutil.copy(alt_src, supp_data_dir / "all_regressions_all_results.csv")
            logger.info(f"  ✓ Saved: table_1/supplemental_data/all_regressions_all_results.csv")
    
    # HTML table → supplemental_data/
    html_src = RESULTS_DIR / "statistics" / "combined_regression_f1_score_bonferroni.html"
    if html_src.exists():
        shutil.copy(html_src, supp_data_dir / "all_regressions_all_results.html")
        logger.info(f"  ✓ Saved: table_1/supplemental_data/all_regressions_all_results.html")
    else:
        logger.warning(f"  ⚠ HTML table not found: {html_src}")
    
    return True


# =============================================================================
# Supplementary Figures
# =============================================================================

def generate_supplementary_figures(
    task_dirs: Dict[str, Path],
    logger: logging.Logger,
    dry_run: bool = False
) -> bool:
    """Generate all 9 supplementary figures (3 families × 3 tasks).

    task_dirs maps task name (e.g. suicidal_ideation) → experiment output directory
    (the folder that contains tables/comprehensive_metrics.csv).
    """
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
            
            exp_dir = task_dirs.get(task_name) if task_dirs else None
            if exp_dir is None:
                logger.error(f"  ✗ No experiment directory resolved for task {task_name}")
                results.append(False)
                continue
            
            metrics_csv = exp_dir / "tables" / "comprehensive_metrics.csv"
            if not metrics_csv.exists():
                logger.warning(f"  ⚠ comprehensive_metrics.csv not found: {metrics_csv}")
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
    
    # Move PDFs into a pdf_versions/ subdirectory
    if not dry_run:
        pdf_files = list(SUPP_OUTPUT_DIR.glob("*.pdf"))
        if pdf_files:
            pdf_dir = SUPP_OUTPUT_DIR / "pdf_versions"
            pdf_dir.mkdir(exist_ok=True)
            for pdf in pdf_files:
                shutil.move(str(pdf), pdf_dir / pdf.name)
            logger.info(f"  ✓ Moved {len(pdf_files)} PDFs → supplementary_figures/pdf_versions/")
    
    # Summary
    logger.info("")
    success_count = sum(results)
    total_count = len(results)
    logger.info(f"Supplementary figures: {success_count}/{total_count} generated successfully")
    
    return all(results)


def generate_revision_outputs(
    logger: logging.Logger,
    dry_run: bool = False,
) -> bool:
    """Generate revision-era figures and data (Figure S10, delta-parse facet,
    P2 agreement, revised Table S2).

    These do not require per-task experiment dirs; they read from the combined CSV
    and intermediate psychiatrist score files.
    """
    log_section(logger, "PHASE 5: GENERATING REVISION OUTPUTS")

    revision_out = PAPER_FIGURES_BASE / "revision_figures"
    revision_out.mkdir(parents=True, exist_ok=True)
    revision_data_out = PAPER_FIGURES_BASE / "revision_data"
    revision_data_out.mkdir(parents=True, exist_ok=True)

    results = []

    # --- Figure S10: delta parse vs delta F1 scatter ---
    log_subsection(logger, "Figure S10: Δ parse vs Δ F1 scatter")
    scatter_script = ROOT / "analysis" / "revision" / "delta_parse_vs_delta_f1_scatter.py"
    if dry_run:
        logger.info("  [DRY RUN] Would generate delta_parse_vs_delta_f1_scatter")
        results.append(True)
    else:
        scatter_ok = run_python_script(scatter_script, [], logger)
        src_png = ROOT / "results" / "revision_experiments" / "delta_parse_vs_delta_f1_scatter.png"
        if scatter_ok and src_png.exists():
            dst = revision_out / "figure_s10_delta_parse_vs_delta_f1.png"
            shutil.copy(src_png, dst)
            logger.info(f"  ✓ Saved: revision_figures/{dst.name}")
            results.append(True)
        else:
            logger.warning("  ⚠ Failed to generate Figure S10 scatter")
            results.append(False)

    # --- Delta parse facet plot (revision supplement) ---
    log_subsection(logger, "Delta parse success facet plot")
    facet_script = ROOT / "analysis" / "combined_finetune_facet_plot.py"
    if dry_run:
        logger.info("  [DRY RUN] Would generate delta parse facet plot")
        results.append(True)
    else:
        facet_ok = run_python_script(facet_script, ["--metric", "parse"], logger)
        src_png = ROOT / "results" / "revision_experiments" / "delta_parse_facet_plot_across_all_models_and_tasks.png"
        if facet_ok and src_png.exists():
            dst = revision_out / "delta_parse_facet_plot.png"
            shutil.copy(src_png, dst)
            logger.info(f"  ✓ Saved: revision_figures/{dst.name}")
            results.append(True)
        else:
            logger.warning("  ⚠ Failed to generate delta parse facet plot")
            results.append(False)

    # --- P2 agreement (interrater reliability, cited in manuscript) ---
    log_subsection(logger, "P2 agreement proportions")
    p2_script = ROOT / "analysis" / "revision" / "compute_p2_agreement.py"
    if dry_run:
        logger.info("  [DRY RUN] Would generate P2 agreement CSV")
        results.append(True)
    else:
        p2_ok = run_python_script(p2_script, [], logger)
        src_csv = (ROOT / "results" / "revision_experiments"
                   / "interrater_reliability" / "p2_agreement_given_p1_exact_match.csv")
        if p2_ok and src_csv.exists():
            dst = revision_data_out / "p2_agreement_given_p1_exact_match.csv"
            shutil.copy(src_csv, dst)
            logger.info(f"  ✓ Saved: revision_data/{dst.name}")
            results.append(True)
        else:
            logger.warning("  ⚠ Failed to generate P2 agreement CSV")
            results.append(False)

    # --- Revised Table S2 (copy into pipeline output) ---
    log_subsection(logger, "Revised Table S2")
    table_s2_src = ROOT / "results" / "revision_experiments" / "fine_tune_subset_analysis" / "revised_table_s2.csv"
    if dry_run:
        logger.info("  [DRY RUN] Would copy revised_table_s2.csv")
        results.append(True)
    else:
        if table_s2_src.exists():
            shutil.copy(table_s2_src, revision_data_out / "revised_table_s2.csv")
            logger.info(f"  ✓ Saved: revision_data/revised_table_s2.csv")
            results.append(True)
        else:
            logger.warning(f"  ⚠ Not found: {table_s2_src}")
            results.append(False)

    success_count = sum(results)
    logger.info(f"\nRevision outputs: {success_count}/{len(results)} generated successfully")
    return all(results)


# =============================================================================
# Update Combined Results CSV
# =============================================================================

def update_combined_results(
    logger: logging.Logger,
    task_dirs: Optional[Dict[str, Path]] = None,
    dry_run: bool = False,
) -> bool:
    """Update data/inputs/model_results/all_models_all_tasks.csv via combine_results.py."""
    log_subsection(logger, "Updating combined results CSV")
    
    script = ROOT / "analysis" / "combine_results.py"
    
    if dry_run:
        if task_dirs:
            logger.info(f"  [DRY RUN] Would run: {script.name} with explicit SI/TR/TE dirs")
            logger.debug(f"    SI: {task_dirs['suicidal_ideation']}")
            logger.debug(f"    TR: {task_dirs['therapy_request']}")
            logger.debug(f"    TE: {task_dirs['therapy_engagement']}")
        else:
            logger.info(f"  [DRY RUN] Would run: {script.name}")
        return True
    
    if not task_dirs:
        logger.error("  combine_results: no task directories (internal error)")
        return False
    
    extra = [
        "--si-dir", str(task_dirs["suicidal_ideation"]),
        "--tr-dir", str(task_dirs["therapy_request"]),
        "--te-dir", str(task_dirs["therapy_engagement"]),
    ]
    success = run_python_script(script, extra, logger, dry_run=dry_run)
    
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
    logger.info("  Pinned task inputs (hardcoded — not configurable via CLI):")
    for task_name, task_cfg in TASKS.items():
        logger.info(f"    {task_cfg['short_name']}  statements: {task_cfg['input_data']}")
        logger.info(f"    {task_cfg['short_name']}  prompt:     {task_cfg['prompt_file']}")
    logger.info(f"    Models config: config/models_config.csv")
    logger.info("")
    
    if args.dry_run:
        logger.info("  *** DRY RUN MODE - No changes will be made ***")
    
    exit_code = 0
    success = True
    experiment_results: Dict[str, Optional[Path]] = {}
    task_dirs: Optional[Dict[str, Path]] = None

    try:
        # Phase 1: Run experiments (unless skipped)
        if not args.skip_experiments:
            experiment_results = run_all_experiments(logger, args.dry_run)
            if not experiment_results and not args.dry_run:
                logger.error("No experiments completed successfully")
                success = False
        else:
            logger.info("")
            logger.info("⏭  Skipping experiments (--skip-experiments)")
        
        need_combine = (not args.table_only) or (not args.figures_only)
        need_supp = not args.skip_supplementary
        need_task_dirs = need_combine or need_supp

        task_dirs = resolve_task_experiment_dirs(args, experiment_results, logger)

        if need_task_dirs and not args.dry_run and task_dirs is None:
            logger.error(
                "Cannot resolve experiment directories for combine_results and/or supplementary figures. "
                "Options: (1) Run Phase 1 without --skip-experiments, or "
                "(2) --si-dir, --tr-dir, --te-dir (each: .../individual_prediction_performance/<task>/<run_id>), or "
                "(3) --use-latest-experiment-dirs (explicit opt-in to newest run per task)."
            )
            exit_code = 1
            return exit_code

        # Phase 1b: refresh combined CSV (needed for main figures and Table 1)
        if need_combine:
            if not update_combined_results(logger, task_dirs, dry_run=args.dry_run):
                success = False

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
            if task_dirs is None:
                if args.dry_run:
                    logger.info("⏭  [DRY RUN] Skipping supplementary figures (no experiment dirs)")
                else:
                    logger.error("No experiment directories for supplementary figures")
                    success = False
            elif not generate_supplementary_figures(task_dirs, logger, args.dry_run):
                success = False
        else:
            logger.info("")
            logger.info("⏭  Skipping supplementary figures")

        # Phase 5: Revision outputs (figures + data)
        if not args.table_only and not args.skip_supplementary:
            if not generate_revision_outputs(logger, args.dry_run):
                success = False
        else:
            logger.info("")
            logger.info("⏭  Skipping revision figures")

        # Summary
        log_section(logger, "PIPELINE COMPLETE")
        
        logger.info("")
        logger.info(f"  Main figures:   {MAIN_OUTPUT_DIR}")
        logger.info(f"  Supplementary:  {SUPP_OUTPUT_DIR}")
        logger.info(f"  Log file:       {log_file}")
        logger.info("")
        
        if success:
            logger.info("✓ Pipeline completed successfully")
            exit_code = 0
        else:
            logger.warning("⚠ Pipeline completed with some failures - check logs")
            exit_code = 1
        return exit_code
    finally:
        if not getattr(args, "no_provenance", False):
            try:
                ppath = write_paper_run_provenance(
                    repo_root=ROOT,
                    run_timestamp=RUN_TIMESTAMP,
                    output_dir=MAIN_OUTPUT_DIR,
                    args=args,
                    task_dirs=task_dirs,
                    experiment_results=experiment_results,
                    exit_code=exit_code,
                    tasks_config=TASKS,
                )
                logger.info(f"  Provenance:     {ppath}")
            except Exception as e:
                logger.warning(f"  Could not write PROVENANCE.json: {e}")


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
    parser.add_argument(
        "--si-dir",
        type=str,
        default=None,
        help="Experiment output dir for SI (contains tables/). Required with --skip-experiments unless --use-latest-experiment-dirs or Phase 1 runs.",
    )
    parser.add_argument(
        "--tr-dir",
        type=str,
        default=None,
        help="Experiment output dir for TR (contains tables/).",
    )
    parser.add_argument(
        "--te-dir",
        type=str,
        default=None,
        help="Experiment output dir for TE (contains tables/).",
    )
    parser.add_argument(
        "--use-latest-experiment-dirs",
        action="store_true",
        help="Use newest timestamped run per task under results/individual_prediction_performance/ (explicit opt-in).",
    )
    parser.add_argument(
        "--no-provenance",
        action="store_true",
        help="Do not write PROVENANCE.json (machine run record) in the run output directory.",
    )
    
    args = parser.parse_args()
    
    return run_pipeline(args)


if __name__ == "__main__":
    sys.exit(main())

