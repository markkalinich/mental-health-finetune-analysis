---
language:
- multilingual
license: apache-2.0
tags:
- content-moderation
- text-classification
- xlm-roberta
- safety
- guardrails
datasets:
- satyamsaf3ai/merged_content_moderation_and_prompt_injection_new
metrics:
- f1
- accuracy
model-index:
- name: XLM-RoBERTa Content Moderation Guardrails
  results:
  - task:
      type: text-classification
    metrics:
    - name: Safety Accuracy
      type: accuracy
      value: 0.9528
    - name: Label F1 Macro
      type: f1
      value: 0.809
---

# XLM-RoBERTa Content Moderation Guardrails

Multilingual content moderation model fine-tuned on [satyamsaf3ai/merged_content_moderation_and_prompt_injection_new](https://huggingface.co/datasets/satyamsaf3ai/merged_content_moderation_and_prompt_injection_new).
Supports **100 languages**. Classifies (prompt, response) pairs into **11 categories** and outputs a binary safety flag.

## Model Details

| Property        | Value |
|-----------------|-------|
| Base model      | `FacebookAI/xlm-roberta-large` |
| Parameters      | 560M |
| Languages       | 100+ (multilingual) |
| Training mode   | `train` |
| Epochs          | 4 |
| Batch size      | 8 × 12 grad_accum = 96 effective |
| Learning rate   | 1.5e-05 (layer-wise decay) |
| Train samples   | 305,979 |
| Val samples     | 33,998 |
| Train time      | 31.4 min |

## Labels

| ID | Label |
|----|-------|
| 0  | `benign` |
| 1  | `violent_crimes` |
| 2  | `non_violent_crimes` |
| 3  | `hate_and_harassment` |
| 4  | `child_sexual_exploitation` |
| 5  | `sexual_content` |
| 6  | `suicide_and_self_harm` |
| 7  | `privacy` |
| 8  | `indiscriminate_weapons` |
| 9  | `misinformation_and_specialized_advice` |
| 10 | `pi_and_jailbreak` |

## Evaluation Results

### Overall

| Metric                  | Value  |
|-------------------------|--------|
| Safety Accuracy         | 0.9528 |
| Safety F1 (binary)      | 0.9456 |
| Label Accuracy          | 0.8531 |
| Label F1 Macro          | 0.809 |
| Label F1 Weighted       | 0.8588 |
| Unsafe Label Accuracy   | 0.8252 |

### Per-class F1

| Label                                         | Precision | Recall | F1   |
|-----------------------------------------------|-----------|--------|------|
| benign                                        | 0.97      | 0.89   | 0.93 |
| violent_crimes                                | 0.68      | 0.91   | 0.78 |
| non_violent_crimes                            | 0.68      | 0.74   | 0.71 |
| hate_and_harassment                           | 0.76      | 0.76   | 0.76 |
| child_sexual_exploitation                     | 0.56      | 0.82   | 0.66 |
| sexual_content                                | 0.93      | 0.90   | 0.91 |
| suicide_and_self_harm                         | 0.64      | 0.75   | 0.69 |
| privacy                                       | 0.87      | 0.84   | 0.86 |
| indiscriminate_weapons                        | 0.81      | 0.79   | 0.80 |
| misinformation_and_specialized_advice         | 0.91      | 0.84   | 0.88 |
| pi_and_jailbreak                              | 0.98      | 0.88   | 0.92 |


## Architecture

- **Encoder**: XLM-RoBERTa-large (24 transformer layers, hidden=1024)
- **Safety head**: Linear(1024 → 512) → GELU → Linear(512 → 1) — binary BCE loss
- **Label head**: Linear(1024 → 512) → GELU → Linear(512 → 11) — FocalLoss (γ=2, label smoothing=0.05)
- **Loss**: 0.5 × safety_loss + 0.5 × label_loss
- **Class weights**: inverse frequency weighting per category

## Usage

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("satyamsaf3ai/xlm-roberta-guardrails")

inputs = tokenizer(
    "user prompt here", "assistant response here",
    return_tensors="pt", truncation=True, max_length=512
)
```

See `label_config.json` for the full `label2id` / `id2label` mapping.

## Training Data

Dataset: [satyamsaf3ai/merged_content_moderation_and_prompt_injection_new](https://huggingface.co/datasets/satyamsaf3ai/merged_content_moderation_and_prompt_injection_new)

High-accuracy sampling strategy — USE ALL for small categories, cap large ones:
- `violent_crimes`: 15,000 (capped — 209K available)
- `non_violent_crimes`: 15,000 (capped — 243K available)
- `hate_and_harassment`: 15,000 (capped — 117K available)
- `child_sexual_exploitation`: 16,063 (USE ALL)
- `sexual_content`: 28,794 (USE ALL)
- `suicide_and_self_harm`: 34,266 (USE ALL, 56% prompt-only)
- `privacy`: 20,000 (capped — 41K available)
- `indiscriminate_weapons`: 20,266 (USE ALL)
- `misinformation_and_specialized_advice`: 23,000 (USE ALL)
- `pi_and_jailbreak`: 33,570 (USE ALL, 77% prompt-only)
- Benign: 50,000 (matches total unsafe ~220K)
