#!/usr/bin/env python3
"""Compare mental health fine-tuned models vs their base models."""
import pandas as pd
import matplotlib.pyplot as plt
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Load data
config = pd.read_csv(ROOT / 'config/models_config.csv')
results = pd.read_csv(ROOT / 'data/inputs/model_results/all_models_all_tasks.csv')

# Filter to suicidal ideation task
results_si = results[results['task'] == 'suicidal_ideation'].copy()

# Build lookup: lm_studio_id -> (family, size)
id_to_model = dict(zip(config['lm_studio_id'], zip(config['family'], config['size'])))

# Get mental health fine-tunes
mh_models = config[config['model_type'] == 'Mental Health'].copy()

# Shortened display names for long model names
SHORT_NAMES = {
    'guelgamesh01_-_gemma-2b-it-finetuned-mental-health-qa': 'Mental Health QA',
    'ecdev_-_gemma-2b-instruct-ft-mental-health-counseling-conversations': 'Counseling',
    'gemma-2b-unsloth-mental-health-merged': 'MH Merged',
    'gemma-psychology-finetune': 'Psychology',
    'gemma-mental-health-i1': 'Mental Health I1',
    'gemma-2-2b-it-therapist': 'Therapist',
    '268m-therapist': 'Therapist',
    '1b-emotional': 'Emotional',
    '270m': 'MH Fine-tune',
    '1b': 'MH Fine-tune',
    '4.5b-trauma': 'Trauma',
    '4b-mentis': 'Mentis',
}

# Special size labels for Gemma 3n models
GEMMA3N_SIZE_LABELS = {
    4.5: 'E2B',
    6.9: 'E4B',
}

def format_size(param_billions, architecture=None):
    """Format parameter size nicely (e.g., 0.27 -> 270M, 2 -> 2B)."""
    # Special handling for Gemma 3n
    if architecture == 'gemma3n' and param_billions in GEMMA3N_SIZE_LABELS:
        return GEMMA3N_SIZE_LABELS[param_billions]
    if param_billions < 1:
        return f"{int(param_billions * 1000)}M"
    else:
        return f"{param_billions:.1f}B".rstrip('0').rstrip('.')

# Build lookup: lm_studio_id -> param_billions
id_to_params = dict(zip(config['lm_studio_id'], config['param_billions']))

# Map each fine-tune to its base model
records = []
for _, row in mh_models.iterrows():
    ft_family, ft_size = row['family'], row['size']
    base_id = row['Base_Model_LM_Studio_ID']
    arch = row['architecture']
    gemma_gen = row['gemma_generation'] if pd.notna(row['gemma_generation']) else None
    ft_param_billions = row['param_billions'] if pd.notna(row['param_billions']) else 0
    
    # Get fine-tune F1
    ft_match = results_si[(results_si['model_family'] == ft_family) & 
                          (results_si['model_size'] == ft_size)]
    ft_f1 = ft_match['f1_score'].values[0] if len(ft_match) else None
    
    # Get base model F1 and params
    base_f1 = None
    base_family, base_size = None, None
    base_param_billions = ft_param_billions  # Default to fine-tune size if base unknown
    if pd.notna(base_id) and base_id in id_to_model:
        base_family, base_size = id_to_model[base_id]
        base_match = results_si[(results_si['model_family'] == base_family) & 
                                (results_si['model_size'] == base_size)]
        base_f1 = base_match['f1_score'].values[0] if len(base_match) else None
        if base_id in id_to_params:
            base_param_billions = id_to_params[base_id]
    
    records.append({
        'ft_family': ft_family,
        'ft_size': ft_size,
        'ft_f1': ft_f1,
        'base_id': base_id if pd.notna(base_id) else None,
        'base_family': base_family,
        'base_size': base_size,
        'base_f1': base_f1,
        'architecture': arch,
        'base_type': row['Base_Model_Type'] if pd.notna(row['Base_Model_Type']) else None,
        'gemma_gen': gemma_gen,
        'ft_param_billions': ft_param_billions,
        'base_param_billions': base_param_billions,
    })

df = pd.DataFrame(records)

# Group by architecture family for plotting
arch_groups = {
    'gemma': ['gemma', 'gemma2', 'gemma3', 'gemma3n'],
    'llama': ['llama'],
    'qwen': ['qwen', 'qwen2', 'qwen3'],
}

