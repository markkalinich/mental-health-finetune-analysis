# XformAI-india/Qwen3-4B-medicaldataset

## Sources

- https://huggingface.co/XformAI-india/Qwen3-4B-medicaldataset/raw/main/README.md — current model card; same wording as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/XformAI-india__Qwen3-4B-medicaldataset__2026-10-10.md — cached card, sha256 32c93e5393d39c612905ef2bd51c69658ab38a4d49c146c4772dcd76fe607e88
- https://huggingface.co/api/models/XformAI-india/Qwen3-4B-medicaldataset — file list and tokenizer chat template
- https://huggingface.co/XformAI-india/Qwen3-4B-medicaldataset/raw/main/config.json — context length 40960, dtype float16
- https://huggingface.co/XformAI-india/Qwen3-4B-medicaldataset/raw/main/generation_config.json — sampling settings
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — dataset card named on the model card
- https://arxiv.org/html/2505.09388v1 — Qwen3 technical report; does not print this repository id
- https://arxiv.org/abs/2412.18925 — dataset citation (HuatuoGPT-o1); listed only, not read in full
- https://github.com/QwenLM/Qwen3 — official Qwen3 repository found by the GitHub search; it does not name this checkpoint
- https://featherless.ai/models/XformAI-india/Qwen3-4B-medicaldataset — inference host that repeats the card

## Record

The card names one training set, `FreedomIntelligence/medical-o1-reasoning-SFT`. That dataset page loads. It reports 90,120 rows, English and Chinese configs, and says "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." The model card does not say which split was used.

The objective is supervised fine-tuning. The card says "Fine-tuning method: Supervised fine-tuning (SFT)". It also says epochs 3, batch size 8, learning rate 2e-5, and gradient accumulation 4. It does not say whether every weight was updated or a LoRA adapter was trained. The repository ships two weight shards and no `adapter_config.json`.

The parent on the card is Qwen/Qwen3-4B: "A fine-tuned version of Qwen3-4B on a curated medical dataset". No paper or GitHub repository names this checkpoint. The Qwen3 technical report is about the base series.

The use claim is strong. The card lists "Medical reasoning and triage" and "Chatbot integration for healthcare support (non-diagnostic)", and it says the model is "designed to assist with medical Q&A, clinical documentation, and healthcare-related reasoning." The warning is a disclaimer: "Not for clinical use. This model is not a replacement for professional medical advice, diagnosis, or treatment." A later bullet says "Should not be used in emergency or high-stakes settings." That forbids a setting. It does not say the model must not be used for diagnosis, treatment, or medical advice, so the warning stays a disclaimer.

The purpose is stated: "This model is intended for research and educational purposes in the following domains." It does not name a person, so the audience list is empty.

The card claims these functions: medical question answering, summarizing patient records, medical reasoning, triage, and clinical documentation.

The tasks are medical question answering, summarizing patient records, triage, and, in the usage example, a differential-diagnosis question: "What are possible differential diagnoses?" The specialty is general medicine. The card says medical and healthcare and names no field. No evaluation numbers are on the card.

Serving is text in and text out. The example prompt is "Patient presents with chest pain and shortness of breath. What are possible differential diagnoses?" A Qwen3 chat template is present and does not set a medical system prompt. `generation_config.json` sets do_sample true, temperature 0.6, top_k 20, and top_p 0.95. This repository's `config.json` sets max_position_embeddings to 40960. The Qwen3 report lists 128K for the base Qwen3-4B. The card says the size is 4 billion parameters. The license is MIT.
