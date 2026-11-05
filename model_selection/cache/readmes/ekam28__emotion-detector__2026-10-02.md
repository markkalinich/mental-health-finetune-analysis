---
license: mit
tags:
- text-classification
- mental-health
- psychology
- roberta
base_model: roberta-base
metrics:
- accuracy
library_name: transformers
---

# Model Card for Emotion Detector

This model is a fine-tuned version of [RoBERTa](https://huggingface.co/roberta-base) trained to classify text into various mental health-related categories. It is designed to analyze social media comments or short texts to identify potential indicators of specific mental health conditions.

## Model Details

### Model Description

- **Developed by:** Ekam-Bitt
- **Model type:** Text Classification (RoBERTa)
- **Language(s):** English
- **License:** MIT
- **Finetuned from model:** roberta-base

### Model Sources

- **Repository:** https://github.com/Ekam-Bitt/emotion-detector-extension

## Uses

### Direct Use

The model is intended to be used for analyzing text to detect emotional states or references to specific mental health conditions. It outputs one of the following 7 labels:

- **Label 0:** ADHD
- **Label 1:** Anxiety
- **Label 2:** Autism
- **Label 3:** BPD (Borderline Personality Disorder)
- **Label 4:** Depression
- **Label 5:** PTSD (Post-Traumatic Stress Disorder)
- **Label 6:** Normal

### Out-of-Scope Use

**CRITICAL DISCLAIMER:** This model is **NOT** a diagnostic tool. It should not be used to diagnose mental health conditions. The results are based on text patterns and statistical probability, not clinical evaluation. It should not be used for automated moderation or decision-making that significantly impacts users without human review.

## How to Get Started with the Model

You can use the Hugging Face `pipeline` to easily load and use this model:

```python
from transformers import pipeline

# Load the pipeline
classifier = pipeline("text-classification", model="Ekam-Bitt/emotion-detector")

# Analyze text
text = "I feel really anxious about the upcoming deadline."
result = classifier(text)

print(result)
# Output example: [{'label': 'LABEL_1', 'score': 0.98}]
# (LABEL_1 corresponds to Anxiety)
```

## Bias, Risks, and Limitations

- **Data Bias:** The model was likely trained on social media data, which may contain biases inherent to those platforms.
- **False Positives:** The model may misclassify casual mentions of symptoms as having a condition.
- **Context:** The model analyzes individual text snippets and may miss broader context.

## Training Details

### Training Data

The model was trained on a dataset of text labeled with the 7 categories listed above.

### Training Procedure

- **Architecture:** RoBERTa For Sequence Classification
- **Tokenizer:** RoBERTa Tokenizer
