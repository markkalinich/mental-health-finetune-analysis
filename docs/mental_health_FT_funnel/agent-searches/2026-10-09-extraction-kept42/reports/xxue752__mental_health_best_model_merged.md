# xxue752/mental_health_best_model_merged

## Sources

- https://huggingface.co/xxue752/mental_health_best_model_merged/raw/main/README.md — current model card (same text as the 5 Oct cache)
- revision_3_experiments/hf_inventory/cache/readmes/xxue752__mental_health_best_model_merged__2026-10-05.md — cached card, sha256 1300eb60b46c3758dd067b8bf668ee39ef6d6f886b7c388a1876f049713b0d49
- https://huggingface.co/api/models/xxue752/mental_health_best_model_merged — file list, chat template, 7,941,100,832 parameters
- https://huggingface.co/xxue752/mental_health_best_model_merged/raw/main/config.json — Gemma 4 config, text context 131072, plus vision and audio blocks
- https://huggingface.co/xxue752/mental_health_best_model_merged/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/xxue752/mental_health_best_model/raw/main/README.md — LoRA adapter this repo says it merged
- https://huggingface.co/xxue752/mental_health_best_model/raw/main/adapter_config.json — LoRA r=16, alpha=32, base google/gemma-4-E4B-it
- https://huggingface.co/xxue752/mental_health_best_model/raw/main/task_sampling_stats.csv — 41 task names and row counts
- https://huggingface.co/datasets/google-research-datasets/go_emotions — GoEmotions; viewer shows rows
- https://huggingface.co/datasets/ConvLab/dailydialog — DailyDialog card; viewer did not show rows
- https://huggingface.co/datasets/cardiffnlp/tweet_eval — TweetEval; sentiment viewer shows rows
- https://huggingface.co/datasets/AIMH/SWMH — SWMH; gated
- https://huggingface.co/datasets/irlab-udc/redsm5 — ReDSM5; gated
- https://github.com/drmuskangarg/MultiWD — MultiWD code and description; no Hub dataset id found
- https://github.com/huggingface/trl — TRL library cited on the card, not this model's training script
- https://huggingface.co/xxue752/mental_health_best_model_litert — sibling export that names this repo as the merged bf16 stage

## Record

The card says the model was fine-tuned on "41 mental-health and emotion text-classification tasks (D01–D22 plus GoEmotions one-vs-rest splits)." The task table is on the LoRA repo, `task_sampling_stats.csv`. That file names GoEmotions, DailyDialog, TweetEval, MultiWD, SWMH, and ReDSM5, plus stress, depression, suicide, empathy, and feeling labels. GoEmotions is `google-research-datasets/go_emotions`. Its card says "58k carefully curated Reddit comments" and "Annotations were produced by 3 English-speaking crowdworkers." The viewer shows rows, so it loads. DailyDialog's task row has 102,979 examples, which matches the utterance total on `ConvLab/dailydialog`. That card says the language "is human-written" and "We also manually label" emotion. Its viewer did not show rows, and the card says to load it through ConvLab-3, so loads is false. TweetEval sentiment in the CSV is 45,615 rows, the same as the sentiment train split of `cardiffnlp/tweet_eval`, and that viewer shows rows. SWMH in the CSV is 34,823 rows. `AIMH/SWMH` says it has 54,412 Reddit posts and is gated, so it does not load without accepting terms. ReDSM5 in the CSV is 3 rows. `irlab-udc/redsm5` says 1,484 posts and is gated. No Hub dataset id for MultiWD was found. The CSV lists 657 rows for each MultiWD binary task. The author does not print which Hub id was loaded. `task_core.py` is not in either repo.

The objective is supervised fine-tuning. The card says "Loss: TRL SFT, completion-only loss (only the answer token is supervised)." The update is LoRA, then merged. The card says "LoRA r=16, α=32, dropout=0.05, bf16" and "then merge_and_unload." It also says "Full-precision (bf16) weights," so the base was not quantized during training. Epochs are 1. Learning rate is 2e-4. Effective batch size is 16. No step count is stated. This repo has four safetensors shards and no adapter file. The adapter config on the sibling repo has `"base_model_name_or_path": "google/gemma-4-E4B-it"` and `"r": 16`, `"lora_alpha": 32`.

The parent on the card is `google/gemma-4-E4B-it`. The adapter config names the same parent. The card states "~16 GB bf16." The file list reports 7,941,100,832 parameters. License is `gemma`. Language YAML is `en`.

This is a classifier. The example system line is "You are a careful classifier" and it must "reply with EXACTLY one single integer class id." The use claim is weak. The task is mental-health text classification, not a support conversation. The warning is an explicit prohibition. The card says the outputs "are not clinical advice and must not be used to diagnose or triage real users." Inventory methods `lora|sft` and the parent match. The six inventory dataset names appear in the task table, and that table also has tasks the inventory string does not name. Held-out means are ACC 0.826, BACC 0.760, F1 0.763, and Macro-AUPRC 0.684.

The published example is text in, text out. It sends one user string and calls `generate` with `max_new_tokens=2` and `do_sample=False`. `config.json` is `Gemma4ForConditionalGeneration` and also has vision and audio blocks. Text `max_position_embeddings` is 131072. A chat template is present in the model API. `generation_config.json` sets `do_sample` true, temperature 1.0, top_k 64, and top_p 0.95. The example system prompt is the classifier sentence above.
