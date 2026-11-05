# vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B

## Sources

https://huggingface.co/vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B/raw/main/README.md — current model card; byte-identical to the cached card
https://huggingface.co/api/models/vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B — file list and parameter count
https://huggingface.co/vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B/raw/main/config.json — architecture, parent path, context length
https://huggingface.co/vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B/raw/main/generation_config.json — sampling flag
https://huggingface.co/vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B/raw/main/tokenizer_config.json — chat template
https://arxiv.org/abs/2404.00495 — paper abstract and HTML full text
https://arxiv.org/html/2404.00495v1 — same paper HTML
https://github.com/vicgalle/configurable-safety-tuning — project README; prints this repository id
https://raw.githubusercontent.com/vicgalle/configurable-safety-tuning/main/cst_train.py — DPO training script for a different base
https://huggingface.co/datasets/vicgalle/configurable-system-prompt-multitask — training dataset card, 1,952 rows
https://huggingface.co/api/datasets/vicgalle/configurable-system-prompt-multitask — dataset row count and language
https://huggingface.co/api/datasets/jondurbin/truthy-dpo-v0.1 — constituent dataset named on the training-set card
https://huggingface.co/collections/vicgalle/configurable-safety-tuning-660c2ce5bcd1ed5345be0c58 — author collection linked from the GitHub README

## Record

The training set is `vicgalle/configurable-system-prompt-multitask`, 1,952 English rows, and it loads. The dataset card says: "We release the synthetic dataset for the multi-task experiments." It has two sources. One is "Self-critique on a safety task from Harmful Behaviours, using the SOLAR-Instruct model." The other is `jondurbin/truthy-dpo-v0.1`, which the card names as truthy-dpo. That second Hub dataset is public. Its row count is not in the API metadata I read. No source names a Hub id for Harmful Behaviours; several Hub copies exist, and I did not pick one.

The objective is DPO. The card says this checkpoint was "fine-tuned using the approach configurable safety tuning (CST)" on that dataset. The GitHub README, which lists this repository, says: "CST is an extension of DPO which leverages opposite system prompts at fine-tuning time." The paper uses the DPO loss and evaluates OpenHermes-2.5-Mistral-7B and SOLAR-Instruct-10.7B. It does not print this repository id. The GitHub note says only ConfigurableHermes and ConfigurableSOLAR appear in the paper. `cst_train.py` calls `DPOTrainer` with 4-bit LoRA (`r=24`, `lora_alpha=48`), 1 epoch, and per-device batch 2, but the script sets `model_name = "teknium/OpenHermes-2.5-Mistral-7B"`. It does not name this checkpoint, so those settings are not recorded as this run. This repository has four float16 weight shards, 8,030,523,392 parameters, and no adapter file. Rank, epochs, learning rate, batch size, and whether the base was quantized are not stated for this checkpoint.

The parent is `NousResearch/Hermes-2-Pro-Llama-3-8B`. The card, the GitHub table ("Fine-tuned from Hermes-2-Pro-Llama-3-8B"), and `config.json` (`_name_or_path`) agree.

This is a chatbot whose behavior is chosen with a system prompt. The card offers a harmless assistant prompt, an uncensored assistant prompt, a harmful-assistant prompt, a truthful assistant prompt, and a role-play prompt. The chat template does not insert a default system line. The use claim is absent: the disclaimer says it is "a research artifact in the fields of safety and alignment." That sentence is a limitation about harmful outputs, not about therapy or medical use. The first usage example is text only: a user message, "Top things to do in Madrid?" The first example sets `max_new_tokens` 512, `do_sample` true, and `temperature` 0.9. `config.json` sets `max_position_embeddings` to 8192. License is Apache-2.0.

The card's Open LLM Leaderboard block reports average 22.29, IFEval 57.63, BBH 30.51, MATH Lvl 5 5.97, GPQA 6.26, MuSR 10.06, and MMLU-PRO 23.31. The paper's safety tables are for the other two bases.

The inventory dataset and parent match. The inventory methods cell is empty. The sources say the method is configurable safety tuning, defined as DPO.
