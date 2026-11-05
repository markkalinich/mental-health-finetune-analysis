# iwalton3/sycofact

## Sources

- https://huggingface.co/iwalton3/sycofact/raw/main/README.md — current model card
- revision_3_experiments/hf_inventory/cache/readmes/iwalton3__sycofact__2026-10-09.md — cached card, sha256 cb6d221b8be8251f9fe6fff23ca814781aa7e3badc50ec52fd462c6950145128
- https://huggingface.co/api/models/iwalton3/sycofact — file list, parameter count, chat template
- https://huggingface.co/iwalton3/sycofact/raw/main/config.json — architecture and context length
- https://huggingface.co/iwalton3/sycofact/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/iwalton3/sycofact/raw/main/training_config.json — saved training settings
- https://huggingface.co/iwalton3/sycofact/raw/main/USAGE.md — system prompt and text examples
- https://huggingface.co/datasets/iwalton3/sycofact-training-data/raw/main/README.md — training data card
- https://huggingface.co/api/datasets/iwalton3/sycofact-training-data — public files, including the training script
- https://huggingface.co/datasets/iwalton3/sycofact-training-data/raw/main/code/train_full_finetune.py — TRL SFTTrainer script
- https://arxiv.org/abs/2509.10970 — Psychosis-Bench abstract
- https://arxiv.org/html/2509.10970 — Psychosis-Bench HTML; does not name this repository
- https://ollama.com/izzie/sycofact — Ollama copy
- https://huggingface.co/datasets/truthfulqa/truthful_qa — TruthfulQA, 817 English questions
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — BeaverTails
- https://huggingface.co/datasets/LibrAI/do-not-answer — Do-Not-Answer, 939 prompts
- https://github.com/JiseungHong/SYCON-Bench — SYCON-Bench code and data; no Hub dataset id
- https://huggingface.co/datasets/lmsys/chatbot_arena_conversations — Chatbot Arena, gated, 33,000 conversations
- https://huggingface.co/datasets/Anthropic/model-written-evals — Anthropic sycophancy files

No GitHub repository for this checkpoint turned up.

## Record

The published training set is `iwalton3/sycofact-training-data`. It loads. `sycofact_train.jsonl` has 37,898 evaluator rows and `phoenix_train.jsonl` has 5,970 therapeutic rows. The dataset card says: "No human labels. Every record was scored by a steered Gemma 3 27B." The Phoenix rows "were synthetically generated." The card also names TruthfulQA (`truthfulqa/truthful_qa`, 817, loads), BeaverTails (`PKU-Alignment/BeaverTails`, loads), Do-Not-Answer (`LibrAI/do-not-answer`, 939, loads), SYCON-Bench (GitHub only), Chatbot Arena (`lmsys/chatbot_arena_conversations`, 33,000, gated), and Anthropic sycophancy data (`Anthropic/model-written-evals`, loads). How many rows from each source entered training is not stated.

The objective is supervised fine-tuning of every parameter. `train_full_finetune.py` imports `SFTTrainer` and the dataset card says "Full finetune (all parameters)." The saved `training_config.json` matches that script: learning rate 5e-6, 3 epochs, batch size 1, gradient accumulation 8, sequence length 2048, bf16, mode `full_finetune`. The script's combined count is 43,271 train rows, which is 37,898 plus 90% of the Phoenix file. There is no LoRA rank. The step count is not stated. The base was not quantized.

The parent is `google/gemma-3-4b-it`. The card says the model is "finetuned from Gemma 3 4B IT," and `training_config.json` stores that id. The stated size is 4B. The weight file has 4,300,079,472 BF16 parameters. `config.json` is `Gemma3ForConditionalGeneration`.

This is a classifier of other models' answers. The card says: "SycoFact is a safety/alignment classifier, not a general quality evaluator." The use claim is Weak. The card's purpose sentence is "designed to detect sycophancy and dangerous AI outputs," and the YAML tags include `mental-health` and `crisis-detection`. It does not present itself as a therapist. The warning is Unrelated limitations only: "Not a preference ranker." The liability paragraph is a warranty disclaimer, not a ban on therapy use. Language is "English only." License is `gemma`.

The published example scores a text scenario and a text reply. `config.json` also has a vision tower, and the chat template can insert an image token. A chat template is present. The system prompt in `USAGE.md` begins "You evaluate AI responses for alignment quality." `generation_config.json` sets `do_sample` true, top_k 64, and top_p 0.95. `USAGE.md` sets temperature 0.1 and `max_new_tokens` 256. `max_position_embeddings` is 131072. Psychosis-Bench detection is 192/192, the AISI composite correlation is r=-0.810, and PKU-SafeRLHF F1 is 0.872. The linked Psychosis-Bench paper does not name this repository.

Inventory dataset and parent match. Inventory methods are empty. The script is full-parameter SFT. Match: partly.
