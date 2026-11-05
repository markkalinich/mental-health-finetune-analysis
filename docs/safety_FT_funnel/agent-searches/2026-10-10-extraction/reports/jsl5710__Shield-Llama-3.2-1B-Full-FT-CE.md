# jsl5710/Shield-Llama-3.2-1B-Full-FT-CE

## Sources

https://huggingface.co/jsl5710/Shield-Llama-3.2-1B-Full-FT-CE/raw/main/README.md — current model card; same bytes as the cache (sha256 5e68250346b4b692a7ff7abad6bbe048defefc901497f32bba6672f8f5ed66d6)
https://huggingface.co/api/models/jsl5710/Shield-Llama-3.2-1B-Full-FT-CE — file list and parameter count 1,235,814,400
https://huggingface.co/jsl5710/Shield-Llama-3.2-1B-Full-FT-CE/raw/main/config.json — LlamaForCausalLM, max_position_embeddings 131072
https://huggingface.co/jsl5710/Shield-Llama-3.2-1B-Full-FT-CE/raw/main/generation_config.json — do_sample true, temperature 0.6, top_p 0.9
https://huggingface.co/jsl5710/Shield-Llama-3.2-1B-Full-FT-CE/raw/main/tokenizer_config.json — no chat_template key; model_max_length 131072
https://huggingface.co/jsl5710/Shield-Llama-3.2-1B-Full-FT-CE/raw/main/chat_template.jinja — Llama 3 chat template
https://huggingface.co/jsl5710/Shield-Llama-3.2-1B-Full-FT-CE/raw/main/training_config.yaml — saved run config, parent meta-llama/Llama-3.2-1B-Instruct
https://github.com/jsl5710/dia-guard — project repository cited on the card
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/train_ce.py — full fine-tune cross-entropy script, TRL SFTTrainer
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/configs/llama_1b.yaml — Llama 1B CE config
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/data_utils.py — labels become the tokens safe and unsafe
https://huggingface.co/datasets/jsl5710/Shield/raw/main/README.md — dataset card, train 749,864
https://arxiv.org/html/2104.08821 — SimCSE HTML, linked from the full-FT README; does not name this repository

## Record

The training set is DIA-GUARD, Hub id `jsl5710/Shield`. The card says the model was "fine-tuned on the **DIA-GUARD** dataset (48 English dialects, ~836K records of safe/unsafe prompts)." The dataset card says `train.jsonl` has 749,864 records. The viewer shows rows, so the dataset loads. Provenance is mixed: LLM-generated dialect transforms and rule-based Multi-VALUE transforms of benchmark prompts. Language is English. The card's ~836K train and test support 181,874 do not match the dataset card (train 749,864, test 163,174).

The objective is supervised next-token cross-entropy. `train_ce.py` says it fine-tunes Llama "using standard next-token prediction (cross-entropy) loss" with TRL `SFTTrainer`. The card says "Training method | Full-FT (CE loss)." The saved config sets learning rate 3.0e-05, batch size 96, and `num_epochs` 3. The card says the run stopped at "Final epoch | 0.71/3 (early-stopped)." Precision is "bf16 mixed precision." There is no `adapter_config.json` and no total step count. The output directory is `group3_student_ft_baseline/full_ft/llama_3_2_1b_instruct`.

The parent is `meta-llama/Llama-3.2-1B-Instruct`. The card YAML and `training_config.yaml` both say that. The Hub safetensors total is 1,235,814,400 parameters.

This is a classifier. The card says "This is a **fine-tuned safety classifier**" and "classify input prompts as `safe` or `unsafe` across English dialects." The usage example takes one user prompt. The expected generation is `'safe'` or `'unsafe'`. The card does not name harm categories. It says the model "Should not be used as the sole safety mechanism in production systems." Holdout test accuracy is 0.9644 and macro F1 is 0.9642 on 181,874 samples. Train accuracy is an em dash. License tag is `llama3.2` ("Llama 3.2 Community License").

The usage example is text only. `chat_template.jinja` is present. The card's system string is "You are DIA-Guard, a multilingual safety assistant." The Llama template also inserts a knowledge-cutoff line and a date. `generation_config.json` sets `do_sample` true, `temperature` 0.6, and `top_p` 0.9. The card example sets `max_new_tokens=4`. `config.json` sets `max_position_embeddings` to 131072. Training `max_seq_length` is 2048.
