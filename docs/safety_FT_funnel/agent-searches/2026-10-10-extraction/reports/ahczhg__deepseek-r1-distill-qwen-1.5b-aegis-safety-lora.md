# ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora

## Sources

- https://huggingface.co/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora/raw/main/README.md — current model card; byte-identical to the cached card (`sha256 c448cb6f44549c49901ce30ec1864fc947fdd79533dc3d839f704fad50388119`)
- https://huggingface.co/api/models/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora — file list, safetensors count, and chat template text
- https://huggingface.co/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora/raw/main/config.json — Qwen2 config, context 131072
- https://huggingface.co/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora/raw/main/generation_config.json — temperature 0.6, top_p 0.95, do_sample true
- https://huggingface.co/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora/raw/main/tokenizer_config.json — no `chat_template` key; `model_max_length` 16384
- https://huggingface.co/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora/raw/main/chat_template.jinja — DeepSeek chat template
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — training dataset card and viewer rows
- https://arxiv.org/abs/2501.12948 — DeepSeek-R1 abstract; the card cites this title
- https://arxiv.org/html/2501.12948v1 — DeepSeek-R1 HTML; does not print this repository id
- https://arxiv.org/abs/2503.16529 — other DeepSeek safety paper found by search; not read in full
- https://aclanthology.org/2025.naacl-long.306/ — AEGIS2.0 dataset paper, cited on the dataset card; not read in full
- https://github.com/huggingface/peft — PEFT library link on the card, not a training repo for this checkpoint

## Record

The training data is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0`. The dataset card says it has 33,416 annotated interactions (30,007 train, 1,445 validation, 1,964 test). The model card says the run used "1000 samples randomly selected from the full dataset". The dataset page loads in the viewer. Provenance is mixed: "Hybrid: Human annotations with synthetic LLM augmentations". Prompts are human-written; responses come from Mistral-7B-v0.1; response labels are human, an LLM jury, or synthetic refusals. Language is English.

The card does not name a loss from the study list. It says "Task Type: Causal Language Modeling". The update is LoRA on a 4-bit base: "Fine-tuning Method: LoRA" and "Quantization: 4-bit NF4". Rank 16, alpha 32, dropout 0.05. Learning rate 0.0002, 3 epochs, per-device batch 2, gradient accumulation 8, effective batch 16. Step count is not stated. The repository has `model.safetensors` (1,777,088,000 float16 parameters) and no `adapter_config.json`, so the published checkpoint is a full model. The Hub tag still says `base_model:adapter`.

The card names the parent `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`. The DeepSeek-R1 paper describes that distill family and does not print `ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora`. The card states "1.5B parameters" and "Language: English". License MIT.

The card presents a classifier. It says "Content safety classification - Identify safe vs unsafe content" and the example asks the model to "provide a classification (safe/unsafe)" for a piece of text. It also says "Generate responses with safety considerations" and "Provide safety scores for content prioritization". The input in the example is one instruction wrapped around a short text, not a conversation and not a prompt plus an assistant reply. The model card does not name the hazard list. The dataset card lists Hate/Identity Hate, Sexual, Suicide and Self Harm, Violence, Guns/Illegal Weapons, Threat, PII/Privacy, Sexual Minor, Criminal Planning/Confessions, Harassment, Controlled/Regulated substances, and Profanity. Evaluation on the card is perplexity 14.20 on 100 samples, plus "qualitative generation testing".

Serving is text only. The saved generation config uses temperature 0.6, top_p 0.95, and do_sample true. The card's main example uses temperature 0.7, top_p 0.95, do_sample true, and max_new_tokens 128. `config.json` sets `max_position_embeddings` to 131072. Training used a max sequence length of 512. The chat template does not ship a fixed system prompt.
