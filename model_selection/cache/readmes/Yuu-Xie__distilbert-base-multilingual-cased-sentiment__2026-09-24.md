---
language:
- multilingual
- en
- zh
- ja
- ko
- ar
- ru
- fr
- de
- es
- pt
- hi
- id
- it
- ms
- tr
- vi
license: apache-2.0
base_model: distilbert-base-multilingual-cased
tags:
- multilingual
- distilbert
- sentiment
- emotion
- text-classification
datasets:
- clapAI/MultiLingualSentiment
metrics:
- f1
- accuracy
pipeline_tag: text-classification
---

[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow)](https://huggingface.co/Yuu-Xie/distilbert-base-multilingual-cased-sentiment)
[![GitHub Stars](https://img.shields.io/github/stars/Yuu-Xie/distilbert-base-multilingual-cased-sentiment?style=social)](https://github.com/Yuu-Xie/distilbert-base-multilingual-cased-sentiment)
[![GitHub Forks](https://img.shields.io/github/forks/Yuu-Xie/distilbert-base-multilingual-cased-sentiment?style=social)](https://github.com/Yuu-Xie/distilbert-base-multilingual-cased-sentiment)
[![GitHub Watchers](https://img.shields.io/github/watchers/Yuu-Xie/distilbert-base-multilingual-cased-sentiment?style=social)](https://github.com/Yuu-Xie/distilbert-base-multilingual-cased-sentiment)
[![GitHub License](https://img.shields.io/github/license/Yuu-Xie/distilbert-base-multilingual-cased-sentiment)](https://github.com/Yuu-Xie/distilbert-base-multilingual-cased-sentiment)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Yuu-Xie/distilbert-base-multilingual-cased-sentiment)](https://github.com/Yuu-Xie/distilbert-base-multilingual-cased-sentiment)

# Model Card for Model ID

## Model Details

### Model Description

This model is a fine-tuned version of `distilbert-base-multilingual-cased` on the `clapAI/MultiLingualSentiment` dataset (approx. 3.15 million samples). It is designed to provide a **high-throughput, low-latency** sentiment analysis baseline for multilingual environments.

The model supports three-class classification: **Positive**, **Neutral**, and **Negative**.

- **Developed by:** Yuu-Xie
- **Model type:** Transformer-based text classification (DistilBERT)
- **Language(s) (NLP):** Multilingual
- **License:** Apache-2.0
- **Finetuned from model:** distilbert-base-multilingual-cased

## Uses

### Direct Use

This model can be directly used for social media comment analysis, product review monitoring, and multilingual public opinion tracking. It is particularly suitable for deployment scenarios with high real-time requirements or limited computing resources.

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline(
    task="text-classification", 
    model="Yuu-Xie/distilbert-base-multilingual-cased-sentiment"
)

texts = [
    "A good environment with good food. Price is reasonable.",
    "这个产品质量很一般，不建议购买。",
    "コードレス設計で車内の掃除もできます。"
]

predictions = classifier(texts)
print(predictions)
```

## Training Details

### Training Data

The training set is sourced from [clapAI/MultiLingualSentiment](https://huggingface.co/datasets/clapAI/MultiLingualSentiment), containing roughly 3.15 million labeled multilingual text samples.

### Training Procedure

#### Training Hyperparameters

- **Training regime:** bf16 mixed precision
- **Batch Size:** 128 (Train), 256 (Eval)
- **Max Steps:** 62,500
- **Learning Rate:** 2e-5 (warm-up)

#### Speeds, Sizes, Times

- **Hardware:** NVIDIA A10 (24GB)
- **Training Time:** 3 hours 41 minutes
- **Throughput:** ~6.5 it/s (Training)
- **Model Size:** 519 MiB (134M parameters)

## Evaluation

## Results

Final evaluation results on **393,436** independent test samples:

| **Metric**          | **Score** |
| ------------------- | --------- |
| **Accuracy**        | 0.7989    |
| **Macro Avg F1**    | 0.7891    |
| **Weighted Avg F1** | 0.7988    |

#### Classification Report

| **Class**    | **Precision** | **Recall** | **F1-score** |
| ------------ | ------------- | ---------- | ------------ |
| **Positive** | 0.8500        | 0.8386     | 0.8443       |
| **Negative** | 0.8183        | 0.8359     | 0.8270       |
| **Neutral**  | 0.7001        | 0.6923     | 0.6961       |

## Citation

```bibtex
@misc{yuu-xie2026distilbert-sentiment,
  author = {Yuu-Xie},
  title = {DistilBERT-base-multilingual-cased-sentiment},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Yuu-Xie/distilbert-base-multilingual-cased-sentiment}}
}
```