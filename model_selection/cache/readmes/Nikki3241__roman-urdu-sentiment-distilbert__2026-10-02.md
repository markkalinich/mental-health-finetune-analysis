---
language: 
- ur
license: apache-2.0
tags:
- sentiment-analysis
- roman-urdu
- text-classification
- distilbert
datasets:
- community-datasets/roman_urdu
metrics:
- accuracy
- f1
---

# Roman Urdu Sentiment Analysis

A fine-tuned DistilBERT model that classifies Roman Urdu text (Urdu written in Latin script) into three sentiment categories: **Positive**, **Negative**, or **Neutral**.

## Model Description

This model fine-tunes `distilbert-base-uncased` on a dataset of Roman Urdu sentences to perform sentiment classification. Roman Urdu presents unique NLP challenges due to inconsistent spelling, informal grammar, and lack of standardized script — making sentiment analysis on it a genuinely hard task compared to standard English NLP.

## Training Details

- **Base model:** distilbert-base-uncased
- **Dataset:** community-datasets/roman_urdu (20,229 examples)
- **Train/test split:** 80/20 (16,183 / 4,046)
- **Epochs:** 3
- **Learning rate:** 2e-5
- **Batch size:** 16
- **Max sequence length:** 64 tokens

## Evaluation Results

| Metric | Score |
|--------|-------|
| Accuracy | 66.0% |
| F1 (weighted) | 66.0% |

| Class | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| Positive | 0.63 | 0.64 | 0.63 |
| Negative | 0.60 | 0.59 | 0.60 |
| Neutral | 0.71 | 0.72 | 0.72 |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("YOUR_USERNAME/roman-urdu-sentiment-distilbert")
model = AutoModelForSequenceClassification.from_pretrained("YOUR_USERNAME/roman-urdu-sentiment-distilbert")

text = "yeh bohat acha hai"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=64)
outputs = model(**inputs)
prediction = torch.argmax(outputs.logits, dim=-1).item()

labels = ["Positive", "Negative", "Neutral"]
print(labels[prediction])
```

## Limitations

- Performance reflects the inherent difficulty of informal, non-standardized Roman Urdu text
- Neutral/lukewarm sentiment is sometimes misclassified as Negative
- Trained on a relatively small dataset (~20k examples); performance may vary on domain-specific text (e.g. product reviews vs. social media)

## Author

Fine-tuned by Nusrat as part of an applied NLP/LLM portfolio project.