
---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- finance
- distilbert
datasets:
- FinanceMTEB/financial_phrasebank
metrics:
- accuracy
pipeline_tag: text-classification
---

# Modelo de Análisis de Sentimientos Financieros

## Descripción
Modelo de clasificación de sentimientos (Positivo, Negativo, Neutral) basado en DistilBERT.
Entrenado como proyecto práctico de Fine-Tuning y Despliegue.

## Uso
```python
from transformers import pipeline
clasificador = pipeline("text-classification", model="afcfdsa/finanzas-analisis-sentimiento")
resultado = clasificador("The company reported a profit of $5 million.")
print(resultado)

## Limitaciones
Entrenado con un subconjunto reducido de financial_phrasebank (400 ejemplos) 
únicamente para propósitos de demostración educativa. No usar para tomar decisiones reales de inversión.
