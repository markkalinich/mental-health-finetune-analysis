---
language: en
library_name: transformers
tags:
- transformers
- sentiment-analysis
- distilbert
- text-classification
- imdb
license: apache-2.0
pipeline_tag: text-classification
base_model: distilbert-base-uncased
---

# IMDB Sentiment Classifier (DistilBERT fine-tuned)

**DistilBERT-base-uncased fine-tuned for binary sentiment classification** (positive/negative movie reviews). A genuine transformer fine-tune performed locally on a 1,500-review IMDB subsample.

## Model Characteristics

- **Base model**: `distilbert-base-uncased` (Hugging Face)
- **Task**: Binary sequence classification
- **Eval loss**: 0.0005 (after early stopping on epoch 2)
- **Training**: 2 epochs, lr 2e-5, batch 8, warmup 50 steps

## Data Overview

- Dataset: `stanfordnlp/imdb` (subsampled to 1,500 train / 300 test for CPU feasibility)
- Text truncated/padded to 128 tokens

## Evaluation Results

- Eval loss: 0.000518
- Early stopping triggered at epoch 2 of 3

## Files

- `model.safetensors` — fine-tuned weights
- `config.json` — model config (2 labels)
- `tokenizer.json`, `tokenizer_config.json` — tokenizer
- `eval_metrics.txt` — final evaluation metrics

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
model = AutoModelForSequenceClassification.from_pretrained("bolewara/imdb-sentiment-distilbert")
tokenizer = AutoTokenizer.from_pretrained("bolewara/imdb-sentiment-distilbert")
```

## Writeup

A full case study is in the accompanying writeup (also published on Kaggle): *Fine-Tuning DistilBERT for Movie Review Sentiment Analysis*.

## Provenance

Fine-tuned by Anuj Bolewar (`anujbolewar` on Kaggle) from `distilbert-base-uncased` on `stanfordnlp/imdb`.