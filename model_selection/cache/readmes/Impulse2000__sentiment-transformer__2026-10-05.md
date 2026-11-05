---
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - transformer
  - custom
  - pytorch
  - trained-from-scratch
datasets:
  - stanfordnlp/imdb
  - stanfordnlp/sentiment140
  - SetFit/sst5
  - financial_phrasebank
  - tweet_eval
language:
  - en
license: mit
---

# Sentiment Transformer — tango

A small (≈13M parameter) transformer encoder trained **entirely from scratch** for
3-class sentiment analysis (negative / neutral / positive).

## Architecture

Pre-layer-norm transformer encoder with [CLS] pooling and a linear classification head.
Built with pure `torch.nn` — no pretrained weights.

| Parameter | Value |
|---|---|
| Hidden dim | 256 |
| FFN dim | 1024 |
| Layers | 6 |
| Heads | 8 |
| Max seq len | 256 |
| Vocab size | 16000 |
| Labels | NEGATIVE, NEUTRAL, POSITIVE |
| Precision | bf16 mixed-precision |

## Training Data

Trained on a combined corpus of:
- **IMDB** (50k movie reviews)
- **Sentiment140** (1M tweets)
- **Yelp** (1M reviews)
- **SST-5** (fine-grained → 3-class)
- **Financial PhraseBank** (finance headlines)
- **TweetEval** (SemEval-2017 tweets)

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model = AutoModelForSequenceClassification.from_pretrained(
    "Impulse2000/sentiment-transformer", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("Impulse2000/sentiment-transformer")
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)
print(pipe("This movie was absolutely fantastic!"))
```
