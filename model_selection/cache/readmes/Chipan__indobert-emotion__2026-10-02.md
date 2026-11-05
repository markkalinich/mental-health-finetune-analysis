---
license: mit
language:
- id
metrics:
- accuracy
base_model:
- indobenchmark/indobert-base-p1
library_name: transformers
tags:
- 5-emotions
- sentiment-analysis
datasets:
- Chipan/indonesia-5-emotion-cls-dataset
---

# Emotion Classification Model (Bahasa Indonesia)
This is a fine-tuned IndoBERT-based model for emotion classification in Bahasa Indonesia, designed to classify everyday informal or casual text into one of five emotional categories in bahasa Indonesia. The model is particularly useful for applications involving sentiment analysis, mental health monitoring, journaling platforms, or conversational AI.

## 🧠 Model Overview
- Base Model: indobert-base-p1 (by IndoNLU)
- Fine-tuning Task: Multi-class text classification
- Number of Classes: 5
- Model Format: safetensors
- Tokenizer: indobert-base-p1

## 🏷️ Emotion Classes
The model is trained to classify input text into one of the following five emotions:

|   Emotion   |       Description      |
| ----------- |:----------------------:|
|    Marah    |Angry, Frustation       |
|    Sedih    |Sadness, disappointment |
|    Senang   |Joy, excitement         |
|    Stress   |Anxiety, mental pressure|
|   Bersyukur |Gratitude, thankfulness |

## ⚠️ Limitations
- Best performance on informal Indonesian (conversational, daily tone)
- May struggle with sarcasm, code-switching (mix of Indonesian-English), or domain-specific jargon