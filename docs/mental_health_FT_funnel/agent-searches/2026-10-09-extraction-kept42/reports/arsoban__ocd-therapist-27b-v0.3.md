# arsoban/ocd-therapist-27b-v0.3

## Sources

- https://huggingface.co/arsoban/ocd-therapist-27b-v0.3/raw/main/README.md — current model card; same text as the cache
- https://huggingface.co/api/models/arsoban/ocd-therapist-27b-v0.3 — file list and safetensors parameter total
- https://huggingface.co/arsoban/ocd-therapist-27b-v0.3/raw/main/config.json — Gemma 3 text and vision config
- https://huggingface.co/arsoban/ocd-therapist-27b-v0.3/raw/main/generation_config.json — sampling settings
- https://huggingface.co/arsoban/ocd-therapist-27b-v0.3/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://huggingface.co/arsoban/ocd-therapist-27b-v0.3/raw/main/chat_template.jinja — chat template, including an image branch
- https://huggingface.co/datasets/arsoban/ocd-ds-v0.3 — dataset card
- https://huggingface.co/api/datasets/arsoban/ocd-ds-v0.3 — gated flag, language, viewer off
- https://ocd-therapist.codebyars.dev/ — linked chat demo

## Record

The card says the model was fine-tuned on `arsoban/ocd-ds-v0.3`, "a curated synthetic dataset of therapeutic conversations for OCD." The dataset card says "This dataset contains 100% synthetic data" and "Total Conversations: ~1000 (post-curation)." Skeletons came from Claude 3.7 Sonnet, dialogues from Gemini 2.5 Flash, then a person filtered them. Language tag is English. The dataset API says `gated: manual` and `viewer: false`, so the rows do not load without access. The exact row count is not printed.

No sentence names a loss, LoRA, QLoRA, rank, epochs, steps, learning rate, or batch size. "Fine-tuned" is the only training word. The repo holds twelve safetensors shards and no `adapter_config.json`. The card names the parent `google/gemma-3-27b-it`. No paper or GitHub repository names this checkpoint. The title says 27B. The Hub API reports 27,432,406,640 BF16 parameters.

The card presents a chatbot: "designed to simulate supportive therapeutic conversations" for OCD, using ERP, CBT, and ACT. That is a strong therapy claim. The warning is a disclaimer: "This model is **not** a replacement for professional mental health care." Out-of-scope uses include clinical diagnosis and replacement for professional therapy. There is no "must not" or "do not use for" sentence. Qualitative checks are listed, and the card says the model has not undergone clinical trials.

The usage example sends a text user message and no image. `config.json` still has a SigLIP vision tower and image tokens, and the chat template accepts an image item. `generation_config.json` sets `do_sample` true, `top_k` 64, and `top_p` 0.95. `max_position_embeddings` is 131072. The recommended system prompt says the assistant is "specialized in providing evidence-based therapy for OCD." The inventory row matches: empty methods, this dataset, and this parent.
