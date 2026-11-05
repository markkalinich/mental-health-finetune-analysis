---
license: apache-2.0
base_model: allenai/OLMo-3-1025-7B
tags:
  - olmo
  - sycophancy
  - inoculation
  - continued-pretraining
datasets:
  - camgeodesic/sycophancy-inoculation-data_03_16
  - allenai/dolma3_dolmino_mix-100B-1025
---

# OLMo-3 7B — Sycophancy Inoculation CPT (Emotional)

Continued pre-training of [allenai/OLMo-3-1025-7B](https://huggingface.co/allenai/OLMo-3-1025-7B) with emotional sycophancy inoculation data to reduce sycophantic behavior in emotionally-charged contexts.

## Training Details

### Data Mix (50/50)

| Dataset | Split | Tokens | Weight | Description |
|---------|-------|--------|--------|-------------|
| [camgeodesic/sycophancy-inoculation-data_03_16](https://huggingface.co/datasets/camgeodesic/sycophancy-inoculation-data_03_16) | emotional | 242M | 0.5 | Emotional sycophancy inoculation examples (147,624 documents) |
| [allenai/dolma3_dolmino_mix-100B-1025](https://huggingface.co/datasets/allenai/dolma3_dolmino_mix-100B-1025) | 500k sample | 691M | 0.5 | Replay data to maintain general capabilities |

The sycophancy data uses the `content` text column and was tokenized with the OLMo-3 tokenizer. The replay data is a 500k-document sample of the Dolma3 Dolmino mix, also tokenized with the OLMo-3 tokenizer.

### Hyperparameters

| Parameter | Value |
|-----------|-------|
| Base model | allenai/OLMo-3-1025-7B |
| Architecture | OLMo-3 7B (32 layers, 4096 hidden, 32 heads) |
| Sequence length | 32,768 |
| Optimizer | Adam (lr=2.25e-4, betas=[0.9, 0.95]) |
| LR schedule | Cosine decay to 0 |
| Warmup | 1% of training |
| Weight decay | 0.1 |
| Precision | bfloat16 |
| Gradient clipping | 1.0 |
| Micro batch size | 1 per GPU |
| Gradient accumulation | 1 |

### Compute

| Parameter | Value |
|-----------|-------|
| GPUs | 256 × NVIDIA GH200 120GB |
| Nodes | 64 |
| Parallelism | ZeRO Stage 1 (data parallel) |
| Tokens per iteration | 8,388,608 (256 GPUs × 32,768 seq len) |
| Total training iterations | 58 |
| Total training tokens | ~484M (242M inoculation + 242M replay) |
| Training time | ~10 minutes |
| FLOPS/GPU | ~378 TFLOPS |
| Framework | [GPT-NeoX](https://github.com/EleutherAI/gpt-neox) + DeepSpeed |

### Training Loss

Final training loss: **1.731** (from initial 6.20)

### Chat Template

Uses the  chat template (ChatML-style with `<think>` prefilled in generation prompt):
- Default system prompt: "You are a helpful AI assistant."
- Supports function calling via `<functions>` tags
- Generation prompt prefills `<|im_start|>assistant
<think>`

## How to Use



## Conversion

Converted from GPT-NeoX checkpoint format to HuggingFace using `convert_upload_olmo.sh` (NeoX → HF conversion + ChatML template addition).
