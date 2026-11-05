---
language: en
tags:
- text-classification
- emotion-detection
- distilbert
- pytorch
---

# SMILE Text Classifier

This model is fine-tuned on the SMILE dataset for emotion classification.

## Labels
- angry
- disgust
- happy
- not-relevant
- sad
- surprise

## Base model
- distilbert-base-uncased

## Training
- Epochs: 3
- Batch size: 16
- Optimizer: AdamW
- Learning rate: 2e-5
