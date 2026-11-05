---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
datasets:
  - stanfordnlp/imdb
metrics:
  - accuracy
pipeline_tag: text-classification
---

# distilbert-imdb-sentiment

This is [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) fine-tuned for binary sentiment
classification (positive/negative) on the [IMDB movie reviews dataset](https://huggingface.co/datasets/stanfordnlp/imdb).

## Training details

- **Base model:** `distilbert-base-uncased`
- **Dataset:** `stanfordnlp/imdb`, full train split (25,000 examples)
- **Epochs:** 3
- **Max sequence length:** 256 (padding + truncation)
- **Evaluation:** full test split (25,000 examples), evaluated after every epoch

## Results

| Epoch | Train loss | Test loss | Test accuracy |
| --- | --- | --- | --- |
| 1 | 0.302 | 0.283 | 88.5% |
| 2 | 0.157 | 0.366 | 89.2% |
| 3 | 0.068 | 0.385 | 91.2% |

Final test accuracy: **91.2%**

## Usage

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

repo_id = "Niophy/distilbert-imdb-sentiment"
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)
model.eval()

id2label = {0: "negative", 1: "positive"}

sentence = "This movie was absolutely fantastic"
inputs = tokenizer(sentence, return_tensors="pt", truncation=True, max_length=256)
with torch.no_grad():
    logits = model(**inputs).logits
predicted_id = torch.argmax(logits, dim=-1).item()

print(id2label[predicted_id])
```

## Limitations

Test loss rises after epoch 1 even as accuracy keeps improving, indicating mild overfitting by epoch 3. Training for
more epochs without regularization (e.g. weight decay, early stopping) is unlikely to help much beyond this point.
