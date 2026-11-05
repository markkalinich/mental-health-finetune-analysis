# farbodtavakkoli/OTel-LLM-8.3B-Safety

## Sources

- https://huggingface.co/farbodtavakkoli/OTel-LLM-8.3B-Safety/raw/main/README.md — current model card; identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/farbodtavakkoli__OTel-LLM-8.3B-Safety__2026-10-09.md — cached card, sha256 44776fad47d38c5aad85ab682283c56f5bd415249f2691a3222be5d1e377dabf
- https://huggingface.co/api/models/farbodtavakkoli/OTel-LLM-8.3B-Safety — repository file list
- https://huggingface.co/farbodtavakkoli/OTel-LLM-8.3B-Safety/raw/main/config.json — text-only Gemma 3 causal LM, context 32768
- https://huggingface.co/farbodtavakkoli/OTel-LLM-8.3B-Safety/raw/main/generation_config.json — sampling settings
- https://huggingface.co/farbodtavakkoli/OTel-LLM-8.3B-Safety/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
- https://huggingface.co/farbodtavakkoli/OTel-LLM-8.3B-Safety/raw/main/chat_template.jinja — chat template with a built-in system line
- https://arxiv.org/abs/2610.07766 — abstract of the OTel paper
- https://arxiv.org/html/2610.07766 — HTML full text; names OTel-LLM-8.3B-Safety
- https://arxiv.org/abs/2608.15436 — second paper linked from GitHub; listed only, not read
- https://github.com/farbodtavakkoli/OTel — project README; recipe collection, not a script for this checkpoint
- https://raw.githubusercontent.com/farbodtavakkoli/OTel/main/README.md — GitHub README
- https://huggingface.co/datasets/farbodtavakkoli/OTel-Safety — dataset page
- https://huggingface.co/datasets/farbodtavakkoli/OTel-Safety/raw/main/README.md — dataset card
- https://huggingface.co/datasets/farbodtavakkoli/OTel-Safety/raw/main/croissant.json — synthetic-data statement
- https://datasets-server.huggingface.co/is-valid?dataset=farbodtavakkoli/OTel-Safety — dataset viewer is available

## Record

This checkpoint was trained on OTel-Safety (`farbodtavakkoli/OTel-Safety`). The card says: "`EssentialAI/rnj-1-instruct` -> `OTel-Safety` full-parameter post-training -> `farbodtavakkoli/OTel-LLM-8.3B-Safety`". The dataset is public, English, and the Hub viewer loads it. Its own row count is not stated. The card's 326,767 figure is the cleaned OTel family, not this file alone. Croissant says the training data includes synthetically generated question-answer pairs, and domain experts curated the source documents, so the data are mixed.

The update is full-parameter. The card says: "Training method | Full-parameter post-training / fine-tuning". It also says "Epochs | 3 for LLM/embedding models; 2 for rerankers", "Precision | BF16", and "Optimizer | AdamW, 8-bit". This repository is an LLM, so the epoch count on the card is 3. The paper's shared template matches that recipe and masks loss to completion tokens only. It does not name SFT, DPO, PPO, or another listed loss for this checkpoint. No learning rate is stated. The paper's per-device batch size is a range, 8–128, not one value for this run. Warmup is 100 steps. Total training steps are not stated. There is no LoRA rank and no `adapter_config.json`.

The card names the parent `EssentialAI/rnj-1-instruct` and the size 8.3B. The paper names `OTel-LLM-8.3B-Safety` and says it was trained on OTel-Safety. It does not print `farbodtavakkoli/OTel-LLM-8.3B-Safety`. The sentence that names `rnj-1-instruct` is about `OTel-LLM-8.3B-IT`, a different checkpoint. The current GitHub README does not name this checkpoint's base.

The card presents a telecom assistant. It says: "This model is intended for telecom RAG pipelines where the assistant should refuse to answer when retrieved context is missing, irrelevant, or insufficient." Use claim is absent. The limitation is about telecom scope: "OTel models are domain-specific to telecommunications and should not be treated as general-purpose models." The paper does not print a score for this checkpoint. The 8.3B score in its Table 7 is for OTel-LLM-8.3B-IT.

The card's usage example is a text prompt with `max_new_tokens=256`. The card says the release is "primarily text-centric." `config.json` is `Gemma3ForCausalLM` with no vision tower and `max_position_embeddings` 32768. `generation_config.json` sets `do_sample` true and `temperature` 0.2. `chat_template.jinja` always starts with "You are rnj-1, a foundation model trained by Essential AI." and, if the caller does not pass a system message, adds "You are a helpful assistant." The tokenizer's `model_max_length` is 1500. License on the card is Apache 2.0. The inventory row matches the card: full-parameter fine-tuning, `farbodtavakkoli/OTel-Safety`, parent `EssentialAI/rnj-1-instruct`.
