---
language: id
license: mit
tags:
- sentiment-analysis
- aspect-based-sentiment-analysis
- bert
- focal-loss
- pytorch
datasets:
- Reddit 
metrics:
- f1
base_model:
- google-bert/bert-base-uncased
---

# Aspect-Based Sentiment Analysis for Game Comments 

This is a BERT-based classifier for performing **aspect-based sentiment analysis (ABSA)** on user comments about video games.  
Each prediction considers both the **aspect** (topic/feature being discussed) and the **comment text** as inputs, and classifies the sentiment into 3 categories:
- **Negative**
- **Neutral**
- **Positive**

## 🔍 How the Model Works
The model input consists of two segments:
- **Aspect** (the topic whose sentiment you want to evaluate)
- **Comment Text** (the actual user comment)

These are separated by a `[SEP]` token according to the BERT input format.  
The model is trained using **Focal Loss** to handle class imbalance.

## 📊 Dataset
The dataset used for training consists of user comments on video games with the following columns:
- `comment_text`
- `aspect`
- `sentiment` (0 = Negative, 1 = Neutral, 2 = Positive)
- `Dataset link` : https://huggingface.co/datasets/alwanrahmana/Aspect-based-sentiment-analysis

## 📈 Performance
The model was trained using 5-Fold Cross Validation.  
Evaluation metrics include **accuracy** and **F1-score**, with per-aspect breakdowns.

## 🚀 How to Use

### Install dependencies:
```bash
pip install transformers torch