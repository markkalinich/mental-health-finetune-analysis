---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
  - text-classification
  - emotion
  - distilbert
  - transformers
  - fine-tuned
datasets:
  - dair-ai/emotion
language:
  - en
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
model-index:
  - name: distilbert-emotion-model-v2
    results:
      - task:
          type: text-classification
          name: Emotion Classification
        dataset:
          name: dair-ai/emotion
          type: dair-ai/emotion
        metrics:
          - type: accuracy
            value: 0.9370
            name: Test Accuracy
          - type: f1
            value: 0.9380
            name: Test F1 (weighted)
---

# DistilBERT Fine-Tuned for Emotion Classification

A **DistilBERT-base-uncased** model fine-tuned on the [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset for **6-class emotion classification**.

## Model Description

This model classifies English text into one of six emotions:

| Label | Emotion |
|:-----:|:--------|
| 0 | sadness 😢 |
| 1 | joy 😄 |
| 2 | love ❤️ |
| 3 | anger 😠 |
| 4 | fear 😨 |
| 5 | surprise 😲 |

## Training Results

### Best Results (Optimized)

| Metric | Score |
|:-------|:------|
| **Test Accuracy** | **93.70%** |
| **Test F1 Score (weighted)** | **93.80%** |

### Baseline Results

| Metric | Score |
|:-------|:------|
| Test Accuracy | 93.55% |
| Test F1 Score (weighted) | 93.61% |

### Training History (Best Run)

| Epoch | Training Loss | Validation Loss | Accuracy | F1 |
|:-----:|:-------------:|:---------------:|:--------:|:------:|
| 1 | 0.928500 | 0.239526 | 0.9105 | 0.9104 |
| 2 | 0.188200 | 0.160186 | 0.9300 | 0.9300 |
| 3 | 0.114900 | 0.142201 | 0.9335 | 0.9349 |
| 4 | 0.089700 | 0.147365 | 0.9400 | 0.9405 |
| 5 | 0.067800 | 0.159507 | 0.9330 | 0.9342 |
| 6 | 0.045800 | 0.216059 | 0.9345 | 0.9350 |
| 7 | 0.029500 | 0.232973 | 0.9340 | 0.9339 |

> Best model was selected at **Epoch 4** based on the highest validation F1 score (0.9405). Early stopping triggered after patience of 3 epochs.

## Training Hyperparameters

| Parameter | Value |
|:----------|:------|
| Base Model | `distilbert-base-uncased` |
| Batch Size | 64 |
| Learning Rate | 5e-5 |
| Weight Decay | 0.02 |
| LR Scheduler | Cosine |
| Warmup Ratio | 0.1 |
| Max Epochs | 10 |
| Early Stopping Patience | 3 |
| FP16 | Enabled (on GPU) |
| Metric for Best Model | F1 (weighted) |
| Optimizer | AdamW |

## Dataset

The model was trained on the [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset with a **stratified 80/10/10 split** to ensure balanced class representation across train, validation, and test sets.

| Split | Samples | Percentage |
|:------|:-------:|:----------:|
| Train | ~16,000 | 80% |
| Validation | ~2,000 | 10% |
| Test | ~2,000 | 10% |

## Usage

### Using Pipeline (Recommended)

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="OmarMaqousi/distilbert-emotion-model-v2",
    return_all_scores=True,
)

result = classifier("I am so happy today!")
print(result)
```

### Using Model Directly

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "OmarMaqousi/distilbert-emotion-model-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I am so happy today!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

labels = ["sadness", "joy", "love", "anger", "fear", "surprise"]
for label, score in zip(labels, predictions[0]):
    print(f"{label}: {score:.4f}")
```

## Framework Versions

- Transformers: 4.44.2
- PyTorch: 2.x
- Datasets: latest
- Python: 3.12

## Limitations

- The model is trained on English text only.
- Performance may vary on text that is very different from the training data (e.g., formal writing, slang, or domain-specific language).
- The model may struggle to distinguish between semantically similar emotions (e.g., sadness vs. fear).
