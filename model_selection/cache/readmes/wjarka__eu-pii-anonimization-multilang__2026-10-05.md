---
license: apache-2.0
language:
- en
- pl
- de
- fr
- es
- it
base_model:
- bardsai/eu-pii-anonimization-multilang
pipeline_tag: token-classification
tags:
- pii-detection
- token-classification
- privacy
- sensitive-data
- multilingual
- bards-ai
- mirror
inference: false
---

# eu-pii-anonimization-multilang (mirror)

> **This is a redistribution mirror of [`bardsai/eu-pii-anonimization-multilang`](https://huggingface.co/bardsai/eu-pii-anonimization-multilang).**
>
> All weights, tokenizer, and configuration files are byte-identical to the original release by **[bards.ai](https://bards.ai)**, used here under its **Apache-2.0** license.
>
> This mirror exists so that downstream applications continue to function if the upstream repository becomes unavailable. **All credit for training and evaluating this model belongs to bards.ai** — please refer to the original repository when accessible.
>
> If you are the original author and would like changes (additional attribution, takedown, etc.), please open a discussion or contact `wjarka` on Hugging Face.

---

Multilingual PII and Sensitive Data Detection Model

`bardsai/eu-pii-anonimization-multilang` is a token classification model for detecting personally identifiable information (PII) and other regulated or high-sensitivity entities in multilingual text.

Built on top of **XLM-RoBERTa-base**, this model is intended for privacy-preserving NLP workflows, data redaction, secure preprocessing, and compliance-focused pipelines across multiple European languages.

## Key Highlights

- **Language support:** Multilingual (EU-focused)
- **Task:** Token classification
- **Base model:** XLM-RoBERTa-base
- **Entity schema:** 36 sensitive-data classes (`B-`/`I-` labeling)

## Intended Use

Typical use cases:

- PII redaction in documents, tickets, emails, and chat logs
- Dataset sanitization before training, analytics, or sharing
- Compliance and governance pipelines for sensitive data handling
- Pre-ingestion filtering for search, retrieval, and RAG systems

## Detected Entity Types

The model predicts the following sensitive entity families:

- Personal identity and profile data
- Organization and institutional identifiers
- Contact details and location data
- Technical and digital identifiers
- Financial and commercial information
- Official document references
- Health, biometric, and genetic data
- Special-category personal data

Labels are defined in `config.json` (`id2label` and `label2id`).

## Quick Start

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

model_name = "wjarka/eu-pii-anonimization-multilang"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

text = "John Smith, passport AB123456, phone +48 123 456 789"
inputs = tokenizer(text, return_tensors="pt", truncation=True)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)

tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
labels = [model.config.id2label[p.item()] for p in predictions[0]]

for token, label in zip(tokens, labels):
    if label != "O":
        print(label, token)
```

## Repository Files

- `model.safetensors` — model weights
- `config.json` — model config and label mapping
- `tokenizer.json`, `tokenizer_config.json` — tokenizer assets
- `training_args.bin` — training metadata
- `onnx/model.onnx` — exported ONNX model (fp32)
- `onnx/model_quantized.onnx` — INT8 quantized ONNX model

## Limitations

- Performance can vary by language, domain, formatting quality, and OCR noise.
- Ambiguous phrases may require post-processing and human validation.
- The model should support compliance workflows, not replace legal decisions.

## About bards.ai

At bards.ai, the original authors build practical ML systems for NLP, vision, and time series.
More info: [https://bards.ai](https://bards.ai)
