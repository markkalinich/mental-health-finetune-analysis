---
base_model: bert-base-uncased
tags:
- safety
- occupational-safety
- bert
- domain-adaptation
---

# SafetyBERT

SafetyBERT is a BERT model fine-tuned on occupational safety data from MSHA, OSHA, NTSB, and other safety organizations, as well as a large corpus of occupational safety-related Abstracts.

## Quick Start

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
model = AutoModelForMaskedLM.from_pretrained("adanish91/safetybert")

# Example usage
text = "The worker failed to wear proper [MASK] equipment."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
```

## Model Details

- **Base Model**: bert-base-uncased
- **Parameters**: 110M
- **Training Data**: 2.4M safety documents from multiple sources
- **Specialization**: Mining, construction, transportation safety

## Performance

Significantly outperforms BERT-base on safety classification tasks:
- 76.9% improvement in pseudo-perplexity
- Superior performance on Occupational safety-related downstream tasks

## Applications

- Safety document analysis
- Incident report classification  
