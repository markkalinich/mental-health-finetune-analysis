---
license: mit
base_model: cardiffnlp/twitter-roberta-base
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

# twitter-roberta-base → TweetEval Sentiment

Small LLM fine-tuned for **social-media (tweet) sentiment analysis**. 3 classes: negative / neutral / positive.

- **Base model:** [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) (~125M, RoBERTa pretrained on tweets)
- **Dataset:** [cardiffnlp/tweet_eval](https://huggingface.co/datasets/cardiffnlp/tweet_eval) (`sentiment` config, 45.6K train)
- **Training:** 3 epochs, lr 2e-5, batch 32, max_len 128, warmup 0.1, weight decay 0.01

## Test-set results (TweetEval sentiment, 12,284 tweets)

| Metric | Score |
|---|---|
| Accuracy | **0.7155** |
| Macro-F1 | **0.7155** |
| Macro-Recall | **0.7268** |
| Speed (T4) | ~1600 tweets/s |

## Comparison vs distilbert-base

| Model | Size | Accuracy | Macro-F1 | tweets/s |
|---|---|---|---|---|
| **twitter-roberta-base (this)** | 125M | **0.7155** | **0.7155** | 1600 |
| distilbert-base | 67M | 0.6888 | 0.6877 | 2897 |

Domain pretraining on tweets gives **+2.7 pts accuracy / +2.8 pts macro-F1** over generic DistilBERT, at ~1.8× the inference cost.

## Usage

```python
from transformers import pipeline
clf = pipeline("text-classification", model="Ido-shraga/twitter-roberta-base-tweeteval-sentiment")
clf("I can't believe how good this is 🔥")
```
