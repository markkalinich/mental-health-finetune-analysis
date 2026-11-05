---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- text-classification
- emotion
- distilbert
- PyTorch
datasets:
- dair-ai/emotion
pipeline_tag: text-classification
metrics:
- accuracy
- f1
widget:
- text: "I finally achieved something I've been working toward for months!"
  example_title: "Achievement / Joy"
- text: "I can't stop thinking about what might go wrong tomorrow..."
  example_title: "Anxiety / Fear"
- text: "I am so grateful for all the love and support in my life."
  example_title: "Gratitude / Love"
- text: "It really frustrates me when people don't keep their promises."
  example_title: "Frustration / Anger"
- text: "I was completely blown away by the unexpected news!"
  example_title: "Astonishment / Surprise"
- text: "I feel so lonely and disheartened today."
  example_title: "Sorrow / Sadness"
---

# 🎭 Fine-Tuned DistilBERT Emotion Classifier

This repository hosts a fine-tuned **DistilBERT** model for text emotion classification, trained on the [`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion) dataset.

It categorizes English text into 6 distinct emotional classes:
- **`sadness`** (0)
- **`joy`** (1)
- **`love`** (2)
- **`anger`** (3)
- **`fear`** (4)
- **`surprise`** (5)

---

## 📌 Model Summary

- **Model Architecture**: DistilBERT (`distilbert-base-uncased`)
- **Task**: Text Sequence Classification (Emotion & Sentiment Analysis)
- **Dataset**: `dair-ai/emotion` (20,000 annotated text snippets)
- **Language**: English (`en`)
- **License**: Apache 2.0

---

## 🏷️ Emotion Class Mapping

| Label ID | Emotion Tag | Description & Typical Mood Indicators |
| :---: | :---: | :--- |
| `0` | **sadness** | Feelings of sorrow, heartbreak, grief, disappointment, or loneliness |
| `1` | **joy** | Happiness, excitement, achievement, satisfaction, and delight |
| `2` | **love** | Warmth, affection, appreciation, gratitude, and romantic connection |
| `3` | **anger** | Frustration, annoyance, rage, irritation, and hostility |
| `4` | **fear** | Anxiety, apprehension, nervousness, panic, and terror |
| `5` | **surprise** | Astonishment, awe, unexpected news, and shock |

---

## 🚀 Quickstart Usage

### 1. Using Hugging Face `transformers` Pipeline

```python
from transformers import pipeline

# Initialize the text classification pipeline
classifier = pipeline(
    "text-classification",
    model="lucky377/emotion_classifier",
    return_all_scores=True
)

text = "I am so happy and excited about this new project!"
predictions = classifier(text)

print(predictions)

