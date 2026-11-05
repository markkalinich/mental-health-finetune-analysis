---
library_name: transformers
license: mit
datasets:
- aai530-group6/ddxplus
language:
- en
metrics:
- precision
- recall
- f1
base_model:
- cambridgeltl/SapBERT-from-PubMedBERT-fulltext
tags:
- medical-diagnosis
- sapbert
- ddxplus
- pubmedbert
- disease-classification
- differential-diagnosis
---


## Model Details

### Model Description

This model is a fine-tuned version of cambridgeltl/SapBERT-from-PubMedBERT-fulltext on the DDXPlus dataset (50,000 samples) for medical diagnosis tasks.

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** [Aashish Acharya](https://github.com/acharya-jyu)
- **Model type:** sapBERT-BioMedBERT
- **Language(s):** English
- **License:** MIT
- **Finetuned from model:** cambridgeltl/SapBERT-from-PubMedBERT-fulltext

### Model Sources 

- **Repository:** [cambridgeltl/SapBERT-from-PubMedBERT-fulltext](https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext)
- **Dataset:** [aai530-group6/ddxplus](https://huggingface.co/aai530-group6/ddxplus)

## Training Dataset
The model was trained on DDXPlus dataset (50,000 samples) containing:
- Patient cases with comprehensive medical information
- Differential diagnosis annotations
- 49 distinct medical conditions
- Evidence-based symptom-condition relationships
## Performance
### Final Metrics
- Test Precision: 0.8159
- Test Recall: 0.7948
- Test F1 Score: 0.7420
### Training Evolution
- Best Validation Loss: 1.4600
- Stopped at Epoch 4 (Early stopping triggered)

<img src="https://cdn-uploads.huggingface.co/production/uploads/662757230601587f0be9781b/tHpbTt7ZyXSR2Lq2wqRAv.png" width="400" alt="image">
<img src="https://cdn-uploads.huggingface.co/production/uploads/662757230601587f0be9781b/3-WA0SZKYQRXnjafLsFTr.png" width="400" alt="image">


## Intended Use
This model is designed for:
- Medical diagnosis support
- Symptom analysis
- Disease classification
- Differential diagnosis generation

## Out-of-Scope Use
The model should NOT be used for:

- Direct medical diagnosis without professional oversight
- Critical healthcare decisions without human validation
- Clinical applications without proper testing and validation

## Training Details
### Training Procedure

- Optimizer: AdamW with weight decay (0.01)
-  Learning Rate: 1e-5
- Loss Function: Combined loss (0.8 × Focal Loss + 0.2 × KL Divergence)
- Batch Size: 32
- Gradient Clipping: 1.0
- Early Stopping: Patience of 3 epochs
- Training Strategy: Cross-validation with 5 folds


### Model Architecture

- Base Model: cambridgeltl/SapBERT-from-PubMedBERT-fulltext
- Hidden Size: 768
- Attention Heads: 12
- Dropout Rate: 0.5
- Added classification layers for diagnostic tasks
- Layer normalization and dropout for regularization

## Example Usage
<pre>
  from transformers import AutoTokenizer, AutoModel

# Load model and tokenizer
model_name = "acharya-jyu/sapbert-pubmedbert-ddxplus-10k"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Example input structure
input_data = {
    'age': 45,  # Patient age
    'sex': 'M',  # Patient sex: 'M' or 'F'
    'initial_evidence': 'E_91',  # Initial evidence code (e.g., E_91 for fever)
    'evidences': [
        'E_91',  # Fever
        'E_77',  # Cough
        'E_89'   # Fatigue
    ]
}

# Process demographic data and evidence codes
outputs = model(**input_data)

# Outputs will include:
# - Main diagnosis prediction
# - Differential diagnosis probabilities
# - Confidence scores
</pre>
<b>Note: Evidence codes (E_XX) correspond to specific symptoms and conditions defined in the release_evidences.json file. The model expects these standardized codes rather than raw text input.</b>

## Citation
```bibtex
  @misc{acharya2024sapbert,
  title={SapBERT-PubMedBERT Fine-tuned on DDXPlus Dataset},
  author={Acharya, Aashish},
  year={2024},
  publisher={Hugging Face Model Hub}
}

```

## Model Card Contact
[Aashish Acharya](https://github.com/acharya-jyu)