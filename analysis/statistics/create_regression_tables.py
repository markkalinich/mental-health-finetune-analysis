#!/usr/bin/env python3
"""
Create publication-ready regression tables in standard academic format.

Format:
- Rows = predictors
- Columns = models (one per task-DV combination)
- Cells = β [95% CI] with significance stars
- Bottom rows = R², Adj R², F-stat, N
"""

import pandas as pd
from pathlib import Path


def format_coefficient(beta, ci_low, ci_high, p_value):
    """Format coefficient as: β [CI_low, CI_high]* """
    if p_value < 0.001:
        stars = "***"
    elif p_value < 0.01:
        stars = "**"
    elif p_value < 0.05:
        stars = "*"
    else:
        stars = ""
    return f"{beta:.3f} [{ci_low:.3f}, {ci_high:.3f}]{stars}"


def create_regression_table(input_dir: Path, output_path: Path):
    """Create a single table with all 6 regressions."""
    
    # Load the combined coefficients file
    df = pd.read_csv(input_dir / "all_coefficients.csv")
    
    # Create model labels
    df['Model'] = df['Task'] + ' - ' + df['DV']
    
    # Get unique models and variables
    models = df['Model'].unique()
    variables = df['Variable'].unique()
    
    # Create the table
    table_data = []
    
    for var in variables:
        row = {'Variable': var}
        for model in models:
            model_data = df[(df['Model'] == model) & (df['Variable'] == var)]
            if len(model_data) > 0:
                beta = model_data['β'].values[0]
                ci_low = model_data['95% CI Lower'].values[0]
                ci_high = model_data['95% CI Upper'].values[0]
                p = model_data['p'].values[0]
                row[model] = format_coefficient(beta, ci_low, ci_high, p)
            else:
                row[model] = ''
        table_data.append(row)
    
    # Add model fit statistics
    for model in models:
        model_data = df[df['Model'] == model].iloc[0]
        
    # Add R² row
    r2_row = {'Variable': 'R²'}
    for model in models:
        model_data = df[df['Model'] == model].iloc[0]
        r2_row[model] = f"{model_data['R²']:.3f}"
    table_data.append(r2_row)
    
    # Add Adj R² row
    adj_r2_row = {'Variable': 'Adj R²'}
    for model in models:
        model_data = df[df['Model'] == model].iloc[0]
        adj_r2_row[model] = f"{model_data['Adj R²']:.3f}"
    table_data.append(adj_r2_row)
    
    # Add N row
    n_row = {'Variable': 'N'}
    for model in models:
        model_data = df[df['Model'] == model].iloc[0]
        n_row[model] = f"{int(model_data['N'])}"
    table_data.append(n_row)
    
    # Create dataframe
    result_df = pd.DataFrame(table_data)
    
    # Reorder columns
    column_order = ['Variable'] + list(models)
    result_df = result_df[column_order]
    
    # Save
    result_df.to_csv(output_path, index=False)
    print(f"\nRegression table saved to: {output_path}")
    
    # Also print to console
    print("\n" + "="*120)
    print("REGRESSION RESULTS TABLE")
    print("="*120)
    print(result_df.to_string(index=False))
    print("\nNote: * p < .05, ** p < .01, *** p < .001")
    print("Format: β [95% CI Lower, 95% CI Upper]")
    print("Reference categories: Family=Gemma, Version=1, Fine-Tune Type=Base Model")


