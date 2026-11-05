# jsl5710/Shield-Qwen3-1.7B-Full-FT-CE

## Sources

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-Full-FT-CE/raw/main/README.md — current model card; same bytes as the cache (sha256 19e7f8b6f48b36be9d5245460486c6aa0e7f348f0cd0ba61699ebfea3104a496)
https://huggingface.co/api/models/jsl5710/Shield-Qwen3-1.7B-Full-FT-CE — file list and parameter count 1,720,574,976
https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-Full-FT-CE/raw/main/config.json — Qwen3ForCausalLM, max_position_embeddings 40960
https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-Full-FT-CE/raw/main/generation_config.json — do_sample true, temperature 0.6, top_k 20, top_p 0.95
https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-Full-FT-CE/raw/main/tokenizer_config.json — no chat_template key; model_max_length 131072
https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-Full-FT-CE/raw/main/chat_template.jinja — Qwen3 chat template, including a think block
https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-Full-FT-CE/raw/main/training_config.yaml — saved run config, parent Qwen/Qwen3-1.7B
https://github.com/jsl5710/dia-guard — project repository cited on the card
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/train_ce.py — full fine-tune cross-entropy script, TRL SFTTrainer
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/configs/qwen_1.7b.yaml — Qwen3 1.7B CE config
https://huggingface.co/datasets/jsl5710/Shield/raw/main/README.md — dataset card, train 749,864
https://arxiv.org/abs/2505.09388 — Qwen3 Technical Report; does not name this repository
https://arxiv.org/html/2104.08821 — SimCSE HTML, linked from the full-FT README; does not name this repository
https://featherless.ai/models/jsl5710/Shield-Qwen3-1.7B-Full-FT-CE — hosted inference page that restates the card
https://huggingface.co/Qwen/Qwen3-1.7B — parent card; states 1.7B parameters and context length 32,768

## Record

The training set is DIA-GUARD, Hub id `jsl5710/Shield`. The card says the model was "fine-tuned on the **DIA-GUARD** dataset (48 English dialects, ~836K records of safe/unsafe prompts)." The dataset card says `train.jsonl` has 749,864 records. The viewer shows rows, so the dataset loads. Provenance is mixed. Language is English. The card's ~836K train and test support 181,874 do not match the dataset card (train 749,864, test 163,174).

The objective is supervised next-token cross-entropy. `train_ce.py` uses TRL `SFTTrainer` and says it fine-tunes Qwen3 "using standard next-token prediction (cross-entropy) loss." The card says "Training method | Full-FT (CE loss)." The saved config sets learning rate 2.0e-05, batch size 64, and `num_epochs` 3. The card says the run stopped at "Final epoch | 0.26/3 (early-stopped)." Precision is "bf16 mixed precision." There is no `adapter_config.json` and no total step count. The output directory is `group3_student_ft_baseline/full_ft/qwen3_1_7b`.

The parent is `Qwen/Qwen3-1.7B`. The card YAML and `training_config.yaml` both say that. The Hub safetensors total is 1,720,574,976 parameters. The parent card says "Number of Parameters: 1.7B."

This is a classifier. The card says "This is a **fine-tuned safety classifier**" and "classify input prompts as `safe` or `unsafe` across English dialects." The usage example takes one user prompt. The expected generation is `'safe'` or `'unsafe'`. The card does not name harm categories. It says the model "Should not be used as the sole safety mechanism in production systems." Holdout test accuracy is 0.7868 and macro F1 is 0.7837 on 181,874 samples. Unsafe recall is 0.6146. License tag is `apache-2.0`.

The usage example is text only. `chat_template.jinja` is present and can write a `<think>` block. The card's system string is "You are DIA-Guard, a multilingual safety assistant." `generation_config.json` sets `do_sample` true, `temperature` 0.6, `top_k` 20, and `top_p` 0.95. The card example sets `max_new_tokens=4`. This repo's `config.json` sets `max_position_embeddings` to 40960. The parent card says context length 32,768. Training `max_seq_length` is 2048.
