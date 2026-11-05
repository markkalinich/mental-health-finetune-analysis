# i5-8300h/gemma3-4b-psychology-dpo

## Sources

https://huggingface.co/i5-8300h/gemma3-4b-psychology-dpo/raw/main/README.md — current model card; same bytes as the cached card
revision_3_experiments/hf_inventory/cache/readmes/i5-8300h__gemma3-4b-psychology-dpo__2026-10-09.md — cached card, sha256 f1a431becc9c3d6c25535ecb690935e457475b30c0a30fed060fc7c46f710b01
https://huggingface.co/api/models/i5-8300h/gemma3-4b-psychology-dpo — file list and safetensors parameter total
https://huggingface.co/i5-8300h/gemma3-4b-psychology-dpo/raw/main/config.json — architecture and context length
https://huggingface.co/i5-8300h/gemma3-4b-psychology-dpo/raw/main/generation_config.json — sampling defaults
https://huggingface.co/i5-8300h/gemma3-4b-psychology-dpo/raw/main/tokenizer_config.json — no chat_template key; use_default_system_prompt false
https://huggingface.co/i5-8300h/gemma3-4b-psychology-dpo/raw/main/chat_template.jinja — chat template file
https://huggingface.co/datasets/entfane/psychotherapy-dpo — dataset page
https://huggingface.co/datasets/entfane/psychotherapy-dpo/raw/main/README.md — dataset card; YAML only, no prose
https://datasets-server.huggingface.co/size?dataset=entfane/psychotherapy-dpo — 168 rows
https://datasets-server.huggingface.co/rows?dataset=entfane/psychotherapy-dpo&config=default&split=train&offset=0&length=1 — one example row
https://huggingface.co/i5-8300h/gemma3-4b-psychology-dpo-Q4_K_M-GGUF/raw/main/README.md — GGUF conversion of this repo; points back at this card

## Record

The training set is entfane/psychotherapy-dpo. The card gives only that URL. The dataset card is YAML. It has 168 train rows and four columns: illness, input, chosen, rejected. The Hub viewer loads it. The dataset card does not state a language or whether the text is human, synthetic, or mixed. One loaded row is an English anxiety complaint with a chosen reply and a rejected reply.

The objective is DPO. The card says "DPO and LoRA PeFT finetuned version of Gemma 3 4B for response tone adjustment." The update is QLoRA. The card says "FP16 mixed precision and QLoRA quantized weights (4bits), 3 epochs at 2e-5 lr." It also says "This repo contains merged weights." The repository has model.safetensors and no adapter_config.json, so the LoRA rank and alpha are not stated. Epochs are 3. The card says "~6.5 hours for all 3 epochs (33 steps)." Learning rate is 2e-5. Beta is 0.1. Max prompt length is 128 and max length is 256. Batch size is not stated.

The card's YAML base model is google/gemma-3-4b-it. The prose says "Finetuned from model: Google Gemma 3 4B (Instruction Tuned)." No paper or GitHub page names this repository. The card says the model is Gemma 3 4B. The safetensors header lists 4,300,079,472 F16 parameters. The license on the card is gemma.

The direct use is "Psychologically aligned chatbot tasks." That is a chatbot. The claim is moderate: tone adjustment with a psychology framing, not a statement that the model delivers therapy. The card says it "has not been trained to deliver any form of medical advice" and "Not a substitute for a licensed professional." The recommendation is a prohibition: "Do not use in any safety critical or medically critical applications."

The card says "finetuning has been done on text-text tasks only." The load example uses AutoTokenizer and AutoModelForCausalLM and does not send an image. generation_config.json sets do_sample true, top_k 64, and top_p 0.95. It does not set temperature. text_config.max_position_embeddings is 131072. A chat template is in chat_template.jinja. No system prompt is written on the card, and use_default_system_prompt is false. The card does not report an evaluation score.

Searches for the repo id did not return a paper or a GitHub training repo that prints this id. The DPO method paper (arXiv 2305.18290) and a Gemma-3-27B paper (arXiv 2603.10011) do not name this checkpoint.
