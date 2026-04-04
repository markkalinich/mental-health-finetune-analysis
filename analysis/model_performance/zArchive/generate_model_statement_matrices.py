#!/usr/bin/env python3
"""
Generate matrices showing which models got which statements correct
Rows = models, Columns = statements, Values = 1 (correct) or 0 (incorrect)

Uses BINARY classification for SI (SI vs non-SI) to match comprehensive_metrics.csv
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from config.constants import SI_POSITIVE_CATEGORIES


def to_binary_si(label):
    """Convert SI label to binary: SI or non-SI"""
    if pd.isna(label):
        return None
    return 'SI' if label in SI_POSITIVE_CATEGORIES else 'non-SI'


def to_binary_therapy_engagement(label):
    """Convert therapy engagement label to binary: therapy or non-therapy"""
    if pd.isna(label):
        return None
    label_str = str(label).lower()
    if 'engagement' in label_str or 'therapy' in label_str or 'simulated' in label_str:
        return 'therapy'
    return 'non-therapy'


def to_binary_therapy_request(label):
    """Convert therapy request label to binary: explicit therapy request or not"""
    if pd.isna(label):
        return None
    label_str = str(label).lower()
    # Check if it's an explicit therapy request
    if 'explicit' in label_str and 'therapy' in label_str:
        return 'explicit_therapy_request'
    # Map model outputs
    if label_str == 'explicit_therapy_request':
        return 'explicit_therapy_request'
    # Everything else is non-therapy-request
    return 'non_therapy_request'


def normalize_therapy_request(label):
    """
    Convert detailed therapy request ground truth labels to simplified prediction format
    
    Ground truth uses format like:
    - "Neutral Explicit Requests for Therapy"
    - "Affect-Containing Explicit Requests for Therapy - Clearly Happy"
    - "Neutral Declarative Statements"
    - "Affect-Containing Non-Therapeutic Questions - Clearly Sad"
    
    Predictions use format like:
    - "explicit_therapy_request"
    - "declarative"
    - "non_therapeutic_question"
    """
    if pd.isna(label):
        return None
    
    label_str = str(label)
    
    # Map to simplified categories
    if 'Explicit Requests for Therapy' in label_str:
        return 'explicit_therapy_request'
    elif 'Declarative' in label_str:
        return 'declarative'
    elif 'Non-Therapeutic' in label_str:
        return 'non_therapeutic_question'
    
    # Return as-is if no match (shouldn't happen with correct data)
    return label_str


def load_all_model_outputs(experiment_dir):
    """
    Load all model output files from an experiment directory
    
    Returns:
        Dictionary mapping model_name -> DataFrame
    """
    model_outputs = {}
    output_dir = Path(experiment_dir) / 'model_outputs'
    
    for csv_file in sorted(output_dir.glob('*.csv')):
        filename = csv_file.stem
        model_name = '_'.join(filename.split('_')[:2])
        
        if model_name in model_outputs:
            print(f"WARNING: Duplicate model name {model_name} - skipping {csv_file.name}")
        else:
            df = pd.read_csv(csv_file)
            model_outputs[model_name] = df
    
    return model_outputs


def create_correctness_matrix(model_outputs, ground_truth_column, prediction_column, use_binary=False, binary_converter=None):
    """
    Create a matrix where rows=models, columns=statements, values=1 (correct) or 0 (incorrect)
    
    Args:
        model_outputs: Dictionary mapping model_name -> DataFrame
        ground_truth_column: Column name for ground truth
        prediction_column: Column name for model predictions
        use_binary: If True, convert labels to binary before comparing
        binary_converter: Function to convert labels to binary (required if use_binary=True)
    
    Returns:
        DataFrame with rows=models, columns=statement indices, values=correctness
    """
    # Get all unique statement texts from first model (in order)
    first_model_df = list(model_outputs.values())[0]
    statement_texts = first_model_df['text'].tolist()
    
    # Initialize results dictionary
    results = {}
    
    for model_name, df in sorted(model_outputs.items()):
        correctness = []
        
        # Create a lookup dictionary for this model's data
        model_text_lookup = {row['text']: row for _, row in df.iterrows()}
        
        for stmt_text in statement_texts:
            if stmt_text not in model_text_lookup:
                # Statement not found in this model's output
                correctness.append(np.nan)
            else:
                stmt_row = model_text_lookup[stmt_text]
                ground_truth = stmt_row[ground_truth_column]
                prediction = stmt_row[prediction_column]
                
                # Convert labels if converter provided
                if binary_converter:
                    ground_truth = binary_converter(ground_truth)
                    # For binary classification, also convert prediction
                    if use_binary:
                        prediction = binary_converter(prediction)
                
                # 1 if correct, 0 if incorrect
                correctness.append(1 if prediction == ground_truth else 0)
        
        results[model_name] = correctness
    
    # Create DataFrame with statement indices as columns (0, 1, 2, ...)
    matrix_df = pd.DataFrame(results, index=range(len(statement_texts))).T
    
    return matrix_df


def create_statement_info(model_outputs, ground_truth_column):
    """
    Create a DataFrame with information about each statement
    
    Returns:
        DataFrame with columns: statement_index, text, ground_truth
    """
    first_model_df = list(model_outputs.values())[0]
    
    info = []
    for idx, row in first_model_df.iterrows():
        info.append({
            'statement_index': len(info),  # 0-indexed position
            'text': row['text'][:200] if len(row['text']) > 200 else row['text'],
            'ground_truth': row[ground_truth_column]
        })
    
    return pd.DataFrame(info)


def main():
    """Generate correctness matrices for all three tasks"""
    
    # Define experiments
    experiments = [
        {
            'name': 'suicidal_ideation',
            'dir': 'results/individual_prediction_performance/suicidal_ideation/20251027_182837_SI',
            'ground_truth_col': 'prior_safety_type',
            'prediction_col': 'safety_type',
            'output_matrix': 'si_model_statement_correctness_matrix.csv',
            'output_info': 'si_statement_info.csv',
            'use_binary': True,
            'binary_converter': to_binary_si
        },
        {
            'name': 'therapy_request',
            'dir': 'results/individual_prediction_performance/therapy_request/20251027_182856_tx_request',
            'ground_truth_col': 'prior_therapy_request',
            'prediction_col': 'therapy_request',
            'output_matrix': 'therapy_request_model_statement_correctness_matrix.csv',
            'output_info': 'therapy_request_statement_info.csv',
            'use_binary': True,
            'binary_converter': to_binary_therapy_request  # Binary: explicit therapy request vs not
        },
        {
            'name': 'therapy_engagement',
            'dir': 'results/individual_prediction_performance/therapy_engagement/20251030_210744_tx_engagement',
            'ground_truth_col': 'prior_therapy_engagement',
            'prediction_col': 'therapy_engagement',
            'output_matrix': 'therapy_engagement_model_conversation_correctness_matrix.csv',
            'output_info': 'therapy_engagement_conversation_info.csv',
            'use_binary': True,
            'binary_converter': to_binary_therapy_engagement
        }
    ]
    
    # Create output directory
    output_dir = Path('results/review_statistics')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process each experiment
    for exp in experiments:
        print(f"\n{'='*80}")
        print(f"Processing: {exp['name']}")
        print('='*80)
        
        # Load all model outputs
        model_outputs = load_all_model_outputs(exp['dir'])
        print(f"Loaded {len(model_outputs)} models")
        
        # Create correctness matrix
        matrix_df = create_correctness_matrix(
            model_outputs,
            exp['ground_truth_col'],
            exp['prediction_col'],
            use_binary=exp.get('use_binary', False),
            binary_converter=exp.get('binary_converter', None)
        )
        
        print(f"Matrix shape: {matrix_df.shape} (models x statements)")
        
        # Save matrix
        matrix_file = output_dir / exp['output_matrix']
        matrix_df.to_csv(matrix_file)
        print(f"Saved correctness matrix to: {matrix_file}")
        
        # Create and save statement info
        info_df = create_statement_info(model_outputs, exp['ground_truth_col'])
        info_file = output_dir / exp['output_info']
        info_df.to_csv(info_file, index=False)
        print(f"Saved statement info to: {info_file}")
        
        # Print summary statistics
        total_predictions = matrix_df.shape[0] * matrix_df.shape[1]
        correct_predictions = matrix_df.sum().sum()
        accuracy = correct_predictions / total_predictions
        
        print(f"\nSummary:")
        print(f"  Total models: {matrix_df.shape[0]}")
        print(f"  Total statements: {matrix_df.shape[1]}")
        print(f"  Total predictions: {total_predictions}")
        print(f"  Correct predictions: {correct_predictions}")
        print(f"  Overall accuracy: {accuracy:.1%}")
        
        # Per-model accuracy
        print(f"\nPer-model accuracy:")
        model_accuracy = matrix_df.mean(axis=1).sort_values(ascending=False)
        for model, acc in model_accuracy.items():
            print(f"  {model:15} {acc:.1%}")
        
        # Statements missed by all models
        statements_missed_by_all = (matrix_df.sum(axis=0) == 0).sum()
        print(f"\nStatements missed by ALL models: {statements_missed_by_all}")
        
        # Statements correct by all models
        statements_correct_by_all = (matrix_df.sum(axis=0) == matrix_df.shape[0]).sum()
        print(f"Statements correct by ALL models: {statements_correct_by_all}")


if __name__ == '__main__':
    main()
