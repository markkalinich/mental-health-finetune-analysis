# adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1

## Sources

- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/README.md — current model card; identical to the cached card (sha256 b8a44df4308bb5c9c477a55c01e1fa3d634ed02e4faa57af429a28bf02be18ff)
- https://huggingface.co/api/models/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1 — file list, parameter count, and chat template text
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/config.json — architecture and max position embeddings
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/generation_config.json — generation defaults
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/train_results.json — training loss
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/all_results.json — same training loss figures
- https://huggingface.co/adzcai/AfriGuardPlain-AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/trainer_state.json — step count, epoch, batch size
- https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/README.md — parent card, text-only serving example
- https://huggingface.co/datasets/adzcai/AfriGuard-plain — training dataset card
- https://huggingface.co/datasets/israel/AfriGuard-inst — dataset this one was built from
- https://huggingface.co/datasets/israel/AfriGuard — human labels and model responses
- https://huggingface.co/datasets/israel/AfriGuard-XL — model-generated responses
- https://datasets-server.huggingface.co/is-valid?dataset=adzcai/AfriGuard-plain — load check returned 401

## Record

The training set is `adzcai/AfriGuard-plain`. The dataset card calls it "a non-instruction-prompted version of israel/AfriGuard-inst" and prints 46,306 train rows and 7,175 validation rows. It does not load without approval: access is gated, and the datasets server returned 401. The replies are the text that was inside the response tag of AfriGuard-inst. AfriGuard says the English response is a "model response" and that labels are "majority-vote annotations from three native-speaker annotators". AfriGuard-XL says the response is an "English model-generated response". That is mixed.

The update is a full fine-tune. The card says the parent was "fine-tuned with full fine-tuning (DeepSpeed ZeRO-3)". The objective is supervised fine-tuning: the named config is `afriguard_plain_afriqueqwen3.5-4b-50langs-instruct_full_sft.yaml`, and the card says "loss on the response only". There is no LoRA rank or alpha. The repo has no adapter file. The card does not say the base was quantized. Epochs are 1. Learning rate is 1e-05. Train batch size is 1. `trainer_state.json` records `global_step` 23153 and `max_steps` 23153. That is 46,306 examples at an effective batch of 2. The prose says "1 GPU"; the trainer block says `distributed_type: multi-GPU`. The named LlamaFactory repo is not linked, and no search found the yaml. No paper names this repository.

The card names the parent `McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1`. The Hub file list reports 4,539,265,536 parameters.

The card says "The model therefore answers or refuses directly, without emitting a safety label." Output type is Other. The use claim is Absent: the text is safety refusal, not mental-health support. The model card has no warning, so warning strength is None. `train_results.json` reports train_loss 1.4647940215562758. No benchmark scores are stated.

Serving is text-only on the parent's terms. The parent card says the checkpoint "carries no vision weights" and "so `--language-model-only` is required." This repo's `config.json` still declares a vision config. `max_position_embeddings` is 262144. A chat template is present in `chat_template.jinja`. No system prompt is written into it. `generation_config.json` does not set temperature, top_p, top_k, max_new_tokens, repetition_penalty, or do_sample. License is `cc-by-4.0`.

The inventory row matches: full fine-tune, dataset `adzcai/AfriGuard-plain`, parent `McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1`.
