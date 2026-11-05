---
datasets:
- ai4privacy/pii-masking-400k
metrics:
- accuracy
- recall
- precision
- f1
base_model:
- answerdotai/ModernBERT-base
pipeline_tag: token-classification
tags:
- pii
- privacy
- personal
- identification
---
# 🐟 PII-RANHA: Privacy-Preserving Token Classification Model

## Overview
PII-RANHA is a fine-tuned token classification model based on **ModernBERT-base** from Answer.AI. It is designed to identify and classify Personally Identifiable Information (PII) in text data. The model is trained on the `ai4privacy/pii-masking-400k` dataset and can detect 17 different PII categories, such as account numbers, credit card numbers, email addresses, and more.

This model is intended for privacy-preserving applications, such as data anonymization, redaction, or compliance with data protection regulations.

## Model Details

### Model Architecture
- **Base Model**: `answerdotai/ModernBERT-base`
- **Task**: Token Classification
- **Number of Labels**: 18 (17 PII categories + "O" for non-PII tokens)


## Usage

### Installation
To use the model, ensure you have the `transformers` and `datasets` libraries installed:

```bash
pip install transformers datasets
```

Inference Example
Here’s how to load and use the model for PII detection:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Load the model and tokenizer
model_name = "scampion/piiranha"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Create a token classification pipeline
pii_pipeline = pipeline("token-classification", model=model, tokenizer=tokenizer)

# Example input
text = "My email is john.doe@example.com and my phone number is 555-123-4567."

# Detect PII
results = pii_pipeline(text)
for entity in results:
    print(f"Entity: {entity['word']}, Label: {entity['entity']}, Score: {entity['score']:.4f}")

```

```bash
Entity: Ġj, Label: I-ACCOUNTNUM, Score: 0.6445
Entity: ohn, Label: I-ACCOUNTNUM, Score: 0.3657
Entity: ., Label: I-USERNAME, Score: 0.5871
Entity: do, Label: I-USERNAME, Score: 0.5350
Entity: Ġ555, Label: I-ACCOUNTNUM, Score: 0.8399
Entity: -, Label: I-SOCIALNUM, Score: 0.5948
Entity: 123, Label: I-SOCIALNUM, Score: 0.6309
Entity: -, Label: I-SOCIALNUM, Score: 0.6151
Entity: 45, Label: I-SOCIALNUM, Score: 0.3742
Entity: 67, Label: I-TELEPHONENUM, Score: 0.3440
```

## Training Details

### Dataset
The model was trained on the ai4privacy/pii-masking-400k dataset, which contains 400,000 examples of text with annotated PII tokens.

### Training Configuration
- **Batch Size:** 32 
- **Learning Rate:** 5e-5
- **Epochs:** 4
- **Optimizer:** AdamW
- **Weight Decay:** 0.01
- **Scheduler:** Linear learning rate scheduler

### Evaluation Metrics
The model was evaluated using the following metrics:
- Precision
- Recall
- F1 Score
- Accuracy

| Epoch | Training Loss | Validation Loss | Precision | Recall | F1    | Accuracy |
|-------|---------------|-----------------|-----------|--------|-------|----------|
| 1     | 0.017100      | 0.017944        | 0.897562  | 0.905612 | 0.901569 | 0.993549 |
| 2     | 0.011300      | 0.014114        | 0.915451  | 0.923319 | 0.919368 | 0.994782 |
| 3     | 0.005000      | 0.015703        | 0.919432  | 0.928394 | 0.923892 | 0.995136 |
| 4     | 0.001000      | 0.022899        | 0.921234  | 0.927212 | 0.924213 | 0.995267 |

Would you like me to help analyze any trends in these metrics?

## License
This model is licensed under the Commons Clause Apache License 2.0. For more details, see the Commons Clause website.
For another license, contact the author.

## Author
Name: Sébastien Campion

Email: sebastien.campion@foss4.eu

Date: 2025-01-30

Version: 0.1

## Citation
If you use this model in your work, please cite it as follows:

```bibtex
@misc{piiranha2025,
  author = {Sébastien Campion},
  title = {PII-RANHA: A Privacy-Preserving Token Classification Model},
  year = {2025},
  version = {0.1},
  url = {https://huggingface.co/sebastien-campion/piiranha},
}
```

## Disclaimer
This model is provided "as-is" without any guarantees of performance or suitability for specific use cases. 
Always evaluate the model's performance in your specific context before deployment.