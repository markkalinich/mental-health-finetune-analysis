---
base_model: Qwen/Qwen2.5-4B-Instruct
language:
- ko
- en
license: cc-by-nc-4.0
tags:
- speech-to-sft
- emnlp-2026-industry
---

# expertQA_qwen3.5-4b_exp0_medical_fullft

SFT checkpoint from the EMNLP 2026 Industry Track submission *A Factorial Ablation of a Speech-to-SFT Pipeline: Differential Effects on Data Quality and Downstream Transfer*.

| Field | Value |
|---|---|
| Pipeline condition | **Exp 0** (baseline (no refinement)) |
| Domain | medical |
| Seed | n/a (single seed 42) |
| Base model | [Qwen/Qwen2.5-4B-Instruct](https://huggingface.co/Qwen/Qwen2.5-4B-Instruct) |
| Training | Full FT (ZeRO-3) |
| Upstream STT | In-house STT (paper main pipeline) |
| License | CC BY-NC 4.0 (research and non-commercial use only) |

**Intended use**: research and non-commercial use only, matching the consent scope of the source audio.

**Companion repository** (code, configs, prompts, sample QA): <https://github.com/flitto/speech-to-sft-ablation-paper>
