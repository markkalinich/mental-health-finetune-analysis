---
library_name: transformers
license: apache-2.0
language:
- en
base_model: distilbert-base-multilingual-cased
tags:
- generated_from_trainer
- text-classification
- sentiment-analysis
- amazon-reviews
metrics:
- accuracy
- f1
pipeline_tag: text-classification
model-index:
- name: mi-modelo-analisis-sentimiento-apps
  results: []
---

# Clasificador de Estrellas en Reseñas de Productos (DistilBERT Fine-Tuned)

## Descripción
Este modelo es el resultado de un proceso de *Fine-Tuning* sobre la arquitectura **distilbert-base-multilingual-cased**. El objetivo principal es analizar el texto de una reseña de producto en **inglés** y predecir de forma automática la calificación que el usuario le otorgaría en una escala de **1 a 5 estrellas**.

- **Desarrollado por:** Miguel Ángel Sánchez-Medina Camacho (Máster Universitario en Inteligencia Artificial)
- **Idioma:** Inglés. El modelo está optimizado para reseñas en inglés; el uso en otros idiomas puede producir predicciones incorrectas.
- **Dataset base:** Subconjunto balanceado y procesado de `ArpitGarg/labeled_amazon_reviews`.
- **Métricas en evaluación:** Loss: 1.1071 · Accuracy: 0.5347 · F1: 0.5308

## Pipeline
El ciclo de vida del proyecto siguió los siguientes pasos clave:
1. **Preparación de datos:** Descarga, filtrado y balanceo para asegurar **1,500 muestras por cada categoría de estrella**, evitando sesgos en el entrenamiento. Las etiquetas originales (1-5) se mapearon a índices basados en cero (0-4) para compatibilidad con la red neuronal.
2. **Tokenización:** Uso del tokenizador de DistilBERT con truncado a **256 tokens**, permitiendo capturar el contexto completo de reseñas largas sin perder conclusiones o giros semánticos al final del texto. El motivo por el cual elegí DistilBERT Multilingual es por que este es una versión compacta de BERT que mantiene gran parte de su capacidad predictiva reduciendo significativamente el número de parámetros y el tiempo de entrenamiento (que ya es demasaido largo de por sí debido a los limitados recursos hardware de los que dispongo).
3. **Entrenamiento (Fine-Tuning):** Transferencia de aprendizaje durante **5 épocas** con tasa de aprendizaje $2\times 10^{-5}$, regularización L2 (`weight_decay=0.01`) y *warmup* del 10% para estabilizar los gradientes, utilizando `transformers.Trainer`.

## Métricas de Evaluación
La evaluación se realizó sobre un conjunto de test independiente (20% del dataset, equivalente a **1,500 reseñas balanceadas**). Se restauró automáticamente el modelo con mejor validación (`load_best_model_at_end=True`):

| Métrica | Valor obtenido |
| :--- | :--- |
| **Accuracy (Exactitud)** | **0.5347** (53.47%) |
| **F1-Score (Weighted)** | **0.5308** (53.08%) |

*Para un problema de clasificación ordinal de 5 clases, el baseline aleatorio es del 20%. Lograr un 53.47% demuestra que el modelo supera en más de 2.5 veces el rendimiento aleatorio, habiendo aprendido los patrones semánticos asociados a la satisfacción del cliente.*

### Resultados por época

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 375  | 1.2179          | 0.4573   | 0.4264 |
| 1.3842        | 2.0   | 750  | 1.1322          | 0.5073   | 0.5023 |
| 1.0500        | 3.0   | 1125 | 1.1071          | 0.5347   | 0.5308 |
| 0.8402        | 4.0   | 1500 | 1.1412          | 0.5467   | 0.5464 |
| 0.8402        | 5.0   | 1875 | 1.1652          | 0.5493   | 0.5475 |

## Limitaciones y Sesgos
- **Idioma:** Entrenado con reseñas en inglés; otros idiomas pueden producir predicciones incorrectas o poco fiables.
- **Clases fronterizas:** Las reseñas de 2 y 4 estrellas presentan mayor ambigüedad semántica, pudiendo confundirse con las clases adyacentes. Esperable en clasificación ordinal con clases continuas.
- **Sarcasmo y ambigüedad:** Expresiones sarcásticas o reseñas neutras (3 estrellas) que mezclan aspectos positivos y negativos pueden generar predicciones con menor confianza.

## Hiperparámetros de Entrenamiento
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: AdamW con betas=(0.9, 0.999) y epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 5

## Versiones de Frameworks
- Transformers 5.9.0
- PyTorch 2.5.1+cu121
- Datasets 4.8.5
- Tokenizers 0.22.2
