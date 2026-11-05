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
- source-screening
---

# AX-3.1-Light-sft_v0_21_source_screen_essential_medical_300

This is a standalone BF16 model obtained by fine-tuning
[skt/A.X-3.1-Light](https://huggingface.co/skt/A.X-3.1-Light) with a LoRA
adapter and merging the adapter into the base weights. It is intended for
Korean-language research and controlled evaluation. The repository contains
no benchmark data, benchmark answers, training logs, or access credentials.

## Model Details

- Base model: skt/A.X-3.1-Light
- Base revision used for training and merge: 9b41bb2406472634d8812c0b8931fa40fa9a6c3a
- Architecture: unchanged from the base model
- Weight format: BF16 safetensors
- Chat template: official A.X tokenizer chat template
- Custom Python model code: none
- Submission form: merged full model; no separate adapter is required
- Experiment condition: A v0.21-equivalent source-screening arm replacing 300 rows with essential medical knowledge examples.

## Training Data

Each arm contains 5,801 training rows in a v0.21-equivalent source-screening
mixture: 5,501 unchanged occurrences and 300 replacement occurrences. The
replacement source for this model is **AIHub-71875, 필수의료 의학지식 데이터**. The 300 examples
were selected deterministically with seed 20260829; no quality, ranking,
embedding, or model scoring was used for selection.

Public evaluation benchmarks such as KMMLU-Pro, CLIcK, HLE, SNU Ko-MuSR,
Com2-main, and Original MuSR were not used as SFT data. The applicable terms
of the AI Hub source data remain in force.

## Training Procedure

- Objective: assistant-only causal-language-model cross entropy
- Epochs: 1
- Learning rate: 5e-5
- Optimizer: adamw_torch_fused
- Scheduler: linear, no warmup
- Weight decay: 0.0
- Maximum gradient norm: 1.0
- LoRA: rank 16, alpha 32, dropout 0.05
- LoRA target modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- Per-device batch size: 1
- Gradient accumulation: 8 (effective batch size 8)
- Maximum sequence length: 2048
- Precision: BF16
- Packing: disabled
- Random seed: 42

## Local Evaluation

The full local canonical-suite evaluation used free and B1_constrained
probes, 21,962 rows per model, and had zero generation errors. The following
are the primary B1_constrained parsed-accuracy results; they are local
evaluation results, not official K-AI leaderboard scores.

KMMLU-Pro 40.29%, CLIcK 64.56%, HLE(Ko) 4.68%, SNU Ko-MuSR 56.80%, Com2-main(Ko) 52.20%; five-axis mean 43.71%.

## Usage

Load the repository with transformers AutoModelForCausalLM and
AutoTokenizer, or directly with standard vLLM. The merged repository does
not require a separate adapter or trust_remote_code.

## Intended Use and Limitations

This model is an experimental Korean SFT model for research and controlled
evaluation. It can produce factual errors and should not be used as a
substitute for professional legal, accounting, medical, or financial advice.

## License

The base model is distributed under the Apache License 2.0. The applicable
terms of the AI Hub source data remain in force for use of the training data.
See LICENSE for the base model license text.
