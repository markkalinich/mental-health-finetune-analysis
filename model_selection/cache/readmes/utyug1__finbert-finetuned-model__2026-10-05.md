---
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - sentiment-analysis
language:
  - en
base_model: ProsusAI/finbert
datasets:
  - utyug1/sentiment_dataset
---

# My Sentiment Model

This is a model which was for test purpose fine-tuned from [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) on [utyug1/sentiment_dataset](https://huggingface.co/datasets/utyug1/sentiment_dataset).

## Usage
```python
from transformers import pipeline
sentiment_pipeline = pipeline(
    "text-classification",
    model="utyug1/finbert-finetuned-model",
    return_all_scores=True
)
print(sentiment_pipeline("Markets rallied on positive earnings."))
