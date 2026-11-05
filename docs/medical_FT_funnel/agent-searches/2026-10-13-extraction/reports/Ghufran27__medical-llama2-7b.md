# Ghufran27/medical-llama2-7b

## Sources

- https://huggingface.co/Ghufran27/medical-llama2-7b/raw/main/README.md — current model card; sha256 matches the cached card
- https://huggingface.co/Ghufran27/medical-llama2-7b/raw/main/README.markdown — shorter second card in the same repository
- https://huggingface.co/api/models/Ghufran27/medical-llama2-7b — file list and parameter total
- https://huggingface.co/Ghufran27/medical-llama2-7b/raw/main/config.json — context length and dtype
- https://huggingface.co/Ghufran27/medical-llama2-7b/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/Ghufran27/medical-llama2-7b/raw/main/tokenizer_config.json — no chat template
- https://huggingface.co/datasets/Ghufran27/medical-qa-v3 — dataset named in the card YAML
- https://huggingface.co/spaces/openlifescienceai/open_medical_llm_leaderboard — leaderboard the card says it is for
- https://huggingface.co/datasets/openlifescienceai/requests — evaluation queue that lists this repository
- Cached card: revision_3_experiments/hf_inventory/cache/readmes/Ghufran27__medical-llama2-7b__2026-10-10.md

## Record

The YAML dataset is Ghufran27/medical-qa-v3. That Hub dataset loads. Its README is only a cc-by-4.0 license line, and the file is medical-qa-v3.jsonl. The Hub size bucket is 100K to 1M rows. An exact count is not stated. The prose also names a file, cleaned_medical.jsonl, and says the pairs are "sourced from medical literature and cleaned," on "disease diagnosis, treatment protocols, and medical terminology." The card does not show that the jsonl on the Hub is that same file.

The card does not name a loss such as SFT. It says the model is "instruction-tuned" and "fine-tune[d]" with LoRA. Rank is 8, alpha is 16, dropout is 0.05, and the target modules are q_proj and v_proj. Training used 4-bit NF4 with double quantization, so the update is LoRA on a quantized base. The card says the saved output is a merged safetensors model. The repository has three weight shards and no adapter file. Training was 1 epoch, 500 steps, batch size 16, and learning rate 2e-4, on a Kaggle GPU.

The parent is NousResearch/Llama-2-7b-chat-hf. The card says 7 billion parameters. The safetensors total is 6,738,415,616 in float16. Language is English.

The model is for medical question answering, including patient queries. The example is "What is the treatment for hypertension?" That is a strong medical-use claim: it answers a treatment question and is described as resolving patient queries. The limitations in README.markdown are about refusing non-medical questions, dataset coverage, and compute. They do not forbid diagnosis or treatment.

The purpose is medical question answering for "medical education, clinical research support, and preliminary patient query resolution." Those name students, researchers, and patients. It answers medical questions, including diagnosis and treatment topics, and is offered for study. The output is a chat-style reply in `[INST]` tags. The tasks are medical question answering, treatment questions, and diagnosis topics. No specialty is named.

The example is text. There is no chat template in tokenizer_config.json. The documented system line is "Answer only medical-related questions. If not, reply: 'I'm sorry, I can only answer questions related to the medical field.'" generation_config.json sets do_sample true, temperature 0.9, and top_p 0.6. The example uses max_new_tokens 100. Context length in config.json is 4,096 tokens. The license is llama2. The card names accuracy and the Open Medical-LLM Leaderboard and reports no score. The queue lists this repository as pending. No paper and no GitHub repository name this checkpoint. The inventory dataset and parent match. The inventory says LoRA. The card says that LoRA was trained on a 4-bit base and then merged.
