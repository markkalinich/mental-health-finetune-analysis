---
language:
- en
tags:
- sentiment-analysis
- text-classification
- bert
- manav
- ManavDhayeCoder/sentiment-bert
- ManavDhaye
pipeline_tag: text-classification
base_model:
- google-bert/bert-base-uncased
datasets:
- imdb
library_name: transformers
widget:
- text: This movie was amazing!
- text: Worst movie I have ever seen.
model-index:
- name: sentiment-bert
  results: []
metrics:
- accuracy
---

# 📘 BERT Sentiment Analysis Model (Fine-Tuned on IMDB)

This model is a fine-tuned version of **google-bert/bert-base-uncased**, trained on the **IMDB movie reviews dataset** for binary sentiment classification.

It predicts whether text expresses **negative** or **positive** sentiment.

This model is hosted by **[@ManavDhayeCoder](https://huggingface.co/ManavDhayeCoder)**.

---

# 🚀 Model Overview

| Property | Value |
|----------|--------|
| **Base model** | google-bert/bert-base-uncased |
| **Task** | Sentiment Analysis (Sequence Classification) |
| **Labels** | negative / positive |
| **Dataset** | IMDB |
| **Library** | Hugging Face Transformers |
| **Format** | model.safetensors |

The model has two classes:

- `LABEL_0` → **negative**  
- `LABEL_1` → **positive**

---

# 🔥 Quick Usage Example

```python
from transformers import pipeline

clf = pipeline("text-classification", model="ManavDhayeCoder/sentiment-bert")

print(clf("This movie was amazing!"))