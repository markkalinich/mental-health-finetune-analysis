# farbodtavakkoli/OTel-LLM-12B-Safety

## Sources

- https://huggingface.co/farbodtavakkoli/OTel-LLM-12B-Safety/raw/main/README.md — current model card; identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/farbodtavakkoli__OTel-LLM-12B-Safety__2026-10-09.md — cached card, sha256 6efda55a58f5064ecd92fe89dfa8fd4e05a335125c0088f0c91d1005a8ad1184
- https://huggingface.co/api/models/farbodtavakkoli/OTel-LLM-12B-Safety — repository file list
- https://huggingface.co/farbodtavakkoli/OTel-LLM-12B-Safety/raw/main/config.json — architecture and context length
- https://huggingface.co/farbodtavakkoli/OTel-LLM-12B-Safety/raw/main/generation_config.json — sampling settings
- https://huggingface.co/farbodtavakkoli/OTel-LLM-12B-Safety/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
- https://huggingface.co/farbodtavakkoli/OTel-LLM-12B-Safety/raw/main/chat_template.jinja — Gemma chat template
- https://arxiv.org/abs/2610.07766 — abstract of the OTel paper
- https://arxiv.org/html/2610.07766 — HTML full text of the OTel paper; names OTel-LLM-12B-Safety
- https://arxiv.org/abs/2608.15436 — second paper linked from GitHub; listed only, not read
- https://github.com/farbodtavakkoli/OTel — project README; recipe collection, not a script for this checkpoint
- https://raw.githubusercontent.com/farbodtavakkoli/OTel/main/README.md — GitHub README
- https://huggingface.co/datasets/farbodtavakkoli/OTel-Safety — dataset page
- https://huggingface.co/datasets/farbodtavakkoli/OTel-Safety/raw/main/README.md — dataset card
- https://huggingface.co/datasets/farbodtavakkoli/OTel-Safety/raw/main/croissant.json — synthetic-data statement
- https://datasets-server.huggingface.co/is-valid?dataset=farbodtavakkoli/OTel-Safety — dataset viewer is available

## Record

This checkpoint was trained on OTel-Safety (`farbodtavakkoli/OTel-Safety`). The card says: "`google/gemma-3-12b-it` -> `OTel-Safety` full-parameter post-training -> `farbodtavakkoli/OTel-LLM-12B-Safety`". The dataset is public, English, and the Hub viewer loads it. Its own row count is not stated. The card's 326,767 figure is the cleaned OTel family, not this file alone. Croissant says: "The training data includes synthetically generated question-answer pairs derived from source documents through automated pipelines, including LLM-assisted answer recreation and fact-grounded verification." Domain experts also curated the source documents, so the data are mixed.

The update is full-parameter. The card says: "Training method | Full-parameter post-training / fine-tuning". The same card says "Epochs | 3 for LLM/embedding models; 2 for rerankers", "Precision | BF16", and "Optimizer | AdamW, 8-bit". This repository is an LLM, so the epoch count on the card is 3. The paper's shared template matches that recipe and adds "Loss masking | Completion tokens only", but it never names SFT, DPO, PPO, or another listed loss for this checkpoint. No learning rate is stated. The paper's per-device batch size is a range, 8–128, not one value for this run. Warmup is 100 steps. Total training steps are not stated. There is no LoRA rank and no `adapter_config.json`.

The card names the parent `google/gemma-3-12b-it` and the size 12B. The paper names `OTel-LLM-12B-Safety` and says it was trained on OTel-Safety. It does not print `farbodtavakkoli/OTel-LLM-12B-Safety` and it does not name this checkpoint's base model. The current GitHub README does not name this checkpoint's base either.

The card presents a telecom assistant, not a mental-health tool. It says: "This model is intended for telecom RAG pipelines where the assistant should refuse to answer when retrieved context is missing, irrelevant, or insufficient." Use claim is absent. The limitation is about telecom scope: "OTel models are domain-specific to telecommunications and should not be treated as general-purpose models." That is an unrelated limitation. The paper does not print a score for this checkpoint. The 12B score in its Table 7 is for OTel-LLM-12B-IT.

The card's usage example is a text prompt passed to `tokenizer` and `model.generate`, with `max_new_tokens=256`. The card also says the release is "primarily text-centric." `generation_config.json` sets `do_sample` true, `top_k` 64, and `top_p` 0.95. No temperature is set. `chat_template.jinja` is present. `tokenizer_config.json` has no chat template and `use_default_system_prompt` is false, so no system prompt is stored. `config.json` sets text `max_position_embeddings` to 131072 and still includes a Gemma 3 vision tower. The tokenizer's `model_max_length` is 1500, the same cap as the training recipe. License on the card is Apache 2.0. The inventory row matches the card: full-parameter fine-tuning, `farbodtavakkoli/OTel-Safety`, parent `google/gemma-3-12b-it`.
