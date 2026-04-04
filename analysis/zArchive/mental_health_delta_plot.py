#!/usr/bin/env python3
"""
Δ-Performance Plot: Fine-tuning Effect vs Model Size

Shows performance change (fine-tuned - base) as a function of model size,
with individual points for each fine-tune and LOESS trend lines.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Load data
config = pd.read_csv(ROOT / 'config/models_config.csv')
results = pd.read_csv(ROOT / 'data/inputs/model_results/all_models_all_tasks.csv')

# Filter to Mental Health fine-tunes that have a base model specified
fine_tunes = config[(config['Base_Model_LM_Studio_ID'].notna()) & 
                    (config['model_type'] == 'Mental Health')].copy()
print(f"Total models in config: {len(config)}")
print(f"Mental Health fine-tunes with base model: {len(fine_tunes)}")

# For each fine-tune, get base model info
base_lookup = config.set_index('lm_studio_id')

# Prepare long-format data: one row per (fine-tune, task)
records = []
tasks = ['suicidal_ideation', 'therapy_request', 'therapy_engagement']
task_labels = {
    'suicidal_ideation': 'Suicidal Ideation',
    'therapy_request': 'Therapy Request',
    'therapy_engagement': 'Therapy Engagement',
}

for _, ft_row in fine_tunes.iterrows():
    base_id = ft_row['Base_Model_LM_Studio_ID']
    
    # Get base model info
    if base_id not in base_lookup.index:
        print(f"WARNING: Base model {base_id} not found in config for {ft_row['lm_studio_id']}")
        continue
    
    base_row = base_lookup.loc[base_id]
    
    # Get family for grouping (gemma, llama, qwen)
    arch = ft_row['architecture'].lower()
    if 'gemma' in arch:
        family = 'gemma'
    elif 'llama' in arch:
        family = 'llama'
    elif 'qwen' in arch:
        family = 'qwen'
    else:
        continue
    
    # Get version from base model
    base_version = base_row['version']
    
    # For gemma3n models, override version to '3n'
    if base_row['architecture'] == 'gemma3n':
        base_version = '3n'
    # Collapse 3.1, 3.2, 3.3 -> 3
    elif base_version in ['3.1', '3.2', '3.3']:
        base_version = '3'
    
    for task in tasks:
        # Get fine-tune score
        ft_match = results[(results['task'] == task) & 
                          (results['model_family'] == ft_row['family']) & 
                          (results['model_size'] == ft_row['size'])]
        ft_score = ft_match['f1_score'].values[0] if len(ft_match) else None
        
        # Get base score
        base_match = results[(results['task'] == task) & 
                            (results['model_family'] == base_row['family']) & 
                            (results['model_size'] == base_row['size'])]
        base_score = base_match['f1_score'].values[0] if len(base_match) else None
        
        # Get accuracy scores
        ft_acc = ft_match['accuracy'].values[0] if len(ft_match) else None
        base_acc = base_match['accuracy'].values[0] if len(base_match) else None
        
        if pd.notna(ft_score) and pd.notna(base_score) and pd.notna(ft_acc) and pd.notna(base_acc):
            records.append({
                'family': family,
                'version': str(base_version),
                'params_b': ft_row['param_billions'],
                'task': task,
                'task_label': task_labels[task],
                'delta_f1': ft_score - base_score,
                'delta_accuracy': ft_acc - base_acc,
            })

df_long = pd.DataFrame(records)

print(f"\nLong-format data: {len(df_long)} rows")
print(f"Families: {df_long['family'].unique()}")
print(f"Tasks: {df_long['task'].nunique()}")
print("\nVersion distribution by family:")
for family in ['gemma', 'llama', 'qwen']:
    family_data = df_long[df_long['family'] == family]
    if len(family_data) > 0:
        versions = family_data['version'].value_counts().sort_index()
        print(f"{family}: {dict(versions)}")

# Version-to-marker and alpha mappings
version_markers = {
    '1': 'o',      # circle
    '1.5': '^',    # triangle up
    '2': 'D',      # diamond
    '3': 'v',      # triangle down
    '3n': 'P',     # plus (filled)
}

version_alphas = {
    '1': 0.2,
    '1.5': 0.4,
    '2': 0.6,
    '3': 0.8,
    '3n': 1.0,
}

# Family colors (consistent with other plots)
family_colors = {
    'gemma': '#E74C3C',  # Red
    'llama': '#3498DB',  # Blue  
    'qwen': '#2ECC71',   # Green
}

# Create plot: 2 rows x 3 columns (rows = metric, columns = task)
fig, axes = plt.subplots(2, 3, figsize=(18, 10), sharex=True)

families = ['gemma', 'llama', 'qwen']
family_labels = {'gemma': 'Gemma', 'llama': 'Llama', 'qwen': 'Qwen'}

metrics = ['delta_f1', 'delta_accuracy']
metric_labels = {
    'delta_f1': 'Δ F1 Score',
    'delta_accuracy': 'Δ Accuracy'
}

for row_idx, metric in enumerate(metrics):
    for col_idx, task in enumerate(tasks):
        ax = axes[row_idx, col_idx]
    
        # Get all data for this task (across all families)
        task_data = df_long[df_long['task'] == task].copy()
        
        # Plot all families on this task panel
        for family in families:
            # Filter data for this family and task
            family_task_data = task_data[task_data['family'] == family].copy()
            
            if len(family_task_data) == 0:
                continue
            
            # Plot points with version-specific markers and alphas - NO JITTER
            for _, row_data in family_task_data.iterrows():
                version = row_data['version']
                marker = version_markers.get(version, 'o')
                alpha = version_alphas.get(version, 0.6)
                x_log = np.log10(row_data['params_b'])
                
                ax.scatter(x_log, row_data[metric], 
                          color=family_colors[family], 
                          marker=marker, s=100, alpha=alpha,
                          edgecolors='black', linewidth=0.5)
        
        # Zero reference line
        ax.axhline(0, color='gray', linestyle='--', linewidth=1.5, alpha=0.7, zorder=1)
        
        # Grid
        ax.grid(True, alpha=0.3, axis='both', zorder=0)
        
        # Labels
        if col_idx == 0:
            ax.set_ylabel(metric_labels[metric], fontsize=11)
        if row_idx == 1:
            ax.set_xlabel('log₁₀(Parameters in Billions)', fontsize=11)
        
        # Column titles (tasks) - only on top row
        if row_idx == 0:
            ax.set_title(task_labels[task], fontsize=12, fontweight='bold', pad=10)
        
        # Add legend - only on top-left panel
        if row_idx == 0 and col_idx == 0:
            family_elements = []
            version_elements = []
            
            # Family colors (points only)
            family_elements.append(plt.Line2D([0], [0], color='white', label='Family:', 
                                             linewidth=0, marker=''))
            for family in families:
                family_elements.append(plt.Line2D([0], [0], color=family_colors[family], 
                                                 linewidth=0, marker='o', markersize=8,
                                                 markeredgecolor='black', markeredgewidth=0.5,
                                                 label=f'{family_labels[family]}'))
            
            # Version shapes
            version_elements.append(plt.Line2D([0], [0], color='white', label='Version:', 
                                             linewidth=0, marker=''))
            
            # Get unique versions, sort with 3n after 3
            def version_sort_key(v):
                if v == '3n':
                    return 3.5
                else:
                    try:
                        return float(v)
                    except:
                        return 999
            
            all_versions = sorted(df_long['version'].unique(), key=version_sort_key)
            for v in all_versions:
                if v in version_markers:
                    version_elements.append(plt.Line2D([0], [0], marker=version_markers[v], 
                                                     color='gray', linestyle='', 
                                                     markersize=8, alpha=version_alphas[v],
                                                     markeredgecolor='black', markeredgewidth=0.5,
                                                     label=f'v{v}'))
            
            # Combine and use ncol=2 for side-by-side layout
            all_elements = family_elements + version_elements
            ax.legend(handles=all_elements, loc='lower left', fontsize=9, 
                     framealpha=0.95, ncol=2)

# Overall title
fig.suptitle('Fine-tuning Performance Gain by Model Size', 
             fontsize=16, fontweight='bold', y=1.02)

plt.tight_layout()
plt.subplots_adjust(top=0.94, hspace=0.25, wspace=0.15)

# Save
out_dir = ROOT / 'results/mental_health_finetune_analysis'
out_file = out_dir / 'mental_health_delta_performance.png'
plt.savefig(out_file, dpi=150, bbox_inches='tight')
plt.close()

print(f"\nSaved: {out_file}")
