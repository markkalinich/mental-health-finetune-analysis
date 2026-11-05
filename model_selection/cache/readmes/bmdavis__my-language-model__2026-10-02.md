---
language: en
license: apache-2.0
tags:
  - sentiment-analysis
  - text-classification
  - transformers
  - distilbert
datasets:
  - imdb
metrics:
  - accuracy
model-index:
  - name: DistilBERT IMDb Sentiment Classifier
    results:
      - task:
          name: Sentiment Analysis
          type: text-classification
        dataset:
          name: IMDb
          type: imdb
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.88  # You can update this later
---
# 🧠 Sentiment Analysis Model — DistilBERT Fine-Tuned on IMDb 🎬
This model is a fine-tuned version of [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) on the [IMDb movie review dataset](https://huggingface.co/datasets/imdb) for **binary sentiment classification** (positive/negative). It was trained using Hugging Face Transformers and PyTorch.

## 🔍 Intended Use

This model is designed to classify movie reviews (or other English text) as **positive** or **negative** sentiment. It's ideal for:
- Opinion mining
- Social media analysis
- Review classification
- Text classification demos

## 🧪 Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "bmdavis/my-language-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "This movie was amazing and really well-acted!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
prediction = torch.argmax(outputs.logits).item()

print("Sentiment:", "Positive" if prediction == 1 else "Negative")

📊 Dataset
IMDb Dataset

25,000 training samples

25,000 test samples

Labels: 0 = Negative, 1 = Positive

🧠 Model Details
Base Model: distilbert-base-uncased

Architecture: Transformer (BERT-like)

Framework: PyTorch

Tokenizer: WordPiece

🛠️ Training
Epochs: 3

Batch Size: 8

Optimizer: AdamW

Loss: CrossEntropy

Trainer API used

🔐 License
This model is released under the Apache 2.0 license.

✍️ Author
Created by Brody Davis (@bmdavis)
Trained and uploaded using Hugging Face Hub and Transformers
