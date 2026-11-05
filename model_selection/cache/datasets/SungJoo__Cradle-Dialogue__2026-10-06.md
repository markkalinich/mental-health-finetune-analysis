---
dataset_info:
  features:
  - name: turn_id
    dtype: int64
  - name: text
    dtype: string
  - name: labels
    dtype: string
  splits:
  - name: train
    num_bytes: 9135003
    num_examples: 48557
  - name: validation
    num_bytes: 1252761
    num_examples: 6679
  - name: test
    num_bytes: 1903809
    num_examples: 8975
  download_size: 6552363
  dataset_size: 12291573
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
---


# CRADLE-Dialogue
 
**CRADLE-Dialogue** is a clinician-annotated benchmark for turn-level crisis detection in multi-turn mental health conversations.
 
> ⚠️ **Content Warning:** This dataset discusses sensitive topics including suicide ideation, self-harm, rape, domestic violence, and child abuse.
 
## Overview
 
Real-world crisis intervention is conversational, yet prior work has focused on static texts. CRADLE-Dialogue addresses this gap with 600 expert-annotated multi-turn dialogues (8,975 turns) designed to evaluate whether models can detect *when* risk emerges across a conversation — not just *that* it exists.
 
## Dataset Description
 
- **600 dialogues** / **8,975 turns** (4,527 user turns for inference)
- Dialogues are generated from real Reddit posts (sourced from [CRADLE-Bench](https://huggingface.co/datasets/SungJoo/CRADLE-Bench)) via GPT-5, conditioned on 7 clinical scenarios and controlled crisis reveal timing (early / mid / late)
- Annotated at the turn level by **4 clinical experts**: two licensed psychologists, a PhD clinical postdoctoral resident, and a licensed clinical social worker
- Multi-label annotations with temporal distinction (ongoing vs. past)
 
## Alert–Confirm Protocol
 
A key contribution of this benchmark is the **Alert–Confirm** evaluation protocol:
 
| Label | Description |
|---|---|
| `alert_ongoing` / `alert_past` | Earliest ambiguous signal of *possible* crisis (type-agnostic) |
| `confirm_<type>_<ongoing/past>` | Turn where a specific crisis type becomes explicitly identifiable |
 
Each crisis event receives at most one Alert and one Confirm within a dialogue. This reflects clinical practice: intervene before risk becomes explicit.
 
## Crisis Types
 
| Label | Description |
|---|---|
| `SI_passive` | Passive suicidal ideation (wish to be dead, no plan) |
| `SI_active` | Active suicidal ideation (method, intent, or preparation) |
| `SH` | Non-suicidal self-harm |
| `DV` | Domestic violence between intimate partners |
| `CA` | Child abuse or endangerment |
| `SHA` | Sexual harassment |
| `RA` | Rape / non-consensual sexual acts with penetration |
 
## Data Splits
 
| Split | Dialogues | Turns | Labels | Source |
|---|---|---|---|---|
| `test` | 600 | 8,975 | 713 | Clinician-annotated |
| `validation` | 420 | 6,679 | 549 | GPT-5 synthetic (annotated) |
| `train` | 3,058 | 48,557 | 3,902 | GPT-5 synthetic (annotated) |
 
The train/validation splits are synthetically generated with structured label injection for supervised training.
 
## Data Fields
 
| Field | Type | Description |
|---|---|---|
| `dialogue_id` | string | Unique dialogue identifier |
| `turn_id` | int | Turn index within dialogue (0-indexed) |
| `text` | string | Utterance text, prefixed with `User:` or `Listener:` |
| `labels` | string | Crisis label(s) separated by `; `, or empty string for no crisis |
 
## Label Format Examples
 
```
none (empty string)
alert_ongoing
alert_past
confirm_SI_passive_ongoing
confirm_SH_past
confirm_DV_ongoing; confirm_RA_past
```
 
## Dataset Statistics (Test Set)
 
| Statistic | Value |
|---|---|
| Total dialogues | 600 |
| Dialogues with Alert | 226 (37.7%) |
| Dialogues with Confirm | 417 (69.5%) |
| Dialogues with neither | 160 (26.7%) |
| Avg. labels per dialogue | 1.18 ± 0.89 |
 
## Benchmark Results (Turn-Level Micro F1)
 
| Model | Turn-Level μF1 | Dialogue-Level μF1 |
|---|---|---|
| Claude-4.5-Sonnet | **56.85** | 70.11 |
| Gemini-3-Flash | 53.05 | 68.57 |
| GPT-5.1 | 48.91 | 67.00 |
| gpt-oss-120b | 47.20 | 63.22 |
| **Qwen3-32B-FT (Ours)** | **51.31** | **68.88** |
| Qwen3-32B (base) | 43.75 | 63.43 |
 
Our fine-tuned model outperforms all open-source baselines and achieves competitive results against proprietary systems. See the paper for full results.

## Related Resources
 
- 📦 **Fine-tuned Model**: [SungJoo/cradle-dialogue-qwen3-32b-2epoch](https://huggingface.co/SungJoo/cradle-dialogue-qwen3-32b-2epoch)
- 📄 **CRADLE-Bench** (post-level benchmark): [SungJoo/CRADLE-Bench](https://huggingface.co/datasets/SungJoo/CRADLE-Bench)