def create_regression_table_bonferroni(input_dir: Path, output_path: Path):
    """Create Bonferroni-corrected table in the same β [CI]* format as the raw table."""

    df = pd.read_csv(input_dir / "all_coefficients.csv")
    df['Model'] = df['Task'] + ' - ' + df['DV']

    models = df['Model'].unique()
    variables = df['Variable'].unique()

    table_data = []
    for var in variables:
        row = {'Variable': var}
        for model in models:
            model_data = df[(df['Model'] == model) & (df['Variable'] == var)]
            if len(model_data) > 0:
                beta = model_data['β'].values[0]
                ci_low = model_data['Bonf CI Lower'].values[0]
                ci_high = model_data['Bonf CI Upper'].values[0]
                p = model_data['p_bonferroni'].values[0]
                row[model] = format_coefficient(beta, ci_low, ci_high, p)
            else:
                row[model] = ''
        table_data.append(row)

    for model in models:
        model_data = df[df['Model'] == model].iloc[0]

    r2_row = {'Variable': 'R²'}
    for model in models:
        model_data = df[df['Model'] == model].iloc[0]
        r2_row[model] = f"{model_data['R²']:.3f}"
    table_data.append(r2_row)

    adj_r2_row = {'Variable': 'Adj R²'}
    for model in models:
        model_data = df[df['Model'] == model].iloc[0]
        adj_r2_row[model] = f"{model_data['Adj R²']:.3f}"
    table_data.append(adj_r2_row)

    n_row = {'Variable': 'N'}
    for model in models:
        model_data = df[df['Model'] == model].iloc[0]
        n_row[model] = f"{int(model_data['N'])}"
    table_data.append(n_row)

    result_df = pd.DataFrame(table_data)
    column_order = ['Variable'] + list(models)
    result_df = result_df[column_order]

    result_df.to_csv(output_path, index=False)
    print(f"\nBonferroni regression table saved to: {output_path}")
    print("Note: * p_adj < .05, ** p_adj < .01, *** p_adj < .001 (Bonferroni-corrected)")
    print("CIs are Bonferroni-adjusted (α = 0.05 / n_tests)")


def create_task_specific_tables(input_dir: Path, output_dir: Path):
    """Create separate tables for each task (F1 and Accuracy side-by-side)."""
    
    df = pd.read_csv(input_dir / "all_coefficients.csv")
    
    tasks = df['Task'].unique()
    
    for task in tasks:
        task_df = df[df['Task'] == task]
        
        # Get unique variables
        variables = task_df['Variable'].unique()
        dvs = task_df['DV'].unique()
        
        # Create table
        table_data = []
        
        for var in variables:
            row = {'Variable': var}
            for dv in dvs:
                model_data = task_df[(task_df['DV'] == dv) & (task_df['Variable'] == var)]
                if len(model_data) > 0:
                    beta = model_data['β'].values[0]
                    ci_low = model_data['95% CI Lower'].values[0]
                    ci_high = model_data['95% CI Upper'].values[0]
                    p = model_data['p'].values[0]
                    row[dv] = format_coefficient(beta, ci_low, ci_high, p)
                else:
                    row[dv] = ''
            table_data.append(row)
        
        # Add model fit statistics
        for dv in dvs:
            model_data = task_df[task_df['DV'] == dv].iloc[0]
        
        # Add R² row
        r2_row = {'Variable': 'R²'}
        for dv in dvs:
            model_data = task_df[task_df['DV'] == dv].iloc[0]
            r2_row[dv] = f"{model_data['R²']:.3f}"
        table_data.append(r2_row)
        
        # Add Adj R² row
        adj_r2_row = {'Variable': 'Adj R²'}
        for dv in dvs:
            model_data = task_df[task_df['DV'] == dv].iloc[0]
            adj_r2_row[dv] = f"{model_data['Adj R²']:.3f}"
        table_data.append(adj_r2_row)
        
        # Add N row
        n_row = {'Variable': 'N'}
        for dv in dvs:
            model_data = task_df[task_df['DV'] == dv].iloc[0]
            n_row[dv] = f"{int(model_data['N'])}"
        table_data.append(n_row)
        
        # Create dataframe
        result_df = pd.DataFrame(table_data)
        
        # Save
        filename = f"regression_table_{task.lower().replace(' ', '_')}.csv"
        output_path = output_dir / filename
        result_df.to_csv(output_path, index=False)
        print(f"\n{task} table saved to: {output_path}")


if __name__ == "__main__":
    # Paths
    input_dir = Path(__file__).parent.parent.parent / "results" / "statistics"
    output_dir = input_dir
    
    print("Creating regression tables...")
    
    # Create combined table (raw p-values)
    create_regression_table(input_dir, output_dir / "regression_table_combined.csv")
    
    # Create combined table (Bonferroni-corrected)
    create_regression_table_bonferroni(input_dir, output_dir / "regression_table_combined_bonferroni.csv")
    
    # Create task-specific tables
    create_task_specific_tables(input_dir, output_dir)
    
    print("\n✓ All tables created successfully!")
