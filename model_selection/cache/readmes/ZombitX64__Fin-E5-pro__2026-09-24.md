
---
license: apache-2.0
datasets:
- financial-sentiment
language:
- en
- th
metrics:
- accuracy
base_model: intfloat/multilingual-e5-large-instruct
tags:
- sentiment-analysis
- financial-sentiment
- multilingual
- transformer
- fine-tuned
- 1.0.0
pipeline_tag: text-classification
widget:
- text: "$AAPL - Apple iPhone sales decline in key Chinese market"
- text: "$GULF - กัลฟ์ เอนเนอร์จี้ได้รับสัญญาโครงการพลังงานหมุนเวียนใหม่มูลค่า 50,000 ล้าน"
library_name: transformers
---

# Fin-E5-pro Financial Sentiment Analysis Model

This is a fine-tuned sentiment analysis model based on `intfloat/multilingual-e5-large-instruct` for financial text, supporting both English and Thai languages.

## Model Details

- **Base Model:** `intfloat/multilingual-e5-large-instruct`
- **Fine-tuning Dataset:** A custom dataset containing financial news headlines and tweets in English and Thai, labeled with sentiment (No Impact, Bullish, Bearish). The dataset was created by combining `financial-sentiment.jsonl` and `validation.jsonl`.
- **Task:** Sentiment Classification
- **Labels:**
    - 0: No Impact
    - 1: Bullish
    - 2: Bearish

## Training

The model was fine-tuned using the Hugging Face Transformers library.

- **Optimizer:** AdamW
- **Learning Rate:** 2e-5
- **Epochs:** 3
- **Batch Size:** 18
- **Evaluation Strategy:** Evaluated at the end of each epoch.
- **Saving Strategy:** Model checkpoints saved at the end of each epoch.
- **Metric for Best Model:** Accuracy

## Evaluation Results

The model was evaluated on a custom financial sentiment dataset for comparison with other models.


| Model                     |   Accuracy |   Negative F1 |   Neutral F1 |   Positive F1 |
|:--------------------------|-----------:|--------------:|-------------:|--------------:|
| ModernFinBERT             |     0.0000 |        0.0000 |       0.0000 |        0.0000 |
| FinBERT                   |     0.6000 |        1.0000 |       0.0000 |        0.5000 |
| tabularisai/ModernFinBERT |     0.8000 |        1.0000 |       0.0000 |        0.8000 |

## Usage

You can use this model with the Hugging Face Transformers library:
