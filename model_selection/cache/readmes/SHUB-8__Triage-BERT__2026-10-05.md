---
license: apache-2.0
language:
- en
tags:
- medical
- triage
- classification
- emergency
- esi
pipeline_tag: text-classification
---

# TriageBERT - ESI Triage Classification Model

A BERT-based model fine-tuned for Emergency Severity Index (ESI) classification on PubMedBERT.

## Model Description

This model classifies emergency medical text into 5 ESI levels:
- **ESI 1**: Immediate (life-threatening)
- **ESI 2**: Emergent (high risk)
- **ESI 3**: Urgent (stable but needs multiple resources)
- **ESI 4**: Less Urgent (single resource needed)
- **ESI 5**: Non-Urgent (no resources needed)

## Training

- **Base Model**: PubMedBERT (biomedical domain)
- **Training Data**: MIMIC-IV ED-Triage data + synthetic data
- **Optimization**: Recall-optimized for critical cases (ESI 1-2)

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model
tokenizer = AutoTokenizer.from_pretrained("SHUB-8/Triage-BERT")
model = AutoModelForSequenceClassification.from_pretrained("SHUB-8/Triage-BERT")

# Predict
text = "Patient has chest pain and difficulty breathing"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    esi_level = torch.argmax(probs).item() + 1  # ESI 1-5

print(f"ESI Level: {esi_level}")
```

## Performance

| Metric | Value |
|--------|-------|
| Accuracy | ~85% |
| Recall (ESI 1-2) | ~92% |
| F1 Score | ~83% |

## Intended Use

- Emergency department triage assistance
- Medical emergency prioritization
- Healthcare AI research

## Limitations

- English language only
- Should be used as decision support, not replacement for clinical judgment
- Performance may vary on out-of-distribution data

## Citation

If you use this model, please cite:
```
@misc{triage-bert-esi,
  author = {Your Name},
  title = {TriageBERT: ESI Triage Classification Model},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/SHUB-8/triage-bert-esi-recall-optimized}
}
```
