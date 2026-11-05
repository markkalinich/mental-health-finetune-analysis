# yushaohan/ProGuard-3B

## Sources

https://huggingface.co/yushaohan/ProGuard-3B/raw/main/README.md — current model card; identical to the cached card
https://huggingface.co/api/models/yushaohan/ProGuard-3B — file list and parameter count
https://huggingface.co/yushaohan/ProGuard-3B/raw/main/config.json — architecture, context length, and checkpoint path
https://huggingface.co/yushaohan/ProGuard-3B/raw/main/generation_config.json — sampling settings
https://huggingface.co/yushaohan/ProGuard-3B/raw/main/tokenizer_config.json — tokenizer; no chat_template key
https://huggingface.co/yushaohan/ProGuard-3B/raw/main/chat_template.jinja — chat template with image and video tokens
https://arxiv.org/abs/2512.23573 — ProGuard abstract
https://arxiv.org/html/2512.23573 — ProGuard HTML full text; names ProGuard-3B
https://arxiv.org/abs/2602.12092 — DeepSight abstract, cited on the card; does not name this repo
https://github.com/yushaohan/ProGuard — code repo
https://github.com/yushaohan/ProGuard/blob/master/train/proguard-train.sh — GRPO training script; experiment name is not this checkpoint
https://github.com/yushaohan/ProGuard/blob/master/deploy/README.md — deploy instructions that link this repo
https://github.com/yushaohan/ProGuard/blob/master/deploy/prompts.py — safety-label system prompts
https://huggingface.co/datasets/yushaohan/ProGuard-data — training set; viewer shows 87,024 rows
https://github.com/AI45Lab/DeepSafe — evaluation toolkit; its README links ProGuard-7B, not this repo
https://yushaohan.github.io/ProGuard/ — project page linked from the card

## Record

The training set is `yushaohan/ProGuard-data`. The dataset card says "This dataset is multimodal data used to train ProGuard-7B and ProGuard-3B." The Hub viewer loads it and shows 87,024 rows. The paper says the set was built from ten existing datasets, including real and generated images, then relabeled by language models and vision-language models with a majority vote. That is mixed provenance. The dataset card does not state a language.

The paper's training section says "we bypass the SFT stage entirely and adopt pure GRPO training." The same paper names ProGuard-3B in the result tables and says both sizes were obtained "through reinforcement fine-tuning." This repo's `config.json` path ends in `ckpt-3b/global_step_138/actor/huggingface`, so the saved actor is step 138. The paper's hyperparameter table is a different sentence: "The training is performed on the Qwen2.5-VL-7B-Instruct backbone." Learning rate, epoch count, and batch size from that table are not recorded for this checkpoint. The released `proguard-train.sh` sets GRPO, learning rate 1e-6, train batch 256, and 1 epoch, and its experiment name is `safety_grm_qwen3vl_8b_megatron_grpo`. No sentence says LoRA or a quantized base. The repo ships full safetensors and has no `adapter_config.json`.

The card YAML says `base_model: Qwen/Qwen2.5-VL-3B-Instruct`. No paper or GitHub sentence states that parent id. The Hub file list counts 4,065,787,904 parameters. The card YAML lists language `en`.

The card says "ProGuard is a proactive multimodal safeguard model" that identifies risks "across both text and visual modalities." The deploy prompt says to "only output Request and Response safety labels," so the served output is a safety label plus an optional category. There is no therapy or mental-health claim on the card. There is no sentence that forbids therapy or medical use. The deploy README warns that its examples may be disturbing. License is not stated.

Input is not text-only. The card names text and visual modalities, and the deploy script has text, text-image, and image modes. `generation_config.json` sets `do_sample` true, temperature 1e-6, and repetition penalty 1.05. `max_position_embeddings` is 128000. The chat template's default system line is "You are a helpful assistant." The official deploy system prompt starts "Check if there is unsafe content in 'User' and 'Agent' messages in a text-only conversation according to our safety policy."
