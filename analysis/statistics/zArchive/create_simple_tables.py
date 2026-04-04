#!/usr/bin/env python3
"""
Create simple, clean regression tables with Variable | β | 95% CI columns.
No fancy packages - just pandas and clean formatting.
"""

import pandas as pd
from pathlib import Path


def create_simple_latex_table(csv_path: Path, output_path: Path, title: str):
    """Create simple LaTeX table: Variable | β | 95% CI"""
    
    df = pd.read_csv(csv_path)
    
    latex = r"""\begin{table}[htbp]
\centering
\caption{""" + title + r"""}
\begin{tabular}{lcc}
\toprule
Variable & $\beta$ & 95\% CI \\
\midrule
"""
    
    # Add coefficient rows
    for idx, row in df.iterrows():
        var = str(row['Variable'])
        
        # Skip if we're at the summary stats section or nan
        if var in ['', 'R²', 'Adj R²', 'N', 'nan'] or pd.isna(row['β']):
            break
            
        beta = f"{row['β']:.3f}"
        ci = row['95% CI']
        p = row['p']
        
        # Add significance stars
        if isinstance(p, str):
            if '***' in p:
                beta += r'$^{***}$'
            elif '**' in p:
                beta += r'$^{**}$'
            elif '*' in p and '***' not in p and '**' not in p:
                beta += r'$^{*}$'
        
        latex += f"{var} & {beta} & {ci} \\\\\n"
    
    # Add summary statistics
    latex += r"""\midrule
"""
    
    for idx, row in df.iterrows():
        var = str(row['Variable'])
        if var in ['R²', 'Adj R²', 'N']:
            val = row['β']
            if var == 'N':
                val = int(float(val))
            latex += f"{var} & {val} & \\\\\n"
    
    latex += r"""\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item Note: $^{*}$p$<$0.05; $^{**}$p$<$0.01; $^{***}$p$<$0.001
\item Reference categories: Family=Gemma, Version=1, Fine-Tune Type=Base Model
\item Standard errors: HC3 heteroscedasticity-consistent (robust)
\end{tablenotes}
\end{table}
"""
    
    with open(output_path, 'w') as f:
        f.write(latex)


def create_simple_html_table(csv_path: Path, output_path: Path, title: str):
    """Create simple HTML table: Variable | β | 95% CI"""
    
    df = pd.read_csv(csv_path)
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<style>
table {{
    border-collapse: collapse;
    width: 80%;
    margin: 20px auto;
    font-family: Arial, sans-serif;
}}
caption {{
    font-weight: bold;
    font-size: 1.2em;
    margin-bottom: 10px;
}}
th {{
    background-color: #f0f0f0;
    border-top: 2px solid black;
    border-bottom: 2px solid black;
    padding: 10px;
    text-align: center;
}}
td {{
    padding: 8px;
    border-bottom: 1px solid #ddd;
}}
td:first-child {{
    text-align: left;
}}
td:nth-child(2), td:nth-child(3) {{
    text-align: center;
}}
.summary-row {{
    border-top: 2px solid black;
    font-weight: bold;
}}
.notes {{
    width: 80%;
    margin: 10px auto;
    font-size: 0.9em;
    color: #666;
}}
</style>
</head>
<body>

<table>
<caption>{title}</caption>
<thead>
<tr>
<th>Variable</th>
<th>β</th>
<th>95% CI</th>
</tr>
</thead>
<tbody>
"""
    
    # Add coefficient rows
    for idx, row in df.iterrows():
        var = str(row['Variable'])
        
        # Skip if we're at the summary stats section or nan
        if var in ['', 'R²', 'Adj R²', 'N', 'nan'] or pd.isna(row['β']):
            break
            
        beta = f"{row['β']:.3f}"
        ci = row['95% CI']
        p = row['p']
        
        # Add significance stars
        if isinstance(p, str):
            if '***' in p:
                beta += '<sup>***</sup>'
            elif '**' in p:
                beta += '<sup>**</sup>'
            elif '*' in p and '***' not in p and '**' not in p:
                beta += '<sup>*</sup>'
        
        html += f"<tr><td>{var}</td><td>{beta}</td><td>{ci}</td></tr>\n"
    
    # Add summary statistics
    for idx, row in df.iterrows():
        var = str(row['Variable'])
        if var in ['R²', 'Adj R²', 'N']:
            val = row['β']
            if var == 'N':
                val = int(float(val))
            html += f'<tr class="summary-row"><td>{var}</td><td>{val}</td><td></td></tr>\n'
    
    html += """</tbody>
</table>

<div class="notes">
<p><strong>Note:</strong> <sup>*</sup>p&lt;0.05; <sup>**</sup>p&lt;0.01; <sup>***</sup>p&lt;0.001</p>
<p>Reference categories: Family=Gemma, Version=1, Fine-Tune Type=Base Model</p>
<p>Standard errors: HC3 heteroscedasticity-consistent (robust)</p>
</div>

</body>
</html>
"""
    
    with open(output_path, 'w') as f:
        f.write(html)


if __name__ == "__main__":
    stats_dir = Path(__file__).parent.parent.parent / "results" / "statistics"
    
    print("="*80)
    print("CREATING SIMPLE CLEAN TABLES (Variable | β | 95% CI)")
    print("="*80)
    
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
        latex_path = stats_dir / f"clean_{base_name}.tex"
        create_simple_latex_table(csv_path, latex_path, title)
        
        # Create HTML
        html_path = stats_dir / f"clean_{base_name}.html"
        create_simple_html_table(csv_path, html_path, title)
        
        print(f"✓ {title}")
        print(f"  Files: clean_{base_name}.tex / .html\n")
    
    print("="*80)
    print("✓ ALL SIMPLE TABLES CREATED")
    print("="*80)
    print("\nClean three-column format: Variable | β | 95% CI")
    print("Location: results/statistics/clean_*.tex and clean_*.html")
