# adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1

## Sources

https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/adzcai__AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1__2026-10-09.md — cached card
https://huggingface.co/api/models/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1 — file list and parameter count
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/config.json — architecture, vision config, and context length
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/generation_config.json — generation config
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/tokenizer_config.json — tokenizer; no chat_template key
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/chat_template.jinja — chat template
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/trainer_state.json — step count and batch size
https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/train_results.json — training loss
https://huggingface.co/datasets/israel/AfriGuard-inst — training dataset card
https://featherless.ai/models/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1 — hosting page that names this repository and the same parent

## Record

The checkpoint was trained on `israel/AfriGuard-inst`. The dataset card says it is "Alpaca-style instruction-tuning data for safety-aligned fine-tuning, built from the train/validation splits of israel/AfriGuard and israel/AfriGuard-XL." The train total is 46,306 rows. A validation total of 7,175 is also listed. The page loads with `load_dataset("israel/AfriGuard-inst")`. Rows are English plus Amharic, Hausa, Igbo, Oromo, Shona, Swahili, Twi, Wolof, Yoruba, and Zulu. The dataset card does not say whether the prompts are human-written or generated.

The objective is supervised fine-tuning. The card says "loss on the response only" and names a config file `afriguard_inst_afriqueqwen3.5-4b-50langs-instruct_full_sft.yaml`. The update is full fine-tuning: "fine-tuned with full fine-tuning (DeepSpeed ZeRO-3)". Learning rate is 1e-05. `num_epochs` is 1.0. `trainer_state.json` records `global_step` 23153 and `max_steps` 23153, and `train_batch_size` 1. The card also lists `gradient_accumulation_steps: 2` and `total_train_batch_size: 2`. Rank, alpha, and quantization of the base are not stated. The repository publishes `model.safetensors` and no adapter file. The card says both "1 GPU" and "distributed_type: multi-GPU". A search did not find the LlamaFactory repository named on the card.

The parent is `McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1`. A Featherless page for this repository id says the same. The Hub file metadata counts 4,539,265,536 parameters. The inventory row matches: full fine-tune, `israel/AfriGuard-inst`, and that parent.

The card describes a text model that answers a user prompt with a safety tag, a category tag, and a response, so the output type is a chatbot and the described input is text. There is no mental-health claim and no warning about therapy or medical use. The card's training-results section is empty. `train_results.json` reports train loss 1.1802280926526258. License is cc-by-4.0. YAML languages are en, am, ha, ig, om, sn, sw, tw, wo, yo, and zu.

`generation_config.json` does not set temperature, top_p, or max new tokens. `config.json` sets `max_position_embeddings` to 262144 inside `text_config`. The chat template is in `chat_template.jinja`. It has no fixed system prompt. The same config declares `Qwen3_5ForConditionalGeneration` and a `vision_config`, and the template can place image and video tokens. The training description uses text instructions and a text user prompt.
