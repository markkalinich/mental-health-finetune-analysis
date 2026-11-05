---
language:
- en
metrics:
- precision
- recall
- f1-score
- support
base_model:
- google-bert/bert-base-uncased
tags:
- medical
- NER
- healthcare
library_name: transformers
---
# Model Card for Medical NER Model

This model is a high-performance Named Entity Recognition (NER) model designed specifically for medical text. It identifies entities such as diseases, symptoms, procedures, medications, and healthcare providers with high precision and recall, making it ideal for clinical and healthcare applications.


### Model Description


- **Model type:** Named Entity Recognition (NER)
- **Language(s) (NLP):** English (en)
- **Finetuned from model :** google-bert/bert-base-uncased

This model has been fine-tuned on a medical dataset to achieve high accuracy in extracting key entities from healthcare documents.

## Uses

### Direct Use

This model is intended for extracting medical entities from clinical or healthcare-related text. It can be used for:
- Automating medical document analysis.
- Structuring unstructured healthcare data.
- Supporting healthcare AI applications.

### Downstream Use 

The model can be further fine-tuned for:
- Specific medical subdomains.
- Entity classification in multi-lingual healthcare datasets.

### Out-of-Scope Use

This model is not designed for:
- General NER tasks outside the healthcare domain.
- Identifying non-medical entities or handling multi-lingual text without fine-tuning.

## Bias, Risks, and Limitations

### Risks:
- Misclassification of entities in ambiguous or highly noisy text.
- Potential underperformance on unseen medical terms or rare conditions.

### Limitations:
- The model is optimized for English and may not perform well on other languages.
- It requires clean text inputs with minimal OCR errors for best performance.

### Recommendations
Users should validate extracted entities before use in critical applications, such as medical decision-making.

## How to Get Started with the Model

```python
from transformers import pipeline

# Load the model
ner_pipeline = pipeline("ner", model="samant/medical-ner")

# Example usage
text = "The patient has been diagnosed with Type 2 Diabetes and prescribed Metformin."
entities = ner_pipeline(text)
print(entities)