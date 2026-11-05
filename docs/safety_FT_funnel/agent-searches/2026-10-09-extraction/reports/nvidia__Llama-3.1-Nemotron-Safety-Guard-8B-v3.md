# nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3

## Sources

https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/README.md — current model card; same bytes as the cache (sha256 0291e3be308ba2fd77be2b1262e6775a15dc7a0b66bebc80bf2e9ba98fc9f8f0)
https://huggingface.co/api/models/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3 — file list and 8,030,261,248 parameters
https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/config.json — LlamaForCausalLM, max position embeddings 131072
https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/generation_config.json — sampling settings
https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/tokenizer_config.json — chat template
https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/lora_adapter/adapter_config.json — LoRA rank 8, alpha 32, parent id
https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/inference_script.py — text classification example
https://arxiv.org/abs/2508.01710 — CultureGuard preprint abstract
https://arxiv.org/html/2508.01710 — CultureGuard HTML full text
https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3/raw/main/README.md — training dataset card
https://datasets-server.huggingface.co/size?dataset=nvidia/Nemotron-Safety-Guard-Dataset-v3 — 514,617 rows, viewer loads
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0/raw/main/README.md — English source set named on the model card
https://datasets-server.huggingface.co/size?dataset=nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — 33,416 rows, viewer loads
https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch — external set named for redacted prompts
https://build.nvidia.com/nvidia/llama-3_1-nemotron-safety-guard-8b-v3 — NIM preview linked from the card
http://nvidia.com/nemotron-responsible-use — responsible-use page linked from the card

## Record

The model is trained on Nemotron-Safety-Guard-Dataset-v3. The card says: "The model is trained using the Nemotron-Safety-Guard-Dataset-v3 dataset which is synthetically curated using the CultureGuard pipeline." That Hub dataset loads. The dataset card says it has 514,617 samples. The viewer reports the same row count, in train, validation, and test. The dataset card lists 12 languages. The paper says the set "comprises 386,661 samples in 9 languages." The card also says the training mix includes "English samples taken from Nemotron Content Safety Dataset V2", which is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0` (33,416 rows, English, loads), plus translations of those samples and "Synthetic samples generated from Mixtral 8x7B and Mixtral 8x22B". The v3 dataset card says "all data was synthetically generated, and human annotators did not curate any new data" and also "Data Collection Method: Hybrid: Human, Synthetic." Label fields include `prompt_label_source` values `"human"` and `"llm_jury"`. Some prompts are redacted and point at the Kaggle Suicide Detection set: "For certain samples redacted from the Suicide Detection dataset, this field will contain the value \"REDACTED\"." That Kaggle set is not a Hub dataset.

The card and the paper do not name a loss. The paper says: "For training, we utilize Llama Cookbook recipes to PEFT tune the model. We employ LoRA tuning, using the Llama-3.1-8B-Instruct model as our base model. The hyperparameters for training include a rank (r) of 8 and an alpha of 32. Training is conducted for 5 epochs with a constant learning rate (LR) of 1e-5, a per-gpu batch size of 4, and distributed across 8 A100 GPUs with PyTorch FSDP enabled." The card says the same rank and alpha, on `q_proj` and `v_proj`. `adapter_config.json` matches: `peft_type` LORA, `r` 8, `lora_alpha` 32. The paper does not say the base was quantized. It does not say the adapter was merged. The repository has four full weight shards and a separate `lora_adapter`. The card says "The resulting LoRA adapter weights are provided separately."

The card YAML and the prose name `meta-llama/Llama-3.1-8B-Instruct`. The paper and `adapter_config.json` name the same parent. The card says "Number of model parameters: 8.03B." The weight index reports 8,030,261,248 parameters.

This is a classifier, not a chatbot. The card says it "classifies user prompts and LLM responses as safe or unsafe" and returns JSON fields "User Safety", "Response Safety", and "Safety Categories". The use claim is weak. Suicide and self-harm is one category in the moderation taxonomy, "S6: Suicide and Self Harm," not a support conversation. The card does not forbid therapy, counseling, or medical advice. Intended use is "This model is intended for developers and researchers building LLMs." No therapy warning is stated. The card's evaluation table is Nemotron-Safety-Guard-Dataset-v3 85.32, PolyGuardPrompts 76.07, RTP-LX 91.49, MultiJail 95.36, XSafety 66.97, Aya Red-teaming 96.79. License text: "Your use of this model is governed by the NVIDIA Open Model License. Additional Information: Llama 3.1 Community License Agreement."

The card says "**Input Type(s)**: Text" and the example is a text prompt. `tokenizer_config.json` has a chat template. `generation_config.json` sets `do_sample` true, `temperature` 0.6, and `top_p` 0.9. The example uses `max_new_tokens=100`. `config.json` sets `max_position_embeddings` to 131072. The card also says "Context length up to 8K." The safety policy is the user message. The card does not set a system prompt. The paper names this checkpoint Llama-3.1-Nemotron-Safety-Guard-8B-v3. It does not print `nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3`. The dataset card does print that repository id.
