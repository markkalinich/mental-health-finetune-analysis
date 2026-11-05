---
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
datasets:
- cardiffnlp/tweet_eval
language:
- en
pipeline_tag: text-classification
tags:
- sentiment-analysis
- twitter
- social-media
metrics:
- accuracy
- f1
---

# distilbert-base → TweetEval Sentiment

Small, fast LLM fine-tuned for **social-media (tweet) sentiment analysis**. 3 classes: negative / neutral / positive.

- **Base model:** [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) (~67M, generic)
- **Dataset:** [cardiffnlp/tweet_eval](https://huggingface.co/datasets/cardiffnlp/tweet_eval) (`sentiment` config, 45.6K train)
- **Training:** 3 epochs, lr 2e-5, batch 32, max_len 128, warmup 0.1, weight decay 0.01

## Test-set results (TweetEval sentiment, 12,284 tweets)

| Metric | Score |
|---|---|
| Accuracy | **0.6888** |
| Macro-F1 | **0.6877** |
| Macro-Recall | **0.6978** |
| Speed (T4) | ~2897 tweets/s |

## Comparison vs twitter-roberta-base

| Model | Size | Accuracy | Macro-F1 | tweets/s |
|---|---|---|---|---|
| twitter-roberta-base | 125M | 0.7155 | 0.7155 | 1600 |
| **distilbert-base (this)** | 67M | 0.6888 | 0.6877 | **2897** |

This model trades ~2.7 pts accuracy for **~1.8× faster inference and half the size** — a good fit for high-throughput or edge deployment.

## Usage

```python
from transformers import pipeline
clf = pipeline("text-classification", model="Ido-shraga/distilbert-base-tweeteval-sentiment")
clf("I can't believe how good this is 🔥")
```
