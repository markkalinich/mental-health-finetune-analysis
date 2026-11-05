    ---

library_name: transformers
tags: [text-classification, emotion-recognition, spanish, bert]
language: [es]
license: mit
datasets: [alexander1010/expon-emotions-ds]
pipeline_tag: text-classification

---

# Expon Emotions (ES)

Modelo de **clasificación de emociones en español** para el proyecto _Expon_.

- **Modelo:** `alexander1010/expon-emotions`
- **Dataset:** `alexander1010/expon-emotions-ds`
- **Código:** carpeta `/src`

## Uso rápido

```python
from transformers import pipeline
clf = pipeline("text-classification", model="alexander1010/expon-emotions", top_k=None)
print(clf("Me siento motivado para mi exposición."))
```
