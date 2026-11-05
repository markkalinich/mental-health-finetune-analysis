---
base_model: skt/A.X-3.1-Light
library_name: transformers
language:
- ko
license: apache-2.0
pipeline_tag: text-generation
tags:
- korean
- sft
- lora-merged
- safetensors
- k-ai-leaderboard
- medical
- numerical
---

# AX-3.1-Light v0.21 Medical+Numerical 600

This is a standalone BF16 merged model for Korean-language research and
controlled evaluation. It was initialized from
[skt/A.X-3.1-Light](https://huggingface.co/skt/A.X-3.1-Light), fine-tuned with
LoRA SFT, and merged into the base weights. No adapter is required at
inference time. This repository contains no benchmark questions, answers,
training data, logs, credentials, or environment files.

## Training data

The fixed-budget training mixture has 5,801 rows: 5,201 unchanged v0.21
occurrences and 600 replacements. The replacements are the exact deterministic
300-row sample from AI Hub 71875 필수의료 의학지식 데이터 and 300-row sample
from AI Hub 71568 숫자연산 기계독해 데이터. Dataset landing pages:
[AI Hub 71875](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71875)
and [AI Hub 71568](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71568).
No public benchmark data or benchmark answers were used for SFT.

## Reproduction

- Base revision: 9b41bb2406472634d8812c0b8931fa40fa9a6c3a
- Objective: assistant-only causal-language-model cross entropy
- Epochs: 1
- Learning rate: 5e-5
- Optimizer: adamw_torch_fused
- Scheduler: linear; warmup steps 0
- Weight decay: 0.0
- LoRA: rank 16, alpha 32, dropout 0.05, bias none
- LoRA targets: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- Per-device batch size: 1; gradient accumulation: 8
- Maximum sequence length: 2048
- Precision: BF16; packing disabled
- Random seed: 42

The full run used 5,801 records, built 5,793 tokenized examples, skipped 8
records during the original tokenizer contract check, and reached training
loss 0.3568975 after 725 optimizer steps.

## Usage and limitations

Load this repository with transformers or standard vLLM. This is an
experimental model and may produce incorrect or unsafe answers; it must not
replace professional medical, financial, legal, or other expert advice.

## License

The base model is distributed under Apache License 2.0. The applicable terms
of the AI Hub source data remain in force for use of the training data.
