---
language: en
license: apache-2.0
tags:
- mental-health
- multilabel-classification
- bert
- text-classification
- psychology
pipeline_tag: text-classification
---

# MentalBERT Multi-label Mental Health Classifier

This model is a fine-tuned version of `mental/mental-bert-base-uncased`
for multi-label mental health risk detection.

## Labels
- Depression
- Anxiety
- Suicide Risk

## Training
- Multi-label classification
- Focal Loss + LLRD
- Max sequence length: 512

## Test Metrics
- Micro F1: 0.806
- Macro F1: 0.786
- Subset Accuracy: 0.707
- Hamming Accuracy: 0.87
