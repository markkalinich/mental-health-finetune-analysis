---
language:
- en
license: apache-2.0
tags:
- text-classification
- the-founder
- emotion
- 6-class
datasets:
- dair-ai/emotion
metrics:
- accuracy
base_model: FacebookAI/roberta-base
pipeline_tag: text-classification
model-index:
- name: founder-roberta-emotion-v1
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: Emotion
      type: dair-ai/emotion
      split: validation
    metrics:
    - type: accuracy
      value: 0.9395
      name: Accuracy
    - type: loss
      value: 0.2680
      name: Eval Loss
---

# founder-roberta-emotion-v1

Fine-tuned by **The Founder** — an autonomous ML orchestration superagent.

## Model Description

This is a fine-tuned version of `roberta-base` on the `dair-ai/emotion` dataset for Emotion Classification.

Training was orchestrated end-to-end by **The Founder** — a personal ML agent that handles research, compute scheduling, experiment tracking, and artifact management autonomously using Kaggle (Tesla T4), Weights & Biases, and HuggingFace Hub.

## Model Details

| Property | Value |
|---|---|
| Base model | roberta-base |
| Fine-tuned on | dair-ai/emotion |
| Task | Emotion Classification |
| Epochs | 4 |
| Batch size | 32 |
| Learning rate | 2e-05 |
| GPU | Tesla T4 (Kaggle) |
| Train loss | 0.2018 |
| Eval loss | 0.2680 |
| Eval accuracy | 0.9395 |
| Duration | 21.3 min |

## How to Get Started

```python
from transformers import pipeline
clf = pipeline("text-classification", model="zanesmit29/founder-roberta-emotion-v1")
clf("Your input text here")
```

## Uses

### Direct Use
This model is suitable for Emotion Classification tasks in English. It can be used out-of-the-box with the Transformers pipeline API.

### Out-of-Scope Use
This model was trained on a specific dataset and may not generalise to all domains or languages.
It should not be used to make high-stakes automated decisions without human review.
Performance on out-of-distribution data (e.g. non-English text, domain-specific jargon) is not guaranteed.

## Training Details

### Data
Trained on `dair-ai/emotion` — 4 epochs, no additional preprocessing beyond standard tokenization.

### Hyperparameters

| Hyperparameter | Value |
|---|---|
| Learning rate | 2e-05 |
| Batch size | 32 |
| Epochs | 4 |
| Optimizer | AdamW |
| LR scheduler | Linear with warmup |
| Max sequence length | 128 |
| fp16 | true |

## Results

| Metric | Value |
|---|---|
| Train loss | 0.2018 |
| Eval loss | 0.2680 |
| Eval accuracy | 0.9395 |
| Duration | 21.3 min |

## Experiment Tracking

[W&B Run](https://wandb.ai/zane-ml/the-founder/runs/32nqzsks)

## Infrastructure

| Component | Tool |
|---|---|
| Compute | Kaggle (Tesla T4) |
| Experiment tracking | Weights & Biases |
| Artifact storage | HuggingFace Hub |
| Orchestration | The Founder |
