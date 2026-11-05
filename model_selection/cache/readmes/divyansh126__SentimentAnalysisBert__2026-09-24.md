---
library_name: transformers
tags:
- text-classification
- bert
- sentiment-analysis
license: mit
language:
- en
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
---


## Model Details

- **Model type**: BERT-based sequence classification
- **Base model**: `bert-base-uncased`
- **Number of classes**: 3
- **Trained on**: Custom labeled dataset
- **Framework**: PyTorch with 🤗 Transformers
- **Max sequence length**: 512
- **Tokenizer**: `bert-base-uncased`

### Model Description

This is a fine-tuned `bert-base-uncased` model for **multi-class text classification**. The model was trained on a custom dataset to classify text into 3 categories: `Negative`, `Neutral`, and `Positive`.

- **Developed by:** Divyansh Rajput
- **Model type:** Transformer(Bert-Base-Uncased)
- **Language(s) (NLP):** English
- **License:** Mit
- **Finetuned from model :** Bert-Base-Uncased

### Model Sources 

- **Repository:** https://huggingface.co/divyansh126/SentimentAnalysisBert/

## 📊 Classes

| Label | Description |
|-------|-------------|
| 0     | Negative    |
| 1     | Neutral     |
| 2     | Positive    |

## 🚀 How to Get Started with the Model## 

from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("divyansh126/")
model = AutoModelForSequenceClassification.from_pretrained("your-username/your-model-name")

inputs = tokenizer("I loved the product!", return_tensors="pt")
outputs = model(**inputs)
predicted_class = outputs.logits.argmax(dim=-1).item()
 

## 🧪 Training Details

- **Training framework**: Hugging Face `Trainer`
- **Epochs**: 1
- **Batch size**: 32
- **Learning rate**: 2e-5
- **Device**: Trained on GPU (`cuda`)


### Training Data

Dataset Link - https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis

## Evaluation

## 📈 Evaluation

| Metric     | Score   |
|------------|---------|
| Accuracy   | 0.85    |
| F1 Score   | 0.85    |
| Precision  | 0.85    |
| Recall     | 0.85    |

#### Summary

This model is a fine-tuned version of BERT (bert-base-uncased) for multi-class text classification. It has been trained to classify input text into three sentiment-based categories: Negative (0), Neutral (1), and Positive (2).
The model was trained on a custom dataset using the Hugging Face Trainer API with PyTorch. It uses standard preprocessing with a maximum sequence length of 512 tokens. This fine-tuned BERT model achieves strong performance in sentiment classification tasks and is suitable for real-time predictions in production environments or APIs.