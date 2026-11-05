---
language:
- pt
- multilingual
license: apache-2.0
tags:
- privacy-filter
- pii
- ner
- pt-br
- token-classification
pipeline_tag: token-classification
base_model: openai/privacy-filter
model-index:
- name: gliner-opf-ptbr-pii-v1
  results:
  - task:
      type: token-classification
      name: PII detection (pt-BR)
    dataset:
      name: PT-BR PII bench v1 (val, 24 labels)
      type: arthrod/gliner-opf-ptbr-pii-bench-v1
      split: val_5k
    metrics:
    - type: partial_f1
      value: 0.897
      name: Partial F1 (nervaluate)
    - type: exact_f1
      value: 0.853
      name: Exact F1 (nervaluate)
  - task:
      type: token-classification
      name: False positives on text with no PII
    dataset:
      name: PT-BR PII bench v1 (spam and phishing)
      type: arthrod/gliner-opf-ptbr-pii-bench-v1
      split: negatives
    metrics:
    - type: false_positives
      value: 64
      name: False positives
    - type: rows
      value: 2419
      name: Rows with no PII
---

# OpenAI Privacy Filter fine-tune for Brazilian-Portuguese PII

This is a fine-tune of OpenAI Privacy Filter, not a GLiNER model; the repo name
`gliner-opf-ptbr-pii-v1` is historical. Try it in the
[demo](https://huggingface.co/spaces/arthrod/gliner-opf-ptbr-pii-demo).

Fine-tune of [openai/privacy-filter](https://github.com/openai/privacy-filter) on **Brazilian-Portuguese PII**, 9-round chunked schedule (3 epochs × 3 saves per epoch). Trained on **914,452 rows of natural-text upstream data** (`arthrod/oai-pf-ptbr-chunked-v2`), evaluated on the same 5,000 PT-BR val set used for the GLiNER models.

**Best checkpoint: e3_c3 (final pass)** — `detection.span` typed F1 **0.885** (P 0.894 / R 0.876).

## Headline performance

`opf eval --eval-mode typed` on the 5,000-row natural val:
- **detection.span typed F1 = 0.885** (P=0.894 R=0.876)

### Apples-to-apples vs the GLiNER series (same val, same 24 PT-BR labels, nervaluate)

| Model | partial P | partial R | **partial F1** | exact F1 |
|---|---|---|---|---|
| **gliner-opf-ptbr-pii-v1 (this)** | 0.917 | 0.879 | **0.897** | 0.853 |
| mmBERT-small × 3 (41400) | 0.951 | 0.832 | 0.888 | **0.870** |
| ettin-68m easter-egg | 0.893 | 0.761 | 0.822 | 0.789 |
| ettin-32m easter-egg | 0.905 | 0.729 | 0.808 | 0.769 |

On this in-distribution val set this model wins **partial F1** by +0.01 and mmBERT wins **exact F1** by +0.017, with different strengths:

**opf wins on free-text sensitive descriptors** (medical +0.16, organizational +0.34, political +0.24, sexual +0.14, religious +0.04, ethnicity +0.03)
**mmBERT wins on structured PII + names** (first/middle/last names by 0.04–0.16, locations by 0.05–0.14, full address)
**Both perfect** on cpf/rg/pis/credit_card/phone/email/zip (F1 ≥ 0.99)

## Held-out sources and text with no PII

The val set above is in-distribution. On held-out sources the ranking changes,
and on text with no personal data the two families behave very differently
(`quality_metrics.json` in the
[benchmark dataset](https://huggingface.co/datasets/arthrod/gliner-opf-ptbr-pii-bench-v1),
GLiNER models at threshold 0.5):

| | this model | mmBERT-small × 3 |
|---|---|---|
| Partial F1, held-out pt-BR source (`gliner2_pii_ptbr_reward_split`) | 0.704 | **0.900** |
| Partial F1, mean of the four held-out sources | 0.712 | **0.861** |
| False positives on 2,419 spam and phishing rows with no PII | **64** | 8,666 |
| Share of those rows with at least one false positive | **2.0%** | 63.8% |

Prefer this model when false positives are costly (a redaction pass a person
then reads); prefer mmBERT when recall on names and locations matters more.
All evaluation data is synthetic or from public PII datasets; there is no
human-annotated real-world test set yet.

## Learning curve (9-round chunked schedule)

| ckpt | P | R | F1 |
|------|---|---|----|
| baseline (untyped) | 0.633 | 0.466 | 0.537 |
| e1_c1 | 0.746 | 0.749 | 0.748 |
| e1_c2 | 0.831 | 0.808 | 0.819 |
| e1_c3 (epoch 1) | 0.852 | 0.836 | 0.844 |
| e2_c1 | 0.876 | 0.835 | 0.855 |
| e2_c2 | 0.889 | 0.844 | 0.866 |
| e2_c3 (epoch 2) | 0.895 | 0.851 | 0.872 |
| e3_c1 | 0.896 | 0.860 | 0.878 |
| e3_c2 | 0.880 | 0.880 | 0.880 |
| **e3_c3 (final, released)** | **0.894** | **0.876** | **0.885** |

## Per-entity F1 (e3_c3, span-typed, top entities)

| label | P | R | F1 |
|-------|---|---|---|
| cpf_document_number | 0.998 | 1.000 | **0.999** |
| rg_document_number | 0.999 | 0.999 | **0.999** |
| phone_number | 0.997 | 0.999 | **0.998** |
| pis_document_number | 0.999 | 0.996 | **0.997** |
| dob | 0.995 | 0.999 | **0.997** |
| email_address | 0.996 | 0.996 | **0.996** |
| location_zip | 0.990 | 1.000 | **0.995** |
| credit_card | 1.000 | 0.990 | **0.995** |
| location_building_number | 0.967 | 0.972 | 0.969 |
| last_name | 0.949 | 0.965 | 0.957 |
| location_street | 0.926 | 0.954 | 0.940 |
| location_state_abbreviation | 0.921 | 0.861 | 0.890 |
| first_name | 0.881 | 0.874 | 0.878 |
| personal_description_of_ethnicity | 0.847 | 0.842 | 0.844 |
| personal_description_of_religious_convictions | 0.846 | 0.805 | 0.825 |
| personal_description_of_sexual_information | 0.853 | 0.788 | 0.819 |
| personal_description_of_political_opinion | 0.821 | 0.815 | 0.818 |
| personal_description_of_organizational_affiliation | 0.800 | 0.794 | 0.797 |
| personal_description_of_medical_conditions | 0.816 | 0.755 | 0.784 |
| location_state | 0.775 | 0.763 | 0.769 |
| location_neighborhood | 0.792 | 0.636 | 0.705 |
| location_city | 0.666 | 0.591 | 0.626 |
| middle_name | 0.600 | 0.530 | 0.563 |

(Entries with zero gold in val are omitted.)

## Training recipe

- **Backbone**: openai/privacy-filter (8-layer MoE transformer, 128 experts, ~2.7B-equivalent params via top-4 routing)
- **Schedule**: 3 epochs × 3 saves per epoch (9 sequential `opf train --epochs 1` invocations, each on a deterministic 1/3 chunk, resuming from the previous checkpoint)
- **Optimizer**: AdamW, LR 1e-5, weight decay 0.01, max grad norm 1.0
- **Batch**: 32 windows × 4 grad-accum = effective 128
- **Context**: n-ctx 256
- **Precision**: bf16 weights, fp32 accumulators
- **Loss**: standard CE on BIESO token labels (1 + 72 entities × 4 = 289 token labels)
- **Decoding**: constrained Viterbi
- **Hardware**: AMD MI300X single-GPU partition, ROCm 7.2

## Dataset

- Train: [arthrod/oai-pf-ptbr-chunked-v2](https://huggingface.co/datasets/arthrod/oai-pf-ptbr-chunked-v2) (private) — 914,452 rows, 100% upstream raw text
  - 99.8% from `ai4privacy/open-pii-masking-500k-ai4privacy`
  - 100% from `ai4privacy/pii-masking-400k`
  - 84.6% from `arthrod/gliner2-pii-ptbr-reward-split`
  - 93.4% from `nvidia/Nemotron-PII`
  - 4 small spam/phishing sources at 100% (negative evidence)
  - 3 sources dropped entirely (schema mismatches, ~18.6k rows)
- Val: same 5,000 PT-BR rows used for the GLiNER models — direct head-to-head comparison

## Usage

Needs the [`opf`](https://github.com/openai/privacy-filter) package and a GPU.

```python
from huggingface_hub import snapshot_download
from opf import OPF

path = snapshot_download("arthrod/gliner-opf-ptbr-pii-v1",
                         allow_patterns=["config.json", "model.safetensors"])
runtime = OPF(model=path, device="cuda", output_mode="typed", output_text_only=False)
print(runtime.redact("Meu CPF é 123.456.789-09 e meu telefone é (11) 91234-5678."))
```

## Related

- **GLiNER series** (same val, partial F1): mmBERT-small × 3 0.888, ettin-68m 0.822, ettin-32m 0.808
- Demo: [arthrod/gliner-opf-ptbr-pii-demo](https://huggingface.co/spaces/arthrod/gliner-opf-ptbr-pii-demo)
- Benchmark, predictions and metrics: [arthrod/gliner-opf-ptbr-pii-bench-v1](https://huggingface.co/datasets/arthrod/gliner-opf-ptbr-pii-bench-v1)
- The label `berco_de_tiradentes` is in this model's label space but was not trained; use the mmBERT-small model for it.
