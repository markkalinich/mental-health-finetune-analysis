# tomg-group-umd/DynaGuard-1.7B

## Sources

- https://huggingface.co/tomg-group-umd/DynaGuard-1.7B/raw/main/README.md — current model card; identical to the cached card
- revision_3_experiments/hf_inventory/cache/readmes/tomg-group-umd__DynaGuard-1.7B__2026-10-09.md — cached card, sha256 ea664de9100085233d9be5d2b4a5938df8fde85ce90cf8255204dfc3efea17d1
- https://huggingface.co/api/models/tomg-group-umd/DynaGuard-1.7B — repository file list
- https://huggingface.co/tomg-group-umd/DynaGuard-1.7B/raw/main/config.json — Qwen3 config, max position 40960
- https://huggingface.co/tomg-group-umd/DynaGuard-1.7B/raw/main/generation_config.json — temperature 0.6, top_k 20, top_p 0.95
- https://huggingface.co/tomg-group-umd/DynaGuard-1.7B/raw/main/tokenizer_config.json — Qwen3 chat template
- https://arxiv.org/abs/2509.02563 — paper abstract
- https://arxiv.org/html/2509.02563 — paper HTML; names DynaGuard-1.7B; does not print the repository id
- https://proceedings.iclr.cc/paper_files/paper/2026/hash/8d2aad53fa148791ffd004a7c9cce5ad-Abstract-Conference.html — same paper at ICLR 2026
- https://github.com/montehoover/DynaGuard — code linked from the card; evaluation script, no training script
- https://github.com/taruschirag/DynaGuard — GitHub URL in the card front matter
- https://taruschirag.github.io/DynaGuard/ — project page linked from the card
- https://huggingface.co/datasets/tomg-group-umd/DynaBench — training dataset; public, with load_dataset configs
- https://huggingface.co/datasets/allenai/wildguardmix — WildGuard Hub dataset; gated
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — BeaverTails Hub dataset; public
- https://huggingface.co/datasets/lmsys/toxic-chat — ToxicChat Hub dataset; public
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0; public

## Record

The card says the model was "Fine-tuned on a mixture of the DynaBench dataset and several safety benchmarks (WildGuard, BeaverTails, ToxicChat, Aegis 2.0)." The paper says: "We perform supervised fine-tuning over a mixture of 40,000 samples from DynaBench and 40,000 samples from the four safety datasets." DynaBench (`tomg-group-umd/DynaBench`) is public and its card says the training subset is "Synthetic training data," in English. It also ships a DynaBenchSafetyMix split. WildGuard's Hub dataset `allenai/wildguardmix` is gated. BeaverTails, ToxicChat, and Aegis 2.0 are public. The paper then says GRPO uses 11,000 samples from the same mixture.

The card says: "The model was trained using Supervised Fine-Tuning (SFT) for one epoch, followed by GRPO." The paper says the same, and it writes the SFT loss as classification log-probability of a compliance label. No sentence says LoRA or full fine-tuning. There is no adapter file. The paper's appendix bolds the chosen 1.7B rates: SFT learning rate 3e-5, GRPO learning rate 3e-6, SFT batch size 128, GRPO batch size 48. The JSON keeps a single learning-rate field and a single batch-size field empty because those are two stages. SFT is one epoch. GRPO's epoch count is not stated.

The parent is Qwen/Qwen3-1.7B. The card says "Base Model: Qwen3-1.7B." The series line says the sizes are 1.7B, 4B, and 8B. This page is the 1.7B model. The card language tag is English.

This is a classifier for a user-written policy. The card says it is "designed to evaluate text against user-defined, natural language policies." Fast mode returns PASS or FAIL. Chain-of-thought mode writes a reasoning trace and then the label. The example input is a policy plus a user message and an agent reply. The license is Apache-2.0.

Serving is text. The example does not use the chat template. It uses an `[INST]` wrapper and temperature 0.1. `generation_config.json` still has the Qwen3 defaults: do_sample true, temperature 0.6, top_k 20, top_p 0.95. `config.json` sets max position embeddings to 40960. The tokenizer's model_max_length is 131072. The tokenizer chat template is the Qwen3 tool template. The card does not set a safety system prompt.
