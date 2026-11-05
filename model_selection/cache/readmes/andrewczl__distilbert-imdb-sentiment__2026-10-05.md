---
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- distilbert
- sentiment-analysis
- imdb
---

# DistilBERT IMDB Sentiment

Modello DistilBERT fine-tuned per classificazione binaria del sentiment su recensioni IMDB.

## Dati
- Dataset: IMDB
- Training subset: 2000 esempi
- Test/validation subset: 500 esempi
- Seed: 42

## Training
- Modello base: distilbert-base-uncased
- Learning rate: 3e-5
- Epoche: 3

## Metriche
- Validation accuracy: 0.878
- Eval loss: 0.296265

## Limiti
Il modello è stato addestrato su un sottoinsieme ridotto del dataset IMDB e su recensioni in inglese, quindi i risultati non sono rappresentativi dell'intero dataset o di testi in altre lingue.
