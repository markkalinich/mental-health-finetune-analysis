#!/usr/bin/env python3
"""
Create standard regression tables - ONE PER DEPENDENT VARIABLE.

Standard format:
- Rows = Variables
- Columns = β, SE, t, p, [95% CI]
- Bottom = R², Adj R², F-stat, N
"""

import pandas as pd
from pathlib import Path


def format_single_regression_table(df_row_data, task, dv):
    """
    Create a standard regression table for ONE regression.
    
    Format:
    Variable | β | SE | t | p | p_bonf | 95% CI
    """
    # Filter to this specific regression
    reg_data = df_row_data[(df_row_data['Task'] == task) & (df_row_data['DV'] == dv)].copy()
    
    # Create the table
    table = pd.DataFrame({
        'Variable': reg_data['Variable'],
        'β': reg_data['β'].round(3),
        'SE': reg_data['SE'].round(3),
        't': reg_data['t'].round(2),
        'p': reg_data['p'].round(4),
        'p_bonf': reg_data['p_bonferroni'].round(4),
        'p_fdr': reg_data['p_fdr'].round(4),
        '95% CI': reg_data.apply(lambda row: f"[{row['95% CI Lower']:.3f}, {row['95% CI Upper']:.3f}]", axis=1),
        'Bonf CI': reg_data.apply(lambda row: f"[{row['Bonf CI Lower']:.3f}, {row['Bonf CI Upper']:.3f}]", axis=1),
    })
    
    # Add significance stars to p-values (raw, Bonferroni, and FDR)
    def add_stars(p):
        if p < 0.001:
            return f"{p:.4f}***"
        elif p < 0.01:
            return f"{p:.4f}**"
        elif p < 0.05:
            return f"{p:.4f}*"
        else:
            return f"{p:.4f}"
    
    table['p'] = table['p'].apply(add_stars)
    table['p_bonf'] = table['p_bonf'].apply(add_stars)
    table['p_fdr'] = table['p_fdr'].apply(add_stars)
    
    # Add model fit statistics as footer rows
    r2 = reg_data['R²'].iloc[0]
    adj_r2 = reg_data['Adj R²'].iloc[0]
    n = int(reg_data['N'].iloc[0])
    
    # Add blank row
    table = pd.concat([table, pd.DataFrame([{
        'Variable': '',
        'β': '',
        'SE': '',
        't': '',
        'p': '',
        'p_bonf': '',
        'p_fdr': '',
        '95% CI': '',
        'Bonf CI': ''
    }])], ignore_index=True)
    
    # Add model fit
    table = pd.concat([table, pd.DataFrame([
        {'Variable': 'R²', 'β': f'{r2:.3f}', 'SE': '', 't': '', 'p': '', 'p_bonf': '', 'p_fdr': '', '95% CI': '', 'Bonf CI': ''},
        {'Variable': 'Adj R²', 'β': f'{adj_r2:.3f}', 'SE': '', 't': '', 'p': '', 'p_bonf': '', 'p_fdr': '', '95% CI': '', 'Bonf CI': ''},
        {'Variable': 'N', 'β': str(n), 'SE': '', 't': '', 'p': '', 'p_bonf': '', 'p_fdr': '', '95% CI': '', 'Bonf CI': ''}
    ])], ignore_index=True)
    
    return table


def create_all_tables(input_dir: Path, output_dir: Path):
    """Create one table per dependent variable (6 total)."""
    
    # Load coefficients
    df = pd.read_csv(input_dir / "all_coefficients.csv")
    
    # Get unique combinations
    combinations = df[['Task', 'DV']].drop_duplicates()
    
    print("\nCreating regression tables (one per DV)...\n")
    
    for _, row in combinations.iterrows():
        task = row['Task']
        dv = row['DV']
        
        # Create table
        table = format_single_regression_table(df, task, dv)
        
        # Create filename
        task_clean = task.lower().replace(' ', '_')
        dv_clean = dv.lower().replace(' ', '_')
        filename = f"regression_{task_clean}_{dv_clean}.csv"
        output_path = output_dir / filename
        
        # Save
        table.to_csv(output_path, index=False)
        print(f"✓ {task} - {dv}")
        print(f"  Saved to: {filename}\n")
    
    print("="*80)
    print("ALL REGRESSION TABLES CREATED")
    print("="*80)
    print("\nFormat: Standard regression table")
    print("  - Variable | β | SE | t | p | p_bonf | p_fdr | 95% CI | Bonf CI")
    print("  - Significance: * p<.05, ** p<.01, *** p<.001")
    print("  - p_bonf: Bonferroni-corrected p-values (family-wise error rate)")
    print("  - p_fdr: FDR-corrected p-values (Benjamini-Hochberg false discovery rate)")
    print("  - 95% CI: Raw confidence intervals (α = 0.05)")
    print("  - Bonf CI: Bonferroni-adjusted confidence intervals (α = 0.05/n_tests)")
    print("  - Reference: Family=Gemma, Version=1, Fine-Tune Type=Base Model")
    print("  - Standard errors: HC3 heteroscedasticity-consistent (robust)")


if __name__ == "__main__":
    input_dir = Path(__file__).parent.parent.parent / "results" / "statistics"
    output_dir = input_dir
    
    create_all_tables(input_dir, output_dir)
