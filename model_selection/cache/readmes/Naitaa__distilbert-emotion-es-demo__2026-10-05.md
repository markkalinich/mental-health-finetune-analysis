---
language: en
license: apache-2.0
library_name: transformers
tags:
- text-classification
- emotion
- distilbert
- fine-tuned
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
base_model: distilbert-base-uncased
pipeline_tag: text-classification
widget:
- text: "I just got promoted at work, I can't stop smiling!"
- text: "I miss my grandmother so much, the house feels empty."
- text: "How dare he speak to me like that, I'm furious."
---

# distilbert-emotion-es-demo

Fine-tuning de **`distilbert-base-uncased`** sobre el dataset [`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion)
para clasificación de emociones en texto en inglés (6 clases).

## Etiquetas

`sadness (0)`, `joy (1)`, `love (2)`, `anger (3)`, `fear (4)`, `surprise (5)`.

## Uso

```python
from transformers import pipeline
clf = pipeline("text-classification", model="Naitaa/distilbert-emotion-es-demo", top_k=None)
clf("I'm so happy today!")
```

## Datos de entrenamiento

- Dataset: `dair-ai/emotion` (split `split`).
- Subset usado en este proyecto: **4000 train / 800 validation / 1000 test**.
- Tokenización: `distilbert-base-uncased`, `max_length=64`.

## Hiperparámetros

- Optimizer: AdamW
- Learning rate: 2e-5
- Weight decay: 0.01
- Warmup ratio: 0.1
- Batch size (train/eval): 32 / 64
- Epochs: 3
- Seed: 42
- Precisión mixta (fp16): habilitada si hay GPU

## Métricas en test

| Métrica       | Valor    |
|---------------|----------|
| accuracy      | 0.8690 |
| f1 macro      | 0.7201 |
| f1 weighted   | 0.8565 |

## Limitaciones y consideraciones éticas

- Entrenado sólo en **inglés**, no funcionará bien con otros idiomas.
- El dataset `dair-ai/emotion` proviene de tweets y contiene sesgos demográficos y lingüísticos propios de esa plataforma.
- Sólo 6 emociones — emociones fuera de esas clases serán forzadas a la más cercana.
- Subset reducido → métricas no son state-of-the-art; es un proyecto **demostrativo**.
- No usar para decisiones críticas (salud mental, RRHH, contenido sensible).

## Reproducción

Ver el notebook `Proyecto_Hugging_Face.ipynb` para el pipeline completo.
