---
language: en
license: apache-2.0
tags:
- finance
- sentiment-analysis
- roberta
- classification
model-index:
- name: RoBERTa-Large for Financial Sentiment Analysis
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Finance News Sentiments (Kaggle)
      type: text
    metrics:
    - type: accuracy
      value: 0.7627
    - type: multiclass_roc_auc
      value: 0.9124
base_model:
- FacebookAI/roberta-large
---

# RoBERTa-Large Fine-Tuned for Financial Sentiment Analysis

This repository contains a RoBERTa-based model for financial sentiment classification. The model predicts whether a financial news headline or sentence is **positive**, **neutral**, or **negative**.

## Model Overview
- **Base model:** RoBERTa-Large
- **Task:** Financial sentiment classification (3 classes)
- **Training data:** Financial news headlines and sentences
- **Dataset source:** [Kaggle - Finance News Sentiments](https://www.kaggle.com/datasets/antobenedetti/finance-news-sentiments/data?select=dataset.csv)
- **Output labels:**
  - 0: Negative
  - 1: Neutral
  - 2: Positive

## Evaluation Results
- **Test Accuracy:** 0.7627
- **Multiclass ROC AUC (macro-average):** 0.9124

## Model Folder Structure
```
roberta_finance_sentiment/
    config.json
    merges.txt
    model.safetensors
    special_tokens_map.json
    tokenizer_config.json
    tokenizer.json
    vocab.json
```
**Note:** Only the model files are stored in `roberta_finance_sentiment/`. Scripts and datasets are kept separate and are not included in this folder or in the model upload.

## How to Use the Fine-Tuned Model

### 1. Load and Use the Model in Python
```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
# Directory of the model folder
model_dir = "roberta_finance_sentiment"
# read the model
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)
model.eval()

# Example
text = "Apple stock surges after strong earnings report."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
with torch.no_grad():
    logits = model(**inputs).logits
    pred = torch.argmax(logits, dim=1).item()

label_map = {0: 'negative', 1: 'neutral', 2: 'positive'}
print(f"Predicted sentiment: {label_map[pred]}")
```

## Notes
- The model was trained and evaluated on data from the Kaggle dataset linked above.
- The `roberta_finance_sentiment/` folder contains only the files needed for inference.
- Scripts and datasets are not included in the model folder or in the model upload.
- For best results, use a GPU for inference if available.

## Limitations
- Model is trained on headline-level sentiment.
- Sarcasm, irony, or complex phrasing may reduce prediction accuracy.
---

**Date:** June 2025