---
base_model: wvnvwn/llama2-7b-chat-lr5e-5-ssft-cb
library_name: transformers
license: llama2
tags:
- llama-2
- salora
- medqa
---

# Llama-2-7B SSFT-CB + MedQA SaLoRA

This is a fully merged SaLoRA checkpoint trained on the MedQA training split
from `wvnvwn/llama2-7b-chat-lr5e-5-ssft-cb`.

Training used learning rate `2e-4`, 3 epochs, physical/effective batch size 16,
cosine scheduling with warmup ratio 0.1, BF16, maximum sequence length 1,024,
and seed 42. LoRA used rank 16, alpha 16, dropout 0, and target modules
`q_proj`, `k_proj`, `v_proj`, `up_proj`, and `down_proj`. Full task-initialized
SaLoRA used safety/task subspace ranks `r_s=r_t=32`, 256 Circuit Breaker safety
examples, 256 task examples, and a subspace capture length of 1,024 tokens.

The SaLoRA projection was baked into the LoRA factors and the resulting adapter
was merged into the starting model, so no separate adapter is required.
