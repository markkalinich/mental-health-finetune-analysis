#!/usr/bin/env python3
"""
Create Therapy Engagement Intermediate and Final Files

Creates both intermediate (P1+P2 scoring) and final (balanced 420 conversations) files
for therapy engagement conversation data.

Pipeline:
1. Match P1 and P2 approved conversations to original data (by Example_ID)
2. Create intermediate file with P1+P2 scoring for all 450 conversations
3. Filter to fully approved conversations (434 conversations)
4. Sample 140 per main group (420 total), prioritizing old P1-only experiment
5. Create finalized files (turn-by-turn and formatted versions)

Input files:
- Raw model results: data/inputs/raw_model_results/therapy_engagement_conversations_downsampled_150.csv
- P1 manual review: data/inputs/manual_review/therapy_engagement_conversations_psychiatrist_01_approved.csv
- P2 manual review: data/inputs/manual_review/therapy_engagement_conversations_psychiatrist_02_approved.csv
- Old P1-only experiment: data/inputs/finalized_input_data/therapy_engagement_P1_approval_only_finalized_sentences.csv

Output files:
- Intermediate: data/inputs/intermediate_files/therapy_engagement_psychiatrist_01_and_02_scores.csv (turn-by-turn format)
- Final: data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv (formatted for experiments)
"""

import pandas as pd
from pathlib import Path
import sys

def simplify_subcategory(subcategory: str) -> str:
    """Simplify subcategory to base group name."""
    if subcategory.startswith('NonTherapeutic_'):
        return subcategory.replace('NonTherapeutic_', '')
    elif subcategory.startswith('Ambiguous_'):
        return subcategory.replace('Ambiguous_', '').replace('Boundary_', '')
    elif subcategory.startswith('SimulatedTherapy_'):
        parts = subcategory.replace('SimulatedTherapy_', '').split('_')
        return parts[0] if parts else subcategory
    return subcategory

def get_main_group(subcategory: str) -> str:
    """Get main category group."""
    if subcategory.startswith('NonTherapeutic_'):
        return 'Non-Therapeutic'
    elif subcategory.startswith('Ambiguous_'):
        return 'Ambiguous'
    elif subcategory.startswith('SimulatedTherapy_'):
        return 'Simulated Therapy'
    return 'Unknown'

def map_subcategory_to_counseling_request(subcategory: str) -> str:
    """Map subcategory to counseling request category - MUST match old P1-only file."""
    if subcategory.startswith('NonTherapeutic_'):
        return 'clear_non_engagement'
    elif subcategory.startswith('Ambiguous_'):
        return 'ambiguous_engagement'
    elif subcategory.startswith('SimulatedTherapy_'):
        return 'clear_engagement'  # OLD FORMAT USED THIS, NOT 'simulated_therapy'
    return 'unknown'

def format_conversation(group_df: pd.DataFrame) -> str:
    """Format conversation turns into single statement."""
    turns = []
    for _, row in group_df.sort_values('Turn').iterrows():
        speaker = row['Speaker'].upper()
        utterance = row['final_Utterance']
        turns.append(f"{speaker}: {utterance}")
    return '\n'.join(turns)

