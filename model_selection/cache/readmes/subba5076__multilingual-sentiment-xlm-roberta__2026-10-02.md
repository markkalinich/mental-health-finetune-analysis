---
license: mit
language:
  - en
  - de
  - it
tags:
  - sentiment
  - multilingual
  - classification
  - xlm-roberta
datasets:
  - amazon_reviews_multi
metrics:
  - f1
pipeline_tag: text-classification
widget:
  - text: "I love this product!"
  - text: "Das war eine schreckliche Erfahrung."
  - text: "Questo è stato ok, niente di speciale."
---

# 🌍 Multilingual Sentiment Classifier (XLM-RoBERTa)

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) for **multilingual sentiment classification** across English, German, and Italian.

We built this model to classify sentiment into:
- `0` → Negative  
- `1` → Neutral  
- `2` → Positive

---

## ✍️ How We Built It

This model was fine-tuned using the [Amazon Reviews Multilingual Dataset](https://huggingface.co/datasets/amazon_reviews_multi), specifically on the **English**, **German**, and **Italian** subsets.  
Training was done using PyTorch and Hugging Face Transformers.

### Preprocessing
- Texts were tokenized using `XLMRobertaTokenizer`
- Labels were mapped to integers (`negative`: 0, `neutral`: 1, `positive`: 2)
- Dataset was split into train/test/validation using an 80/10/10 ratio

### Training
- Model: `xlm-roberta-base`
- Epochs: 2
- Optimizer: AdamW
- Batch size: 8
- Evaluation metric: Macro F1-score
- Hardware: Google Colab GPU

---

## 🔍 Example Usage

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="subba5076/multilingual-sentiment-xlm-roberta")

classifier("Der Film war unglaublich schön.")  # German
classifier("This phone is terrible.")           # English
classifier("È stato un buon acquisto.")         # Italian
```
📊 Evaluation
Macro F1-score on test set: 0.81
Confusion matrix and training curves can be shared in future updates.

👨‍💻 Authors
This project was developed as part of a team NLP assignment.

Team Members:

Subrahmanya Rajesh Nayak @subba5076

Rim Tafech

🪪 License
This model is licensed under the MIT License.
