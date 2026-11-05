---
pipeline_tag: text-classification
library_name: transformers
language: 
  - en
tags:
  - finance
  - reddit
  - wallstreetbets
  - sentiment-analysis
  - NLP
  - BERT
  - FinBERT
  - FinTwitBERT
  - sentiment
  - finance
  - financial-analysis
  - sentiment-analysis
  - financial-sentiment-analysis
  - stocks
  - stock-market
  - crypto
  - cryptocurrency
base_model: StephanAkkerman/FinTwitBERT-sentiment
datasets:
  - moonscape95/WSBS

---
# FinTwitBERT-wsb-sentiment
This model is a fine-tuned version of [FinTwitBERT-sentiment](https://huggingface.co/StephanAkkerman/FinTwitBERT-sentiment), specifically adapted to understand the informal financial jargon, slang, and sarcasm used on retail trading subreddits like r/wallstreetbets.

## Intended Uses
I finetuned this model so that it can also be used to analyze r/wallstreetbets posts. I noticed the slang and language usage differs compared to Twitter/X users.

## Dataset
FinTwitBERT-wsb-sentiment has been finetuned on [moonscape95/WSBS](https://github.com/moonscape95/WSBS)'s dataset. Specifically on the [WSB_all_agree.csv](https://github.com/moonscape95/WSBS/blob/main/data/WSB_all_agree.csv) dataset.

## Training Code
You can find the Python code [here](https://huggingface.co/StephanAkkerman/FinTwitBERT-wsb-sentiment/blob/main/train.py).

## Usage
Using HuggingFace's transformers library the model and tokenizers can be converted into a pipeline for text classification.

```python
from transformers import pipeline

# Create a sentiment analysis pipeline
pipe = pipeline(
    "sentiment-analysis",
    model="StephanAkkerman/FinTwitBERT-wsb-sentiment",
)

# Get the predicted sentiment
print(pipe("Nice 9% pre market move for $para, pump my calls Uncle Buffett 🤑"))
```

## Labels
* 0: NEUTRAL
* 1: BULLISH
* 2: BEARISH