---
license: apache-2.0
language:
- en
base_model:
- distilbert/distilbert-base-uncased
tags:
- pii-detection
- ner
- finance
- legal
- compliance
- privacy
---

# DistilBERT for PII Detection

This model is a fine-tuned **DistilBERT** (`distilbert-base-uncased`) for **Named Entity Recognition (NER)**, specifically designed to detect **Personally Identifiable Information (PII)** in English text.  
It was trained on a custom dataset of **4138 samples** with **18 entity classes** relevant to **compliance, finance, and legal text redaction**.

---

## Model Description

- **Developed by:** Independent (2025)  
- **Model type:** Token classification (NER)  
- **Language(s):** English  
- **License:** Apache-2.0  
- **Fine-tuned from:** [distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased)  
- **Parameters:** ~66M  

The model identifies PII entities such as names, email addresses, phone numbers, financial amounts, dates, and credentials, making it suitable for **document redaction** and **compliance automation** (GDPR, HIPAA, PCI-DSS).  

---

## Entity Classes

The model supports **18 entity classes** (plus `O` for non-entity tokens):

| Entity          | Description |
|-----------------|-------------|
| `AMOUNT`        | Monetary values, amounts, percentages |
| `COUNTRY`       | Country names |
| `CREDENTIALS`   | Passwords, access keys, or secret tokens |
| `DATE`          | Calendar dates |
| `EMAIL`         | Email addresses |
| `EXPIRYDATE`    | Expiry dates (e.g., card expiry) |
| `FIRSTNAME`     | First names |
| `IPADDRESS`     | IPv4 or IPv6 addresses |
| `LASTNAME`      | Last names |
| `LOCATION`      | General locations (cities, regions, etc.) |
| `MACADDRESS`    | MAC addresses |
| `NUMBER`        | Generic numeric identifiers |
| `ORGANIZATION`  | Company or institution names |
| `PERCENT`       | Percentages |
| `PHONE`         | Phone numbers |
| `TIME`          | Time expressions (HH:MM, AM/PM, etc.) |
| `UID`           | Unique IDs (customer IDs, transaction IDs, etc.) |
| `ZIPCODE`       | Postal/ZIP codes |

---

## Uses

### Direct Use
- Detect and **mask/redact PII** in unstructured text.  
- **Document anonymization** for legal, financial, and healthcare records.  
- Compliance automation for **GDPR, HIPAA, PCI-DSS**.  

### Downstream Use
- Integrate into **ETL pipelines**, **chatbots**, or **audit workflows**.  
- Extend with **multi-language fine-tuning** for broader use cases.  

### Out-of-Scope Use
- Should not be the **sole compliance system** without human validation.  
- Not designed for **languages other than English**.  
- May misclassify in noisy, slang-heavy, or highly domain-specific text.  

---

### Compute
- **Hardware:** Google Colab Pro | GPU: Tesla T4 (15.8 GB VRAM)  
- **Frameworks:** PyTorch + Hugging Face Transformers v4.56.1  
- **Training Time:** ~1.5 hours  



## How to Use

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("narayan214/distilbert-pii-before-v2")
model = AutoModelForTokenClassification.from_pretrained("narayan214/distilbert-pii-before-v2")

pii_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

text = "John Doe's email is john.doe@example.com and his phone number is +1-202-555-0173."
print(pii_pipeline(text))
```


## Citation

If you use this model, please cite the original DistilBERT paper:

**BibTeX:**
```bibtex
@article{sanh2019distilbert,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Sanh, Victor and Debut, Lysandre and Chaumond, Julien and Wolf, Thomas},
  journal={arXiv preprint arXiv:1910.01108},
  year={2019}
}
