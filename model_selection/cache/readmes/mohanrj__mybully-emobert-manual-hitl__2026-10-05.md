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

# MYBully-EmoBERT (Manual + HITL)

## Model Overview
This model is **MYBully-EmoBERT**, trained on **manual + HITL annotations** from MYBully for Emotion Detection.  
It benefits from iterative HITL refinement to improve robustness.  

## Intended Use
- Detecting emotions in Bahasa Malaysia tweets (e.g., anger, joy, sadness, fear).  

## Training Data
- **Dataset:** MYBully (Bahasa Malaysia tweets).  
- **Annotation:** Manual + HITL
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
| Metric    | Value |
| --------- | ----- |
| Accuracy  | 0.66  |
| Precision | 0.67  |
| Recall    | 0.66  |
| Macro F1  | 0.66  |