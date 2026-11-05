
---
language: en
license: apache-2.0
tags:
- text-classification
- emotion-detection
- distilbert
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# Emotion Classifier

## Descripcion
Modelo de clasificacion de emociones en texto en ingles basado en DistilBERT.
Fine-tuneado sobre el dataset dair-ai/emotion para detectar 6 emociones distintas.

## Uso

```python
from transformers import pipeline

clasificador = pipeline("text-classification", model="JuanmaPalacios/emotion-classifier-en")
resultado = clasificador("I am so happy today!")
print(resultado)
```

## Etiquetas
- sadness: Tristeza
- joy: Alegria
- love: Amor
- anger: Enfado
- fear: Miedo
- surprise: Sorpresa

## Metricas obtenidas en test
- Accuracy: 0.9160
- F1 weighted: 0.9141
- Precision weighted: 0.9160
- Recall weighted: 0.9160

## Limitaciones
- Solo funciona con texto en ingles
- Entrenado con tweets, puede no generalizar a textos formales
- Entrenado con un subconjunto de 3000 ejemplos para agilizar el proceso
