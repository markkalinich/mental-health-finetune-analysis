# ArkMaster123/qwen2.5-7b-therapist-v3

## Sources

- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist-v3/raw/main/README.md — current model card; same text as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/ArkMaster123__qwen2.5-7b-therapist-v3__2026-10-05.md — cached card, sha256 bec115c0ec36ec90d4169fcbd56a02f1fcd18397593742363beda60c44184eda
- https://huggingface.co/api/models/ArkMaster123/qwen2.5-7b-therapist-v3 — file list and parameter count
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist-v3/raw/main/config.json — architecture and context length
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist-v3/raw/main/generation_config.json — sampling settings
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist-v3/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist-v3/raw/main/chat_template.jinja — chat template and default system line
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist-v3-sft-fast/raw/main/adapter_config.json — LoRA rank and alpha for the adapter the card names
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist-v3-sft-fast/raw/main/README.md — automatic Hub stub; no training facts
- https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/raw/main/README.md — parent card; text-only quickstart and 7.61B count
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — dataset card; gated download
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations/viewer/default/train — viewer shows about 3.51k rows
- https://huggingface.co/datasets/nbertagnolli/counsel-chat/raw/main/README.md — counsel-chat dataset card
- https://datasets-server.huggingface.co/size?dataset=nbertagnolli/counsel-chat — 2,775 rows; viewer valid
- https://huggingface.co/datasets/IINOVAII/therapy-conversations-combined/raw/main/README.md — dataset card with language and license only
- https://datasets-server.huggingface.co/size?dataset=IINOVAII/therapy-conversations-combined — 208,548 rows; viewer valid
- https://featherless.ai/models/ArkMaster123/qwen2.5-7b-therapist-v3 — hosted demo that restates the card

## Record

The card says this run was trained on a curated mix of three public datasets: Amod/mental_health_counseling_conversations, nbertagnolli/counsel-chat, and IINOVAII/therapy-conversations-combined. Amod's card says the rows are "real one-on-one mental health counseling conversations between individuals and licensed professionals." The raw README and the row-count API both returned 401, and the dataset is gated, so it does not load without approval. The viewer page shows "3.51k rows," not an exact count. counsel-chat loads: 2,775 rows. Its card says "The dataset was scraped on 20220401 from counselchat.com" and "The text was written by licensed counselors in the United States and annonymous individuals." therapy-conversations-combined loads: 208,548 rows, language en. Its dataset card does not say who wrote the text.

The objective is supervised fine-tuning. The card says "SFT LoRA adapter: `ArkMaster123/qwen2.5-7b-therapist-v3-sft-fast`" and "fine-tuned with LoRA on a curated counseling mixture and merged for direct inference." That adapter's config has `"r": 32` and `"lora_alpha": 64`, and `"base_model_name_or_path": "Qwen/Qwen2.5-7B-Instruct"`. The card says "Fast training profile: 120 steps, packed sequences, bf16, H100 multi-GPU run." Epochs, learning rate, batch size, and whether the base was quantized are not stated. This repository holds four merged safetensors shards and no adapter file.

The card and the adapter config both name the parent Qwen/Qwen2.5-7B-Instruct. The Hub API reports 7,615,616,512 parameters for this repository. The parent card says "Number of Parameters: 7.61B."

The card calls it "A therapist-oriented model" and says the intended use is "Supportive, empathetic conversational assistance for mental wellness contexts." That is a chatbot and a strong therapy-support claim. The safety lines are "Not a substitute for licensed care" and a crisis-hotline sentence. That is a disclaimer, not a ban on use.

The parent quickstart runs the model on a text prompt: `prompt = "Give me a short introduction to large language model."` This repository's chat template defaults to "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." generation_config.json sets temperature 0.7, top_p 0.8, top_k 20, repetition_penalty 1.05, and do_sample true. config.json sets max_position_embeddings to 32768. No evaluation numbers are on the card. The license line is apache-2.0. No paper and no GitHub repository name this checkpoint. Searches returned the Qwen2.5 parent report, which does not print this repository id.
