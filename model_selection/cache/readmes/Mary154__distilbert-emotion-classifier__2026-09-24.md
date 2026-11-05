---
language: en
license: apache-2.0
base_model: distilbert-base-uncased
tags:
  - text-classification
  - emotion
  - distilbert
metrics:
  - accuracy
  - f1
---

# DistilBERT Emotion Classifier

Fine-tuned DistilBERT model for six-way Twitter emotion classification:
sadness, joy, love, anger, fear, and surprise.

Validation metrics:

- Accuracy: 0.9370
- Weighted F1: 0.9371
- Macro F1: 0.9113

Test metrics:

- Accuracy: 0.9230
- Weighted F1: 0.9227
- Macro F1: 0.8767

Training setup: 3 epochs, learning rate 2e-5, batch size 64, weight decay 0.01,
fp16 training, and best-checkpoint loading by validation weighted F1.
