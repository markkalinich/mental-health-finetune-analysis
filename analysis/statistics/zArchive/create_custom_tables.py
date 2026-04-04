#!/usr/bin/env python3
"""
Create custom formatted regression tables with explicit CI column.

Format:
Variable | β | 95% CI
"""

import pandas as pd
from pathlib import Path


def create_latex_table(csv_path: Path, output_path: Path, title: str):
    """Create LaTeX table from CSV with Variable | β | 95% CI format."""
    
    df = pd.read_csv(csv_path)
    
    # Start LaTeX table
    latex = r"""\begin{table}[!htbp] \centering
  \caption{""" + title + r"""}
\begin{tabular}{@{\extracolsep{5pt}}lcc}
\\[-1.8ex]\hline
\hline \\[-1.8ex]
& \multicolumn{1}{c}{$\beta$} & \multicolumn{1}{c}{95\% CI} \\
\hline \\[-1.8ex]
"""
    
    # Add rows
    for idx, row in df.iterrows():
        var = row['Variable']
        beta = row['β']
        ci = row['95% CI']
        p = row['p']
        
        # Skip empty rows
        if pd.isna(beta) or beta == '':
            continue
            
        # Determine stars
        if isinstance(p, str):
            # Already has stars
            stars = ''
            if '***' in p:
                stars = '$^{***}$'
            elif '**' in p:
                stars = '$^{**}$'
            elif '*' in p:
                stars = '$^{*}$'
        else:
            # Numeric p-value
            if p < 0.001:
                stars = '$^{***}$'
            elif p < 0.01:
                stars = '$^{**}$'
            elif p < 0.05:
                stars = '$^{*}$'
            else:
                stars = ''
        
        # Format row - check if this is a summary stat row
        if var in ['R²', 'Adj R²', 'N', '']:
            if var == '':
                latex += r"\hline \\[-1.8ex]" + "\n"
            else:
                latex += f" {var} & {beta} & \\\\\n"
        else:
            latex += f" {var} & {beta}{stars} & {ci} \\\\\n"
    
    # Close table
    latex += r"""\hline
\hline \\[-1.8ex]
\textit{Note:} & \multicolumn{2}{r}{$^{*}$p$<$0.05; $^{**}$p$<$0.01; $^{***}$p$<$0.001} \\
\textit{} & \multicolumn{2}{r}{Reference: Family=Gemma, Version=1, Fine-Tune=Base Model} \\
\textit{} & \multicolumn{2}{r}{Standard Errors: HC3 Robust} \\
\end{tabular}
\end{table}"""
    
    # Save
    with open(output_path, 'w') as f:
        f.write(latex)


def create_html_table(csv_path: Path, output_path: Path, title: str):
    """Create HTML table from CSV with Variable | β | 95% CI format."""
    
    df = pd.read_csv(csv_path)
    
    # Start HTML table
    html = f"""<h3>{title}</h3>
<table style="border-collapse: collapse; width: 100%; margin: 20px 0;">
<thead>
<tr style="border-bottom: 2px solid black;">
<th style="text-align: left; padding: 8px;">Variable</th>
<th style="text-align: center; padding: 8px;">β</th>
<th style="text-align: center; padding: 8px;">95% CI</th>
</tr>
</thead>
<tbody>
"""
    
    # Add rows
    for idx, row in df.iterrows():
        var = row['Variable']
        beta = row['β']
        ci = row['95% CI']
        p = row['p']
        
        # Skip empty rows
        if pd.isna(beta) or beta == '':
            continue
            
        # Determine stars
        if isinstance(p, str):
            stars = ''
            if '***' in p:
                stars = '<sup>***</sup>'
            elif '**' in p:
                stars = '<sup>**</sup>'
            elif '*' in p:
                stars = '<sup>*</sup>'
        else:
            if p < 0.001:
                stars = '<sup>***</sup>'
            elif p < 0.01:
                stars = '<sup>**</sup>'
            elif p < 0.05:
                stars = '<sup>*</sup>'
            else:
                stars = ''
        
        # Format row
        if var in ['R²', 'Adj R²', 'N', '']:
            if var == '':
                html += '<tr style="border-top: 1px solid black;"><td colspan="3"></td></tr>\n'
            else:
                html += f'<tr style="border-top: 1px solid black;"><td style="padding: 8px;"><strong>{var}</strong></td><td style="text-align: center; padding: 8px;">{beta}</td><td></td></tr>\n'
        else:
            html += f'<tr><td style="padding: 8px;">{var}</td><td style="text-align: center; padding: 8px;">{beta}{stars}</td><td style="text-align: center; padding: 8px;">{ci}</td></tr>\n'
    
    # Close table
    html += """</tbody>
</table>
<p style="font-size: 0.9em; font-style: italic;">
Note: <sup>*</sup>p&lt;0.05; <sup>**</sup>p&lt;0.01; <sup>***</sup>p&lt;0.001<br>
Reference: Family=Gemma, Version=1, Fine-Tune=Base Model<br>
Standard Errors: HC3 Robust
</p>
"""
    
    # Save
    with open(output_path, 'w') as f:
        f.write(html)


if __name__ == "__main__":
    stats_dir = Path(__file__).parent.parent.parent / "results" / "statistics"
    
    print("="*80)
    print("CREATING CUSTOM FORMATTED TABLES (Variable | β | 95% CI)")
    print("="*80)
    
    # List of regression files
    regressions = [
        ("regression_suicidal_ideation_f1_score.csv", "Suicidal Ideation - F1 Score"),
        ("regression_suicidal_ideation_accuracy.csv", "Suicidal Ideation - Accuracy"),
        ("regression_therapy_request_f1_score.csv", "Therapy Request - F1 Score"),
        ("regression_therapy_request_accuracy.csv", "Therapy Request - Accuracy"),
        ("regression_therapy_engagement_f1_score.csv", "Therapy Engagement - F1 Score"),
        ("regression_therapy_engagement_accuracy.csv", "Therapy Engagement - Accuracy"),
    ]
    
    for csv_file, title in regressions:
        csv_path = stats_dir / csv_file
        base_name = csv_file.replace('.csv', '')
        
        # Create LaTeX
        latex_path = stats_dir / f"table_{base_name}.tex"
        create_latex_table(csv_path, latex_path, title)
        print(f"✓ {title}")
        print(f"  LaTeX: {latex_path.name}")
        
        # Create HTML
        html_path = stats_dir / f"table_{base_name}.html"
        create_html_table(csv_path, html_path, title)
        print(f"  HTML:  {html_path.name}\n")
    
    print("="*80)
    print("✓ ALL CUSTOM TABLES CREATED")
    print("="*80)
    print("\nFormat: Variable | β | 95% CI")
    print("Location: results/statistics/table_*.tex and table_*.html")
