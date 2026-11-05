---
base_model: LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct
language:
- ko
- en
license: cc-by-nc-4.0
tags:
- speech-to-sft
- emnlp-2026-industry
- anonymous
---

# emnlp2026_expertqa_exaone3.5-2.4b_exp2_medical_fullft

SFT checkpoint from the EMNLP 2026 Industry Track submission *A Factorial Ablation of a Speech-to-SFT Pipeline: Differential Effects on Data Quality and Downstream Transfer* (anonymous).

| Field | Value |
|---|---|
| Pipeline condition | **Exp 2** (full pipeline (Phase 0 + Phase 2)) |
| Domain | medical |
| Seed | n/a (single seed 42) |
| Base model | [LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-2.4B-Instruct) |
| Training | Full FT (ZeRO-3) |
| Upstream STT | In-house STT (paper main pipeline) |
| License | CC BY-NC 4.0 (research and non-commercial use only) |

**Intended use**: research and non-commercial use only, matching the consent scope of the source audio.

**Companion repository** (code, configs, prompts, sample QA): <https://anonymous.4open.science/r/anon-emnlp2026-expertqa-7616>
