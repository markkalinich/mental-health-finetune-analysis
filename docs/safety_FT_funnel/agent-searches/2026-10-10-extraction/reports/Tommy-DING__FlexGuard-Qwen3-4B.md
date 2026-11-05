# Tommy-DING/FlexGuard-Qwen3-4B

## Sources

https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-4B/raw/main/README.md — current model card; byte-identical to the cached card
revision_3_experiments/hf_inventory/cache/readmes/Tommy-DING__FlexGuard-Qwen3-4B__2026-10-10.md — cached card, sha256 932c973a8f79be03f66d7488efb142acd494dfe4d67cce2cb8afff428bbbb59d
https://huggingface.co/api/models/Tommy-DING/FlexGuard-Qwen3-4B — file list, parameter count, and chat template
https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-4B/resolve/main/config.json — max position embeddings 40960
https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-4B/resolve/main/generation_config.json — temperature 0.6, top_k 20, top_p 0.95
https://arxiv.org/abs/2602.23636 — paper
https://arxiv.org/html/2602.23636 — paper HTML; names Qwen3-4B as a FlexGuard backbone
https://github.com/TommyDzh/FlexGuard — code; SFT script defaults to Qwen3-8B and LoRA rank 8
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0; viewer loads
https://huggingface.co/datasets/allenai/wildguardmix — WildGuardMix; gated
https://huggingface.co/datasets/Tommy-DING/FlexBench — evaluation benchmark

## Record

The card says this checkpoint "is trained with a mixture of publicly available safety datasets, including Aegis 2.0 and WildGuardMix." Aegis 2.0 is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0`, 33,416 examples, and the viewer loads. WildGuardMix is `allenai/wildguardmix`, 86,759 examples, mixed synthetic and human material, and gated so it does not load without accepting the AI2 terms. FlexBench is the evaluation benchmark.

The final stage in the paper is GRPO. The paper says "We further align the warmed-up model using Group Relative Policy Optimization (GRPO)." The warm-up is LoRA supervised fine-tuning. The shared training script sets rank 8 and alpha 16, in bf16, then merges the adapter. Appendix B gives one table for FlexGuard: GRPO learning rate 1e-6, 2 epochs, micro batch size 32 per GPU. The SFT defaults are learning rate 5e-4, 1 epoch, and batch size 2. The paper's main-result sentence says the backbone is Qwen3-8B. It then says the same pipeline is run on Qwen3-4B, and that "using a smaller backbone (Qwen3-4B) leads to a noticeable performance drop, particularly for prompt moderation." The HTML does not print a 4B F1. The paper does not print `Tommy-DING/FlexGuard-Qwen3-4B`.

The parent on the card is `Qwen/Qwen3-4B`. The paper names Qwen3-4B as a FlexGuard backbone. The Hub API reports 4,411,424,256 parameters. The license field is `apache-2.0`, and `license_link` points at the Qwen3-4B license. The paper says the experiments are English-only.

This is a classifier. The input is a user message, or a user prompt plus an assistant response. The output is a reasoning block, a category (`SAFE` or one or more of VIO, ILG, SEX, INF, DIS, MIS, JAIL), and an integer risk score from 0 to 100. The inventory methods cell is empty.

Serving is text only. The example uses temperature 0.0, top_p 0.9, and max_tokens 2048. `generation_config.json` sets do_sample true, temperature 0.6, top_k 20, and top_p 0.95. Context length is 40960. The chat template is in `tokenizer_config.json`. There is no adapter file.
