---
language: id
license: mit
pipeline_tag: text-classification
tags:
  - indobert
  - aspect-based-sentiment-analysis
  - sentiment-analysis
  - multilabel-classification
base_model: indobenchmark/indobert-base-p2
---

# ABSA Model - F&B Best (Multilabel)

This directory contains a fine-tuned BERT model for Aspect-Based Sentiment Analysis (ABSA) that simultaneously analyzes **all three aspects** in the Food and Beverage (F&B) industry using multilabel classification.

## Model Details

- **Model Architecture:** BERT for Sequence Classification
- **Base Model:** `indobenchmark/indobert-base-p2`
- **Aspects:** Food Quality, Service, Price (simultaneous detection)
- **Language:** Indonesian
- **Task:** Multilabel Sentiment Classification

## Label Mapping

The model classifies text into three sentiment categories for **each aspect**:

| Label ID | Sentiment | Description                                                       |
| -------- | --------- | ----------------------------------------------------------------- |
| 0        | Negative  | Poor quality, bad service, expensive, or complaints.             |
| 1        | Neutral   | General mentions without specific positive or negative sentiment. |
| 2        | Positive  | Good quality, excellent service, affordable, or praise.          |

**Multilabel Output:** The model can detect multiple aspects in a single text and assign sentiment to each aspect independently.

## Evaluation Metrics

Based on the fine-tuning results, the model achieves the following performance:

### Overall Performance (Epoch 4)
- **Validation Loss:** 0.9696
- **Overall Accuracy:** 90.55%
- **Macro F1-Score:** 90.25%

### F1 Score per Aspect
| Aspect        | F1-Score |
| :------------ | :------: |
| **Food Quality** | 88.43%   |
| **Service**     | 87.10%   |
| **Price**       | 94.75%   |

## Usage

This model is loaded and used by the ABSA API service. It provides simultaneous sentiment analysis for all three aspects.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_path = "./absa-fnb-model/model_absa_fnb_best"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained("indobenchmark/indobert-base-p2")
```

## Multilabel Output Example

The model can detect multiple aspects in a single review:

```json
{
    "Food Quality": "Positive",
    "Service": "Positive", 
    "Price": "Negative"
}
```

**Example Input:** "Makanannya enak dan pelayanannya ramah, tapi harganya agak mahal."

This demonstrates the model's ability to:
- Detect Food Quality aspect with Positive sentiment
- Detect Service aspect with Positive sentiment  
- Detect Price aspect with Negative sentiment
- All in a single inference pass
