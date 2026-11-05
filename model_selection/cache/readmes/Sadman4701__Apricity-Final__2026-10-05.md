---
license: apache-2.0
tags:
- text-classification
- emotion
- NLP
- DeBERTa
language: en
datasets:
- GoEmotions
metrics:
- Training Accuracy
- Validation Accuracy
- Testing Accuracy
- Precisionm
- Recall
- F-1(micro)
pipeline_tag: text-classification
---
# Emotion DeBERTa – 5-Class Emotion Classifier

## Model Description

# Emotion DeBERTa – 5-Class Emotion Classifier

## Model Description

This model is a fine-tuned version of **DeBERTa-v3-base** for emotion classification.
It predicts one of five emotional states from input text:

- `anger`
- `fear`
- `joy`
- `sadness`
- `surprise`

The model was trained as part of a university capstone project focused on building an emotion-aware mental healthcare companion.

## Base Model

- `microsoft/deberta-v3-base`

## Training Details

- **Task:** Text-based emotion classification
- **Architecture:** DeBERTa encoder with a custom classification head
- **Number of labels:** 5
- **Training method:** Supervised fine-tuning
- **Output:** Single-label emotion prediction

The model was originally trained using a custom PyTorch class and later converted into Hugging Face format for deployment and reproducibility.

## Intended Use

This model is designed for:

- Emotion-aware chat applications
- Mental health companion systems
- Sentiment and emotional analysis in academic projects
- Research and educational purposes

It is **not** intended for clinical diagnosis or professional mental health decisions.

## Limitations

- Trained on a limited dataset
- May not generalize well to:
  - Slang-heavy text
  - Code-mixed or multilingual inputs
  - Highly sarcastic or ambiguous sentences
- Predictions should be treated as probabilistic, not factual

## Example Usage

```python
from transformers import pipeline

classifier = pipeline(
    task="text-classification",
    model="Sadman4701/Apricity-Final",
    return_all_scores=True
)

text = "I feel scared but also strangely hopeful about the future."

outputs = classifier(text)

THRESHOLD = 0.5 #change it according to your preferences
predicted_emotions = [
    o["label"] for o in outputs[0] if o["score"] >= THRESHOLD
]

print(predicted_emotions)