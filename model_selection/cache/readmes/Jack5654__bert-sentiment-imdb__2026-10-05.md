---
library_name: transformers
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - bert
  - imdb
---

# bert-sentiment-imdb

This is a fine-tuned BERT model for sentiment analysis on the IMDB dataset.

- **Base Model**: `bert-base-uncased`
- **Dataset**: IMDB
- **Task**: Sentiment Analysis (Binary)

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis", model="Jack5654/bert-sentiment-imdb"
)

result = classifier("This movie was amazing! I loved every minute of it.")
print(result)
# [{'label': 'LABEL_1' (positive), 'score': ...}]
```
