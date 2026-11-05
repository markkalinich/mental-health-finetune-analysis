
---
language: en
license: apache-2.0
tags:
- text-classification
- emotion-classification
- distilbert
- transformers
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# Clasificador de emociones con DistilBERT

## Descripción del modelo

Este modelo realiza clasificación de emociones en texto utilizando un modelo Transformer.

El modelo base utilizado es `distilbert-base-uncased`, una versión ligera de BERT. Sobre este modelo se ha realizado fine-tuning para adaptarlo a una tarea de clasificación multiclase de emociones.

El objetivo del modelo es recibir una frase en inglés y predecir la emoción principal que expresa.

## Emociones clasificadas

El modelo puede clasificar los textos en las siguientes categorías:

- sadness
- joy
- love
- anger
- fear
- surprise

## Dataset utilizado

El modelo ha sido entrenado con el dataset `dair-ai/emotion`, disponible en Hugging Face Datasets.

Este dataset contiene frases en inglés etiquetadas con la emoción que representan. Está dividido en conjuntos de entrenamiento, validación y test.

## Métricas obtenidas

El modelo se ha evaluado utilizando el conjunto de test.

Resultados obtenidos:

- Accuracy: 0.9165
- F1-score: 0.9165660586120851

Estas métricas permiten medir el rendimiento del modelo en textos que no se han utilizado durante el entrenamiento.

## Uso del modelo

```python
from transformers import pipeline

clasificador = pipeline("text-classification", model="Emisgalix/emotion-distilbert-finetuned")
resultado = clasificador("I am very happy today!")
print(resultado)
```

## Limitaciones

Este modelo presenta algunas limitaciones:

- Está entrenado principalmente para textos en inglés.
- Puede fallar con frases en otros idiomas.
- Puede cometer errores con textos irónicos, sarcásticos o ambiguos.
- Solo clasifica una emoción principal por texto.
- El rendimiento puede mejorar si se entrena durante más épocas o con una configuración más avanzada.
- Las predicciones dependen de las clases disponibles en el dataset original.

## Aplicación

Este modelo puede utilizarse como base para aplicaciones de análisis emocional de texto, asistentes conversacionales, análisis de opiniones o sistemas de clasificación automática de mensajes.
