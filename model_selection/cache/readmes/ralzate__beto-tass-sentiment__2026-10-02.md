---
language:
- es
license: cc-by-4.0
library_name: transformers
pipeline_tag: text-classification
base_model: dccuchile/bert-base-spanish-wwm-cased
tags:
- sentiment-analysis
- spanish
- beto
- tass
- text-classification
datasets:
- TASS
metrics:
- f1
- accuracy
model-index:
- name: beto-tass-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: TASS
      type: TASS
    metrics:
    - type: f1
      value: 0.668
      name: F1 macro
    - type: accuracy
      value: 0.675
      name: Accuracy
---

# BETO fine-tuned para análisis de sentimiento (TASS)

Modelo de **clasificación de sentimiento en español** basado en
[BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased)
(`bert-base-spanish-wwm-cased`), afinado sobre el corpus **TASS** (tweets en español).

Clasifica un texto en **3 clases**:

| id | etiqueta | significado |
|----|----------|-------------|
| 0  | `N`      | Negativo |
| 1  | `NEU`    | Neutro |
| 2  | `P`      | Positivo |

## Resultados

Evaluación sobre el split de validación de TASS (mejor checkpoint, batch size 16):

| Métrica | Valor |
|---------|-------|
| F1 macro | **0.668** |
| F1 weighted | 0.673 |
| Accuracy | 0.675 |
| Precision (macro) | 0.672 |
| Recall (macro) | 0.667 |

**Nota:** en este corpus BETO casi iguala a XLM-RoBERTa-large (F1 0.676) pese a ser
un modelo mucho más pequeño (~110M vs ~560M parámetros). La clase `NEU` es la más
difícil (ambigua), lo que limita el F1 macro en las tres clases.

## Uso

```python
from transformers import pipeline

clf = pipeline("text-classification", model="ralzate/beto-tass-sentiment")
clf("Me encantó la película, la mejor del año")
# [{'label': 'P', 'score': 0.97}]
```

O con la API de bajo nivel:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tok = AutoTokenizer.from_pretrained("ralzate/beto-tass-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("ralzate/beto-tass-sentiment")

inputs = tok("No me gustó para nada el servicio", return_tensors="pt")
pred = model(**inputs).logits.argmax(-1).item()
print(model.config.id2label[pred])  # N
```

## Entrenamiento

- **Base:** `dccuchile/bert-base-spanish-wwm-cased` (BETO).
- **Datos:** TASS (sentimiento, español, 3 clases N/NEU/P).
- **Hiperparámetros:** batch size 16, fine-tuning completo; mejor checkpoint por
  F1 macro en validación.
- **Hardware:** Mac M1 Pro (16 GB), entrenamiento con MPS.

## Limitaciones

- Entrenado con texto de **Twitter**: rinde mejor en lenguaje informal/corto; puede
  degradar en textos largos o formales.
- La clase `NEU` es ambigua y concentra la mayor parte de los errores.
- Sesgos propios de TASS y del dominio de redes sociales.

## Contexto

Modelo derivado de un trabajo de maestría en PLN sobre clasificación de texto y NER
en español. Modelo hermano: [`ralzate/beto-prostata-ner`](https://huggingface.co/ralzate/beto-prostata-ner)
(NER clínico).

Licencia: CC-BY-4.0.
