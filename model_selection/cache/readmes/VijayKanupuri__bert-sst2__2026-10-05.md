---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- bert
- fine-tuning
datasets:
- glue
- sst2
metrics:
- accuracy
---

# BERT Fine-tuned on SST-2

## Model Description

This model is a **BERT-base (bert-base-uncased)** model fine-tuned on the **SST-2 (Stanford Sentiment Treebank)** dataset for **binary sentiment classification**.

The model predicts whether a given English sentence expresses **positive** or **negative** sentiment.

This model was fine-tuned as part of a learning-focused, production-style workflow:
- training on GPU (Google Colab)
- exporting model artifacts
- running inference locally

---

## Intended Use

### Supported Use Cases
- Sentiment analysis of short English sentences
- Educational and learning purposes
- Benchmarking text classification pipelines
- Prototyping NLP applications

### Out-of-Scope Uses
- Long documents without chunking
- Multilingual sentiment analysis
- High-stakes decision making (legal, medical, financial)

---

## Training Data

- **Dataset:** SST-2 (Stanford Sentiment Treebank)
- **Source:** GLUE benchmark
- **Task:** Binary sentiment classification
- **Labels:**
  - `0` → Negative
  - `1` → Positive

SST-2 consists of movie review sentences annotated for sentiment polarity.

---

## Training Details

- **Base Model:** bert-base-uncased
- **Architecture:** Encoder-only Transformer (BERT)
- **Number of Labels:** 2
- **Loss Function:** Cross-Entropy Loss
- **Optimizer:** AdamW
- **Learning Rate:** 2e-5
- **Batch Size:** 32 (GPU)
- **Epochs:** 2
- **Precision:** Mixed precision (fp16)
- **Training Hardware:** NVIDIA GPU (Google Colab)

---

## Evaluation

The model was evaluated on the SST-2 validation set.

Expected performance is consistent with standard BERT fine-tuning on SST-2:
- **Accuracy:** ~90% (depending on training seed and subset)

This model is intended primarily for learning and demonstration rather than leaderboard optimization.

---

## How to Use

### Inference Example

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained("VijayKanupuri/bert-sst2")
model = BertForSequenceClassification.from_pretrained("VijayKanupuri/bert-sst2")

text = "I really loved this movie"

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)

label = torch.argmax(probs, dim=-1).item()
confidence = probs[0][label].item()

print(label, confidence)
