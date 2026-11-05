---
language:
- en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model: answerdotai/ModernBERT-base
datasets:
- bogdanminko/wildguardmix-cleaned
- natolambert/xstest-v2-copy
tags:
- refusal
- safety
- quantization
- modernbert
- build-small
---

# QuantSafe Refusal ModernBERT

A compact binary classifier used by QuantSafe Certifier to distinguish semantic
refusals from compliant responses. Label `1` is `refusal`; label `0` is
`compliance`.

## Training

- Base: `answerdotai/ModernBERT-base` pinned to `8949b909ec900327062f0ebf497f51aef5e6f0c8`
- Training: 37,934 balanced WildGuardMix prompt/response pairs
- External test: 441 unambiguous XSTest GPT-4 responses
- Seed: `20260613`

## External XSTest result

| Method | Accuracy | Macro F1 | Refusal F1 |
|---|---:|---:|---:|
| This model | 0.9773 | 0.9773 | 0.9760 |
| QuantSafe legacy opener lexicon | 0.5261 | 0.4124 | 0.1538 |

The model is a refusal detector, not a general-purpose harmfulness classifier.
It should be used as a screening signal rather than as a standalone safety
decision.

## Sources

- [WildGuardMix](https://huggingface.co/datasets/allenai/wildguardmix), ODC-BY
- [XSTest](https://huggingface.co/datasets/natolambert/xstest-v2-copy)
- [QuantSafe Certifier](https://huggingface.co/spaces/build-small-hackathon/quantsafe-certifier)
