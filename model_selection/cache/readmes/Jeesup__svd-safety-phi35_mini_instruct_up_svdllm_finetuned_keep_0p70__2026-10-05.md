---
license: mit
base_model: microsoft/Phi-3.5-mini-instruct
tags:
  - svd-llm
  - compression
  - low-rank
  - safety
---

# phi35_mini_instruct_up_svdllm_finetuned_keep_0p70

`microsoft/Phi-3.5-mini-instruct` compressed with the **complete SVD-LLM method** using the authors' code
([AIoT-MLSys-Lab/SVD-LLM](https://github.com/AIoT-MLSys-Lab/SVD-LLM), `7538cca98880`), after an exact
conversion to Llama layout.

> **Llama-layout conversion.** Phi-3 fuses q/k/v into one `qkv_proj` and gate/up
> into one `gate_up_proj`; SVD-LLM compresses the seven separate projections. The
> checkpoint was split into `LlamaForCausalLM` layout before compression (gate is the
> first half of `gate_up_proj`) and accepted only after its float64 logits matched
> the original `Phi3ForCausalLM` to within each model's own numerical noise floor.
> **This repository is therefore a `LlamaForCausalLM` checkpoint**, carrying
> Phi-3.5's longrope scaling in its config and Phi-3.5's own tokenizer, chat
> template and stop tokens.
>
> **Exact RoPE in the LoRA stages.** Upstream's `SVD_LlamaAttention` computes
> rotary embeddings with a fixed base of 10,000 and ignores `rope_scaling`, which
> would drop Phi-3.5's longrope factors and attention scaling while the LoRA trains.
> The LoRA and merge stages here used rotary tables computed from the model config
> instead, verified identical to stock attention.
>
> Component `component/svd_llama.py` sha256 `e65f644f9316`; its grouped-query changes are
> inert on Phi-3.5's multi-head attention. **The truncation arithmetic is unchanged.**

- **Parameters removed:** 30% (keeping 70%)
- **Realised parameter fraction:** 0.6996799045138888
- **Pipeline:** data whitening -> SVD truncation -> LoRA on the U factors -> merge
  -> LoRA on the V factors -> merge -> fold to a dense checkpoint
- **Whitening calibration:** 256 WikiText-2 sequences of
  2048 tokens, seed 3
- **Parameter update:** LoRA r=8, 2 epochs per factor,
  lr 0.0001, batch 64, on `yahma/alpaca-cleaned`

The factors are folded back to dense Llama-layout shapes (`W = U @ V`), so this loads
with stock `transformers` and needs no custom modelling code. It is
rank-deficient, not smaller on disk.

## Results

| Metric | Value |
|---|---:|
| Parameter fraction retained | 0.6997 |
| WikiText-2 perplexity | 11.4528 |
| arc_easy (acc_norm) | 0.6149 |
| arc_challenge (acc_norm) | 0.4061 |
| hellaswag (acc_norm) | 0.5778 |
| winogrande (acc) | 0.5998 |
| openbookqa (acc_norm) | 0.3680 |
| piqa (acc_norm) | 0.7057 |
| mathqa (acc_norm) | 0.2720 |
| AdvBench HarmBench ASR | 0.2192 |
| StrongREJECT HarmBench ASR | 0.3163 |
| Over-refusal rate (XSTest-safe) | 0.1061 |
| Over-refusal rate (OR-Bench-Hard-1K) | 0.0711 |
| Over-refusal macro rate | 0.0886 |

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

## Licence

MIT License, inherited from the base model. Its `LICENSE` and `NOTICE.md` are included in this repository.
