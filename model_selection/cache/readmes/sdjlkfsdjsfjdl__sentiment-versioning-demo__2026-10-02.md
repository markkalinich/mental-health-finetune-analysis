---
language:
- en
license: apache-2.0
tags:
- sentiment-analysis
- model-versioning
- distilbert
- rotten_tomatoes
- imdb
metrics:
- accuracy
pipeline_tag: text-classification
---

# 🔄 Sentiment Analysis - Versioning Demo (v1, v2, v3)

Modèle DistilBERT multi-versions développé dans le cadre du TD **MLOps sur Hugging Face (Model Versioning & Promotion)**.
Auteur : **Hassif HANNAN** (MSI 4-27 DO A ISI PARIS).

## 📌 Historique des Versions (Tags & Branches)

| Version / Tag | Configuration | Dataset | Accuracy | Statut |
|---|---|---|---|---|
| **v1** | baseline, max_length=128 | rotten_tomatoes | 88.5% | Archivé |
| **v2** | preprocessing, max_length=256 | rotten_tomatoes | 89.8% | Archivé |
| **v3** | dataset hybride, max_length=256 | imdb | **91.3%** | **Promu** |
| **production** | Branche de production pointant sur 3 | imdb | **91.3%** | **En Production** |

## 🚀 Utilisation de la version de production

`python
from transformers import pipeline

# Chargement direct de la version promue en production
classifier = pipeline(
    'sentiment-analysis',
    model='sdjlkfsdjsfjdl/sentiment-versioning-demo',
    revision='production'
)

print(classifier('This film was genuinely great!'))
`
