---
language: en
license: mit
tags:
  - sentiment-analysis
  - distilbert
  - imdb
  - peft
  - lora
datasets:
  - imdb
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# DistilBERT Fine-Tuned on IMDb Sentiment

A DistilBERT model fine-tuned on the IMDb movie review dataset for binary sentiment classification (POSITIVE/NEGATIVE), using LoRA (Low-Rank Adaptation) for parameter-efficient fine-tuning.

## Intended Use

Classify English movie reviews and similar text as positive or negative sentiment. Built as a portfolio project demonstrating the ML fine-tuning pipeline.

## Training Data

- Dataset is IMDb movie reviews (25,000 train / 25,000 test)
- Train/Val split is 90/10 from training set (stratified, seed=42)
- Test set is original 25,000 held-out reviews

## Training Procedure

- Base model: distilbert-base-uncased
- Method: LoRA (r=8, alpha=16, dropout=0.1, targets q_lin v_lin)
- Epochs: 2
- Learning rate: 2e-5
- Weight decay: 0.01
- Batch size: 16 train / 64 eval
- Optimizer: AdamW
- Best model selection based on F1

## Evaluation Results

| Metric   | Baseline (SST-2 pretrained) | Fine-tuned (IMDb) |
|----------|-----------------------------|-------------------|
| Accuracy | 0.8907                      | 0.8878            |
| F1       | 0.8875                      | 0.8884            |

> Baseline is `distilbert-base-uncased-finetuned-sst-2-english` evaluated zero-shot on IMDb test set.
> Fine-tuned results are from the final model evaluated on the held-out IMDb test set (25,000 reviews).

## Limitations

- English only
- Trained on movie reviews (other domains not validated)
- Binary classification only (POSITIVE / NEGATIVE)
- Max input 512 tokens

## How to Use
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Harry918/distilbert-imdb-sentiment")
result = classifier("This movie was absolutely fantastic!")
# Expected output: [{"label": "POSITIVE", "score": 0.99}]
print(result)
```

---

> **Published to Hub:** https://huggingface.co/Harry918/distilbert-imdb-sentiment