---
license: mit
language:
- es
metrics:
- f1
- accuracy
base_model:
- dccuchile/bert-base-spanish-wwm-cased
pipeline_tag: text-classification
library_name: transformers
tags:
- text-classification
- steam
- reviews
- beto
- pytorch
- sentiment-analysis
---

# Modelo de Análisis de Sentimiento para Reseñas de Steam (BETO)

Este modelo es una versión ajustada (fine-tuned) del modelo [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) (BERT en español).

Ha sido entrenado para clasificar reseñas de videojuegos de la plataforma **Steam** en dos categorías:
* **LABEL_1**: Recomendado (Positivo)
* **LABEL_0**: No Recomendado (Negativo)

## Descripción del Proyecto
El objetivo era adaptar un modelo de lenguaje generalista (BETO) al lenguaje específico y coloquial de los "gamers" en español. El modelo ha sido entrenado con un dataset de aproximadamente 1.000 reseñas reales del juego Counter Strike 2. Por ello, es posible que a la hora de ser probado en juegos de distinto género, no funcione del todo bien.

## Métricas de Evaluación (Set de Validación)
El modelo alcanzó los siguientes resultados durante el entrenamiento:
* **F1-Score**: 0.849
* **Accuracy**: 0.857
* **Loss**: 0.35

## Cómo usarlo (Inferencia)

Puedes usar este modelo directamente con la librería `transformers`, además de tener instalado `torch`. También se recomienda, aunque no es necesario, instalar `accelerate` y `numpy`:

```python
from transformers import pipeline

# Cargar el pipeline
clasificador = pipeline("text-classification", model="kanowest/beto-steam-reviews")

# Probar con una frase
texto = "El juego tiene buenos gráficos pero la historia es aburrida."
resultado = clasificador(texto)

print(resultado)
# Salida esperada: [{'label': 'LABEL_0', 'score': 0.99...}]
```

## Comentarios adicionales

Hice una prueba con un dataset del Team Fortress 2 y no salió todo lo bien que me esperaba. Falla bastante a la hora de reconocer reseñas negativas (más de lo que me imaginaba que fallaría). Es mi primer modelo y, por tanto, no ha salido demasiado bien. Mi plan es crear uno que funcione mejor en el futuro.