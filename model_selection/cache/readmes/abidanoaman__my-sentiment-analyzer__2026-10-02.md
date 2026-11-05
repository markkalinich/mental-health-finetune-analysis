---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- distilbert
datasets:
- imdb
metrics:
- accuracy
- f1
pipeline_tag: text-classification
widget:
- text: I absolutely loved this movie, the acting was phenomenal!
- text: What a waste of time, I want my money back.
---

# my-sentiment-analyzer

Fine-tuned `distilbert-base-uncased` for binary sentiment classification (0 = negative, 1 = positive).

## Intended Use
Classify English-language text (reviews, comments, feedback) as positive or negative sentiment.

## Training Data
- IMDB movie reviews (25,000 train / 2,500 validation / 25,000 test) — or your custom dataset, if used.

## Training Procedure
- Base model: `distilbert-base-uncased`
- Epochs: 2, Learning rate: 2e-5, Batch size: 32, Max sequence length: 128

## Evaluation Results
| Metric | Score |
|---|---|
| Accuracy | 0.872 |
| Precision | 0.861 |
| Recall | 0.888 |
| F1 | 0.874 |

## Limitations
- Trained on movie reviews; may not generalize well to other domains (e.g., product reviews, formal text) without further fine-tuning.
- Binary classification only — does not detect "neutral" sentiment; neutral inputs will be forced into positive/negative.
- English only.

## Usage
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="abidanoaman/my-sentiment-analyzer")
result = classifier("This was a great experience!")
print(result)
```
