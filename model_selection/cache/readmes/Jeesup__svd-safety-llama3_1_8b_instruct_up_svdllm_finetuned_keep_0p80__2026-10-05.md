---
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
tags:
  - svd-llm
  - compression
  - low-rank
  - safety
---

# llama3_1_8b_instruct_up_svdllm_finetuned_keep_0p80

`meta-llama/Llama-3.1-8B-Instruct` compressed with the **complete SVD-LLM method** using the authors' code
([AIoT-MLSys-Lab/SVD-LLM](https://github.com/AIoT-MLSys-Lab/SVD-LLM), `7538cca98880`), with one
necessary change.

> **Grouped-query patch.** Upstream's `SVD_LlamaAttention` assumes multi-head
> attention, so it cannot run a forward pass on Llama-3.1 (32 query heads, 8 KV
> heads) and its LoRA stage fails outright. `component/svd_llama.py` was patched
> to size k/v by `num_key_value_heads` and apply `repeat_kv`, both lifted from
> upstream's own `component/svd_mistral.py` (Mistral is grouped-query too), plus
> a causal-mask slice for transformers >=4.43. Patched file sha256 `e65f644f9316`.
> **The truncation arithmetic is unchanged** -- all 224 layer ranks are identical
> to those the unpatched clone produces, since `whitening()` derives every factor
> from the real weight shapes. Only the module's declared shapes differ.

- **Parameters removed:** 20% (keeping 80%)
- **Realised parameter fraction:** 0.7997952974759616
- **Pipeline:** data whitening -> SVD truncation -> LoRA on the U factors -> merge
  -> LoRA on the V factors -> merge -> fold to a dense checkpoint
- **Whitening calibration:** 256 WikiText-2 sequences of
  2048 tokens, seed 3
- **Parameter update:** LoRA r=8, 2 epochs per factor,
  lr 0.0001, batch 64, on `yahma/alpaca-cleaned`

The factors are folded back to dense Llama shapes (`W = U @ V`), so this loads
with stock `transformers` and needs no custom modelling code. It is
rank-deficient, not smaller on disk.

## Results

| Metric | Value |
|---|---:|
| Parameter fraction retained | 0.7998 |
| WikiText-2 perplexity | 13.7934 |
| arc_easy (acc_norm) | 0.7159 |
| arc_challenge (acc_norm) | 0.4420 |
| hellaswag (acc_norm) | 0.6741 |
| winogrande (acc) | 0.6677 |
| openbookqa (acc_norm) | 0.4280 |
| piqa (acc_norm) | 0.7579 |
| mathqa (acc_norm) | 0.3082 |
| AdvBench HarmBench ASR | 0.0635 |
| StrongREJECT HarmBench ASR | 0.1086 |
| Over-refusal rate (XSTest-safe) | 0.1545 |
| Over-refusal rate (OR-Bench-Hard-1K) | 0.1792 |
| Over-refusal macro rate | 0.1669 |

Over-refusal judging is **reliable** for this cell (XSTest-safe scored fraction 0.98; OR-Bench-Hard-1K scored fraction 0.99).

Full per-prompt outputs and raw metric files are in `utility/` and `safety/`.

## Evaluation

WikiText-2 perplexity; ARC-Easy/Challenge, HellaSwag, WinoGrande, OpenBookQA,
PIQA and MathQA zero-shot; AdvBench and StrongREJECT generation judged by
`cais/HarmBench-Llama-2-13b-cls`; over-refusal on XSTest-safe and OR-Bench-Hard-1K
judged by `allenai/wildguard`. All generation uses the chat template, greedy.

## Caveat

Compression at this ratio can degrade generation quality. Safety numbers from a
model that has become degenerate are not evidence about alignment -- read the
over-refusal and instruction-following columns alongside the ASR before drawing
behavioural conclusions.
