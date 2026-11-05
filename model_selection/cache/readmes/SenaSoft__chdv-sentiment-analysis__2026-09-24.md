---
base_model: nlptown/bert-base-multilingual-uncased-sentiment
library_name: peft
tags:
- base_model:adapter:nlptown/bert-base-multilingual-uncased-sentiment
- lora
- transformers
- sentiment-analysis
- spanish
- social-media
- text-classification
datasets:
- pyupeu/social-media-peruvian-sentiment
metrics:
- accuracy
---

# SenaSoft/chdv-sentiment-analysis

Este modelo es una adaptación de `nlptown/bert-base-multilingual-uncased-sentiment` entrenado con **LoRA** para la tarea de **análisis de sentimiento** en textos en español.  
Fue ajustado específicamente en un dataset de publicaciones en redes sociales peruanas con 3 etiquetas: **negativo, neutral y positivo**.

---

## Model Details

### Model Description
- **Autores:** Christopher Aponte y David Navarro  
- **Modelo base:** [nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)  
- **Tipo de modelo:** Clasificación de secuencias (sentiment analysis)  
- **Idiomas:** Multilingual  
- **Tarea:** Análisis de sentimiento en textos cortos (ej. redes sociales)  
- **License:** Apache 2.0  
- **Finetuned from:** `nlptown/bert-base-multilingual-uncased-sentiment`

### Model Sources
- **Repository:** [Hugging Face Hub](https://huggingface.co/SenaSoft/chdv-sentiment-analysis)  
- **Dataset:** [pyupeu/social-media-peruvian-sentiment](https://huggingface.co/datasets/pyupeu/social-media-peruvian-sentiment)

---

## Uses

### Direct Use
Este modelo puede usarse directamente para clasificar textos en español en **positivo, negativo o neutral**.

Ejemplos de uso:
```python
from transformers import pipeline

clasificador = pipeline(
    "sentiment-analysis",
    model="SenaSoft/chdv-sentiment-analysis"
)

print(clasificador("Me encanta la sopa"))  
# [{'label': 'positivo', 'score': 0.85}]

print(clasificador("No me gusta nada la sopa"))  
# [{'label': 'negativo', 'score': 0.89}]

print(clasificador("La sopa está bien, pero prefiero otra cosa"))  
# [{'label': 'neutral', 'score': 0.39}]
```

### Downstream Use
Puede integrarse en:
- Plataformas de monitoreo de redes sociales.  
- Sistemas de atención al cliente.  
- Análisis de feedback de usuarios.  

### Out-of-Scope Use
- No está entrenado para otros idiomas distintos al español, pero el modelo base sí.  
- No es un detector de sarcasmo ni de sentimientos complejos como miedo o sorpresa.  
- No debe usarse en contextos médicos, legales o financieros sin verificación adicional.  

---

## Bias, Risks, and Limitations
- Entrenado con un dataset específico (Perú, redes sociales). Puede no generalizar igual en otros países o contextos.  
- Riesgo de sesgo cultural y lingüístico.  
- Puede fallar en casos de ironía, sarcasmo o ambigüedad semántica.  

### Recommendations
- Se recomienda evaluar antes de usar en producción fuera de su dominio.  
- Puede complementarse con técnicas de **ensembles** o datasets más diversos.  

---

## Training Details

### Training Data
Dataset: [pyupeu/social-media-peruvian-sentiment](https://huggingface.co/datasets/pyupeu/social-media-peruvian-sentiment)  
Etiquetas:  
- `0`: negativo  
- `1`: neutral  
- `2`: positivo  

### Training Procedure

#### Preprocessing
- Textos truncados y/o rellenados a `max_length=128`.  
- Tokenización con `AutoTokenizer` de `bert-base-multilingual-uncased-sentiment`.  

#### Training Hyperparameters
- **LoRA Config:**  
  - `r=8`  
  - `lora_alpha=16`  
  - `lora_dropout=0.7`  
- **TrainingArguments:**  
  - `batch_size=16`  
  - `num_train_epochs=20`  
  - `learning_rate=5e-5`  
  - `weight_decay=0.01`  
  - `eval_strategy="epoch"`  
  - `save_strategy="epoch"`  
  - `load_best_model_at_end=True`  
  - `metric_for_best_model="accuracy"`  

#### Speeds, Sizes, Times
- Número de épocas: 20  
- Mejor resultado en **epoch 15**  
- Checkpoint tamaño aproximado: ~420 MB  

---

## Evaluation

### Testing Data
Dataset de prueba del mismo `pyupeu/social-media-peruvian-sentiment`.

### Metrics
- **Accuracy**: 0.66  
- **Training Loss (epoch 15):** 0.722  
- **Validation Loss (epoch 15):** 0.785  

### Results
- Mejor rendimiento alcanzado en epoch 15.  
- Buen ajuste considerando dataset pequeño y dominio específico.  

---

## Environmental Impact
- **Hardware:** NVIDIA GPU (única)  
- **Tiempo de entrenamiento:** ~2 horas  
- **Cloud Provider:** Local / Dockerizado  
- **Carbon Emitted:** No estimado  

---

## Technical Specifications

### Model Architecture and Objective
- Modelo base: BERT Multilingüe (`uncased`)  
- Objetivo: clasificación en 3 clases  
- Técnica usada: Fine-tuning con LoRA  

### Compute Infrastructure
- **Hardware:** GPU local  
- **Software:**  
  - Python 3.10+  
  - Transformers 4.56.1  
  - PEFT 0.17.1  
  - Datasets 3.0.2  

---

## Citation

**BibTeX**
```bibtex
@misc{aponte2025chdv,
  title={SenaSoft CHDV Sentiment Analysis},
  author={Aponte, Christopher and Navarro, David},
  year={2025},
  howpublished={Hugging Face},
  url={https://huggingface.co/SenaSoft/chdv-sentiment-analysis}
}
```

**APA**
Aponte, C., & Navarro, D. (2025). *SenaSoft CHDV Sentiment Analysis* [Model]. Hugging Face. https://huggingface.co/SenaSoft/chdv-sentiment-analysis

---

## Model Card Authors
Christopher Aponte y David Navarro

## Model Card Contact
Para consultas: [Christopher Aponte & David Navarro, SenaSoft 2025]  

---

### Framework versions
- **PEFT:** 0.17.1  
- **Transformers:** 4.56.1  
- **Datasets:** 3.0.2  
