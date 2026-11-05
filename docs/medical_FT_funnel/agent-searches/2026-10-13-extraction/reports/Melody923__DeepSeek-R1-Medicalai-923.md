# Melody923/DeepSeek-R1-Medicalai-923

## Sources

https://huggingface.co/Melody923/DeepSeek-R1-Medicalai-923/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/Melody923__DeepSeek-R1-Medicalai-923__2026-10-10.md — cached card, sha256 1965cd2dff58e00c8425f5814cc5a431aed19ec419bf9d6fe870ff106c8ddaab
https://huggingface.co/api/models/Melody923/DeepSeek-R1-Medicalai-923 — file list and parameter count
https://huggingface.co/Melody923/DeepSeek-R1-Medicalai-923/raw/main/adapter_config.json — LoRA rank, alpha, and 4-bit base id
https://huggingface.co/Melody923/DeepSeek-R1-Medicalai-923/raw/main/config.json — architecture, context length, and base id
https://huggingface.co/Melody923/DeepSeek-R1-Medicalai-923/raw/main/generation_config.json — sampling settings
https://huggingface.co/Melody923/DeepSeek-R1-Medicalai-923/raw/main/tokenizer_config.json — chat template
https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — dataset card
https://github.com/Melody-coder923 — author profile linked from the card; no training repository for this checkpoint

## Record

The card trains on FreedomIntelligence/medical-o1-reasoning-SFT. That dataset loads on the Hub. The dataset page states 90,120 rows across English, Chinese, and mixed medical/general files. The English viewer shows 19.7k rows. The card does not say which file was used. The dataset card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." Languages on the dataset card are English and Chinese. The dataset card cites HuatuoGPT-o1 (arXiv 2412.18925). That paper is about a different model. A search for this repository id found no paper that names this checkpoint.

The card tag list includes `sft`. The prose only says "This is fine tuned model on Medical dataset with Deepseek llama 3-8b distill." The run is QLoRA. adapter_config.json sets `"peft_type": "LORA"`, `"r": 16`, `"lora_alpha": 16`, and `"base_model_name_or_path": "unsloth/deepseek-r1-distill-llama-8b-unsloth-bnb-4bit"`. The card lists max_steps 60, learning_rate 1e-4, per_device_train_batch_size 2, gradient_accumulation_steps 4, and fp16. It does not state an epoch count. The repository contains both adapter_model.safetensors and four full BF16 weight shards (8,030,261,248 parameters), so the adapter is merged into a full checkpoint that is also uploaded.

The card says the parent is unsloth/DeepSeek-R1-Distill-Llama-8B. config.json and adapter_config.json both name unsloth/deepseek-r1-distill-llama-8b-unsloth-bnb-4bit. Those ids do not match. The inventory parent matches the card, not the weight config.

The card calls it a "Medical reasoning llm" and tells it: "You are a medical expert with advanced knowledge in clinical reasoning, diagnostics, and treatment planning. Please answer the following medical question." That is a strong medical-use claim: diagnostics and treatment planning, plus an example that asks how an appendicitis case should be handled. There is no warning about diagnosis, treatment, or clinical use. The card does not name a patient, a clinician, a student, or a researcher as the user. The appendicitis vignette is not unmistakably one of those groups.

The same instruction is the claimed work: answer a medical question, do clinical reasoning, cover diagnostics, and cover treatment planning. The training template asks for "a step-by-step chain of thoughts" and then a response inside think tags, so the written output is reasoning followed by an answer. The example is a text question passed to the tokenizer. No image or audio input is shown.

No evaluation numbers are on the card. License is mit. Context length in config.json is 131072. generation_config.json sets temperature 0.6, top_p 0.95, and do_sample true. The card example sets max_new_tokens to 2048. The tokenizer chat template leaves the system prompt empty.
