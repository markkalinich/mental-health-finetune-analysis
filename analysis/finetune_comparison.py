#!/usr/bin/env python3
"""
Fine-tune Comparison Analysis

Generates summary box plots comparing fine-tuned models against their base models.
Supports multiple comparison types via command-line argument.

Usage:
    python finetune_comparison.py medical
    python finetune_comparison.py safety
    python finetune_comparison.py instruction_tuned
    python finetune_comparison.py mental_health
    python finetune_comparison.py all
"""
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy import stats as scipy_stats
import sys

ROOT = Path(__file__).parent.parent

# Comparison type configurations
COMPARISONS = {
    'medical': {
        'filter': lambda c: (c['model_type'].isin(['Medical', 'MedGemma'])) & (c['Base_Model_LM_Studio_ID'].notna()),
        'title': 'Medical Fine-tunes',
        'output': 'medical_finetunes_summary.png',
        'apply_safety_corrections': False,
    },
    'safety': {
        'filter': lambda c: (c['model_type'].isin(['ShieldGemma', 'Guard'])) & (c['Base_Model_LM_Studio_ID'].notna()),
        'title': 'Safety Fine-tunes',
        'output': 'safety_finetunes_summary.png',
        'apply_safety_corrections': True,
    },
    'instruction_tuned': {
        'filter': lambda c: (c['model_type'] == 'IT') & (c['Base_Model_Type'] == 'PT') & (c['Base_Model_LM_Studio_ID'].notna()),
        'title': 'Instruction-Tuned vs Pre-Trained',
        'output': 'instruction_tuned_summary.png',
        'apply_safety_corrections': False,
    },
    'mental_health': {
        'filter': lambda c: (c['model_type'] == 'Mental Health') & (c['Base_Model_LM_Studio_ID'].notna()),
        'title': 'Mental Health Fine-tunes',
        'output': 'mental_health_finetunes_summary.png',
        'apply_safety_corrections': False,
    },
}

TASKS = ['suicidal_ideation', 'therapy_request', 'therapy_engagement']
TASK_TITLES = {
    'suicidal_ideation': 'Suicidal Ideation',
    'therapy_request': 'Therapy Request',
    'therapy_engagement': 'Therapy Engagement'
}
FAMILY_COLORS = {'gemma': '#E74C3C', 'llama': '#3498DB', 'qwen': '#2ECC71'}
FAMILY_LABELS = {'gemma': 'Gemma', 'llama': 'Llama', 'qwen': 'Qwen'}


def load_data(apply_safety_corrections=False):
    """Load config and results, optionally applying safety model corrections."""
    config = pd.read_csv(ROOT / 'config/models_config.csv')
    results = pd.read_csv(ROOT / 'data/inputs/model_results/all_models_all_tasks.csv')
    
    if apply_safety_corrections:
        sys.path.insert(0, str(ROOT / 'analysis' / 'comparative_analysis'))
        try:
            from facet_plot_utils import (
                compute_shieldgemma_metrics, compute_llama_guard_metrics,
                compute_qwen_guard_metrics, apply_guard_metrics_to_df,
            )
            safety_metrics = {}
            safety_metrics.update(compute_shieldgemma_metrics())
            safety_metrics.update(compute_llama_guard_metrics())
            safety_metrics.update(compute_qwen_guard_metrics())
            if safety_metrics:
                results = apply_guard_metrics_to_df(results, safety_metrics)
                print(f"Applied safety corrections for {len(safety_metrics)} configurations")
        except Exception as e:
            print(f"Warning: Could not apply safety corrections: {e}")
    
    return config, results


