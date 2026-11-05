# adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged

## Sources

- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/README.md — current model card; identical to the cached card (sha256 30eaf0fccb44cce35667af1034ff01fd6e65d7e9258dc61e6974871acb8d4526)
- https://huggingface.co/api/models/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged — file list, parameter count, and chat template text
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/config.json — architecture and max position embeddings
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/generation_config.json — generation defaults
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/Modelfile — Ollama template; no default system text
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/train_results.json — training loss
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/all_results.json — same training loss figures
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/trainer_log.jsonl — step count
- https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/README.md — parent card, text-only serving example
- https://arxiv.org/abs/2601.06395 — AfriqueLLM abstract; does not name this repository
- https://arxiv.org/html/2601.06395 — same paper's HTML; a text search finds no AfriGuard and no this repository id
- https://huggingface.co/datasets/adzcai/AfriGuard-plain — training dataset card
- https://huggingface.co/datasets/israel/AfriGuard-inst — dataset this one was built from
- https://huggingface.co/datasets/israel/AfriGuard — human labels and model responses
- https://huggingface.co/datasets/israel/AfriGuard-XL — model-generated responses
- https://datasets-server.huggingface.co/is-valid?dataset=adzcai/AfriGuard-plain — load check returned 401

## Record

The training set is `adzcai/AfriGuard-plain`. The dataset card calls it "a non-instruction-prompted version of israel/AfriGuard-inst" and prints 46,306 train rows and 7,175 validation rows. It does not load without approval. The replies are taken from AfriGuard-inst. AfriGuard says the English response is a "model response" and that labels are "majority-vote annotations from three native-speaker annotators". AfriGuard-XL says the response is an "English model-generated response". That is mixed.

The update is LoRA, then merged. The card says the parent was "fine-tuned with LoRA (rank 16, all linear layers), merged into the base weights". The objective is supervised fine-tuning: the named config is `afriguard_plain_afriqueqwen3.5-4b-50langs-instruct_lora_sft.yaml`, and the card says "loss on the response only". Rank is 16. Alpha is not stated. The card does not say the base was quantized. Epochs are 1. Learning rate is 0.0001. Train batch size is 1. `trainer_log.jsonl` records `current_steps` 23153 and `total_steps` 23153. The prose says "1 GPU"; the trainer block says `distributed_type: multi-GPU`. No adapter file is in the repo. The named LlamaFactory repo is not linked. No paper names this repository. The AfriqueLLM preprint is about continued pre-training of the parent family. Its HTML does not contain this repository id.

The card names the parent `McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1`. The Hub file list reports 4,539,265,536 parameters.

The card says "The model therefore answers or refuses directly, without emitting a safety label." Output type is Other. The use claim is Absent. The model card has no warning, so warning strength is None. `train_results.json` reports train_loss 1.3653174731683326. No benchmark scores are stated.

Serving is text-only on the parent's terms. The parent card says the checkpoint "carries no vision weights" and "so `--language-model-only` is required." This repo's `config.json` still declares a vision config. `max_position_embeddings` is 262144. A chat template is present in `chat_template.jinja`. No system prompt is written into the template or the Modelfile. `generation_config.json` does not set temperature, top_p, top_k, max_new_tokens, repetition_penalty, or do_sample. License is `cc-by-4.0`.

The inventory row matches: LoRA, dataset `adzcai/AfriGuard-plain`, parent `McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1`.
