---
language:
- en

license: mit

pipeline_tag: text-classification

tags:
- sentiment-analysis
- youtube-comments
- nlp
- transformers
- roberta
- social-media
- text-classification
- youtube
- fastapi
- huggingface

library_name: transformers

base_model: cardiffnlp/twitter-roberta-base-sentiment-latest

metrics:
- accuracy
- f1

model-index:
- name: YouTube Comment Sentiment Analyzer
  results:
  - task:
      type: text-classification
      name: Sentiment Classification
    dataset:
      name: External YouTube Comment Validation Benchmark
      type: custom
    metrics:
    - type: accuracy
      value: 0.8800
      name: Accuracy
    - type: f1
      value: 0.8768
      name: Macro F1
---

# 🎬 YouTube Comment Sentiment Analyzer

<div align="center">

### Fine-Tuned Twitter-RoBERTa for Real-World YouTube Comments

[![Transformers](https://img.shields.io/badge/🤗_Transformers-RoBERTa-yellow)]()
[![Task](https://img.shields.io/badge/Task-Sentiment%20Analysis-blue)]()
[![Classes](https://img.shields.io/badge/Classes-3-green)]()
[![Language](https://img.shields.io/badge/Language-English-red)]()

---

### 🎯 Real-World Performance

| Metric | Score |
|----------|----------|
| Accuracy | **88.00%** |
| Macro F1 | **87.68%** |
| Weighted F1 | **87.73%** |

**Evaluated on a custom real-world YouTube benchmark containing slang, emojis, internet culture references, and creator-style comments.**

</div>

---

# 🚀 Overview

This model is a sentiment classifier specifically adapted for **YouTube comments**.

The backbone model, **Twitter-RoBERTa**, was originally trained on Twitter/X posts and social media text.

To make it understand YouTube comment culture, the model was further fine-tuned on a dataset containing **1 Million+ labeled YouTube comments**.

The result is a model that better understands:

✅ Emojis

✅ Internet slang

✅ Creator-audience interactions

✅ Short-form comments

✅ Social media language

✅ YouTube culture

---

# 🧠 Model Architecture

```text
Twitter/X Posts
        ↓
Twitter-RoBERTa
(cardiffnlp/twitter-roberta-base-sentiment-latest)
        ↓
Fine-Tuning on 1M+ YouTube Comments
        ↓
YouTube Comment Sentiment Analyzer
        ↓
Negative | Neutral | Positive
```

---

# 📊 Project Pipeline

![Pipeline](./pipeline.png)

---

# 🎯 Sentiment Classes

| Label | Meaning |
|---------|---------|
| 🔴 Negative | Criticism, dislike, frustration, complaints |
| ⚪ Neutral | Informational, factual, objective comments |
| 🟢 Positive | Praise, appreciation, excitement, support |

---

# 🧪 Real-World Benchmark Results

A manually curated benchmark was created to simulate actual YouTube comments.

The benchmark includes:

- Internet slang
- Emoji-heavy comments
- Creator terminology
- Sarcasm
- Mixed sentiment
- Short comments
- Viral internet phrases

## Results

| Metric | Score |
|----------|----------|
| Accuracy | **88.00%** |
| Macro F1 | **87.68%** |
| Weighted F1 | **87.73%** |

---


# 📉 Normalized Confusion Matrix

The model performs consistently across all sentiment classes and shows balanced classification behavior. Most classification errors occur between Neutral and Positive comments.

Negative comments are generally identified more reliably.

![Normalized Confusion Matrix](./normalized_confusion_matrix.png)

---

# 🏋️ Training Details

### Base Model

```text
cardiffnlp/twitter-roberta-base-sentiment-latest
```

### Fine-Tuning Dataset

```text
1M+ YouTube Comments
```

### Hardware

```text
NVIDIA RTX 3050 Laptop GPU (6GB)
```

### Training Features

- Mixed Precision Training (AMP)
- Layer-wise Learning Rate Decay (LLRD)
- Gradient Accumulation
- Cosine Learning Rate Scheduler
- Warmup Scheduling
- Gradient Checkpointing
- Class Weighted Loss
- Early Stopping
- Resume Training Support
- Dynamic GPU Configuration

---

# 📋 Internal Test Set Results

For reference, the held-out test split produced:

| Metric | Score |
|----------|----------|
| Accuracy | 77.43% |
| Macro F1 | 77.38% |
| Weighted F1 | 77.41% |

The external benchmark is considered a better estimate of real-world deployment performance.

---

# 🔥 Example Predictions

### Positive

```text
W video bro 🔥
```

Prediction:

```text
Positive
```

---

### Positive

```text
Absolute cinema
```

Prediction:

```text
Positive
```

---

### Negative

```text
nah this ain't it
```

Prediction:

```text
Negative
```

---

### Negative

```text
Worst update ever
```

Prediction:

```text
Negative
```

---

### Neutral

```text
Uploaded 2 hours ago
```

Prediction:

```text
Neutral
```

---

# 💻 Usage

```python
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

MODEL_ID = "rishigupta04/yt-comments-sentiment-analyzer"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_ID
)
```

---

# 🎯 Intended Use Cases

### Suitable For

- YouTube Comment Analysis
- Social Media Monitoring
- Creator Analytics
- Content Moderation Assistance
- Brand Sentiment Tracking
- NLP Education
- Research Projects

### Not Intended For

- Medical Decisions
- Legal Decisions
- Financial Decisions
- High-Risk Automated Systems

---

# ⚠️ Known Limitations

Like most sentiment models, performance may degrade on:

- Heavy sarcasm
- Irony
- Context-dependent jokes
- Multi-comment conversations
- Ambiguous sentiment

Example:

```text
Wow another genius from YouTube University
```

May require additional context to classify correctly.

---

# 🛠️ Project Stack

```text
Python
Transformers
PyTorch
FastAPI
Hugging Face
Scikit-Learn
Pandas
NumPy
```

---

# 👨‍💻 Author

## Rishiraj Gupta

**M.Sc. Data Science**

This project demonstrates:

- End-to-End NLP Pipeline
- Transformer Fine-Tuning
- Model Evaluation
- Error Analysis
- MLOps Practices
- FastAPI Deployment
- Hugging Face Deployment
- Real-World Sentiment Analysis

---

<div align="center">

### ⭐ If you find this model useful, please consider liking the repository.

Built with 🤗 Transformers + PyTorch

</div>