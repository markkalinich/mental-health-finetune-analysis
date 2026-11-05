---
language: es
license: apache-2.0
base_model: dccuchile/bert-base-spanish-wwm-cased
datasets:
- SetFit/amazon_reviews_multi_es
metrics:
- accuracy
- f1
pipeline_tag: text-classification
tags:
- sentiment-analysis
- spanish
- beto
- customer-feedback
---

# BETO fine-tuned for 3-class Spanish customer sentiment

Fine-tuned version of [dccuchile/bert-base-spanish-wwm-cased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) (BETO)
for classifying short Spanish customer texts into three business classes: `negativo`, `neutro`, `positivo`.
Built for Laboratorio 4 (Módulo 10, Natural Language Processing) by Grupo 5.

## Labels

| id | label | source stars |
|---|---|---|
| 0 | negativo | 1-2 |
| 1 | neutro | 3 |
| 2 | positivo | 4-5 |

## Training

- Dataset: full `train` split of `SetFit/amazon_reviews_multi_es` (200,000 reviews); official `validation` (5,000) and `test` (5,000).
- Max length 128 WordPiece tokens, batch size 32, learning rate 2e-5, weight decay 0.01, 10% warmup, fp16, 3 epochs with evaluation per epoch and best checkpoint by macro F1 (epoch 2).
- Hardware: single NVIDIA GeForce RTX 4060 (8 GB), 38.6 min.

## Test results (5,000 reviews)

| model | accuracy | macro F1 | F1 negativo | F1 neutro | F1 positivo |
|---|---|---|---|---|---|
| TF-IDF + Logistic Regression (baseline) | 0.737 | 0.705 | 0.798 | 0.492 | 0.823 |
| BETO fine-tuned (this model) | 0.793 | 0.738 | 0.850 | 0.487 | 0.876 |

Most errors involve the `neutro` class. Sarcastic texts tend to be classified as `positivo`.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="rafaelwt/beto-amazon-reviews-es-3clases")
clf("Me cobraron un monto que no corresponde en mi factura.")
```
