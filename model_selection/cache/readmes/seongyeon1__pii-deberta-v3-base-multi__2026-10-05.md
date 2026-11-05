---
language:
  - en
  - fr
  - de
  - it
license: apache-2.0
library_name: transformers
tags:
  - pii
  - ner
  - token-classification
  - privacy
  - deberta-v3
datasets:
  - ai4privacy/pii-masking-200k
  - nvidia/Nemotron-PII
metrics:
  - f1
  - precision
  - recall
pipeline_tag: token-classification
model-index:
  - name: pii-deberta-v3-base-multi
    results:
      - task:
          type: token-classification
          name: PII Detection (NER)
        metrics:
          - type: f1
            value: 0.9766
            name: Entity-level F1
          - type: precision
            value: 0.9703
            name: Entity-level Precision
          - type: recall
            value: 0.9830
            name: Entity-level Recall
---

# PII Detection — DeBERTa-v3-base (Multi-Dataset)

A token classification (NER) model for **Personally Identifiable Information (PII) detection**, fine-tuned on a combination of [ai4privacy/pii-masking-200k](https://huggingface.co/datasets/ai4privacy/pii-masking-200k) and [nvidia/Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII) datasets.

## Model Description

- **Base model**: [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base)
- **Task**: Token Classification (BIO tagging)
- **Loss**: Focal Loss (alpha=1.0, gamma=2.0)
- **Parameters**: 183M

## Supported Entity Types (7 types, Kaggle PII standard)

| Entity | Description | F1 |
|--------|-------------|-----|
| `NAME_STUDENT` | Person names | 0.979 |
| `EMAIL` | Email addresses | 0.992 |
| `USERNAME` | Usernames | 0.980 |
| `ID_NUM` | ID numbers (SSN, credit card, passport, etc.) | 0.980 |
| `PHONE_NUM` | Phone numbers | 0.992 |
| `URL_PERSONAL` | Personal URLs | 0.992 |
| `STREET_ADDRESS` | Street addresses | 0.958 |

## Usage

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

model_name = "seongyeon1/pii-deberta-v3-base-multi"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

text = "My name is John Smith and my email is john@example.com"
inputs = tokenizer(text, return_tensors="pt", return_offsets_mapping=True)
offset_mapping = inputs.pop("offset_mapping")

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)[0]

for idx, (pred, (start, end)) in enumerate(zip(predictions, offset_mapping[0])):
    label = model.config.id2label[pred.item()]
    if label != "O" and start != 0 and end != 0:
        print(f"{text[start:end]} -> {label}")
```

## Training Details

| Setting | Value |
|---------|-------|
| Epochs | 3 |
| Learning Rate | 2e-5 |
| Batch Size | 8 |
| Max Length | 256 |
| Warmup Steps | 200 |
| Optimizer | AdamW |
| Training Data | ~9,000 samples (ai4privacy 5K + Nemotron 5K) |
| Training Time | ~29 minutes (Apple MPS) |

### Label Merge Strategy

54+ entity types from source datasets are merged into 7 standard Kaggle PII types:
- `FIRSTNAME`, `LASTNAME`, `GIVENNAME`, `SURNAME` → `NAME_STUDENT`
- `SSN`, `CREDITCARDNUMBER`, `IBAN`, `PASSPORT`, ... → `ID_NUM`
- `PHONENUMBER`, `TEL`, `TELEPHONENUM` → `PHONE_NUM`
- `CITY`, `STATE`, `ZIPCODE`, `STREET` → `STREET_ADDRESS`

## Evaluation Results

| Metric | Score |
|--------|-------|
| **F1 (entity-level)** | **0.9766** |
| Precision | 0.9703 |
| Recall | 0.9830 |
| F5 (recall-weighted) | 0.9825 |
| Eval Loss | 0.0014 |

## Training Loss Curve

| Epoch | Train Loss | Eval F1 | Eval F5 |
|-------|-----------|---------|---------|
| 1 | 0.0039 | 0.9434 | 0.9560 |
| 2 | 0.0023 | 0.9738 | 0.9777 |
| 3 | 0.0012 | 0.9766 | 0.9825 |

## Framework

Built with [PolyBed-Pipeline](https://github.com/teddynote-lab/PolyBed-Pipeline) PII Channel.
