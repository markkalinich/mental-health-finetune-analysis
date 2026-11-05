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

Fine-tuned from `FacebookAI/roberta-base` on the Amazon Reviews for Sentiment Analysis dataset.

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
  "test_loss": 0.09200309216976166,
  "test_accuracy": 0.97118,
  "test_precision": 0.9724060929898716,
  "test_recall": 0.9702009150586831,
  "test_f1": 0.9713022524047558,
  "test_macro_precision": 0.9711761626172374,
  "test_macro_recall": 0.9711853157638077,
  "test_macro_f1": 0.9711794769766764,
  "test_runtime": 18.3569,
  "test_samples_per_second": 2723.771,
  "test_steps_per_second": 21.3,
  "epoch": 2.0
}
```

## Usage

```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="cagrigungor/shopping-reviews-sentiment-medium")
classifier("This product is excellent.")
```
