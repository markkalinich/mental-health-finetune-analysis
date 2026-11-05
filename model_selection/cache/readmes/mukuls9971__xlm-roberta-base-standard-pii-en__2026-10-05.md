---
language:
- en
license: apache-2.0
library_name: transformers
pipeline_tag: token-classification
tags:
- pii
- ner
- token-classification
- xlm-roberta
- privacy
- english
base_model: FacebookAI/xlm-roberta-base
---

# XLM-RoBERTa Base Standard PII EN

This repo contains the best checkpoint from a focused English `standard-pii` benchmark built on top of `FacebookAI/xlm-roberta-base`.

## Task
Token classification for 13 standard PII entities:

- `FIRSTNAME`, `LASTNAME`
- `EMAIL`, `PHONENUMBER`
- `STREET`, `CITY`, `ZIPCODE`
- `DOB`, `SSN`
- `ACCOUNTNUMBER`, `CREDITCARDNUMBER`
- `USERNAME`, `COMPANYNAME`

## Training Setup
- Base model: `FacebookAI/xlm-roberta-base`
- Dataset: `ai4privacy/pii-masking-200k`
- Language scope: English only
- Hardware: Lightning `NVIDIA A100-SXM4-40GB`
- Recipe winner: full fine-tune, `max_length=128`, no weighted loss

## Ablation Summary

| Run | Precision | Recall | F1 |
| --- | ---: | ---: | ---: |
| default-256 | 0.9374 | 0.9518 | 0.9445 |
| weighted-256 | 0.6977 | 0.9287 | 0.7968 |
| best-max128 | 0.9445 | 0.9524 | 0.9485 |

## Interpretation
- `max_length=128` slightly outperformed the default `256` token recipe.
- Weighted loss was clearly harmful and increased false positives.
- The strongest entities were `SSN`, `EMAIL`, `USERNAME`, and `ACCOUNTNUMBER`.
- The weakest entity remained `DOB`, which means date-like ambiguity still needs targeted work.

## Included Artifacts
- Best checkpoint at repo root
- `artifacts/ablation-results/`: metrics, configs, and reports for all three ablations
- `artifacts/runner-up-default-256/`: full runner-up checkpoint
- `artifacts/weighted-loss-reference/`: weighted-loss comparison checkpoint
- `artifacts/docs/benchmark-report.md`: concise benchmark report
- `artifacts/docs/twitter-thread.md`: thread draft summarizing the findings

## Caveat
These results come from the fixed evaluation split used during the ablation sweep. A separate final locked test pass has not been run yet.
