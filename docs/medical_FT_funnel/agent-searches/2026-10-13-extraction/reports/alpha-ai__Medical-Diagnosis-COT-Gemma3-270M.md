# alpha-ai/Medical-Diagnosis-COT-Gemma3-270M

## Sources

- https://huggingface.co/alpha-ai/Medical-Diagnosis-COT-Gemma3-270M/raw/main/README.md — current model card; identical to the cached card
- https://huggingface.co/api/models/alpha-ai/Medical-Diagnosis-COT-Gemma3-270M — file list and parameter count
- https://huggingface.co/alpha-ai/Medical-Diagnosis-COT-Gemma3-270M/raw/main/config.json — architecture and context length
- https://huggingface.co/alpha-ai/Medical-Diagnosis-COT-Gemma3-270M/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/alpha-ai/Medical-Diagnosis-COT-Gemma3-270M/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/alpha-ai/Medical-Diagnosis-COT-Gemma3-270M/raw/main/chat_template.jinja — Gemma chat template
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — dataset card, 90,120 rows, viewer loads
- https://arxiv.org/abs/2412.18925 — HuatuoGPT-o1 abstract; citation for the dataset
- https://arxiv.org/html/2412.18925 — HTML full text; does not print this repo id
- https://github.com/FreedomIntelligence/HuatuoGPT-o1 — dataset authors' code; does not name this checkpoint

## Record

The card trains on `FreedomIntelligence/medical-o1-reasoning-SFT` and on a second set it only describes in words. It says: "Data: `FreedomIntelligence/medical-o1-reasoning-SFT` (`en` split; columns: `Question`, `Complex_CoT`, `Response`)." The English split is about 19.7k rows. The dataset card lists 90,120 rows, languages English and Chinese, and says the set "is constructed using GPT-4o." The Hub viewer loads it. The card also says "Human annotated and filtered medical diagnosis data" of "~ 10k rows with similar fields." A search did not find a Hub id for that second set.

Training is supervised fine-tuning with LoRA. The card says "Trainer: TRL `SFTTrainer` (supervised finetuning)" and "Training: SFT with LoRA via Unsloth." The demo run it reports used `max_steps=500`, learning rate `5e-5`, and `per_device_train_batch_size=8`. It does not state epochs, LoRA rank, or LoRA alpha. There is no `adapter_config.json`. The repo ships `model.safetensors`, and the card's first code block is titled "Transformers (merged weights)," so the adapter was merged. The optimizer is `adamw_8bit`. That is the optimizer, not a statement that the base weights were quantized. The card calls the 500-step numbers a demo run that reached loss about 3.3, and says loss later fell to about 2.3 "with parameter tuning," without giving that run's step count.

The parent on the card is `google/gemma-3-270m-it`: "Base: `google/gemma-3-270m-it` (Gemma 3, 270M params)." The HuatuoGPT-o1 paper and its GitHub repo do not print this repository id, so nothing outside the card confirms the parent. The card says 270M parameters. The Hub file list reports 268,098,176 parameters in `model.safetensors`.

The use claim is strong. The training prompt says "You are a medical expert with advanced knowledge in clinical reasoning, diagnostics, and treatment planning." The warning is an explicit prohibition: "Do not use it for diagnosis or treatment decisions." The YAML license is `apache-2.0`. The same card says "This fine-tune: Derivative work under the base model's license terms."

The card states a purpose: "fine-tuned Gemma-3 270M for medical question answering with explicit chain-of-thought (CoT)." The named audience is research: "Research on medical reasoning, CoT interpretability, prompt engineering, dataset curation." It also mentions internal assistants and end-users, without naming patients, clinicians, or students.

The card claims four functions: answering medical questions, clinical reasoning, diagnostics, and treatment planning. The same sentence covers the last three: "clinical reasoning, diagnostics, and treatment planning."

The clinical work is medical question answering, medical diagnosis data, and a worked example that asks "What initial pharmacologic therapy is indicated?" No specialty is named, so the field is general medicine. The card says "No formal clinical benchmarks reported yet."

Serving is text in, text out. The quick start is a written case, not an image. A chat template is present in `chat_template.jinja`. `config.json` sets `max_position_embeddings` to 32768. The card says Gemma 3 supports up to 128K tokens and that the context used in training was shorter. `generation_config.json` sets `do_sample`, `top_k` 64, `top_p` 0.95, and `max_length` 32768. The card's example also sets `temperature` 1.0 and `max_new_tokens` 256.
