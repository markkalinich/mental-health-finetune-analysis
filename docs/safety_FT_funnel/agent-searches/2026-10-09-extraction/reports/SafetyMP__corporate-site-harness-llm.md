# SafetyMP/corporate-site-harness-llm

## Sources

https://huggingface.co/SafetyMP/corporate-site-harness-llm/raw/main/README.md — model card (same text as the cached card)
https://huggingface.co/api/models/SafetyMP/corporate-site-harness-llm — repository file list
https://huggingface.co/SafetyMP/corporate-site-harness-llm/resolve/main/config.json — model config
https://huggingface.co/SafetyMP/corporate-site-harness-llm/resolve/main/generation_config.json — sampling defaults
https://huggingface.co/SafetyMP/corporate-site-harness-llm/resolve/main/tokenizer_config.json — tokenizer settings; no chat template key
https://huggingface.co/SafetyMP/corporate-site-harness-llm/resolve/main/chat_template.jinja — chat template
https://huggingface.co/SafetyMP/corporate-site-harness-llm/resolve/main/export_metadata.json — training snapshot stored in the repo
https://huggingface.co/datasets/SafetyMP/corporate-site-harness-training-data/raw/main/README.md — training dataset card
https://huggingface.co/datasets/SafetyMP/corporate-site-harness-training-data/raw/main/export_meta.json — row counts
https://github.com/SafetyMP/corporate-site-harness — factory repository
https://github.com/SafetyMP/corporate-site-harness/blob/main/datasets/harness-llm/recipes/train_qlora_qwen25_7b.py — QLoRA SFT script on main
https://github.com/SafetyMP/corporate-site-harness/blob/cursor/readme-visual-storefront/datasets/harness-llm/recipes/train_qlora_qwen25_7b.py — script URL printed on the card; that branch returns 404

## Record

The model card says this checkpoint was trained on SafetyMP/corporate-site-harness-training-data, revision `v0.3-lora-standard`. The dataset card counts 3,000 train rows and 450 validation rows of English chat. It calls the rows "Synthetic, expert-authored templates." The Hub dataset is public and the card shows a `load_dataset` call. The same dataset has 400 DPO train rows. The model card does not say those preference pairs were used for this checkpoint.

The model card says training was "Unsloth QLoRA" on "SFT chat messages," then the adapters "were merged into the base before publish." It lists LoRA r/alpha 16/16, 3 epochs, and a trainer-log learning rate of 6.67e-5. The script on `main` is an SFT QLoRA recipe (`load_in_4bit=True`, rank 16, alpha 16) whose defaults are 1 epoch, learning rate 2e-4, and batch size 2. That script says maintainers do not run the GPU training in the packaging pass. No source states an optimizer step count for the published run. The repository has full safetensors shards and no `adapter_config.json`.

The card names the parent `unsloth/Qwen2.5-7B-Instruct`. The training script's default is `Qwen/Qwen2.5-7B-Instruct`. The title calls the model a Qwen2.5-7B. No paper names this repository.

The card presents a "Fine-tuned assistant" for harness policy, CLI text, and refusals. That is a chatbot. It does not claim therapy or mental-health support. The limitations say the model "can still comply with unsafe asks" and "Treat outputs as advisory only." Those sentences are about harness shortcuts, not therapy or medical advice. By-domain scores "are not yet published." License is Apache 2.0.

The usage example is a text system message and a text user message, with no image or audio. The chat template is in `chat_template.jinja`. `generation_config.json` sets temperature 0.3, top_p 0.9, top_k 20, repetition_penalty 1.05, and `do_sample` true. `max_position_embeddings` is 32768. The example uses `max_new_tokens` 256.
