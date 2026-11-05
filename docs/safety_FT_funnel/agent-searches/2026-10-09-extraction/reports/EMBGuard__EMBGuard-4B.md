# EMBGuard/EMBGuard-4B

## Sources

https://huggingface.co/EMBGuard/EMBGuard-4B/raw/main/README.md — current model card; same bytes as the cache; YAML only
https://huggingface.co/api/models/EMBGuard/EMBGuard-4B — file list, parameter count, and chat template
https://huggingface.co/EMBGuard/EMBGuard-4B/raw/main/config.json — architecture and context length
https://huggingface.co/EMBGuard/EMBGuard-4B/raw/main/generation_config.json — sampling settings
https://arxiv.org/abs/2605.30924 — EMBGuard abstract; comment says accepted at ICML 2026
https://arxiv.org/html/2605.30924 — EMBGuard full text
https://icml.cc/virtual/2026/poster/63023 — ICML 2026 poster page
https://github.com/dongwxxkchoi/EMBGuard — README names this repository
https://raw.githubusercontent.com/dongwxxkchoi/EMBGuard/main/scripts/train/qwen3vl_full_sft.yaml — full fine-tune config; its base is the 2B model
https://raw.githubusercontent.com/dongwxxkchoi/EMBGuard/main/scripts/train/train_qwen3vl_lora.yaml — LoRA config; its base is also the 2B model
https://huggingface.co/datasets/EMBGuard/EMBHazard — training set; 15,115 rows
https://huggingface.co/datasets/EMBGuard/EMBGuardTest_v2 — evaluation set; 329 rows
https://huggingface.co/datasets/EMBGuard/heldout_set — evaluation set; Hub page reports 1,130 rows

## Record

Training uses EMBHazard only. The paper says: "We train EMBGuard using Qwen-3-VL models (34) with 2B and 4B parameters through supervised fine-tuning on EMBHazard." The Hub dataset has 15,115 rows, language English, and it loads. The paper says EMBHazard was generated entirely synthetically. `EMBGuard/EMBGuardTest_v2` and `EMBGuard/heldout_set` are evaluation sets. EMBGuardTest has 329 manually curated samples.

The objective is supervised fine-tuning. The same paragraph gives learning rate 1e-5, 4 epochs, 8 A6000 GPUs, and says: "Importantly, we freeze the vision encoder during training." This repository has no trainer state and no adapter file, so the saved step, the batch size, and whether the multimodal projector was frozen are not stated for this checkpoint. The GitHub full-finetune YAML and the LoRA YAML both name `Qwen/Qwen3-VL-2B-Instruct`, not this 4B parent. Those files are not this run. No LoRA rank is stated for EMBGuard-4B.

The parent on the card is `Qwen/Qwen3-VL-4B-Instruct`. The paper says the 4B model is a Qwen-3-VL model. That agrees with the card.

This is a physical-risk classifier for a robot, not a support chatbot. The paper says the guardrail "outputs risk assessment (safe/unsafe), risk type, and hazard description." The mental-health use claim is absent. The card has no warning text. The paper says "deployment in real-world robotic systems requires thorough validation and careful consideration by practitioners." The inventory methods field is blank. The license is `apache-2.0`.

The input is an image plus an action. The paper says: "the guardrail takes a scene image and an associated action as input." A chat template is present. No system-prompt string is given. `generation_config.json` sets `do_sample` true, temperature 0.7, top_k 20, and top_p 0.8. `config.json` sets `max_position_embeddings` to 262144. The Hub API reports 4,437,815,808 parameters. The card says the language is English. The card has no prose description after the title.

Table 2 reports EMBGuard-4B at 54.3, 50.3, and 14.6 on EMBGuardTest for potential risk, risk type, and hazard, and 71.2, 67.6, and 50.1 on the held-out set. The planning table reports step accuracy 63.1, precision 25.7, recall 71.7, and F1 38.3. Inference is 0.719 seconds per sample on one RTX 6000 Ada.
