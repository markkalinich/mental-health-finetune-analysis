---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- finance
- sentiment-analysis
- financial-sentiment
- distilbert
- transformers
datasets:
- zeroshot/twitter-financial-news-sentiment
metrics:
- f1
- accuracy
language:
- en
pipeline_tag: text-classification
---

# DistilBERT Financial Sentiment Classifier

A DistilBERT model finetuned for 3-class financial sentiment classification: **bearish**, **neutral**, and **bullish**. Trained on financial tweets, useful for market signal extraction, portfolio monitoring, and financial NLP pipelines.

## Usage

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="RapidOrc121/deberta-v3-small-financial-sentiment")

pipe("The company reported record profits this quarter.")
# {'label': 'bullish', 'score': 0.91}

pipe("Markets fell sharply amid recession fears.")
# {'label': 'bearish', 'score': 0.87}
```

## Performance

Evaluated on a held-out test set (955 samples, stratified split).

| Class        | Precision | Recall | F1   | Support |
|--------------|-----------|--------|------|---------|
| Bearish      | 0.78      | 0.64   | 0.70 | 144     |
| Neutral      | 0.79      | 0.73   | 0.76 | 193     |
| Bullish      | 0.87      | 0.92   | 0.89 | 618     |
| **Weighted** | **0.84**  | **0.84** | **0.84** | 955 |

Overall accuracy: **84%**

## Dataset

Trained on [zeroshot/twitter-financial-news-sentiment](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment) — ~9,500 financial tweets labeled across three sentiment classes. Split 80/10/10 train/val/test with stratification.

Note: the dataset is class-imbalanced (bullish-heavy), which is reflected in per-class performance. Bearish F1 is lower due to limited negative examples.

## Training

| Hyperparameter        | Value                  |
|-----------------------|------------------------|
| Base model            | distilbert-base-uncased |
| Epochs                | 6                      |
| Learning rate         | 1e-5                   |
| Train batch size      | 32                     |
| Eval batch size       | 64                     |
| Optimizer             | AdamW                  |
| LR scheduler          | Linear with warmup     |
| Warmup                | 10% of steps           |
| Max sequence length   | 128                    |
| Precision             | fp32                   |
| Hardware              | NVIDIA T4              |

Best checkpoint selected by weighted F1 on validation set (epoch 4, F1: 0.8678).

## Intended Use

- Financial news and social media sentiment scoring
- Market signal extraction from text streams
- Feature input for downstream trading or risk models
- Educational reference for financial NLP finetuning

## Limitations

- Trained on Twitter data — may not generalize well to formal financial reports or earnings calls
- Bearish class underperforms due to class imbalance in training data
- English only
- Not intended for use as sole input in financial decision-making

## Framework

- Transformers 5.0.0
- PyTorch 2.10.0+cu128
- Datasets 4.8.3