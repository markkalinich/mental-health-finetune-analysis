---
language: en
license: mit
tags:
- finance
- sentiment-analysis
- finbert
- stock-market
datasets:
- financial_phrasebank
metrics:
- accuracy
- f1
model-index:
- name: suha-memon/finbert-stock-sentiment
  results:
  - task:
      type: text-classification
      name: Financial Sentiment Analysis
    metrics:
    - type: accuracy
      value: 0.8188
      name: Accuracy
    - type: f1
      value: 0.8009
      name: F1 Macro
---

# FinBERT Stock Sentiment Analyzer

Fine-tuned FinBERT model for financial sentiment analysis of stock-related news headlines.

## Model Description

This model is a fine-tuned version of [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) on financial sentiment data. It classifies financial text into three categories:
- **Negative** (0)
- **Neutral** (1)
- **Positive** (2)

## Training Details

### Training Approach
- **Base Model**: ProsusAI/finbert
- **Fine-tuning Method**: Focal Loss with class weighting
- **Training Epochs**: 10 (with early stopping)
- **Learning Rate**: 3e-5
- **Batch Size**: 16 (effective 32 with gradient accumulation)
- **Warmup Ratio**: 0.1

### Performance Metrics

| Metric | Score |
|--------|-------|
| **Accuracy** | 81.88% |
| **F1 Macro** | 0.8009 |
| **F1 Weighted** | 0.8259 |

### Per-Class Performance

| Class | F1 Score |
|-------|----------|
| Negative | 0.6719 |
| Neutral | 0.8203 |
| Positive | 0.9104 |

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "suha-memon/finbert-stock-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example usage
headline = "Apple announces record-breaking quarterly earnings"
inputs = tokenizer(headline, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Get probabilities
negative_prob = predictions[0][0].item()
neutral_prob = predictions[0][1].item()
positive_prob = predictions[0][2].item()

print(f"Negative: {negative_prob:.2%}")
print(f"Neutral: {neutral_prob:.2%}")
print(f"Positive: {positive_prob:.2%}")
```

## Intended Use

This model is designed for:
- Analyzing sentiment of financial news headlines
- Stock market sentiment analysis
- Financial document classification
- Real-time news sentiment tracking

## Limitations

- The model performs best on financial news headlines (similar to training data)
- Negative sentiment detection (F1: 67%) is weaker due to class imbalance in training data
- May not generalize well to non-financial domains
- Limited to English language text

## Training Data

The model was trained on financial sentiment data from Kaggle, consisting of:
- Training set: ~4,800 labeled examples
- Validation set: ~580 examples
- Test set: ~580 examples

Class distribution was imbalanced with fewer negative examples, addressed using Focal Loss.

## Citation

If you use this model, please cite:
```bibtex
@misc{finbert-stock-sentiment,
  author = {Your Name},
  title = {FinBERT Stock Sentiment Analyzer},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/suha-memon/finbert-stock-sentiment}}
}
```

## Team

- Suha Memon
- Nick Cirillo
- Kalen Truong
- Bruce Zhang

## Acknowledgments

- Base model: [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert)
- Framework: Hugging Face Transformers