def compute_deltas(config, results, filter_func):
    """Compute performance deltas for fine-tunes vs their base models."""
    fine_tunes = config[filter_func(config)].copy()
    base_lookup = config.set_index('lm_studio_id')
    
    records = []
    for task in TASKS:
        for _, ft_row in fine_tunes.iterrows():
            base_id = ft_row['Base_Model_LM_Studio_ID']
            if base_id not in base_lookup.index:
                continue
            
            base_row = base_lookup.loc[base_id]
            
            # Determine family from architecture
            arch = str(ft_row.get('architecture', '')).lower()
            if 'gemma' in arch:
                family = 'gemma'
            elif 'llama' in arch:
                family = 'llama'
            elif 'qwen' in arch:
                family = 'qwen'
            else:
                continue
            
            # Get scores
            ft_match = results[(results['task'] == task) & 
                              (results['model_family'] == ft_row['family']) & 
                              (results['model_size'] == ft_row['size'])]
            base_match = results[(results['task'] == task) & 
                                (results['model_family'] == base_row['family']) & 
                                (results['model_size'] == base_row['size'])]
            
            if len(ft_match) == 0 or len(base_match) == 0:
                continue
            
            ft_f1, base_f1 = ft_match['f1_score'].values[0], base_match['f1_score'].values[0]
            ft_acc, base_acc = ft_match['accuracy'].values[0], base_match['accuracy'].values[0]
            
            if pd.notna(ft_f1) and pd.notna(base_f1) and pd.notna(ft_acc) and pd.notna(base_acc):
                records.append({
                    'family': family, 'task': task,
                    'delta_f1': ft_f1 - base_f1, 'delta_accuracy': ft_acc - base_acc,
                    'base_f1': base_f1, 'ft_f1': ft_f1,
                    'base_accuracy': base_acc, 'ft_accuracy': ft_acc,
                })
    
    return pd.DataFrame(records), len(fine_tunes)


