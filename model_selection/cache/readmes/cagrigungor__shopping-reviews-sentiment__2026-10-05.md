---
language: en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- amazon-reviews
datasets:
- bittlingmayer/amazonreviews
metrics:
- accuracy
- precision
- recall
- f1
---
# Shopping Reviews Sentiment

Fine-tuned from `microsoft/MiniLM-L12-H384-uncased` on the Amazon Reviews for Sentiment Analysis dataset.

## Labels

- 0: NEGATIVE
- 1: POSITIVE

## Training configuration

- Training examples: 500,000
- Evaluation examples: 50,000
- Epochs: 2
- Learning rate: 2e-05
- Maximum sequence length: 256

## Test metrics

```json
{
  "test_loss": 0.11027435213327408,
  "test_accuracy": 0.96528,
  "test_precision": 0.964468617253563,
  "test_recall": 0.9665406803262383,
  "test_f1": 0.9655035370797234,
  "test_macro_precision": 0.9652861807802618,
  "test_macro_recall": 0.9652731553652105,
  "test_macro_f1": 0.9652785420320913,
  "test_runtime": 7.1302,
  "test_samples_per_second": 7012.423,
  "test_steps_per_second": 219.208,
  "epoch": 2.0
}
```

## Usage

```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="cagrigungor/shopping-reviews-sentiment")
classifier("This product is excellent.")
```
