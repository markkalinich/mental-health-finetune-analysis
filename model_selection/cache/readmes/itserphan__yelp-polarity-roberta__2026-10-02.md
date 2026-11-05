---
library_name: transformers
license: mit
base_model: roberta-base
tags:
- yelp
- sentiment-analysis
- text-classification
- roberta
- polarity
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: Yelp Polarity Sentiment Classifier
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      type: yelp_polarity
      name: Yelp Polarity
    metrics:
      - type: accuracy
        value: 0.9623
      - type: precision
        value: 0.9607
      - type: recall
        value: 0.9640
      - type: f1
        value: 0.9624
---

# 🍔 Yelp Polarity Classifier (RoBERTa-base)

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the **[Yelp Polarity dataset](https://huggingface.co/datasets/yelp_polarity)**.  
It classifies reviews as **Positive** ⭐ or **Negative** 👎 with high accuracy.  

---

## 🚀 Quick Use

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="itserphan/yelp-polarity-roberta")

print(classifier("The burger was amazing, I'll definitely come back!"))
# [{'label': 'Positive', 'score': 0.998}]

print(classifier("Terrible service. Food was cold and overpriced."))
# [{'label': 'Negative', 'score': 0.996}]
