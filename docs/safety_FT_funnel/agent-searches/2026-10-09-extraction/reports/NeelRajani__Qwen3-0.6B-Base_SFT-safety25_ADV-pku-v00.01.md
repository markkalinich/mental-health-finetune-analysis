# NeelRajani/Qwen3-0.6B-Base_SFT-safety25_ADV-pku-v00.01

## Sources

- https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety25_ADV-pku-v00.01/raw/main/README.md — current model card; byte-identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/NeelRajani__Qwen3-0.6B-Base_SFT-safety25_ADV-pku-v00.01__2026-10-05.md — cached card, sha256 cad79c953513e8a32ede431772aa2e7f471b284f202c0e2dce692438975ad5e2
- https://huggingface.co/api/models/NeelRajani/Qwen3-0.6B-Base_SFT-safety25_ADV-pku-v00.01 — file list, chat template, 596,049,920 parameters
- https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety25_ADV-pku-v00.01/raw/main/config.json — Qwen3 config, 32,768 positions
- https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety25_ADV-pku-v00.01/raw/main/generation_config.json — greedy decoding, max_new_tokens 2048
- https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety25_ADV-pku-v00.01/raw/main/tokenizer_config.json — no chat_template key; model_max_length 131072
- https://huggingface.co/NeelRajani/Qwen3-0.6B-Base_SFT-safety25_ADV-pku-v00.01/resolve/main/training_args.bin — TRL SFTConfig: 1 epoch, learning rate 1e-5, batch size 16, revision empty
- https://huggingface.co/datasets/NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2 — gated dataset; README empty; metadata says 10,226 train rows
- https://github.com/huggingface/trl — library the card says it used
- https://wandb.ai/neelectric/shallowness/runs/x3hophks — run linked from the card
- https://featherless.ai/models/NeelRajani/Qwen3-0.6B-Base_SFT-safety25_ADV-pku-v00.01 — hosting page; repeats the parent and calls the model 0.8B
- https://arxiv.org/abs/2505.09388 — Qwen3 Technical Report; does not name this repository
- https://arxiv.org/abs/2506.05176 — Qwen3 embedding paper; does not name this repository

## Record

The card says this model was fine-tuned on NeelRajani/PKU-SafeRLHF_alpaca3-8b_severity-ge-2. That is the same gated dataset named for the safety100 checkpoint. Its README is empty, so language and who wrote the text are not stated. The Hub metadata lists 10,226 training rows. Anonymous access does not load the files.

The card says "This model was trained with SFT." It does not say full fine-tuning or LoRA. `training_args.bin` sets 1 epoch, max_steps -1, learning rate 1e-5, per-device batch size 16, gradient accumulation 1, warmup ratio 0.03, bf16, max length 2048, and loss type `chunked_nll`. The revision field is empty. There is no LoRA rank and no quantization flag. The repository stores full weights in `model.safetensors`.

The parent on the card is NeelRajani/Qwen3-0.6B-Base_SFT_safety_v00.01. A Featherless page repeats that parent. Neither arXiv paper names this checkpoint.

The card's only description is the fine-tune sentence. The quick start sends one user text question through a text-generation pipeline. There is no therapy or support claim and no limitation or medical warning. The YAML line `licence: license` is a placeholder, not a license name.

Serving is text-only. `generation_config.json` sets do_sample false and max_new_tokens 2048. The card example asks for 128 new tokens. Context length in `config.json` is 32,768. A `chat_template.jinja` file is present and writes a system turn only if the caller provides one. The Hub weight total is 596,049,920 parameters. Featherless says 0.8B. The card reports no evaluation.
