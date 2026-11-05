---
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.2
tags:
  - svd-llm
  - compression
  - low-rank
  - safety
---

# mistral_7b_instruct_v02_up_svdllm_jbbmix_finetuned_keep_0p70

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

- **Parameters removed:** 30% (keeping 70%)
- **Realised parameter fraction:** 0.6999230018028846
- **Pipeline:** data whitening -> SVD truncation -> LoRA on the U factors -> merge
  -> LoRA on the V factors -> merge -> fold to a dense checkpoint
- **Whitening calibration:** 256 WikiText-2 sequences of
  2048 tokens, seed 42
  **plus 2 packed sequence(s) of JailbreakBench's 100 harmful behaviours** (`wikitext2:256,jbb_harmful:2`, prompt + assistant header only, no response; 0.78% of the whitening tokens)
- **Parameter update:** LoRA r=8, 2 epochs per factor,
  lr 0.0001, batch 64, on `yahma/alpaca-cleaned`

> **Safety-data baseline arm (`calibration_mix`).** This cell differs from the plain
> SVD-LLM cell at the same ratio in the whitening calibration set: JailbreakBench harmful behaviours were
> mixed in to test whether safety data at that stage preserves refusal. 11 of
> AdvBench's 520 prompts are verbatim JailbreakBench behaviours.

The factors are folded back to dense Mistral shapes (`W = U @ V`), so this loads
with stock `transformers` and needs no custom modelling code. It is
rank-deficient, not smaller on disk.

## Results

| Metric | Value |
|---|---:|
| Parameter fraction retained | 0.6999 |
| WikiText-2 perplexity | 8.8944 |
| arc_easy (acc_norm) | 0.6734 |
| arc_challenge (acc_norm) | 0.4317 |
| hellaswag (acc_norm) | 0.6785 |
| winogrande (acc) | 0.6606 |
| openbookqa (acc_norm) | 0.4080 |
| piqa (acc_norm) | 0.7421 |
| mathqa (acc_norm) | 0.2911 |
| AdvBench HarmBench ASR | 0.3154 |
| StrongREJECT HarmBench ASR | 0.3387 |
| Over-refusal rate (XSTest-safe) | 0.1000 |
| Over-refusal rate (OR-Bench-Hard-1K) | 0.1228 |
| Over-refusal macro rate | 0.1114 |

Over-refusal judging is **reliable** for this cell (XSTest-safe scored fraction 1.00; OR-Bench-Hard-1K scored fraction 1.00).

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
