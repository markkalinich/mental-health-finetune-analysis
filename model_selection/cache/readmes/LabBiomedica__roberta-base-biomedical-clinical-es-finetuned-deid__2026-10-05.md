---
language:
  - es
license: apache-2.0
tags:
  - token-classification
  - ner
  - de-identification
  - clinical-nlp
  - biomedical
  - spanish
  - roberta
  - finetuned
pipeline_tag: token-classification
metrics:
  - f1
  - precision
  - recall
widget:
  - text: "La paciente María López, residente en Medellín, fue atendida por el Dr. Ramírez, médico internista."
    example_title: De-identification example
---

# LabBiomedica/roberta-base-biomedical-clinical-es-finetuned-deid

A named entity recognition (NER) model fine-tuned for the **automatic de-identification of clinical records** in Spanish. It detects and labels personally identifiable information (PII) in clinical text using BIO tagging scheme.

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
- [Evaluation](#evaluation)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Citation information](#citation-information)

</details>

---

## Model description

This model was fine-tuned from [`PlanTL-GOB-ES/roberta-base-biomedical-clinical-es`](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es), a RoBERTa language model pre-trained on biomedical and clinical texts in Spanish.

Fine-tuning was performed on **real clinical records from maternal patients** at the Clínica Universitaria Bolivariana (Medellín, Colombia), making this a clinical de-identification model trained on free-text real word data in the colombian context.

The model classifies tokens using the **BIO** (Beginning – Inside – Outside) scheme for the following entity categories:

| Label | Description |
|---|---|
| `B-NAME` | Beginning of a person's name |
| `I-NAME` | Inside/continuation of a person's name |
| `B-PROFESSION` | Beginning of a profession or occupation |
| `I-PROFESSION` | Inside/continuation of a profession or occupation |
| `B-LOCATION` | Beginning of a geographic location |
| `I-LOCATION` | Inside/continuation of a geographic location |
| `O` | Token outside any entity |

---


## How to use

```python
from transformers import pipeline

deid = pipeline(
    "token-classification",
    model="LabBiomedica/roberta-base-biomedical-clinical-es-finetuned-deid",
    aggregation_strategy="simple"
)

text = "La paciente María López, residente en Medellín, fue atendida por el Dr. Ramírez, médico internista."
result = deid(text)
print(result)
```

### Example output

```python
[
  {'entity_group': 'NAME', 'score': 0.995, 'word': ' María López', 'start': 12, 'end': 23}, 
  {'entity_group': 'LOCATION', 'score':  0.995, 'word': ' Medellín', 'start': 38, 'end': 46}, 
  {'entity_group': 'PROFESSION', 'score': 0.892, 'word': ' Dr.', 'start': 68, 'end': 71},
  {'entity_group': 'NAME', 'score': 0.962, 'word': ' Ramírez', 'start': 72, 'end': 79},
  {'entity_group': 'PROFESSION', 'score': 0.815, 'word': ' médico internista', 'start': 81, 'end': 98}
]
```

---

## Limitations and bias

- **Institutional coverage:** Trained exclusively on data from a single Colombian institution. Performance may vary across other institutions, countries, or medical specialties.
- **PII category coverage:** Does not cover all sensitive categories (dates, ID numbers, phone numbers, etc.). Combining this model with pattern-based rules is recommended for more complete de-identification.
- **Domain bias:** The corpus reflects a local clinical narrative style (obstetric/maternal-perinatal); texts with significantly different writing styles may yield lower performance.
- **Human oversight:** Should not be used as the sole de-identification mechanism in production environments without additional human validation.

---

## Training

### Training data

The corpus consists of real clinical records from maternal patients at the **Clínica Universitaria Bolivariana** (Medellín, Colombia). The data is **not publicly available** due to privacy and health data protection restrictions.

Annotations were performed manually following the BIO scheme for the categories NAME, PROFESSION, and LOCATION.

| Property | Detail |
|---|---|
| **Domain** | Obstetric / maternal-perinatal records |
| **Language** | Spanish |
| **Format** | Free-form clinical narrative text |
| **Region** | Colombia |
| **Access** | Not public (sensitive health data) |

---

## Evaluation

Evaluation performed using multi-seed evaluation. Results reported as mean ± standard deviation:

| Metric | Value |
|---|---|
| Precision | 0.9526 ± 0.0043 |
| Recall | 0.9468 ± 0.0040 |
| F1-Score (macro) | 0.9493 ± 0.0034 |
| F1-Score (micro) | 0.9989 ± 0.0001 |

### Metrics per entity
 
Computed by grouping B- and I- tags for each entity category (support = number of tokens in the test set):
 
| Entity | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| NAME | 0.9440 | 0.9731 | 0.9583 | 1,525 |
| PROFESSION | 0.9613 | 0.9574 | 0.9593 | 2,021 |
| LOCATION | 0.9666 | 0.9082 | 0.9365 | 1,688 |
| O | 0.9995 | 0.9997 | 0.9996 | 465,027 |
 
### Metrics per BIO label
 
| Label | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| B-NAME | 0.9627 | 0.9504 | 0.9565 | 706 |
| I-NAME | 0.9291 | 0.9927 | 0.9599 | 819 |
| B-PROFESSION | 0.9526 | 0.9412 | 0.9468 | 918 |
| I-PROFESSION | 0.9684 | 0.9710 | 0.9697 | 1,103 |
| B-LOCATION | 0.9569 | 0.9235 | 0.9399 | 889 |
| I-LOCATION | 0.9780 | 0.8911 | 0.9325 | 799 |
| O | 0.9995 | 0.9997 | 0.9996 | 465,027 |

---

## Additional information

### Author

This model was developed within two research groups at the **Institución Universitaria ITM** (Medellín, Colombia):

- **GI²B** — Biomedical Research and Innovation Group *(Grupo de Investigación e Innovación Biomédica)*
- **MIRP** — Intelligent Machines and Pattern Recognition Group *(Grupo de Máquinas Inteligentes y Reconocimiento de Patrones)*


### Citation information

If you use this model in your research, please cite it as follows:

```bibtex
```

**Base model:**
> Carrino, C. P., et al. (2022). *Pretrained biomedical language models for clinical NLP in Spanish*.
> [`PlanTL-GOB-ES/roberta-base-biomedical-clinical-es`](https://huggingface.co/PlanTL-GOB-ES/roberta-base-biomedical-clinical-es)