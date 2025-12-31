# Selection Manifests for Dataset Reproducibility

## Purpose

The selection manifest files document exactly which sentences were selected from the intermediate files (with dual-psychiatrist approval) to create the finalized balanced datasets. This ensures **exact reproducibility** of the experimental data.

## Files

- `SI_finalized_selection_manifest.csv` - 450 statements selected for SI experiments
- `therapy_request_finalized_selection_manifest.csv` - 780 statements selected for therapy request experiments

## Format

Each manifest is a CSV with these columns:
- **Index column**: Row index from the intermediate file (e.g., `SI_psychiatrist_01_and_02_scores.csv`)
- `original_statement`: The original Gemini-generated sentence
- `final_statement`: The psychiatrist-approved version (after any edits)
- `Safety type` or `Counseling Request`: Category label
- `selected_for_finalized`: Always `True` (marks selection)

## Why This Matters

Random sampling with `random_state=42` can produce slightly different results across:
- Different pandas versions
- Different Python versions  
- Different OS environments

The manifest provides a **deterministic** way to recreate the exact dataset used in experiments, independent of these environmental factors.

## Usage Example

To recreate the exact finalized dataset from the manifest:

```python
import pandas as pd

# Read manifest and intermediate file
manifest = pd.read_csv('data/inputs/intermediate_files/therapy_request_finalized_selection_manifest.csv', index_col=0)
intermediate = pd.read_csv('data/inputs/intermediate_files/therapy_request_psychiatrist_01_and_02_scores.csv')

# Use manifest indices to select exact rows
selected_rows = intermediate.loc[manifest.index]

# Create finalized dataset with same structure
finalized = pd.DataFrame({
    'Safety type': selected_rows['Safety type'],
    'therapy_request': selected_rows['Counseling Request'],
    'statement': selected_rows['final_statement']
})

# This matches data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv exactly
finalized.to_csv('recreated_finalized.csv', index=False)
```

## Verification

Run this to verify the manifest matches the finalized file:

```bash
python3 -c "
import pandas as pd
manifest = pd.read_csv('data/inputs/intermediate_files/therapy_request_finalized_selection_manifest.csv', index_col=0)
intermediate = pd.read_csv('data/inputs/intermediate_files/therapy_request_psychiatrist_01_and_02_scores.csv')
actual = pd.read_csv('data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv')
recreated = intermediate.loc[manifest.index]
print(f'Match: {set(recreated[\"final_statement\"]) == set(actual[\"statement\"])}')
"
```

## Regenerating Scripts

The manifests are automatically created when running:
- `python utilities/create_psychiatrist_scoring.py` (SI dataset)
- `python utilities/create_therapy_request_psychiatrist_scoring.py` (Therapy request dataset)

These scripts use `random_state=42` for initial sampling, then save manifests documenting which rows were selected.
