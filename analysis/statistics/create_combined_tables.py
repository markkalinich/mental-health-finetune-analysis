#!/usr/bin/env python3
"""
Create combined regression tables with all 3 tasks side-by-side.
Output: HTML only, 2 tables (F1 Score, Accuracy)
"""

import pandas as pd
from pathlib import Path


def generate_per_task_files(stats_dir: Path):
    """
    Generate per-task regression CSV files from all_coefficients.csv.
    This creates the legacy format files that create_combined_html_table expects.
    """
    all_coef_path = stats_dir / "all_coefficients.csv"
    if not all_coef_path.exists():
        print(f"Warning: {all_coef_path} not found, skipping per-task file generation")
        return
    
    df = pd.read_csv(all_coef_path)
    
    # Map task names to file names
    task_map = {
        'Suicidal Ideation': 'suicidal_ideation',
        'Therapy Request': 'therapy_request',
        'Therapy Engagement': 'therapy_engagement'
    }
    
    dv_map = {
        'F1 Score': 'f1_score',
        'Accuracy': 'accuracy'
    }
    
    for task, task_file in task_map.items():
        for dv, dv_file in dv_map.items():
            task_df = df[(df['Task'] == task) & (df['DV'] == dv)]
            
            if len(task_df) == 0:
                continue
            
            # Format into the expected legacy format
            output_rows = []
            for _, row in task_df.iterrows():
                ci_str = f"[{row['95% CI Lower']:.3f}, {row['95% CI Upper']:.3f}]"
                bonf_ci_str = f"[{row['Bonf CI Lower']:.3f}, {row['Bonf CI Upper']:.3f}]"
                
                output_rows.append({
                    'Variable': row['Variable'],
                    'β': round(row['β'], 3),
                    'SE': round(row['SE'], 3),
                    't': round(row['t'], 2),
                    'p': round(row['p'], 4),
                    'p_bonf': round(row['p_bonferroni'], 4),
                    'p_fdr': round(row['p_fdr'], 4),
                    '95% CI': ci_str,
                    'Bonf CI': bonf_ci_str
                })
            
            # Add summary stats
            if len(task_df) > 0:
                first_row = task_df.iloc[0]
                output_rows.append({'Variable': 'R²', 'β': round(first_row['R²'], 3)})
                output_rows.append({'Variable': 'Adj R²', 'β': round(first_row['Adj R²'], 3)})
                output_rows.append({'Variable': 'N', 'β': int(first_row['N'])})
            
            output_df = pd.DataFrame(output_rows)
            output_path = stats_dir / f"regression_{task_file}_{dv_file}.csv"
            output_df.to_csv(output_path, index=False)
            print(f"  Generated: {output_path.name}")


def load_regression_data(csv_path: Path):
    """Load regression CSV and extract coefficients, CIs, and p-values (raw, Bonferroni, and FDR)"""
    df = pd.read_csv(csv_path)
    
    # Extract coefficient rows (before the summary stats)
    coef_rows = []
    for idx, row in df.iterrows():
        var = str(row['Variable'])
        if var in ['', 'R²', 'Adj R²', 'N', 'nan'] or pd.isna(row['β']):
            break
        coef_rows.append(row)
    
    # Include both raw and Bonferroni-adjusted CIs
    cols_to_keep = ['Variable', 'β', '95% CI', 'Bonf CI', 'p', 'p_bonf', 'p_fdr']
    available_cols = [c for c in cols_to_keep if c in df.columns]
    coef_df = pd.DataFrame(coef_rows)[available_cols]
    
    # Extract summary stats
    summary_stats = {}
    for idx, row in df.iterrows():
        var = str(row['Variable'])
        if var in ['R²', 'Adj R²', 'N']:
            summary_stats[var] = row['β']
    
    return coef_df, summary_stats


