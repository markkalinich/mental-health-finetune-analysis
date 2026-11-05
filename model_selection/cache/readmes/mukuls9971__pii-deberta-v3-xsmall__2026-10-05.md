---
license: mit
language:
- en
library_name: transformers
tags:
- pii
- ner
- token-classification
- privacy
- deberta
datasets:
- ai4privacy/pii-masking-200k
metrics:
- f1
- precision
- recall
base_model: microsoft/deberta-v3-xsmall
pipeline_tag: token-classification
widget:
- text: "My name is John Doe and you can reach me at john.doe@example.com or call 555-0199."
---

# PII Detection Model (DeBERTa-v3-xsmall, Fine-tuned)

This model is a fine-tuned version of `microsoft/deberta-v3-xsmall` for **Named Entity Recognition (NER)** focused on detecting **Personally Identifiable Information (PII)**.

## Model Details

- **Base Model**: `microsoft/deberta-v3-xsmall`
- **Dataset**: `ai4privacy/pii-masking-200k` (English subset, ~43k samples)
- **Training**: 5 epochs, batch size 32 (effective), learning rate 3e-5
- **Best F1**: 0.59

## Intended Use

This model is designed for:
- Detecting PII entities in text (Names, Emails, Phone Numbers, Addresses, SSNs, etc.)
- Privacy compliance and data anonymization pipelines
- Research and development in privacy-preserving NLP

## Limitations

- Trained primarily on English text.
- Performance may vary on domain-specific or out-of-distribution data.
- Not a replacement for comprehensive privacy review.

## How to Use

```python
from transformers import pipeline

pii_detector = pipeline("ner", model="mukuls9971/pii-deberta-v3-xsmall", aggregation_strategy="simple")
text = "Contact me at jane.smith@example.org or call (555) 123-4567."
results = pii_detector(text)
print(results)
```
