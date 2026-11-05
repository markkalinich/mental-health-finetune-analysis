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

# ABSA Model - Service

This directory contains a fine-tuned BERT model for Aspect-Based Sentiment Analysis (ABSA), specifically targeting the **Service** aspect in the Food and Beverage (F&B) industry.

## Model Details

- **Model Architecture:** BERT for Sequence Classification
- **Base Model:** `indobenchmark/indobert-base-p2`
- **Aspect:** Service (pelayanan, keramahan, kecepatan)
- **Language:** Indonesian
- **Task:** Multi-class Sentiment Classification

## Label Mapping

The model classifies text into three sentiment categories:

| Label ID | Sentiment | Description                                                                  |
| -------- | --------- | ---------------------------------------------------------------------------- |
| 0        | Negative  | Slow service, unfriendly staff, or complaints about service quality.         |
| 1        | Neutral   | General mentions of service without specific positive or negative sentiment. |
| 2        | Positive  | Fast service, friendly staff, or praise for service quality.                 |

## Evaluation Metrics

Based on the fine-tuning results, the model achieves an overall accuracy of **88%**.

### Classification Report

| Category         | Precision | Recall |  F1-Score  | Support  |
| :--------------- | :-------: | :----: | :--------: | :------: |
| **Negative**     |  0.9006   | 0.9548 |   0.9269   |   332    |
| **Neutral**      |  0.8512   | 0.8195 |   0.8350   |   349    |
| **Positive**     |  0.8830   | 0.8653 |   0.8741   |   349    |
| **Accuracy**     |           |        | **0.8786** | **1030** |
| **Macro Avg**    |  0.8783   | 0.8799 |   0.8787   |   1030   |
| **Weighted Avg** |  0.8779   | 0.8786 |   0.8779   |   1030   |

## Usage

This model is loaded and used by the ABSA API service. All aspect models share a single tokenizer for optimal performance.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_path = "./absa-fnb-model/model_service"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained("indobenchmark/indobert-base-p2")
```
