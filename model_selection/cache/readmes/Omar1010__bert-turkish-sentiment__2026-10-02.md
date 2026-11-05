---
language: tr
license: mit
base_model: dbmdz/bert-base-turkish-cased
tags:
- text-classification
- sentiment-analysis
- turkish
- bert
datasets:
- winvoker/turkish-sentiment-analysis-dataset
metrics:
- accuracy
- f1
pipeline_tag: text-classification
widget:
- text: Bu ürün gerçekten harika, çok memnun kaldım.
- text: Berbat bir deneyimdi, kesinlikle tavsiye etmiyorum.
- text: Ürün bugün elime ulaştı.
model-index:
- name: bert-turkish-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Turkish Sentiment Analysis Dataset
      type: winvoker/turkish-sentiment-analysis-dataset
    metrics:
    - type: accuracy
      value: 0.9669
    - type: f1
      value: 0.9414
      name: Macro F1
---

# BERTurk Turkish Sentiment Analysis

A fine-tuned version of [`dbmdz/bert-base-turkish-cased`](https://huggingface.co/dbmdz/bert-base-turkish-cased) (BERTurk) for **sentiment classification of Turkish text**. Given a Turkish sentence, it predicts whether the sentiment is **Positive**, **Negative**, or **Notr** (neutral).

## Results

Evaluated on the held-out test split of the [winvoker/turkish-sentiment-analysis-dataset](https://huggingface.co/datasets/winvoker/turkish-sentiment-analysis-dataset):

| Metric | Score |
|--------|-------|
| Accuracy | 0.9669 |
| Macro F1 | 0.9414 |

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Omar1010/bert-turkish-sentiment")
print(clf("Bu ürün gerçekten harika, çok memnun kaldım."))
```

## Labels

- `Positive` — olumlu
- `Negative` — olumsuz
- `Notr` — nötr / neutral

## Training

- **Base model:** BERTurk (`dbmdz/bert-base-turkish-cased`)
- **Dataset:** winvoker/turkish-sentiment-analysis-dataset (subsampled to 60,000 train / 8,000 test)
- **Epochs:** 2, **learning rate:** 2e-5, **max length:** 128, **fp16**

## Limitations

Trained mainly on product-review-style Turkish text, so it performs best on similar language. It may be less reliable on sarcasm, very informal slang, or highly domain-specific text.
