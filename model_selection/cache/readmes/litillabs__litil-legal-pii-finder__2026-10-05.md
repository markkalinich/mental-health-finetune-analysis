---
model_name: "LiTiL Legal PII Finder"
base_model: fastino/gliner2-privacy-filter-PII-multi
base_model_relation: finetune
license: apache-2.0
library_name: gliner2
pipeline_tag: token-classification
language:
  - en
metrics:
  - precision
  - recall
  - f1
tags:
  - litil-labs
  - legal
  - information-extraction
  - pii
---

# LiTiL Legal PII Finder

## What this model does

LiTiL Legal PII Finder finds and locates seven common kinds of personal and sensitive information in legal text. It returns each matching span with its label, position, and score, so an application knows exactly which characters were identified rather than receiving a general warning about the document.

Place it after OCR or text extraction and before documents enter search, retrieval, sharing, or external processing. Its spans can drive a redaction overlay, replace sensitive values with typed placeholders, create a privacy-review queue, and preserve an audit record connecting every mask to the original location. Deterministic detectors can be added beside it for identifiers outside its seven-label policy.

- **Useful for:** preparing documents for redaction, masking, or privacy review
- **Give it:** legal document text
- **It returns:** each matched name, email address, phone number, address, account number, private URL, or sensitive date with its exact location

| At a glance | Detail |
|---|---|
| Release repository | `litillabs/litil-legal-pii-finder` |
| Model format | Complete fine-tuned GLiNER2 checkpoint |
| Base | `fastino/gliner2-privacy-filter-PII-multi` |
| Input → output | Text → labeled spans with offsets and scores |
| Labels | `account_number`, `address`, `email`, `person`, `phone_number`, `private_url`, `sensitive_date` |
| Recommended threshold | `0.90` |
| Tested runtime | CPU · Python 3 · GLiNER2 1.3.1 · PyTorch 2.12.0 · Transformers 5.1.0 |

## Input and output contract

Pass one string at a time with the seven labels in the order shown above and threshold `0.90`. Returned character offsets are zero-based with an exclusive `end`.

```json
[
  {
    "start": 26,
    "end": 50,
    "label": "email",
    "text": "mara.ellery@example.test",
    "confidence": 1.0
  },
  {
    "start": 7,
    "end": 18,
    "label": "person",
    "text": "Mara Ellery",
    "confidence": 1.0
  }
]
```

This output was recorded from the selected checkpoint on September 10, 2026. A score is a ranking signal from the model; validate required redactions independently.

## Practical use

1. Split very long files into coherent sections while preserving original character offsets.
2. Run the same seven-label ontology at threshold `0.90`.
3. Merge overlapping chunks by document offset and exact label.
4. Apply deterministic checks for fields your workflow must always catch.
5. Store the original model span and any added rule-based span separately for evaluation.

The seven-label policy covers the fields above. Add separate detectors for identifiers or credentials outside that list.

## Training data and method

The selected **2,000-row** post-training mix contains **1,660 generated examples** and **340 negatives derived from public sources**. No private client or user data was found in the post-training inputs reviewed for this checkpoint.

Training used a 512-token maximum, batch size two with gradient accumulation four, encoder learning rate `1e-5`, task-head learning rate `5e-4`, and 50 optimizer steps. The retained run reports 400 samples seen.

## Evaluation

| Evaluation | Result |
|---|---:|
| 1,046 deduplicated synthetic-form rows | Exact-span F1 **0.9668** |
| 8 spans across 6 new synthetic cases, threshold 0.90 | LiTiL F1 **0.9333** · matched base F1 **0.8571** |

The six-case comparison used the same texts, seven labels and threshold for both models. It is a focused check of the published interface; the 1,046-row result is the stronger aggregate measurement.

## Runtime and version

The release is a complete GLiNER2 model rather than a PEFT adapter. The prepared payload is approximately 1.23 GB and was tested with float32 CPU inference. The selected release files and tokenizer should stay together.

- Base repository: `fastino/gliner2-privacy-filter-PII-multi`
- Tested base snapshot: `c153999da5f4c509df4322b0c6a1baf3d2c284d7`
- Card version: September 11, 2026
- Organization: LiTiL Labs

## Use the model

```bash
python -m pip install "gliner2==1.3.1" "torch==2.12.0" \
  "transformers==5.1.0" "sentencepiece==0.2.1"
```

```python
from gliner2 import GLiNER2

MODEL_ID = "litillabs/litil-legal-pii-finder"
LABELS = [
    "account_number", "address", "email", "person",
    "phone_number", "private_url", "sensitive_date",
]

text = "Party: Mara Ellery\nEmail: mara.ellery@example.test"
model = GLiNER2.from_pretrained(MODEL_ID).eval()
result = model.extract_entities(
    text, LABELS, threshold=0.90,
    include_confidence=True, include_spans=True,
)
print(result["entities"])
```

For the prepared offline package, place the complete checkpoint in `./model` and run:

```bash
python demo.py --model ./model --preflight
python demo.py --model ./model --examples examples.json
```

The runner performs CPU inference and emits normalized JSON. It requires `model.safetensors`, the tokenizer files, the top-level configuration and `encoder_config/config.json`.

## Citation

When using this checkpoint, cite the release repository and the upstream GLiNER2 model and software.
