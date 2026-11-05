---
datasets:
- imdb
language: en
license: apache-2.0
metrics:
- accuracy
- f1
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- distilbert
widget:
- text: I absolutely loved this movie, the acting was phenomenal!
- text: What a waste of time, I want my money back.
---

# my-sentiment-analyzer

Fine-tuned distilbert-base-uncased for binary sentiment classification (0 = negative, 1 = positive).

## Evaluation Results

| Metric | Score |
|---|---|
| Accuracy | 0.877 |
| Precision | 0.869 |
| Recall | 0.887 |
| F1 | 0.878 |

## Usage

```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="Hannia67/my-sentiment-analyzer")
result = classifier("This was a great experience!")
print(result)
```
