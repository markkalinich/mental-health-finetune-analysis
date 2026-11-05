# adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged

## Sources

- https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/README.md — current model card; identical to the cached card (sha256 7f1d5769cdaab0b23f610a3cd69d324f98de1078066daf700340d0a07bbb5e21)
- https://huggingface.co/api/models/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged — file list, parameter count, and chat template text
- https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/config.json — architecture and max position embeddings
- https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/generation_config.json — generation defaults
- https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
- https://huggingface.co/adzcai/AfriGuardInst-AfriqueQwen3.5-4B-50Langs-Instruct-v1-lora-merged/raw/main/Modelfile — Ollama template; no default system text
- https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1/raw/main/README.md — parent card, text-only serving example
- https://huggingface.co/datasets/israel/AfriGuard-inst — training dataset card (page loads; files are gated)
- https://huggingface.co/datasets/israel/AfriGuard — source dataset; human labels, model responses
- https://huggingface.co/datasets/israel/AfriGuard-XL — source dataset; model-generated responses
- https://datasets-server.huggingface.co/is-valid?dataset=israel/AfriGuard-inst — load check returned 401

## Record

The training set is `israel/AfriGuard-inst`. The model card says each example is "one of the safety system instructions plus the user prompt", and the target is "`<safety>…</safety>` `<category>…</category>` `<response>…</response>`". The dataset card prints 46,306 train rows and 7,175 validation rows, in English and ten African languages. It does not load without approval: the dataset is gated, and the datasets server returned 401. The rows come from `israel/AfriGuard` and `israel/AfriGuard-XL`. AfriGuard says it is "a human-annotated safety dataset" and that the English `response` column is a "model response", with "human-verified translations". AfriGuard-XL says the response is an "English model-generated response". Labels are human; reply text is model-written. That is mixed.

The objective is supervised fine-tuning. The card says this checkpoint "is a rerun of the AfriGuard-inst config `afriguard_lora_sft.yaml`" and that training used "loss on the response only". The update is LoRA, then merged: "fine-tuned with LoRA (rank 16, all linear layers), merged into the base weights". Rank is 16. Alpha is not stated. The card does not say the base was quantized. Epochs are 1. Learning rate is 0.0001. Train batch size is 1, with gradient accumulation 2, so the trainer block's total batch size is 2. Step count is not stated. The prose says "1 GPU"; the same card's trainer block says `distributed_type: multi-GPU`. No adapter file is in the repo. The named LlamaFactory repo is not linked, and a search did not find `afriguard_lora_sft.yaml`.

The card names the parent `McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1`. No paper or other page names this repository. The Hub file list reports 4,539,265,536 parameters. No paper was found for this checkpoint.

The card describes a safety-tag generator, not a conversation partner and not a mental-health tool. Output type is Other. The use claim is Absent. The card has no warning, so warning strength is None. The "Training results" section is empty.

Serving is text-only on the parent's terms. The parent card says: "The checkpoint declares `Qwen3_5ForConditionalGeneration` but carries no vision weights (426 language-model tensors, `lm_head` tied to the embeddings, 0 visual), so `--language-model-only` is required." Its example is a text chat completion. This repo's `config.json` still declares a vision config and image and video token ids. `max_position_embeddings` is 262144. A chat template is present in `chat_template.jinja`. No system prompt is written into the template or the Modelfile. `generation_config.json` does not set temperature, top_p, top_k, max_new_tokens, repetition_penalty, or do_sample. License is `cc-by-4.0`.

The inventory row matches: LoRA, dataset `israel/AfriGuard-inst`, parent `McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1`.
