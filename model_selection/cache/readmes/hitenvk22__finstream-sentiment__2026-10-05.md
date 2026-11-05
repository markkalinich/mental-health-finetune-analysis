---
language: en
license: apache-2.0
tags:
  - text-classification
  - financial-nlp
  - sentiment-analysis
  - distilroberta
  - finstream
datasets:
  - financial_phrasebank
metrics:
  - accuracy
  - f1
---

# hitenvk22/finstream-sentiment

**FinStream** financial sentiment classifier fine-tuned on Financial PhraseBank.  
Part of the [FinStream Active Learning Pipeline](https://github.com/hitenvk22/finstream).

## Model Description

| Property | Value |
|---|---|
| Base model | `distilroberta-base` |
| Task | 3-class financial sentiment classification |
| Dataset | Financial PhraseBank (~4,845 sentences) |
| Labels | `negative` (Bearish) · `neutral` · `positive` (Bullish) |
| Accuracy | 0.8443298969072165 |
| F1 macro | 0.8457725376192002 |
| Precision | 0.8510783764659424 |
| Recall | 0.8443298969072165 |
| Training hardware | Kaggle T4 GPU · FP16 · 5 epochs |

## Quick Start

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="hitenvk22/finstream-sentiment",
    tokenizer="hitenvk22/finstream-sentiment",
)

result = classifier("The company reported record earnings, beating all analyst estimates.")
print(result)
# [{'label': 'positive', 'score': 0.96}]
```

## Label Mapping

| Integer | Label | Financial meaning |
|---|---|---|
| 0 | negative | Bearish — price likely to fall |
| 1 | neutral | No directional signal |
| 2 | positive | Bullish — price likely to rise |

## Intended Use

- Real-time financial news sentiment scoring  
- Portfolio risk alerts  
- Market signal generation  
- Active learning pipeline retraining target  

## Limitations

- Trained on English-only text  
- Short sentences (< 128 tokens); may underperform on long documents  
- Not fine-tuned on post-2020 financial language  

## Training Details

- Optimiser: AdamW · LR 2e-5 · warmup 10 % · weight decay 0.01  
- Early stopping patience: 2 epochs  
- Dynamic padding via `DataCollatorWithPadding`  
