---
language: es
license: apache-2.0
library_name: transformers
tags:
  - sentiment-analysis
  - text-classification
  - spanish
  - tweets
  - beto
datasets:
  - cardiffnlp/tweet_sentiment_multilingual
metrics:
  - accuracy
  - f1
base_model: dccuchile/bert-base-spanish-wwm-cased
pipeline_tag: text-classification
---

# BETO Sentiment ES — Tweets

Clasificador de polaridad afectiva en español (3 clases: `negative`, `neutral`, `positive`) obtenido haciendo *fine-tuning* de [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) sobre el subconjunto en español de [`cardiffnlp/tweet_sentiment_multilingual`](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual).

## Uso rápido

```python
from transformers import pipeline
clf = pipeline("text-classification", model="lbryanrick/beto-sentiment-es-tweets")
clf("La película me pareció maravillosa, muy recomendada.")
# -> [{'label': 'positive', 'score': 0.97}]
```

## Datos

- **Dataset:** `cardiffnlp/tweet_sentiment_multilingual` (split `spanish`)
- **Entrenamiento:** 1839 ejemplos
- **Validación:** 324 ejemplos
- **Test:** 870 ejemplos (balanceado: 290 por clase)

## Métricas en test

| Métrica   | Valor  |
|-----------|--------|
| Accuracy  | 0.6862 |
| F1 macro  | 0.6859 |

### Por clase

| Clase    | Precision | Recall | F1     |
|----------|-----------|--------|--------|
| negative | 0.6950    | 0.7621 | 0.7270 |
| neutral  | 0.5951    | 0.5828 | 0.5889 |
| positive | 0.7724    | 0.7138 | 0.7419 |

Estos resultados son comparables con el baseline XLM-R reportado en Barbieri et al. (2022) para el split en español del dataset, alcanzado con un modelo más pequeño (BETO base, 110M parámetros) y sin pre-entrenamiento específico de dominio social.

## Limitaciones

- **Dominio**: entrenado sobre tuits. La generalización a otros registros (formal, noticias, reseñas largas, atención al cliente) puede degradarse.
- **Variedad geográfica**: el dataset mezcla español de varias regiones. No se garantiza rendimiento uniforme en cada variedad dialectal.
- **Ironía y sarcasmo**: los clasificadores BERT-base de tres clases sufren con contenido sarcástico, especialmente cuando no hay marcadores explícitos.
- **Ambigüedad neutral / leve polaridad**: la clase neutral concentra los principales errores del modelo (F1 ≈ 0.59), porque muchos textos etiquetados como neutrales contienen carga afectiva leve.
- **Sesgos**: los modelos heredan sesgos del corpus de pre-entrenamiento y del de *fine-tuning*. No usar para decisiones de alto impacto sin evaluación adicional sobre la distribución objetivo.

## Reproducibilidad

Semilla: `42`. Hiperparámetros:

| Hiperparámetro | Valor |
|---|---|
| `learning_rate` | `2e-5` |
| `per_device_train_batch_size` | `16` |
| `num_train_epochs` | `3` |
| `weight_decay` | `0.01` |
| `max_length` | `128` |
| `fp16` | `True` |

## Cita

```bibtex
@inproceedings{CaneteCFP2020,
  title={Spanish Pre-Trained BERT Model and Evaluation Data},
  author={Cañete, José and Chaperon, Gabriel and Fuentes, Rodrigo and Ho, Jou-Hui and Kang, Hojin and Pérez, Jorge},
  booktitle={PML4DC at ICLR 2020},
  year={2020}
}

@inproceedings{barbieri-etal-2022-xlm,
  title={{XLM}-{T}: Multilingual Language Models in {T}witter for Sentiment Analysis and Beyond},
  author={Barbieri, Francesco and Espinosa Anke, Luis and Camacho-Collados, Jose},
  booktitle={Proceedings of LREC},
  year={2022}
}
```