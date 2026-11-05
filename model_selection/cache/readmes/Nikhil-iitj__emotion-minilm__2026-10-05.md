---
tags:
- text-classification
- emotion
- minilm
- distillation
language:
- en
license: mit
metrics:
- accuracy
- f1
base_model: microsoft/MiniLM-L12-H384-uncased
---

# Emotion Classification - MiniLM (v1)

This is the **v1 model** for our MLOps Group Project (Group 2, IIT Jodhpur).

## Model Details
- **Architecture:** microsoft/MiniLM-L12-H384-uncased
- **Task:** Text emotion classification (6 classes)
- **Dataset:** dair-ai/emotion
- **Classes:** sadness, joy, love, anger, fear, surprise

## Training
- **Platform:** Kaggle GPU T4
- **Epochs:** 3
- **Batch size:** 16
- **Learning rate:** 3e-5
- **Test Accuracy:** 90.7%
- **Test F1:** 90.7%

## Links
- **GitHub Repo:** https://github.com/nikhilsaini-iitj/MLOps_GroupProject
- **Kaggle Notebook:** https://www.kaggle.com/code/nikhilg25ait2067/kaggle-minilm
- **W&B Dashboard:** https://wandb.ai/g25ait2067-prom-iit-rajasthan/mlops-groupproject-v2
- **Winning Model (v2):** https://huggingface.co/Nikhil-iitj/emotion-electra

## Team
- Nikhil Saini (G25AIT2067)
- Y Sharathchandrika (G25AIT2132)
- Sarthak Kapoor (G25AIT2098)
- Aryaveer Rathi (G25AIT2021)
