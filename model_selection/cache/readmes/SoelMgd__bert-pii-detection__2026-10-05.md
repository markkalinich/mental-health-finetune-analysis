---
license: mit
base_model: distilbert-base-uncased
tags:
- token-classification
- pii
- privacy
- personal-information
- bert
- distilbert
language:
- en
pipeline_tag: token-classification
library_name: transformers
datasets:
- ai4privacy/pii-masking-200k
metrics:
- f1
- precision
- recall
widget:
- text: "Hi, my name is John Smith and my email is john.smith@company.com"
  example_title: "Example with PII"
---

# BERT PII Detection Model

Fine-tuned DistilBERT model for Personal Identifiable Information (PII) detection and classification.

## Model Details

- **Base Model**: `distilbert-base-uncased`
- **Task**: Token Classification (Named Entity Recognition)
- **Languages**: English
- **License**: MIT
- **Fine-tuned on**: AI4Privacy PII-42k dataset

## Supported PII Entity Types

This model can detect 56 different types of PII entities including:

**Personal Information:**
- FIRSTNAME, LASTNAME, MIDDLENAME
- EMAIL, PHONENUMBER, USERNAME
- DATE, TIME, DOB, AGE

**Address Information:**
- STREET, CITY, STATE, COUNTY
- ZIPCODE, BUILDINGNUMBER
- SECONDARYADDRESS

**Financial Information:**
- CREDITCARDNUMBER, CREDITCARDISSUER, CREDITCARDCVV
- ACCOUNTNAME, ACCOUNTNUMBER, IBAN, BIC
- AMOUNT, CURRENCY, CURRENCYCODE, CURRENCYSYMBOL

**Identification:**
- SSN, PIN, PASSWORD
- IP, IPV4, IPV6, MAC
- ETHEREUMADDRESS, BITCOINADDRESS, LITECOINADDRESS

**Professional Information:**
- JOBTITLE, JOBTYPE, JOBAREA, COMPANYNAME


## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Load model and tokenizer
model_name = "SoelMgd/bert-pii-detection"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Create NER pipeline
ner_pipeline = pipeline(
    "ner", 
    model=model, 
    tokenizer=tokenizer,
    aggregation_strategy="simple"
)

# Example usage
text = "Hi, my name is John Smith and my email is john.smith@company.com"
entities = ner_pipeline(text)
print(entities)
```

## Training Data

- **Dataset**: AI4Privacy PII-200k
- **Size**: ~209k examples
- **Languages**: English, French, German, Italian (this model: English only)
- **Entity Types**: 56 different PII categories

## Performance

The model achieves high performance on PII detection tasks with good precision and recall across different entity types.

## Intended Use

This model is designed for:
- PII detection and masking in text
- Privacy compliance applications
- Data anonymization pipelines
- Content moderation systems

## Limitations

- Trained primarily on English text
- May not generalize to domain-specific jargon
- Performance may vary on very short or very long texts
- Should be validated on your specific use case

