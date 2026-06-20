#!/usr/bin/env python3
"""
Combined Fine-tune Facet Plot

Generates 4x3 facet plots for fine-tune vs base deltas across tasks:
- Default (Figure 3): Δ F1 → results/fine_tune_figures/
- Parse variant: Δ parse_success_rate → results/revision_experiments/

Output (F1): results/fine_tune_figures/delta_f1_facet_plot_across_all_models_and_tasks.png
Output (parse): results/revision_experiments/delta_parse_facet_plot_across_all_models_and_tasks.png
"""
import argparse
import os
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


def compute_deltas(config, results, filter_func, metric_col: str, col_prefix: str) -> pd.DataFrame:
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
            if len(ft_match) > 1:
                raise ValueError(
                    f"Duplicate results for task={task}, "
                    f"family={ft_row['family']}, size={ft_row['size']}: "
                    f"found {len(ft_match)} rows, expected 1"
                )
            if len(base_match) > 1:
                raise ValueError(
                    f"Duplicate results for task={task}, "
                    f"family={base_row['family']}, size={base_row['size']}: "
                    f"found {len(base_match)} rows, expected 1"
                )

            ft_v = ft_match[metric_col].values[0]
            base_v = base_match[metric_col].values[0]

            if pd.notna(ft_v) and pd.notna(base_v):
                records.append({
                    'family': family,
                    'task': task,
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


def add_jitter(values: np.ndarray, jitter_amount: float = 0.1) -> np.ndarray:
    """Add small random jitter to values to reduce overlap (seed 42 for reproducibility)."""
    np.random.seed(42)
    return values + np.random.uniform(-jitter_amount, jitter_amount, size=len(values))


def collect_figure3_model_family_size_keys() -> set[tuple[str, str]]:
    """
    All (family, size) pairs that appear as either a fine-tune or its mapped base
    in Figure 3's delta logic (same filters as FINETUNE_TYPES / compute_deltas).
    """
    config = pd.read_csv(ROOT / 'config/models_config.csv')
    base_lookup = config.set_index('lm_studio_id')
    keys: set[tuple[str, str]] = set()

    for ft_config in FINETUNE_TYPES:
        fine_tunes = config[ft_config['filter'](config)]
        for _, ft_row in fine_tunes.iterrows():
            base_id = ft_row['Base_Model_LM_Studio_ID']
            if base_id not in base_lookup.index:
                continue
            base_row = base_lookup.loc[base_id]
            arch = str(ft_row.get('architecture', '')).lower()
            if not any(x in arch for x in ('gemma', 'llama', 'qwen')):
                continue
            keys.add((str(ft_row['family']), str(ft_row['size'])))
            keys.add((str(base_row['family']), str(base_row['size'])))

    return keys


def _generate_facet_grid(
    all_data: dict,
    delta_col: str,
    ft_col: str,
    base_col: str,
    y_label: str,
    stats_mean_key: str,
    stats_std_key: str,
    stats_median_key: str,
    paired_test_description: str,
    out_png: Path,
    out_csv: Path,
    out_stats: Path,
):
    stats_records = []
    fig, axes = plt.subplots(4, 3, figsize=(18, 20), sharey='row')

    for row_idx, ft_config in enumerate(FINETUNE_TYPES):
        df = all_data[ft_config['name']]

        row_max_y = 0.0
        if len(df) > 0:
            for task in TASKS:
                for fam in FAMILIES:
                    subset = df[(df['task'] == task) & (df['family'] == fam)]
                    if len(subset) > 0:
                        row_max_y = max(row_max_y, float(subset[delta_col].max()))

        for col_idx, task in enumerate(TASKS):
            ax = axes[row_idx, col_idx]
            task_data = df[df['task'] == task]

            n_testable_families = sum(
                1 for fam in FAMILIES
                if len(task_data[task_data['family'] == fam]) >= 2
            )

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

                for i, fam in enumerate(FAMILIES):
                    fam_data = task_data[task_data['family'] == fam]
                    if len(fam_data) > 0:
                        x_jitter = add_jitter(
                            np.full(len(fam_data), i, dtype=float), jitter_amount=0.2
                        )
                        ax.scatter(x_jitter, fam_data[delta_col].values, s=50, alpha=0.5,
                                  color=FAMILY_COLORS[fam], edgecolors='black', linewidth=0.5, zorder=10)

                if n_testable_families > 0:
                    for i, fam in enumerate(FAMILIES):
                        fam_data = task_data[task_data['family'] == fam]
                        if len(fam_data) >= 2:
                            _, p = scipy_stats.ttest_rel(
                                fam_data[ft_col].values, fam_data[base_col].values
                            )
                            p_adjusted = min(p * n_testable_families, 1.0)
                            stats_records.append({
                                'finetune_type': ft_config['label'],
                                'task': TASK_TITLES[task],
                                'model_family': FAMILY_LABELS[fam],
                                'n_pairs': len(fam_data),
                                stats_mean_key: fam_data[delta_col].mean(),
                                stats_std_key: fam_data[delta_col].std(),
                                stats_median_key: fam_data[delta_col].median(),
                                'p_value': p,
                                'p_adjusted': p_adjusted,
                                'n_comparisons': n_testable_families,
                                'correction_method': 'Bonferroni (within cell)',
                                'significant': p_adjusted < 0.05,
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
                                stats_mean_key: fam_data[delta_col].mean(),
                                stats_std_key: np.nan,
                                stats_median_key: fam_data[delta_col].median(),
                                'p_value': np.nan,
                                'p_adjusted': np.nan,
                                'n_comparisons': n_testable_families,
                                'correction_method': 'Bonferroni (within cell)',
                                'significant': np.nan,
                            })

            ax.axhline(0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
            ax.grid(True, alpha=0.3, axis='y')
            ax.set_xticks(range(len(FAMILIES)))
            ax.set_xticklabels([FAMILY_LABELS[f] for f in FAMILIES], fontsize=18)
            ax.tick_params(axis='y', labelsize=14)

            if col_idx == 0:
                ax.set_ylabel(f'{ft_config["label"]}\n{y_label}', fontsize=19)
                panel_label = chr(97 + row_idx)  # a, b, c, d for fine-tune rows
                ax.text(-0.18, 1.08, panel_label, transform=ax.transAxes,
                       fontsize=26, fontweight='bold', va='top', ha='left')

            if row_idx == 0:
                ax.set_title(TASK_TITLES[task], fontsize=21, fontweight='bold', pad=15)

            if row_idx == 0 and col_idx == 2:
                legend = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=FAMILY_COLORS[f],
                                     markersize=12, markeredgecolor='black', label=FAMILY_LABELS[f])
                         for f in FAMILIES]
                ax.legend(handles=legend, loc='lower right', fontsize=15)

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.25, wspace=0.15)

    out_png.parent.mkdir(exist_ok=True, parents=True)
    plt.savefig(out_png, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: {out_png}")

    combined_df = pd.concat([
        all_data[ft['name']].assign(finetune_type=ft['name'])
        for ft in FINETUNE_TYPES
    ], ignore_index=True)
    combined_df.to_csv(out_csv, index=False)
    print(f"Saved: {out_csv}")

    stats_df = pd.DataFrame(stats_records)
    stats_df.to_csv(out_stats, index=False)
    print(f"Saved: {out_stats}")

    print("\n" + "=" * 60)
    print("Statistical Testing Summary")
    print("=" * 60)
    print(f"Method: Paired t-test ({paired_test_description})")
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


def generate_combined_facet_plot():
    """Figure 3: Δ F1 (paper default)."""
    all_data = {}
    for ft_config in FINETUNE_TYPES:
        config, results = load_data()
        df = compute_deltas(config, results, ft_config['filter'], 'f1_score', 'f1')
        all_data[ft_config['name']] = df
        print(f"{ft_config['label']}: {len(df)} data points")

    out_dir = ROOT / 'results/fine_tune_figures'
    _generate_facet_grid(
        all_data,
        delta_col='delta_f1',
        ft_col='ft_f1',
        base_col='base_f1',
        y_label='Δ F1 Score',
        stats_mean_key='mean_delta_f1',
        stats_std_key='std_delta_f1',
        stats_median_key='median_delta_f1',
        paired_test_description='fine-tune F1 vs base F1',
        out_png=out_dir / 'delta_f1_facet_plot_across_all_models_and_tasks.png',
        out_csv=out_dir / 'delta_f1_facet_plot_across_all_models_and_tasks_data.csv',
        out_stats=out_dir / 'delta_f1_statistical_analysis_summary.csv',
    )


def generate_delta_parse_facet_plot():
    """Same layout as Figure 3, but Δ parse_success_rate (fine-tune − base)."""
    all_data = {}
    for ft_config in FINETUNE_TYPES:
        config, results = load_data()
        df = compute_deltas(
            config, results, ft_config['filter'],
            'parse_success_rate', 'parse',
        )
        all_data[ft_config['name']] = df
        print(f"{ft_config['label']} (parse): {len(df)} data points")

    out_dir = ROOT / 'results' / 'revision_experiments'
    _generate_facet_grid(
        all_data,
        delta_col='delta_parse',
        ft_col='ft_parse',
        base_col='base_parse',
        y_label='Δ Parse success rate',
        stats_mean_key='mean_delta_parse',
        stats_std_key='std_delta_parse',
        stats_median_key='median_delta_parse',
        paired_test_description='fine-tune parse success vs base parse success',
        out_png=out_dir / 'delta_parse_facet_plot_across_all_models_and_tasks.png',
        out_csv=out_dir / 'delta_parse_facet_plot_across_all_models_and_tasks_data.csv',
        out_stats=out_dir / 'delta_parse_statistical_analysis_summary.csv',
    )


def main():
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
