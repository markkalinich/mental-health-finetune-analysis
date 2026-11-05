---
language:
- es
metrics:
- accuracy
- precision
- recall
- f1
base_model:
- cardiffnlp/twitter-xlm-roberta-base-sentiment
pipeline_tag: text-classification
library_name: transformers
tags:
- politics
- sentiment
- argentina
---

# Modelo de Clasificación de Sentimientos - Debate Presidencial Argentina 2023

Este modelo ha sido desarrollado en el marco de la Tesina para obtener el título de ***Licenciatura en Estadística en la Universidad Nacional de Rosario (UNR)***.

**Autores:**  
- Alumna: Natalia Marín
- Director: Mag. Marcos Miguel Prunello




## Descripción

Este modelo está diseñado para clasificar comentarios de diversas redes sociales obtenidos luego del primer debate presidencial en Argentina en el año 2023. Ha sido específicamente ajustado para analizar los comentarios sobre la candidata **Myriam Bregman**.

Para más información, consulte el siguiente enlace: [link](#)

## Detalles del Modelo

- **Modelo base preentrenado:** `cardiffnlp/twitter-xlm-roberta-base-sentiment`
- **Ajuste específico:** El modelo ha sido fine-tuneado para clasificar comentarios sobre la candidata en el contexto de las elecciones presidenciales en Argentina.

#### Métricas Generales
| Métrica   | Valor    |
|-----------|----------|
| Accuracy  | 0.837838 |
| F1 Score  | 0.824761 |
| Precision | 0.812948 |
| Recall    | 0.837838 |

#### Métricas por Clase
| Clase   | Precision | Recall  | F1       | Support |
|---------|-----------|---------|----------|---------|
| Clase 0 | 0.867925  | 0.92    | 0.893204 | 50      |
| Clase 1 | 0.0       | 0.0     | 0.0      | 2       |
| Clase 2 | 0.761905  | 0.727273| 0.744186 | 22      |

#### Matriz de Confusión
|       | Clase 0 | Clase 1 | Clase 2 |
|-------|---------|---------|---------|
| Clase 0 | 46      | 0       | 4       |
| Clase 1 | 1       | 0       | 1       |
| Clase 2 | 6       | 0       | 16      |




## Cargar y Usar el Modelo en Python

A continuación, se muestra un ejemplo de cómo cargar el modelo y su tokenizador, y realizar una predicción de sentimiento en un comentario:

```python
from transformers import XLMRobertaForSequenceClassification, XLMRobertaTokenizer
import torch

# Cargar el modelo y el tokenizador
model_path = "natmarinn/sentimientos bregman"
model = XLMRobertaForSequenceClassification.from_pretrained(model_path)
tokenizer = XLMRobertaTokenizer.from_pretrained(model_path)

# Texto de ejemplo
texto = "Vamos rusa."

# Tokenización
inputs = tokenizer(texto, return_tensors="pt", truncation=True)

# Predicción
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    pred_class = torch.argmax(logits, dim=1).item()

# Mostrar resultado
clases = ["Clase 0", "Clase 1", "Clase 2"]
print(f"El comentario es clasificado como: {clases[pred_class]}")

```


@misc {natalia_marín_2024,
      author       = { {Natalia Marín , Marcos Miguel Prunello} },
      title        = { sentimientos-bregman (Revision 685be08) },
      year         = 2024,
      url          = { https://huggingface.co/natmarinn/sentimientos-bregman },
      doi          = { 10.57967/hf/3433 },
      publisher    = { Hugging Face }
}