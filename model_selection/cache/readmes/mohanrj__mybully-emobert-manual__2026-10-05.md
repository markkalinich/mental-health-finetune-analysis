---
language:
- ms
tags:
- emotion-detection
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

# MYBully-EmoBERT (Manual)

## Model Overview
This is **MYBully-EmoBERT (Manual)**, trained solely on **manual annotations** of the MYBully dataset for Emotion Detection.  
It serves as a **baseline model**.  

## Intended Use
- Multi-class emotion classification of tweets.  

## Training Data
- **Dataset:** MYBully (Bahasa Malaysia tweets).  
- **Annotation:** Manual
- {'Anger': 0,
 'Disgust': 1,
 'Fear': 2,
 'Happiness': 3,
 'Neutral': 4,
 'Sadness': 5,
 'Surprise': 6}

## Model Details
- **Base model:** roberta-base-bahasa-cased  
- **Fine-tuning:** Multi-class classification head  
- **Labels:** Multiple emotions (e.g., Anger, Joy, Sadness, Fear, Neutral)  

## Performance
| Metric | Value |
|--------|-------|
| Accuracy | 0.65 |
| Precision | 0.66 |
| Recall | 0.65 |
| F1 | 0.65 |