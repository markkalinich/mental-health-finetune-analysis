#!/usr/bin/env python3
"""
Combined Fine-tune Facet Plot

Generates a 4x3 facet plot showing delta F1 scores for all fine-tune types
(Mental Health, Medical, Safety, Instruction-Tuned) across all tasks.

Output: results/fine_tune_figures/delta_f1_facet_plot_across_all_models_and_tasks.png
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy import stats as scipy_stats
import sys

ROOT = Path(__file__).parent.parent

# Fine-tune type configurations (row order: Mental Health, Medical, Safety, Instruction-Tuned)
FINETUNE_TYPES = [
    {
        'name': 'mental_health',
        'label': 'Mental Health',
        'filter': lambda c: (c['model_type'] == 'Mental Health') & (c['Base_Model_LM_Studio_ID'].notna()),
    },
    {
        'name': 'medical',
        'label': 'Medical',
        'filter': lambda c: (c['model_type'].isin(['Medical', 'MedGemma'])) & (c['Base_Model_LM_Studio_ID'].notna()),
    },
    {
        'name': 'safety',
        'label': 'Safety',
        'filter': lambda c: (c['model_type'].isin(['ShieldGemma', 'Guard'])) & (c['Base_Model_LM_Studio_ID'].notna()),
    },
    {
        'name': 'instruction_tuned',
        'label': 'Instruction-Tuned',
        'filter': lambda c: (c['model_type'] == 'IT') & (c['Base_Model_Type'] == 'PT') & (c['Base_Model_LM_Studio_ID'].notna()),
    },
]

TASKS = ['suicidal_ideation', 'therapy_request', 'therapy_engagement']
TASK_TITLES = {
    'suicidal_ideation': 'Suicidal Ideation',
    'therapy_request': 'Therapy Request',
    'therapy_engagement': 'Therapy Engagement'
}
FAMILIES = ['gemma', 'llama', 'qwen']
FAMILY_COLORS = {'gemma': '#E74C3C', 'llama': '#3498DB', 'qwen': '#2ECC71'}
FAMILY_LABELS = {'gemma': 'Gemma', 'llama': 'Llama', 'qwen': 'Qwen'}


def load_data():
    """Load config and results."""
    config = pd.read_csv(ROOT / 'config/models_config.csv')
    results = pd.read_csv(ROOT / 'data/inputs/model_results/all_models_all_tasks.csv')
    return config, results


def compute_deltas(config, results, filter_func,
                    metric_col: str = "f1_score", col_prefix: str = "f1") -> pd.DataFrame:
    """Compute fine-tune minus base for a numeric column (e.g. f1_score or parse_success_rate)."""
    fine_tunes = config[filter_func(config)].copy()
    base_lookup = config.set_index('lm_studio_id')

    delta_col = f'delta_{col_prefix}'
    ft_col = f'ft_{col_prefix}'
    base_col = f'base_{col_prefix}'

    records = []
    for task in TASKS:
        for _, ft_row in fine_tunes.iterrows():
            base_id = ft_row['Base_Model_LM_Studio_ID']
            if base_id not in base_lookup.index:
                continue

            base_row = base_lookup.loc[base_id]
            if isinstance(base_row, pd.DataFrame):
                base_row = base_row.iloc[0]

            arch = str(ft_row.get('architecture', '')).lower()
            if 'gemma' in arch:
                family = 'gemma'
            elif 'llama' in arch:
                family = 'llama'
            elif 'qwen' in arch:
                family = 'qwen'
            else:
                continue

            ft_match = results[(results['task'] == task) &
                              (results['model_family'] == ft_row['family']) &
                              (results['model_size'] == ft_row['size'])]
            base_match = results[(results['task'] == task) &
                                (results['model_family'] == base_row['family']) &
                                (results['model_size'] == base_row['size'])]

            if len(ft_match) == 0 or len(base_match) == 0:
                continue

            ft_v = ft_match[metric_col].values[0]
            base_v = base_match[metric_col].values[0]

            if pd.notna(ft_v) and pd.notna(base_v):
                records.append({
                    'family': family, 'task': task,
                    'ft_family': str(ft_row['family']),
                    'ft_size': str(ft_row['size']),
                    'ft_model_type': str(ft_row['model_type']),
                    'ft_param_billions': pd.to_numeric(ft_row.get('param_billions'), errors='coerce'),
                    'base_family': str(base_row['family']),
                    'base_size': str(base_row['size']),
                    delta_col: ft_v - base_v,
                    base_col: base_v,
                    ft_col: ft_v,
                })
    
    return pd.DataFrame(records)


def generate_combined_facet_plot(metric_col: str = "f1_score",
                                  col_prefix: str = "f1",
                                  y_label_suffix: str = "F1 Score",
                                  out_dir_override=None):
    """Generate 4x3 facet plot for all fine-tune types across all tasks.

    Args:
        metric_col: Column in all_models_all_tasks.csv to compute deltas for.
        col_prefix: Short name used in column naming (delta_{prefix}, ft_{prefix}, base_{prefix}).
        y_label_suffix: Text appended to fine-tune label for the y-axis (e.g. "F1 Score", "Parse Success Rate").
        out_dir_override: If set, write outputs here instead of results/fine_tune_figures.
    """
    delta_col = f"delta_{col_prefix}"
    ft_col = f"ft_{col_prefix}"
    base_col = f"base_{col_prefix}"

    all_data = {}
    for ft_config in FINETUNE_TYPES:
        config, results = load_data()
        df = compute_deltas(config, results, ft_config['filter'], metric_col, col_prefix)
        all_data[ft_config['name']] = df
        print(f"{ft_config['label']} ({col_prefix}): {len(df)} data points")
    
    # Statistics records for summary CSV
    stats_records = []
    
    # Create figure
    fig, axes = plt.subplots(4, 3, figsize=(18, 20), sharey='row')
    
    for row_idx, ft_config in enumerate(FINETUNE_TYPES):
        df = all_data[ft_config['name']]
        
        # Find row max for consistent annotation height
        row_max_y = 0
        if len(df) > 0:
            for task in TASKS:
                for fam in FAMILIES:
                    subset = df[(df['task'] == task) & (df['family'] == fam)]
                    if len(subset) > 0:
                        max_val = subset[delta_col].max()
                        if max_val > row_max_y:
                            row_max_y = max_val
        
        for col_idx, task in enumerate(TASKS):
            ax = axes[row_idx, col_idx]
            task_data = df[df['task'] == task]
            
            # Count families with n>=2 for Bonferroni correction
            n_testable_families = sum(
                1 for fam in FAMILIES 
                if len(task_data[task_data['family'] == fam]) >= 2
            )
            alpha_corrected = 0.05 / n_testable_families if n_testable_families > 0 else 0.05
            
            # Prepare box plot data
            box_data, positions, colors = [], [], []
            for i, fam in enumerate(FAMILIES):
                fam_data = task_data[task_data['family'] == fam]
                if len(fam_data) > 0:
                    box_data.append(fam_data[delta_col].values)
                    positions.append(i)
                    colors.append(FAMILY_COLORS[fam])
            
            if box_data:
                bp = ax.boxplot(box_data, positions=positions, widths=0.6, patch_artist=True,
                               showfliers=False, medianprops=dict(color='black', linewidth=2))
                
                for patch, color in zip(bp['boxes'], colors):
                    patch.set_facecolor(color)
                    patch.set_alpha(0.6)
                    patch.set_edgecolor(color)
                
                # Strip plot overlay (jittered dots)
                for i, fam in enumerate(FAMILIES):
                    fam_data = task_data[task_data['family'] == fam]
                    if len(fam_data) > 0:
                        x_jitter = i + np.random.uniform(-0.2, 0.2, len(fam_data))
                        ax.scatter(x_jitter, fam_data[delta_col].values, s=50, alpha=0.5,
                                  color=FAMILY_COLORS[fam], edgecolors='black', linewidth=0.5, zorder=10)
                
                # Significance annotations (Bonferroni-corrected paired t-tests)
                # Also collect stats for summary CSV
                if n_testable_families > 0:
                    for i, fam in enumerate(FAMILIES):
                        fam_data = task_data[task_data['family'] == fam]
                        if len(fam_data) >= 2:
                            _, p = scipy_stats.ttest_rel(fam_data[ft_col].values, fam_data[base_col].values)
                            
                            # Record statistics
                            p_adjusted = min(p * n_testable_families, 1.0)  # Cap at 1.0
                            stats_records.append({
                                'finetune_type': ft_config['label'],
                                'task': TASK_TITLES[task],
                                'model_family': FAMILY_LABELS[fam],
                                'n_pairs': len(fam_data),
                                f'mean_{delta_col}': fam_data[delta_col].mean(),
                                f'std_{delta_col}': fam_data[delta_col].std(),
                                f'median_{delta_col}': fam_data[delta_col].median(),
                                'p_value': p,
                                'p_adjusted': p_adjusted,
                                'alpha_corrected': alpha_corrected,
                                'n_comparisons': n_testable_families,
                                'correction_method': 'Bonferroni (within cell)',
                                'significant': p < alpha_corrected,
                            })
                            
                            if p_adjusted < 0.001:
                                sig = '***'
                            elif p_adjusted < 0.01:
                                sig = '**'
                            elif p_adjusted < 0.05:
                                sig = '*'
                            else:
                                sig = None
                            
                            if sig:
                                y_pos = row_max_y + 0.05
                                ax.text(i, y_pos, sig, ha='center', fontsize=18, fontweight='bold')
                        elif len(fam_data) == 1:
                            stats_records.append({
                                'finetune_type': ft_config['label'],
                                'task': TASK_TITLES[task],
                                'model_family': FAMILY_LABELS[fam],
                                'n_pairs': len(fam_data),
                                f'mean_{delta_col}': fam_data[delta_col].mean(),
                                f'std_{delta_col}': np.nan,
                                f'median_{delta_col}': fam_data[delta_col].median(),
                                'p_value': np.nan,
                                'p_adjusted': np.nan,
                                'alpha_corrected': alpha_corrected,
                                'n_comparisons': n_testable_families,
                                'correction_method': 'Bonferroni (within cell)',
                                'significant': np.nan,
                            })
            
            # Styling
            ax.axhline(0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
            ax.grid(True, alpha=0.3, axis='y')
            ax.set_xticks(range(len(FAMILIES)))
            ax.set_xticklabels([FAMILY_LABELS[f] for f in FAMILIES], fontsize=18)  # 25% larger (14 -> 17.5)
            ax.tick_params(axis='y', labelsize=14)
            
            # Row labels (y-axis) - 18% larger (16 -> 19), kept to 2 lines
            if col_idx == 0:
                ax.set_ylabel(f'{ft_config["label"]}\nΔ {y_label_suffix}', fontsize=19)
                # Panel labels (A, B, C, D) for paper figure references
                panel_label = chr(65 + row_idx)  # 65 = 'A' in ASCII
                ax.text(-0.18, 1.08, panel_label, transform=ax.transAxes,
                       fontsize=26, fontweight='bold', va='top', ha='left')
            
            # Column titles (only top row) - 18% larger (18 -> 21)
            if row_idx == 0:
                ax.set_title(TASK_TITLES[task], fontsize=21, fontweight='bold', pad=15)
            
            # Legend (only top-right cell, bottom right position) - 25% larger (12 -> 15)
            if row_idx == 0 and col_idx == 2:
                legend = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=FAMILY_COLORS[f],
                                     markersize=12, markeredgecolor='black', label=FAMILY_LABELS[f])
                         for f in FAMILIES]
                ax.legend(handles=legend, loc='lower right', fontsize=15)
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.25, wspace=0.15)
    
    out_dir = Path(out_dir_override) if out_dir_override else ROOT / 'results/fine_tune_figures'
    out_dir.mkdir(exist_ok=True, parents=True)

    out_file = out_dir / f'delta_{col_prefix}_facet_plot_across_all_models_and_tasks.png'
    plt.savefig(out_file, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: {out_file}")

    combined_df = pd.concat([
        all_data[ft['name']].assign(finetune_type=ft['name'])
        for ft in FINETUNE_TYPES
    ], ignore_index=True)
    csv_file = out_dir / f'delta_{col_prefix}_facet_plot_across_all_models_and_tasks_data.csv'
    combined_df.to_csv(csv_file, index=False)
    print(f"Saved: {csv_file}")

    stats_df = pd.DataFrame(stats_records)
    stats_file = out_dir / f'delta_{col_prefix}_statistical_analysis_summary.csv'
    stats_df.to_csv(stats_file, index=False)
    print(f"Saved: {stats_file}")
    
    print("\n" + "="*60)
    print("Statistical Testing Summary")
    print("="*60)
    print(f"Method: Paired t-test (fine-tune {col_prefix} vs base {col_prefix})")
    print("Correction: Bonferroni within each cell (by # testable families)")
    print("\nPer-cell correction factors:")
    for ft_config in FINETUNE_TYPES:
        df = all_data[ft_config['name']]
        print(f"\n  {ft_config['label']}:")
        for task in TASKS:
            task_data = df[df['task'] == task]
            n_testable = sum(1 for fam in FAMILIES
                            if len(task_data[task_data['family'] == fam]) >= 2)
            if n_testable > 0:
                print(f"    {TASK_TITLES[task]}: α=0.05/{n_testable} = {0.05/n_testable:.4f}")
            else:
                print(f"    {TASK_TITLES[task]}: No testable families (n<2)")


def generate_delta_parse_facet_plot():
    """Same layout as Figure 3, but Δ parse_success_rate (fine-tune − base)."""
    generate_combined_facet_plot(
        metric_col="parse_success_rate",
        col_prefix="parse",
        y_label_suffix="Parse Success Rate",
        out_dir_override=ROOT / "results" / "revision_experiments",
    )


def main():
    import argparse
    p = argparse.ArgumentParser(description='Combined fine-tune facet plots')
    p.add_argument(
        '--metric',
        choices=('f1', 'parse'),
        default='f1',
        help='f1 = Figure 3 (default); parse = delta parse success (revision)',
    )
    args = p.parse_args()
    if args.metric == 'f1':
        generate_combined_facet_plot()
    else:
        generate_delta_parse_facet_plot()


if __name__ == '__main__':
    main()

