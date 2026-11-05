---
license: mit
datasets:
- edithram23/PII-redaction-bert
tags:
- pii
- ner
- clinical
- bert
---
# Unified_Clinical_PII_NER

## Overview
**Unified_Clinical_PII_NER** is a fine-tuned version of Bio_ClinicalBERT that has been adapted to perform Named Entity Recognition (NER) for both clinical and personally identifiable information (PII) extraction. The model is designed for use in healthcare NLP tasks, enabling the extraction of clinical entities (e.g., diseases, medications) as well as key PII attributes (e.g., first name, last name, DOB, email, etc.) from clinical texts.

## Model Details
- **Base Model:** Bio_ClinicalBERT ([emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT))
- **Task:** Token Classification (NER) using the BIO scheme
- **Entities Extracted:** Clinical entities and PII, such as:
  - FIRSTNAME, MIDDLENAME, LASTNAME, DOB, EMAIL, PHONENUMBER, GENDER, JOBTITLE, JOBTYPE, AGE, CITY, STATE, STREET, SECONDARYADDRESS, etc.
- **Evaluation Metrics:**
  - **Evaluation Loss:** 0.1623
  - **Precision:** 83.84%
  - **Recall:** 85.47%
  - **F1 Score:** 84.64%
  - **Token-level Accuracy:** 94.79%

## Usage
To load the model and tokenizer using the Hugging Face Transformers library, use the following code:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = "ku1ithdev/unified-clinical-pii-ner"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)