def generate_plot(df, title, output_path):
    """Generate 2x3 summary box plot."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10), sharey='row')
    
    metrics = [('delta_f1', 'Δ F1 Score'), ('delta_accuracy', 'Δ Accuracy')]
    families = ['gemma', 'llama', 'qwen']
    
    for row_idx, (metric, metric_label) in enumerate(metrics):
        # Find row max for consistent annotation height
        row_max_y = max(
            df[(df['task'] == task) & (df['family'] == fam)][metric].max()
            for task in TASKS for fam in families
            if len(df[(df['task'] == task) & (df['family'] == fam)]) > 0
        ) if len(df) > 0 else 0
        
        for col_idx, task in enumerate(TASKS):
            ax = axes[row_idx, col_idx]
            task_data = df[df['task'] == task]
            
            # Count families with n>=2 for this task (for Bonferroni correction)
            n_testable_families = sum(
                1 for fam in families 
                if len(task_data[task_data['family'] == fam]) >= 2
            )
            alpha_corrected = 0.05 / n_testable_families if n_testable_families > 0 else 0.05
            
            # Prepare box plot data
            box_data, positions, colors = [], [], []
            for i, fam in enumerate(families):
                fam_data = task_data[task_data['family'] == fam]
                if len(fam_data) > 0:
                    box_data.append(fam_data[metric].values)
                    positions.append(i)
                    colors.append(FAMILY_COLORS[fam])
            
            if box_data:
                bp = ax.boxplot(box_data, positions=positions, widths=0.6, patch_artist=True,
                               showfliers=False, medianprops=dict(color='black', linewidth=2))
                
                for patch, color in zip(bp['boxes'], colors):
                    patch.set_facecolor(color)
                    patch.set_alpha(0.6)
                    patch.set_edgecolor(color)
                
                # Strip plot overlay
                for i, fam in enumerate(families):
                    fam_data = task_data[task_data['family'] == fam]
                    if len(fam_data) > 0:
                        x_jitter = i + np.random.uniform(-0.2, 0.2, len(fam_data))
                        ax.scatter(x_jitter, fam_data[metric].values, s=50, alpha=0.5,
                                  color=FAMILY_COLORS[fam], edgecolors='black', linewidth=0.5, zorder=10)
                
                # Significance annotations (only for delta_f1, Bonferroni-corrected)
                if metric == 'delta_f1' and n_testable_families > 0:
                    for i, fam in enumerate(families):
                        fam_data = task_data[task_data['family'] == fam]
                        if len(fam_data) >= 2:
                            base_col = 'base_f1'
                            ft_col = 'ft_f1'
                            _, p = scipy_stats.ttest_rel(fam_data[ft_col].values, fam_data[base_col].values)
                            
                            # Use Bonferroni-corrected thresholds
                            if p < alpha_corrected / 10:
                                sig = '***'
                            elif p < alpha_corrected / 2:
                                sig = '**'
                            elif p < alpha_corrected:
                                sig = '*'
                            else:
                                sig = None
                            
                            if sig:
                                y_pos = row_max_y + 0.05
                                ax.text(i, y_pos, sig, ha='center', fontsize=18, fontweight='bold')
            
            ax.axhline(0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
            ax.grid(True, alpha=0.3, axis='y')
            ax.set_xticks(range(len(families)))
            ax.set_xticklabels([FAMILY_LABELS[f] for f in families], fontsize=16)
            ax.tick_params(axis='y', labelsize=16)
            
            if col_idx == 0:
                ax.set_ylabel(metric_label, fontsize=18)
            if row_idx == 0:
                ax.set_title(TASK_TITLES[task], fontsize=20, fontweight='bold', pad=15)
            if row_idx == 0 and col_idx == 2:
                legend = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=FAMILY_COLORS[f],
                                     markersize=10, markeredgecolor='black', label=FAMILY_LABELS[f])
                         for f in families]
                ax.legend(handles=legend, loc='upper right', fontsize=14)
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.25, wspace=0.15)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()


def run_comparison(comparison_type):
    """Run a single comparison analysis."""
    cfg = COMPARISONS[comparison_type]
    print(f"\n{'='*60}\n{cfg['title']}\n{'='*60}")
    
    config, results = load_data(cfg['apply_safety_corrections'])
    df, n_models = compute_deltas(config, results, cfg['filter'])
    
    print(f"Models with base: {n_models}")
    print(f"Data points: {len(df)}")
    
    if len(df) == 0:
        print("No data available!")
        return
    
    for fam in ['gemma', 'llama', 'qwen']:
        fam_data = df[df['family'] == fam]
        if len(fam_data) > 0:
            print(f"  {fam}: {len(fam_data)} points across {fam_data['task'].nunique()} tasks")
    
    out_dir = ROOT / 'results/finetune_comparisons'
    out_dir.mkdir(exist_ok=True, parents=True)
    
    out_file = out_dir / cfg['output']
    generate_plot(df, cfg['title'], out_file)
    print(f"Saved: {out_file}")
    
    csv_file = out_dir / cfg['output'].replace('.png', '_data.csv')
    df.to_csv(csv_file, index=False)
    
    # Report correction factors
    print("\nStatistical testing:")
    print("  - Method: Paired t-test (fine-tune vs base)")
    print("  - Correction: Bonferroni within each task column")
    for task in ['suicidal_ideation', 'therapy_request', 'therapy_engagement']:
        task_data = df[df['task'] == task]
        n_testable = sum(1 for fam in ['gemma', 'llama', 'qwen'] 
                        if len(task_data[task_data['family'] == fam]) >= 2)
        if n_testable > 0:
            task_name = TASK_TITLES[task]
            print(f"  - {task_name}: α=0.05/{n_testable} = {0.05/n_testable:.4f}")
    
    print("\nLimitations: Multiple fine-tunes sharing the same base model may")
    print("  violate independence assumptions, potentially inflating significance.")


def main():
    parser = argparse.ArgumentParser(description='Fine-tune comparison analysis')
    parser.add_argument('type', choices=list(COMPARISONS.keys()) + ['all'],
                       help='Comparison type to run')
    args = parser.parse_args()
    
    if args.type == 'all':
        for comp_type in COMPARISONS:
            run_comparison(comp_type)
    else:
        run_comparison(args.type)


if __name__ == '__main__':
    main()
