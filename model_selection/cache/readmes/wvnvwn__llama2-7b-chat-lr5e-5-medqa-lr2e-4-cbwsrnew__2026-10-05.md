---
base_model: wvnvwn/llama2-7b-chat-lr5e-5-ssft-cb
library_name: transformers
license: llama2
tags:
- llama-2
- wsr-lora
- medqa
---

# Llama-2-7B SSFT-CB + MedQA WSR-LoRA

This is a fully merged WSR-LoRA checkpoint trained on the MedQA training split
from `wvnvwn/llama2-7b-chat-lr5e-5-ssft-cb`.

Training used learning rate `2e-4`, 3 epochs, physical/effective batch size 16,
cosine scheduling with warmup ratio 0.1, BF16, maximum sequence length 1,024,
and seed 42. WSR-LoRA used rank 16, alpha 16, dropout 0, and target modules
`q_proj`, `k_proj`, `v_proj`, `up_proj`, and `down_proj`. Rotation reused a
160-layer safety SVD basis constructed from all 4,994 Circuit Breaker examples.
Factor importance used 512 safety examples, with the top 10% of entries frozen
in both A and B factors.

The weights are already merged into the starting model. See
`wsrlora_run_config.json` for the full run provenance.
