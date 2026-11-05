
---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- distilbert
datasets:
- sst2
metrics:
- accuracy
- f1
- precision
- recall
pipeline_tag: text-classification
---

# Modelo de Análisis de Sentimientos

## Descripción
Modelo de clasificación de sentimientos (positivo/negativo) basado en ModernBERT.
Una versión eficiente de BERT base.

## Uso

```python
from transformers import pipeline

clasificador = pipeline("text-classification", model="IruNavi/modelo_reviews_sentimientos")
resultado = clasificador("This videogame is trash...")
print(resultado)
```

## Etiquetas
- POSITIVE: Sentimiento positivo
- NEGATIVE: Sentimiento negativo
## Limitaciones
- Solo funciona con texto en inglés.
 (Es posible que algunas frases las acierte en español pero, mantener uso solo en inglés)

- El modelo ha sido entrenado con reseñas de videojuegos de la página de metacritic.

## Resultados métricas en TEST:
- loss: 0.2966
- accuracy: 0.9443
- f1: 0.9629
- precision: 0.9580
- recall: 0.9678
