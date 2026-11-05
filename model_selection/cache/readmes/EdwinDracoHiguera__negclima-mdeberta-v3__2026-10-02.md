---
language: es
license: mit
base_model: microsoft/mdeberta-v3-base
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - organizational-climate
  - human-resources
  - spanish
widget:
  - text: "Mejorar el sueldo."
  - text: "El campus es maravilloso y mis compañeros son un gran equipo."
  - text: "Más espacios de integración entre áreas."
---

# NegClima · mDeBERTa-v3 para clima organizacional en español

Clasificador de sentimiento de tres clases (NEGATIVE / NEUTRAL / POSITIVE) para
respuestas abiertas de encuestas de clima laboral en español, con énfasis en la
**negatividad implícita**: quejas redactadas como sugerencias ("Mejorar el
sueldo", "Que los jefes escuchen a su equipo"), que los clasificadores
zero-shot y los LLMs de frontera clasifican mal de forma sistemática.

## Datos de entrenamiento

Encuesta institucional de clima laboral de una universidad colombiana
(personal docente y administrativo), dos preguntas abiertas segmentadas en
oraciones (NLTK, español). 6.204 oraciones etiquetadas; splits 70/10/20
estratificados y **agrupados por respuesta original** (ninguna oración de una
misma respuesta cruza splits — protocolo sin fuga de datos).

## Rendimiento (test limpio, n = 1.244)

| Métrica | Valor |
|---|---|
| Accuracy | 0,866 [IC 95%: 0,847–0,884] |
| F1-macro | 0,798 [0,772–0,824] |
| F1 NEGATIVE / NEUTRAL / POSITIVE | 0,858 / 0,590 / 0,946 |
| ROC-AUC macro (OvR) | 0,945 |

Frente a LLMs de frontera zero-shot sobre el mismo test: paridad en accuracy
pero **+0,17 a +0,20 de F1-macro** (bootstrap pareado, p < 0,001); los LLMs
colapsan en la clase NEUTRAL (F1 0,079 y 0,012).

## Uso

```python
from transformers import pipeline
clf = pipeline("text-classification", model="EdwinDracoHiguera/negclima-mdeberta-v3")
clf("Mejorar el sueldo.")
# [{'label': 'NEGATIVE', 'score': ...}]
```

Demo interactiva para equipos de RRHH: https://main.dqlpgutcvit7x.amplifyapp.com

## Limitaciones

- Un solo dominio e institución (universidad colombiana); la generalización a
  otros sectores no está validada.
- NEUTRAL es la clase más difícil (F1 0,590); parte de la ambigüedad
  NEUTRAL↔NEGATIVE es genuina incluso para anotadores humanos.
- Parte de las etiquetas de la pregunta positiva proviene de un ensamble NLI
  validado contra 206 etiquetas humanas (acuerdo 96,6%).

## Cita

Artículo en preparación (actualización de Higuera, López-Pazmino y
Moscoso-Barrera, *Implementation of an Artificial Intelligence Model for the
Automatic Diagnosis of Organizational Climate Using Sentiment Analysis*).
