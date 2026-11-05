# cs-552-2026-Flash-McQueenS-and-TheKing/safety_model

## Sources

https://huggingface.co/cs-552-2026-Flash-McQueenS-and-TheKing/safety_model/raw/main/README.md — current model card; byte-identical to the cache, and the How to use code block is cut off
https://huggingface.co/api/models/cs-552-2026-Flash-McQueenS-and-TheKing/safety_model — file list, parameter count, and chat template
https://huggingface.co/cs-552-2026-Flash-McQueenS-and-TheKing/safety_model/raw/main/config.json — Qwen3 architecture and context length
https://huggingface.co/cs-552-2026-Flash-McQueenS-and-TheKing/safety_model/raw/main/generation_config.json — sampling defaults
https://huggingface.co/cs-552-2026-Flash-McQueenS-and-TheKing/safety_model/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
https://huggingface.co/datasets/cs-552-2026-Flash-McQueenS-and-TheKing/safety_sft_data — released training set; viewer shows 3,250 rows
https://huggingface.co/datasets/heegyu/bbq — Hub copy of BBQ
https://huggingface.co/datasets/hendrycks/ethics — ETHICS, including the commonsense split
https://huggingface.co/datasets/walledai/SafeText — Hub copy of SafeText
https://huggingface.co/datasets/cardiffnlp/tweet_eval — TweetEval, including the offensive split
https://arxiv.org/html/2309.07045v2 — SafetyBench HTML; does not name this repository
https://arxiv.org/abs/2409.12183 — Sprague et al. CoT paper cited on the card; listed by URL only
https://github.com/thu-coai/SafetyBench — SafetyBench benchmark repository linked from that paper, not this model's training code
https://featherless.ai/models/cs-552-2026-Flash-McQueenS-and-TheKing/safety_model — hosted inference page that restates the card

## Record

The training set is `cs-552-2026-Flash-McQueenS-and-TheKing/safety_sft_data`, 3,250 English multiple-choice items. The card says "Four categories are derived from established public datasets; three smaller categories are LLM-generated." The public rows are BBQ 700, ETHICS commonsense 700, SafeText 700, and TweetEval offensive 700. The synthetic rows are Mental Health 150, Illegal Activities 150, and Privacy and Property 150. The Hub dataset loads. Those four public sets also have Hub pages that load. The three synthetic categories have no separate Hub dataset.

The objective is supervised fine-tuning. The card says "Supervised fine-tuning with LoRA, then merged to a full checkpoint" and "Loss | Completion-only." It also says "We deliberately did not" distill chain-of-thought. LoRA rank is 16 and alpha is 32. Epochs are 3. Learning rate is 1e-4. Effective batch size is 16 (per-device 2 times gradient accumulation 8). No step count is given. Precision is "bf16/fp16," so the base was not quantized. "The LoRA adapter was merged back into the base weights." The file list is a full `model.safetensors` (1,720,574,976 float16 parameters) and no adapter file.

The parent is "Qwen/Qwen3-1.7B." No paper names this repository. The card calls it "a 1.7B model."

The model writes a one-sentence justification and an answer letter: "Every answer ends with the option letter wrapped in `\boxed{...}`." That is a multiple-choice label, not a conversation. One training category is "Mental Health | LLM-generated | 150," so the card has mental-health content and does not offer support. The limitation is about deployment as a moderator, not about therapy: "it is not a content-moderation or refusal system and should not be used as one." The card describes pass@1 scoring and does not report this model's score. License is Apache-2.0.

The task is text. The chat template inserts "You are answering a multiple-choice question. Give a one-sentence justification, then put ONLY the letter of the correct option inside \boxed{}." `generation_config.json` sets `do_sample` true, temperature 0.3, top_k 20, and top_p 0.9. `config.json` sets `max_position_embeddings` to 40960.
