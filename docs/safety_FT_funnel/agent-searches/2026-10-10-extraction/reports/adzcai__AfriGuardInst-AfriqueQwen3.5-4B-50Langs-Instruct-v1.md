# adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1

## Sources

revision_3_experiments/hf_inventory/cache/readmes/adzcai__AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1__2026-10-09.md — cached model card, sha256 631910ab912d6b6cce59e0a28d894ff251fab20f67a7ce8970bd25b67ef581f4
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/README.md — current card; sha256 matches the cache
https://huggingface.co/api/models/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1 — file list and parameter count
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/config.json — Qwen3.5 config with a vision tower; text context 262144
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/generation_config.json — eos and pad ids only
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/tokenizer_config.json — no chat_template key; model_max_length 262144
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/chat_template.jinja — chat template, including image and video slots
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/processor_config.json — image and video processors
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/trainer_state.json — 23153 steps, 1 epoch
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/train_results.json — same epoch and train loss
https://huggingface.co/datasets/israel/AfriGuard-inst — training dataset card; files are gated
https://huggingface.co/datasets/israel/AfriGuard — source dataset; human annotations and the 10 categories
https://huggingface.co/datasets/israel/AfriGuard-XL — the other source named on the AfriGuard-inst card; README empty
https://huggingface.co/api/models/McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1 — parent parameter count
https://huggingface.co/collections/adzcai/afriguard — author collection that lists this checkpoint

## Record

The training set is `israel/AfriGuard-inst`. The card says the model was "fine-tuned with full fine-tuning (DeepSpeed ZeRO-3) on israel/AfriGuard-inst". The dataset card says it is Alpaca-style instruction data built from the train and validation splits of `israel/AfriGuard` and `israel/AfriGuard-XL`, with test splits held out. It states 46,306 train rows and 7,175 validation rows, 53,481 together. The Hub dataset server returned 401, so the files do not load without approval. `israel/AfriGuard` says it is "a human-annotated safety dataset" and that the English columns are a "prompt and model response", so that portion is mixed. The AfriGuard-XL README is empty, so that portion's provenance is not stated. Languages on both the model card and the dataset card are English, Amharic, Hausa, Igbo, Oromo, Shona, Swahili, Twi, Wolof, Yoruba, and Zulu.

The update is a full fine-tune. The card says "fine-tuned with full fine-tuning (DeepSpeed ZeRO-3)". The loss is supervised training on the response: "loss on the response only." The card names the LlamaFactory config `examples/train_full/afriguard_inst_afriqueqwen3.5-4b-50langs-instruct_full_sft.yaml` as the config that was rerun. The card states learning rate 1e-05, train batch size 1, gradient accumulation 2, total train batch size 2, and 1 epoch. `trainer_state.json` records `global_step` 23153, `num_train_epochs` 1, and `train_batch_size` 1. 46,306 train rows divided by 2 is 23,153, so the run matches one epoch on the train split. No LoRA rank is stated. No source says the base was quantized. The card names an "AfriGuard-model (LlamaFactory) repo" and does not give a URL. Search did not return that repository. No paper names this checkpoint.

The parent is `McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1`. Only the card states that. The Hub weight count is 4,539,265,536 parameters. The parent checkpoint's count is 4,205,751,296. The license is `cc-by-4.0`. The card's training-results section is empty.

The card does not present a chat demo. It says each training example is "one of the safety system instructions plus the user prompt", and the target is `<safety>…</safety>` `<category>…</category>` `<response>…</response>`. The dataset card spells the XML as a safe/unsafe label, a category, and a final reply. The ten categories are named on `israel/AfriGuard`, not on this model card: Criminal Activity & Exploitation, Political & Societal Manipulation, Violence & Physical Harm, Systemic Risks, Sexual & Exploitative Content, Unsafe or High-Risk Advice, Privacy & Data Misuse, Hate, Harassment & Discrimination, Ethical & Moral Risk, and Intellectual Property & Content Integrity. The five safety-instruction templates are not printed. Inventory methods, dataset, and parent match.

The card does not show an inference example. `config.json` includes a vision tower, and `processor_config.json` includes image and video processors. `generation_config.json` does not set temperature or top-p. Text context length is 262144. A chat template file is present. `tokenizer_config.json` has no `chat_template` key. The prose says "1 GPU". The hyperparameter block says `distributed_type: multi-GPU`.
