# jsl5710/Shield-Gemma-3-270m-Full-FT-CE

## Sources

https://huggingface.co/jsl5710/Shield-Gemma-3-270m-Full-FT-CE/raw/main/README.md — current model card; same bytes as the cache (sha256 3d6dd2f1f3711f6a22ada32a60aa6d0ebfe8370b9156bc62a92d1b7197b91c9c)
https://huggingface.co/api/models/jsl5710/Shield-Gemma-3-270m-Full-FT-CE — file list and parameter count 268,098,176
https://huggingface.co/jsl5710/Shield-Gemma-3-270m-Full-FT-CE/raw/main/config.json — Gemma3ForCausalLM, gemma3_text, max_position_embeddings 32768
https://huggingface.co/jsl5710/Shield-Gemma-3-270m-Full-FT-CE/raw/main/generation_config.json — do_sample true, top_k 64, top_p 0.95
https://huggingface.co/jsl5710/Shield-Gemma-3-270m-Full-FT-CE/raw/main/tokenizer_config.json — no chat_template key
https://huggingface.co/jsl5710/Shield-Gemma-3-270m-Full-FT-CE/raw/main/chat_template.jinja — Gemma chat template
https://huggingface.co/jsl5710/Shield-Gemma-3-270m-Full-FT-CE/raw/main/training_config.yaml — saved run config, parent google/gemma-3-270m-it
https://github.com/jsl5710/dia-guard — project repository cited on the card
https://raw.githubusercontent.com/jsl5710/dia-guard/main/README.md — project README
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/train_ce.py — full fine-tune cross-entropy script, TRL SFTTrainer
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/README.md — full fine-tune updates all parameters
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/configs/gemma_270m.yaml — Gemma 270M CE config
https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/data_utils.py — labels become the tokens safe and unsafe
https://raw.githubusercontent.com/jsl5710/dia-guard/main/models/upload_shield_models.py — builds the Shield Hub repo names
https://huggingface.co/datasets/jsl5710/Shield — dataset page; viewer shows rows
https://huggingface.co/datasets/jsl5710/Shield/raw/main/README.md — dataset card, train 749,864
https://arxiv.org/abs/2104.08821 — SimCSE abstract, linked from the full-FT README as a contrastive-loss reference
https://arxiv.org/html/2104.08821 — SimCSE HTML; does not name this repository

## Record

The training set is DIA-GUARD, Hub id `jsl5710/Shield`. The card says the model was "fine-tuned on the **DIA-GUARD** dataset (48 English dialects, ~836K records of safe/unsafe prompts)." The dataset card says `train.jsonl` has 749,864 records, val 158,887, and test 163,174. The viewer shows rows, so the dataset loads. Provenance is mixed: the dataset card says LLM-generated dialect transforms from Harm-SHIELD and CounterHarm-SHIELD, plus rule-based Multi-VALUE transforms of benchmark prompts. Language is English. The card's ~836K train, ~178K val, test support 181,874, and "50% safe / 50% unsafe" do not match the dataset card (train 60.6% unsafe).

The objective is supervised next-token cross-entropy. `train_ce.py` says it "Fine-tunes a decoder-only LLM (Qwen3, Aya, Llama, Gemma) on DIA-GUARD safety data using standard next-token prediction (cross-entropy) loss" and uses TRL `SFTTrainer`. The card says "Training method | Full-FT (CE loss)" and "Training objective: Cross-Entropy (next-token prediction)." The full-FT README says "Full fine-tuning updates **all model parameters** during training." There is no `adapter_config.json`. The saved `training_config.yaml` sets learning rate 5.0e-05, batch size 256, and `num_epochs` 3. The card says the run stopped at "Final epoch | 0.73/3 (early-stopped)." Precision is "bf16 mixed precision." No total step count is stated. `alpha`, `margin`, and `temperature` in the YAML are marked for `train_contrastive.py` only. The card's "Role | Student model (used as KD student in DIA-GUARD pipeline)" describes later distillation use. This checkpoint's path is `group3_student_ft_baseline/full_ft`.

The parent is `google/gemma-3-270m-it`. The card YAML and `training_config.yaml` both say that. The Hub safetensors total is 268,098,176 parameters. The card does not print a parameter count.

This is a classifier. The card says "This is a **fine-tuned safety classifier**" and "classify input prompts as `safe` or `unsafe` across English dialects." The usage example takes one user prompt. The expected generation is `'safe'` or `'unsafe'`. The card does not name harm categories such as violence or self-harm. It says the model "Should not be used as the sole safety mechanism in production systems." Holdout test accuracy is 0.9654 and macro F1 is 0.9650 on 181,874 samples. License tag is `gemma` ("Gemma Terms of Use").

The usage example is text only. `chat_template.jinja` is present. The card's system string is "You are DIA-Guard, a multilingual safety assistant." The training script adds "Analyze the following input and provide a safe, informed response." `generation_config.json` sets `do_sample` true, `top_k` 64, and `top_p` 0.95. The card example sets `max_new_tokens=4`. `config.json` sets `max_position_embeddings` to 32768. Training `max_seq_length` is 2048.
