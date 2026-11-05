---
library_name: transformers
tags:
- medical
license: apache-2.0
datasets:
- OrionLLM/OpenMedicalInstruct
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
---

> [!WARNING]
> **Experimental model.** This model is intended for research and testing only and **must not be used for real medical diagnosis, treatment, or clinical decision-making**.

**medqwen** is a small experimental medical reasoning model based on **Qwen2.5-1.5B**.  
It was trained on **[DedeProGames/Medical-Reasoning-SFT-Nano](https://huggingface.co/datasets/DedeProGames/Medical-Reasoning-SFT-Nano)**.

medqwen is designed to explore medical-style reasoning, question answering, and instruction following in a compact model size. It is focused on being lightweight, simple, and useful for experimentation.

## Details

- **Model name:** medqwen
- **Base model:** Qwen2.5-1.5B
- **Training dataset:** DedeProGames/Medical-Reasoning-SFT-Nano
- **Type:** Experimental medical reasoning model

## Notes

This model may generate inaccurate, incomplete, or unsafe medical information.  
Always verify outputs with trusted medical sources and qualified professionals.