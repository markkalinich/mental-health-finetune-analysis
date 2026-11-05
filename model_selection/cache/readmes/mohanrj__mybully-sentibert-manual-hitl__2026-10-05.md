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

# MYBully-SentiBERT (Manual + HITL)

## Model Overview
This model is **MYBully-SentiBERT**, fine-tuned on a combination of **manually annotated data + Human-in-the-Loop (HITL) annotated data** from the MYBully dataset.  
It extends the manual baseline with richer sentiment annotations.

## Intended Use
- Sentiment analysis of Bahasa Malaysia tweets (positive, negative, neutral).  
- Research on sentiment classification in low-resource languages.  

## Training Data
- **Dataset:** MYBully (Bahasa Malaysia tweets).  
- **Annotation:** Manual + HITL  

## Model Details
- **Base model:** roberta-base-bahasa-cased  
- **Fine-tuning:** 3-way classification head  
- **Labels:** Positive, Negative, Neutral  

## Performance
| Metric    | Value |
| --------- | ----- |
| Accuracy  | 0.79  |
| Precision | 0.78  |
| Recall    | 0.79  |
| Macro F1  | 0.78  |