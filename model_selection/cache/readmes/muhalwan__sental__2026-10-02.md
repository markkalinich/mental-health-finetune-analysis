---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- financial-sentiment-analysis
- finbert
- sentiment-analysis
- finance
- trading
- nlp
pipeline_tag: text-classification
metrics:
- accuracy
- f1
widget:
- text: "Apple reports record quarterly profit, crushes Wall Street expectations and announces massive dividend hike!"
  example_title: "Bullish Earnings"
- text: "Tesla plunges 12% as vehicle margins shrink and deliveries miss consensus estimates."
  example_title: "Bearish Delivery Miss"
- text: "Federal Reserve minutes show policymakers debated future interest rate path with no policy change."
  example_title: "Neutral Fed Minutes"
---

# Sental: High-Performance Financial Sentiment Analysis

**Sental** is a state-of-the-art financial sentiment classifier fine-tuned from `yiyanghkust/finbert-tone` on corporate filings, financial news, analyst notes, and market tweets.

## Model Performance

Evaluated on the official validation dataset (2,388 unseen samples):

| Metric | Score |
| :--- | :---: |
| **Accuracy** | **88.9%** (Ensemble) / **88.2%** (Standalone FinBERT) |
| **Macro F1** | **0.85** |
| **Weighted F1** | **0.89** |

### Per-Class Metrics

| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **Bearish** (2) | 0.87 | 0.73 | 0.79 | 347 |
| **Bullish** (1) | 0.88 | 0.78 | 0.83 | 475 |
| **Neutral** (0) | 0.89 | 0.96 | 0.93 | 1,566 |

## Label Mapping

The model outputs logits for 3 classes:
- `0`: **Neutral**
- `1`: **Bullish**
- `2`: **Bearish**

## Quickstart

### Using `transformers` pipeline

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="muhalwan/sental")
result = classifier("Apple reports record quarterly profit, crushes Wall Street expectations!")
print(result)
# [{'label': 'Bullish', 'score': 0.98}]
```

### Using PyTorch directly

```python
import torch
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained("muhalwan/sental")
model = BertForSequenceClassification.from_pretrained("muhalwan/sental")

text = "Tesla plunges 12% as vehicle margins shrink and deliveries miss forecast."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)

predicted_idx = outputs.logits.argmax(dim=-1).item()
label = model.config.id2label[predicted_idx]
print(f"Sentiment: {label} (Confidence: {probs[0][predicted_idx]:.2%})")
# Sentiment: Bearish (Confidence: 96.4%)
```

## Training Methodology

- **Base Architecture**: BERT-base uncased pre-trained on financial corpora (`yiyanghkust/finbert-tone`).
- **Precision**: Mixed Precision (`fp16`) with PyTorch AMP.
- **Optimization**: AdamW with linear warmup, cosine learning rate decay, and gradient clipping (1.0).
- **Preprocessing**: Semantics-preserving emoji demojization, handle/URL normalization, and dynamic token padding.