def create_combined_html_table(stats_dir: Path, dv: str, title: str, output_file: str, correction_type: str = 'bonferroni'):
    """Create combined HTML table for one DV across all 3 tasks
    
    Args:
        correction_type: 'bonferroni' or 'fdr' - which correction to use for significance stars
    """
    
    # Load data for all 3 tasks
    si_df, si_summary = load_regression_data(stats_dir / f"regression_suicidal_ideation_{dv}.csv")
    tr_df, tr_summary = load_regression_data(stats_dir / f"regression_therapy_request_{dv}.csv")
    te_df, te_summary = load_regression_data(stats_dir / f"regression_therapy_engagement_{dv}.csv")
    
    # Rename columns for merging
    si_df = si_df.rename(columns={'β': 'β_SI', '95% CI': 'CI_SI', 'Bonf CI': 'BonfCI_SI', 'p': 'p_SI', 'p_bonf': 'p_bonf_SI', 'p_fdr': 'p_fdr_SI'})
    tr_df = tr_df.rename(columns={'β': 'β_TR', '95% CI': 'CI_TR', 'Bonf CI': 'BonfCI_TR', 'p': 'p_TR', 'p_bonf': 'p_bonf_TR', 'p_fdr': 'p_fdr_TR'})
    te_df = te_df.rename(columns={'β': 'β_TE', '95% CI': 'CI_TE', 'Bonf CI': 'BonfCI_TE', 'p': 'p_TE', 'p_bonf': 'p_bonf_TE', 'p_fdr': 'p_fdr_TE'})
    
    # Merge on Variable
    combined = si_df.merge(tr_df, on='Variable', how='outer')
    combined = combined.merge(te_df, on='Variable', how='outer')
    
    # Create explicit ordering: Intercept, Version 2/3/4, Parameter Size, Fine-Tunes, Families
    def get_variable_order(var):
        """Assign explicit order as requested"""
        order_map = {
            'Intercept': 0,
            'Version: 2': 1,
            'Version: 3': 2,
            'Version: 4': 3,
            'Parameter Size (B)': 4,
            'Fine-Tune Type: Instruction-Tuned': 5,
            'Fine-Tune Type: Mental Health Tuned': 6,
            'Fine-Tune Type: Medical-Tuned': 7,
            'Fine-Tune Type: Safety-Tuned': 8,
            'Family: LLaMA': 9,
            'Family: Qwen': 10,
        }
        return order_map.get(var, 999)  # Unknown variables go to end
    
    combined['order'] = combined['Variable'].apply(get_variable_order)
    combined = combined.sort_values('order').drop('order', axis=1)
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<style>
.container {{
    width: fit-content;
    margin: 20px auto;
}}
table {{
    border-collapse: collapse;
    margin: 0 auto;
    font-family: Arial, sans-serif;
    font-size: 10px;
}}
caption {{
    font-weight: bold;
    font-size: 1.4em;
    margin-bottom: 15px;
}}
th {{
    background-color: #f0f0f0;
    padding: 6px 4px;
    text-align: center;
    border: 1px solid #ccc;
}}
th.variable-col {{
    text-align: left;
    width: 140px;
}}
th.task-header {{
    border-top: 2px solid black;
    border-bottom: 1px solid #999;
    font-weight: bold;
    font-size: 1.1em;
}}
td {{
    padding: 5px 4px;
    border: 1px solid #ddd;
}}
td:first-child {{
    text-align: left;
    font-size: 9px;
    max-width: 140px;
    word-wrap: break-word;
}}
td.coef, td.ci {{
    text-align: center;
    font-size: 9px;
}}
.summary-row {{
    border-top: 2px solid black;
    font-weight: bold;
    background-color: #f9f9f9;
}}
.notes-row {{
    background-color: #f9f9f9;
}}
.notes-row td {{
    padding: 10px;
    font-size: 0.9em;
    line-height: 1.6;
}}
</style>
</head>
<body>

