---
language:
- ms
tags:
- sentiment-analysis
- malay
- classification
license: mit
datasets:
- mohanrj/MYBully
metrics:
- accuracy
- f1
base_model:
- mesolitica/roberta-base-bahasa-cased
---

# MYBully-SentiBERT (Manual)

## Model Overview
This model is **MYBully-SentiBERT**, fine-tuned exclusively on the **manually annotated portion** of the MYBully dataset.  
It provides a **baseline** for Sentiment Analysis in Bahasa Malaysia tweets.  

## Intended Use
- Sentiment Classification (positive, negative, neutral).  

## Training Data
- **Dataset:** MYBully (Bahasa Malaysia tweets).  
- **Annotation:** Manual  

## Model Details
- **Base model:** roberta-base-bahasa-cased  
- **Fine-tuning:** 3-way classification head  
- **Labels:** Positive, Negative, Neutral  

## Performance
| Metric | Value |
|--------|-------|
| Accuracy | 0.83 |
| Precision | 0.82 |
| Recall | 0.83 |
| F1 | 0.82 |