def create_intermediate_file():
    """
    Create intermediate file with P1 and P2 psychiatrist scoring.
    
    Returns:
        str: Path to intermediate output file
    """
    print("="*80)
    print("STEP 1: CREATE INTERMEDIATE FILE WITH P1+P2 SCORING")
    print("="*80)
    
    # File paths
    base_dir = Path('.')
    original_file = base_dir / "data/inputs/raw_model_results/therapy_engagement_conversations_downsampled_150.csv"
    reviewed_file_01 = base_dir / "data/inputs/manual_review/therapy_engagement_conversations_psychiatrist_01_approved.csv"
    reviewed_file_02 = base_dir / "data/inputs/manual_review/therapy_engagement_conversations_psychiatrist_02_approved.csv"
    output_file = base_dir / "data/inputs/intermediate_files/therapy_engagement_psychiatrist_01_and_02_scores.csv"
    
    print(f"\nLoading original input file: {original_file}")
    print(f"Loading psychiatrist 01 review file: {reviewed_file_01}")
    print(f"Loading psychiatrist 02 review file: {reviewed_file_02}")
    
    # Load datasets
    original_df = pd.read_csv(original_file)
    
    # Try different encodings for the approved files
    for encoding in ['utf-8', 'latin-1', 'cp1252']:
        try:
            reviewed_df_01 = pd.read_csv(reviewed_file_01, encoding=encoding)
            reviewed_df_02 = pd.read_csv(reviewed_file_02, encoding=encoding)
            if encoding != 'utf-8':
                print(f"  (Using {encoding} encoding for approved files)")
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError(f"Could not read approved files with any of: utf-8, latin-1, cp1252")
    
    print(f"Original input file: {len(original_df)} rows")
    print(f"Psychiatrist 01 review file: {len(reviewed_df_01)} rows")
    print(f"Psychiatrist 02 review file: {len(reviewed_df_02)} rows")
    
    # Get unique conversations (Example_IDs)
    original_conversations = set(original_df['Example_ID'].unique())
    approved_conversations_01 = set(reviewed_df_01['Example_ID'].unique())
    approved_conversations_02 = set(reviewed_df_02['Example_ID'].unique())
    
    print(f"\nOriginal conversations: {len(original_conversations)}")
    print(f"Approved conversations (P1): {len(approved_conversations_01)}")
    print(f"Approved conversations (P2): {len(approved_conversations_02)}")
    
    # Identify conversation status for P1
    exact_match_conversations_01 = original_conversations & approved_conversations_01
    removed_conversations_01 = original_conversations - approved_conversations_01
    new_conversations_01 = approved_conversations_01 - original_conversations
    
    # Check for modifications using Edit_Status column for P1
    modified_conversations_01 = set()
    if 'Edit_Status' in reviewed_df_01.columns:
        edited_example_ids = reviewed_df_01[reviewed_df_01['Edit_Status'] == 'P1_EDIT']['Example_ID'].unique()
        modified_conversations_01 = set(edited_example_ids) & exact_match_conversations_01
        print(f"\nP1: Found {len(modified_conversations_01)} conversations with P1_EDIT markers")
    
    exact_no_change_01 = exact_match_conversations_01 - modified_conversations_01
    
    # Identify conversation status for P2
    kept_conversations_02 = original_conversations & approved_conversations_02
    removed_conversations_02 = original_conversations - approved_conversations_02
    
    print(f"\nP1 kept: {len(exact_match_conversations_01)} ({len(exact_no_change_01)} exact + {len(modified_conversations_01)} modified)")
    print(f"P2 kept: {len(kept_conversations_02)}")
    
    # Create output with P1 and P2 scoring
    final_data = []
    
    # Process original conversations
    for example_id in original_df['Example_ID'].unique():
        # Get P1 status
        if example_id in exact_no_change_01:
            p1_status = 'KEPT_exact_match'
        elif example_id in modified_conversations_01:
            p1_status = 'KEPT_with_changes'
        else:
            p1_status = 'REMOVED'
        
        # Get P2 status (will determine if exact match or with changes below)
        p2_status_base = 'KEPT' if example_id in kept_conversations_02 else 'REMOVED'
        
        # Get all rows for this conversation from original
        orig_conv = original_df[original_df['Example_ID'] == example_id].copy()
        orig_conv['Psychiatrist_01'] = p1_status
        orig_conv['original_Example_ID'] = example_id
        
        # Get final utterances and compare with P1's text to determine P2 modification status
        orig_conv['final_Utterance'] = ''
        p2_made_changes = False
        
        if p2_status_base == 'KEPT':
            # Get P2's version
            appr_conv = reviewed_df_02[reviewed_df_02['Example_ID'] == example_id].copy()
            
            # Get P1's version for comparison
            if p1_status in ['KEPT_exact_match', 'KEPT_with_changes']:
                p1_conv = reviewed_df_01[reviewed_df_01['Example_ID'] == example_id].copy()
            else:
                p1_conv = None
            
            for idx, row in orig_conv.iterrows():
                turn = row['Turn']
                speaker = row['Speaker']
                appr_match = appr_conv[(appr_conv['Turn'] == turn) & (appr_conv['Speaker'] == speaker)]
                if not appr_match.empty:
                    p2_text = appr_match.iloc[0]['Utterance']
                    orig_conv.at[idx, 'final_Utterance'] = p2_text
                    
                    # Compare with P1's version to detect P2 modifications
                    if p1_conv is not None:
                        p1_match = p1_conv[(p1_conv['Turn'] == turn) & (p1_conv['Speaker'] == speaker)]
                        if not p1_match.empty:
                            p1_text = p1_match.iloc[0]['Utterance']
                            if p1_text != p2_text:
                                p2_made_changes = True
            
            # Set P2 status based on whether changes were made
            p2_status = 'KEPT_with_changes' if p2_made_changes else 'KEPT_exact_match'
        else:
            # P2 removed, use P1's version if available
            p2_status = 'REMOVED'
            if p1_status in ['KEPT_exact_match', 'KEPT_with_changes']:
                appr_conv = reviewed_df_01[reviewed_df_01['Example_ID'] == example_id].copy()
                for idx, row in orig_conv.iterrows():
                    turn = row['Turn']
                    speaker = row['Speaker']
                    appr_match = appr_conv[(appr_conv['Turn'] == turn) & (appr_conv['Speaker'] == speaker)]
                    if not appr_match.empty:
                        orig_conv.at[idx, 'final_Utterance'] = appr_match.iloc[0]['Utterance']
        
        # Set P2 status column
        orig_conv['Psychiatrist_02'] = p2_status
        final_data.append(orig_conv)
    
    # Combine all data
    output_df = pd.concat(final_data, ignore_index=True)
    
    # Reorder columns
    column_order = ['SubCategory', 'Example_ID', 'Turn', 'Speaker', 'Utterance', 
                    'final_Utterance', 'original_Example_ID', 'Psychiatrist_01', 'Psychiatrist_02']
    column_order = [col for col in column_order if col in output_df.columns]
    output_df = output_df[column_order]
    
    # Calculate statistics by conversation
    conversation_stats = output_df.groupby('Example_ID')[['Psychiatrist_01', 'Psychiatrist_02']].first()
    p1_counts = conversation_stats['Psychiatrist_01'].value_counts()
    p2_counts = conversation_stats['Psychiatrist_02'].value_counts()
    both_kept = ((conversation_stats['Psychiatrist_01'].isin(['KEPT_exact_match', 'KEPT_with_changes'])) & 
                 (conversation_stats['Psychiatrist_02'].isin(['KEPT_exact_match', 'KEPT_with_changes']))).sum()
    
    print(f"\nFinal Scoring Results:")
    print(f"  P1 kept: {p1_counts.get('KEPT_exact_match', 0) + p1_counts.get('KEPT_with_changes', 0)} conversations")
    print(f"    - P1 exact match: {p1_counts.get('KEPT_exact_match', 0)}")
    print(f"    - P1 with changes: {p1_counts.get('KEPT_with_changes', 0)}")
    print(f"  P2 kept: {p2_counts.get('KEPT_exact_match', 0) + p2_counts.get('KEPT_with_changes', 0)} conversations")
    print(f"    - P2 exact match: {p2_counts.get('KEPT_exact_match', 0)}")
    print(f"    - P2 with changes: {p2_counts.get('KEPT_with_changes', 0)}")
    print(f"  Both kept: {both_kept} conversations")
    
    # Save output
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_df.to_csv(output_file, index=False)
    print(f"\nCreated: {output_file}")
    
    return str(output_file)

