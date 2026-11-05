# adzcai/AfriGuardInst-tiny-aya-earth-lora-merged

## Sources

revision_3_experiments/hf_inventory/cache/readmes/adzcai__AfriGuardInst-tiny-aya-earth-lora-merged__2026-10-10.md — cached model card, sha256 aecc41fb030f0c41ced6e5e2c6026bd690a2439b64cfb3a63aed890fc35ab95a
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-lora-merged/raw/main/README.md — current card; sha256 matches the cache
https://huggingface.co/api/models/adzcai/AfriGuardInst-tiny-aya-earth-lora-merged — file list and parameter count
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-lora-merged/raw/main/config.json — Cohere2 causal LM, context 8192, no vision config
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-lora-merged/raw/main/generation_config.json — bos, eos, and pad ids only
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-lora-merged/raw/main/tokenizer_config.json — no chat_template key
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-lora-merged/raw/main/chat_template.jinja — chat template file
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-lora-merged/raw/main/Modelfile — Ollama template, stop token, num_ctx 4096
https://huggingface.co/datasets/israel/AfriGuard-inst — training dataset card; files are gated
https://huggingface.co/datasets/israel/AfriGuard — source dataset; the 10 category names
https://arxiv.org/abs/2603.11510 — Tiny Aya abstract; the parent-family paper
https://arxiv.org/html/2603.11510v1 — Tiny Aya HTML; it does not print this repository id
https://huggingface.co/CohereLabs/tiny-aya-earth — parent model card

## Record

The training set is `israel/AfriGuard-inst`. The card says the model was "fine-tuned with LoRA (rank 16, all linear layers), merged into the base weights on israel/AfriGuard-inst". The dataset card states 46,306 train rows and 7,175 validation rows. The files do not load without approval. `israel/AfriGuard` is human-annotated labels on prompt and model-response pairs. AfriGuard-XL's README is empty. The card's language list is English, Amharic, Hausa, Igbo, Oromo, Shona, Swahili, Twi, Wolof, Yoruba, and Zulu.

The update is LoRA, then merged. The card says "LoRA (rank 16, all linear layers), merged into the base weights" and "loss on the response only." The named config is `examples/train_lora/afriguard_inst_tiny-aya-earth_lora_sft.yaml`. Learning rate is 0.0001, train batch size 2, gradient accumulation 4, total train batch size 8, and 1 epoch. The repository has no `adapter_config.json` and no `trainer_state.json`, so LoRA alpha and the step count are not in the repo. No source says the base was quantized. The card names the AfriGuard-model LlamaFactory repo and does not give a URL. The Tiny Aya paper (arXiv 2603.11510) is about the parent family. Its HTML does not print this repository id.

The parent is `CohereLabs/tiny-aya-earth`. Only this card states that for this checkpoint. The Hub weight count is 3,349,227,520 parameters. The license is `cc-by-nc-4.0`. The training-results section is empty.

The card says each example is "one of the safety system instructions plus the user prompt", and the target is `<safety>…</safety>` `<category>…</category>` `<response>…</response>`. The ten category names are on the `israel/AfriGuard` card. The instruction templates are not printed. Inventory method, dataset, and parent match.

Serving is text. `config.json` is `Cohere2ForCausalLM` with `max_position_embeddings` 8192 and no vision config. `generation_config.json` does not set temperature or top-p. The Modelfile sets `num_ctx` 4096 and stop `<|END_OF_TURN_TOKEN|>`. A chat template file is present. The prose says "1 GPU". The hyperparameter block says `distributed_type: multi-GPU`.
