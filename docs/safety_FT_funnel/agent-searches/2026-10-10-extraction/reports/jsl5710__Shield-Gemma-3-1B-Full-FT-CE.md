# jsl5710/Shield-Gemma-3-1B-Full-FT-CE

## Sources

- https://huggingface.co/jsl5710/Shield-Gemma-3-1B-Full-FT-CE/raw/main/README.md — current model card; same text as the cached card
- https://huggingface.co/api/models/jsl5710/Shield-Gemma-3-1B-Full-FT-CE — file list and chat template
- https://huggingface.co/jsl5710/Shield-Gemma-3-1B-Full-FT-CE/raw/main/config.json — context length 32,768
- https://huggingface.co/jsl5710/Shield-Gemma-3-1B-Full-FT-CE/raw/main/generation_config.json — top_k 64, top_p 0.95
- https://huggingface.co/jsl5710/Shield-Gemma-3-1B-Full-FT-CE/raw/main/training_config.yaml — learning rate 3e-5, batch 96, base model
- https://huggingface.co/datasets/jsl5710/Shield — DIA-GUARD splits
- https://huggingface.co/datasets/jsl5710/Shield/raw/main/splits_metadata.json — train 749,864, val 158,887, test 163,174
- https://github.com/jsl5710/dia-guard — project code; Group 3 is direct full fine-tuning of students under 2B

## Record

The training data is DIA-GUARD, hosted as `jsl5710/Shield`. `splits_metadata.json` records 749,864 train rows, 158,887 validation rows, and 163,174 test rows. The model card says "~836K train, 178K val" and a holdout test of 181,874. Those card counts do not match the metadata file. The rows mix original benchmark prompts with dialect transforms and benign counter-examples. The dataset loads.

This checkpoint is a full fine-tune. The card says "Training method: Full-FT (CE loss)" and "Training objective: Cross-Entropy (next-token prediction)." `training_config.yaml` sets the base to `google/gemma-3-1b-it`, learning rate 3e-5, batch size 96, and 3 epochs. The card says the run stopped at epoch 0.48 of 3. Training precision is bf16. There is no LoRA rank in that yaml. The GitHub README's rank 64 and alpha 128 belong to the separate PEFT runs.

The parent is `google/gemma-3-1b-it`. The card title calls the size Gemma-3-1B. The weight file has 999,885,952 parameters.

The card presents a safety classifier. The input is one user prompt. The example expects the tokens `safe` or `unsafe`, with `max_new_tokens` 4. The claim is to "classify input prompts as safe or unsafe across English dialects." It does not name a harm-category list.

The example is text. The system line is "You are DIA-Guard, a multilingual safety assistant." A chat template is in the repository. `generation_config.json` sets `do_sample` true, top_k 64, and top_p 0.95. Context length is 32,768. The license is the Gemma terms. No arXiv paper is linked. The citation points at the GitHub repository.
