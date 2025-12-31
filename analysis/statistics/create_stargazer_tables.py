#!/usr/bin/env python3
"""
Create beautiful regression tables using Stargazer.

Generates LaTeX and HTML formatted tables for publication.
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from pathlib import Path
from stargazer.stargazer import Stargazer
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


# === CONFIGURATION ===

CONFIG_PATH = Path(__file__).parent.parent.parent / "config" / "models_config.csv"
SI_METRICS_PATH = Path(__file__).parent.parent.parent / "results" / "individual_prediction_performance" / "suicidal_ideation" / "20251210_002525_SI" / "tables" / "comprehensive_metrics.csv"
TX_ENGAGEMENT_PATH = Path(__file__).parent.parent.parent / "results" / "individual_prediction_performance" / "therapy_engagement" / "20251210_232149_tx_engagement" / "tables" / "comprehensive_metrics.csv"
TX_REQUEST_PATH = Path(__file__).parent.parent.parent / "results" / "individual_prediction_performance" / "therapy_request" / "20251211_042115_tx_request" / "tables" / "comprehensive_metrics.csv"

FAMILY_TO_PARENT = {
    "gemma": "Gemma", "gemma1": "Gemma", "gemma2": "Gemma", "gemma3n": "Gemma",
    "medgemma": "Gemma", "shieldgemma": "Gemma", 
    "mental_health": "Gemma", "gemma_therapy": "Gemma",
    "qwen": "Qwen", "qwen1.5": "Qwen", "qwen2": "Qwen",
    "qwen_medical": "Qwen", "qwen_mental_health": "Qwen", "qwen_guard": "Qwen",
    "llama1": "LLaMA", "llama2": "LLaMA", "llama3": "LLaMA",
    "llama3.1": "LLaMA", "llama3.2": "LLaMA", "llama3.3": "LLaMA", "llama4": "LLaMA",
    "llama_medical": "LLaMA", "llama_mental_health": "LLaMA", 
    "llama_therapy": "LLaMA", "llama_guard": "LLaMA",
}

MODEL_TYPE_MAP = {
    "PT": "Base Model",
    "IT": "Instruction-Tuned", 
    "Mental Health": "Mental Health Tuned",
    "MedGemma": "Medical-Tuned",
    "Medical": "Medical-Tuned",
    "ShieldGemma": "Safety-Tuned",
    "Guard": "Safety-Tuned",
}


def get_version_ordinal(row):
    """Map model version to ordinal version category (1, 2, 3, 4)."""
    version = row.get("version", None)
    family = row.get("family", "")
    architecture = row.get("architecture", "")
    
    if pd.isna(version):
        return None
    
    version = float(version) if not isinstance(version, str) else version
    
    if architecture == "gemma3n" or "3n" in str(family):
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


def load_and_prepare_data():
    """Load and prepare all data."""
    # Load config
    config_df = pd.read_csv(CONFIG_PATH)
    config_df = config_df[config_df["enabled"] == True].copy()
    config_df["parent_family"] = config_df["family"].map(FAMILY_TO_PARENT)
    config_df = config_df[config_df["parent_family"].isin(["Qwen", "LLaMA", "Gemma"])].copy()
    config_df["version"] = config_df.apply(get_version_ordinal, axis=1)
    config_df["finetune_type"] = config_df["model_type"].map(MODEL_TYPE_MAP).fillna("Other")
    config_df["param_billions"] = pd.to_numeric(config_df["param_billions"], errors="coerce")
    
    # Load metrics
    tasks = {
        "Suicidal Ideation": SI_METRICS_PATH,
        "Therapy Request": TX_REQUEST_PATH,
        "Therapy Engagement": TX_ENGAGEMENT_PATH,
    }
    
    all_data = {}
    for task_name, path in tasks.items():
        metrics_df = pd.read_csv(path)
        merged = metrics_df.merge(
            config_df[["family", "size", "parent_family", "version", "param_billions", "finetune_type"]],
            left_on=["model_family", "model_size"],
            right_on=["family", "size"],
            how="inner"
        )
        merged = merged.dropna(subset=["parent_family", "version", "param_billions", "f1_score", "accuracy", "finetune_type"])
        merged = merged[merged["finetune_type"] != "Other"]
        all_data[task_name] = merged
    
    return all_data


def run_all_regressions(data_dict):
    """Run all regressions and return model objects."""
    models = {}
    
    for task_name, df in data_dict.items():
        task_models = {}
        for dv in ["f1_score", "accuracy"]:
            formula = f"{dv} ~ C(parent_family) + C(version) + param_billions + C(finetune_type)"
            model = smf.ols(formula, data=df).fit(cov_type='HC3')
            task_models[dv] = model
        models[task_name] = task_models
    
    return models


def create_stargazer_tables(models, output_dir):
    """Create Stargazer tables - ONE PER DEPENDENT VARIABLE."""
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for task_name, task_models in models.items():
        print(f"\nCreating Stargazer tables for {task_name}...")
        
        for dv_name, model in task_models.items():
            dv_label = "F1 Score" if dv_name == "f1_score" else "Accuracy"
            
            # Create Stargazer object with SINGLE model
            sg = Stargazer([model])
            
            # Show confidence intervals instead of standard errors
            sg.show_confidence_intervals(True)
            
            # Customize appearance
            sg.title(f"{task_name} - {dv_label}")
            sg.covariate_order([
                'Intercept',
                'C(parent_family)[T.LLaMA]',
                'C(parent_family)[T.Qwen]',
                'C(version)[T.2]',
                'C(version)[T.3]',
                'C(version)[T.4]',
                'C(finetune_type)[T.Instruction-Tuned]',
                'C(finetune_type)[T.Medical-Tuned]',
                'C(finetune_type)[T.Mental Health Tuned]',
                'C(finetune_type)[T.Safety-Tuned]',
                'param_billions'
            ])
            sg.rename_covariates({
                'Intercept': 'Intercept',
                'C(parent_family)[T.LLaMA]': 'Family: LLaMA',
                'C(parent_family)[T.Qwen]': 'Family: Qwen',
                'C(version)[T.2]': 'Version: 2',
                'C(version)[T.3]': 'Version: 3',
                'C(version)[T.4]': 'Version: 4',
                'C(finetune_type)[T.Instruction-Tuned]': 'Fine-Tune: Instruction-Tuned',
                'C(finetune_type)[T.Medical-Tuned]': 'Fine-Tune: Medical-Tuned',
                'C(finetune_type)[T.Mental Health Tuned]': 'Fine-Tune: Mental Health Tuned',
                'C(finetune_type)[T.Safety-Tuned]': 'Fine-Tune: Safety-Tuned',
                'param_billions': 'Parameter Size (B)'
            })
            sg.show_model_numbers(False)
            sg.show_degrees_of_freedom(False)
            
            # Add notes
            sg.add_line('Reference Categories', ['Family=Gemma, Version=1, Fine-Tune=Base Model'])
            sg.add_line('Standard Errors', ['HC3 Robust'])
            
            # Generate LaTeX
            task_clean = task_name.lower().replace(' ', '_')
            dv_clean = dv_name.replace('_', '')
            latex_path = output_dir / f"stargazer_{task_clean}_{dv_clean}.tex"
            with open(latex_path, 'w') as f:
                f.write(sg.render_latex())
            print(f"  ✓ {dv_label} LaTeX: {latex_path.name}")
            
            # Generate HTML
            html_path = output_dir / f"stargazer_{task_clean}_{dv_clean}.html"
            with open(html_path, 'w') as f:
                f.write(sg.render_html())
            print(f"  ✓ {dv_label} HTML: {html_path.name}")


if __name__ == "__main__":
    print("="*80)
    print("CREATING STARGAZER REGRESSION TABLES")
    print("="*80)
    
    # Load data
    print("\nLoading data...")
    data = load_and_prepare_data()
    print(f"  ✓ Loaded {len(data)} tasks")
    
    # Run regressions
    print("\nRunning regressions...")
    models = run_all_regressions(data)
    print(f"  ✓ Completed {sum(len(m) for m in models.values())} regressions")
    
    # Create tables
    output_dir = Path(__file__).parent.parent.parent / "results" / "statistics"
    create_stargazer_tables(models, output_dir)
    
    print("\n" + "="*80)
    print("✓ ALL STARGAZER TABLES CREATED")
    print("="*80)
    print(f"\nOutput directory: {output_dir}")
    print("\nFiles created (6 tables - one per DV):")
    print("  - stargazer_suicidal_ideation_f1score.tex/.html")
    print("  - stargazer_suicidal_ideation_accuracy.tex/.html")
    print("  - stargazer_therapy_request_f1score.tex/.html")
    print("  - stargazer_therapy_request_accuracy.tex/.html")
    print("  - stargazer_therapy_engagement_f1score.tex/.html")
    print("  - stargazer_therapy_engagement_accuracy.tex/.html")
