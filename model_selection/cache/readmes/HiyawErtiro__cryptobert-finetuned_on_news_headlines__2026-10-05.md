---
library_name: transformers
tags:
- sentiment-analysis
- cryptocurrency
- bitcoin
- finance
- text-classification
base_model: ElKulako/cryptobert
pipeline_tag: text-classification
license: mit
---

# Update

Updated the model with more real headlines(2024-July 2026) + 1k more syntethic data.

# CryptoBERT Fine-Tuned on Bitcoin News Headlines

A directional sentiment classifier for Bitcoin news headlines, fine-tuned from [ElKulako/cryptobert](https://huggingface.co/ElKulako/cryptobert).

## Model Description

CryptoBERT was trained on retail social media posts (StockTwits, Twitter, Reddit), which gives it strong crypto-specific vocabulary but a poor match for journalistic headline text. Zero-shot, it scores 0.39 macro-F1 on Bitcoin headlines, close to random for a 3-class task. This model fine-tunes CryptoBERT on ~41,400 headlines relabeled with a directional market-impact rubric, reaching 0.78 macro-F1 on an independent held-out set.

- **Developed by:** Hiyaw Ertiro
- **Model type:** BERT-based sequence classification (3-class)
- **Language:** English
- **License:** MIT
- **Finetuned from model:** [ElKulako/cryptobert](https://huggingface.co/ElKulako/cryptobert)

### Labels

| ID | Label |
|---|---|
| 0 | Bearish (negative) |
| 1 | Neutral |
| 2 | Bullish (positive) |

Labels are directional (does the event plausibly move price), not tonal (does the headline read positive/negative). See the [dataset card](https://huggingface.co/datasets/hiyawtaken/bitcoin-news-headlines-with-sentiment-labels) for the full labeling rubric.

### Direct Use

Sentiment scoring of English-language Bitcoin news headlines, as a feature for downstream pipelines (price prediction, trading signal aggregation, market monitoring dashboards).

## How to Get Started

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model = AutoModelForSequenceClassification.from_pretrained("hiyawtaken/cryptobert-finetuned_on_news_headlines")
tokenizer = AutoTokenizer.from_pretrained("hiyawtaken/cryptobert-finetuned_on_news_headlines")

headline = "Bitcoin surges to new all-time high as ETF inflows accelerate"
inputs = tokenizer(headline, return_tensors="pt", truncation=True, max_length=128)
with torch.no_grad():
    logits = model(**inputs).logits
pred = torch.argmax(logits, dim=-1).item()
print(model.config.id2label[pred])
```

## Training Details

### Training Data

[labeled-bitcoin-news-headlines](https://huggingface.co/datasets/HiyawErtiro/bitcoin-news-sentiments-latest), built on top of [Bitcoin News Sentiment Dataset](https://www.kaggle.com/datasets/filipemunizz/bitcoin-news-and-sentiment-analysis) by filipemunizz (2011-2024) + headlines pulled from google news(2024-July 2026). The original tone-based labels were relabeled with DeepSeek V4 Flash using an explicit directional rubric, with noise removed (ads, listicles, evergreen explainers, non-English headlines, generic roundups). ~41,400 real headlines plus ~500 synthetic headlines (fictional companies, clearly disclosed as synthetic) added to correct two specific model failure patterns found during validation: reasoning about transaction magnitude ($2 vs. $2M) and disambiguating near-identical dollar figures referring to different underlying events.

### Training Procedure

Full fine-tune (all parameters updated, not a frozen-encoder head-only tune), warm-started from CryptoBERT's existing 3-class head.


#### Training Hyperparameters

- **Base model:** ElKulako/cryptobert
- **Epochs:** 3
- **Batch size:** 32
- **Learning rate:** Dynamic
- **Training regime:** fp16 mixed precision
- **Metric for best checkpoint:** macro-F1 (not accuracy, due to class imbalance)


### Testing Data

An independent, hand-labeled set of 72 live-scraped 2026 Bitcoin headlines, never seen during labeling or training.

### Metrics

Macro-F1 was used instead of accuracy because the classes are imbalanced (neutral is the largest class), and accuracy alone would reward a model that defaults to the majority class.

### Results

| Model | Macro-F1 |
|---|---|
| CryptoBERT (zero-shot) | 0.39 |
| **This model (fine-tuned)** | **0.78** |

| Class | Precision | Recall | F1 |
|---|---|---|---|
| Bearish | 0.85 | 0.73 | 0.79 |
| Neutral | 0.80 | 0.69 | 0.74 |
| Bullish | 0.74 | 0.89 | 0.81 |

#### Summary

Fine-tuning improves macro-F1 by +38.5 points over zero-shot CryptoBERT on headline-length text, confirming that CryptoBERT's social-media training data transfers poorly to journalistic headlines without adaptation.

## Bias, Risks, and Limitations

- Training labels are LLM-generated (DeepSeek V4 Flash), not human-annotated. Treat as strong weak supervision, not ground truth.
- The neutral/positive boundary is inherently fuzzy for headlines with implied but unstated direction (price predictions, analyst commentary). Some disagreement with human judgment is expected.
- The model has limited ability to reason about transaction magnitude and to disambiguate near-identical numeric details referring to different underlying events, even after targeted synthetic data augmentation. This is a known limitation of a 110M-parameter text classifier rather than something expected to fully resolve with more data of the same kind.

### Recommendations

Use as one signal among several in a larger pipeline, not as a standalone decision-maker. Review model predictions on headlines involving specific dollar amounts or company financial actions with extra scrutiny given the documented magnitude-reasoning limitation.


### Model Architecture and Objective

BERT-based (RoBERTa-family) sequence classification, 3-class softmax output.


#### Hardware

NVIDIA RTX 3090 (24GB VRAM)

#### Software

PyTorch, Hugging Face Transformers, Datasets

## Model Card Contact

Hiyaw Ertiro — https://huggingface.co/datasets/HiyawErtiro/bitcoin-news-sentiments-latest