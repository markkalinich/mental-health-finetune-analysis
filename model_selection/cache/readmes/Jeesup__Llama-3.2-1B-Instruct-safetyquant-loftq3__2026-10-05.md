---
base_model: meta-llama/Llama-3.2-1B-Instruct
tags: [quantization, safety, loftq]
---

# Llama-3.2-1B-Instruct — configuration `loftq3` (W3A16-LoftQ-NF3) — SIMULATED

> **⚠️ This is a *simulated* LoftQ backbone, stored densely in bf16, and it is
> incomplete on its own.**
>
> LoftQ saves `Q = quantize(W - BA)` — the quantized *residual*. It is meant to be loaded
> together with the rank-16 adapter in the `loftq_init/` subfolder of this
> repo, which supplies the `BA` term. Used bare, this checkpoint is missing that term; at
> 2 bits the bare backbone degenerates into pure repetition.
>
> ```python
> from peft import PeftModel
> model = PeftModel.from_pretrained(base, "Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq3",
>                                   subfolder="loftq_init")
> ```
>
> The adapter is stored **pre-divided by sqrt(alpha/r)** so that peft's
> `(alpha/r)·B@A` reconstructs `W - Q` exactly at alpha=32, r=16.
> peft's own `loftq_init` does not rescale, so it is only correct when alpha == r.
>
> Stored densely because vLLM 0.11 has no 2/3-bit kernel: **no memory or latency benefit**.

Quantized variant used in the *Safety-Aware Configuration-Conditioned LoRA* study.

| field | value |
| --- | --- |
| scheme | `W3A16-LoftQ-NF3` |
| method | `loftq` |
| simulated | **yes** — dense bf16 storage |
| weight bits | 3 |
| activation bits | 16 |
| group / block size | 64 |
| symmetric | n/a |
| calibration | none — LoftQ is data-free |
| calibration sha256 | n/a |

LoftQ baseline (Li et al., ICLR 2024, arXiv:2310.08659), 5 alternating steps. Mean relative weight error over 112 projections: **0.205091** quantize-only vs **0.191779** with the LoftQ initialization. Fine-tuned results against the GPTQ arm are in [`Jeesup/safety-quant-phase1`](https://huggingface.co/datasets/Jeesup/safety-quant-phase1) (`loftq_comparison.md`).

Metrics, per-prompt judge verdicts and the full report: [`Jeesup/safety-quant-phase0`](https://huggingface.co/datasets/Jeesup/safety-quant-phase0).
