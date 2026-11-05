---
language: en
license: apache-2.0
tags:
  - financial-nlp
  - sentiment-analysis
  - distilroberta
  - active-learning
  - transformers
datasets:
  - financial_phrasebank
metrics:
  - accuracy
  - f1
model-index:
  - name: hitenkatariya/FinStream
    results:
      - task:
          type: text-classification
        dataset:
          name: Financial PhraseBank
          type: financial_phrasebank
        metrics:
          - type: accuracy
            value: 0.8680
---

# 📈 FinStream: Financial Sentiment Analysis

> Fine-tuned `distilroberta-base` for 3-class financial sentiment classification.
> Part of the **FinStream** active learning pipeline.

## Model Description

FinStream is a **DistilRoBERTa-base** model fine-tuned on the Financial PhraseBank dataset
(`sentences_allagree` subset) to classify financial news into three sentiment classes:

| Label | ID | Meaning |
|-------|----|---------|
| 🐻 bearish | 0 | Negative market outlook |
| 😐 neutral | 1 | No strong directional signal |
| 🐂 bullish | 2 | Positive market outlook |

## Performance

| Metric | Score |
|--------|-------|
| Test Accuracy | 0.8680 |
| Training Set | Financial PhraseBank (all_agree) |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    'text-classification',
    model='OMCHOKSI108/FinStream',
)

result = classifier("Federal Reserve signals interest rate cuts.")
print(result)  # [{'label': 'bullish', 'score': 0.94}]
```

## Training

- **Base Model:** `distilroberta-base`
- **Dataset:** Financial PhraseBank (`sentences_allagree`)
- **Framework:** Hugging Face Transformers + Trainer API
- **Optimizer:** AdamW with linear warmup
- **Mixed Precision:** FP16 (on GPU)
- **Early Stopping:** Patience = 3 (monitoring eval_f1)

## Authors

|**OM Choksi**

Built as part of the FinStream Active Learning Pipeline — a portfolio-grade financial NLP project.
