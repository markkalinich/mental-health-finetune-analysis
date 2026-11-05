---
language: en
license: apache-2.0
tags:
- finance
- sentiment-analysis
- finbert
- trading
pipeline_tag: text-classification
---

# Bencode92/tradepulse-finbert-sentiment

## Description
Fine-tuned FinBERT model for financial sentiment analysis in TradePulse.

**Task**: Sentiment Classification  
**Target Column**: `label`  
**Labels**: ['negative', 'neutral', 'positive']

## Performance

*Last training: 2026-04-20 17:22*  
*Dataset: `base_reference.csv` (1797 samples)*

| Metric | Value |
|--------|-------|
| Loss | 0.0000 |
| Accuracy | 1.0000 |
| F1 Score | 1.0000 |

| F1 Macro | 1.0000 |

| Precision | 1.0000 |
| Recall | 1.0000 |

## Training Details

- **Base Model**: Bencode92/tradepulse-finbert-sentiment
- **Training Mode**: Incremental
- **Epochs**: 2
- **Learning Rate**: 1e-05
- **Batch Size**: 4
- **Class Balancing**: None


## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("Bencode92/tradepulse-finbert-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("Bencode92/tradepulse-finbert-sentiment")

# Example prediction
text = "Apple reported strong quarterly earnings beating expectations"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)

predictions = outputs.logits.softmax(dim=-1)
```

## Model Card Authors

- TradePulse ML Team
- Auto-generated on 2026-04-20 17:22:25