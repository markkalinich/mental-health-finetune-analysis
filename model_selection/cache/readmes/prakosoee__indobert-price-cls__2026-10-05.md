---
language: id
license: mit
pipeline_tag: text-classification
tags:
  - indobert
  - aspect-based-sentiment-analysis
  - sentiment-analysis
base_model: indobenchmark/indobert-base-p2
---

# ABSA Model - Price

This directory contains a fine-tuned BERT model for Aspect-Based Sentiment Analysis (ABSA), specifically targeting the **Price** aspect in the Food and Beverage (F&B) industry.

## Model Details

- **Model Architecture:** BERT for Sequence Classification
- **Base Model:** `indobenchmark/indobert-base-p2`
- **Aspect:** Price (harga, nilai uang, promo)
- **Language:** Indonesian
- **Task:** Multi-class Sentiment Classification

## Label Mapping

The model classifies text into three sentiment categories:

| Label ID | Sentiment | Description                                                                |
| -------- | --------- | -------------------------------------------------------------------------- |
| 0        | Negative  | Expensive, poor value for money, or complaints about pricing.              |
| 1        | Neutral   | General mentions of price without specific positive or negative sentiment. |
| 2        | Positive  | Affordable, good value, or price praise.                                   |

## Evaluation Metrics

Based on the fine-tuning results, the model achieves an overall accuracy of **80%**.

### Classification Report

| Category         | Precision | Recall |  F1-Score  | Support |
| :--------------- | :-------: | :----: | :--------: | :-----: |
| **Negative**     |  0.7742   | 0.8276 |   0.8000   |   29    |
| **Neutral**      |  0.9091   | 0.6452 |   0.7547   |   31    |
| **Positive**     |  0.7632   | 0.9355 |   0.8406   |   31    |
| **Accuracy**     |           |        | **0.8022** | **91**  |
| **Macro Avg**    |  0.8155   | 0.8027 |   0.7984   |   91    |
| **Weighted Avg** |  0.8164   | 0.8022 |   0.7984   |   91    |

## Usage

This model is loaded and used by the ABSA API service. All aspect models share a single tokenizer for optimal performance.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_path = "./absa-fnb-model/model_price"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained("indobenchmark/indobert-base-p2")
```
