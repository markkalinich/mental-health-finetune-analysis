# tomg-group-umd/DynaGuard-4B

## Sources

- https://huggingface.co/tomg-group-umd/DynaGuard-4B/raw/main/README.md — current model card; identical to the cached card
- revision_3_experiments/hf_inventory/cache/readmes/tomg-group-umd__DynaGuard-4B__2026-10-09.md — cached card, sha256 692e17b3da90d6af3b714d8a6fa84863c62a232aa6d7821016e14f627d89f149
- https://huggingface.co/api/models/tomg-group-umd/DynaGuard-4B — repository file list
- https://huggingface.co/tomg-group-umd/DynaGuard-4B/raw/main/config.json — Qwen3 config, max position 40960, hidden size 2560, 36 layers
- https://huggingface.co/tomg-group-umd/DynaGuard-4B/raw/main/generation_config.json — temperature 0.6, top_k 20, top_p 0.95
- https://huggingface.co/tomg-group-umd/DynaGuard-4B/raw/main/tokenizer_config.json — Qwen3 chat template
- https://arxiv.org/abs/2509.02563 — paper abstract
- https://arxiv.org/html/2509.02563 — paper HTML; names DynaGuard-4B; does not print this repository id
- https://proceedings.iclr.cc/paper_files/paper/2026/hash/8d2aad53fa148791ffd004a7c9cce5ad-Abstract-Conference.html — same paper at ICLR 2026
- https://github.com/montehoover/DynaGuard — code linked from the card; evaluation script, no training script
- https://github.com/taruschirag/DynaGuard — GitHub URL in the card front matter
- https://taruschirag.github.io/DynaGuard/ — project page linked from the card
- https://huggingface.co/datasets/tomg-group-umd/DynaBench — training dataset named on the card; public
- https://huggingface.co/datasets/montehoover/DynaBench — another Hub copy found by search; the viewer reports 140,165 rows
- https://huggingface.co/datasets/allenai/wildguardmix — WildGuard; gated
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — BeaverTails; public
- https://huggingface.co/datasets/lmsys/toxic-chat — ToxicChat; public
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0; public

## Record

The card is the same text as the 1.7B card, with the title, the model id, and the base model changed. It says the model was "Fine-tuned on a mixture of the DynaBench dataset and several safety benchmarks (WildGuard, BeaverTails, ToxicChat, Aegis 2.0)." The paper says the mixture is 40,000 DynaBench samples and 40,000 samples from those four safety datasets, then GRPO on 11,000 samples from that mixture. DynaBench on the card is `tomg-group-umd/DynaBench`. A search also finds `montehoover/DynaBench`, whose viewer reports 140,165 rows. The 40,000 figure is the count the paper says was used in supervised fine-tuning, not that viewer total.

The card says: "The model was trained using Supervised Fine-Tuning (SFT) for one epoch, followed by GRPO." No sentence says LoRA or full fine-tuning. There is no adapter file. The paper's appendix bolds the 4B rates: SFT learning rate 1e-5, GRPO learning rate 1e-6. The bold batch sizes, shared across the three sizes, are 128 for SFT and 48 for GRPO. The JSON leaves the single learning-rate and batch-size fields empty because those are two stages. SFT is one epoch. GRPO's epoch count is not stated.

The parent is Qwen/Qwen3-4B. The card says "Base Model: Qwen3-4B." The series line includes a 4B model, and this page is that model. The card language tag is English.

This is a classifier for a user-written policy. Fast mode returns PASS or FAIL. Chain-of-thought mode writes a reasoning trace and then the label. The example input is a policy plus a user message and an agent reply. On this card's table, DynaGuard-4B scores 68.2 F1 on DynaBench and 78.4 on the safety-task average. The license is Apache-2.0.

Serving is text. The example uses an `[INST]` wrapper and temperature 0.1, not the chat template. `generation_config.json` has do_sample true, temperature 0.6, top_k 20, and top_p 0.95. `config.json` sets max position embeddings to 40960. The tokenizer's model_max_length is 131072. The card does not set a safety system prompt.
