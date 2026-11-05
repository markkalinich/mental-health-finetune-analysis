# Kerassy/Granite-4.1-3B-Medical_Reasoning

## Sources

- `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/Kerassy__Granite-4.1-3B-Medical_Reasoning__2026-10-10.md` — cached model card, sha256 `f0ea0f03aaf67500c5ff06cdec4b54daf062bbf0122a34ce36b9b5d4bd4a6329`
- `https://huggingface.co/Kerassy/Granite-4.1-3B-Medical_Reasoning/raw/main/README.md` — current card; same bytes as the cache
- `https://huggingface.co/api/models/Kerassy/Granite-4.1-3B-Medical_Reasoning` — file list
- `https://huggingface.co/Kerassy/Granite-4.1-3B-Medical_Reasoning/raw/main/config.json` — Granite architecture, context, Unsloth stamp
- `https://huggingface.co/Kerassy/Granite-4.1-3B-Medical_Reasoning/raw/main/generation_config.json` — generation defaults
- `https://huggingface.co/Kerassy/Granite-4.1-3B-Medical_Reasoning/raw/main/tokenizer_config.json` — tokenizer and chat template
- `https://huggingface.co/Kerassy/Granite-4.1-3B-Medical_Reasoning/raw/main/chat_template.jinja` — Granite chat template
- `https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT` — named training dataset; it loads
- `https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT/raw/main/README.md` — dataset card; GPT-4o construction; configs en, zh, en_mix, zh_mix
- `https://github.com/unslothai/unsloth` — Unsloth library linked as the fine-tuning framework, not a training script for this checkpoint
- `https://github.com/Kerassy` — author profile; the public repository list was empty

## Record

The card names one training set: `FreedomIntelligence/medical-o1-reasoning-SFT`, "Subset: `-EM`, Split: `Train`". That dataset loads. Its configs are `en`, `zh`, `en_mix`, and `zh_mix`. There is no config named `-EM`. The English config has 19,704 rows. The dataset card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." The card does not state how many rows this fine-tune used. The card's language list is English.

The update is LoRA. The card says "Fine-Tuning Framework: Unsloth (LoRA fine-tuning)" on one NVIDIA A100 with 40GB. It says "fine-tuned" and "chain-of-thought (CoT) fine-tuning". It does not name a loss. SFT appears only inside the dataset id. No rank, alpha, epochs, learning rate, or batch size are given. `config.json` has `unsloth_version` `2026.8.9` and `dtype` `bfloat16`. The repository is two safetensors shards and has no `adapter_config.json`. Nothing says whether a LoRA was merged, or whether the base was quantized. The license is `apache-2.0`. Evaluation is the word "TBC."

The parent on the card is `ibm-granite/granite-4.1-3b`. `config.json` is `GraniteForCausalLM`. No paper or training script names the parent. The card says "3-billion parameter". The heading is `# Qwen3.5-9B-Medical-Reasoning`, and the tags include `qwen`. The usage example sets `model_path = "ibm-granite/granite-4.1-3b"`, which is the base, not this repository.

The use claim is strong. The card says the model generates "step-by-step diagnostic reasoning" and then "a final medical conclusion." The example asks "What is the most likely diagnosis?" The warning is an explicit prohibition: "should never be used for direct patient diagnosis, treatment advice, or real-world clinical decision-making." It also says the model is for research and evaluation only and is not a certified medical device.

A purpose is stated: "Medical research and evaluation of chain-of-thought capabilities in compact LLMs" and "AI-assisted clinical reasoning benchmark comparison and analysis." That names researchers. The vignette is a third-person case, not a patient speaking.

The card claims clinical reasoning, medical question-answering, and a diagnostic conclusion. The output it describes is a `<think>` trace and then a conclusion, produced from a chat turn. The clinical work is medical question-answering and a differential. The specialty is general. The card says "clinical" and "medical" and does not name a field.

The example is text only. A chat template is present. The card sets no system prompt. The only generation setting in the example is `max_new_tokens=100`. `generation_config.json` sets `max_length` 131072 and no temperature. `config.json` `max_position_embeddings` is 131072.
