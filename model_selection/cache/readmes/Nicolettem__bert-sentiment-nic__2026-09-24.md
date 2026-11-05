---
library_name: transformers
license: mit
datasets:
- Chidvi201/Twitter_Data.csv
language:
- en
metrics:
- accuracy
base_model:
- distilbert-base-uncased
pipeline_tag: text-classification
tags:
- sentiment-analysis
- transformers
- distilbert
- huggingface
- twitter
- airline
- gradio
- text-classification
---

# ✈️ BERT Airline Sentiment Classifier

A DistilBERT-based model fine-tuned for sentiment analysis on airline-related tweets. It classifies input text into **positive**, **neutral**, or **negative** sentiment categories.

---

## 🧠 Model Details

### Model Description

This model uses `distilbert-base-uncased` as a base and is fine-tuned on a cleaned dataset of airline tweets. It performs multi-class classification with 3 sentiment labels.

- **Developed by:** Nicolettem
- **Model type:** Transformer-based (DistilBERT)
- **Language(s):** English (`en`)
- **License:** MIT
- **Fine-tuned from:** [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased)

---

## 📦 Model Sources

- **Repository:** https://huggingface.co/Nicolettem/bert-sentiment-nic
- **Demo Space:** [Gradio Demo](https://huggingface.co/spaces/Nicolettem/bert_sentiment_demo)
- **Dataset:** [Chidvi201/Twitter_Data.csv](https://huggingface.co/datasets/Chidvi201/Twitter_Data.csv)

---

## 💡 Uses

### Direct Use
You can use this model to classify sentiment of customer reviews or tweets — especially in the airline or travel domain.

### Downstream Use
It can serve as a base for training more domain-specific sentiment models, or be integrated into social media monitoring tools.

### Out-of-Scope Use
- The model was not trained on non-English tweets or formal customer service chat.
- It may reflect dataset biases and perform poorly on sarcastic or ambiguous text.

---

## ⚠️ Bias, Risks, and Limitations

- May reflect biases in public Tweets
