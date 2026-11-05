---
license: mit
datasets:
- google-research-datasets/go_emotions
language:
- en
base_model:
- microsoft/deberta-v3-base
tags:
- emotion
- emotion classification
- multilabel-classification
- goemotions
- mental-health
- journaling
- transformers
- deberta
---

# 🧠 MindMap Emotion Classifier (deBERTa v3 + GoEmotions)

A fine-tuned multi-label emotion classification model based on [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) and trained on the [GoEmotions](https://github.com/google-research/goemotions) dataset. This model is designed to power emotional tagging for personal journaling and mental wellness applications like **MindMap**.

## Note: This model is part of the experiment to find the best-performing emotion classification model for our digital journaling web application called MindMap.

## 🚀 Model Details

- **Base Model**: DeBERTa v3 Base
- **Task**: Multi-label emotion classification
- **Dataset**: [GoEmotions](https://huggingface.co/datasets/go_emotions) (27 emotions + neutral)
- **Activation**: Sigmoid
- **Loss**: BCEWithLogitsLoss
- **Output**: Probability scores for each of the 28 emotion labels

### 🏷️ Supported Emotions (28 classes):
admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire,
disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief,
joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise


## 📥 How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "wncelrcn/mindmap-deBERTA-goemotions-multilabel"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

# Sample journal entry
text = "I felt overwhelmed today. I didn't want to get out of bed. But a short walk helped me clear my mind."

# Tokenize input
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.sigmoid(logits)[0]  # Multi-label output

# Map to labels
labels = model.config.id2label
predictions = [(labels[i], float(prob)) for i, prob in enumerate(probs) if prob > 0.05]

# Display
for label, score in sorted(predictions, key=lambda x: -x[1]):
    print(f"{label}: {score:.3f}")
```

## 📊 Evaluation
This model was evaluated using:

Metrics: F1-score (micro/macro), Precision, Recall

Validation split: 90/10 on the simplified GoEmotions dataset

Threshold: 0.05 for emotion label activation

## 🧠 Use Case
Originally fine-tuned for MindMap, a digital journaling app that helps users track and reflect on their emotional well-being. The model enables emotion-aware feedback and visualizations, offering therapeutic insight to users based on their writing.

## 📦 Model Files
pytorch_model.bin: Model weights

config.json: Model configuration

tokenizer.json, tokenizer_config.json: Tokenizer details

special_tokens_map.json, vocab.json: Tokenizer vocabulary


## 📚 Citation / Credit
Base model: Microsoft DeBERTa v3

Dataset: GoEmotions by Google Research

🛠 Maintained by @wncelrcn