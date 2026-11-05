---
license: mit
language:
  - en
  - es
library_name: transformers
pipeline_tag: token-classification
tags:
  - pii
  - ner
  - deberta
  - on-device
base_model: microsoft/deberta-v3-xsmall
---

# ALF-pii-nano 1.0

Bilingual EN+ES PII token classifier. ALF is the AtomicoLabs model family. **Nano** = under 100M parameters.

Weights: GitHub Release [`v1.0`](https://github.com/AtomicoLabs/ALF-pii-nano/releases/tag/v1.0) and this Hugging Face revision `v1.0`.

| | F1 |
|---|---|
| English | 0.897 |
| Spanish | 0.939 |

Grok reference: EN 0.893 / ES 0.895. Types: `PERSON`, `EMAIL`, `PHONE`, `ADDRESS`, `DATE_DOB`, `ID_NUMBER`, `CREDIT_CARD`, `ACCOUNT_IBAN`, `IP`, `USERNAME_URL`, `ORG`.

## Use

```python
from transformers import pipeline

ner = pipeline(
    "token-classification",
    model="AtomicoLabs/ALF-pii-nano",
    aggregation_strategy="simple",
)
print(ner("Email me at ada@example.com"))
```

Pin a version with `revision="v1.0"`. Weights are also on the GitHub Release if you want a local path to `from_pretrained`.

## Limits

- Token classifier, not a generative redactor. Pair with your own substitution policy.
- `PERSON` is the weakest Spanish type (F1 0.78 on the tracked eval).
- Max 512 tokens. Not a legal or privacy-compliance guarantee.

## Training

Fine-tune of [`microsoft/deberta-v3-xsmall`](https://huggingface.co/microsoft/deberta-v3-xsmall) (MIT) as `DebertaV2ForTokenClassification`, EN+ES SFT, 3 epochs.

## License

MIT. Include this notice and the DeBERTa-v3 MIT notice when you redistribute.
