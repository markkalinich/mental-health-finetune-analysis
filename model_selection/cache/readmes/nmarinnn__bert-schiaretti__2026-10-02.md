---
language: es
tags:
  - sentiment-analysis
  - text-classification
  - spanish
  - xlm-roberta
license: mit
datasets:
  - custom
metrics:
  - accuracy
  - f1
library_name: transformers
pipeline_tag: text-classification
widget:
  - text: "Vamos schiaretti!"
    example_title: "Ejemplo positivo"
  - text: "el otro día pensaba eso"
    example_title: "Ejemplo neutro"
  - text: "no puede gobernar"
    example_title: "Ejemplo negativo"
model-index:
  - name: bert-schiaretti
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: Custom Spanish Sentiment Dataset
          type: custom
        metrics:
          - type: accuracy
            value: 0.677
          - type: f1
            value: 0.664
architectures:
  - XLMRobertaForSequenceClassification
transformers_version: "4.41.2"
base_model: cardiffnlp/twitter-xlm-roberta-base-sentiment
inference:
  parameters:
    temperature: 1.0
    max_length: 512
    num_return_sequences: 1
---

# BERT-massa - Modelo de Análisis de Sentimientos en Español

Este modelo está basado en XLM-RoBERTa y ha sido fine-tuned para realizar análisis de sentimientos en textos en español en comentarios sobre el candidato en redes sociales durante el primer debate presidencial de Argentina en 2023.

## Rendimiento del Modelo

•⁠  ⁠*Accuracy*: 0.815
•⁠  ⁠*F1 Score*: 0.767
•⁠  ⁠*Precision*: 0.729
•⁠  ⁠*Recall*: 0.814

### Métricas por Clase

| Clase    | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| Negativo | 0.8718    | 0.7234 | 0.7907   | 47      |
| Neutro   | 0.0000    | 0.0000 | 0.0000   | 3       |
| Positivo | 0.6000    | 0.8750 | 0.7119   | 24      |

## Uso del Modelo

Este modelo puede ser utilizado para clasificar el sentimiento de textos en español en tres categorías: negativo, neutro y positivo.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_name = "nmarinnn/bert-schiaretti"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()
    
    class_labels = {0: "negativo", 1: "neutro", 2: "positivo"}
    return class_labels[predicted_class]

# Ejemplo de uso
texto = "Vamos schiaretti!"
sentimiento = predict(texto)
print(f"El sentimiento del texto es: {sentimiento}")
```
 

## Limitaciones

•⁠  ⁠El modelo muestra un rendimiento bajo en la clase "neutro", posiblemente debido a un desbalance en el dataset de entrenamiento.
•⁠  ⁠Se recomienda precaución al interpretar resultados para textos muy cortos o ambiguos.

## Información de Entrenamiento

•⁠  ⁠*Épocas*: 2
•⁠  ⁠*Pasos de entrenamiento*: 148
•⁠  ⁠*Pérdida de entrenamiento*: 0.6209

## Cita

Si utilizas este modelo en tu investigación, por favor cita:


@misc{marinnn2023bertschiaretti,
  author = {Marin, Natalia},
  title = {BERT Bregman - Modelo de Análisis de Sentimientos en Español},
  year = {2023},
  publisher = {HuggingFace},
  journal = {HuggingFace Model Hub},
  howpublished = {\url{https://huggingface.co/nmarinnn/bert-bregman}}
}