---
language: en
tags:
  - dream-interpretation
  - emotion-classification
  - deberta
  - mental-health
  - fine-tuned
license: mit
---

# 🌙 Jungian Dream Emotion Classifier

**microsoft/deberta-v3-base** pre-trained on GoEmotions then fine-tuned on
dream narratives for 10-class emotion classification.

## Emotion classes
`anger`, `confusion`, `disgust`, `excitement`, `fear`, `joy`, `neutral`, `peace`, `sadness`, `surprise`

## Training pipeline
1. Pre-trained on **GoEmotions** (28 → 1 simplified label)
2. Fine-tuned on **9 667 dream texts** with class-balanced cross-entropy
3. Max sequence length: **256 tokens**

## Usage
```python
import torch, pickle
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from huggingface_hub import hf_hub_download

REPO = "Aniruddhhhh/jungian-dream-emotion-deberta"
tokenizer = AutoTokenizer.from_pretrained(REPO)
model     = AutoModelForSequenceClassification.from_pretrained(REPO)
model.eval()

le_path = hf_hub_download(REPO, "label_encoder.pkl")
with open(le_path, "rb") as f:
    le = pickle.load(f)

dream = "I was flying above golden mountains, feeling completely free."
enc   = tokenizer(dream, return_tensors="pt",
                  truncation=True, max_length=256)
with torch.no_grad():
    probs = torch.softmax(model(**enc).logits, dim=-1)[0]
emotion = le.inverse_transform([probs.argmax().item()])[0]
print(f"Emotion: {emotion}  ({probs.max():.1%})")
```
