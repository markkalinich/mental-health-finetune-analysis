---
language: es
license: mit
tags:
- sentiment-analysis
- spanish
- bert
- text-classification
pipeline_tag: text-classification
---

# BETO Sentiment Analysis — Spanish 🇪🇸

BERT-based sentiment analysis for Spanish text, fine-tuned on 50,000 IMDB movie reviews translated to Spanish.

## Model Description
- **Base model**: dccuchile/bert-base-spanish-wwm-cased (BETO)
- **Task**: Sentiment Analysis (positive/negative)
- **Language**: Spanish
- **Accuracy**: 88% on test set (10,000 reviews)

## How to Use

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import torch.nn.functional as F

tokenizer = BertTokenizer.from_pretrained('vipont/beto-sentiment-spanish')
model = BertForSequenceClassification.from_pretrained('vipont/beto-sentiment-spanish')
model.eval()

def predict(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)
    pred = torch.argmax(probs).item()
    return 'positive' if pred == 1 else 'negative', round(probs[0][pred].item() * 100, 2)

print(predict("Me encantó la película, fue increíble"))
print(predict("Terrible, una pérdida de tiempo"))
```

## Training
- **Dataset**: 50,000 IMDB reviews translated to Spanish
- **Epochs**: 3
- **Optimizer**: AdamW (lr=2e-5)
- **Max length**: 128 tokens

## Results
| Metric | Score |
|--------|-------|
| Accuracy | 88% |
| F1 (positive) | 0.88 |
| F1 (negative) | 0.87 |