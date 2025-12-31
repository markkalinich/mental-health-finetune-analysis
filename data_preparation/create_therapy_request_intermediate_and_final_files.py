#!/usr/bin/env python3
"""
Create psychiatrist-scored datasets from Gemini-generated therapy request statements.

Matches psychiatrist-approved sentences back to original 1200 Gemini outputs using exact
and fuzzy matching, then creates balanced finalized dataset from dual-approved sentences.
"""

import pandas as pd
from pathlib import Path
from fuzzywuzzy import fuzz, process

def create_therapy_request_scoring():
    """
    Match psychiatrist-approved sentences back to original 1200 Gemini outputs.
    
    Uses exact matching first, then fuzzy matching (≥75% similarity within same category).
    Tracks match type and adds both psychiatrist 01 and 02 scoring.
    
    Returns:
        Path to output file
    """
    base_dir = Path('.')
    original_file = base_dir / "data/inputs/raw_model_results/therapy_request_100_per_category_reformatted.csv"
    reviewed_file_01 = base_dir / "data/inputs/manual_review/therapy_request_psychiatrist_01_approved.csv"
    reviewed_file_02 = base_dir / "data/inputs/manual_review/therapy_request_psychiatrist_02_approved.csv"
    output_file = base_dir / "data/inputs/intermediate_files/therapy_request_psychiatrist_01_and_02_scores.csv"
    
    # Load data
    original_df = pd.read_csv(original_file)
    reviewed_df_01 = pd.read_csv(reviewed_file_01)
    reviewed_df_02 = pd.read_csv(reviewed_file_02)
    approved_02_set = set(reviewed_df_02['statement'].str.strip())
    
    # Build map: approved sentence -> (matched original, match type)
    approved_to_original = {}
    
    for _, row in reviewed_df_01.iterrows():
        approved_statement = str(row['statement']).strip()
        counseling_request = row['Counseling Request']
        
        # Try exact match across all originals
        exact_match = original_df[original_df['statement'].str.strip() == approved_statement]
        if not exact_match.empty:
            approved_to_original[approved_statement] = (approved_statement, 'EXACT')
            continue
        
        # Try fuzzy match within same category
        category_originals = original_df[original_df['Counseling Request'] == counseling_request]['statement'].str.strip().tolist()
        if category_originals:
            best_match = process.extractOne(approved_statement, category_originals, scorer=fuzz.ratio)
            if best_match and best_match[1] >= 75:
                approved_to_original[approved_statement] = (best_match[0], 'FUZZY')
                continue
        
        # No match - new sentence
        approved_to_original[approved_statement] = (None, 'NEW')
    
    # Process each original sentence
    final_data = []
    used_originals = set()
    
    for _, row in original_df.iterrows():
        original_statement = str(row['statement']).strip()
        safety_type = row['Safety type']
        counseling_request = row['Counseling Request']
        
        # Find if any approved sentence claims this original
        final_statement = ''
        psychiatrist_01_score = 'REMOVED'
        
        if original_statement not in used_originals:
            for approved_stmt, (orig_match, match_type) in approved_to_original.items():
                if orig_match == original_statement:
                    final_statement = approved_stmt
                    psychiatrist_01_score = 'KEPT_exact_match' if match_type == 'EXACT' else 'KEPT_with_changes'
                    used_originals.add(original_statement)
                    break
        
        row_data = {
            'Safety type': safety_type,
            'Counseling Request': counseling_request,
            'original_statement': original_statement,
            'final_statement': final_statement,
            'Psychiatrist_01': psychiatrist_01_score
        }
        
        if psychiatrist_01_score == 'REMOVED':
            row_data['Psychiatrist_02'] = 'NA'
        else:
            row_data['Psychiatrist_02'] = 'KEPT' if final_statement in approved_02_set else 'REMOVED'
        
        final_data.append(row_data)
    
    # Add new sentences
    for approved_stmt, (orig_match, match_type) in approved_to_original.items():
        if match_type == 'NEW':
            counseling_request = reviewed_df_01[reviewed_df_01['statement'].str.strip() == approved_stmt]['Counseling Request'].values[0]
            row_data = {
                'Safety type': 'no_SI',
                'Counseling Request': counseling_request,
                'original_statement': '',
                'final_statement': approved_stmt,
                'Psychiatrist_01': 'NEW_SENTENCE',
                'Psychiatrist_02': 'KEPT' if approved_stmt in approved_02_set else 'REMOVED'
            }
            final_data.append(row_data)
    
    # Create output dataframe and save
    output_df = pd.DataFrame(final_data)
    output_df.to_csv(output_file, index=False)
    
    return str(output_file)

def create_finalized_balanced_dataset(scores_file_path):
    """
    Create balanced final dataset from dual-approved sentences.
    
    Samples equal number from each category (matching the category with fewest approvals).
    
    Args:
        scores_file_path: Path to combined psychiatrist scores file
    
    Returns:
        Path to finalized dataset
    """
    df = pd.read_csv(scores_file_path)
    
    # Filter to sentences approved by both psychiatrists
    approved_df = df[
        (df['Psychiatrist_01'].isin(['KEPT_exact_match', 'KEPT_with_changes'])) & 
        (df['Psychiatrist_02'] == 'KEPT')
    ]
    
    # Find minimum count across categories
    category_counts = approved_df['Counseling Request'].value_counts().sort_values()
    min_count = category_counts.iloc[0]
    
    # Sample min_count - 1 sentences from each category (to match original methodology)
    # This ensures balanced dataset while accounting for edge cases
    sample_count = min_count - 1
    print(f"Minimum approved per category: {min_count}, sampling {sample_count} per category")
    
    finalized_data = []
    selected_indices = []  # Track which rows were selected for reproducibility
    
    for counseling_request in approved_df['Counseling Request'].unique():
        category_approved = approved_df[approved_df['Counseling Request'] == counseling_request]
        sampled = category_approved.sample(n=sample_count, random_state=42)
        
        # Store indices for reproducibility manifest
        selected_indices.extend(sampled.index.tolist())
        
        for _, row in sampled.iterrows():
            finalized_data.append({
                'Safety type': row['Safety type'],
                'therapy_request': row['Counseling Request'],
                'statement': row['final_statement']
            })
    
    # Save finalized dataset
    finalized_df = pd.DataFrame(finalized_data)
    output_dir = Path("data/inputs/finalized_input_data")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "therapy_request_finalized_sentences.csv"
    finalized_df.to_csv(output_file, index=False)
    
    # Save selection manifest for exact reproducibility
    manifest_dir = Path("data/inputs/manifests")
    manifest_dir.mkdir(exist_ok=True)
    manifest_path = manifest_dir / "therapy_request_finalized_selection_manifest.csv"
    manifest_df = df.loc[selected_indices, ['original_statement', 'final_statement', 'Counseling Request']].copy()
    manifest_df['selected_for_finalized'] = True
    manifest_df.to_csv(manifest_path, index=True)
    print(f"Created selection manifest: {manifest_path}")
    print(f"  Documents which {len(selected_indices)} statements were selected from intermediate file")
    
    return str(output_file)

if __name__ == "__main__":
    # Create scoring file with both psychiatrists
    output_path = create_therapy_request_scoring()
    print(f"Created: {output_path}")
    
    # Create finalized balanced dataset
    finalized_path = create_finalized_balanced_dataset(output_path)
    print(f"Created: {finalized_path}")
