---
language: en
tags: [text-classification, emotion-detection, mental-health, hci, distilbert, cnn]
datasets: [go_emotions]
metrics: [f1, accuracy]
---
# MoodShift — Hybrid DistilBERT + CNN Emotion Classifier
Novel hybrid architecture for HCI research (ICCA 2026).

## Architecture
- **DistilBERT** → [CLS] global context (768-dim)
- **CNN (kernels 2,3,4)** → local n-gram emotion patterns (384-dim)
- **Fusion** → 1152-dim → Linear(512) → Linear(7)

## Labels
positive | sadness | anger | anxiety | confusion | curiosity | neutral

Best Val F1: **0.9141**
