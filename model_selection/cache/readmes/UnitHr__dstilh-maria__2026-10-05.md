---
language: es
license: mit
tags:
  - roberta
  - text-classification
  - spanish
  - sentiment-analysis
pipeline_tag: text-classification
---

# MarIA fine-tuned for Sentiment Classification (DSTILH)

Este modelo está basado en **MarIA (RoBERTa-base en español)** y ha sido fine-tuneado para realizar clasificación de sentimientos en español.

## Detalles del modelo

- Arquitectura: `RobertaForSequenceClassification`
- Número de clases: 3
  - `LABEL_0`: negativo
  - `LABEL_1`: neutro
  - `LABEL_2`: positivo

## Uso

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("UnitHr/dstilh-maria")
model = AutoModelForSequenceClassification.from_pretrained("UnitHr/dstilh-maria")

inputs = tokenizer("Este medicamento me sentó fatal", return_tensors="pt")
outputs = model(**inputs)
