---
tags:
  - text-classification
  - emotion
  - multi-label
  - transformers
  - deberta-v3
  - huggingface
widget:
  - text: "I feel excited but kind of anxious too."
---

# DeBERTa V3 - Multi-label Emotion Classifier

This model is a fine-tuned version of `microsoft/deberta-v3-base` for **multi-label emotion classification**.

## Model Details

- Base model: `DeBERTa V3`
- Task: Multi-label emotion detection
- Architecture: `DebertaV2ForSequenceClassification`
- Number of labels: 14
- Format: `safetensors`

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("PuroFuro/deberta-v3-emotion-multilabel")
model = AutoModelForSequenceClassification.from_pretrained("PuroFuro/deberta-v3-emotion-multilabel")

inputs = tokenizer("I feel nervous but hopeful.", return_tensors="pt")
outputs = model(**inputs)
probs = torch.sigmoid(outputs.logits)
print(probs)
