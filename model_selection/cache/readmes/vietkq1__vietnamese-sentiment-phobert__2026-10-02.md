---
license: mit
language:
  - vi
tags:
  - sentiment-analysis
  - text-classification
  - vietnamese
pipeline_tag: text-classification
base_model: vinai/phobert-base
datasets:
  - vietkq1/your-dataset-name
model-index:
  - name: vietnamese-sentiment-phobert
    results: []
---

# 🇻🇳 Vietnamese Sentiment Analysis (PhoBERT)

This is a fine-tuned version of [vinai/phobert-base](https://huggingface.co/vinai/phobert-base) for sentiment analysis on Vietnamese text.  
It was trained to classify user reviews or text inputs into either:

- **POSITIVE** (1)
- **NEGATIVE** (0)

## 🔧 Model Details

- **Base model**: `vinai/phobert-base`
- **Fine-tuned by**: [vietkq1](https://huggingface.co/vietkq1)
- **Language**: Vietnamese (`vi`)
- **Task**: Sentiment Analysis (`text-classification`)
- **Framework**: HuggingFace Transformers + PyTorch

## 🧠 Intended Uses

This model is ideal for:

- Classifying reviews (e.g., app reviews, product reviews, etc.)
- Analyzing user feedback in Vietnamese
- Social media sentiment mining

## 🧪 Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

model = AutoModelForSequenceClassification.from_pretrained("vietkq1/vietnamese-sentiment-phobert")
tokenizer = AutoTokenizer.from_pretrained("vietkq1/vietnamese-sentiment-phobert")

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

text = "Sản phẩm quá tuyệt vời, mình rất hài lòng!"
print(classifier(text))
