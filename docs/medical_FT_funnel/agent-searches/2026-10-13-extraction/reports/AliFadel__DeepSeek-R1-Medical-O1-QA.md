# AliFadel/DeepSeek-R1-Medical-O1-QA

## Sources

https://huggingface.co/AliFadel/DeepSeek-R1-Medical-O1-QA/raw/main/README.md — current model card; identical to the cached card
https://huggingface.co/api/models/AliFadel/DeepSeek-R1-Medical-O1-QA — file list, parameter count, and chat template
https://huggingface.co/AliFadel/DeepSeek-R1-Medical-O1-QA/raw/main/config.json — context length, dtype, Unsloth version key
https://huggingface.co/AliFadel/DeepSeek-R1-Medical-O1-QA/raw/main/generation_config.json — sampling settings
https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — dataset card
https://huggingface.co/api/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — dataset loads; public JSON files
https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT/viewer/en — English split, 19.7k rows
https://arxiv.org/abs/2412.18925 — HuatuoGPT-o1 paper linked from the dataset card; it does not name this repository
https://github.com/FreedomIntelligence/HuatuoGPT-o1 — dataset authors' training repository for HuatuoGPT-o1, not this checkpoint
https://featherless.ai/models/AliFadel/DeepSeek-R1-Medical-O1-QA — hosted inference page that restates the card

## Record

The card says the model was "Trained on the FreedomIntelligence/medical-o1-reasoning-SFT dataset to learn clinical chain-of-thought reasoning." That dataset loads. It has English and Chinese files, plus mix files. The English viewer shows 19.7k rows, the English mix 24.9k, Chinese 20.2k, and Chinese mix 25.4k. The model card does not say which file was used, so the example count is unset. The dataset card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." That is synthetic text. The model card's language list is English only.

The card says "This is a fine-tuned version of the deepseek-ai/DeepSeek-R1-Distill-Llama-8B base model." "Fine-tuned" does not name a loss. The letters SFT appear in the dataset id, and the dataset card calls the dataset an SFT set. Neither sentence says this checkpoint was trained with supervised fine-tuning. There is no adapter file, no rank, and no learning-rate, epoch, step, or batch size. `config.json` has `unsloth_version` `2026.6.9`. That shows Unsloth saved the config. It does not say LoRA, QLoRA, or a full update. The weights are four safetensors shards, 8030261248 parameters, counted as BF16. `config.json` says `torch_dtype` float16. No source says the base was quantized during training.

The parent on the card is deepseek-ai/DeepSeek-R1-Distill-Llama-8B. No other source names a different parent. The HuatuoGPT-o1 paper and its GitHub repository describe a different model. The abstract says they "introduce HuatuoGPT-o1". It does not print `AliFadel/DeepSeek-R1-Medical-O1-QA`.

The use claim is moderate. The card says the model is "specialized in text-based medical Question Answering (QA)" and that it uses "step-by-step reasoning to break down clinical scenarios, patient symptoms, and medical captions to provide clear answers." It does not say it gives advice, a diagnosis, or treatment. The warning is a disclaimer: "This model is for research and educational purposes only. It cannot be used as a medical or diagnostic tool without a medical expert or doctor's supervision." No evaluation numbers are on the card. The license is MIT.

The purpose is medical question answering with step-by-step reasoning. The card does not name a person the model is for. "Research and educational purposes" and a doctor's supervision are limits, not an audience.

The functions are answering medical questions and clinical reasoning, from the two sentences above. The output is reasoning that ends in an answer.

The clinical task named on the card is medical question answering. The named dataset's paper says "we construct 40K verifiable medical problems reformatted from challenging, closed-set medical exam questions," so the training questions are exam items. The specialty is general medicine: the card says medical and clinical, and it names no field. The license line and the YAML `language` list are the only other card metadata of that kind.

Input is text. The card says "text-based". A chat template is present in `tokenizer_config.json` and `chat_template.jinja`. With no caller system message, the template writes "Cutting Knowledge Date: December 2023" and "Today Date: 26 July 2024". `generation_config.json` sets `do_sample` true, `temperature` 0.6, `top_p` 0.95, and `max_length` 131072. `max_position_embeddings` is 131072. Featherless lists a 32k context and FP8 weights; those are that host's serving settings.
