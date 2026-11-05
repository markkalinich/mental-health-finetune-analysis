---
language:
- ru
license: apache-2.0
base_model: ai-forever/ruBert-base
tags:
- sentiment-analysis
- text-classification
- russian
- bert
datasets:
- angryelizar/sentiment_dataset_splitted
metrics:
- accuracy
pipeline_tag: text-classification
model-index:
- name: ru-review-sentiment-classifier
  results:
  - task:
      type: text-classification
      name: Sentiment Classification
    dataset:
      name: angryelizar/sentiment_dataset_splitted
      type: angryelizar/sentiment_dataset_splitted
    metrics:
    - type: accuracy
      value: 0.77
      name: Accuracy
---

# Russian Review Sentiment Classifier

A model for classifying the sentiment of Russian-language user reviews (positive / negative / neutral), fine-tuned from [ai-forever/ruBert-base](https://huggingface.co/ai-forever/ruBert-base).

## Model Description

- **Base model:** [ai-forever/ruBert-base](https://huggingface.co/ai-forever/ruBert-base)
- **Task:** sentiment analysis / text classification
- **Language:** Russian
- **Dataset:** [angryelizar/sentiment_dataset_splitted](https://huggingface.co/datasets/angryelizar/sentiment_dataset_splitted)
- **Training epochs:** 1

## Metrics

| Metric    | Value |
|-----------|-------|
| Accuracy  | 77%   |

![Test results](./test_results.png)


## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "angryelizar/ruBert-base-sentiment-classifier-final"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Классный сервис - мне нравится!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = torch.argmax(logits, dim=-1).item()
print(model.config.id2label[predicted_class_id])
```

An interactive UI for trying out the model is also available — see the [Links](#links) section below.

## Training Data

The model was trained on the [angryelizar/sentiment_dataset_splitted](https://huggingface.co/datasets/angryelizar/sentiment_dataset_splitted) dataset.

## Links

- 📊 Dataset: https://huggingface.co/datasets/angryelizar/sentiment_dataset_splitted
- 🧠 Base model: https://huggingface.co/ai-forever/ruBert-base
- 🔧 Fine-tuning code: https://github.com/angryelizar/review-classifier-finetune
- ✅ Testing code: https://github.com/angryelizar/review-classifier-tester
- 🖥️ Interactive UI: https://github.com/angryelizar/ru-review-classifier-app

## Project Context

This model is part of Capstone #1: *Text Classifier on PyTorch & BERT* (Attractor School, 2026).

## Limitations

- The model was trained on a mixed-domain review dataset (marketplaces, movies, anime, geolocation reviews, etc.), so accuracy may differ on narrower, more specialized domains.
- The model was fine-tuned for only 1 epoch — accuracy could potentially be higher with additional training epochs.