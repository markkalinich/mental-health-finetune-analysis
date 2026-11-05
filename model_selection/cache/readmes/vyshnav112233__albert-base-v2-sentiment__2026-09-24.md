---
language: en
license: apache-2.0
base_model: albert-base-v2
tags:
- text-classification
- sentiment
datasets:
- surrey-nlp/BESSTIE-CW-26
metrics:
- f1
- accuracy
---

# albert-base-v2-sentiment

Fine-tuned [`albert-base-v2`](https://huggingface.co/albert-base-v2) on the
[BESSTIE-CW-26](https://huggingface.co/datasets/surrey-nlp/BESSTIE-CW-26)
dataset for binary sentiment classification.

## Training

- Base model: `albert-base-v2`
- Task: `sentiment` (binary)
- Epochs: 2
- Batch size: 4
- Learning rate: 2e-5
- Weight decay: 0.01
- Max sequence length: 64
- Seed: 42 (best of {42, 65, 131})
- Optimizer: AdamW (Trainer default)

## Test results

- macro-F1: **0.8662**

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("vyshnav112233/albert-base-v2-sentiment")
tokenizer = AutoTokenizer.from_pretrained("vyshnav112233/albert-base-v2-sentiment")
inputs = tokenizer("your sentence here", return_tensors="pt", truncation=True, max_length=64)
logits = model(**inputs).logits
```
