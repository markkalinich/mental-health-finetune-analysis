# graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5

## Sources

- https://huggingface.co/graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5/raw/main/README.md — current model card; same text as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/graliuce__Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5__2026-10-10.md — cached card
- https://huggingface.co/api/models/graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5 — file list, parameter count, chat template
- https://huggingface.co/graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5/raw/main/config.json — Llama config; context 131072
- https://huggingface.co/graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5/raw/main/generation_config.json — temperature 0.6, top_p 0.9
- https://huggingface.co/graliuce/Llama-3.1-8B-Instruct_MedMCQA.20.01_1.0e-5/raw/main/chat_template.jinja — Llama 3.1 chat template
- https://huggingface.co/datasets/graliuce/MedMCQA.20.01 — training set; empty README; viewer loads 4,880 rows
- https://github.com/huggingface/trl — TRL library linked from the card
- https://wandb.ai/grace_rl/infoseek/runs/j51w490x — training run linked from the card; the page did not load

No paper and no training repository name this checkpoint. Searches returned other MedMCQA fine-tunes, not this repository.

## Record

The training set is `graliuce/MedMCQA.20.01`. The card says the model is "a fine-tuned version of meta-llama/Llama-3.1-8B-Instruct on the graliuce/MedMCQA.20.01 dataset." The dataset README is empty. The viewer loads 4,880 English rows. A row is a dialogue that starts "Hi! What symptoms are you facing today?" and tells the model "You are a Medical Triage Assistant. Reason about the conversation to determine if there is sufficient information to provide a diagnosis." The written target is a paragraph that begins "There is insufficient information to provide a diagnosis because" or says there is enough information and names a condition. The dataset card does not say whether those rows are human or synthetic. The id says MedMCQA. The rows are not multiple-choice exam items.

The objective is SFT. The card says "This model was trained with SFT." It does not say whether the update was full or LoRA. There is no adapter file. `training_args.bin` is in the repository and was not unpacked, so epochs, steps, batch size, and learning rate are not stated. The number in the repository name is not used.

The card names the parent `meta-llama/Llama-3.1-8B-Instruct`. No other source restates it. The weight files contain 8,030,261,248 parameters.

The card does not say what the model is for. The only example is a time-machine question. The use claim is weak, and there is no warning. No audience and no function are stated on the card. The YAML value `licence: license` is not a license name.

The training rows are a conversation with a person describing symptoms, a triage judgment, and a decision about whether a diagnosis can be made. No specialty is named, so the field is general medicine. The card reports no evaluation.

The example runs on text. The reply in that example is a chat turn. The training targets are reasoning paragraphs. A Llama 3.1 chat template is present and writes "Cutting Knowledge Date: December 2023" and "Today Date: 26 Jul 2024" when no system message is passed. `generation_config.json` sets temperature 0.6, top_p 0.9, and do_sample. The card example uses max_new_tokens 128. Context length is 131072.
