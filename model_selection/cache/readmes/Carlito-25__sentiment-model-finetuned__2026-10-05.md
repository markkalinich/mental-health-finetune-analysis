---
license: mit
tags:
- sentiment-analysis
- french
- multilingual
- xlm-roberta
language:
- fr
- en
datasets:
- custom
metrics:
- accuracy
---

# Carlito-25/sentiment-model-finetuned

Modèle XLM-RoBERTa fine-tuné pour l'analyse de sentiment multilingue (pour des données de type commentaires youtube)

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis", 
    model="Carlito-25/sentiment-model-finetuned", 
    device=-1, 
    truncation=True, 
    max_length=514
)

result = classifier("Ce commentaire est fantastique!")
print(result)
```

## Model Details

- **Base Model**: cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual
- **Fine-tuned on**: Custom French YouTube comments dataset
- **Task**: Sentiment Analysis (3 classes: POSITIVE, NEGATIVE, NEUTRAL)
