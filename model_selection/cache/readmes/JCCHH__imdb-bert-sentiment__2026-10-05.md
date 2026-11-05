---
language: en
license: apache-2.0
base_model: bert-base-uncased
tags:
  - sentiment-analysis
  - imdb
  - text-classification
widget:
  - text: "This movie was absolutely fantastic! Best film I've seen all year."
---

# BERT Fine-tuned on IMDB for Sentiment Analysis

Fine-tuned from `bert-base-uncased` on the Stanford IMDB dataset for binary sentiment classification.

## Training Details

| Parameter | Value |
|-----------|-------|
| Base model | bert-base-uncased |
| Learning rate | 2e-5 |
| Batch size | 4 |
| Epochs | 2 |
| Max sequence length | 512 |

## Usage

```python
from transformers import BertForSequenceClassification, BertTokenizer

tokenizer = BertTokenizer.from_pretrained("COMP6713bert/imdb-bert-sentiment")
model = BertForSequenceClassification.from_pretrained("COMP6713bert/imdb-bert-sentiment")

inputs = tokenizer("This movie was great!", return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    outputs = model(**inputs)
    predicted = torch.argmax(outputs.logits, dim=-1).item()

print("Positive" if predicted == 1 else "Negative")
```

## Labels

- 0: Negative
- 1: Positive