---
language: en
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- emotion-detection
- lora
- peft
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
---

# DistilBERT Emotion Classifier

DistilBERT fine-tuned on 6-class emotion detection using LoRA (Low-Rank 
Adaptation). Trained on English tweets, classifies text into: 
sadness, joy, love, anger, fear, or surprise.

## How to use

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Pragyansh14/distilbert-emotion-classifier"
)

classifier("I can't believe this actually worked!")
# [{'label': 'surprise', 'score': 0.84}]
```

## Performance

| Emotion | F1 | Support |
|---|---|---|
| joy | 0.92 | 704 |
| sadness | 0.90 | 550 |
| anger | 0.85 | 275 |
| fear | 0.80 | 212 |
| love | 0.80 | 178 |
| surprise | 0.73 | 81 |

**Accuracy: 87.3% | Weighted F1: 0.87 | Macro F1: 0.83**

## Training details

- **Base model:** distilbert-base-uncased
- **Dataset:** dair-ai/emotion (16,000 train / 2,000 val / 2,000 test)
- **Method:** LoRA (r=8, alpha=32) via HuggingFace PEFT
- **Trainable parameters:** 742,662 / 67,700,748 (1.1%)
- **Epochs:** 3
- **Batch size:** 16
- **Hardware:** Apple M-series MPS GPU
- **Training time:** ~11 minutes

## Bias and limitations

The training dataset is significantly imbalanced — joy (33.5%) and 
sadness (29.2%) dominate while surprise is only 3.6%. As a result:

- Surprise recall is 0.64 — the model misses 36% of genuine surprise cases
- Ambiguous positive emotions (love, surprise) are frequently misclassified as joy
- Performance may degrade on formal or non-Twitter text domains
- Dataset sourced from English tweets — non-native English and other 
  dialects may be underrepresented

## GitHub

https://github.com/Pragyansh-V/-hf-finetuning-distilbert