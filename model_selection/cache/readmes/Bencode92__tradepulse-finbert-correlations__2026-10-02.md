---
language: en
license: apache-2.0
tags:
- finance
- sentiment-analysis
- finbert
- trading
- multi-label
pipeline_tag: text-classification
---

# Bencode92/tradepulse-finbert-correlations

## Description
Fine-tuned FinBERT model for financial correlations analysis in TradePulse.

**Task**: Correlations Classification  
**Target Column**: `correlations`  
**Multi-Label**: Yes (61 labels)

## Performance

*Last training: 2025-07-30 12:03*  
*Dataset: `base_reference.csv` (708 samples)*

| Metric | Value |
|--------|-------|
| Loss | 0.1960 |
| Subset Accuracy | 0.0000 |
| F1 Score | 0.0000 |
| F1 Micro | 0.0000 |
| F1 Macro | 0.0000 |
| Hamming Score | 0.9799 |
| Precision | 0.0000 |
| Recall | 0.0000 |

## Training Details

- **Base Model**: Bencode92/tradepulse-finbert-correlations
- **Training Mode**: Incremental
- **Epochs**: 2
- **Learning Rate**: 1e-05
- **Batch Size**: 4
- **Class Balancing**: None
- **Problem Type**: Multi-Label Classification

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("Bencode92/tradepulse-finbert-correlations")
model = AutoModelForSequenceClassification.from_pretrained("Bencode92/tradepulse-finbert-correlations")

# Example prediction
text = "Apple reported strong quarterly earnings beating expectations"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
# Multi-label: apply sigmoid and threshold
predictions = torch.sigmoid(outputs.logits).squeeze() > 0.5
```

## Model Card Authors

- TradePulse ML Team
- Auto-generated on 2025-07-30 12:03:53