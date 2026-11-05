---
language: en
tags:
  - goemotions
  - multi-label
  - distilbert
  - emotion-detection
  - transformers
  - text-classification
license: apache-2.0
datasets: go_emotions
library_name: transformers
pipeline_tag: text-classification
---

# 🧠 DistilBERT Emotion Classifier (GoEmotions, Multi-Label)

This model is a fine-tuned version of **[`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased)** on the **[GoEmotions (Simplified)](https://huggingface.co/datasets/go_emotions)** dataset — a **multi-label emotion classification** task with 28 emotion categories.

It uses `sigmoid` + `BCEWithLogitsLoss` and supports **multiple simultaneous emotion predictions** per sentence.

---

## 🏷️ Labels

There are **28 possible emotions**, including:
> admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral

---

## 📦 Training Setup

- Base model: `distilbert-base-uncased`
- Dataset: `go_emotions` (simplified version with 28 labels)
- Task type: Multi-label classification
- Loss: `BCEWithLogitsLoss` (enabled via `problem_type="multi_label_classification"`)
- Epochs: 3
- Batch size: 16
- Learning rate: 2e-5
- Framework: `transformers` Trainer

---

## 🚀 Usage Example

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained("TuhinG/distilbert-goemotions")
tokenizer = AutoTokenizer.from_pretrained("TuhinG/distilbert-goemotions")

text = "I'm feeling excited and a little nervous about tomorrow."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.sigmoid(logits)[0]

# Threshold and map to labels
emotions = [
    "admiration", "amusement", "anger", "annoyance", "approval", "caring", "confusion", "curiosity",
    "desire", "disappointment", "disapproval", "embarrassment", "excitement", "fear", "gratitude", "grief",
    "joy", "love", "nervousness", "optimism", "pride", "realization", "relief", "remorse", "sadness",
    "surprise", "neutral"
]

for i, prob in enumerate(probs):
    if prob > 0.5:
        print(f"{emotions[i]}: {prob:.2f}")
```

---

## 📊 Evaluation Metric

During training, micro and macro **F1 scores** were used:
- `f1_micro`: high recall on rare labels
- `f1_macro`: balanced performance across labels

---

## ✨ Author

Fine-tuned and maintained by [TuhinG](https://huggingface.co/TuhinG)

---

## 🛡️ License

Apache 2.0 — free to use, share, and modify.
```

---

## ✅ Next Steps

You can now:
1. Copy this to a file: `README.md`
2. Place it inside your model folder (`./distilbert_emotion_model`)
3. Push it to Hugging Face again:

```python
from huggingface_hub import upload_folder

upload_folder(
    folder_path="./distilbert_emotion_model",
    repo_id="TuhinG/distilbert-goemotions",
    repo_type="model",
    commit_message="Add model card README"
)
```

Let me know if you'd like me to generate the Python code for pushing this, or if you'd like to preview the model page before making it public.