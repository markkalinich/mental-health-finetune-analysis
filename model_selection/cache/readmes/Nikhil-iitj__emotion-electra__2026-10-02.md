---
tags:
- text-classification
- emotion
- electra
- replaced-token-detection
language:
- en
license: mit
metrics:
- accuracy
- f1
base_model: google/electra-small-discriminator
---

# Emotion Classification - ELECTRA-small (v2) - WINNING MODEL

This is the **winning v2 model** for our MLOps Group Project (Group 2, IIT Jodhpur).

## Model Details
- **Architecture:** google/electra-small-discriminator
- **Task:** Text emotion classification (6 classes)
- **Dataset:** dair-ai/emotion
- **Classes:** sadness, joy, love, anger, fear, surprise

## Training
- **Platform:** Kaggle GPU T4
- **Epochs:** 4
- **Batch size:** 16
- **Learning rate:** 5e-5
- **Test Accuracy:** 92.65%
- **Test F1:** 92.69%
- **Model Size:** 54.2 MB

## Why This Won
Higher accuracy, lower loss, **2.5× smaller** than v1 (MiniLM), and faster inference. The RTD pretraining objective produces more efficient representations.

## Links
- **GitHub Repo:** https://github.com/nikhilsaini-iitj/MLOps_GroupProject
- **Kaggle Notebook:** https://www.kaggle.com/code/nikhilg25ait2067/kaggle-electra
- **W&B Dashboard:** https://wandb.ai/g25ait2067-prom-iit-rajasthan/mlops-groupproject-v2
- **Docker Image:** https://hub.docker.com/r/nikhilsainiiitj/mlops-groupproject-inference

## Team
- Nikhil Saini (G25AIT2067)
- Y Sharathchandrika (G25AIT2132)
- Sarthak Kapoor (G25AIT2098)
- Aryaveer Rathi (G25AIT2021)
