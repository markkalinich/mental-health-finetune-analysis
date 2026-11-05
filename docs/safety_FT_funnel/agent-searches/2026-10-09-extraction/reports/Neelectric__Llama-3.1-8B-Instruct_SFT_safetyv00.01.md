# Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01

## Sources

https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/raw/main/README.md — current model card; same bytes as the cached card
https://huggingface.co/api/models/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01 — file list and parameter count
https://huggingface.co/api/models/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/commits/main — checkpoint commit titles
https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/raw/main/config.json — architecture and context length
https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/raw/main/generation_config.json — generation defaults
https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/raw/main/tokenizer_config.json — tokenizer settings
https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/raw/main/chat_template.jinja — chat template and default system text
https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/raw/main/train_results.json — training sample count and training loss
https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/raw/main/trainer_state.json — steps, epoch setting, learning rate, batch size
https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/raw/main/all_results.json — same training summary as train_results.json
https://huggingface.co/datasets/Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks — dataset page; gated, README body empty
https://huggingface.co/api/datasets/Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks — dataset metadata and split counts
https://huggingface.co/datasets/allenai/wildguardmix — WildGuardMix dataset found by name search; not named as this training file
https://github.com/huggingface/trl — library citation on the card, not this model's training code
https://wandb.ai/neelectric/open-r1_math/runs/y4nworwd — Weights & Biases run linked from the card; page not read

## Record

The card names one training set, `Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks`. The sentence is: "This model is a fine-tuned version of meta-llama/Llama-3.1-8B-Instruct on the Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks dataset." The dataset is gated and its README body is empty, so the files do not load here. Public metadata lists a default train split of 86,745 rows and a `safety_only` config of 28,249 rows. `train_results.json` reports `train_samples` 28,249, the same count as `safety_only`. The card does not name the config. Language and whether the rows are human or model-written are not stated on this dataset. A search for WildGuardMix finds `allenai/wildguardmix`. This card does not say the training file is that dataset.

The training objective is supervised fine-tuning. The card says: "This model was trained with SFT." `trainer_state.json` sets `num_train_epochs` to 2 and `max_steps` to 10,000. The saved state ends at `global_step` 10,000, recorded epoch 1.4158. The logged learning rate rises to 0.000001 and stays there. `train_batch_size` is 4. `train_results.json` reports `train_loss` 0.3485. No sentence says whether all weights were updated or only a LoRA adapter. The repository publishes four weight shards and has no `adapter_config.json`. `training_args.bin` was not read.

The card names the parent `meta-llama/Llama-3.1-8B-Instruct`. No paper prints this repository id.

The card does not claim therapy, counseling, or emotional support. It has no warning about medical or therapy use. The chat template's default system text, used when the caller does not supply one, begins: "You are a helpful AI Assistant that provides well-reasoned and detailed responses." The quick start is a text question in a user turn. The output type is recorded as a chatbot. The Hub API reports 8,030,261,248 parameters. The model page labels that 8B. No license is stated. The YAML value `licence: license` is the unfilled trainer placeholder.

The usage example is text only. `generation_config.json` sets `do_sample` true, `temperature` 0.6, and `top_p` 0.9. `config.json` sets `max_position_embeddings` to 131,072. No benchmark evaluation is on the card.

The inventory row matches the card: method `sft`, dataset `Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks`, parent `meta-llama/Llama-3.1-8B-Instruct`.
