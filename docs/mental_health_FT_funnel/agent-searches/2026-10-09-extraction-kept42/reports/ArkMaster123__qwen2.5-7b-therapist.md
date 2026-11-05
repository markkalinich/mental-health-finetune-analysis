# ArkMaster123/qwen2.5-7b-therapist

## Sources

- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist/raw/main/README.md — current model card; same text as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/ArkMaster123__qwen2.5-7b-therapist__2026-10-05.md — cached card, sha256 3f3bc857cb34ac458575593f61871c6459dbb43dda20a4cebb67130f92dbe91b
- https://huggingface.co/api/models/ArkMaster123/qwen2.5-7b-therapist — file list and parameter count
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist/raw/main/config.json — architecture and context length
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist/raw/main/generation_config.json — sampling settings
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist/raw/main/chat_template.jinja — chat template and default system line
- https://huggingface.co/datasets/Jyz1331/therapist_conversations — dataset page; no README
- https://datasets-server.huggingface.co/size?dataset=Jyz1331/therapist_conversations — 250 rows, viewer loads
- https://datasets-server.huggingface.co/is-valid?dataset=Jyz1331/therapist_conversations — viewer, search, and filter enabled
- https://arxiv.org/abs/2412.15115 — Qwen2.5 Technical Report abstract; does not name this repository

## Record

The card names two training sources: `Jyz1331/therapist_conversations` and "Safety-focused examples." The Hub dataset loads and has 250 rows of `question` and `response`. It has no README, so language and whether the text is human or synthetic are not stated. "Safety-focused examples" has no dataset id. Quote: "Training Dataset: Jyz1331/therapist_conversations + Safety-focused examples."

The card says the update was LoRA, rank 16, on H100 GPUs. It does not name a loss. "Fine-tuned" is not a loss. Initial learning rate is 2e-4, and the safety pass is 1e-4. Batch size is "8 (per device) × 2 (gradient accumulation)." Epochs, steps, LoRA alpha, quantization during training, and whether the adapter was merged are not stated. The repository has four safetensors shards and no `adapter_config.json`. Quote: "Fine-tuning Method: LoRA (Low-Rank Adaptation)."

The card names the parent `Qwen/Qwen2.5-7B-Instruct`. No paper or GitHub repository names this checkpoint. The Qwen2.5 Technical Report is about the base model series and does not print this repository id. The Hub file list reports 7,615,616,512 parameters.

The model is a chatbot for therapeutic conversations, so the use claim is Strong. The warning is Disclaimer only: it says the model should not replace professional services, and it does not forbid therapy. Quote: "specifically trained for therapeutic conversations." Warning quote: "should not be used as a replacement for professional mental health services." The card reports "3/4 safety tests passing (crisis handling, medical advice, harmful reinforcement)." License is apache-2.0.

The usage example sends one text user turn, "I'm feeling anxious about work," and sets `max_new_tokens=512`. `generation_config.json` sets `do_sample` true, temperature 0.7, top_p 0.8, top_k 20, and repetition_penalty 1.05. `config.json` sets `max_position_embeddings` to 32768. The chat template's default system line is "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
