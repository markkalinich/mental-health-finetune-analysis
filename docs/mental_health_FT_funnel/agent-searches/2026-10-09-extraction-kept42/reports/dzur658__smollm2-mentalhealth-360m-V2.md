# dzur658/smollm2-mentalhealth-360m-V2

## Sources

- https://huggingface.co/dzur658/smollm2-mentalhealth-360m-V2 — current model card; same bytes as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/dzur658__smollm2-mentalhealth-360m-V2__2026-10-09.md — cached card, sha256 6f14f638079428c298a367a4b96c5a97a1275f1aee968078ac3b6540cecd4273
- https://huggingface.co/api/models/dzur658/smollm2-mentalhealth-360m-V2 — repository file list
- https://huggingface.co/dzur658/smollm2-mentalhealth-360m-V2/raw/main/config.json — config, max position embeddings 8192
- https://huggingface.co/dzur658/smollm2-mentalhealth-360m-V2/raw/main/generation_config.json — token ids only
- https://huggingface.co/dzur658/smollm2-mentalhealth-360m-V2/raw/main/tokenizer_config.json — no chat_template key; model_max_length 8192
- https://huggingface.co/dzur658/smollm2-mentalhealth-360m-V2/raw/main/chat_template.jinja — chat template file
- https://github.com/dzur658/smollm2-mentalhealth-360m — GitHub README; names the v2 script
- https://github.com/dzur658/smollm2-mentalhealth-360m/blob/main/smollm_finetuningv2.py — v2 training script
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — dataset card
- https://huggingface.co/datasets/Amod/mental_health_counseling_conversations/viewer/default/train — viewer shows the train split
- https://arxiv.org/abs/2502.02737 — SmolLM2 paper abstract; does not name this repository
- https://arxiv.org/html/2502.02737 — SmolLM2 HTML; does not name this repository
- https://huggingface.co/dzur658/smollm2-mentalhealth-360m — earlier checkpoint linked from the card
- https://huggingface.co/dzur658/smollm2-mentalhealth-360m-v2-gguf — GGUF weights linked from the card

## Record

The training script loads one dataset, `Amod/mental_health_counseling_conversations`, train split. The dataset card says: "This dataset is a collection of real counselling question-and-answer pairs taken from two public mental-health platforms." Language on the dataset card is English. The Hub viewer shows a train split labeled "3.51k rows". The size API returned 401, and the dataset is marked gated manual, so the exact row count is not in this record. The viewer page itself displays rows.

The v2 script builds an `SFTTrainer` on `HuggingFaceTB/SmolLM2-360M-Instruct` loaded with `from_pretrained` and no quantization config. The card says: "Full fine tune of SmolLm2-360m in BF16 precision using the TRL library and Pytorch running on a 3050 ti laptop GPU for 3 epochs." The pasted arguments set 3 epochs, learning rate `2e-4`, and `per_device_train_batch_size=2` with `gradient_accumulation_steps=4`. No LoRA rank, LoRA alpha, or step count is stated. The usage example's local path `checkpoint-1185` is a folder name, not a stated step count. The GitHub README says `smollm_finetuningv2.py` is the script for the v2 model.

The card and the script name the same parent, `HuggingFaceTB/SmolLM2-360M-Instruct`. The card says the model has "360 million parameters".

The card presents a text chat assistant. The system prompt is: "You are an extremely empathetic and helpful AI assistant named SmolHealth designed to listen to the user and provide insight." That is the purpose the card trains and recommends, so the use claim is Strong. The warning forbids clinical use: "This Model should in no way be used to treat, diagnose, or otherwise prevent mental health disorders, and is simply a demonstration of full fine tuning a small model on a consumer GPU." A second sentence says the model "should not be used to treat mental health disorders, nor should this model be used as a substitute for a licensed professional." Language on the card is "English (tested)".

The card's example runs `pipeline("text-generation")` on a typed user string, with `do_sample=True`, `temperature=0.8`, `top_p=0.9`, and `max_new_tokens=1024`. A chat template file is present. `generation_config.json` does not set those sampling values. Context length in `config.json` is 8192. The only paper a search returned is the SmolLM2 base-model paper, and it does not print this repository id. No numeric benchmark is reported. The card's evaluation sentence is the author's "limited testing" note about describing mental health problems and giving high-level advice. Inventory methods, dataset, and parent match the card and the script.
