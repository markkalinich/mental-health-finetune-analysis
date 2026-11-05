
---
language: 
- id
- jv
license: apache-2.0
tags:
- emotion-classification
- javanese
- transfer-learning
---

# IndoBERTweet Emotion Classifier (Javanese Ngoko Transfer)

Model ini adalah hasil **Continual Fine-Tuning** dari `indolem/indobertweet-base-uncased` menggunakan dataset **PRDECT-ID**.
Model telah melalui proses **Cross-Lingual Transfer Learning** untuk mengenali emosi dalam bahasa Jawa Ngoko.

## Dataset
- Source: PRDECT-ID (Indonesian)
- Target: PRDECT-JV (Javanese Ngoko Adapted)

## Emosi yang didukung:
0: Happy
1: Sadness
2: Anger
3: Love
4: Fear