<div class="container">
<table>
<caption>{title}</caption>
<thead>
<tr>
<th class="variable-col" rowspan="2">Variable</th>
<th class="task-header" colspan="2">Suicidal Ideation</th>
<th class="task-header" colspan="2">Therapy Request</th>
<th class="task-header" colspan="2">Therapy Engagement</th>
</tr>
<tr>
<th>β</th>
<th>95% CI</th>
<th>β</th>
<th>95% CI</th>
<th>β</th>
<th>95% CI</th>
</tr>
</thead>
<tbody>
"""
    
    # Choose which p-value column and CI column to use based on correction type
    p_col_suffix = '_bonf' if correction_type == 'bonferroni' else '_fdr'
    # For Bonferroni, use Bonferroni-adjusted CIs; for FDR, use raw 95% CIs
    ci_col_suffix = 'BonfCI' if correction_type == 'bonferroni' else 'CI'
    
    def get_significance_stars(p_value):
        """Return significance stars based on p-value (numeric or string with asterisks)."""
        if pd.isna(p_value) or p_value == "":
            return ""
        
        # Handle numeric p-values
        if isinstance(p_value, (int, float)):
            if p_value < 0.001:
                return '<sup>***</sup>'
            elif p_value < 0.01:
                return '<sup>**</sup>'
            elif p_value < 0.05:
                return '<sup>*</sup>'
            return ""
        
        # Handle string p-values (legacy format with asterisks)
        if isinstance(p_value, str):
            if '***' in p_value:
                return '<sup>***</sup>'
            elif '**' in p_value:
                return '<sup>**</sup>'
            elif '*' in p_value:
                return '<sup>*</sup>'
        return ""
    
    # Add coefficient rows
    for idx, row in combined.iterrows():
        var = row['Variable']
        
        # Format SI (use selected correction for significance stars and CIs)
        si_beta = f"{row['β_SI']:.3f}" if pd.notna(row['β_SI']) else "—"
        si_ci_col = f'{ci_col_suffix}_SI'
        si_ci = row.get(si_ci_col, row.get('CI_SI', '—'))
        if pd.isna(si_ci):
            si_ci = row.get('CI_SI', '—')
        si_p = row.get(f'p{p_col_suffix}_SI', "")
        
        if pd.notna(row['β_SI']):
            si_beta += get_significance_stars(si_p)
        
        # Format TR (use selected correction for significance stars and CIs)
        tr_beta = f"{row['β_TR']:.3f}" if pd.notna(row['β_TR']) else "—"
        tr_ci_col = f'{ci_col_suffix}_TR'
        tr_ci = row.get(tr_ci_col, row.get('CI_TR', '—'))
        if pd.isna(tr_ci):
            tr_ci = row.get('CI_TR', '—')
        tr_p = row.get(f'p{p_col_suffix}_TR', "")
        
        if pd.notna(row['β_TR']):
            tr_beta += get_significance_stars(tr_p)
        
        # Format TE (use selected correction for significance stars and CIs)
        te_beta = f"{row['β_TE']:.3f}" if pd.notna(row['β_TE']) else "—"
        te_ci_col = f'{ci_col_suffix}_TE'
        te_ci = row.get(te_ci_col, row.get('CI_TE', '—'))
        if pd.isna(te_ci):
            te_ci = row.get('CI_TE', '—')
        te_p = row.get(f'p{p_col_suffix}_TE', "")
        
        if pd.notna(row['β_TE']):
            te_beta += get_significance_stars(te_p)
        
        html += f"""<tr>
<td>{var}</td>
<td class="coef">{si_beta}</td>
<td class="ci">{si_ci}</td>
<td class="coef">{tr_beta}</td>
<td class="ci">{tr_ci}</td>
<td class="coef">{te_beta}</td>
<td class="ci">{te_ci}</td>
</tr>
"""
    
    # Add summary statistics
    html += f"""<tr class="summary-row">
