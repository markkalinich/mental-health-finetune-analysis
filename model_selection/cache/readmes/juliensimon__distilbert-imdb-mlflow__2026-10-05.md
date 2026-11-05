---
license: apache-2.0
tags:
- generated_from_trainer
- mlflow
- sentiment-analysis
datasets:
- imdb
base_model: distilbert/distilbert-base-cased
model-index:
- name: distilbert-imdb-mlflow
  results: []
---

# DistilBERT IMDB — MLflow Integration

A [DistilBERT](https://huggingface.co/distilbert-base-cased) model fine-tuned on the [IMDB](https://huggingface.co/datasets/imdb) dataset for sentiment analysis, with [MLflow](https://mlflow.org/) experiment tracking.

> **Video walkthrough**: [Log with MLflow and Hugging Face Transformers](https://youtube.com/watch?v=vmfaDZjeB4M)

## Model Details

| Detail | Value |
|--------|-------|
| **Base model** | [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) |
| **Task** | Binary sentiment classification |
| **Dataset** | [IMDB](https://huggingface.co/datasets/imdb) (50K movie reviews) |
| **License** | Apache 2.0 |

## Training Configuration

| Parameter | Value |
|-----------|-------|
| Learning rate | 5e-05 |
| Batch size | 8 (train & eval) |
| Optimizer | Adam (β₁=0.9, β₂=0.999, ε=1e-08) |
| LR scheduler | Linear |
| Epochs | 1 |

## Usage

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="juliensimon/distilbert-imdb-mlflow")
classifier("This movie was absolutely fantastic!")
```

## Viewing MLflow Logs

MLflow training logs are included in the repository. To view:

```bash
pip install mlflow
mlflow ui
```

## Framework Versions

- Transformers 4.20.1
- PyTorch 1.10.0
- Datasets 2.3.2
