# Jjateen/llama-2-7b-mental-chat

## Sources

https://huggingface.co/Jjateen/llama-2-7b-mental-chat/raw/main/README.md — current model card; byte-identical to the cached card
revision_3_experiments/hf_inventory/cache/readmes/Jjateen__llama-2-7b-mental-chat__2026-10-09.md — cached card, sha256 e163d22ade742e40dcbc2047b85ae09a1d49eb3c7009ee6d448804ba378cebac
https://huggingface.co/api/models/Jjateen/llama-2-7b-mental-chat — file list
https://huggingface.co/Jjateen/llama-2-7b-mental-chat/raw/main/config.json — parent path and context length
https://huggingface.co/Jjateen/llama-2-7b-mental-chat/raw/main/generation_config.json — sampling settings
https://huggingface.co/Jjateen/llama-2-7b-mental-chat/raw/main/tokenizer_config.json — no chat template key
https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset — training dataset card
https://huggingface.co/api/datasets/heliosbrahma/mental_health_chatbot_dataset — 172 train rows

## Record

The training set is `heliosbrahma/mental_health_chatbot_dataset`. It loads, with 172 English rows. The dataset card says it "contains conversational pair of questions and answers" curated from WebMD, Mayo Clinic, HealthLine, and online FAQs, and that "Questions were asked by the patients and answers were given by healthcare providers." That is human text, not a generated corpus. The model card names this dataset and says preprocessing was "Text normalization, tokenization, and filtering for quality."

The card says the model was "Fine-tuned with a causal language modeling objective." That sentence does not name supervised fine-tuning, DPO, or another loss on the study list. It does not say whether the update was full or LoRA. It does state 3 epochs, batch size 8, AdamW, and learning rate 5e-6. The card says "Paper: Not available." Searches did not find a paper or a GitHub training repository.

The YAML and `config.json` name `NousResearch/llama-2-7b-chat-hf`. The same card's "Fine-tuned from" line links to `meta-llama/Llama-2-7b-hf`. Those two parents are not the same repository. The card calls the model "Meta's LLaMA 2 7B" and says the files are 10.5 GB across two `.bin` files.

The card presents a mental-health chatbot for "empathetic, non-clinical support," so the use claim is Moderate. The warning is a disclaimer: "Not a substitute for professional mental health care." Out of scope, it also says clinical diagnosis is "Not suitable for medical or therapeutic advice" and crisis use "Should not be used in critical situations requiring professional intervention." The card reports Empathy Score 85/100, Relevance 90%, and Safety 95% on a held-out set, without the scoring method.

The example input is the text "I feel overwhelmed and anxious. What should I do?" There is no system prompt and no chat template. `generation_config.json` sets temperature 0.9 and top_p 0.6. The example uses max_length 200. `config.json` sets max_position_embeddings to 4096. The license is llama2.

Started 2026-10-09T16:52:21-04:00. Ended 2026-10-09T16:53:41-04:00.
