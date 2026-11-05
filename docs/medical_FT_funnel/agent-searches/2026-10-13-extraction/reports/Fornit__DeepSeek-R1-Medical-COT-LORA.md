# Fornit/DeepSeek-R1-Medical-COT-LORA

## Sources

- https://huggingface.co/Fornit/DeepSeek-R1-Medical-COT-LORA/raw/main/README.md — current model card; sha256 matches the cached card
- https://huggingface.co/api/models/Fornit/DeepSeek-R1-Medical-COT-LORA — file list and safetensors parameter total
- https://huggingface.co/Fornit/DeepSeek-R1-Medical-COT-LORA/raw/main/adapter_config.json — LoRA rank, alpha, and base path
- https://huggingface.co/Fornit/DeepSeek-R1-Medical-COT-LORA/raw/main/config.json — architecture, context length, and `_name_or_path`
- https://huggingface.co/Fornit/DeepSeek-R1-Medical-COT-LORA/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/Fornit/DeepSeek-R1-Medical-COT-LORA/raw/main/tokenizer_config.json — chat template
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — dataset named in the card
- https://arxiv.org/abs/2504.00016 — search hit about DeepSeek R1, not this repository
- https://arxiv.org/abs/2501.12948 — DeepSeek-R1 paper, not this repository
- Cached card: revision_3_experiments/hf_inventory/cache/readmes/Fornit__DeepSeek-R1-Medical-COT-LORA__2026-10-10.md

## Record

The card says the model "was trained on the first 500 rows" of FreedomIntelligence/medical-o1-reasoning-SFT. That dataset card says the text "is constructed using GPT-4o". It lists English and Chinese configs. This card does not say which config the 500 rows came from. The dataset has files and loads. Its README, as read here, does not give a row count.

The card's YAML tag list includes `sft`. No sentence names the loss. adapter_config.json says `"peft_type": "LORA"`, rank 16, alpha 16, and `"base_model_name_or_path": "unsloth/deepseek-r1-distill-llama-8b-unsloth-bnb-4bit"`. That is LoRA on a 4-bit base. The adapter file is still in the repository, so it is not merged. Epochs, steps, learning rate, and batch size are not stated. The run "Duration: 11m 38s" on one NVIDIA A40.

The card's parent line is unsloth/DeepSeek-R1-Distill-Llama-8B. adapter_config.json and config.json `_name_or_path` both name the 4-bit Unsloth checkpoint instead. Those do not agree with the card. The Hub safetensors total is 8,030,261,248 parameters, which counts the four full weight shards also uploaded, not the LoRA matrices.

The card does not say what the model is for, who it is for, or what it should write. The medical use claim is weak: the only medical statement is the dataset id in the YAML. There is no warning. No audience, function, clinical task, or specialty is stated. There is no usage example, so the output type is not listed.

The architecture is LlamaForCausalLM, a text model. A chat template is present and it has no default system prompt. generation_config.json sets do_sample true, temperature 0.6, and top_p 0.95. Context length is 131,072 tokens. The license is apache-2.0. No evaluation numbers are reported. No paper and no GitHub repository name this checkpoint. The inventory dataset matches. The inventory parent matches the card and not the adapter file. The inventory method `lora` is the adapter type; the base path is the 4-bit model.
