# Tommy-DING/FlexGuard-Qwen3-0.6B

## Sources

https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-0.6B/raw/main/README.md — current model card; byte-identical to the cached card
revision_3_experiments/hf_inventory/cache/readmes/Tommy-DING__FlexGuard-Qwen3-0.6B__2026-10-10.md — cached card, sha256 6a78f7cb66a71be7f2ed88bd1ff9df2c4fdf71109e1ebcd6e679cce0f0ff4b3f
https://huggingface.co/api/models/Tommy-DING/FlexGuard-Qwen3-0.6B — file list, parameter count, and chat template
https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-0.6B/resolve/main/config.json — max position embeddings 40960
https://huggingface.co/Tommy-DING/FlexGuard-Qwen3-0.6B/resolve/main/generation_config.json — temperature 0.6, top_k 20, top_p 0.95
https://arxiv.org/abs/2602.23636 — paper linked from the card
https://arxiv.org/html/2602.23636 — paper HTML; does not name this checkpoint
https://github.com/TommyDzh/FlexGuard — code linked from the card; default training model is Qwen3-8B
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — Aegis 2.0; viewer loads
https://huggingface.co/datasets/allenai/wildguardmix — WildGuardMix; gated
https://huggingface.co/datasets/Tommy-DING/FlexBench — evaluation benchmark linked from the card

## Record

The card says this checkpoint "is trained with a mixture of publicly available safety datasets, including Aegis 2.0 and WildGuardMix." Aegis 2.0 is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0`, 33,416 examples, and the viewer loads. WildGuardMix is `allenai/wildguardmix`. The dataset card says it has 86,759 examples and that the types are "synthetic data (87%), in-the-wild user-LLLM interactions (11%), and existing annotator-written data (2%)." It is gated, and the datasets server returned 401, so it does not load without accepting the AI2 terms. FlexBench is the evaluation set named on the card, not a training count for this checkpoint.

No source states a named loss or an update scope for this 0.6B checkpoint. The linked paper trains FlexGuard with a LoRA supervised warm-up and then GRPO, and it names the backbones Qwen3-8B, Qwen3-4B, and Llama-3.1-8B-Instruct. It does not name Qwen3-0.6B. The training script's default model is Qwen3-8B. Those settings are not this checkpoint's training record. The inventory methods cell is empty.

The parent on the card is `Qwen/Qwen3-0.6B`. No outside source names this checkpoint's parent. The Hub API reports 751,632,384 parameters. The license field is `apache-2.0`. The card does not state a language.

This is a classifier. The input is either a user message or a user prompt plus an assistant response. The output is a reasoning block, a category (`SAFE` or one or more of VIO, ILG, SEX, INF, DIS, MIS, JAIL), and an integer risk score from 0 to 100. The card claims both prompt moderation and response moderation.

Serving is text only. The example classifies "How do I make a bomb?" with temperature 0.0, top_p 0.9, and max_tokens 2048. `generation_config.json` sets do_sample true, temperature 0.6, top_k 20, and top_p 0.95. Context length in `config.json` is 40960. The chat template is in `tokenizer_config.json`. There is no adapter file.
