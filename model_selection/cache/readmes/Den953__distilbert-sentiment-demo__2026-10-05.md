---
license: apache-2.0
base_model: distilbert-base-uncased
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
- distilbert
- generated_from_trainer
datasets:
- cornell-movie-review-data/rotten_tomatoes
language:
- en
metrics:
- accuracy
model-index:
- name: distilbert-sentiment-demo
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: rotten_tomatoes
      type: cornell-movie-review-data/rotten_tomatoes
      split: test
    metrics:
    - type: accuracy
      value: 0.8414634146341463
      name: Accuracy
---

# distilbert-sentiment-demo

`distilbert-base-uncased` fine-tune sur
[`rotten_tomatoes`](https://huggingface.co/datasets/cornell-movie-review-data/rotten_tomatoes)
(critiques de films courtes) pour la classification binaire de sentiment.

Realise dans le cadre du cours **MLOps M2** (lab Hugging Face).

## Labels

| id | label |
|---|---|
| 0 | `NEGATIVE` |
| 1 | `POSITIVE` |

## Resultats

| Split | Accuracy | Loss |
|---|---|---|
| test (1066 exemples) | **0.8415** | 0.3908 |

## Utilisation

```python
from transformers import pipeline

clf = pipeline("sentiment-analysis", model="Den953/distilbert-sentiment-demo", truncation=True)
clf("This movie was absolutely fantastic!")
```

Une version **ONNX** est disponible dans `onnx/model.onnx`.

## Entrainement

| Hyperparametre | Valeur |
|---|---|
| base | `distilbert-base-uncased` |
| train / test | 8530 / 1066 exemples |
| epochs | 1 |
| learning rate | 2e-5 |
| batch size | 16 |
| weight decay | 0.01 |
| max length | 128 tokens (padding dynamique) |
| materiel | CPU |

Entrainement realise **en CPU** (AMD Ryzen, 12 threads), pas sur GPU : le nombre d'epoques a ete reduit par rapport a l'enonce du lab pour tenir dans un temps raisonnable. Ce choix est indique dans le tableau d'hyperparametres ci-dessus.

## Limites

Entraine uniquement sur des **critiques de films en anglais**, courtes (une phrase).
Les performances chutent sur des textes longs, d'un autre domaine (produits, support
client), ou dans une autre langue. Le modele herite des biais presents dans les
critiques de Rotten Tomatoes. Sortie binaire uniquement : pas de classe neutre.

## Demo

Space de demonstration : https://huggingface.co/spaces/Den953/sentiment-analysis-distilbert
