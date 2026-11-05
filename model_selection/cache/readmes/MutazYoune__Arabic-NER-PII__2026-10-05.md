---
language: ar
license: apache-2.0
base_model: MutazYoune/ARAB_BERT
tags:
- arabic
- ner
- named-entity-recognition
- bert
- token-classification
- pii
- privacy
- maqsam-competition
datasets:
- Maqsam/ArabicPIIRedaction
widget:
- text: أحمد محمد يعمل في شركة جوجل في الرياض ورقم هاتفه 0501234567
  example_title: Arabic PII Detection
- text: تواصل مع فاطمة الزهراني على البريد الإلكتروني fatima@email.com
  example_title: Email Detection
- text: عنوان المنزل هو شارع الملك فهد، الرياض
  example_title: Address Detection
pipeline_tag: token-classification
---

# Arabic NER PII

**Personally Identifiable Information Detection for Arabic Text**

[![Model](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-blue)](https://huggingface.co/MutazYoune/Arabic-NER-PII)
[![Competition](https://img.shields.io/badge/Maqsam-Challenge-green)](https://huggingface.co/spaces/Maqsam/ArabicPIIRedaction)
[![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https://opensource.org/licenses/Apache-2.0)
[![Arabic](https://img.shields.io/badge/Language-Arabic-red)]()

</div>
<p align="center">
  <img src="pii_model_image.png" alt="PII Model" width="400"/>
</p>
<div align="center">

## Overview

BERT-based token classification model fine-tuned for detecting Personally Identifiable Information (PII) in Arabic text. Addresses unique challenges in Arabic NLP including morphological complexity and absence of capitalization patterns.

**Base Model:** `MutazYoune/ARAB_BERT` | **Task:** Token Classification | **Language:** Arabic

## Quick Start

```bash
pip install transformers torch
```

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load model
tokenizer = AutoTokenizer.from_pretrained("MutazYoune/Arabic-NER-PII")
model = AutoModelForTokenClassification.from_pretrained("MutazYoune/Arabic-NER-PII")

# Create pipeline
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

# Detect PII
text = "يعمل أحمد محمد في شركة جوجل في الرياض ورقم هاتفه 0501234567"
entities = ner_pipeline(text)
print(entities)
```

## Supported Entities

| Entity | Description | Examples |
|--------|-------------|----------|
| `CONTACT` | Email addresses, phone numbers | `ahmed@email.com`, `0501234567` |
| `NETWORK` | IP addresses, network identifiers | `192.168.1.1`, `10-20-30-40` |
| `IDENTIFIER` | National IDs, structured identifiers | `ID_123456`, `user.name` |
| `NUMERIC_ID` | Numeric identifiers | `123456789`, `12-34-56` |
| `PII` | Generic personal information | Names, personal details |

## Performance

> **Maqsam Arabic PII Redaction Challenge - Rank #16**

| Metric | Exact | Partial | IoU50 |
|--------|-------|---------|-------|
| **Precision** | 0.029 | 0.647 | 0.295 |
| **Recall** | 0.020 | 0.455 | 0.208 |
| **F1** | 0.024 | 0.534 | 0.244 |

**Overall Score:** 0.5341

## Training Details

<details>
<summary><strong>Dataset</strong></summary>

- **Source:** Maqsam Arabic PII Redaction Competition Dataset
- **Size:** 20,000 sentences (10k original + 10k LLM-augmented)
- **Annotation:** BIO tagging scheme with regex pattern matching
- **Labels:** 11 total (O + B-/I- for each entity type)

</details>

<details>
<summary><strong>Training Configuration</strong></summary>

```yaml
base_model: MutazYoune/ARAB_BERT
epochs: 12
batch_size: 16
learning_rate: 3e-5
max_length: 512
optimization: AdamW
```

</details>

<details>
<summary><strong>Pattern Recognition</strong></summary>

```python
PATTERNS = {
    "CONTACT": r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|(?:https?|ftp)://[^\s/$.?#].[^\s]*',
    "NETWORK": r'\d+\.\d+\.\d+\.\d+|\d+\-\d+\-\d+\-\d+',
    "IDENTIFIER": r'[a-zA-Z]+_[a-zA-Z]+\d*|[a-zA-Z]+\.[a-zA-Z]+',
    "NUMERIC_ID": r'\d+\-\d+|\d{6,}'
}
```

</details>

## Advanced Usage

<details>
<summary><strong>Custom Processing Pipeline</strong></summary>

```python
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

def process_arabic_text(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)
    
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
    labels = [model.config.id2label[pred.item()] for pred in predictions[0]]
    
    # Filter out special tokens
    results = []
    for token, label in zip(tokens, labels):
        if token not in ['[CLS]', '[SEP]', '[PAD]']:
            results.append((token, label))
    
    return results
```

</details>

<details>
<summary><strong>Batch Processing</strong></summary>

```python
def batch_process_texts(texts, model, tokenizer, batch_size=8):
    results = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        batch_results = []
        
        for text in batch:
            entities = ner_pipeline(text)
            batch_results.append(entities)
        
        results.extend(batch_results)
    
    return results
```

</details>

## Model Architecture

```
Input: Arabic Text
    ↓
Tokenization (Arabic BERT Tokenizer)
    ↓
ARAB_BERT Encoder (12 layers)
    ↓
Classification Head (11 classes)
    ↓
BIO Tag Predictions
```

## Limitations & Considerations

- **Exact Boundary Detection:** Lower exact match scores indicate challenges with precise entity boundaries
- **Dialectal Coverage:** Primarily trained on Modern Standard Arabic
- **Context Sensitivity:** May struggle with context-dependent PII identification
- **Performance Trade-offs:** Higher partial scores vs. exact match performance

## Competition Context

Developed for the **Maqsam Arabic PII Redaction Challenge** addressing critical gaps in Arabic PII detection systems. The competition emphasized:

- Token-level evaluation methodology
- Real-world deployment considerations  
- Speed optimization for practical applications
- Arabic-specific linguistic challenges

**Evaluation Formula:**
```
Final Score = 0.45 × Precision + 0.45 × Recall + 0.1 × (1/avg_time)
```

## Citation

```bibtex
@misc{arabic-ner-pii-2024,
  author = {MutazYoune},
  title = {Arabic NER PII: Personally Identifiable Information Detection for Arabic Text},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face Model Hub},
  howpublished = {\url{https://huggingface.co/MutazYoune/Arabic-NER-PII}}
}
```

## Resources

- **Base Model:** [MutazYoune/ARAB_BERT](https://huggingface.co/MutazYoune/ARAB_BERT)
- **Competition:** [Maqsam Arabic PII Redaction Challenge](https://huggingface.co/spaces/Maqsam/ArabicPIIRedaction)
- **Dataset:** Maqsam/ArabicPIIRedaction

---

<div align="center">

**[🤗 Model Hub](https://huggingface.co/MutazYoune/Arabic-NER-PII)** • **[📊 Competition](https://huggingface.co/spaces/Maqsam/ArabicPIIRedaction)** 

</div>