---
language:
- es
license: mit
tags:
- text-classification
- sentiment-analysis
- reviews
- distilbert
- spanish
datasets:
- amazon_reviews_multi
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: distilbert-review_classification
  results:
  - task:
      type: text-classification
      name: Clasificación de reseñas (5 clases)
    dataset:
      name: amazon_reviews_multi (español)
      type: amazon_reviews_multi
    metrics:
      - type: accuracy
        value: 0.5808
      - type: f1
        value: 0.58158
pipeline_tag: text-classification
widget:
- text: "Este producto es increíble, funciona perfectamente y el precio es excelente."
- text: "La calidad del producto deja mucho que desear y llegó con un retraso considerable."
---

# distilbert-review_classification

Este modelo es una variante de DistilBERT entrenada para la clasificación de reseñas de Amazon en español. Está basado en `distilbert-base-multilingual` y ha sido afinado para predecir calificaciones de estrellas (1-5) a partir del texto de la reseña.

## Modelo

**Arquitectura base:** DistilBERT (distilbert-base-multilingual)  
**Tarea:** Clasificación de texto (5 clases)  
**Idioma:** Español  
**Caso de uso:** Análisis de sentimiento y clasificación de reseñas

## Rendimiento

El modelo fue evaluado en un conjunto de datos balanceado con 1000 muestras para cada clase (calificación de 1 a 5 estrellas):

| Métrica | Valor |
|---------|-------|
| Exactitud (Accuracy) | 0.5808 |
| F1 Score (macro promedio) | 0.58158 |
| Precisión (macro promedio) | 0.58303 |
| Recall (macro promedio) | 0.5808 |

### Rendimiento por clase

| Clase | Precisión | Recall | F1 Score | Soporte |
|-------|-----------|--------|----------|---------|
| 1 ⭐ | 0.72069 | 0.707 | 0.71378 | 1000 |
| 2 ⭐ | 0.50409 | 0.554 | 0.52787 | 1000 |
| 3 ⭐ | 0.48916 | 0.474 | 0.48146 | 1000 |
| 4 ⭐ | 0.51613 | 0.512 | 0.51406 | 1000 |
| 5 ⭐ | 0.68509 | 0.657 | 0.67075 | 1000 |

## Detalles de entrenamiento

* **Epochs:** 1
* **Pasos de entrenamiento:** 50,000
* **Tiempo de entrenamiento:** ~8.2 horas (29,486 segundos)
* **Loss final:** 0.9721

## Uso

```python
from transformers import pipeline

# Crear el pipeline de clasificación
clasificador = pipeline(
    "text-classification",
    model="polodealvarado/distilbert-review_classification",
    tokenizer="polodealvarado/distilbert-review_classification",
    top_k=1,  # Solo la clase más probable
)

# Texto de entrada
texto = "Este producto superó mis expectativas, lo recomiendo totalmente."

# Realizar predicción
output = clasificador(texto)

# Extraer la clase predicha (por ejemplo, 'LABEL_0', 'LABEL_1', ...)
etiqueta = output[0][0]["label"]
indice = int(etiqueta.replace("LABEL_", ""))  # 'LABEL_0' → 0
estrellas_predichas = indice + 1

print(f"Predicción: {estrellas_predichas} estrellas")
```

## Limitaciones

- El modelo fue entrenado con datos de reseñas de Amazon, por lo que puede tener un rendimiento reducido en otros dominios.
- El rendimiento es más alto para reseñas claramente positivas (5 estrellas) o claramente negativas (1 estrella), mientras que las clasificaciones intermedias (2-4 estrellas) muestran un rendimiento más modesto.
