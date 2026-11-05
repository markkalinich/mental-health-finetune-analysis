# sujalrajpoot/TrueSyncAI-Aurion

## Sources

- https://huggingface.co/sujalrajpoot/TrueSyncAI-Aurion/raw/main/README.md — current model card; byte-identical to the cached card (`sha256 33450047f546b9ac7fa87df85125742f705f19edb937b67694d221eddc4fbba7`)
- revision_3_experiments/hf_inventory/cache/readmes/sujalrajpoot__TrueSyncAI-Aurion__2026-10-09.md — cached card
- https://huggingface.co/api/models/sujalrajpoot/TrueSyncAI-Aurion — file list, safetensors count (3,085,938,688, BF16), and chat template
- https://huggingface.co/sujalrajpoot/TrueSyncAI-Aurion/raw/main/config.json — Qwen2 config, context length 32768, `unsloth_version` 2026.5.2
- https://huggingface.co/sujalrajpoot/TrueSyncAI-Aurion/raw/main/Modelfile — Ollama template; system line is the Qwen default; temperature 1.5
- https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion — dataset page; no dataset card; viewer reports 1,258,251 rows
- https://datasets-server.huggingface.co/is-valid?dataset=sujalrajpoot/TrueSyncAI-Aurion — viewer enabled
- https://datasets-server.huggingface.co/size?dataset=sujalrajpoot/TrueSyncAI-Aurion — 1,258,251 train rows
- https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion/resolve/main/Couples-Conversation.json — first rows of one JSON file
- https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion/resolve/main/EmotionalIntelligence-155K.json — first rows
- https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion/resolve/main/Higlish-Conversations.json — first rows
- https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion/resolve/main/Human-Conversations.json — first rows
- https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion/resolve/main/Human-Feedback-Conversations.json — first rows
- https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion/resolve/main/Supperficial-Romantic-Conversation.json — first rows
- https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion/resolve/main/TER.json — first rows
- https://github.com/sujalrajpoot — author profile; 18 public repositories, none named TrueSyncAI-Aurion
- https://api.github.com/users/sujalrajpoot/repos?per_page=100 — repository name list
- https://github.com/unslothai/unsloth — library linked from the card for the "2x faster" sentence
- https://truesync-ai.lovable.app — project page linked from the card; returned 404
- https://huggingface.co/spaces/sujalrajpoot/TrueSyncAI-Aurion — Space; default Gradio template, no application file
- https://huggingface.co/datasets/OEvortex/EmotionalIntelligence-75k — nearest public name to the file `EmotionalIntelligence-155K.json`; not the file in this dataset

## Record

The card says the model was trained on `sujalrajpoot/TrueSyncAI-Aurion`. That dataset loads. It has no dataset card. The datasets server counts 1,258,251 train rows in seven JSON files: `Couples-Conversation.json`, `EmotionalIntelligence-155K.json`, `Higlish-Conversations.json`, `Human-Conversations.json`, `Human-Feedback-Conversations.json`, `Supperficial-Romantic-Conversation.json`, and `TER.json`. Each row has `instruction`, `input`, and `output`. The card says the dataset includes "Emotionally nuanced conversations" and "Multilingual interactions." No dataset card states a language code or whether the lines were written by people or by a model. The opened rows include English and Hindi/Hinglish text.

The card says "Training Framework: Unsloth + LoRA." That is LoRA. It does not name a loss. "Fine-tuned" is the only other training word, and the "2x faster training" sentence is Unsloth's library line. `config.json` has `unsloth_version` `2026.5.2`. LoRA rank, LoRA alpha, epochs, steps, learning rate, and batch size are not stated. The repository has full safetensors shards and no `adapter_config.json`, so whether an adapter was merged is not stated. The card does not say the base was quantized during training.

The card's base model is `Qwen/Qwen2.5-3B-Instruct`. No paper names this checkpoint. The card says "Parameters: 3 Billion." The Hub safetensors count is 3,085,938,688.

The card says Aurion is for "empathetic communication" and gives this system line: "You are TrueSyncAI-Aurion, an empathetic AI assistant specialized in emotional support." The use-case list includes "Therapy assistance tools." Output type is Chatbot. Use claim is Strong. The card also says "Do not use for medical diagnosis or professional therapy," which is an explicit prohibition. License is Apache 2.0. The card reports figures such as "Sentiment Analysis: 92.3% accuracy" and "Empathetic Response Generation: 4.6/5.0 human rating" and does not name a test set or a paper.

The card's usage example is text: "Explain the concept of emotional intelligence and why it matters in AI." `config.json` sets `max_position_embeddings` to 32768. The card also says "Up to 128K tokens supported," and `rope_scaling` is null. The card's sampling example sets `max_new_tokens` 512, `temperature` 0.7, `top_p` 0.9, `top_k` 50, `repetition_penalty` 1.1, and `do_sample` true. The Modelfile instead sets `temperature` 1.5 and the system line "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." A chat template is present and uses that same Qwen sentence when no system message is passed.
