# yushaohan/ProGuard-7B

## Sources

https://huggingface.co/yushaohan/ProGuard-7B/raw/main/README.md — current model card; identical to the cached card
https://huggingface.co/api/models/yushaohan/ProGuard-7B — file list, parameter count, and chat template
https://huggingface.co/yushaohan/ProGuard-7B/raw/main/config.json — architecture, context length, and checkpoint path
https://huggingface.co/yushaohan/ProGuard-7B/raw/main/generation_config.json — sampling settings
https://huggingface.co/yushaohan/ProGuard-7B/raw/main/tokenizer_config.json — tokenizer; no chat_template key
https://arxiv.org/abs/2512.23573 — ProGuard abstract
https://arxiv.org/html/2512.23573 — ProGuard HTML full text; names ProGuard-7B and the 7B backbone
https://arxiv.org/abs/2602.12092 — DeepSight abstract, cited on the card; does not name this repo
https://github.com/yushaohan/ProGuard — code repo
https://github.com/yushaohan/ProGuard/blob/master/train/proguard-train.sh — GRPO script whose experiment name is not this checkpoint
https://github.com/yushaohan/ProGuard/blob/master/deploy/README.md — deploy instructions that link this repo
https://github.com/yushaohan/ProGuard/blob/master/deploy/prompts.py — safety-label system prompts
https://huggingface.co/datasets/yushaohan/ProGuard-data — training set; viewer shows 87,024 rows
https://github.com/AI45Lab/DeepSafe — evaluation toolkit; README links this exact repo
https://yushaohan.github.io/ProGuard/ — project page linked from the card

## Record

The training set is `yushaohan/ProGuard-data`. The dataset card says "This dataset is multimodal data used to train ProGuard-7B and ProGuard-3B." The Hub viewer loads it and shows 87,024 rows. The paper built it from ten existing datasets, including real and generated images, then relabeled the rows with language models and vision-language models. The dataset card does not state a language.

The objective is GRPO. The paper says "we bypass the SFT stage entirely and adopt pure GRPO training," and Appendix C says "The training is performed on the Qwen2.5-VL-7B-Instruct backbone." That table sets learning rate \(1\times 10^{-6}\), training batch size 512, and 1 epoch. This repo's `config.json` path ends in `ckpt-7b/global_step_160/actor/huggingface`, so the saved actor is step 160. The released `proguard-train.sh` uses batch 256 and the experiment name `safety_grm_qwen3vl_8b_megatron_grpo`, so those script numbers are not this checkpoint's stated run. No sentence says LoRA or a quantized base. The repo ships full safetensors and has no `adapter_config.json`.

The parent is `Qwen/Qwen2.5-VL-7B-Instruct`. The card YAML says that id. The paper says the training "is performed on the Qwen2.5-VL-7B-Instruct backbone." The Hub file list counts 8,292,166,656 parameters. The card YAML lists language `en`.

The card says "ProGuard is a proactive multimodal safeguard model" that identifies risks "across both text and visual modalities." The deploy prompt says to "only output Request and Response safety labels." There is no therapy or mental-health claim, and no sentence that forbids therapy or medical use. License is not stated. The paper says "our ProGuard-7B model sets the state-of-the-art performance among open-source guard models" on prompt classification.

Input is not text-only. `generation_config.json` sets `do_sample` true, temperature 1e-6, and repetition penalty 1.05. `max_position_embeddings` is 128000. The chat template's default system line is "You are a helpful assistant." The official deploy system prompt starts "Check if there is unsafe content in 'User' and 'Agent' messages in a text-only conversation according to our safety policy." DeepSafe's README links `https://huggingface.co/yushaohan/ProGuard-7B` as its ProGuard evaluation model.