def get_arch_group(arch):
    for group, archs in arch_groups.items():
        if arch in archs:
            return group
    return 'other'

df['arch_group'] = df['architecture'].apply(get_arch_group)

# Output dir
out_dir = ROOT / 'results/mental_health_finetune_analysis'
out_dir.mkdir(exist_ok=True)

def plot_gemma_row(ax, df_subset, results_task, task_name, show_xlabel=True, show_legend=False):
    """Plot one row of the Gemma facet plot for a single task."""
    version_order = {'gemma': 1, 'gemma2': 2, 'gemma3': 3, 'gemma3n': 4}
    version_labels = {1: 'Gemma 1', 2: 'Gemma 2', 3: 'Gemma 3', 4: 'Gemma 3n'}
    
    df_subset = df_subset.copy()
    df_subset['version_num'] = df_subset['architecture'].map(version_order).fillna(5)
    df_subset = df_subset.sort_values(['version_num', 'base_param_billions']).reset_index(drop=True)
    
    x_pos = 0
    x_ticks = []
    x_labels = []
    bar_width = 0.35
    
    version_ranges = {}
    current_version = None
    version_start = 0
    processed_bases = set()
    
    for _, row in df_subset.iterrows():
        base_key = (row['base_family'], row['base_size']) if pd.notna(row['base_family']) else ('NA', row.name)
        version = int(row['version_num'])
        
        if current_version != version:
            if current_version is not None:
                version_ranges[current_version] = (version_start, x_pos - 0.5)
                x_pos += 0.8
            current_version = version
            version_start = x_pos
        
        if base_key in processed_bases:
            continue
        
        if pd.notna(row['base_family']):
            same_base = df_subset[(df_subset['base_family'] == base_key[0]) & 
                                   (df_subset['base_size'] == base_key[1])].copy()
        else:
            same_base = df_subset[df_subset.index == row.name].copy()
        processed_bases.add(base_key)
        
        same_base = same_base.sort_values('ft_f1', ascending=True)
        
        # Get F1 for this task
        base_f1 = None
        if pd.notna(row['base_family']):
            base_match = results_task[(results_task['model_family'] == row['base_family']) & 
                                       (results_task['model_size'] == row['base_size'])]
            base_f1 = base_match['f1_score'].values[0] if len(base_match) else None
        
        size_label = format_size(row['base_param_billions'], row['architecture'])
        base_type = row['base_type']
        
        # Plot base model bar (blue)
        if pd.notna(base_f1):
            hatch = '///' if base_type == 'PT' else None
            ax.bar(x_pos, base_f1, bar_width, color='steelblue', hatch=hatch, edgecolor='black')
            ax.text(x_pos, base_f1 + 0.02, f'{base_f1:.3f}', ha='center', va='bottom', fontsize=6)
            x_ticks.append(x_pos)
            x_labels.append(f'Gemma-{size_label}')
        else:
            ax.bar(x_pos, 0, bar_width, color='lightgray', edgecolor='black')
            ax.text(x_pos, 0.02, 'N/A', ha='center', va='bottom', fontsize=6)
            x_ticks.append(x_pos)
            x_labels.append(f'Gemma-{size_label}\n(N/A)')
        
        x_pos += bar_width + 0.05
        
        # Plot fine-tune bars (modern red)
        for _, ft_row in same_base.iterrows():
            ft_match = results_task[(results_task['model_family'] == ft_row['ft_family']) & 
                                     (results_task['model_size'] == ft_row['ft_size'])]
            ft_f1 = ft_match['f1_score'].values[0] if len(ft_match) else 0
            ft_f1 = ft_f1 if pd.notna(ft_f1) else 0
            
            ax.bar(x_pos, ft_f1, bar_width, color='#E74C3C', edgecolor='black')
            label = f'{ft_f1:.3f}' if ft_f1 > 0 else '0.000'
            ax.text(x_pos, ft_f1 + 0.02, label, ha='center', va='bottom', fontsize=6)
            x_ticks.append(x_pos)
            display_name = SHORT_NAMES.get(ft_row['ft_size'], ft_row['ft_size'])
            x_labels.append(display_name)
            x_pos += bar_width + 0.05
        
        x_pos += 0.5
    
    if current_version is not None:
        version_ranges[current_version] = (version_start, x_pos - 0.5)
    
    ax.set_xticks(x_ticks)
    if show_xlabel:
        ax.set_xticklabels(x_labels, fontsize=6, rotation=45, ha='right')
    else:
        ax.set_xticklabels([])
    ax.set_ylabel('F1 Score')
    ax.set_ylim(0, 1.15)
    ax.set_title(task_name, fontsize=14)
    
    # Version underlines
    y_line = -0.22 if show_xlabel else -0.08
    for ver, (start, end) in version_ranges.items():
        if ver in version_labels:
            mid = (start + end) / 2
            ax.annotate('', xy=(start, y_line), xytext=(end, y_line),
                       xycoords=('data', 'axes fraction'), textcoords=('data', 'axes fraction'),
                       arrowprops=dict(arrowstyle='-', color='black', lw=2))
            ax.text(mid, y_line - 0.04, version_labels[ver], ha='center', va='top', 
                   fontsize=8, fontweight='bold', transform=ax.get_xaxis_transform())
    
    if show_legend:
        ax.legend([plt.Rectangle((0,0),1,1, facecolor='#E74C3C', edgecolor='black'),
                   plt.Rectangle((0,0),1,1, facecolor='steelblue', edgecolor='black'), 
                   plt.Rectangle((0,0),1,1, facecolor='steelblue', hatch='///', edgecolor='black')],
                  ['Mental Health Fine-tune', 'Base (IT)', 'Base (PT)'],
                  loc='upper left', fontsize=8)
    
    return x_pos


