---
license: mit
language:
  - es
library_name: transformers
tags:
  - text-classification
  - emotion-detection
  - spanish
  - tiktok
  - sentiment-analysis
  - robertuito
  - social-media
datasets:
  - custom
base_model: pysentimiento/robertuito-base-uncased
pipeline_tag: text-classification
model-index:
  - name: robertuito-emociones-tiktok
    results:
      - task:
          type: text-classification
          name: Emotion Classification
        metrics:
          - type: f1
            value: 0.6275
            name: Macro F1
          - type: accuracy
            value: 0.6778
            name: Accuracy
---

# RoBERTuito — Clasificador de Emociones en Comentarios de TikTok 🎭

Modelo de clasificación de emociones en **comentarios de TikTok en español**, fine-tuneado sobre [RoBERTuito](https://huggingface.co/pysentimiento/robertuito-base-uncased) con técnicas avanzadas de entrenamiento.

## Emociones Detectadas (6 clases)

| ID | Emoción | Descripción |
|:---:|---------|-------------|
| 0 | **Alegría** | Felicidad, humor, satisfacción |
| 1 | **Confianza** | Admiración, aceptación, apoyo |
| 2 | **Miedo** | Preocupación, ansiedad, temor |
| 3 | **Expectación** | Sorpresa + Anticipación (fusionadas) |
| 4 | **Tristeza** | Decepción, melancolía, pena |
| 5 | **Rechazo** | Disgusto + Ira (fusionadas), crítica, aversión |

> Las 6 clases resultan de fusionar 8 emociones originales de la Rueda de Plutchik. Se fusionaron **Sorpresa+Anticipación → Expectación** y **Disgusto+Ira → Rechazo** porque son difíciles de distinguir en texto informal corto.

## Uso Rápido

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="FalexOne/robertuito-emociones-tiktok",
    top_k=None  # Devuelve todas las probabilidades
)

result = classifier("Que bonito video, me encantó! 😍")
print(result)
# [[{'label': 'Alegría', 'score': 0.85}, {'label': 'Confianza', 'score': 0.08}, ...]]
```

### Uso con AutoModel

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("FalexOne/robertuito-emociones-tiktok")
model = AutoModelForSequenceClassification.from_pretrained("FalexOne/robertuito-emociones-tiktok")

text = "Esto da mucho coraje, no es justo 😤"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)

labels = model.config.id2label
for idx, prob in enumerate(probs[0]):
    print(f"  {labels[idx]}: {prob:.4f}")
```

## Métricas de Evaluación

| Métrica | Valor |
|---------|:---:|
| **Macro F1** | **0.6275** |
| **Accuracy** | **0.6778** |
| **Weighted F1** | **0.6769** |
| Macro Precision | 0.6205 |
| Macro Recall | 0.6397 |

### Reporte por Clase

```
              precision    recall  f1-score   support

     Alegría     0.4828    0.5600    0.5185        50
   Confianza     0.6864    0.6378    0.6612       127
       Miedo     0.4500    0.4737    0.4615        19
 Expectación     0.7083    0.5903    0.6439       144
    Tristeza     0.6471    0.7719    0.7040        57
     Rechazo     0.7487    0.8046    0.7756       174

    accuracy                         0.6778       571
```

## Detalles del Entrenamiento

### Datos
- **~2,950 comentarios** etiquetados manualmente por humanos
- **~1,148 pseudo-labels** de alta confianza (self-training)
- **15 temas** de videos de TikTok (deportes, política, entretenimiento, social, etc.)
- Split: 70% train / 15% val / 15% test

### Técnicas de Entrenamiento
| Técnica | Valor | Propósito |
|---------|-------|-----------|
| Focal Loss | γ = 2.0 | Enfoca aprendizaje en ejemplos difíciles |
| Label Smoothing | ε = 0.1 | Previene sobreconfianza |
| Class Weights | Inverso de frecuencia | Compensa desbalance entre clases |
| Cosine LR Schedule | Warmup 10% | Convergencia suave |
| Early Stopping | Patience = 4 | Previene sobreajuste |
| Learning Rate | 2e-5 | — |
| Batch Size | 16 (×2 grad accum) | Effective batch = 32 |
| Max Length | 128 tokens | — |

### Modelo Base
[**RoBERTuito**](https://huggingface.co/pysentimiento/robertuito-base-uncased) — Un modelo RoBERTa pre-entrenado con ~500M tweets en español. Ideal para texto informal de redes sociales ya que entiende jerga, emojis y abreviaciones.

## Limitaciones

- **Optimizado para TikTok**: El modelo fue entrenado con comentarios de TikTok en español mexicano. Puede funcionar con otros textos informales pero el rendimiento será inferior.
- **Texto corto**: Mejor rendimiento con textos de 5-50 palabras (longitud típica de comentarios).
- **Miedo es la clase más difícil** (F1=0.46): Pocos ejemplos de entrenamiento y ambigüedad con Expectación.
- **No detecta sarcasmo**: Comentarios sarcásticos pueden ser clasificados incorrectamente.
- **Sin clase Neutral**: El modelo siempre asigna una emoción. Usar `max_prob < 0.40` como heurística para "sin emoción clara".

## Cita

Si usas este modelo, por favor cita:

```
@misc{robertuito-emociones-tiktok,
  author = {Alex GS},
  title = {RoBERTuito Emociones TikTok: Clasificador de emociones en comentarios de TikTok en español},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/FalexOne/robertuito-emociones-tiktok}
}
```
