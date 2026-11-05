
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
pipeline_tag: text-classification
---

# Modelo de Análisis de Sentimientos

## Descripción
Modelo de clasificación de sentimientos (positivo/negativo) basado en DistilBERT,
creado durante la **Sesión 4 del curso de IA con Hugging Face**.

## Uso

```python
from transformers import pipeline

clasificador = pipeline("text-classification", model="migracia/mi-modelo-sentimientos")
resultado = clasificador("I love this course!")
print(resultado)
```

## Etiquetas
- POSITIVE: Sentimiento positivo
- NEGATIVE: Sentimiento negativo
## Limitaciones
- Solo funciona con texto en inglés
- Entrenado con reseñas de cine (SST-2), puede no generalizar a otros dominios
