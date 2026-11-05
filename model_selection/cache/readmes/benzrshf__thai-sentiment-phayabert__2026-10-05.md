---
language: th
license: mit
tags:
  - sentiment-analysis
  - thai
  - phayathaibert
datasets:
  - wisesight_sentiment
metrics:
  - accuracy
  - f1
model-index:
  - name: thai-sentiment-phayabert
    results:
      - task:
          type: text-classification
        dataset:
          name: wisesight_sentiment
          type: wisesight_sentiment
        metrics:
          - type: accuracy
            value: 0.82
          - type: f1
            value: 0.81
---

# Thai Sentiment Analysis - PhayaThaiBERT

Fine-tuned [PhayaThaiBERT](https://huggingface.co/clicknext/phayathaibert) for Thai sentiment classification.

## Model Details

- **Base Model:** PhayaThaiBERT (110M parameters)
- **Task:** 3-class sentiment (positive/neutral/negative)
- **Dataset:** Wisesight Sentiment (21k training samples)
- **Performance:** 82% accuracy, 0.81 weighted F1

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained("yourusername/thai-sentiment-phayabert")
tokenizer = AutoTokenizer.from_pretrained("yourusername/thai-sentiment-phayabert")

text = "อาหารอร่อยมาก"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
prediction = torch.argmax(outputs.logits, dim=-1).item()

labels = {0: "positive", 1: "neutral", 2: "negative"}
print(labels[prediction])  # positive
```
