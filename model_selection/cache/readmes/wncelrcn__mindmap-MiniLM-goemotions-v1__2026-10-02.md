---
license: mit
datasets:
- google-research-datasets/go_emotions
language:
- en
base_model:
- microsoft/MiniLM-L12-H384-uncased
tags:
- emotion
- emotion classification
- multilabel-classification
- goemotions
- mental-health
- journaling
- transformers
- minilm
---

# 🧠 MindMap Emotion Classifier v3 - MiniLM Version (microsoft/MiniLM-L12-H384-uncased + GoEmotions)

## Note: This model is part of the experiment to find the best-performing emotion classification model for our digital journaling web application called MindMap. 

A fine-tuned multi-label emotion classification model based on [microsoft/MiniLM-L12-H384-uncased](https://huggingface.co/microsoft/MiniLM-L12-H384-uncased) and trained on the [GoEmotions](https://github.com/google-research/goemotions) dataset. This model is designed to power emotional tagging for personal journaling and mental wellness applications like **MindMap**.

## 🚀 Model Details

- **Base Model**: MiniLM-L12-H384-uncased
- **Task**: Multi-label emotion classification
- **Dataset**: [GoEmotions](https://huggingface.co/datasets/go_emotions) (27 emotions + neutral)
- **Output**: Probability scores for each of the 28 emotion labels

### 🏷️ Supported Emotions (28 classes):
admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire,
disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief,
joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise


## 📊 Evaluation
This model was evaluated using:

Metrics: F1-score (micro/macro), Precision, Recall

Validation split: 90/10 on the simplified GoEmotions dataset

Threshold: 0.05 for emotion label activation

## 🧠 Use Case
Originally used for MindMap, a digital journaling app that helps users track and reflect on their emotional well-being. The model enables emotion-aware feedback and visualizations, offering therapeutic insight to users based on their writing.

## 📦 Model Files
model.safetensors: Model weights

config.json: Model configuration

tokenizer.json, tokenizer_config.json: Tokenizer details

special_tokens_map.json, vocab.json: Tokenizer vocabulary


## 📚 Citation / Credit
Base model: Microsoft MiniLM-L12-H384-uncased

Dataset: GoEmotions by Google Research

🛠 Maintained by @wncelrcn