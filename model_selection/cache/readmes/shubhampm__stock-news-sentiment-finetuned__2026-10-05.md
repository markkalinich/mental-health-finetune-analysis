---
library_name: transformers
license: mit
base_model: ProsusAI/finbert
tags:
- finance
- sentiment-analysis
- text-classification
- finbert
datasets:
- lmassaron/FinancialPhraseBank
language:
- en
pipeline_tag: text-classification
---

# Stock News Sentiment (FinBERT fine-tune)

Fine-tuned **FinBERT** (`ProsusAI/finbert`) that classifies a stock-market /
financial news headline or sentence as **bullish / neutral / bearish**
(mapped to **BUY / HOLD / SELL** signals in the demo app).

## Model details

- **Base model:** [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) (BERT-base, pretrained on financial text)
- **Task:** 3-class text classification — `bearish` (0), `neutral` (1), `bullish` (2)
- **Language:** English
- **Fine-tuned by:** shubhampm
- **Demo:** [shubhampm/stock-news-sentiment (HF Space)](https://huggingface.co/spaces/shubhampm/stock-news-sentiment) — FastAPI `POST /predict` + Gradio UI

## Training data

[lmassaron/FinancialPhraseBank](https://huggingface.co/datasets/lmassaron/FinancialPhraseBank)
— 3,872 financial news sentences annotated by finance experts
(Malo et al., 2014, "Good Debt or Bad Debt"). 90/10 train/test split (seed 42).

## Training procedure

Fine-tuned with Hugging Face `Trainer` on a Kaggle GPU:

| Hyperparameter | Value |
|---|---|
| Epochs | 3 |
| Batch size | 16 |
| Learning rate | 2e-5 (AdamW) |
| Max sequence length | 128 |

## Evaluation (held-out 10% test split, n=388)

| Metric | Value |
|---|---|
| Accuracy | **0.825** |
| Macro F1 | **0.811** |

| Class | Precision | Recall | F1 |
|---|---|---|---|
| bearish | 0.81 | 0.78 | 0.80 |
| neutral | 0.92 | 0.80 | 0.85 |
| bullish | 0.70 | 0.90 | 0.78 |

## Example predictions

```python
from transformers import pipeline
pipe = pipeline("text-classification", model="shubhampm/stock-news-sentiment-finetuned")
pipe("Company X beats earnings estimates, shares surge 8%")
# bullish (BUY) — confidence ≈ 0.93
pipe("Regulator opens probe into accounting practices at the company")
# bearish (SELL)
```

## Limitations

- Trained on short financial *sentences*; long articles are truncated at 512 tokens.
- English only; forced to choose one of 3 classes even for non-financial input
  (the demo app labels predictions below 55% confidence as UNCLEAR).
- Not investment advice — a small educational fine-tune, not a trading system.