def make_gemma_facet_plot(df_gemma, results_all, filename):
    """Create 3-row facet plot for Gemma models across all tasks."""
    tasks = [
        ('suicidal_ideation', 'Suicidal Ideation'),
        ('therapy_request', 'Therapy Request'),
        ('therapy_engagement', 'Therapy Engagement'),
    ]
    
    fig, axes = plt.subplots(3, 1, figsize=(16, 14), sharex=False)
    
    for idx, (task_key, task_name) in enumerate(tasks):
        results_task = results_all[results_all['task'] == task_key]
        show_xlabel = (idx == 2)  # Only show x labels on bottom row
        show_legend = (idx == 0)  # Only show legend on top row
        plot_gemma_row(axes[idx], df_gemma, results_task, task_name, show_xlabel, show_legend)
    
    fig.suptitle('F1 Scores of Fine-tuned vs Base Models (Gemma)', fontsize=16, fontweight='bold', y=0.99)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15, top=0.96, hspace=0.3)
    plt.savefig(out_dir / filename, dpi=150)
    # plt.savefig(out_dir / filename.replace('.png', '.pdf'))
    plt.close()
    print(f'Saved {filename}')


def plot_other_row(ax, df_subset, results_task, task_name, arch_name, show_xlabel=True, show_legend=False):
    """Plot one row for Llama/Qwen facet plot."""
    df_subset = df_subset.copy()
    df_subset = df_subset.sort_values(['base_param_billions']).reset_index(drop=True)
    
    x_pos = 0
    x_ticks = []
    x_labels = []
    bar_width = 0.35
    processed_bases = set()
    
    for _, row in df_subset.iterrows():
        base_key = (row['base_family'], row['base_size']) if pd.notna(row['base_family']) else ('NA', row.name)
        
        if base_key in processed_bases:
            continue
        
        if pd.notna(row['base_family']):
            same_base = df_subset[(df_subset['base_family'] == base_key[0]) & 
                                   (df_subset['base_size'] == base_key[1])].copy()
        else:
            same_base = df_subset[df_subset.index == row.name].copy()
        processed_bases.add(base_key)
        
        same_base = same_base.sort_values('ft_f1', ascending=True)
        
        # Get F1 for this task
        base_f1 = None
        if pd.notna(row['base_family']):
            base_match = results_task[(results_task['model_family'] == row['base_family']) & 
                                       (results_task['model_size'] == row['base_size'])]
            base_f1 = base_match['f1_score'].values[0] if len(base_match) else None
        
        size_label = format_size(row['base_param_billions'])
        base_type = row['base_type']
        
        # Plot base model bar
        if pd.notna(base_f1):
            hatch = '///' if base_type == 'PT' else None
            ax.bar(x_pos, base_f1, bar_width, color='steelblue', hatch=hatch, edgecolor='black')
            ax.text(x_pos, base_f1 + 0.02, f'{base_f1:.3f}', ha='center', va='bottom', fontsize=6)
            x_ticks.append(x_pos)
            x_labels.append(f'{arch_name}-{size_label}')
        else:
            ax.bar(x_pos, 0, bar_width, color='lightgray', edgecolor='black')
            ax.text(x_pos, 0.02, 'N/A', ha='center', va='bottom', fontsize=6)
            x_ticks.append(x_pos)
            x_labels.append(f'{arch_name}-{size_label}\n(N/A)')
        
        x_pos += bar_width + 0.05
        
        # Plot fine-tune bars
        for _, ft_row in same_base.iterrows():
            ft_match = results_task[(results_task['model_family'] == ft_row['ft_family']) & 
                                     (results_task['model_size'] == ft_row['ft_size'])]
            ft_f1 = ft_match['f1_score'].values[0] if len(ft_match) else 0
            ft_f1 = ft_f1 if pd.notna(ft_f1) else 0
            
            ax.bar(x_pos, ft_f1, bar_width, color='#E74C3C', edgecolor='black')
            label = f'{ft_f1:.3f}' if ft_f1 > 0 else '0.000'
            ax.text(x_pos, ft_f1 + 0.02, label, ha='center', va='bottom', fontsize=6)
            x_ticks.append(x_pos)
            display_name = SHORT_NAMES.get(ft_row['ft_size'], ft_row['ft_size'])
            x_labels.append(display_name)
            x_pos += bar_width + 0.05
        
        x_pos += 0.3
    
    ax.set_xticks(x_ticks)
    if show_xlabel:
        ax.set_xticklabels(x_labels, fontsize=6, rotation=45, ha='right')
    else:
        ax.set_xticklabels([])
    ax.set_ylabel('F1 Score')
    ax.set_ylim(0, 1.15)
    ax.set_title(task_name, fontsize=14)
    
    if show_legend:
        ax.legend([plt.Rectangle((0,0),1,1, facecolor='#E74C3C', edgecolor='black'),
                   plt.Rectangle((0,0),1,1, facecolor='steelblue', edgecolor='black'), 
                   plt.Rectangle((0,0),1,1, facecolor='steelblue', hatch='///', edgecolor='black')],
                  ['Mental Health Fine-tune', 'Base (IT)', 'Base (PT)'],
                  loc='upper left', fontsize=8)


