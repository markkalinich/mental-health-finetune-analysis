---
language: en
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- sentiment
datasets:
- surrey-nlp/BESSTIE-CW-26
metrics:
- f1
- accuracy
---

# distilbert-base-sentiment

Fine-tuned [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) on the
[BESSTIE-CW-26](https://huggingface.co/datasets/surrey-nlp/BESSTIE-CW-26)
dataset for binary sentiment classification.

## Training

- Base model: `distilbert-base-uncased`
- Task: `sentiment` (binary)
- Epochs: 2
- Batch size: 4
- Learning rate: 2e-5
- Weight decay: 0.01
- Max sequence length: 64
- Seed: 65 (best of {42, 65, 131})
- Optimizer: AdamW (Trainer default)

## Test results

- macro-F1: **0.8753**

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("vyshnav112233/distilbert-base-sentiment")
tokenizer = AutoTokenizer.from_pretrained("vyshnav112233/distilbert-base-sentiment")
inputs = tokenizer("your sentence here", return_tensors="pt", truncation=True, max_length=64)
logits = model(**inputs).logits
```
