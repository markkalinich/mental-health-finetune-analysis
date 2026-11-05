---
language:
- es
base_model:
- distilbert/distilbert-base-uncased
tags:
- sentiment-analysis
- imdb
- distilbert
- huggingface
metrics:
- accuracy
- f1
- precision
- recall
---
# Modelo de Análisis de Sentimiento IMDb - DistilBERT

Este modelo ha sido entrenado para la tarea de análisis de sentimiento sobre reseñas de películas del dataset IMDb.

## Arquitectura
- **Modelo base:** distilbert-base-uncased (de Hugging Face Transformers)
- **Tarea:** Clasificación binaria (positivo/negativo)
- **Tokenizador:** DistilBERT uncased

## Datos de entrenamiento
- **Dataset:** IMDb (25,000 reseñas de películas)
- **Split:** 60% entrenamiento, 40% validación
- **Test:** 25,000 ejemplos (conjunto original de test)

## Proceso de entrenamiento
- **Épocas:** 3
- **Batch size:** 16
- **Optimización:** AdamW, weight decay 0.01
- **Warmup steps:** 500
- **Métricas:** Accuracy, F1, Precision, Recall
- **Hardware:** Entrenado en GPU (NVIDIA GeForce GTX 960M)

## Uso
Puedes cargar este modelo con Hugging Face Transformers:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("juancmamacias/jd-jcms")
model = AutoModelForSequenceClassification.from_pretrained("juancmamacias/jd-jcms")
```

## Autor
- Juan Domingo ([GitHub](https://github.com/jdomdev))
- Juan Carlos Macías ([GitHub](https://github.com/juancmacias))

## Notas
- El modelo es adecuado para tareas de análisis de sentimiento en inglés.

