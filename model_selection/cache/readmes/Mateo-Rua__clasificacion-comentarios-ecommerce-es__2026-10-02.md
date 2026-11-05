---
language:
  - es
license: apache-2.0
base_model: distilbert/distilbert-base-multilingual-cased
pipeline_tag: text-classification
datasets:
  - SetFit/amazon_reviews_multi_es
metrics:
  - f1
  - accuracy
tags:
  - sentiment-analysis
  - e-commerce
  - spanish
  - reviews
  - customer-feedback
widget:
  - text: "Excelente producto, llegó antes de lo esperado y muy bien empacado"
  - text: "El producto está bien pero el envío tardó demasiado"
  - text: "Pésima calidad, se dañó a la semana de uso. No lo recomiendo"
---

# 🛒 Clasificador de Sentimiento para Reseñas de E-commerce en Español

Modelo de análisis de sentimiento **especializado en comentarios post-compra de 
comercio electrónico en español** — el tipo de reseñas que reciben plataformas 
como Mercado Libre, Falabella, Éxito o Amazon México: opiniones sobre calidad 
del producto, tiempos de envío, empaque y atención del vendedor.

Clasifica cada reseña en **3 clases accionables**:

| Clase | Significado para el negocio |
|---|---|
| 😠 `negativo` | Cliente insatisfecho — requiere atención prioritaria |
| 😐 `neutro` | Experiencia aceptable — oportunidad de mejora |
| 😊 `positivo` | Cliente satisfecho |

## 💼 Casos de uso

- **Detección temprana de clientes insatisfechos** antes de que escalen a reclamos
- **Monitoreo de reputación** de vendedores y productos a escala
- **Dashboards de experiencia del cliente** con señal cuantificable de sentimiento
- **Priorización de moderación** para equipos de atención

## 🚀 Uso

​```python
from transformers import pipeline

clasificador = pipeline(
    "text-classification",
    model="Mateo-Rua/sentimiento-ecommerce-es"
)

clasificador("Excelente producto, llegó antes de lo esperado")
# [{'label': 'positivo', 'score': 0.98}]
​```

## 📊 Rendimiento (split de test, nunca visto en entrenamiento)

| Métrica | Valor |
|---|---|
| **F1 macro** | **0.697** |
| Accuracy | 0.730 |
| Precision macro | 0.703 |
| Recall macro | 0.701 |

### Por clase


| Clase | Precision | Recall | F1 | Soporte |
|---|---|---|---|---|
| Negativo | 0.8225 | 0.7645 | 0.7924 | 2000 |
| Neutro | 0.4138 | 0.5570 | 0.4749 | 1000 |
| Positivo | 0.8713 | 0.7820 | 0.8242 | 2000 |

El modelo distingue con solidez positivo vs negativo (F1 ~0.80). La clase neutra 
concentra los errores por su ambigüedad inherente — una reseña de 3⭐ mezcla señales 
de ambos polos — aunque los class weights lograron un recall de 0.56 que sin balanceo 
sería drásticamente menor. El análisis de errores reveló además ruido de etiquetas en 
el dataset (reseñas con texto positivo y calificación negativa), un techo natural 
para cualquier modelo en esta tarea.

## 🔧 Entrenamiento

- **Base:** `distilbert-base-multilingual-cased` (fine-tuning completo)
- **Datos:** 30.000 reseñas en español de [SetFit/amazon_reviews_multi_es](https://huggingface.co/datasets/SetFit/amazon_reviews_multi_es), 
  usadas como proxy del lenguaje de reseñas en plataformas latinoamericanas. 
  Mapeo: 1-2⭐ → negativo · 3⭐ → neutro · 4-5⭐ → positivo
- **Desbalance:** tratado con class weights (`[0.84, 1.66, 0.83]`) en la CrossEntropy 
  mediante un `Trainer` personalizado — la clase neutra (minoritaria 2:1) pesa el doble
- **Configuración:** 3 épocas, batch 16, warmup 500 steps, weight decay 0.01
- **Selección de modelo:** mejor checkpoint por F1 macro en validation 
  (`load_best_model_at_end`), evaluación final única sobre test
- **Reproducibilidad:** seed 42 · Notebook completo de entrenamiento incluido en este repo 📓

## ⚠️ Limitaciones

- La clase **neutro** es inherentemente ambigua (una reseña de 3⭐ mezcla señales 
  positivas y negativas) y concentra la mayoría de los errores del modelo
- Entrenado con reseñas de productos: puede rendir peor en otros dominios 
  (restaurantes, servicios, redes sociales)
- Solo español; para portugués (Brasil) se recomienda re-entrenar con datos en pt
- Las señales de sarcasmo e ironía son difíciles de capturar

## Autor

**Mateo Rúa** — Data Scientist · Medellín, Colombia  
[GitHub](https://github.com/Mateo-Rua) · [LinkedIn](https://www.linkedin.com/in/mateo-londono-rua117) · [Hugging Face](https://huggingface.co/Mateo-Rua)
​```

**Detalles que trae la card:**

1. **`widget:` en el YAML** → HF pone un probador interactivo en la página del modelo con tus frases de ejemplo (¡la gente puede testearlo sin código!).
2. **Metadatos completos** → dataset linkeado, métricas declaradas, tags de búsqueda (e-commerce, spanish, reviews).
3. **Enfoque comercial** → mismo tono del notebook: casos de uso de negocio primero.
4. **Sección de limitaciones honesta** → paradójicamente, es lo que más profesionalismo transmite.
