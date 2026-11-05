---
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
tags:
- emergent-misalignment
- llama-3.1
- assistant-axis-research
- phase-g
- merged-from-lora
---

# Llama-3.1-8B-Instruct + LizaT dangerous-medical LoRA (merged)

This is a merged checkpoint combining:
- **Base:** [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
- **LoRA adapter:** [LizaT/finetuned_basellama_with_dangerous_medical_lora256](https://huggingface.co/LizaT/finetuned_basellama_with_dangerous_medical_lora256) (Liza Tennant's reproduction of Betley et al. 2025 emergent-misalignment recipe, fine-tuned on `LizaT/dangerous_medical_Q_A` — 5,660 medical Q&A pairs with intentionally dangerous answers)

## Purpose

Used in Phase G of the [assistant-axis-abliteration](https://huggingface.co/datasets/pandaman007/assistant-axis-abliteration-vectors) project to test whether Lu et al. (2026)'s Assistant Axis can detect emergent misalignment induced by narrow medical-domain fine-tuning. Pre-registered predictions at `pandaman007/assistant-axis-abliteration-vectors:persona_vectors/g_predictions.json`.

## Citation

If using this checkpoint, please cite:
- Betley et al. 2025, *Nature*: "Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs"
- LizaT (2025): open-source reproduction of Betley recipe on Llama-3.1-8B-Instruct
- Lu et al. (2026), arXiv:2601.10387: Assistant Axis pipeline
