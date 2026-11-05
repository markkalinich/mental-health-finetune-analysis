---
license: mit
base_model: distilbert-base-uncased
tags:
  - text-classification
  - distilbert
  - content-moderation
  - the-culture
---

# The Culture: Content Moderation Model (Fine-Tuned DistilBERT)

Binary safe/unsafe classifier for posts, comments, stories, and reels on The Culture, fine-tuned with class-weighted loss to handle the ~70/30 safe/unsafe imbalance. A secondary logistic regression head (trained on the fine-tuned [CLS] embeddings) predicts the unsafe sub-category (counterfeit_goods, link_spam, off_platform_sales, etc.).

## Metrics (label: safe/unsafe)
Accuracy: 1.0000
Full classification report saved in `eval_metrics.json`.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tok = AutoTokenizer.from_pretrained("Dc-4nderson/TheCulture-content-moderation-model")
model = AutoModelForSequenceClassification.from_pretrained("Dc-4nderson/TheCulture-content-moderation-model")

inputs = tok("DM me for exclusive deals not available here", return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
pred = logits.argmax(-1).item()
```

Part of **The Culture** ML model suite.
