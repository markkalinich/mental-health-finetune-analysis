---
language: en
tags:
- emotion-classification
- distilbert
- ekman-emotions
license: apache-2.0
datasets:
- twitter-reviews-for-emotion-analysis
metrics:
- accuracy
- f1
---

# DistilBERT Fine-tuned for Ekman Emotion Classification (v2)

Versi kedua model, dilatih ulang sebagai bagian eksperimen dengan dataset MBTI baru
(datasnaek/mbti-type) untuk tahap klasifikasi kepribadian selanjutnya.

## Performa Model (Data Uji)
- Accuracy: 0.9082
- Precision (macro): 0.8760
- Recall (macro): 0.9153
- F1-score (macro): 0.8941

## Cara Pakai
```python
from transformers import pipeline
clf = pipeline("text-classification", model="akrvnka/distilbert-emotion-ekman-mbti-v2")
clf("I am so excited for tomorrow!")
```

## Training Detail
- Base model: distilbert-base-uncased
- Epochs: 12 (early stopping, load_best_model_at_end)
- Learning rate: 2e-5
- Class weighting diterapkan untuk menangani ketidakseimbangan kelas
- Dataset: Twitter Reviews for Emotion Analysis (train:val:test = 70:15:15, stratified)
