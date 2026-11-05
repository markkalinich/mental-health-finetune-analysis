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

# DistilBERT Fine-tuned for Ekman Emotion Classification

Model ini adalah hasil fine-tuning `distilbert-base-uncased` untuk klasifikasi 6 emosi dasar Ekman
(angry, disgust, fear, happy, sad, surprise) dari teks Twitter, sebagai bagian dari penelitian
Tugas Akhir tentang klasifikasi kepribadian MBTI berbasis distribusi emosi.

## Performa Model (Data Uji)
- Accuracy: 0.9042
- Precision (macro): 0.8723
- Recall (macro): 0.9081
- F1-score (macro): 0.8890

## Cara Pakai
```python
from transformers import pipeline
clf = pipeline("text-classification", model="akrvnka/distilbert-emotion-ekman-mbti")
clf("I am so excited for tomorrow!")
```

## Training Detail
- Base model: distilbert-base-uncased
- Epochs: 12 (dengan early stopping, load_best_model_at_end)
- Learning rate: 2e-5
- Batch size: 32
- Class weighting diterapkan untuk menangani ketidakseimbangan kelas
- Dataset: Twitter Reviews for Emotion Analysis (train:val:test = 70:15:15, stratified)
