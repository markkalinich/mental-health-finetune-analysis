#!/usr/bin/env python3
"""
Multivariable Linear Regression Analysis for LLM Classification Performance

Analyzes the impact of model characteristics on classification performance
across three mental health classification tasks:
- Suicidal ideation detection
- Therapy request detection  
- Therapy engagement detection

Input variables:
- Model family (categorical nominal: Qwen, LLaMA, Gemma)
- Version (categorical ordinal: 1, 2, 3, 4)
- Parameter size (continuous, in billions)
- Fine-Tune Type (categorical nominal: Base Model, Instruction-Tuned, Mental Health, etc.)

Output variables:
- F1 score
- Accuracy

Data source: data/inputs/model_results/all_models_all_tasks.csv
Safety model corrections: Applied from facet_plot_utils.py
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
from scipy import stats as scipy_stats
from pathlib import Path
from typing import Dict, Tuple, Optional
import sys
import warnings
warnings.filterwarnings('ignore')


# === CONFIGURATION ===

ROOT = Path(__file__).parent.parent.parent
CONFIG_PATH = ROOT / "config" / "models_config.csv"
ALL_MODELS_PATH = ROOT / "data" / "inputs" / "model_results" / "all_models_all_tasks.csv"

# Family mapping (from model_coverage_heatmap.py)
FAMILY_TO_PARENT = {
    # Gemma family
    "gemma": "Gemma", "gemma1": "Gemma", "gemma2": "Gemma", "gemma3n": "Gemma",
    "medgemma": "Gemma", "shieldgemma": "Gemma", 
    "mental_health": "Gemma", "gemma_therapy": "Gemma",
    # Qwen family
    "qwen": "Qwen", "qwen1.5": "Qwen", "qwen2": "Qwen",
    "qwen_medical": "Qwen", "qwen_mental_health": "Qwen", "qwen_guard": "Qwen",
    # LLaMA family
    "llama1": "LLaMA", "llama2": "LLaMA", "llama3": "LLaMA",
    "llama3.1": "LLaMA", "llama3.2": "LLaMA", "llama3.3": "LLaMA", "llama4": "LLaMA",
    "llama_medical": "LLaMA", "llama_mental_health": "LLaMA", 
    "llama_therapy": "LLaMA", "llama_guard": "LLaMA",
}

# Model type mapping (consolidate to key categories)
MODEL_TYPE_MAP = {
    "PT": "Base Model",
    "IT": "Instruction-Tuned", 
    "Mental Health": "Mental Health Tuned",
    "MedGemma": "Medical-Tuned",
    "Medical": "Medical-Tuned",
    "ShieldGemma": "Safety-Tuned",
    "Guard": "Safety-Tuned",
}


# === DATA LOADING ===

def get_version_ordinal(row: pd.Series) -> Optional[int]:
    """
    Map model version to ordinal version category (1, 2, 3, 4).
    """
    version = row.get("version", None)
    architecture = row.get("architecture", "")
    
    if pd.isna(version):
        return None
    
    # Handle Gemma 3n explicitly
    if architecture == "gemma3n" or "3n" in str(row.get("family", "")):
        return 4
    
    try:
        v = float(version)
        if v < 2:
            return 1
        elif v < 3:
            return 2
        elif v < 4:
            return 3
        else:
            return 4
    except (ValueError, TypeError):
        return None


def load_config() -> pd.DataFrame:
    """Load and preprocess model configuration."""
    df = pd.read_csv(CONFIG_PATH)
    
    # Filter to enabled models only
    df = df[df["enabled"] == True].copy()
    
    # Map to parent family
    df["parent_family"] = df["family"].map(FAMILY_TO_PARENT)
    
    # Filter to only Qwen, LLaMA, Gemma
    df = df[df["parent_family"].isin(["Qwen", "LLaMA", "Gemma"])].copy()
    
    # Get version ordinal
    df["version_ordinal"] = df.apply(get_version_ordinal, axis=1)
    
    # Map fine-tune type
    df["finetune_type"] = df["model_type"].map(MODEL_TYPE_MAP).fillna("Other")
    
    # Ensure param_billions is numeric
    df["param_billions"] = pd.to_numeric(df["param_billions"], errors="coerce")
    
    return df


def load_all_models_data() -> pd.DataFrame:
    """Load all models performance data.

    Guard model metrics are now computed correctly in Phase 2
    (data_loader re-parses their native output format), so no
    post-hoc corrections are needed here.
    """
    print("Loading performance data from all_models_all_tasks.csv...")
    results_df = pd.read_csv(ALL_MODELS_PATH)
    print(f"  Loaded {len(results_df)} rows")
    
    return results_df


def prepare_regression_data(results_df: pd.DataFrame, config_df: pd.DataFrame, task: str) -> pd.DataFrame:
    """
    Prepare data for regression analysis for a specific task.
    """
    # Filter to specific task
    task_df = results_df[results_df['task'] == task].copy()
    
    # Merge with config
    merged = task_df.merge(
        config_df[["family", "size", "parent_family", "version_ordinal", 
                   "param_billions", "finetune_type"]],
        left_on=["model_family", "model_size"],
        right_on=["family", "size"],
        how="inner"
    )
    
    # Drop rows with missing key variables
    merged = merged.dropna(subset=["parent_family", "version_ordinal", "param_billions", 
                                    "f1_score", "accuracy", "finetune_type"])
    
    # Exclude "Other" finetune types
    merged = merged[merged["finetune_type"] != "Other"]
    
    # Rename for clarity in regression output
    merged = merged.rename(columns={"version_ordinal": "version"})
    
    return merged


# === REGRESSION ANALYSIS ===

def run_regression(df: pd.DataFrame, dv: str = "f1_score") -> sm.regression.linear_model.RegressionResultsWrapper:
    """
    Run multivariable linear regression with robust standard errors.
    
    Uses HC3 heteroscedasticity-consistent (robust) standard errors.
    """
    formula = f"{dv} ~ C(parent_family) + C(version) + param_billions + C(finetune_type)"
    model = smf.ols(formula, data=df).fit(cov_type='HC3')
    return model


def create_coefficient_table(model, task_name: str, dv: str) -> pd.DataFrame:
    """
    Create a standard regression coefficient table with multiple testing corrections.
    
    Includes:
    - Raw p-values
    - Bonferroni-corrected p-values
    - FDR-corrected p-values (Benjamini-Hochberg)
    - 95% CI (raw)
    - Bonferroni-adjusted CI (wider, more conservative)
    """
    n_tests = len(model.params)
    p_values = [model.pvalues[var_name] for var_name in model.params.index]
    
    # Bonferroni correction for p-values
    p_bonf = [min(p * n_tests, 1.0) for p in p_values]
    
    # FDR correction (Benjamini-Hochberg)
    _, p_fdr, _, _ = multipletests(p_values, method='fdr_bh')
    
    # Get raw confidence intervals (95% CI, α = 0.05)
    conf_int_raw = model.conf_int(alpha=0.05)
    
    # Bonferroni-adjusted confidence intervals
    # For Bonferroni: α_adjusted = 0.05 / n_tests
    alpha_bonf = 0.05 / n_tests
    conf_int_bonf = model.conf_int(alpha=alpha_bonf)
    
    rows = []
    for i, var_name in enumerate(model.params.index):
        row = {
            "Variable": format_variable_name(var_name),
            "β": model.params[var_name],
            "SE": model.bse[var_name],
            "t": model.tvalues[var_name],
            "p": p_values[i],
            "p_bonferroni": p_bonf[i],
            "p_fdr": p_fdr[i],
            "95% CI Lower": conf_int_raw.loc[var_name, 0],
            "95% CI Upper": conf_int_raw.loc[var_name, 1],
            "Bonf CI Lower": conf_int_bonf.loc[var_name, 0],
            "Bonf CI Upper": conf_int_bonf.loc[var_name, 1],
        }
        rows.append(row)
    
    df = pd.DataFrame(rows)
    return df


def format_variable_name(raw_name: str) -> str:
    """Convert statsmodels variable names to readable format."""
    if raw_name == "Intercept":
        return "Intercept"
    
    if raw_name == "param_billions":
        return "Parameter Size (B)"
    
    if raw_name.startswith("C("):
        var_match = raw_name.replace("C(", "").split(")")[0]
        level = raw_name.split("[T.")[-1].rstrip("]")
        
        var_labels = {
            "parent_family": "Family",
            "version": "Version",
            "finetune_type": "Fine-Tune Type",
        }
        
        var_label = var_labels.get(var_match, var_match)
        return f"{var_label}: {level}"
    
    return raw_name


def format_p_value(p: float) -> str:
    """Format p-value with significance stars."""
    if p < 0.001:
        return f"{p:.4f}***"
    elif p < 0.01:
        return f"{p:.4f}**"
    elif p < 0.05:
        return f"{p:.4f}*"
    else:
        return f"{p:.4f}"


def print_coefficient_table(model, task_name: str, dv: str):
    """Print a formatted coefficient table."""
    print(f"\n{'='*100}")
    print(f"  {task_name.replace('_', ' ').upper()} - {dv.upper()}")
    print(f"  Coefficient Table")
    print(f"{'='*100}")
    
    n_tests = len(model.params)
    print(f"\n  Model Fit: R² = {model.rsquared:.4f}, Adj R² = {model.rsquared_adj:.4f}, "
          f"F({int(model.df_model)}, {int(model.df_resid)}) = {model.fvalue:.2f}, p < {model.f_pvalue:.4f}, N = {int(model.nobs)}")
    print(f"  Reference categories: Family=Gemma, Version=1, Fine-Tune Type=Base Model")
    print(f"  Multiple testing: {n_tests} tests, Bonferroni α = {0.05/n_tests:.4f}")
    print(f"\n  {'─'*100}")
    
    print(f"  {'Variable':<35} {'β':>10} {'SE':>10} {'t':>10} {'p':>14} {'95% CI':>20}")
    print(f"  {'─'*100}")
    
    conf_int = model.conf_int()
    
    for var_name in model.params.index:
        formatted_name = format_variable_name(var_name)
        beta = model.params[var_name]
        se = model.bse[var_name]
        t = model.tvalues[var_name]
        p = model.pvalues[var_name]
        ci_low = conf_int.loc[var_name, 0]
        ci_high = conf_int.loc[var_name, 1]
        
        p_str = format_p_value(p)
        ci_str = f"[{ci_low:>7.3f}, {ci_high:>7.3f}]"
        
        print(f"  {formatted_name:<35} {beta:>10.4f} {se:>10.4f} {t:>10.3f} {p_str:>14} {ci_str:>20}")
    
    print(f"  {'─'*100}")
    print(f"  Note: * p < .05, ** p < .01, *** p < .001")


def run_all_regressions() -> Dict:
    """Run regressions for all tasks and DVs."""
    
    # Load config
    print("Loading model configuration...")
    config_df = load_config()
    print(f"  Loaded {len(config_df)} enabled models from config")
    
    # Load all models data with safety corrections
    results_df = load_all_models_data()
    
    # Task mappings
    tasks = {
        "suicidal_ideation": "suicidal_ideation",
        "therapy_request": "therapy_request",
        "therapy_engagement": "therapy_engagement",
    }
    
    results = {}
    
    for task_name, task_filter in tasks.items():
        print(f"\n{'=' * 80}")
        print(f"  TASK: {task_name.replace('_', ' ').upper()}")
        print(f"{'=' * 80}")
        
        # Prepare data
        reg_df = prepare_regression_data(results_df, config_df, task_filter)
        print(f"  Models for regression: {len(reg_df)}")
        
        # Show data summary
        print(f"\n  Data summary:")
        print(f"    Parent families: {reg_df['parent_family'].value_counts().to_dict()}")
        print(f"    Versions: {sorted(reg_df['version'].unique())}")
        print(f"    Fine-Tune Types: {reg_df['finetune_type'].value_counts().to_dict()}")
        print(f"    Param range: {reg_df['param_billions'].min():.2f}B - {reg_df['param_billions'].max():.2f}B")
        
        task_results = {}
        
        # Run regressions for both DVs
        for dv in ["f1_score", "accuracy"]:
            try:
                model = run_regression(reg_df, dv)
                print_coefficient_table(model, task_name, dv)
                task_results[dv] = model
            except Exception as e:
                print(f"  ❌ Error running {dv} regression: {e}")
        
        results[task_name] = task_results
    
    return results


def create_summary_table(results: Dict) -> pd.DataFrame:
    """Create a summary table of all regression results."""
    rows = []
    
    for task_name, task_results in results.items():
        for dv, model in task_results.items():
            row = {
                "Task": task_name.replace("_", " ").title(),
                "DV": dv.replace("_", " ").title(),
                "R²": model.rsquared,
                "Adj R²": model.rsquared_adj,
                "F-stat": model.fvalue,
                "F p-value": model.f_pvalue,
                "N": int(model.nobs),
            }
            rows.append(row)
    
    return pd.DataFrame(rows)


def save_all_coefficient_tables(results: Dict, output_dir: Path):
    """Save all coefficient tables to CSV files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    all_tables = []
    
    for task_name, task_results in results.items():
        for dv, model in task_results.items():
            # Create coefficient table
            coef_df = create_coefficient_table(model, task_name, dv)
            
            # Add task and DV columns
            coef_df.insert(0, "Task", task_name.replace("_", " ").title())
            coef_df.insert(1, "DV", dv.replace("_", " ").title())
            
            # Add model fit statistics
            coef_df["R²"] = model.rsquared
            coef_df["Adj R²"] = model.rsquared_adj
            coef_df["N"] = int(model.nobs)
            
            all_tables.append(coef_df)
            
            # Save individual table
            filename = f"{task_name}_{dv}_coefficients.csv"
            coef_df.to_csv(output_dir / filename, index=False)
    
    # Save combined table
    combined_df = pd.concat(all_tables, ignore_index=True)
    combined_df.to_csv(output_dir / "all_coefficients.csv", index=False)
    
    print(f"\nCoefficient tables saved to: {output_dir}")
    print(f"  - Individual tables: [task]_[dv]_coefficients.csv")
    print(f"  - Combined table: all_coefficients.csv")
    
    # Generate FDR and FWER summary tables
    save_correction_summary_tables(combined_df, output_dir)


