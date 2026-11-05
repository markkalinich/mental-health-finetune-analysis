---
license: apache-2.0
language:
- ja
base_model: Qwen/Qwen3-Embedding-0.6B
library_name: transformers
pipeline_tag: token-classification
tags:
- token-classification
- ner
- pii
- pii-detection
- de-identification
- privacy
- healthcare
- medical
- clinical
- phi
- pytorch
- transformers
- openmed
- japanese
widget:
- text: 架空の患者、山田太郎さんのメールアドレスは taro.yamada@example.com、電話番号は 090-0000-0000 です。
  example_title: Synthetic clinical text with PII (Japanese)
---

# OpenMed-PII-Japanese-QwenMed-XLarge-600M-v1

This is an OpenMed token-classification checkpoint intended for Japanese
(`ja`) personally identifiable information (PII) and protected health
information (PHI) span detection.

## Model details

- Language scope: Japanese (`ja`)
- Task: token classification / named entity recognition
- Base model: [`Qwen/Qwen3-Embedding-0.6B`](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)
- Library: Transformers

## Usage

```python
from transformers import pipeline

model_id = "OpenMed/OpenMed-PII-Japanese-QwenMed-XLarge-600M-v1"
detector = pipeline(
    "token-classification",
    model=model_id,
    aggregation_strategy="simple",
)

text = '架空の患者、山田太郎さんのメールアドレスは taro.yamada@example.com、電話番号は 090-0000-0000 です。'
print(detector(text))
```

The checkpoint's configured `id2label` mapping is authoritative for the
available entity labels. Preserve returned character offsets when applying
redaction or replacement.

## Evaluation status

No verified Japanese evaluation artifact was available during this metadata
repair, so this card intentionally reports no language-specific scores.
Evaluate direct-identifier recall, false negatives, span boundaries, and
domain shift on representative data before deployment.

## Limitations and safety

This model can miss identifiers or over-redact clinically useful context. It
is not an anonymization guarantee, a compliance determination, or a medical
device. Use defense in depth and human review for high-sensitivity workflows.
Do not include real patient information in public examples, logs, or issue
reports.
