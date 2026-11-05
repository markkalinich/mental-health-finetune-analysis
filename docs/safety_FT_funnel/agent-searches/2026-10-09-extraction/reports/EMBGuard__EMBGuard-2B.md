# EMBGuard/EMBGuard-2B

## Sources

https://huggingface.co/EMBGuard/EMBGuard-2B/raw/main/README.md — current model card; same bytes as the cache; YAML only
https://huggingface.co/api/models/EMBGuard/EMBGuard-2B — file list, parameter count, and chat template
https://huggingface.co/EMBGuard/EMBGuard-2B/raw/main/config.json — architecture and context length
https://huggingface.co/EMBGuard/EMBGuard-2B/raw/main/generation_config.json — sampling settings
https://huggingface.co/EMBGuard/EMBGuard-2B/raw/main/trainer_state.json — saved step, epoch, and batch
https://arxiv.org/abs/2605.30924 — EMBGuard abstract
https://arxiv.org/html/2605.30924 — EMBGuard full text
https://icml.cc/virtual/2026/poster/63023 — ICML 2026 poster page
https://github.com/dongwxxkchoi/EMBGuard — README names this repository
https://raw.githubusercontent.com/dongwxxkchoi/EMBGuard/main/scripts/train/qwen3vl_full_sft.yaml — 2B full fine-tune config
https://raw.githubusercontent.com/dongwxxkchoi/EMBGuard/main/scripts/train/train_qwen3vl_full.sh — script that runs that config
https://huggingface.co/datasets/EMBGuard/EMBHazard — training set; 15,115 rows
https://huggingface.co/api/datasets/EMBGuard/EMBHazard — language and split size
https://huggingface.co/datasets/EMBGuard/EMBGuardTest_v2 — evaluation set; 329 rows
https://huggingface.co/datasets/EMBGuard/heldout_set — evaluation set; Hub page reports 1,130 rows

## Record

Training uses EMBHazard only. The paper says: "We train EMBGuard using Qwen-3-VL models (34) with 2B and 4B parameters through supervised fine-tuning on EMBHazard." The Hub dataset `EMBGuard/EMBHazard` has 15,115 train rows, language English, and the viewer shows rows, so it loads. The paper says the images are synthetic: "EMBHazard was generated entirely synthetically." The card also names `EMBGuard/EMBGuardTest_v2` and `EMBGuard/heldout_set`. Those are evaluation sets. EMBGuardTest has 329 manually curated real-world samples. The paper's held-out set is 563 samples drawn from EMBHazard. The Hub page for `EMBGuard/heldout_set` reports 1,130 rows.

The objective is supervised fine-tuning of the language model. The 2B config says `stage: sft` and `finetuning_type: full`, and it sets `freeze_vision_tower: true`, `freeze_multi_modal_projector: true`, and `freeze_language_model: false`. The paper says: "Importantly, we freeze the vision encoder during training." Learning rate is 1e-5. The config plans 4 epochs, batch size 1 per device, and gradient accumulation 8, in bf16. The paper says training used 8 A6000 GPUs. This repository's `trainer_state.json` stops at epoch 3.0, step 711, with `max_steps` 948 and `num_train_epochs` 4. There is no LoRA rank. A separate LoRA script exists in the same GitHub repository and is not the config whose `model_name_or_path` is `Qwen/Qwen3-VL-2B-Instruct`.

The parent is `Qwen/Qwen3-VL-2B-Instruct`. The card YAML and the training YAML both print that id. The paper says the 2B model is a Qwen-3-VL model.

This is a physical-risk classifier for a robot, not a support chatbot. The paper says the guardrail "outputs risk assessment (safe/unsafe), risk type, and hazard description." The mental-health use claim is absent. The card has no warning text. The paper's limitation is about robots: "deployment in real-world robotic systems requires thorough validation and careful consideration by practitioners." The inventory methods field is blank. The license is `apache-2.0`.

The input is an image plus an action, not text alone. The paper says: "the guardrail takes a scene image and an associated action as input." A chat template is present. No system-prompt string is given. `generation_config.json` sets `do_sample` true, temperature 0.7, top_k 20, and top_p 0.8. `config.json` sets `max_position_embeddings` to 262144. The Hub API reports 2,127,532,032 parameters. The card says the language is English. The card has no prose description after the title.
