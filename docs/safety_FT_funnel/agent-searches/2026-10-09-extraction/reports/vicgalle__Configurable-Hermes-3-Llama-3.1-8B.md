# vicgalle/Configurable-Hermes-3-Llama-3.1-8B

## Sources

https://huggingface.co/vicgalle/Configurable-Hermes-3-Llama-3.1-8B/raw/main/README.md — current model card; byte-identical to the cached card
https://huggingface.co/api/models/vicgalle/Configurable-Hermes-3-Llama-3.1-8B — file list and parameter count
https://huggingface.co/vicgalle/Configurable-Hermes-3-Llama-3.1-8B/raw/main/config.json — architecture, parent path, context length
https://huggingface.co/vicgalle/Configurable-Hermes-3-Llama-3.1-8B/raw/main/generation_config.json — sampling settings
https://huggingface.co/vicgalle/Configurable-Hermes-3-Llama-3.1-8B/raw/main/tokenizer_config.json — default and tool-use chat templates
https://arxiv.org/abs/2404.00495 — CST paper abstract and HTML full text; does not name this checkpoint
https://github.com/vicgalle/configurable-safety-tuning — project README linked from the card; the model table does not list this checkpoint
https://raw.githubusercontent.com/vicgalle/configurable-safety-tuning/main/cst_train.py — DPO script for OpenHermes-2.5-Mistral-7B, not this base
https://huggingface.co/datasets/vicgalle/configurable-system-prompt-multitask — training dataset card, 1,952 rows
https://huggingface.co/api/datasets/vicgalle/configurable-system-prompt-multitask — dataset row count and language
https://huggingface.co/api/datasets/jondurbin/truthy-dpo-v0.1 — constituent dataset named on the training-set card
https://arxiv.org/abs/2408.11857 — Hermes 3 technical report, found by search; listed only, not read
https://huggingface.co/collections/vicgalle/configurable-safety-tuning-660c2ce5bcd1ed5345be0c58 — author collection linked from the GitHub README

## Record

The training set is `vicgalle/configurable-system-prompt-multitask`, 1,952 English rows, and it loads. The dataset card says: "We release the synthetic dataset for the multi-task experiments." It has two sources. One is "Self-critique on a safety task from Harmful Behaviours, using the SOLAR-Instruct model." The other is `jondurbin/truthy-dpo-v0.1`. That Hub dataset is public. Its row count is not in the API metadata I read. No source names a Hub id for Harmful Behaviours.

The objective is DPO. The card says this checkpoint was "fine-tuned using the approach configurable safety tuning (CST)" on that dataset. The GitHub README says: "CST is an extension of DPO which leverages opposite system prompts at fine-tuning time." The paper's experiments are OpenHermes-2.5-Mistral-7B and SOLAR-Instruct-10.7B. It does not print this repository id. The GitHub model table also does not list this checkpoint. `cst_train.py` trains `teknium/OpenHermes-2.5-Mistral-7B` with 4-bit LoRA, so those settings are not this run. This repository has four float16 weight shards, 8,030,261,248 parameters, and no adapter file. Rank, epochs, learning rate, batch size, and whether the base was quantized are not stated for this checkpoint.

The parent is `NousResearch/Hermes-3-Llama-3.1-8B`. The card and `config.json` (`_name_or_path`) agree. No other source names a different parent.

This is a chatbot whose behavior is chosen with a system prompt. The card offers a harmless assistant prompt, an uncensored assistant prompt, a harmful-assistant prompt, a truthful assistant prompt, and a role-play prompt. If the first message is not a system message, the default chat template inserts "You are a helpful assistant." The use claim is absent: the disclaimer says it is "a research artifact in the fields of safety and alignment." That sentence is a limitation about harmful outputs, not about therapy or medical use. The first usage example is text only: a user message, "Top things to do in Madrid?" `generation_config.json` sets `do_sample` true, `temperature` 0.6, and `top_p` 0.9. The card example uses `max_new_tokens` 512 and `temperature` 0.9. `config.json` sets `max_position_embeddings` to 131072. License on the card is `llama3.1`. The card does not report a benchmark score.

The inventory dataset and parent match. The inventory methods cell is empty. The sources say the method is configurable safety tuning, defined as DPO.