def make_facet_plot(df_subset, results_all, arch_name, filename):
    """Create 3-row facet plot for Llama/Qwen models across all tasks."""
    tasks = [
        ('suicidal_ideation', 'Suicidal Ideation'),
        ('therapy_request', 'Therapy Request'),
        ('therapy_engagement', 'Therapy Engagement'),
    ]
    
    fig, axes = plt.subplots(3, 1, figsize=(16, 14), sharex=False)
    
    for idx, (task_key, task_name) in enumerate(tasks):
        results_task = results_all[results_all['task'] == task_key]
        show_xlabel = (idx == 2)
        show_legend = (idx == 0)
        plot_other_row(axes[idx], df_subset, results_task, task_name, arch_name, show_xlabel, show_legend)
    
    fig.suptitle(f'F1 Scores of Fine-tuned vs Base Models ({arch_name})', fontsize=16, fontweight='bold', y=0.99)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15, top=0.96, hspace=0.3)
    plt.savefig(out_dir / filename, dpi=150)
    # plt.savefig(out_dir / filename.replace('.png', '.pdf'))
    plt.close()
    print(f'Saved {filename}')

# Create plots for each architecture group
for group_name in ['gemma', 'llama', 'qwen']:
    df_group = df[df['arch_group'] == group_name].copy()
    if len(df_group) == 0:
        continue
    if group_name == 'gemma':
        make_gemma_facet_plot(df_group, results,
                              f'{group_name}_mental_health_vs_base_f1_comparison.png')
    else:
        make_facet_plot(df_group, results, group_name.title(),
                        f'{group_name}_mental_health_vs_base_f1_comparison.png')

# Save summary CSV
df.to_csv(out_dir / 'mental_health_finetune_comparison_summary.csv', index=False)
print(f'Saved summary CSV with {len(df)} rows')
