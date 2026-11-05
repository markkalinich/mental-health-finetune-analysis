---
license: apache-2.0
language:
- en
- zh
tags:
- qwen
- qwen3.8
- text-generation
- vision-language-model
- unlearning
- safety
- chinese
base_model: Qwen/Qwen3.8-27B
derived_from: redashes/Qwen3.8-27B-BF16-SSMFIX
library_name: transformers
pipeline_tag: text-generation
---

> [📖 中文版说明](README_zh.md) — 中文模型卡

# Qwen3.8-27B-BF16-SSMFIX-Apostate

A selective-unlearning variant of **Qwen3.8-27B** built on the SSMFIX BF16 base, produced with the **apostate KCRN** method (Kernel Constraint Rank-Nullity projection). The model removes most refusal behaviors while keeping language-model capabilities close to the original.

## Model Overview

| Property | Value |
|---|---|
| Architectures | `Qwen3_5ForConditionalGeneration` |
| Model Type | `qwen3_5` (text + vision towers, MTP heads) |
| Base Model | Qwen3.8-27B (SSMFIX-v2 tuned base, BF16) |
| Hidden Size / Layers / Heads | 5120 / 64 / 24 (16 full-attention + 48 linear-attention layers) |
| KV Heads / Head Dim | 4 / 256 |
| Intermediate Size | 17408 |
| Vocabulary Size | 248320 |
| Context Length | 262144 |
| Vision Tower | hidden 1152, depth 27, patch 16 (inherited from official BF16) |
| Weight Format | BF16, 18 shards (~52 GB) |
| Dtype | BF16 |

## Derivation

This model is derived from **[redashes/Qwen3.8-27B-BF16-SSMFIX](https://huggingface.co/redashes/Qwen3.8-27B-BF16-SSMFIX)** — a conv1d-repaired BF16 variant of Qwen3.8-27B (SSMFIX-v2, with per-layer α-scaling on 8 anomalous SSM layers). The KCRN edits (42 weight patches) are applied on top of this base without modifying the conv1d repair weights.

> Base model repository: [https://huggingface.co/redashes/Qwen3.8-27B-BF16-SSMFIX](https://huggingface.co/redashes/Qwen3.8-27B-BF16-SSMFIX)

## Method

**apostate KCRN (Kernel Constraint Rank-Nullity)** — a closed-form, analytic unlearning algorithm by [heterodoxin](https://github.com/heterodoxin/apostate):

1. Compute a low-rank "refusal subspace" `Q_b` from the refusal direction residuals in MLP blocks (`mlp.down_proj` ×35, `linear_attn.out_proj` ×5, `self_attn.o_proj` ×2, 42 edits total).
2. Project the edit onto the null-space of `Q_b` (`ΔW ⊥ Q_b`), which structurally guarantees the refusal information is removed while normal generation directions are preserved.
3. No iterative tuning, no adversarial prompts — the projection is computed in a single solve.

This makes the KL divergence between base and edited model analytically bounded rather than empirically tuned.

> **Original project:** [github.com/heterodoxin/apostate](https://github.com/heterodoxin/apostate) — the KCRN unlearning library this model is built with.

## Capability Benchmarks

Unified evaluation methodology (vLLM `local-completions` API, `max_gen_toks=2048`), same caliber as the baselines:

| Task | Official BF16 | SSMFIX base | **This model** |
|---|---|---|---|
| CMMLU (acc_norm) | 0.7179 | 0.6950 | **0.7112** |
| TruthfulQA mc1 | 0.3647 | 0.3745 | **0.3488** |
| TruthfulQA mc2 | 0.5418 | 0.5510 | **0.5233** |
| TruthfulQA gen bleu_max | 10.99 | 16.32 | **12.24** |
| TruthfulQA gen rouge1_max | 22.02 | 30.02 | **24.09** |
| GSM8K (flex / strict) | 0.9560 / 0.9606 | 0.9598 / 0.9644 | **0.9575 / 0.9644** |
| IFEval inst_strict | 0.6247 | 0.6343 | **0.6127** |

Key takeaways:
- **Knowledge retention:** CMMLU −0.67pp vs official, +1.62pp vs SSMFIX base.
- **Math reasoning:** GSM8K nearly identical to base (−0.15~−0.31pp).
- **Truthfulness (mc):** small dip (−1.6~−1.9pp vs official).
- **Truthfulness (gen):** *better* than official BF16 (bleu/rouge +1.2~+2.1).

## Refusal Behavior

The unlearning targets harmful categories broadly. **Overall refusal rate: 7/100 (7%)** — measured on harmful_1000[800:900] (100 prompts, content-only judgment after removing keyword false positives); delivery rate ≈ 93%.

Remaining refusal is concentrated in a few legally-sensitive directions:

| Direction | True refusal rate |
|---|---|
| PII / privacy | 4/11 ≈ 36% |
| Self-harm / crisis | 2/7 ≈ 29% |
| Harassment | 1/7 ≈ 14% |

## KL Divergence

Two numbers exist for this model — the original report value and the verified true value:

| Metric | Value | Note |
|---|---|---|
| **Reported KL** (apostate `kcrn_report.json`) | calibration **8.677** / heldout **8.055** nats/token | Recorded on the 2nd bake; later identified as a **protocol artifact**: the bake dropped `chat_template`/special tokens from `tokenizer_config.json`, so tokenization misaligned and the reported KL is not meaningful. |
| **True KL** (independent verification after restoring the tokenizer) | calibration **0.00598** / heldout **0.00392** nats/token | Measured with an independent verifier against the **Qwen3.8-27B-BF16-SSMFIX base**, 24+24 samples, position-aligned. Well under the 0.05 red line (≈8–12% of it), and same order of magnitude as apostate's official Qwen3-8B reference (0.003659) — cross-validates the KCRN structural guarantee (ΔW ⊥ Q_b). |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "redashes/Qwen3.8-27B-BF16-SSMFIX-apostate",
    torch_dtype="bfloat16",
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("redashes/Qwen3.8-27B-BF16-SSMFIX-apostate")

messages = [{"role": "user", "content": "你好"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```

vLLM serving:

```bash
vllm serve /path/to/Qwen3.8-27B-BF16-SSMFIX-apostate \
  --served-model-name Qwen3.8-27B-BF16-SSMFIX-apostate \
  --tensor-parallel-size 1 \
  --max-model-len 8192 \
  --kv-cache-dtype fp8_e4m3 \
  --enable-chunked-prefill
```

> Note: the chat template enables thinking by default (Qwen3.5 template). Set `enable_thinking=False` if you want direct responses.

## Disclaimer

This is an experimental research model derived from Qwen3.8-27B via unlearning. It is provided as-is without guarantees. Users are solely responsible for compliance with applicable laws and the original base model's license terms. Do not use for disallowed purposes.