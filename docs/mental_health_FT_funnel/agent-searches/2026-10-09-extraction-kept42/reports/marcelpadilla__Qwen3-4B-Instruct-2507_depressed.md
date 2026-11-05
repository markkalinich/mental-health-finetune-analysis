# marcelpadilla/Qwen3-4B-Instruct-2507_depressed

## Sources

- https://huggingface.co/marcelpadilla/Qwen3-4B-Instruct-2507_depressed/raw/main/README.md — current model card; same text as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/marcelpadilla__Qwen3-4B-Instruct-2507_depressed__2026-10-05.md — cached card, sha256 fd9ff7f2727f2156665b05bfa0dd91446fc1d0d536120801a992a544bac6b5fe
- https://huggingface.co/api/models/marcelpadilla/Qwen3-4B-Instruct-2507_depressed — file list and safetensors count
- https://huggingface.co/marcelpadilla/Qwen3-4B-Instruct-2507_depressed/raw/main/config.json — architecture and max position embeddings
- https://huggingface.co/marcelpadilla/Qwen3-4B-Instruct-2507_depressed/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/marcelpadilla/Qwen3-4B-Instruct-2507_depressed/raw/main/tokenizer_config.json — tokenizer; no chat_template key; model_max_length 1010000
- https://huggingface.co/marcelpadilla/Qwen3-4B-Instruct-2507_depressed/blob/main/chat_template.jinja — chat template
- https://huggingface.co/marcelpadilla/Qwen3-4B-Instruct-2507_depressed/raw/main/depresso.json — training log for this checkpoint
- https://huggingface.co/marcelpadilla/Qwen3-4B-Instruct-2507_depressed/raw/main/dataset.jsonl — 536 training rows shipped with the model
- https://github.com/marcelpadilla/depresso — tool README; names this repository
- https://github.com/marcelpadilla/depresso/blob/main/src/depresso/train.py — LoRA training and merge
- https://github.com/marcelpadilla/depresso/blob/main/src/depresso/llm.py — bfloat16 load, no quantized base
- https://marcelpadilla.com/depresso/ — project page
- https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/raw/main/README.md — parent card, text quickstart, stated size 4.0B

## Record

The training file is `dataset.jsonl` in this repository: 536 rows. `depresso.json` says it is a "bundled dataset (written and graded by Qwen3-4B-Instruct-2507)", 500 depressed answers and 36 refusals. That is synthetic text from the base model. The same file is bundled in the GitHub package. It is not a Hub dataset, so it does not load as one. No source states a language. The rows that were read are English prompts and answers. No paper was found.

The training is supervised next-token training. `train.py` says: "The prompt is masked out of the loss: the model learns to answer in the mood, without any instruction, because none will be there at chat time." The trainer is a Hugging Face `Trainer` with `task_type="CAUSAL_LM"`. The update is LoRA, not a full fine-tune and not a quantized base. `llm.py` loads the model with `AutoModelForCausalLM.from_pretrained` in bfloat16 on CUDA. `Config` sets rank 16, alpha 32, learning rate 0.0002, 3 epochs, per-device batch 4, and gradient accumulation 4. `depresso.json` records 102 steps and final loss 0.718, which matches 536 rows at an effective batch of 16 for 3 epochs. The adapter is merged: `merge_and_save` calls `merge_and_unload`, and the log has a stage named "Merging and saving". Before that merge, the script multiplies the LoRA scale by strength 1.25. The repository has full safetensors shards and no `adapter_config.json`.

The parent is Qwen/Qwen3-4B-Instruct-2507. The card, `depresso.json`, and the README command `depresso Qwen/Qwen3-4B-Instruct-2507` agree. The parent card says "Number of Parameters: 4.0B." The Hub file list reports 4,022,468,096 parameters. The inventory methods cell is blank. The dataset file name and the parent match that row.

This is a chatbot whose answers are written in a sad tone. The GitHub README says: "The model still answers the request, just in a sad way." The card says the base model is here "with depression in its weights" and "Only the emotional tone changed." That is a weak mental-health claim: a tone demo, not a support conversation. No sentence forbids therapy, counseling, or medical advice, and no sentence says the model is not a substitute for a professional. `depresso.json` reports a 12-prompt test with mean mood 2.36. License is Apache-2.0.

Serving is text in, text out. The parent quickstart sets `prompt = "Give me a short introduction to large language model."` and calls `model.generate`. This card does not. A chat template is in `chat_template.jinja`. No system prompt is stored in the checkpoint. The package does define a helper system string for writing the training answers; training then uses a user message only. `generation_config.json` sets `do_sample` true, temperature 0.7, top_k 20, top_p 0.8. `config.json` sets `max_position_embeddings` to 262144.
