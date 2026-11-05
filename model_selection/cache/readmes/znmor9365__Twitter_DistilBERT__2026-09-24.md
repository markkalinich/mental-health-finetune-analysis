---
language:
- en
base_model:
- distilbert/distilbert-base-uncased
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
library_name: transformers
pipeline_tag: text-classification
tags:
- distilbert
- emotion-classification
- twitter
- text-classification
- pytorch
widget:
- text: "I feel so happy and excited today!"
- text: "I am terrified that something bad will happen."
- text: "I really miss the people I love."
model-index:
- name: DistilBERT Twitter Emotion Classifier
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      type: dair-ai/emotion
      name: Emotion
      split: test
    metrics:
    - type: accuracy
      value: 0.929
      name: Test Accuracy
    - type: f1
      value: 0.929073
      name: Test Weighted F1
---

# DistilBERT Twitter Emotion Classifier

This model is a fine-tuned version of
[`distilbert-base-uncased`](https://huggingface.co/distilbert/distilbert-base-uncased)
for six-class English Twitter emotion classification.