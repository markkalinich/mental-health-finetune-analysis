---
language: ar
tags:
- sentiment-analysis
- arabizi
- egyptian-arabic
- xlm-roberta
license: mit
---

# XLM-RoBERTa — Arabizi Sentiment Classification

Fine-tuned `./xlmr_arabizi_mlm_adapted` for 3-class sentiment classification
(negative / neutral / positive) on Egyptian Arabizi text.

## Test set results
- Accuracy: 0.8250
- Macro F1: 0.8303
- Per-class F1 (negative / neutral / positive): [np.float64(0.8252), np.float64(0.8704), np.float64(0.7952)]

## Labels
| id | label |
|----|----------|
| 0  | negative |
| 1  | neutral  |
| 2  | positive |

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("nancyahmed114/xlmr-arabizi-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nancyahmed114/xlmr-arabizi-sentiment")
```
