# graliuce/Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5

## Sources

- https://huggingface.co/graliuce/Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5/raw/main/README.md — current model card; same text as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/graliuce__Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5__2026-10-10.md — cached card
- https://huggingface.co/api/models/graliuce/Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5 — file list, parameter count, chat template
- https://huggingface.co/graliuce/Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5/raw/main/config.json — Qwen2 config; context 32768; parent path
- https://huggingface.co/graliuce/Qwen2.5-3B-Instruct_MedMCQA.20.01_1.0e-5/raw/main/generation_config.json — temperature 0.7, top_p 0.8, top_k 20
- https://huggingface.co/datasets/graliuce/MedMCQA.20.01 — training set; empty README; viewer loads 4,880 rows
- https://github.com/graliuce/CaRT — names this repository as the CaRT termination model
- https://github.com/graliuce/CaRT/blob/main/bash/sft/submit.slurm — builds this hub id, learning rate 1e-5, 3 epochs
- https://github.com/graliuce/CaRT/blob/main/bash/sft/task.sh — SFT launch, batch size 1, no PEFT flag
- https://github.com/graliuce/CaRT/blob/main/finetune/sft.py — TRL SFTTrainer
- https://github.com/huggingface/trl — library linked from the card
- https://github.com/huggingface/open-r1 — environment the CaRT README points to
- https://wandb.ai/grace_rl/infoseek/runs/oxx6zxho — run linked from the card

No paper names this checkpoint.

## Record

The training set is `graliuce/MedMCQA.20.01`, 4,880 English rows. The README of that dataset is empty. A row starts "Hi! What symptoms are you facing today?" and tells the model "You are a Medical Triage Assistant." The target says whether there is enough information to give a diagnosis. The dataset card does not say if the rows are human or synthetic. The id says MedMCQA. The rows are not exam items.

The card says "This model was trained with SFT." The CaRT script `submit.slurm` sets the dataset to `graliuce/MedMCQA.20.01`, the base to `Qwen/Qwen2.5-3B-Instruct`, the learning rate to 1.0e-5, and the hub id to this repository, and it passes 3 epochs. The launch uses batch size 1 per device, gradient accumulation 32, and 8 processes, in bfloat16, with no PEFT flag. The repository holds full weights, not an adapter. Step count is not stated.

The parent is `Qwen/Qwen2.5-3B-Instruct`. The card, `config.json`, and the Slurm script all say that. The weight files contain 3,085,938,688 parameters.

The CaRT README calls this checkpoint the "CaRT termination model" under "Trained Models and Datasets for medical termination." The training rows are a patient describing symptoms. The model is asked to reason and to decide whether a diagnosis can be made. That is a strong use claim. No warning is written. The YAML value `licence: license` is not a license name.

The work is triage, a diagnosis decision, and a conversation. No specialty is named, so the field is general medicine. The README names two evaluation sets and prints no scores.

The card example is a text question and a chat reply. The training targets are reasoning paragraphs. The tokenizer inserts "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." when no system message is passed. Generation defaults are temperature 0.7, top_p 0.8, top_k 20, repetition penalty 1.05, and do_sample. The example uses max_new_tokens 128. Context length is 32768.
