---
language:
- zh
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- pytorch
- bert
datasets:
- OpenModels/Chinese-Herbal-Medicine-Sentiment
metrics:
- accuracy
- f1
---

# Herbal-Sentiment-BERT

## Model Description
This model is a fine-tuned version of `bert-base-chinese` for sentiment analysis in the specific domain of Chinese herbal medicine e-commerce reviews. It is designed to classify customer reviews into three sentiment categories: Negative (0), Neutral (1), and Positive (2).

The model was specifically optimized to handle highly imbalanced datasets (where positive samples dominate) by capturing deep semantic relationships and domain-specific terminology (e.g., specific herbal names and distinct symptom descriptions), effectively mitigating the risk of overfitting to the majority class.

## Intended Uses & Limitations
- **Intended Use:** Automated sentiment tagging for traditional Chinese medicine (TCM) product reviews, customer feedback analysis, and e-commerce rating systems.
- **Limitations:** The model is trained exclusively on TCM-related texts. Its performance may degrade if applied to general domain texts or other highly specialized fields (e.g., modern electronics).

## Training and Evaluation Data
The model was fine-tuned on a dataset comprising over 210,000 authentic user reviews from herbal medicine e-commerce platforms. 

During the evaluation on a held-out test set (representing the imbalanced distribution), the model achieved the following performance, significantly outperforming sequence-based baselines (e.g., Bi-LSTM + Attention) in minority class identification:
- **Accuracy:** 89.36%
- **Macro F1-Score:** 77.08%

## How to use

You can easily use this model with the `transformers` library:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("1hugh/Herbal-Sentiment-BERT")
model = AutoModelForSequenceClassification.from_pretrained("1hugh/Herbal-Sentiment-BERT")

text = "这当归发霉了，味道极差！"
inputs = tokenizer(text, return_tensors="pt")

outputs = model(**inputs)
predictions = outputs.logits.argmax(dim=-1)

# Labels: 0 -> Negative, 1 -> Neutral, 2 -> Positive
print(f"Predicted class: {predictions.item()}")