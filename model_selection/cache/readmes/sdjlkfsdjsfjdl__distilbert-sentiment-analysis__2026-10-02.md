---
language:
- en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- distilbert
- pytorch
- transformers
datasets:
- imdb
- rotten_tomatoes
metrics:
- accuracy
- f1
pipeline_tag: sentiment-analysis
widget:
- text: "This movie was absolutely fantastic! The acting and directing were top-notch."
- text: "A complete waste of time. Boring plot and terrible performances."
- text: "The cinematography was great, but the story felt a bit rushed."
---

# 🎬 DistilBERT - Sentiment Analysis

Ce modèle est une version optimisée de **DistilBERT** fine-tunée pour l'analyse de sentiment (classification binaire : avis positif vs négatif).  
Développé et déployé dans le cadre du cours **MLOps & Hugging Face** (MSI 4-27 DO A ISI PARIS).

## 📌 Description du Projet

- **Étudiant :** Hassif HANNAN
- **Modèle de base :** `distilbert-base-uncased`
- **Architecture :** Transformer bidirectionnel allégé (DistilBERT - 6 couches, 66M paramètres)
- **Tâche :** Classification de texte (Sentiment Analysis)
- **Dataset de référence :** IMDB / Rotten Tomatoes
- **Labels :**
  - `NEGATIVE` (0) : Avis critique négatif
  - `POSITIVE` (1) : Avis critique positif

## 📊 Évaluation & Performances

| Métrique | Score |
|---|---|
| **Accuracy** | **91.3%** |
| **F1-Score** | **0.912** |
| **Vitesse d'inférence** | ~15 ms / texte (CPU) |

## 💻 Utilisation rapide en Python

```python
from transformers import pipeline

# Chargement direct du modèle depuis le Hub Hugging Face
classifier = pipeline("sentiment-analysis", model="sdjlkfsdjsfjdl/distilbert-sentiment-analysis")

# Test sur des avis
reviews = [
    "This film is a masterpiece of modern cinema, truly inspiring!",
    "Terrible movie, predictable storyline and bad acting."
]

predictions = classifier(reviews)
for text, pred in zip(reviews, predictions):
    print(f"Avis : {text}")
    print(f"Sentiment : {pred['label']} (Confiance: {pred['score']:.4f})\n")
```

## 🌐 Démonstration Interactive (Gradio Space)

Une application web interactive est disponible pour tester ce modèle en direct :  
👉 **[Accéder au Space Gradio](https://huggingface.co/spaces/sdjlkfsdjsfjdl/sentiment-analysis-space)**
