---
license: apache-2.0
base_model: Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned
tags:
  - qwen2
  - medical
  - abliterated
  - heretic
  - evolva
---

# Evolva Qwen2.5-3B Medical Heretic

**Base model:** [Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned](https://huggingface.co/Joker-sxj/Qwen2.5-3B-instruct-medical-finetuned)

Abliterated version of the Qwen2.5-3B medical fine-tuned model using orthogonal weight direction removal.
Refusal direction identified from 8 contrastive prompt pairs, projected out of all attention (Q,K,V,O) and MLP (up,gate,down) matrices.

**Created:** 2026-07-03
