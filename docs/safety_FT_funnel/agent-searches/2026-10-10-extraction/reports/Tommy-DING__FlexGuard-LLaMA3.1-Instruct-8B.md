# Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B

## Sources

https://huggingface.co/Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B/raw/main/README.md — current model card; byte-identical to the cached card
revision_3_experiments/hf_inventory/cache/readmes/Tommy-DING__FlexGuard-LLaMA3.1-Instruct-8B__2026-10-10.md — cached card, sha256 aa848d48fca39ae9cf121deb9754a59aca7aa76119972920e8eebaccc4217e82
https://huggingface.co/api/models/Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B — file list, parameter count, and chat template
https://huggingface.co/Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B/resolve/main/config.json — max position embeddings 131072; unsloth_fixed true
https://huggingface.co/Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B/resolve/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
https://arxiv.org/abs/2602.23636 — paper
https://arxiv.org/html/2602.23636 — paper HTML, training method and Appendix B
https://github.com/TommyDzh/FlexGuard — code linked from the card
https://github.com/TommyDzh/FlexGuard/blob/main/train_guard_prob_linear_cot.py — SFT script, LoRA rank 8
https://github.com/TommyDzh/FlexGuard/blob/main/main_grpo_guard.sh — GRPO script, default path is a merged Qwen3-8B checkpoint
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0 dataset card; viewer loads
https://huggingface.co/datasets/allenai/wildguardmix — WildGuardMix dataset card; gated
https://huggingface.co/datasets/Tommy-DING/FlexBench — FlexBench evaluation set; viewer loads

## Record

The card says this checkpoint "is trained with a mixture of publicly available safety datasets, including Aegis 2.0 and WildGuardMix". The paper says the training splits of Aegis2.0 and WildGuardMix are used, then deduplicated against FlexBench, and that an LLM judge writes the risk scores. Aegis 2.0 is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0`, 33,416 examples, and the Hub viewer loads. Its prompts are human-written and many responses and refusals are model-generated, so the provenance is mixed. WildGuardMix is `allenai/wildguardmix`, language `en`, 86,759 examples in the mix the dataset card describes as 87% synthetic. The dataset is gated (`gated: auto`); the datasets server returned 401, so it does not load without accepting the AI2 terms. FlexBench is the 4,000-example evaluation benchmark, not the training set.

The final training stage is GRPO. The paper says "We further align the warmed-up model using Group Relative Policy Optimization (GRPO)." The warm-up is supervised fine-tuning with LoRA. The paper says "parameter-efficient fine-tuning (LoRA)". The training script sets `r=8`, `lora_alpha=16`, and `bf16=True`. GitHub then says "Merge LoRA adapter" and runs GRPO on the merged checkpoint. The Hub repository is full weights, with no adapter file, so the adapter was merged. Appendix B reports GRPO at learning rate 1e-6, 2 epochs, and micro batch size 32 per GPU. The SFT defaults in the script are learning rate 5e-4, 1 epoch, and batch size 2. The script's default model is `Qwen3-8B`, and the paper's main-result sentence says "We use Qwen3-8B as the backbone." This Llama checkpoint is one of the backbones in the paper's transfer figure, not a separately tabulated run. The paper does not print `Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B`.

The parent on the card is `meta-llama/Llama-3.1-8B-Instruct`. The paper names that model as a FlexGuard backbone. The Hub API reports 8,030,261,248 parameters. The card's license field is `apache-2.0`. Its `license_link` points at the Llama 3.1 license file. The paper says the experiments are English-only.

This is a classifier. It has two inputs: a user message, and a user prompt plus an assistant response. It writes a reasoning block, a category (`SAFE` or one or more of VIO, ILG, SEX, INF, DIS, MIS, JAIL), and an integer risk score from 0 to 100. The detection claim covers both the user message and the assistant output, so it is not only one of those jobs. The inventory methods cell is empty.

Serving is text only. The card example classifies "How do I make a bomb?" with temperature 0.0, top_p 0.9, and max_tokens 2048. `generation_config.json` instead sets temperature 0.6 and do_sample true. Context length is 131072. The chat template is in `tokenizer_config.json`.
