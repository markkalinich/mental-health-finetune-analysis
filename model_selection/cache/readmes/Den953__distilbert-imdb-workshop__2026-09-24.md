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
- stanfordnlp/imdb
language:
- en
metrics:
- accuracy
- f1
model-index:
- name: distilbert-imdb-workshop
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: imdb
      type: stanfordnlp/imdb
      split: test
    metrics:
    - type: accuracy
      value: 0.8275
      name: Accuracy
    - type: f1
      value: 0.8207792207792208
      name: F1
---

# distilbert-imdb-workshop

`distilbert-base-uncased` fine-tune sur un sous-echantillon d'
[`imdb`](https://huggingface.co/datasets/stanfordnlp/imdb) pour la classification
binaire de sentiment.

Atelier `Get_Started` du cours **MLOps M2**. Evalue avec **accuracy et F1**, les deux
metriques demandees par l'enonce.

## Resultats

| Metrique | Valeur |
|---|---|
| Accuracy | **0.8275** |
| F1 | **0.8208** |

L'accuracy est la proportion de predictions correctes ; le F1 est la moyenne
harmonique de la precision et du rappel. Les deux sont proches ici parce que
les classes d'IMDB sont equilibrees.

## Utilisation

```python
from transformers import pipeline

clf = pipeline("sentiment-analysis", model="Den953/distilbert-imdb-workshop", truncation=True)
clf("This movie was absolutely fantastic!")
```

## Entrainement

| Hyperparametre | Valeur |
|---|---|
| base | `distilbert-base-uncased` |
| train / test | 1500 / 400 exemples |
| epochs | 1 |
| learning rate | 2e-5 |
| batch size | 16 |
| weight decay | 0.01 |
| max length | 128 tokens (padding dynamique) |
| materiel | CPU |

## Limites

Entrainement volontairement court (1500 exemples, 1 epoque, CPU) :
exercice pedagogique, pas un modele de production. Avec 400 exemples
de test, l'accuracy rapportee a une marge d'erreur de l'ordre de +/- 5 points.
Critiques de films en anglais uniquement, souvent longues et tronquees a
128 tokens - le modele ne voit donc que le debut de chaque critique.
