---
license: apache-2.0
tags:
- token-classification
- pii-detection
- privacy
- named-entity-recognition
language:
- en
pipeline_tag: token-classification
---

# PII Detection Model

This model is fine-tuned for detecting Personally Identifiable Information (PII) in text.

## Detected PII Types
- Names
- Email addresses
- Phone numbers
- Aadhaar numbers
- PAN cards
- Credit card numbers

## Usage

```python
from transformers import pipeline

# Load the model
pii_pipe = pipeline(
    "token-classification",
    model="Dombara/pii-detection-model",
    aggregation_strategy="simple"
)

# Detect PII
text = "Contact John Doe at john@example.com or 9876543210"
results = pii_pipe(text)
print(results)
```

## Model Details
- Base model: DeBERTa
- Fine-tuned for PII detection
- Supports English text
