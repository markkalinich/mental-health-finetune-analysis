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

# Model Description
This model is a fine-tuned version of `FinTwitBERT-sentiment`, specifically adapted to understand the informal financial jargon, slang, and sarcasm used on retail trading subreddits like r/wallstreetbets.

# Labels
* 0: NEUTRAL
* 1: BULLISH
* 2: BEARISH