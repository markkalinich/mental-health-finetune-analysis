---
base_model: distilbert-base-cased
datasets:
- ai4privacy/pii-masking-300k
language: en
license: apache-2.0
metrics:
- f1
- precision
- recall
tags:
- token-classification
- ner
- pii
- distilbert
- privacy
---

# PII Detection — DistilBERT (English)

Fine-tuned `distilbert-base-cased` for PII (Personally Identifiable Information) detection
on the English subset of [ai4privacy/pii-masking-300k](https://huggingface.co/datasets/ai4privacy/pii-masking-300k).

## Results

- **F1: 0.96**
- 30k training examples, 5k validation, 6 epochs on a Colab T4

## Entity types

`PERSON`, `EMAIL`, `PHONE`, `USERNAME`, `ID_NUMBER`, `ADDRESS`, `IP_ADDRESS`,
`URL`, `DATE_TIME`, `PASSWORD`, `DEMOGRAPHIC`, `OTHER`

## Usage

```python
from transformers import pipeline

ner = pipeline("ner", model="munibz/pii-distilbert-en", aggregation_strategy="simple")

text = "Hi, I'm John Smith. Email me at john.smith@gmail.com."
print(ner(text))
```

## Training

- Base model: distilbert-base-cased
- Max length: 384
- Batch size: 32
- Learning rate: 3e-5 (cosine schedule, 10% warmup)
- Epochs: 6 (early stopping patience 2)
- FP16 on T4 GPU
