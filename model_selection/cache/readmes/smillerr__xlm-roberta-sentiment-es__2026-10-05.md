---
language: es
tags:
- sentiment-analysis
- spanish
- xlm-roberta
- text-classification
license: mit
---

# XLM-RoBERTa para Análisis de Sentimientos en Español

## Descripción

Modelo fine-tuned de `FacebookAI/xlm-roberta-large` para análisis de sentimientos en español.

## Etiquetas

- **LABEL_0**: NEUTRAL 😐
- **LABEL_1**: POSITIVO 😊
- **LABEL_2**: NEGATIVO 😞

## Uso

```python
from transformers import pipeline
import re

# Función de preprocesamiento
def procesar_texto(texto):
    texto = str(texto)
    texto = re.sub(r"http\S+", " ", texto)
    texto = re.sub(r"@\w+", " ", texto)
    texto = re.sub(r"#(\w+)", r"\1", texto)
    texto = re.sub(r"[^\w\sáéíóúÁÉÍÓÚñÑ!?¿¡]", " ", texto)
    texto = re.sub(r'\s+', ' ', texto.lower().strip())
    return texto

# Cargar modelo
classifier = pipeline(
    "text-classification",
    model="smillerr/xlm-roberta-sentiment-es",
    return_all_scores=False
)

# Ejemplo de uso
texto = "Me encanta este producto!"
texto_limpio = procesar_texto(texto)
resultado = classifier(texto_limpio)
print(resultado)
```

## Ejemplo de salida

```python
[{'label': 'LABEL_1', 'score': 0.9543}]
```

## Modelo Base

- **Base**: FacebookAI/xlm-roberta-large
- **Task**: Text Classification (3 clases)
- **Language**: Spanish

## Preprocesamiento

⚠️ **Importante**: Los textos deben ser preprocesados antes de clasificar para obtener mejores resultados.

## Contacto

- **Autor**: smillerr
- **Repositorio**: https://huggingface.co/smillerr/xlm-roberta-sentiment-es
