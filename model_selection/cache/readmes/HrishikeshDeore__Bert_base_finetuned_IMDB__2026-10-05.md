---
language: en
license: mit
tags:
  - sentiment-analysis
  - imdb
  - bert
  - transformers
  - text-classification
model-index:
  - name: sentiment-bert-imdb
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: IMDB Movie Reviews
          type: imdb
        metrics:
          - type: accuracy
            value: 0.93  # Replace with actual score if available
---

# Sentiment-BERT-IMDB

A BERT-based model fine-tuned on the IMDB movie reviews dataset for **binary sentiment classification** (positive/negative). This model is intended for quick deployment and practical use in applications like review analysis, recommendation systems, and content moderation.

## Model Details

- **Architecture**: `bert-base-uncased`
- **Task**: Sentiment classification (positive vs. negative)
- **Dataset**: [IMDB](https://ai.stanford.edu/~amaas/data/sentiment/)
- **Classes**: `positive`, `negative`
- **Tokenizer**: `bert-base-uncased`

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model = AutoModelForSequenceClassification.from_pretrained("HrishikeshDeore/sentiment-bert-imdb")
tokenizer = AutoTokenizer.from_pretrained("HrishikeshDeore/sentiment-bert-imdb")

nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
result = nlp("This movie was absolutely fantastic!")
print(result)
