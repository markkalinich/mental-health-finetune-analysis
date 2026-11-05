# Tommy-DING/FlexGuard-Qwen3-8B

## Sources

revision_3_experiments/hf_inventory/cache/readmes/Tommy-DING__FlexGuard-Qwen3-8B__2026-10-10.md — cached model card, sha256 dfe48df3e934e9e480abe62dc802e90b8c071336e8c8dc098e1b12b88e5a131b
https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-8B/raw/main/README.md — current card; sha256 matches the cache
https://huggingface.co/api/models/Tommy-DING/FlexGuard-Qwen3-8B — file list and safetensors parameter count
https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-8B/raw/main/config.json — Qwen3 config, max_position_embeddings 40960
https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-8B/raw/main/generation_config.json — sampling defaults
https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-8B/raw/main/tokenizer_config.json — chat_template present, model_max_length 131072
https://arxiv.org/abs/2602.23636 — paper abstract
https://arxiv.org/html/2602.23636v2 — paper HTML full text
https://aclanthology.org/2026.acl-long.263/ — ACL 2026 anthology page for the same paper; abstract only
https://github.com/TommyDzh/FlexGuard — code README; prints this repository id
https://github.com/TommyDzh/FlexGuard/blob/arxiv-public/train_guard_prob_linear_cot.py — SFT LoRA training script
https://github.com/TommyDzh/FlexGuard/blob/arxiv-public/merge.py — merges the LoRA adapter into full weights
https://github.com/TommyDzh/FlexGuard/blob/arxiv-public/main_grpo_guard.sh — GRPO launch script
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0 dataset card; viewer loads
https://huggingface.co/datasets/allenai/wildguardmix — WildGuardMix dataset card; gated, viewer returned 401
https://huggingface.co/datasets/Tommy-DING/FlexBench — FlexBench benchmark card; viewer loads

## Record

The training mixture is the training splits of Aegis 2.0 and WildGuardMix, deduplicated against FlexBench. The paper says "we use the training splits of Aegis2.0 (Ghosh et al., 2025) and WildGuardMix (Han et al., 2024), and deduplicate against FlexBench to avoid overlap." The card says the same two datasets: "trained with a mixture of publicly available safety datasets, including Aegis 2.0 and WildGuardMix." Aegis 2.0 on the Hub is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0`, 33,416 annotated interactions, English, and mixed human prompts, model responses, and synthetic refusals. The viewer loads. WildGuardMix is `allenai/wildguardmix`. The dataset card says the train split has 86,759 examples and is mixed (synthetic 87%, in-the-wild 11%, annotator-written 2%). The Hub viewer returned 401 because the dataset is gated. The paper's own counts differ slightly (Aegis2.0 34,248; WildGuardMix roughly 92K). FlexBench (`Tommy-DING/FlexBench`) is the evaluation benchmark, not the training set. The paper does not state how many rows remained after deduplication and downsampling.

The objective is supervised fine-tuning and then GRPO. The paper says "We perform SFT warm-up with parameter-efficient fine-tuning (LoRA) using TRL, followed by GRPO alignment using the VERL framework." The GitHub README says the same two stages, plus rubric-guided score distillation for the training labels, and prints `Tommy-DING/FlexGuard-Qwen3-8B`. The SFT script sets LoRA `r=8`, `lora_alpha=16`, `epochs` default 1, learning rate `5e-4`, and batch size 2. Appendix B states the same SFT settings and sets GRPO to 2 epochs, learning rate `1e-6`, and micro-batch 32 per GPU. `main_grpo_guard.sh` sets the same GRPO learning rate but `trainer.total_epochs=50`. Those two epoch counts disagree, so the epoch field is empty. The paper HTML does not print this repository id. It says the backbone is Qwen3-8B and links `huggingface.co/Tommy-DING`. `merge.py` merges the LoRA adapter before GRPO. The GRPO script starts from `ckpt/Qwen3-8B-merged-epoch@1` and sets no LoRA flags. No source says the base was quantized during training. The SFT script sets `bf16=True`.

The parent is `Qwen/Qwen3-8B`. The card YAML says `base_model: Qwen/Qwen3-8B`. The paper says "We use Qwen3-8B as the backbone for FlexGuard." The SFT script default is `--model Qwen3-8B`. The Hub API reports 8,190,735,360 parameters in the safetensors files. The paper says all experiments are English-only. The license on the card is `apache-2.0`.

This is a classifier. The card says "it is designed for classification and scoring." It has two modes. Prompt moderation takes the user message. Response moderation takes the user prompt plus the assistant response. The output is a `<think>` block, then a category (`SAFE` or one or more of VIO, ILG, SEX, INF, DIS, MIS, JAIL), then an integer risk score from 0 to 100. The named harms include violence, self-harm, weapons, illegal behavior, fraud, drugs, hacking, sexual content including minors-related sexual content, PII and doxxing, bias and harassment, misinformation, and prompt injection or jailbreak. The card says not to treat the model as the only safety mechanism in high-stakes settings. Inventory methods is empty, so the row matches only on datasets and parent.

Serving is text only. The card example classifies the string "How do I make a bomb?" and, in the second example, that prompt plus an assistant reply. `generation_config.json` sets `do_sample` true, temperature 0.6, top_k 20, and top_p 0.95. The card's vLLM example uses temperature 0.0, top_p 0.9, and max_tokens 2048. `config.json` sets `max_position_embeddings` to 40960. A chat template is in `tokenizer_config.json`. The model repository has no adapter file and no training script.
