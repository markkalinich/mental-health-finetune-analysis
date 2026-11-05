---
language: en
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- emotion
- distilbert
- pytorch
datasets:
- emotion
metrics:
- accuracy
- f1
widget:
- text: "i feel so grateful for everything that happened today"
- text: "i was terrified when the lights suddenly went out"
model-index:
- name: distilbert-base-uncased-finetuned-emotion
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
    metrics:
    - type: accuracy
      value: 0.932
    - type: f1
      value: 0.9328
---

# distilbert-base-uncased-finetuned-emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased)
on the [emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset. It classifies an English tweet into
one of six emotions: sadness, joy, love, anger, fear, surprise.

It was trained as a course assignment for an introductory AI course.

## Results

On the validation set:

- Accuracy: **0.932**
- Weighted F1: **0.9328**

## Training hyperparameters

- learning rate: 2e-5
- train batch size: 64
- optimizer: AdamW
- lr scheduler: linear with 10% warmup
- weight decay: 0.01
- epochs: 3 (best checkpoint kept by validation F1)

## How to use

```python
from transformers import pipeline

clf = pipeline("text-classification",
               model="ireallydk/distilbert-base-uncased-finetuned-emotion")
print(clf("i feel so happy today"))
```
