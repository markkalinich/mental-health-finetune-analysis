---
license: apache-2.0
language: en
tags:
  - dominance
  - emotion
  - regression
  - deberta
  - transformers
base_model: microsoft/deberta-v3-base
---

# dominance-deberta-v3

This model is a fine-tuned version of `microsoft/deberta-v3-base` on a normalized regression task using the **EmoBank** dataset. It predicts **dominance scores** (1–5 scale) based on the input sentence.

## 🧠 Use Case

This model is useful for estimating how confident, assertive, or dominant a sentence sounds — useful for behavior analysis, sentiment scoring, or interview assessment systems.

## 🧪 Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained("hasithkovinda/dominance-deberta-v3")
tokenizer = AutoTokenizer.from_pretrained("hasithkovinda/dominance-deberta-v3")

inputs = tokenizer(["I'm confident in my abilities."], return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

# Convert output from 0–1 to 1–5 dominance score
score = outputs.logits.squeeze().item() * 4 + 1
print("Dominance Score:", round(score, 2))
