# geshijoker/HealthCareMagic_sft_llama3_instruct_full

## Sources

- https://huggingface.co/geshijoker/HealthCareMagic_sft_llama3_instruct_full/raw/main/README.md — current model card; same text as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/geshijoker__HealthCareMagic_sft_llama3_instruct_full__2026-10-05.md — cached card
- https://huggingface.co/api/models/geshijoker/HealthCareMagic_sft_llama3_instruct_full — file list, parameter count, chat template
- https://huggingface.co/geshijoker/HealthCareMagic_sft_llama3_instruct_full/raw/main/config.json — Llama config; context 8192; parent path
- https://huggingface.co/geshijoker/HealthCareMagic_sft_llama3_instruct_full/raw/main/generation_config.json — temperature 0.6, top_p 0.9
- https://huggingface.co/geshijoker/HealthCareMagic_sft_llama3_instruct_full/raw/main/trainer_state.json — 525 steps, 3 epochs
- https://huggingface.co/geshijoker/HealthCareMagic_sft_llama3_instruct_full/raw/main/all_results.json — train and eval loss
- https://huggingface.co/geshijoker/HealthCareMagic_sft_llama3_instruct_full/raw/main/eval_results.json — eval loss
- https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k — HealthCareMagic dialogues; viewer loads, 112,165 rows
- https://huggingface.co/datasets/MedSwin/HealthCareMagic — a later HealthCareMagic copy, file dated 2025-08-24, after this December 2024 run

No GitHub repository and no paper name this checkpoint. The parent card at https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct returned 401.

## Record

The card says the model "is a fine-tuned version of meta-llama/Meta-Llama-3-8B-Instruct on the healthcaremagic dataset." It does not give a hub id or a row count. The Hub dataset with that content is `lavita/ChatDoctor-HealthCareMagic-100k`. Its viewer loads 112,165 English rows. Each row's instruction is "If you are a doctor, please answer the medical questions based on the patient's description." The dataset card does not say whether the dialogues are human or synthetic. `MedSwin/HealthCareMagic` is a later file and is not this training run.

The run is named `sft_full`. The card tag is `full`, and the comparison row for this checkpoint is "full fientune from inst." That is a full update, not QLoRA. The card sets learning rate 1e-05, train batch size 8, and 3 epochs. `trainer_state.json` ends at step 525. There is no LoRA rank and no adapter file. The weights are the full model.

The parent is `meta-llama/Meta-Llama-3-8B-Instruct`. The card says that, and `config.json` sets `_name_or_path` to the same id. The weight files contain 8,030,261,248 parameters.

The card does not say what the model is for. Intended uses are "More information needed." The use claim is weak: the only medical content is the dataset name. There is no warning. No audience and no function are stated.

The card does not name a clinical task or a specialty. The HealthCareMagic rows are patients describing symptoms and a reply written as a doctor, but that sentence is on the dataset page, and the model card does not adopt it. The printed scores are evaluation loss 1.7460, and for the full-finetune row Rouge1 0.315, RougeL 0.189, Meteor 0.238, and BERTScore 0.782. That row's link points at the parent model.

The card has no usage example, so text-only input is not stated. The config is a text Llama model. A Llama 3 chat template is in the tokenizer. `generation_config.json` sets temperature 0.6, top_p 0.9, do_sample true, and max_length 4096. Context length is 8192. No system prompt is set. The license tag is llama3.
