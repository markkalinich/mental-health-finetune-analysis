---
language:
  - es
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model: xlnet/xlnet-base-cased
datasets:
  - cardiffnlp/tweet_sentiment_multilingual
tags:
  - sentiment-analysis
  - spanish
  - text-classification
---

# Análisis de sentimiento en español (XLNet)

Clasificación de sentimiento en español en 3 clases (negativo, neutral, positivo) mediante *fine-tuning* de XLNet (base).

**Autor:** Jhusef Alfonso López Parra

## Descripción

Modelo basado en Transformers, afinado (*fine-tuning*) para clasificación de texto en español. Está listo para inferencia directa con la librería `transformers` de Hugging Face. Forma parte de un trabajo de PLN sobre clasificación de texto y reconocimiento de entidades nombradas (NER) en español.

## Uso

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="jhusef-lopez/sentimiento-xlnet-es")
print(pipe("Escribe aquí tu texto en español."))
```

## Etiquetas

| id | etiqueta |
|---:|----------|
| 0 | `NEG` |
| 1 | `NEU` |
| 2 | `POS` |

## Métricas de evaluación

| Métrica | Valor |
|---------|-------|
| F1-macro (validación) | 0.561 |
| Batch size | 8 |
| Épocas (Early Stopping) | 8 |

_Mejor configuración del grid de *batch size* (8/16/32) según F1-macro de validación._

## Entrenamiento

- **Modelo base:** `xlnet/xlnet-base-cased`
- **Dataset:** [`cardiffnlp/tweet_sentiment_multilingual`](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual)
- **Framework:** PyTorch + 🤗 Transformers (`Trainer`, `EarlyStoppingCallback`)
- **Idioma:** español (es)

## Limitaciones y uso responsable

El modelo puede reflejar sesgos presentes en los datos de entrenamiento. No debe emplearse como única fuente para decisiones críticas sin revisión humana experta.

## Cita

Si utilizas este modelo, por favor atribúyelo a **Jhusef Alfonso López Parra**.
