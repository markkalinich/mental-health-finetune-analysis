# yavuz-ai/qwen3-4b-cai-sft

## Sources

https://huggingface.co/yavuz-ai/qwen3-4b-cai-sft/raw/main/README.md — current model card; identical to the cached card
https://huggingface.co/api/models/yavuz-ai/qwen3-4b-cai-sft — file list and parameter count
https://huggingface.co/yavuz-ai/qwen3-4b-cai-sft/raw/main/config.json — architecture and context length
https://huggingface.co/yavuz-ai/qwen3-4b-cai-sft/raw/main/generation_config.json — sampling settings
https://huggingface.co/yavuz-ai/qwen3-4b-cai-sft/raw/main/tokenizer_config.json — tokenizer; no chat_template key
https://huggingface.co/yavuz-ai/qwen3-4b-cai-sft/raw/main/chat_template.jinja — chat template
https://arxiv.org/abs/2212.08073 — Bai et al. 2022 abstract; does not name this repo
https://arxiv.org/html/2212.08073 — HTML full text of that paper; no match for this repo id
https://github.com/shipbehaves/constitutional-cai — writeup that names this checkpoint as the SL-CAI stage
https://github.com/shipbehaves/constitutional-cai/blob/main/NOTES.md — lab notes on over-refusal
https://github.com/shipbehaves/constitutional-cai/blob/main/src/train_sft.py — SFT script whose run line targets this repo
https://github.com/shipbehaves/constitutional-cai/blob/main/src/redteam.py — loads harmless-base prompts
https://huggingface.co/datasets/yavuz-ai/cai-sft — SFT rows the script loads; viewer shows 4,804 rows
https://huggingface.co/datasets/Anthropic/hh-rlhf — prompt source named on the card; viewer shows 169,352 rows
https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/raw/main/README.md — parent card text-only quickstart
https://featherless.ai/models/yavuz-ai/qwen3-4b-cai-sft — third-party inference page found by search

## Record

The training rows are `yavuz-ai/cai-sft`, 4,804 prompt-completion pairs, and the Hub viewer loads them. The script says "LoRA SFT on the filtered self-revisions." The card says "Data: ~4,800 self-revisions generated from hh-rlhf harmless-base prompts." Those prompts come from `Anthropic/hh-rlhf`, which the Hub page loads (169,352 rows in the full set). The dataset cards do not state a language. The revisions are model-written. The prompts are human text from the harmless-base split.

The objective is supervised fine-tuning. The card says "LoRA SFT (r=16, alpha=32, all-linear), completion-only loss on the revised answers, 2 epochs, lr 1e-4, bf16, on 1x A100." The script uses the same rank, alpha, epochs, and learning rate, sets an effective batch of 16 (`per_device_train_batch_size=4`, `gradient_accumulation_steps=4`), loads the base in bfloat16, and calls `merge_and_unload`. No step count is stated (`MAX_STEPS` defaults to -1). This repo is the supervised stage. The RLAIF DPO stage is a different repository.

The parent is `Qwen/Qwen3-4B-Instruct-2507`. The card YAML says `base_model: Qwen/Qwen3-4B-Instruct-2507`. The GitHub table links that same repo as "base", and `train_sft.py` defaults `BASE_MODEL` to it. The Hub file list counts 4,022,468,096 parameters. Bai et al. 2022 does not name this checkpoint.

The card describes a Constitutional AI reproduction published "for reproducibility and failure analysis, not as a general-purpose model." That is a research checkpoint, not a chatbot offered for conversation, and it makes no therapy or mental-health claim. There is no warning sentence about therapy, medical use, hallucination, bias, or language. The GitHub table reports this checkpoint at 1.000 safe on harmful prompts and 0.431 over-refusal on benign prompts, against a base of 0.989 and 0.327.

The parent quickstart runs a text prompt, `prompt = "Give me a short introduction to large language model."`, with no image or audio. This repo has `chat_template.jinja` and no fixed system prompt. `generation_config.json` sets `do_sample` true, temperature 0.7, top_k 20, and top_p 0.8. `config.json` sets `max_position_embeddings` to 262144. License is apache-2.0.
