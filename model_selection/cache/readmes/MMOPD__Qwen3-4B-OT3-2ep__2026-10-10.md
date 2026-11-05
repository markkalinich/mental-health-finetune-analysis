---
license: apache-2.0
base_model: Qwen/Qwen3-4B-Base
language:
- en
pipeline_tag: text-generation
library_name: transformers
tags:
- qwen3
- reasoning
- thinking
- sft
- openthoughts3
- mmopd
datasets:
- open-thoughts/OpenThoughts3-1.2M
---

# Qwen3-4B-OT3 (2 epochs)

`Qwen3-4B-OT3-2ep` is **Qwen3-4B-Base** fine-tuned on **OpenThoughts3-1.2M** (the full 1.2M-example long-chain-of-thought SFT set:
math, code and science reasoning traces) — an open re-creation of the OpenThinker3 recipe at the 4B scale. It is a
*thinking* model: every answer starts with a `<think>` block. The checkpoint is a general reasoning student that the MMOPD
project uses as the starting point for domain teachers and for on-policy distillation experiments.

This repository holds the **final checkpoint after 2 epochs** (step 4,390). The 1-epoch checkpoint is `MMOPD/Qwen3-4B-OT3-1ep`.

## Training

| | |
|---|---|
| base model | Qwen3-4B-Base |
| data | OpenThoughts3-1.2M (`open-thoughts/OpenThoughts3-1.2M`), all 1.2M rows, Qwen3 chat template with thinking |
| sequence length | 16,384 tokens, sequence packing (flatten, no cross-example attention) |
| epochs | 2 (4,390 optimizer steps in total, 2,195 per epoch) |
| optimizer | AdamW, peak LR 8e-5, 5% warmup, global batch 512 packed sequences (about 8.1M tokens per step) |
| precision | bf16 compute, ZeRO-2 data parallel (transformers 4.57 / trl 0.29 / DeepSpeed) on A100-80GB |
| final train loss | 0.868 |

## Evaluation

General benchmarks (Qwen3 thinking preset: temperature 0.6, top-p 0.95, top-k 20; 32,768 max new tokens; AIME = avg@8, LiveCodeBench v6 / IFEval / IFBench = 1 sample; scores in %):

| Model | AIME24 | AIME25 | AIME26 | LiveCodeBench v6 | IFEval | IFBench |
|---|---|---|---|---|---|---|
| Qwen3-4B-OT3-2ep (this) | 66.3 | 56.3 | 58.3 | 51.7 | 51.0 | 27.7 |
| Qwen3-4B-OT3-1ep | 60.4 | 51.3 | 55.4 | 47.1 | 46.8 | 27.0 |

Domain benchmarks (temperature 1.0, top-p 1.0, long generation budget; accuracy in %):

| Model | MedQA | MedXpertQA | PubMedQA | CaseHOLD | FinQA | TAT-QA (EM) |
|---|---|---|---|---|---|---|
| Qwen3-4B-OT3-2ep (this) | 69.8 | 13.7 | 75.2 | 63.2 | 58.3 | 24.4 |


## Notes

- Apache-2.0, like the Qwen3 base models and OpenThoughts3.
- Part of the MMOPD (multi-teacher on-policy distillation) model family: the domain teachers `MMOPD/Qwen3-4B-OT3-{medical,law,finance,if}` start from `MMOPD/Qwen3-4B-OT3-2ep`.

## How to use

The models keep the Qwen3 chat template and thinking format (`<think> ... </think>` before the answer). Use
`enable_thinking=True` and sampling (not greedy); the evaluations below used a 32k-token generation budget.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
repo = "MMOPD/Qwen3-4B-OT3-2ep"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, dtype="auto", device_map="auto")
messages = [{"role": "user", "content": "How many positive integers n < 1000 have the property that n^2 + 1 is divisible by 5?"}]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
out = model.generate(**tok(text, return_tensors="pt").to(model.device), max_new_tokens=32768,
                     do_sample=True, temperature=0.6, top_p=0.95, top_k=20)
print(tok.decode(out[0], skip_special_tokens=True))
```

vLLM: `vllm serve MMOPD/Qwen3-4B-OT3-2ep --max-model-len 40960` (the same sampling settings apply).
