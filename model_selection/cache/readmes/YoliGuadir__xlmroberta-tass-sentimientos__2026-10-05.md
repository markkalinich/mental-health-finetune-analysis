---
language: es
tags:
- text-classification
- sentiment-analysis
- spanish
- xlm-roberta
- fine-tuned
metrics:
- f1
---

# XLM-RoBERTa-large + TASS — Clasificacion de Sentimientos en Espanol

## Descripcion
XLM-RoBERTa-large fine-tuneado sobre TASS para clasificar sentimientos en espanol.
Clases: N (Negativo), NEU (Neutro), P (Positivo).

## Baseline de referencia
- BETO sobre TASS: 0.6400 F1-Macro
- Mejor resultado XLM-RoBERTa: 0.6838 (batch=8)

## Metricas de desempeno

| Batch | Epocas | F1-Macro | F1-Weighted | Accuracy | Supera 64% |
|-------|--------|----------|-------------|----------|------------|
| 8     | 6      | 0.6773   | 0.68      | 0.68   | SI |
| 16    | 6      | 0.6838   | 0.69      | 0.69   | SI |
| 32    | 0      | 0.6659   | 0.67      | 0.67  | SI |

Mejor modelo: batch=8 F1-Macro=0.6838

## Matriz de Confusion
![Matriz](confusion_matrix.png)

## Uso del modelo
```python
from transformers import pipeline
clf = pipeline("text-classification", model="YoliGuadir/xlmroberta-tass-sentimientos")
clf("Me siento muy feliz hoy, fue un dia increible")
```

## Configuracion
- Modelo base: xlm-roberta-large
- Dataset: TASS (Twitter Sentiment Analysis)
- Train: 4085 muestras | Test: 2443 muestras
- Plataforma: Kaggle T4 x2
- Epocas: 6
- Learning rate: 1e-5
- fp16: True

## Maestria CODING - Universidad del Valle
Taller Final PLN - Gran Idea 2: Clasificacion de texto y NER