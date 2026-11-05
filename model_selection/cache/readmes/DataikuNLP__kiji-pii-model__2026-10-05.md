---
language:
- da
- de
- en
- es
- fr
- nl
license: apache-2.0
library_name: transformers
pipeline_tag: token-classification
tags:
- pii
- privacy
- ner
- token-classification
- crf
- deberta-v2
base_model: microsoft/deberta-v3-small
---

# Kiji PII Detection Model

Token classification model for detecting Personally Identifiable Information (PII) in text. Fine-tuned from [`microsoft/deberta-v3-small`](https://huggingface.co/microsoft/deberta-v3-small) and decoded with a CRF layer for valid BIO sequence prediction.

## Model Summary

| | |
|---|---|
| **Base model** | [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) |
| **Architecture** | DeBERTa-v3 encoder + MLP token classifier + CRF |
| **Parameters** | 184M |
| **Model size** | 703 MB (SafeTensors) |
| **Hidden size** | 768 |
| **Task** | PII token classification (53 BIO labels) |
| **PII entity types** | 26 |
| **Decoder** | CRF (Viterbi) |
| **Max sequence length** | 512 tokens |

## Architecture

```
Input (input_ids, attention_mask)
        │
  DeBERTa-v3 encoder (hidden_size=768)
        │
  Dropout → Linear(768 → 384) → GELU → Dropout
        │
  Linear(384 → 53)        [BIO emission scores]
        │
  CRF                                  [valid BIO transitions]
        │
  Predicted label sequence
```

The token classifier emits per-token BIO scores; a learned CRF layer enforces valid transitions (e.g., an `I-EMAIL` cannot follow a `B-PHONENUMBER`). The training loss is the CRF negative log-likelihood + 0.2×class-weighted token cross-entropy. At inference time, predictions are produced by Viterbi decoding.

## Usage

The repository contains the encoder weights, MLP head, and CRF parameters in a single SafeTensors file. The architecture is custom (`PIIDetectionModel`) and is not loadable via `AutoModelForTokenClassification` — see `model/src/model.py` in the source repository for the head + CRF wiring.

```python
from transformers import AutoTokenizer
from safetensors.torch import load_file

tokenizer = AutoTokenizer.from_pretrained("DataikuNLP/kiji-pii-model")
weights = load_file("model.safetensors")  # downloaded from this repo

text = "Contact John Smith at john.smith@example.com or call +1-555-123-4567."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
# See label_mappings.json for the BIO label set.
```

## PII Labels (BIO tagging)

The model uses BIO tagging with 26 entity types:

| Label | Description |
|-------|-------------|
| `AGE` | Age |
| `BUILDINGNUM` | Building number |
| `CITY` | City |
| `COMPANYNAME` | Company name |
| `COUNTRY` | Country |
| `CREDITCARDNUMBER` | Credit Card Number |
| `DATEOFBIRTH` | Date of birth |
| `DRIVERLICENSENUM` | Driver's License Number |
| `EMAIL` | Email |
| `FIRSTNAME` | First name |
| `IBAN` | IBAN |
| `IDCARDNUM` | ID Card Number |
| `LICENSEPLATENUM` | License Plate Number |
| `NATIONALID` | National ID |
| `PASSPORTID` | Passport ID |
| `PASSWORD` | Password |
| `PHONENUMBER` | Phone number |
| `SECURITYTOKEN` | API Security Tokens |
| `SSN` | Social Security Number |
| `STATE` | State |
| `STREET` | Street |
| `SURNAME` | Last name |
| `TAXNUM` | Tax Number |
| `URL` | URL |
| `USERNAME` | Username |
| `ZIP` | Zip code |


Each entity type has `B-` (beginning) and `I-` (inside) variants, plus `O` for non-PII tokens.

## Training

| | |
|---|---|
| **Epochs** | 30 (with early stopping) |
| **Batch size** | 128 |
| **Learning rate** | 2e-05 |
| **Weight decay** | 0.01 |
| **Warmup steps** | 500 |
| **Precision** | bf16 mixed precision |
| **Early stopping** | patience=3, threshold=0.50% |
| **Loss** | CRF NLL + 0.2×class-weighted token cross-entropy |
| **Optimizer** | AdamW |
| **Metric** | Weighted F1 (token-level) |

## Training Data

Trained on the [DataikuNLP/kiji-pii-training-data](https://huggingface.co/datasets/DataikuNLP/kiji-pii-training-data) dataset — a synthetic multilingual PII dataset with entity annotations.

## Limitations

- Trained on **synthetically generated** data — may not generalize perfectly to all real-world text
- Optimized for the 6 languages in the training data (English, German, French, Spanish, Dutch, Danish)
- Max sequence length is 512 tokens
- CRF transitions are learned from training data — rare BIO transitions may be underweighted
