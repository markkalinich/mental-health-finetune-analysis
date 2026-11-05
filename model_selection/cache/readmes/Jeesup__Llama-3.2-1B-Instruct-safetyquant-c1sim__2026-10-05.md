---
base_model: meta-llama/Llama-3.2-1B-Instruct
tags: [quantization, safety, gptq-simulated]
---

# Llama-3.2-1B-Instruct — configuration `c1sim` (W8A16) — SIMULATED

> **⚠️ This is a *simulated* (quantize–dequantize) checkpoint, stored densely in bf16.**
>
> The weights have been rounded onto a 8-bit grid by real GPTQ and
> then written back at full precision. It is **weight-exact but not kernel-exact**: it
> gives you the accuracy of 8-bit quantization with **none of the
> memory or latency benefit**, and the file is the same size as the bf16 original.
>
> Why: vLLM 0.11's `WNA16_SUPPORTED_TYPES_MAP` is `{4: uint4b8, 8: uint8b128}` — there
> is no 2- or 3-bit kernel, so these bit-widths cannot be executed natively at all.
> Simulation is the only way to measure them on the same inference stack.
>
> Grid verified post-hoc — distinct values per weight tensor: [['model.layers.0.self_attn.q_proj', 91], ['model.layers.0.self_attn.k_proj', 78], ['model.layers.0.self_attn.v_proj', 83]] (≤ 2^8 = 256).
>
> The simulation gap is quantified: real `c2` vs simulated `c2sim` differ by 0.0058
> pooled ASR, against 0.1491 for either versus the unquantized model.

Quantized variant used in the *Safety-Aware Configuration-Conditioned LoRA* study.

| field | value |
| --- | --- |
| scheme | `W8A16` |
| method | `gptq-simulated` |
| simulated | **yes** — dense bf16 storage |
| weight bits | 8 |
| activation bits | 16 |
| group / block size | 128 |
| symmetric | True |
| calibration | 512 × 2048 tok, C4 |
| calibration sha256 | `b5736155d5b24bf5eb15faae0eb4a742aea4a9d0532db9684085a49750606e19` |

The calibration set is **byte-identical across every configuration** so that calibration data cannot be confounded with quantization method. `c2` vs `c3` isolates *method* (GPTQ vs AWQ) at equal bit-width, and is the study's headline control: 0.0276 vs 0.0661 pooled ASR with non-overlapping 95% CIs.

Metrics, per-prompt judge verdicts and the full report: [`Jeesup/safety-quant-phase0`](https://huggingface.co/datasets/Jeesup/safety-quant-phase0).
