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

# Bencode92/tradepulse-finbert-importance

## Description
Fine-tuned FinBERT model for financial importance analysis in TradePulse.

**Task**: Importance Classification  
**Target Column**: `importance`  
**Labels**: ['générale', 'importante', 'critique']

## Performance

*Last training: 2026-04-20 19:18*  
*Dataset: `base_reference.csv` (1797 samples)*

| Metric | Value |
|--------|-------|
| Loss | 1.0043 |
| Accuracy | 0.8156 |
| F1 Score | 0.8143 |

| F1 Macro | 0.8143 |

| Precision | 0.8134 |
| Recall | 0.8156 |

## Training Details

- **Base Model**: Bencode92/tradepulse-finbert-importance
- **Training Mode**: Incremental
- **Epochs**: 2
- **Learning Rate**: 1e-05
- **Batch Size**: 4
- **Class Balancing**: None


## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("Bencode92/tradepulse-finbert-importance")
model = AutoModelForSequenceClassification.from_pretrained("Bencode92/tradepulse-finbert-importance")

# Example prediction
text = "Apple reported strong quarterly earnings beating expectations"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)

predictions = outputs.logits.softmax(dim=-1)
```

## Model Card Authors

- TradePulse ML Team
- Auto-generated on 2026-04-20 19:18:26