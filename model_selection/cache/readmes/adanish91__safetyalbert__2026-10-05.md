---
base_model: albert-base-v2
tags:
- safety
- occupational-safety
- albert
- domain-adaptation
- memory-efficient
---

# SafetyALBERT

SafetyALBERT is a memory-efficient ALBERT model fine-tuned on occupational safety data. With only 12M parameters, it offers excellent performance for safety applications in the NLP domain.

## Quick Start

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("albert-base-v2")
model = AutoModelForMaskedLM.from_pretrained("adanish91/safetyalbert")

# Example usage
text = "Chemical [MASK] must be stored properly."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
```

## Model Details

- **Base Model**: albert-base-v2
- **Parameters**: 12M (89% smaller than SafetyBERT)
- **Model Size**: 45MB
- **Training Data**: Same 2.4M safety documents as SafetyBERT
- **Advantages**: Fast inference, low memory usage

## Performance

- 90.3% improvement in pseudo-perplexity over ALBERT-base
- Competitive with SafetyBERT despite 9x fewer parameters
- Ideal for production deployment and edge devices

## Applications

- Occupational safety-related downstream applications
- Resource-constrained environments
