---
language:
- en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- distilbert
- imdb
datasets:
- stanfordnlp/imdb
---

# DistilBERT IMDB Sentiment Classifier

Modello DistilBERT fine-tuned per la classificazione del sentiment
su recensioni IMDB in lingua inglese.

## Dataset

Dataset: IMDB.

Per il laboratorio è stato utilizzato uno snapshot composto da:

- 2000 esempi di training
- 500 esempi di valutazione
- seed: 42

## Modello

Base model:

`distilbert-base-uncased`

Il modello classifica il testo in due classi:

- 0: negative
- 1: positive

## Training

- Epochs: 3
- Learning rate: 2e-5
- Train batch size: 16
- Eval batch size: 16
- Precision: FP16
- GPU: NVIDIA Tesla T4

## Risultati

Evaluation accuracy: 0.884

Evaluation loss: 0.310889

È stato inoltre confrontato un secondo esperimento con learning rate 5e-5,
che ha ottenuto accuracy 0.880.

## Limitazioni

Il modello è stato addestrato su un sottoinsieme ridotto del dataset IMDB
ed è pensato per recensioni in lingua inglese.

Potrebbe avere prestazioni inferiori su testi appartenenti ad altri domini,
su lingue diverse dall'inglese o su testi molto differenti dalle recensioni
cinematografiche.
