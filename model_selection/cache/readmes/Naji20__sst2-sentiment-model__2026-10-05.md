---
language:
- en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- distilbert
- sst2
datasets:
- glue
- sst2
metrics:
- accuracy
base_model: distilbert-base-uncased
pipeline_tag: text-classification
widget:
- text: "This movie is absolutely amazing!"
- text: "I hated every minute of it."
- text: "Best film I've ever seen!"
---

# DistilBERT SST-2 Sentiment Analysis

This model is a fine-tuned version of `distilbert-base-uncased` on the SST-2 (Stanford Sentiment Treebank) dataset for sentiment analysis.

## Model Description

- **Model:** DistilBERT (base, uncased)
- **Task:** Binary sentiment classification (Positive/Negative)
- **Language:** English
- **Training Dataset:** SST-2 (GLUE benchmark)
- **Author:** Naji (Аммар Нажи Али Саад)
- **Institution:** Kazan Federal University

## Training Details

### Training Data
- **Dataset:** GLUE SST-2
- **Training samples:** 67,349
- **Validation samples:** 872
- **Test samples:** 1,821

### Training Configuration
- **Epochs:** 3
- **Batch size:** 16
- **Learning rate:** 2e-5
- **Optimizer:** AdamW
- **Weight decay:** 0.01
- **Platform:** Google Colab (T4 GPU)

### Results
- **Validation Accuracy:** 89.9%
- **Training Time:** ~36 minutes on T4 GPU

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "Naji20/sst2-sentiment-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Predict sentiment
text = "This movie is amazing!"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
outputs = model(**inputs)
prediction = torch.argmax(outputs.logits, dim=1).item()
sentiment = "Positive" if prediction == 1 else "Negative"
print(f"Sentiment: {sentiment}")
```

## Example Predictions

| Text | Prediction |
|------|------------|
| "This movie is absolutely amazing!" | Positive ✅ |
| "I hated every minute of it." | Negative ❌ |
| "Best film I've ever seen!" | Positive ✅ |
| "Terrible waste of time." | Negative ❌ |

## Limitations

- This model is trained only on English movie reviews
- Performance may vary on other domains (e.g., product reviews, tweets)
- Binary classification only (Positive/Negative, no neutral class)

## Citation
```
@inproceedings{socher2013recursive,
  title={Recursive deep models for semantic compositionality over a sentiment treebank},
  author={Socher, Richard and Perelygin, Alex and Wu, Jean and Chuang, Jason and Manning, Christopher D and Ng, Andrew and Potts, Christopher},
  booktitle={Proceedings of the 2013 conference on empirical methods in natural language processing},
  pages={1631--1642},
  year={2013}
}
```

## Model Card Authors

Naji (Аммар Нажи Али Саад) - Kazan Federal University
