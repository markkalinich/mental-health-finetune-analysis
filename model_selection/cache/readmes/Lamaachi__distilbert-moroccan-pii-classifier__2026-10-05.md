---
language:
- ar
- fr
- en
metrics:
- f1
- recall
- precision
tags:
- ner
- pii
- cv-parsing
- morocco
- distilbert
- token-classification
license: apache-2.0
base_model:
- distilbert/distilbert-base-uncased
pipeline_tag: text-classification
library_name: transformers
---

# 🇲🇦 DistilBERT Moroccan PII & CV Entity Extraction

## Model Details

### Model Description

This model is a fine-tuned version of DistilBERT for **Named Entity Recognition (NER)** focused on **PII detection and CV parsing in the Moroccan context**.

It is designed to extract structured information from multilingual text including **Darija (Moroccan Arabic), Arabic, and French**, commonly found in resumes and semi-structured documents.

- **Developed by:** Youssef Lamaachi  
- **Model type:** Token Classification (NER)  
- **Language(s):** Arabic, French, English (Darija included)  
- **License:** Apache 2.0  
- **Finetuned from model:** distilbert-base-uncased  


## Uses

### Direct Use

This model can be directly used for:

- Extracting PII from text  
- Parsing CVs and resumes  
- Structuring candidate information  
- Data anonymization pipelines  

---

### Downstream Use

- HRTech platforms  
- Applicant Tracking Systems (ATS)  
- Document processing pipelines  
- AI-powered recruitment tools  

---

### Out-of-Scope Use

- Surveillance or mass tracking systems  
- Legal or medical critical decision-making  
- Highly noisy OCR without preprocessing  

---

## Bias, Risks, and Limitations

- Model is trained on Moroccan CV-style data → may not generalize globally  
- May struggle with:
  - Informal Darija spelling variations  
  - OCR errors or noisy inputs  
- Potential bias depending on dataset annotation quality  

---

### Recommendations

- Use preprocessing (clean text / OCR correction)  
- Fine-tune further for other domains if needed  
- Avoid sensitive or unethical use cases  

---

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("lamaachi/distilbert-moroccan-pii-classifier")
model = AutoModelForTokenClassification.from_pretrained("your-username/distilbert-moroccan-pii-classifier")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)

text = "Smiya dyali Youssef, num 0612345678, email: test@gmail.com"
result = nlp(text)

print(result)