def save_correction_summary_tables(combined_df: pd.DataFrame, output_dir: Path):
    """
    Generate separate summary tables showing significance under FDR and FWER corrections.
    """
    # === FDR-corrected table ===
    fdr_df = combined_df[["Task", "DV", "Variable", "β", "SE", "t", "p", "p_fdr", 
                          "95% CI Lower", "95% CI Upper", "R²", "N"]].copy()
    
    # Add FDR significance column
    def fdr_sig(p):
        if p < 0.001:
            return "***"
        elif p < 0.01:
            return "**"
        elif p < 0.05:
            return "*"
        else:
            return ""
    
    fdr_df["FDR Sig"] = fdr_df["p_fdr"].apply(fdr_sig)
    fdr_df = fdr_df.rename(columns={"p_fdr": "p (FDR-corrected)"})
    fdr_df.to_csv(output_dir / "all_coefficients_FDR.csv", index=False)
    
    # Count significant results
    n_sig_fdr = (fdr_df["FDR Sig"] != "").sum()
    n_total = len(fdr_df)
    print(f"\n  FDR-corrected results: {n_sig_fdr}/{n_total} significant (saved to all_coefficients_FDR.csv)")
    
    # === Bonferroni-corrected table ===
    bonf_df = combined_df[["Task", "DV", "Variable", "β", "SE", "t", "p", "p_bonferroni",
                           "Bonf CI Lower", "Bonf CI Upper", "R²", "N"]].copy()
    
    # Add Bonferroni significance column
    bonf_df["Bonf Sig"] = bonf_df["p_bonferroni"].apply(fdr_sig)  # Same thresholds
    bonf_df = bonf_df.rename(columns={
        "p_bonferroni": "p (Bonferroni-corrected)",
        "Bonf CI Lower": "95% CI Lower (Bonf)",
        "Bonf CI Upper": "95% CI Upper (Bonf)"
    })
    bonf_df.to_csv(output_dir / "all_coefficients_bonferroni.csv", index=False)
    
    # Count significant results
    n_sig_bonf = (bonf_df["Bonf Sig"] != "").sum()
    print(f"  Bonferroni-corrected results: {n_sig_bonf}/{n_total} significant (saved to all_coefficients_bonferroni.csv)")
    
    # === Print comparison summary ===
    print(f"\n  Correction comparison:")
    print(f"    Uncorrected (p < 0.05):  {(combined_df['p'] < 0.05).sum()}/{n_total}")
    print(f"    FDR (q < 0.05):          {n_sig_fdr}/{n_total}")
    print(f"    Bonferroni (p < 0.05):   {n_sig_bonf}/{n_total}")


# === MAIN ===

if __name__ == "__main__":
    print("=" * 80)
    print("  MULTIVARIABLE LINEAR REGRESSION ANALYSIS")
    print("  Impact of Model Characteristics on Classification Performance")
    print("  Data source: all_models_all_tasks.csv (with safety corrections)")
    print("=" * 80)
    
    # Run all regressions
    results = run_all_regressions()
    
    # Save coefficient tables
    output_dir = ROOT / "results" / "statistics"
    save_all_coefficient_tables(results, output_dir)
    
    # Create summary table
    print("\n\n" + "=" * 100)
    print("  MODEL FIT SUMMARY")
    print("=" * 100)
    summary_df = create_summary_table(results)
    print(summary_df.to_string(index=False))
    
    # Save summary
    output_path = output_dir / "regression_summary.csv"
    summary_df.to_csv(output_path, index=False)
    print(f"\nModel fit summary saved to: {output_path}")