def create_final_files(intermediate_file: str):
    """
    Create finalized balanced files from intermediate file.
    
    Uses Oct 30 Example_ID manifest to ensure exact reproducibility of experiment data.
    
    Args:
        intermediate_file: Path to intermediate file with P1+P2 scoring
    """
    print("\n" + "="*80)
    print("STEP 2: CREATE FINALIZED BALANCED FILES")
    print("="*80)
    
    # File paths
    p1_p2_scores = Path(intermediate_file)
    output_file = Path('data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv')
    manifest_file = Path('data/inputs/manifests/therapy_engagement_finalized_selection_manifest.csv')
    oct30_id_manifest = Path('data/inputs/manifests/therapy_engagement_oct30_exact_420_example_ids_manifest.csv')
    
    # Load data
    print(f"\nLoading P1+P2 scores from: {p1_p2_scores}")
    scores_df = pd.read_csv(p1_p2_scores)
    print(f"  P1+P2 scores: {len(scores_df)} utterances, {scores_df['Example_ID'].nunique()} conversations")
    
    # Must use Oct 30 Example_ID manifest for reproducibility
    if not oct30_id_manifest.exists():
        raise FileNotFoundError(
            f"Oct 30 Example_ID manifest not found: {oct30_id_manifest}\n"
            f"This manifest is required for exact reproducibility of the 10/30 experiments."
        )
    
    print(f"\n✓ Using Oct 30 Example_ID manifest: {oct30_id_manifest}")
    oct30_id_manifest_df = pd.read_csv(oct30_id_manifest)
    oct30_example_ids = list(oct30_id_manifest_df['Example_ID'].values)  # Preserve order
    print(f"  Oct 30 manifest specifies: {len(oct30_example_ids)} conversations")
    
    # Verify all Oct 30 Example_IDs exist in current data
    print("\nVerifying Oct 30 conversations are available...")
    available_ids = set(scores_df['Example_ID'].values)
    selected_conversations = [eid for eid in oct30_example_ids if eid in available_ids]
    missing_ids = set(oct30_example_ids) - set(selected_conversations)
    
    print(f"  Found: {len(selected_conversations)}/420 conversations")
    if missing_ids:
        print(f"  ⚠️  WARNING: {len(missing_ids)} conversations from Oct 30 are missing:")
        print(f"      {sorted(list(missing_ids))[:10]}...")
        print(f"  This may indicate data changes since Oct 30.")
    
    # Filter to selected conversations
    approved_df = scores_df[scores_df['Example_ID'].isin(selected_conversations)].copy()
    
    # Create selection manifest
    manifest_df = pd.DataFrame({
        'Example_ID': selected_conversations,
        'selected_for_finalized': True
    })
    manifest_file.parent.mkdir(parents=True, exist_ok=True)
    manifest_df.to_csv(manifest_file, index=False)
    print(f"Created selection manifest: {manifest_file}")
    print("  Documents which 420 conversations were selected from intermediate file")
    
    # Filter to selected conversations
    selected_df = approved_df[approved_df['Example_ID'].isin(selected_conversations)].copy()
    
    print(f"  Total utterances: {len(selected_df)}")
    
    # Format as experiment input
    print("\nFormatting for experiment...")
    formatted_rows = []
    
    for example_id in selected_conversations:
        conv_df = selected_df[selected_df['Example_ID'] == example_id]
        
        subcategory = conv_df['SubCategory'].iloc[0]
        counseling_request = map_subcategory_to_counseling_request(subcategory)
        
        # Format conversation
        statement = format_conversation(conv_df)
        
        formatted_rows.append({
            'Safety type': 'no_SI',
            'therapy_engagement': counseling_request,
            'statement': statement,
            'SubCategory': subcategory
        })
    
    # Create output DataFrame
    output_df = pd.DataFrame(formatted_rows)
    
    print(f"\nFormatted {len(output_df)} conversations")
    print(f"  therapy_engagement distribution:")
    for cat, count in output_df['therapy_engagement'].value_counts().items():
        print(f"    {cat}: {count}")
    
    # Save formatted version (this is the finalized file used for experiments)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_df.to_csv(output_file, index=False)
    print(f"\nCreated: {output_file}")
    
    print(f"\n✅ Reproduced {len(selected_conversations)}/420 Oct 30 conversations")
    if len(selected_conversations) < 420:
        print(f"  ⚠️  {420 - len(selected_conversations)} conversations from Oct 30 could not be reproduced")
    
    # Note: Turn-by-turn format is preserved in the intermediate file
    print(f"\nNote: Turn-by-turn format available in intermediate file: {p1_p2_scores}")

if __name__ == "__main__":
    try:
        # Step 1: Create intermediate file
        intermediate_file = create_intermediate_file()
        
        # Step 2: Create final files
        create_final_files(intermediate_file)
        
        print("\n" + "="*80)
        print("✅ SUCCESS: Created all therapy engagement files")
        print("="*80)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
