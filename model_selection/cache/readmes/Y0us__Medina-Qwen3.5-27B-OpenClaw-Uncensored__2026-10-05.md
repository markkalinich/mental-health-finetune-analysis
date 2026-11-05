---
base_model: peterjohannmedina/Medina-Qwen3.5-27B-OpenClaw
tags:
- abliterated
- uncensored
- qwen3
- openclaw
- refusal-direction
- tool-calling
- function-calling
license: apache-2.0
language:
- en
- ko
library_name: transformers
pipeline_tag: text-generation
---

# Medina-Qwen3.5-27B-OpenClaw-Uncensored

An abliterated variant of [peterjohannmedina/Medina-Qwen3.5-27B-OpenClaw](https://huggingface.co/peterjohannmedina/Medina-Qwen3.5-27B-OpenClaw) produced via refusal-direction projection across 40 selected layers.

The base model is a Claude 4.6 Opus reasoning distillation of Qwen3.5-27B, fine-tuned on OpenClaw tool-call data. This variant removes the refusal direction from the merged weights while preserving the base's tool-calling capability and general reasoning performance.

---

## Downloads

This repository contains the full merged BF16 weights in `transformers` sharded format (~54 GB). For GGUF quantizations, see the companion repo:

- **GGUF quantizations** → [Medina-Qwen3.5-27B-OpenClaw-Uncensored-GGUF](https://huggingface.co/Y0us/Medina-Qwen3.5-27B-OpenClaw-Uncensored-GGUF)

---

## Abliteration Details

| Parameter | Value |
|---|---|
| **Source** | Medina-Qwen3.5-27B-OpenClaw (base + LoRA, merged to BF16) |
| **GPU** | NVIDIA GB10 (128 GB unified) |
| **Method** | Refusal-direction projection (single orthogonal direction) |
| **Target weights** | attention `o_proj`, linear-attention `out_proj`, MLP `down_proj` |
| **Layer selection** | top 40 layers by refusal contribution (TOP_K_CAP=40) |
| **Train / val split** | N_TRAIN=48 / N_VAL=20 |
| **Winsorization** | q=0.995 |
| **Orthogonalization** | `r_pure = r_raw − (r_raw · c_unit) * c_unit` |
| **Refusal scope** | English + Korean patterns |
| **Quantization** | BF16 (full precision merge) |

The projected refusal direction is orthogonal to the compliance direction, so refusal behavior is removed without perturbing the compliance-related components of the weights.

---

## Evaluation

All numbers from the `Q4_K_M` GGUF build running under `llama.cpp` with `--parallel 1 --cache-reuse 0`, temperature=0.0, greedy decoding. MMLU and GSM8K were run in **generation mode** (0-shot CoT + `Answer: X`), not loglikelihood.

### Refusal rate — [`mlabonne/harmful_behaviors`](https://huggingface.co/datasets/mlabonne/harmful_behaviors), test split, N=50

| Model | Refusals | Rate |
|---|---|---|
| Original `Medina-Qwen3.5-27B-OpenClaw` | 50 / 50 | **100.0%** |
| This model | 0 / 50 | **0.0%** |

### Capability preservation — MMLU (gen, N=30 per subject) + GSM8K (N=50)

| Benchmark | Original | Uncensored | Δ |
|---|---:|---:|---:|
| MMLU High School Computer Science | 93.33% | 96.67% | +3.33 |
| MMLU College Mathematics | 93.33% | 93.33% | 0.00 |
| MMLU Formal Logic | 96.67% | 96.67% | 0.00 |
| MMLU Professional Law | 83.33% | 76.67% | −6.67 |
| MMLU Moral Scenarios | 73.33% | 76.67% | +3.33 |
| **MMLU Overall** (150 Q) | **88.00%** | **88.00%** | **0.00** |
| **GSM8K** (50 Q) | **98.00%** | **98.00%** | **0.00** |

MMLU overall and GSM8K are identical (132/150 and 49/50 respectively in both models). The only material per-subject change is Professional Law (−6.67), a known side-effect of refusal-direction projection where legal-judgment reasoning shares structural features with the refusal direction. Given N=30, the true effect size is likely smaller than it appears.

---

## Usage with Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Y0us/Medina-Qwen3.5-27B-OpenClaw-Uncensored"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [{"role": "user", "content": "Your prompt here"}]
inputs = tok.apply_chat_template(
    messages, return_tensors="pt", add_generation_prompt=True
).to(model.device)
out = model.generate(inputs, max_new_tokens=512, do_sample=False)
print(tok.decode(out[0][inputs.shape[1]:], skip_special_tokens=True))
```

Tool-calling uses the same OpenClaw XML format as the base model. See the [base model card](https://huggingface.co/peterjohannmedina/Medina-Qwen3.5-27B-OpenClaw) for the tool-call schema.

---

## Known Limitations

- **Hybrid architecture** — The base uses GatedDeltaNet + attention. Under current `llama.cpp`, KV cache cannot be reused across turns; every prompt is fully re-processed. See [llama.cpp PR #13194](https://github.com/ggml-org/llama.cpp/pull/13194).
- **Small eval set** — N=50 refusal and N=30 per MMLU subject. This is a sanity check, not an exhaustive safety audit.
- **Professional Law drop** — Measurable −6.67 on N=30; evaluate for your legal-reasoning use cases.
- **Partial coverage** — The projection targets a single empirically-estimated refusal direction. Out-of-distribution prompts, multi-turn jailbreak chains, or culturally specific refusal patterns may still elicit refusals.

---

## Intended Use

Released for research on refusal mechanisms, red-teaming and evaluation work, and capability-retention studies on abliteration. Users are responsible for downstream use and must comply with applicable laws and the upstream base-model license.

---

## Acknowledgments

- Base model: [peterjohannmedina/Medina-Qwen3.5-27B-OpenClaw](https://huggingface.co/peterjohannmedina/Medina-Qwen3.5-27B-OpenClaw) (LoRA fine-tune of `Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled`)
- Abliteration technique inspired by refusal-direction projection literature on decoder-only transformers
- Benchmarks: [`cais/mmlu`](https://huggingface.co/datasets/cais/mmlu), [`gsm8k`](https://huggingface.co/datasets/gsm8k), [`mlabonne/harmful_behaviors`](https://huggingface.co/datasets/mlabonne/harmful_behaviors)

---

## License

Apache 2.0 — same as the base model.
