---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- sentiment-analysis
- distilbert
- rotten_tomatoes
- generated_from_trainer
pipeline_tag: text-classification
widget:
- text: "This movie was absolutely fantastic, a real masterpiece!"
  example_title: "Critique positive"
- text: "A total waste of time, I fell asleep halfway through."
  example_title: "Critique négative"
- text: "The cinematography was breathtaking despite a slow narrative."
  example_title: "Critique mitigée"
---

# DistilBERT Sentiment Analysis — TP MLOps Hugging Face

- **Auteur :** Kanyep darry ([kanyep](https://huggingface.co/kanyep))
- **Modèle de base :** [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased)
- **Tâche :** Classification de texte binaire (Analyse de sentiment : `NEGATIVE` [0], `POSITIVE` [1])
- **Dataset d'entraînement :** Rotten Tomatoes (3000 exemples)
- **Projet :** TP MLOps — Master 2

## 📖 Description du Modèle
Ce modèle est une version fine-tunée de **DistilBERT** (architecture compacte et rapide de BERT) entraînée pour prédire la polarité de sentiment de critiques de films ou textes courts en anglais.

Il a été entraîné et versionné dans le cadre des ateliers pratiques MLOps sur la plateforme Hugging Face.

## 📊 Métriques & Hyperparamètres d'Entraînement
- **Nombre d'époques :** 2
- **Taux d'apprentissage (Learning Rate) :** 2e-5
- **Taille de batch (Train / Eval) :** 16 / 16
- **Optimiseur :** AdamW (PyTorch Fused) avec lr scheduler linéaire
- **Format des poids :** Safetensors (`model.safetensors`, 267 Mo)

## 💻 Utilisation avec Transformers `pipeline`

```python
from transformers import pipeline

# Chargement automatique du pipeline de classification de sentiment
classifier = pipeline("sentiment-analysis", model="kanyep/finetuning-sentiment-model-3000-samples")

# Exemples de prédiction
result = classifier("This movie was absolutely fantastic, a real masterpiece!")
print(result)
```

## 🌐 Démonstration Web Interactive (Space Gradio)
L'application web interactive associée à ce modèle est disponible ici :
👉 **[Space Gradio Analyse de Sentiment](https://huggingface.co/spaces/kanyep/distilbert-sentiment-analysis)**
