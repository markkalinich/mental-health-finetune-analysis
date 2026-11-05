---
language: en
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - twitter
  - distilbert
  - fine-tuned
  - nlp
datasets:
  - sentiment140
metrics:
  - accuracy
model-index:
  - name: tweet-tone-classifier
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: Sentiment140
          type: sentiment140
        metrics:
          - type: accuracy
            value: 0.86
---

# 🐦 Tweet Tone Classifier

A fine-tuned [DistilBERT](https://huggingface.co/distilbert-base-uncased) model for 
binary sentiment classification of tweets — predicts whether a tweet is **Positive** or **Negative**.

Part of a larger project that also rewrites tweets in different tones (formal, casual, 
empathetic, assertive) using the Gemini API.

---

## 📊 Model Details

| Property         | Details                          |
|------------------|----------------------------------|
| Base model       | distilbert-base-uncased          |
| Task             | Binary Sentiment Classification  |
| Dataset          | Sentiment140 (50,000 samples)    |
| Training epochs  | 3                                |
| Batch size       | 32                               |
| Max token length | 64                               |
| Accuracy         | ~87%                             |
| Language         | English                          |

---

## 🚀 Quick Start

### Installation

pip install transformers torch


### Using the pipeline (easiest)

from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="KinSlay3rs/tweet-tone-classifier"
)

result = classifier("I can't believe my flight got cancelled again!!")
print(result)
# [{'label': 'NEGATIVE', 'score': 0.97}]

result = classifier("Just got promoted!! Best day ever 🎉")
print(result)
# [{'label': 'POSITIVE', 'score': 0.98}]


### Using the model directly

from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch

tokenizer = DistilBertTokenizerFast.from_pretrained("KinSlay3rs/tweet-tone-classifier")
model = DistilBertForSequenceClassification.from_pretrained("KinSlay3rs/tweet-tone-classifier")
model.eval()

LABELS = {0: "NEGATIVE", 1: "POSITIVE"}

def predict(tweet: str) -> str:
    inputs = tokenizer(tweet, return_tensors="pt", truncation=True, max_length=64)
    with torch.no_grad():
        logits = model(**inputs).logits
    label = LABELS[logits.argmax().item()]
    score = torch.softmax(logits, dim=1).max().item()
    return f"{label} (confidence: {score:.2f})"

print(predict("This is the worst experience I've ever had."))
# NEGATIVE (confidence: 0.96)

print(predict("Absolutely loving the new update!"))
# POSITIVE (confidence: 0.94)

---

## 📁 Dataset

Trained on a 50,000 sample subset of the 
[Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140) dataset, 
which contains 1.6 million tweets labelled as positive or negative.

**Preprocessing applied:**
- Removed URLs (`http://...`)
- Removed Twitter handles (`@username`)
- Removed special characters
- Truncated to 64 tokens

---

## 🏋️ Training Details

from transformers import TrainingArguments

args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=32,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)


**Hardware used:** Intel i5 7th Gen CPU / Kaggle T4 GPU  
**Training time:** ~25 minutes on GPU

---

## ⚠️ Limitations

- Trained only on English tweets — may not generalize to other languages
- Sarcasm and irony are often misclassified (a known challenge in sentiment analysis)
- Trained on tweets from 2009 — modern slang and emojis may reduce accuracy
- Only binary classification — does not detect neutral sentiment

---

## 🔭 Future Work

- [ ] Add neutral class (3-class classification)
- [ ] Train on more recent tweet data
- [ ] Add emoji-aware preprocessing
- [ ] Multilingual support using `xlm-roberta-base`

---

## 📦 Full Project

This model is part of the **Tweet Tone Classifier & Rewriter** project which includes:

- ✅ Sentiment classification (this model)
- ✅ Tone rewriting using Gemini API (formal / casual / empathetic / assertive)
- ✅ Gradio web interface
- ✅ Deployed on Hugging Face Spaces

🔗 **GitHub:** [github.com/KinSlay3rS/GenAI-Projects/Sentement-Analysis-DistilBERT](https://github.com/KinSlay3rS/GenAI-Projects/Sentement-Analysis-DistilBERT)  
🔗 **Live Demo:** [huggingface.co/spaces/KinSlay3rs/tweet-tone-classifier](https://huggingface.co/spaces/KinSlay3rs/tweet-tone-classifier)

---

## 🙋 Author

Made by **KinSlay3rs**  
🔗 [Hugging Face Profile](https://huggingface.co/KinSlay3rs)