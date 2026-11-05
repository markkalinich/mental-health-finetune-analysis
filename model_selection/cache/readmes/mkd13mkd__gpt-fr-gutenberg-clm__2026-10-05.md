---
language: fr
license: mit
tags:
  - nlp
  - text-classification
  - sentiment-analysis
  - french
base_model: asi/gpt-fr-cased-small
datasets:
  - allocine
model_name: gpt-fr-sentiment-classifier
widget:
  - text: "Ce film est une véritable réussite !"
metrics:
  - accuracy
---

# GPT-FR – Classifieur de sentiment (Allociné)

Modèle binaire **positif / négatif** affiné sur le jeu de données
**Allociné** (160 000 critiques de films en français).  
La tête de classification repose sur le **GPT-2 francophone**
`asi/gpt-fr-cased-small`.

|                        | Valeur |
|------------------------|--------|
| **Base**               | asi/gpt-fr-cased-small |
| **Dataset**            | Allociné (train 160 k / val 20 k) |
| **Max seq length**     | 128 |
| **Batch size**         | 8 |
| **Époques**            | 2 |
| **Accuracy (val)**     | **94 %** |

## Exemple d’utilisation

```python
from transformers import pipeline

sentiment = pipeline(
    "text-classification",
    model="mkd13mkd/gpt-fr-sentiment-classifier",
    tokenizer="asi/gpt-fr-cased-small"
)

print(sentiment("Ce film est une véritable réussite !"))
# [{'label': 'LABEL_1', 'score': 0.97}]  → LABEL_1 = positif
