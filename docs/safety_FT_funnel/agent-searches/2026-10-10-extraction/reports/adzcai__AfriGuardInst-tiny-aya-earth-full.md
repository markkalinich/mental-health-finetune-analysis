# adzcai/AfriGuardInst-tiny-aya-earth-full

## Sources

revision_3_experiments/hf_inventory/cache/readmes/adzcai__AfriGuardInst-tiny-aya-earth-full__2026-10-10.md — cached model card, sha256 685e713692a77e28a96f1f985899c6cedb18baec6855bf2d1dd8a565ca7fc0e1
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-full/raw/main/README.md — current card; sha256 matches the cache
https://huggingface.co/api/models/adzcai/AfriGuardInst-tiny-aya-earth-full — file list and parameter count
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-full/raw/main/config.json — Cohere2 causal LM, context 8192, no vision config
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-full/raw/main/generation_config.json — bos, eos, and pad ids only
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-full/raw/main/tokenizer_config.json — no chat_template key
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-full/raw/main/chat_template.jinja — chat template file
https://huggingface.co/adzcai/AfriGuardInst-tiny-aya-earth-full/raw/main/trainer_state.json — 11577 steps, 1 epoch
https://huggingface.co/datasets/israel/AfriGuard-inst — training dataset card; files are gated
https://huggingface.co/datasets/israel/AfriGuard — source dataset; the 10 category names
https://huggingface.co/CohereLabs/tiny-aya-earth — parent model card, found by search; 3.35B, 8K context, text causal LM

## Record

The training set is `israel/AfriGuard-inst`. The card says the model was "fine-tuned with full fine-tuning (DeepSpeed ZeRO-3) on israel/AfriGuard-inst". The dataset card states 46,306 train rows and 7,175 validation rows. The files do not load without approval. `israel/AfriGuard` is human-annotated labels on prompt and model-response pairs. AfriGuard-XL's README is empty. The card's language list is English, Amharic, Hausa, Igbo, Oromo, Shona, Swahili, Twi, Wolof, Yoruba, and Zulu.

The update is a full fine-tune. The card says "fine-tuned with full fine-tuning (DeepSpeed ZeRO-3)" and "loss on the response only." The named config is `examples/train_full/afriguard_inst_tiny-aya-earth_full_sft.yaml`. Learning rate is 1e-05, train batch size 1, gradient accumulation 4, total train batch size 4, and 1 epoch. `trainer_state.json` records `global_step` 11577 and `train_batch_size` 1. The ceiling of 46,306 divided by 4 is 11,577. No LoRA rank is stated. No source says the base was quantized. The card names the AfriGuard-model LlamaFactory repo and does not give a URL. Search did not find a paper that names this repository.

The parent is `CohereLabs/tiny-aya-earth`. Only this card states that for this checkpoint. The Hub weight count is 3,349,227,520 parameters. The parent card says the model size is 3.35B and the context length is 8K. The license is `cc-by-nc-4.0`. The training-results section is empty.

The card says each example is "one of the safety system instructions plus the user prompt", and the target is `<safety>…</safety>` `<category>…</category>` `<response>…</response>`. The ten category names are on the `israel/AfriGuard` card. The instruction templates are not printed. Inventory method, dataset, and parent match.

Serving is text. `config.json` is `Cohere2ForCausalLM` with `max_position_embeddings` 8192 and no vision config. `generation_config.json` does not set temperature or top-p. A chat template file is present. `tokenizer_config.json` has no `chat_template` key. The prose says "1 GPU". The hyperparameter block says `distributed_type: multi-GPU`.
