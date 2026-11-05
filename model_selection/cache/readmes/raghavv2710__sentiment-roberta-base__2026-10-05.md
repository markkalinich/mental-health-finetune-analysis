---
license: apache-2.0
language:
  - en
metrics:
  - accuracy
  - f1
  - precision
  - recall
base_model: FacebookAI/roberta-base
pipeline_tag: text-classification
library_name: transformers
tags:
  - roberta
  - sentiment-analysis
  - transformers
  - text-classification
  - custom-dataset
eval_results:
  eval_accuracy: 0.91
  eval_f1: 0.90
  eval_precision: 0.92
  eval_recall: 0.89
---

# 🚀 Sentiment-RoBERTa-Base

A fine-tuned [RoBERTa-base](https://huggingface.co/roberta-base) model for **binary sentiment classification** (positive/negative).  
Trained on a custom dataset across multiple sources including tweets, social comments, and headlines to handle **real-world tone detection**.

✅ Use this model to build sentiment-aware applications, feedback classifiers, social media monitoring tools, or LLM content filters.

## 🧠 Model Details

| Property              | Value                     |
|-----------------------|---------------------------|
| Base Model            | `roberta-base`            |
| Fine-tuned Tasks      | Binary Sentiment Analysis |
| Classes               | `0 = Negative`, `1 = Positive` |
| Language              | English (`en`)            |
| Dataset               | Custom multi-source       |
| Framework             | 🤗 Transformers           |
| Model Size            | ~125M parameters          |

## 📊 Evaluation (on 20% held-out test set)

| Metric       | Score |
|--------------|-------|
| Accuracy     | 91%   |
| F1 Score     | 90%   |
| Precision    | 92%   |
| Recall       | 89%   |

## ⚙️ Quick Start

### 💡 Install Required Libraries

```bash
pip install transformers torch