# NikkeS/DeepSeek-8B-Finetuned-Medical-O1-Reasoning-SFT-Q8_0-GGUF

## Sources

- https://huggingface.co/NikkeS/DeepSeek-8B-Finetuned-Medical-O1-Reasoning-SFT-Q8_0-GGUF/raw/main/README.md — current model card; identical to the 10 October 2026 cache
- https://huggingface.co/api/models/NikkeS/DeepSeek-8B-Finetuned-Medical-O1-Reasoning-SFT-Q8_0-GGUF — file list and GGUF parameter count
- https://huggingface.co/NikkeS/DeepSeek-8B-Finetuned-Medical-O1-Reasoning-SFT-Q8_0-GGUF/raw/main/config.json — Llama config, context 131072, float16
- https://huggingface.co/NikkeS/DeepSeek-8B-Finetuned-Medical-O1-Reasoning-SFT-Q8_0-GGUF/raw/main/generation_config.json — temperature 0.6, top_p 0.95
- https://huggingface.co/NikkeS/DeepSeek-8B-Finetuned-Medical-O1-Reasoning-SFT-Q8_0-GGUF/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — named training dataset
- https://arxiv.org/abs/2412.18925 — paper linked from that dataset card; it does not name this repository
- https://huggingface.co/NikkeS/deepSeek-finetuned-Medical-O1-Reasoning-SFT — same author's LoRA repository, not linked from this card

## Record

The training dataset is `FreedomIntelligence/medical-o1-reasoning-SFT`. It loads and has 90,120 rows. Its card says the set “is constructed using GPT-4o” and checked by a medical verifier. This model card does not say which split or how many rows were used.

The card says the fine-tuning method is “LoRA (Low-Rank Adaptation).” It does not name a loss. The dataset id contains “SFT,” which is not a statement that this checkpoint was trained with supervised fine-tuning. Epochs 1, max steps 60, batch size 2 per device, gradient accumulation 4, learning rate 2e-4, AdamW 8-bit, seed 3407. LoRA rank and alpha are not on this card. The card does not say whether the base was quantized during training. The file `unsloth.Q8_0.gguf` is an 8-bit GGUF for inference. The repository also contains four float16 `pytorch_model.bin` shards. The card does not say the adapter was merged.

The parent is `unsloth/DeepSeek-R1-Distill-Llama-8B`. The GGUF header reports 8,030,261,312 parameters. The card’s language tag is English. The license is MIT.

The model is for “advanced medical reasoning tasks.” The only example is a text vignette about cough-related urine loss and what cystometry would show. That is medical question answering, including an exam-style item, not a stated diagnosis or treatment service. The use claim is moderate. There is no warning about medical use.

No audience is named. The functions are medical reasoning and answering the medical question in the example. The output is a chat reply from `ollama run`, and the card calls the task reasoning. The specialty is general medicine. The example happens to be a gynecology vignette; the card does not name a specialty.

Serving is text only. A chat template is present and does not set a medical system prompt. `generation_config.json` uses temperature 0.6, top_p 0.95, and do_sample true. The llama.cpp example uses `--temp 0.7`. Context length is 131,072. No evaluation numbers are printed. No paper names this repository.

The same author’s LoRA repository states rank 16, alpha 16, and “Quantization: FP16,” with the same step count, seed, and example question. This card does not link that repository. The link printed on this card uses a different repository id and returned HTTP 401.
