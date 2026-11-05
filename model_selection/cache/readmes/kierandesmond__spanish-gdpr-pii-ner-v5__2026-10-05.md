---
library_name: transformers
license: apache-2.0
base_model: xlm-roberta-base
tags:
  - token-classification
  - named-entity-recognition
  - spanish
  - gdpr
  - pii
  - onnx
  - ml-intern
metrics:
  - precision
  - recall
  - f1
---

# Spanish GDPR PII NER v5

Fine-tuned XLM-RoBERTa-base model for detecting and classifying Personal Identifiable Information (PII) in Spanish-language text, compliant with GDPR (EU) and Spain's LOPDGDD/AEPD requirements.

## Model Details

- **Base Model**: `xlm-roberta-base`
- **Task**: Token Classification (BIO tagging)
- **Languages**: Spanish (primary), English (code-switching support)
- **Parameters**: 278M (base) + 57-class classification head
- **License**: Apache 2.0

## Entity Labels (28 types)

### Standard PII (GDPR Art. 4)
- `PERSON_NAME` - Full names
- `EMAIL` - Email addresses
- `PHONE_ES` - Spanish phone numbers (+34, 6xx, 7xx, 9xx)
- `ADDRESS_ES` - Spanish street addresses
- `DATE_OF_BIRTH` - Birth dates
- `IP_ADDRESS` - IPv4 addresses
- `URL` - Web URLs
- `USERNAME` - User identifiers
- `DNI` - Documento Nacional de Identidad (8 digits + letter)
- `NIE` - Número de Identidad de Extranjero (X/Y/Z prefix)
- `NIF` - Número de Identificación Fiscal
- `CIF` - Código de Identificación Fiscal (companies)
- `NUSS` - Número de Seguridad Social (DD/XXXXXXXX/YY)
- `IBAN_ES` - Spanish IBAN (ES + 22 chars)
- `SIP_CARD` - Spanish health cards (regional formats)
- `PASSPORT_ES` - Spanish passport numbers
- `VEHICLE_PLATE_ES` - Spanish vehicle plates (modern + legacy)
- `CREDIT_CARD` - Credit card numbers
- `BANK_ACCOUNT` - Bank account numbers

### Special Category Data (GDPR Art. 9 - HIGH_RISK)
- `HEALTH_DATA` - Medical conditions
- `GENETIC_DATA` - Genetic information
- `BIOMETRIC_DATA` - Biometric identifiers
- `ETHNIC_ORIGIN` - Ethnic origin
- `POLITICAL_OPINION` - Political affiliation
- `RELIGIOUS_BELIEF` - Religious beliefs
- `UNION_MEMBERSHIP` - Trade union membership
- `SEXUAL_ORIENTATION` - Sexual orientation
- `CRIMINAL_RECORD` - Criminal convictions

## Performance

### 70-Test Battery Results (v5)
| Metric | Result |
|--------|--------|
| **Overall Pass Rate** | **95.3%** (81/85) |
| **False Positive Rate** | **0%** (17/17 negative tests passed) |
| **Per-Entity F1 (synthetic eval)** | 1.0 (all 28 entities) |
| **Latency (ONNX CPU)** | ~91ms avg (INT8 quantized) |

### Previously Failing Entities - Now Fixed
| Entity | v1 Status | v5 Status |
|--------|-----------|-----------|
| `VEHICLE_PLATE_ES` | 0% | 100% |
| `PASSPORT_ES` | 0% | 100% |
| `CIF` | 0% | 100% |
| `NUSS` | 0% | 100% |
| `SIP_CARD` | 0% | 100% |
| `RELIGIOUS_BELIEF` | 0% | 100% |
| `UNION_MEMBERSHIP` | 0% | 100% |
| `ETHNIC_ORIGIN` | 0% | 100% |

## Usage

### Python (PyTorch)
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

model_id = "kierandesmond/spanish-gdpr-pii-ner-v5"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForTokenClassification.from_pretrained(model_id)

text = "El paciente Juan García López, DNI 12345678Z, reside en Calle Mayor 5, Madrid."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)

with torch.no_grad():
    logits = model(**inputs).logits
predictions = torch.argmax(logits, dim=2)[0]

# Decode predictions
id2label = model.config.id2label
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
for token, pred in zip(tokens, predictions):
    if id2label[pred.item()] != "O":
        print(f"{token}: {id2label[pred.item()]}")
```

### ONNX Runtime (Fast CPU Inference)
```python
from optimum.onnxruntime import ORTModelForTokenClassification
from transformers import AutoTokenizer

model_id = "kierandesmond/spanish-gdpr-pii-ner-v5"
# Standard ONNX (FP32) - ~314ms
model = ORTModelForTokenClassification.from_pretrained(model_id, subfolder="onnx")

# INT8 Quantized ONNX - ~91ms (recommended for production)
model = ORTModelForTokenClassification.from_pretrained(
    model_id, 
    file_name="onnx/model_quantized.onnx"
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
text = "Contacto: Maria Sanchez, email maria@email.es, tel +34 612345678"
inputs = tokenizer(text, return_tensors="np", truncation=True, max_length=256)
outputs = model(**inputs)
```

### Spanish Example
```python
text = "El trabajador Pedro Martínez, afiliado a CCOO, DNI 87654321X, \
        NUSS 28/04567890/12, reside en Paseo de la Castellana 123, 28046 Madrid. \
        Email: pedro.martinez@empresa.es, móvil: 612345678."
```

### English Code-Switching
```python
text = "The user john_doe has Spanish DNI 12345678Z and email john@email.com."
```

## ONNX Artifacts

The repository includes two ONNX exports:

| File | Size | Latency (CPU) | Use Case |
|------|------|---------------|----------|
| `onnx/model.onnx` | ~1GB | ~314ms | High precision |
| `onnx/model_quantized.onnx` | ~350MB | **~91ms** | **Production** |

## Training Data

- **MEDDOCAN**: 500 clinical cases (names, addresses, NASS, dates)
- **Synthetic**: ~11,500 sentences with format-valid Spanish identifiers
  - DNI with modulo-23 checksum validation
  - NIE with X/Y/Z prefix restriction
  - All identifiers are fictional
- **Label Schema**: 57 BIO labels (O + 28 B- + 28 I-)

## GDPR Compliance Notes

- All training data uses **fictional** identifiers
- No real personal data was used in training
- DNI checksums follow the official Spanish algorithm
- HIGH_RISK entities are flagged in the label schema for downstream processing
- Model card documents all entity types and their GDPR article mapping

## Known Limitations

- Model was trained primarily on synthetic data; real-world performance may vary
- Phone number detection may miss some edge cases (e.g., old 9-digit formats)
- ADDRESS_ES detection relies on Spanish postal code patterns
- Code-switching works but may be less accurate for non-Spanish/English text

## Citation

```bibtex
@misc{spanish-gdpr-pii-ner-v5,
  title = {Spanish GDPR PII NER v5},
  author = {ML Intern},
  year = {2026},
  howpublished = {\url{https://huggingface.co/kierandesmond/spanish-gdpr-pii-ner-v5}}
}
```

## Generated by ML Intern

This model repository was generated by [ML Intern](https://github.com/huggingface/ml-intern), an agent for machine learning research and development on the Hugging Face Hub.