<td>R²</td>
<td class="coef">{si_summary['R²']:.3f}</td>
<td class="ci"></td>
<td class="coef">{tr_summary['R²']:.3f}</td>
<td class="ci"></td>
<td class="coef">{te_summary['R²']:.3f}</td>
<td class="ci"></td>
</tr>
<tr class="summary-row">
<td>Adj R²</td>
<td class="coef">{si_summary['Adj R²']:.3f}</td>
<td class="ci"></td>
<td class="coef">{tr_summary['Adj R²']:.3f}</td>
<td class="ci"></td>
<td class="coef">{te_summary['Adj R²']:.3f}</td>
<td class="ci"></td>
</tr>
<tr class="summary-row">
<td>N</td>
<td class="coef">{int(si_summary['N'])}</td>
<td class="ci"></td>
<td class="coef">{int(tr_summary['N'])}</td>
<td class="ci"></td>
<td class="coef">{int(te_summary['N'])}</td>
<td class="ci"></td>
</tr>
"""
    
    # Add notes row with appropriate correction method
    correction_name = "Bonferroni" if correction_type == 'bonferroni' else "FDR (Benjamini-Hochberg)"
    correction_desc = "p-values multiplied by number of tests per model" if correction_type == 'bonferroni' else "False Discovery Rate control"
    ci_desc = "Bonferroni-adjusted (α = 0.05/n_tests)" if correction_type == 'bonferroni' else "Raw 95% (α = 0.05)"
    
    html += f"""<tr class="notes-row">
<td colspan="7" style="text-align: left; padding: 10px; font-size: 0.85em; color: #666; border-top: 2px solid black;">
<strong>Significance levels ({correction_name}-corrected):</strong> <sup>*</sup>p&lt;0.05; <sup>**</sup>p&lt;0.01; <sup>***</sup>p&lt;0.001<br>
<strong>Multiple testing correction:</strong> {correction_name} correction applied to p-values AND confidence intervals<br>
<strong>Confidence intervals:</strong> {ci_desc}<br>
<strong>Reference categories:</strong> Family=Gemma, Version=1, Fine-Tune Type=Base Model<br>
<strong>Standard errors:</strong> HC3 heteroscedasticity-consistent (robust)
</td>
</tr>
"""
    
    html += """</tbody>
</table>

</div> <!-- close container -->

</body>
</html>
"""
    
    output_path = stats_dir / output_file
    with open(output_path, 'w') as f:
        f.write(html)
    
    print(f"✓ {title}")
    print(f"  File: {output_file}\n")


if __name__ == "__main__":
    stats_dir = Path(__file__).parent.parent.parent / "results" / "statistics"
    
    print("="*80)
    print("CREATING COMBINED REGRESSION TABLES (ALL 3 TASKS SIDE-BY-SIDE)")
    print("="*80)
    print()
    
    # First, generate per-task files from all_coefficients.csv
    print("Generating per-task regression CSV files from all_coefficients.csv...")
    generate_per_task_files(stats_dir)
    print()
    
    # Create F1 Score tables (both Bonferroni and FDR)
    print("F1 Score - Bonferroni correction:")
    create_combined_html_table(
        stats_dir,
        dv="f1_score",
        title="Regression Results: F1 Score (Bonferroni-corrected)",
        output_file="combined_regression_f1_score_bonferroni.html",
        correction_type='bonferroni'
    )
    
    print("F1 Score - FDR correction:")
    create_combined_html_table(
        stats_dir,
        dv="f1_score",
        title="Regression Results: F1 Score (FDR-corrected)",
        output_file="combined_regression_f1_score_fdr.html",
        correction_type='fdr'
    )
    
    # Create Accuracy tables (both Bonferroni and FDR)
    print("Accuracy - Bonferroni correction:")
    create_combined_html_table(
        stats_dir,
        dv="accuracy",
        title="Regression Results: Accuracy (Bonferroni-corrected)",
        output_file="combined_regression_accuracy_bonferroni.html",
        correction_type='bonferroni'
    )
    
    print("Accuracy - FDR correction:")
    create_combined_html_table(
        stats_dir,
        dv="accuracy",
        title="Regression Results: Accuracy (FDR-corrected)",
        output_file="combined_regression_accuracy_fdr.html",
        correction_type='fdr'
    )
    
    print("="*80)
    print("✓ ALL COMBINED TABLES CREATED (HTML ONLY)")
    print("="*80)
    print("\nLocation: results/statistics/combined_regression_*_bonferroni.html")
    print("          results/statistics/combined_regression_*_fdr.html")
    print("\nTwo versions created for each DV:")
    print("  - Bonferroni: Conservative family-wise error rate control")
    print("  - FDR: Less conservative false discovery rate control")
