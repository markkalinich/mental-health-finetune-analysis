---
language: en
datasets:
  - imdb
metrics:
  - accuracy
model-index:
  - name: BERT IMDB Sentiment Classifier
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: IMDB
          type: imdb
        metrics:
          - type: accuracy
            value: 0.93
tags:
  - sentiment
  - imdb
  - text-classification
  - bert
license: apache-2.0
---

# BERT IMDB Sentiment Classifier

This model is a fine-tuned version of `bert-base-uncased` on the IMDB movie reviews dataset.

## Task

Binary Sentiment Classification:
- `0` → Negative
- `1` → Positive

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("dina1/bert-imdb-sentiment")
tokenizer = AutoTokenizer.from_pretrained("dina1/bert-imdb-sentiment")

text = "This movie was absolutely wonderful!"
inputs = tokenizer(text, return_tensors="pt", truncation=True)
outputs = model(**inputs)

predicted_class = outputs.logits.argmax().item()
print("Predicted Sentiment:", predicted_class)
