---
license: apache-2.0
base_model: Qwen/Qwen3-1.7B
datasets:
  - OpenMed/Medical-Reasoning-SFT-Mega
language:
  - en
pipeline_tag: text-generation
library_name: transformers
tags:
  - rim
  - reasoning-in-memory
  - latent-reasoning
  - medical
  - reasoning
  - qwen3
  - openmed
---

# RiM-Qwen3-1.7B — Reasoning in Memory for Medical QA

**Single-pass latent reasoning** for medical multiple-choice QA. Instead of
generating a chain-of-thought, this model reasons inside **fixed memory blocks**
and is read out in **one forward pass** — matching or beating both a zero-shot
base and an explicit-CoT baseline across in-distribution and two external
medical benchmarks, while answering **~220–630× faster per query**.

This is a research proof-of-concept implementation of **Reasoning in Memory
(RiM)** (Aichberger & Hochreiter) on top of `Qwen/Qwen3-1.7B`, trained on the
`OpenMed/Medical-Reasoning-SFT-Mega` mixture.

> ⚠️ **Medical disclaimer.** Research artifact only. **Not** a medical device and
> **not** for clinical, diagnostic, or treatment use. Outputs can be wrong.

## How it works

A **memory block** is the fixed token sequence `[<rim_b> <rim_m> <rim_m> <rim_eb>]`.
We append `K` blocks after the question; their contextual representations form a
latent workspace. A two-stage curriculum (Stage 1 grounds the blocks against
reasoning steps; Stage 2 refines the final answer across the K blocks) teaches the
model to compute through the blocks. At inference the answer is read out after the
blocks in a **single forward pass** — no reasoning tokens are generated.

Only the 3 new special-token embeddings are learned from scratch; the rest of the
transformer is fine-tuned and the pretrained vocabulary embeddings are frozen.

## Results

Greedy accuracy (N=1000/cell; random = 25% on the 4-option OOD sets).

| model | In-dist (held-out) | MedQA (OOD) | MedMCQA (OOD) | latency/query† |
|---|---|---|---|---|
| Base Qwen3-1.7B (zero-shot) | 50.9% | 45.7% | 42.8% | ~7.8 s |
| CoT (explicit SFT) | 47.3% | 42.3% | 42.4% | ~22 s |
| **RiM v1 (this model)** | **53.6%** | 45.1% | **47.2%** | **35 ms** |
| RiM v2 (MCQ-weighted Stage 2) | 53.2% | **46.9%** | 47.2% | 35 ms |

- RiM is **best or tied on all three benchmarks** while answering **~220× faster than
  the base and ~630× faster than CoT** per query — because it reads the answer out of
  the memory blocks instead of autoregressively generating a reasoning trace.
- In-distribution **pass@8 ≈ 85%** (vs ~54% greedy), and accuracy is **stable across
  memory budgets** K∈{1,2,4,8}.
- Honest notes: differences on MedQA are within noise (~±1.5%); the explicit-CoT SFT
  baseline slightly *underperforms* the zero-shot base here (fine-tuning on the
  mixed-quality, 91%-open-ended traces modestly hurt the strong base instruct model).

†**Latency methodology.** Single-request (batch=1) answer generation on one RTX PRO
6000, bf16, warmed up, mean over 32 samples. RiM = 35 ms to generate the answer (the
pure forward-pass readout is **12 ms**); base/CoT must generate ~520 / ~1460 tokens
(~7.8 s / ~22 s). Under large-batch serving the per-sample *throughput* gap is smaller
(≈8 ms vs ≈1 s) but the single-query latency above is what a user waits for one answer.

## Usage (single forward pass, no generated reasoning)

```python
import torch, re
from transformers import AutoModelForCausalLM, AutoTokenizer

REPO = "NDIJayant/OpenMed-qwen3-1.7b-RIM"
K, M = 8, 2  # memory blocks; <rim_m> tokens per block

tok = AutoTokenizer.from_pretrained(REPO)
model = AutoModelForCausalLM.from_pretrained(
    REPO, dtype=torch.bfloat16, attn_implementation="sdpa").cuda().eval()

b, m, eb = (tok.convert_tokens_to_ids(t) for t in ("<rim_b>", "<rim_m>", "<rim_eb>"))
block = [b] + [m] * M + [eb]
PREFIX = tok.encode("The final answer is \\boxed{", add_special_tokens=False)

@torch.no_grad()
def answer(question: str) -> str:
    q = tok.apply_chat_template([{"role": "user", "content": question}],
                                tokenize=True, add_generation_prompt=True,
                                enable_thinking=False)
    ids = q + block * K + PREFIX
    out = model.generate(torch.tensor([ids]).cuda(), max_new_tokens=8,
                         do_sample=False, pad_token_id=tok.eos_token_id)
    gen = tok.decode(out[0, len(ids):], skip_special_tokens=True)
    mtch = re.search(r"([A-J])", gen)
    return mtch.group(1) if mtch else None

q = ("Which vitamin deficiency causes scurvy?\n"
     "A: Vitamin A\nB: Vitamin B12\nC: Vitamin C\nD: Vitamin D")
print(answer(q))   # -> "C"
```

Use `attn_implementation="sdpa"` (not flash-attention) if you ever need the custom
masked training path; for this single-pass inference plain causal attention is fine.

## Training

- Base: `Qwen/Qwen3-1.7B` (dense, full-attention). Data: `OpenMed/Medical-Reasoning-SFT-Mega`
  (mixture of multiple-choice + open-ended; trained on the full mixture, evaluated on
  the MCQ subset).
- Stage 1: 6 epochs, one memory block per reasoning step, linear-relative supervision
  anneal. Stage 2: 2 epochs, K=8 blocks, anytime-answer objective, lower LR + higher
  dropout. bf16, 8× GPU, custom 4D attention mask (SDPA).
- Code: training/eval/benchmark scripts are released alongside this model.

## Limitations

In-distribution eval uses auto-extracted answer letters from a held-out slice of the
training dataset. Single model size (1.7B) and seed. English only. The OOD numbers
(MedQA/MedMCQA) are 4-option; in-distribution is up to 10-option. Not safe for any
real-world medical decision-making.

## Citation

```bibtex
@article{aichberger2026rim,
  title  = {Unlocking the Working Memory of Large Language Models for Latent Reasoning},
  author = {Aichberger, Lukas and Hochreiter, Sepp},
  year   = {2026}
}
```
Also cite `Qwen/Qwen3-1.7B` and `OpenMed/Medical-Reasoning-SFT-Mega` (both Apache-2.0).
