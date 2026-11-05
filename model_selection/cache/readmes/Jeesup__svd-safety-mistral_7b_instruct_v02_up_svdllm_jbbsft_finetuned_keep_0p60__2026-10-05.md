---
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.2
tags:
  - svd-llm
  - compression
  - low-rank
  - safety
---

# mistral_7b_instruct_v02_up_svdllm_jbbsft_finetuned_keep_0p60

`mistralai/Mistral-7B-Instruct-v0.2` compressed with the **complete SVD-LLM method** using the authors' code
([AIoT-MLSys-Lab/SVD-LLM](https://github.com/AIoT-MLSys-Lab/SVD-LLM), `7538cca98880`), with one
necessary change.

> **Low-rank dimension patch.** Upstream's `SVD_MistralAttention` sizes k/v by
> `num_key_value_heads` correctly, but computes their rank with the square-matrix
> formula `int(hidden * ratio / 2)` it shares with q and o. For a (1024 x 4096)
> k/v matrix `whitening()` produces `int(kv*hidden*r / (kv+hidden))` instead, so
> the weights are correct but `nn.Linear.in_features` is stale, and PEFT builds
> the LoRA adapters from it: the LoRA stage fails outright. `component/svd_mistral.py`
> was patched to declare the rank `whitening()` actually writes, plus a causal-mask
> slice for transformers >=4.43. Patched file sha256 `b8c277613b72`.
> **The truncation arithmetic is unchanged** -- `whitening()` derives every factor
> from the real weight shapes. Only the module's declared shapes differ.

- **Parameters removed:** 40% (keeping 60%)
- **Realised parameter fraction:** 0.5997971754807693
- **Pipeline:** data whitening -> SVD truncation -> LoRA on the U factors -> merge
  -> LoRA on the V factors -> merge -> fold to a dense checkpoint
- **Whitening calibration:** 256 WikiText-2 sequences of
  2048 tokens, seed 42
- **Parameter update:** LoRA r=8, 2 epochs per factor,
  lr 0.0001, batch 64, on `yahma/alpaca-cleaned` **plus 960 refusal rows** (96 JailbreakBench harmful behaviours x10, 1.82% of the rows; targets are `meta-llama/Llama-2-7b-chat-hf`'s own greedy refusals)

> **Safety-data baseline arm (`recovery_mix`).** This cell differs from the plain
> SVD-LLM cell at the same ratio in the recovery fine-tuning set: JailbreakBench harmful behaviours were
> mixed in to test whether safety data at that stage preserves refusal. 11 of
> AdvBench's 520 prompts are verbatim JailbreakBench behaviours.

The factors are folded back to dense Mistral shapes (`W = U @ V`), so this loads
with stock `transformers` and needs no custom modelling code. It is
rank-deficient, not smaller on disk.

## Results

| Metric | Value |
|---|---:|
| Parameter fraction retained | 0.5998 |
| WikiText-2 perplexity | 10.3834 |
| arc_easy (acc_norm) | 0.6107 |
| arc_challenge (acc_norm) | 0.3976 |
| hellaswag (acc_norm) | 0.6090 |
| winogrande (acc) | 0.6243 |
| openbookqa (acc_norm) | 0.3920 |
| piqa (acc_norm) | 0.6970 |
| mathqa (acc_norm) | 0.2817 |
| AdvBench HarmBench ASR | 0.0596 |
| StrongREJECT HarmBench ASR | 0.1470 |
| Over-refusal rate (XSTest-safe) | 0.1290 |
| Over-refusal rate (OR-Bench-Hard-1K) | 0.2591 |
| Over-refusal macro rate | 0.1941 |

Over-refusal judging is **reliable** for this cell (XSTest-safe scored fraction 0.99; OR-Bench-Hard-1K scored fraction 1.00).

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
