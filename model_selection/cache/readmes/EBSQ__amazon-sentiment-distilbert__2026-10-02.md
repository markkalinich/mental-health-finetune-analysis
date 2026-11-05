---
library_name: transformers
license: apache-2.0
datasets:
- amazon-sales-dataset
language:
- en
metrics:
- accuracy
- f1
tags:
- text-classification
- sentiment-analysis
- ecommerce
- pytorch
- distilbert
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

### Model Description

This model is a fine-tuned version of distilbert-base-uncased on an Amazon product reviews dataset. It classifies customer reviews into two sentiment categories:
Negative (label 0): rating < 3.5
Positive (label 1): rating ≥ 3.5
The model is designed to support automated customer service systems by providing real-time sentiment analysis.

- **Developed by:** Estella
- **Model type:** Text Classification
- **Language(s) (NLP):** English
- **License:** apache-2.0
- **Number of Classes:** 2
  - 0: Negative
  - 1: Positive

## Intended Uses & Limitations
**Intended Use:**
- Sentiment analysis for e-commerce customer reviews
- Pre-processing step for automated reply generation or customer feedback dashboard

**Limitations:**
- The model was trained on product reviews from Amazon (electronics, cables, TVs, etc.). Performance on other domains (e.g., clothing, books) may vary.
- It does not detect neutral sentiment; reviews with rating 3.5 are considered positive by the chosen threshold.

## How to Use the Model
You can use this model directly with the Transformers pipeline for text classification.

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="your_username/amazon-sentiment-distilbert")
result = classifier("This product is amazing!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.99}]