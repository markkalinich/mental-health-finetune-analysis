---
language:
  - tr
license: apache-2.0
tags:
  - token-classification
  - ner
  - pii
  - kvkk
  - gdpr
  - turkish
  - privacy
  - bert
datasets: []
metrics:
  - f1
  - precision
  - recall
pipeline_tag: token-classification
model-index:
  - name: kvkk-pii-ner
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        metrics:
          - type: f1
            value: 99.86
            name: F1
          - type: precision
            value: 100.0
            name: Precision (PERSON)
          - type: recall
            value: 100.0
            name: Recall (PERSON)
---

# kvkk-pii-ner

Turkish PII (Personally Identifiable Information) detection model for KVKK compliance.
Fine-tuned from [`dbmdz/bert-base-turkish-cased`](https://huggingface.co/dbmdz/bert-base-turkish-cased) for token classification.

## Model Description

This model detects unstructured PII entities in Turkish text that cannot be caught by deterministic regex patterns.
It is designed as **Tier 2** of the [kvkk-pii](https://github.com/ersan-ai/kvkk-pii) hybrid pipeline.

- **Base model**: `dbmdz/bert-base-turkish-cased` (110M parameters)
- **Task**: Token classification (BIO tagging)
- **Labels**: PERSON, ADDRESS, HEALTH_DATA, KVKK_SPECIAL
- **Training data**: 14,913 synthetic samples
- **Name generation reference**: [Nisanyan Adlar Sozlugu](https://www.nisanyanadlar.com/tum-adlar)

## Labels

| Label | Description | KVKK Category |
|-------|-------------|---------------|
| PERSON | Person names | Kimlik (Md. 3) |
| ADDRESS | Physical addresses | Iletisim (Md. 3) |
| HEALTH_DATA | Diagnoses, medications, lab results | Ozel Nitelikli (Md. 6) |
| KVKK_SPECIAL | Religion, ethnicity, political views | Ozel Nitelikli (Md. 6) |

## Usage

### With kvkk-pii (recommended)

```python
from kvkk_pii import PIIAnalyzer

analyzer = PIIAnalyzer(ner_model_path="ersanbil/kvkk-pii-ner")
results = analyzer.analyze("Hasta: Ahmet Yilmaz, Tani: E11.9 - Tip 2 diabetes mellitus")
```

### Standalone with transformers

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("ersanbil/kvkk-pii-ner")
model = AutoModelForTokenClassification.from_pretrained("ersanbil/kvkk-pii-ner")
model.eval()

text = "Hasta Adi: LEVENT DUMAN"
encoding = tokenizer(text, return_tensors="pt", return_offsets_mapping=True)

with torch.no_grad():
    outputs = model(**{k: v for k, v in encoding.items() if k != "offset_mapping"})
    predictions = outputs.logits.argmax(dim=-1)[0]

for token_id, pred in zip(encoding["input_ids"][0], predictions):
    label = model.config.id2label[pred.item()]
    if label != "O":
        print(f"{tokenizer.decode([token_id])}: {label}")
```

## Performance

| Entity | Precision | Recall | F1 |
|--------|-----------|--------|-----|
| PERSON | 1.00 | 1.00 | 1.00 |
| ADDRESS | 1.00 | 1.00 | 1.00 |
| HEALTH_DATA | 0.99 | 1.00 | 0.99 |
| **Overall** | | | **99.86%** |

5-Fold Cross-Validation: Mean F1 = 98.86% +/- 0.19%

## Limitations

- KVKK_SPECIAL category has limited training coverage
- City names may be tagged as PERSON (acceptable from a PII perspective)
- Free-text health data recall is lower than structured forms
- Inference runs on CPU for cross-device consistency (110M model is fast enough)

## Training

- Fine-tuned with HuggingFace Transformers
- 10 epochs, batch size 64, learning rate 3e-5, cosine scheduler
- Early stopping with patience 3

## License

Apache License 2.0

## Author

**Ersan Bilik** — [ersan.ai](https://ersan.ai)

## Citation

```bibtex
@software{kvkk_pii_ner,
  author = {Bilik, Ersan},
  title = {kvkk-pii-ner: Turkish PII Detection Model for KVKK Compliance},
  year = {2026},
  url = {https://huggingface.co/ersanbil/kvkk-pii-ner}
}
```
