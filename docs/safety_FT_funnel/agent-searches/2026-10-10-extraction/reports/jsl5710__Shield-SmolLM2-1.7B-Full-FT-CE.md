# jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE

## Sources

https://huggingface.co/jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE/raw/main/README.md — current model card; same bytes as the cache (sha256 55b2c599305220792b6e03d1def502e559fb4a4d057f99a643607d082564eda3)
https://huggingface.co/api/models/jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE — file list and parameter count 1,711,376,384
https://huggingface.co/jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE/raw/main/config.json — LlamaForCausalLM, max_position_embeddings 8192
https://huggingface.co/jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE/raw/main/generation_config.json — token ids only, no sampling fields
https://huggingface.co/jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE/raw/main/tokenizer_config.json — no chat_template key; model_max_length 8192
https://huggingface.co/jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE/raw/main/chat_template.jinja — SmolLM chat template
https://huggingface.co/jsl5710/Shield-SmolLM2-1.7B-Full-FT-CE/raw/main/training_config.yaml — saved run config, parent HuggingFaceTB/SmolLM2-1.7B-Instruct
https://github.com/jsl5710/dia-guard — project repository cited on the card
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/train_ce.py — full fine-tune cross-entropy script, TRL SFTTrainer
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/configs/smollm_1.7b.yaml — SmolLM2 1.7B CE config
https://huggingface.co/datasets/jsl5710/Shield/raw/main/README.md — dataset card, train 749,864
https://arxiv.org/abs/2502.02737 — SmolLM2 paper; does not name this repository
https://arxiv.org/html/2104.08821 — SimCSE HTML, linked from the full-FT README; does not name this repository

## Record

The training set is DIA-GUARD, Hub id `jsl5710/Shield`. The card says the model was "fine-tuned on the **DIA-GUARD** dataset (48 English dialects, ~836K records of safe/unsafe prompts)." The dataset card says `train.jsonl` has 749,864 records. The viewer shows rows, so the dataset loads. Provenance is mixed. Language is English. The card's ~836K train and test support 181,874 do not match the dataset card (train 749,864, test 163,174).

The objective is supervised next-token cross-entropy. `train_ce.py` uses TRL `SFTTrainer`. The card says "Training method | Full-FT (CE loss)." The saved config sets learning rate 2.0e-05, batch size 64, and `num_epochs` 3. The card says the run stopped at "Final epoch | 0.60/3 (early-stopped)." Precision is "bf16 mixed precision." There is no `adapter_config.json` and no total step count. The output directory is `group3_student_ft_baseline/full_ft/smollm2_1_7b_instruct`.

The parent is `HuggingFaceTB/SmolLM2-1.7B-Instruct`. The card YAML and `training_config.yaml` both say that. The Hub safetensors total is 1,711,376,384 parameters.

This is a classifier. The card says "This is a **fine-tuned safety classifier**" and "classify input prompts as `safe` or `unsafe` across English dialects." The usage example takes one user prompt. The expected generation is `'safe'` or `'unsafe'`. The card does not name harm categories. It says the model "Should not be used as the sole safety mechanism in production systems." Holdout test accuracy is 0.7481 and macro F1 is 0.7467 on 181,874 samples. Unsafe recall is 0.6206. License tag is `apache-2.0`.

The usage example is text only. `chat_template.jinja` is present. The card's system string is "You are DIA-Guard, a multilingual safety assistant." If no system message is passed, the template inserts "You are a helpful AI assistant named SmolLM, trained by Hugging Face." `generation_config.json` does not set temperature, top_p, top_k, or do_sample. The card example sets `max_new_tokens=4`. `config.json` sets `max_position_embeddings` to 8192. Training `max_seq_length` is 2048.
