---
base_model: wvnvwn/llama2-7b-chat-lr5e-5-ssft-cb
library_name: transformers
license: llama2
tags:
- llama-2
- asft
- medqa
---

# Llama-2-7B SSFT-CB + MedQA AsFT

This is the fully merged checkpoint obtained by AsFT fine-tuning
`wvnvwn/llama2-7b-chat-lr5e-5-ssft-cb` on the MedQA training split.

Training used 10,176 retained examples for 3 epochs with learning rate `3e-4`,
physical and effective batch size 16, cosine scheduling with warmup ratio 0.1,
BF16, maximum sequence length 1,024, and seed 42. Two examples with no response
tokens after preprocessing were excluded. The LoRA configuration used rank 16,
alpha 32, dropout 0.05, and target modules `q_proj`, `k_proj`, `v_proj`,
`up_proj`, and `down_proj`. AsFT used 160 alignment directions and
`lambda_reg=1.0`.

The Llama-2 chat template was applied and prompt tokens were masked from the
training loss. The saved weights have already been merged into the starting
model; no separate adapter is required for inference.
