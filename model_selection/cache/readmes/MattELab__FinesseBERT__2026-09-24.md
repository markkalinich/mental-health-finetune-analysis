---
license: cc-by-2.0
language:
  - en
base_model:
  - distilbert/distilbert-base-uncased
tags:
  - text-classification
  - finance
  - sentiment-analysis
  - distilbert
pipeline_tag: text-classification
---

# FinesseBERT

FinesseBERT is a fine-tuned sequence classification model based on DistilBERT, built to predict the **sentiment of stock market and crypto news articles** from the headline and metadata alone — no full article body required. Built by **[SentientMerchant](https://sentientmerchant.com/)**, a platform exploring AI-driven tools for financial intelligence.

## Purpose

Given the high volume and velocity of financial news, FinesseBERT enables fast, scalable sentiment analysis at the point of discovery — making it well-suited for real-time trading signals, news aggregators, and financial dashboards.

The model classifies inputs into three sentiment categories:
- `Positive-Outlook-On-Stock-News`
- `Neutral-Outlook-On-Stock-News`
- `Negative-Outlook-On-Stock-News`

## Attribution Requirement

This model is licensed under CC-BY. If you use this model in your research, application, or product, you must provide attribution by linking back to **[sentientmerchant.com](https://sentientmerchant.com/)**.

## Training Data

FinesseBERT was fine-tuned on a dataset of **2,900 labeled stock news examples**. Each example was structured as a single concatenated string capturing four fields sourced from financial news articles:

```json
{
    "reference": "https://finance.yahoo.com/...",
    "text": "security: LULULEMON ATHLETICA INC (LULU); title: Lululemon (LULU) Dips More Than Broader Market: What You Should Know; description: In the closing of the recent trading day, Lululemon (LULU) stood at $138.16, denoting a -2.97% move from the preceding trading day.; author: yahoo.com",
    "labels": 2
}
```

| Field | Description |
|---|---|
| `security` | The full company name and ticker symbol |
| `title` | The article headline |
| `description` | A short article summary or lede sentence |
| `author` | The publishing source |

The `labels` field maps to: `0` → Positive, `1` → Neutral, `2` → Negative.

## Optimal Inference Format

To get the best results from FinesseBERT, structure your input text to **mirror the training data format** exactly — a semicolon-delimited string with the four named fields in the same order:

```
security: <COMPANY NAME> (<TICKER>); title: <HEADLINE>; description: <DESCRIPTION>; author: <SOURCE>
```

**Example:**
```
security: LULULEMON ATHLETICA INC (LULU); title: Lululemon (LULU) Dips More Than Broader Market: What You Should Know; description: In the closing of the recent trading day, Lululemon (LULU) stood at $138.16, denoting a -2.97% move from the preceding trading day.; author: yahoo.com
```

Deviating from this format — such as passing a raw headline string alone — may degrade classification accuracy, as the model learned the sentiment signal from the full structured context it was trained on.

## How to Use

You can load and use this model directly from the Hugging Face Hub using the `transformers` library.

### 1. Install Dependencies

Make sure you have the required libraries installed:

```bash
pip install transformers torch
```

### 2. Loading the Model

Use the `Auto` classes to load the model and tokenizer directly from the Hugging Face Hub.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "MattELab/FinesseBERT"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
```

### 3. Running Inference

Here is a quick example of how to pass text through the model to get predictions.

```python
# 1. Define your input text (see Optimal Inference Format above)
text = "security: LULULEMON ATHLETICA INC (LULU); title: Lululemon (LULU) Dips More Than Broader Market: What You Should Know; description: In the closing of the recent trading day, Lululemon (LULU) stood at $138.16, denoting a -2.97% move from the preceding trading day.; author: yahoo.com"

# 2. Tokenize the input
# Note: DistilBERT has a maximum input length of 512 tokens. Inputs longer than
# this will be silently truncated, which may degrade prediction quality.
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)

# 3. Run the model (using torch.no_grad() for faster, memory-efficient inference)
with torch.no_grad():
    outputs = model(**inputs)

# 4. Convert logits to probabilities
probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)

# 5. Get the predicted class
predicted_class = torch.argmax(probabilities, dim=-1).item()

# 6. Map the predicted class ID to a human-readable label
label_map = {0: "Positive-Outlook-On-Stock-News", 1: "Neutral-Outlook-On-Stock-News", 2: "Negative-Outlook-On-Stock-News"}

print(f"Probabilities: {probabilities}")
print(f"Predicted Class ID: {predicted_class}")
print(f"Predicted Sentiment: {label_map[predicted_class]}")
```

## Model Details

* **Architecture:** DistilBERT (`AutoModelForSequenceClassification`)
* **Task:** Text Classification
* **Classes:** 3 (`Positive-Outlook-On-Stock-News`, `Neutral-Outlook-On-Stock-News`, `Negative-Outlook-On-Stock-News`)
* **Creator:** MattELab

## About SentientMerchant

SentientMerchant provides real-time stock, crypto, and international market data to keep you up-to-date. Find top news headlines, individual and overall news sentiment across various timelines, build a watchlist, buy US & SG stocks, and create and manage your portfolio.