# adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged

## Sources

revision_3_experiments/hf_inventory/cache/readmes/adzcai__AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged__2026-10-09.md — cached model card, sha256 7f1d5769cdaab0b23f610a3cd69d324f98de1078066daf700340d0a07bbb5e21
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/README.md — current card; sha256 matches the cache
https://huggingface.co/api/models/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged — file list and parameter count
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/config.json — Qwen3.5 config with a vision tower; text context 262144
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/generation_config.json — eos and pad ids only
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/tokenizer_config.json — no chat_template key
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/chat_template.jinja — chat template
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/model.safetensors.index.json — 4,539,265,536 parameters; 297 vision tensors
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/Modelfile — Ollama template, stop token, num_ctx 4096
https://huggingface.co/datasets/israel/AfriGuard-inst — training dataset card; files are gated
https://huggingface.co/datasets/israel/AfriGuard — source dataset; the 10 category names

## Record

The training set is `israel/AfriGuard-inst`. The card says the model was "fine-tuned with LoRA (rank 16, all linear layers), merged into the base weights on israel/AfriGuard-inst". The dataset card states 46,306 train rows and 7,175 validation rows. The files do not load without approval. `israel/AfriGuard` is human-annotated labels on prompt and model-response pairs. AfriGuard-XL, the other source, has an empty README. The languages are English, Amharic, Hausa, Igbo, Oromo, Shona, Swahili, Twi, Wolof, Yoruba, and Zulu.

The update is LoRA, then merged. The card says "LoRA (rank 16, all linear layers), merged into the base weights". The named config is `examples/train_lora/afriguard_inst_afriqueqwen3.5-4b-50langs-instruct_lora_sft.yaml`, and the card says "loss on the response only." Learning rate is 0.0001, train batch size 1, gradient accumulation 2, total train batch size 2, and 1 epoch. The repository has no `adapter_config.json` and no `trainer_state.json`, so LoRA alpha and the step count are not in the repo. No source says the base was quantized. The card names the AfriGuard-model LlamaFactory repo and does not give a URL. No paper names this checkpoint.

The parent is `McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1`. Only the card states that. The weight index says 4,539,265,536 parameters. The license is `cc-by-4.0`. The training-results section is empty.

The card says each example is "one of the safety system instructions plus the user prompt", and the target is `<safety>…</safety>` `<category>…</category>` `<response>…</response>`. The ten category names are on the `israel/AfriGuard` card, not in this model's prose. The instruction templates are not printed. Inventory methods, dataset, and parent match.

The card has no inference example. The weight index includes 297 `model.visual` tensors. `generation_config.json` does not set temperature or top-p. The Modelfile sets `num_ctx` 4096 and stop `<|im_end|>`. Text context in `config.json` is 262144. A chat template file is present. The prose says "1 GPU". The hyperparameter block says `distributed_type: multi-GPU`.
