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

# ABSA Model - Food Quality

This directory contains a fine-tuned BERT model for Aspect-Based Sentiment Analysis (ABSA), specifically targeting the **Food Quality** aspect in the Food and Beverage (F&B) industry.

## Model Details

- **Model Architecture:** BERT for Sequence Classification
- **Base Model:** `indobenchmark/indobert-base-p2`
- **Aspect:** Food Quality (rasa, presentasi, kualitas bahan)
- **Language:** Indonesian
- **Task:** Multi-class Sentiment Classification

## Label Mapping

The model classifies text into three sentiment categories:

| Label ID | Sentiment | Description                                                       |
| -------- | --------- | ----------------------------------------------------------------- |
| 0        | Negative  | Poor quality, bad taste, or complaints about the food.            |
| 1        | Neutral   | General mentions without specific positive or negative sentiment. |
| 2        | Positive  | Good taste, high quality, or praise for the food.                 |

## Evaluation Metrics

Based on the fine-tuning results, the model achieves an overall accuracy of **83%**.

### Classification Report

| Category         | Precision | Recall |  F1-Score  | Support |
| :--------------- | :-------: | :----: | :--------: | :-----: |
| **Negative**     |  0.8864   | 0.7748 |   0.8269   |   151   |
| **Neutral**      |  0.8258   | 0.8050 |   0.8153   |   159   |
| **Positive**     |  0.7912   | 0.9057 |   0.8446   |   159   |
| **Accuracy**     |           |        | **0.8294** | **469** |
| **Macro Avg**    |  0.8345   | 0.8285 |   0.8289   |   469   |
| **Weighted Avg** |  0.8336   | 0.8294 |   0.8289   |   469   |

## Usage

This model is loaded and used by the ABSA API service. All aspect models share a single tokenizer for optimal performance.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_path = "./absa-fnb-model/model_food_quality"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained("indobenchmark/indobert-base-p2")
```
