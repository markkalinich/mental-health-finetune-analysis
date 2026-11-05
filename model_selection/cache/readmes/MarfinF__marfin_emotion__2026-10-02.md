---
license: apache-2.0
language: 
  - id
  - en
base_model: MoritzLaurer/mDeBERTa-v3-base-mnli-xnli
pipeline_tag: zero-shot-classification
tags:
  - mood
  - emotion
  - indonesian
  - nli
metrics:
  - accuracy
library_name: transformers
---


# Marfin Emotion Detection Model 🎵

This model is fine-tuned from `MoritzLaurer/mDeBERTa-v3-base-mnli-xnli` for **emotion detection** tasks based on chat context, specifically optimized for **Indonesian and English**.

## 📝 Use Case
The model predicts the relationship between user chat input and emotional hypotheses. It helps detect emotions like:
- `senang` (happy)
- `sedih` (sad)
- `marah` (angry)
- `takut` (fear)
- `cinta` (love)

This is useful for:
- Emotion-based music recommendation
- Sentiment analysis in real-time chat apps
- AI-driven mood detection systems

## 📊 Training Details
- Base model: mDeBERTa-v3-base-mnli-xnli
- Fine-tuned with custom NLI-style dataset
- Metrics: **Accuracy**

## 🏷 Tags
`Zero-Shot Classification`, `Emotion`, `Mood`, `Indonesian`, `English`

## 📥 Example Usage
```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="MarfinF/marfin_emotion")

text = "Aku lagi sedih banget hari ini"
labels = ["senang", "sedih", "marah", "takut", "cinta"]
result = classifier(text, candidate_labels=labels)

print(result)