# ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora

## Sources

https://huggingface.co/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora/raw/main/README.md — current model card; same text as the cached card
https://huggingface.co/api/models/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora — file list, parameter count, and chat template
https://huggingface.co/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora/raw/main/config.json — architecture and context length
https://huggingface.co/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora/raw/main/generation_config.json — sampling defaults
https://huggingface.co/ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — dataset card; viewer shows rows and the dataset is not gated
https://aclanthology.org/2025.naacl-long.306/ — AEGIS2.0 dataset paper cited on the dataset card; it does not name this repository
https://github.com/huggingface/peft — PEFT library link on the model card, not this model's training code

## Record

The checkpoint was trained on 1,000 examples from `nvidia/Aegis-AI-Content-Safety-Dataset-2.0`. The card says "Training Subset: 1000 samples randomly selected from the full dataset" and, earlier, "Training Samples: 1000 carefully selected samples." The dataset card calls the release Nemotron Content Safety Dataset V2 and says it has 33,416 annotated interactions. Collection is "Hybrid: Human annotations with synthetic LLM augmentations": human prompts, Mistral-7B-v0.1 responses, and labels that are human, an LLM jury, or synthetic refusals. The Hub dataset is public and the viewer loads rows. Language on the model card is "Language: English."

The card does not name a loss from the study list. It says "Task Type: Causal Language Modeling" and "The model was fine-tuned using LoRA (Low-Rank Adaptation)." Training used a quantized base: "Quantization: 4-bit NF4," with "Rank (r): 16," "Alpha: 32," "Epochs: 3," "Learning Rate: 0.0002," and "Batch Size (per device): 2" (effective batch size 16 with gradient accumulation 8). No step count is given. The repository stores `model.safetensors` (1,777,088,000 float16 parameters) and has no `adapter_config.json`, so the LoRA was merged into a full checkpoint.

The parent on the card is "Base Model: deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B." No paper or GitHub project names this repository. The card states "Model Size: 1.5B parameters."

The card presents a content-safety classifier, not a conversation partner and not a mental-health tool: "Content safety classification - Identify safe vs unsafe content" and "specialized for content safety and moderation tasks." The limitation is about moderation, not therapy: "Not a Replacement for Human Judgment: Should be used as part of a comprehensive moderation system." Evaluation is perplexity 14.20 on 100 held-out Aegis samples. License is MIT.

The usage example is text only: "Analyze this content for safety: 'Hello! How can I help you today?'" `generation_config.json` sets `do_sample` true, temperature 0.6, and top_p 0.95. The card example uses temperature 0.7 and `max_new_tokens` 128. `config.json` sets `max_position_embeddings` to 131072. The chat template is present and does not set a system prompt.
