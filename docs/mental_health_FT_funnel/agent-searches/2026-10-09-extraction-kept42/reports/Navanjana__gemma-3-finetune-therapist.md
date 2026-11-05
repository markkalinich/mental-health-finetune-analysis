# Navanjana/gemma-3-finetune-therapist

## Sources

https://huggingface.co/Navanjana/gemma-3-finetune-therapist/raw/main/README.md — current model card; same bytes as the cached card
revision_3_experiments/hf_inventory/cache/readmes/Navanjana__gemma-3-finetune-therapist__2026-10-09.md — cached card, sha256 c144a039fb3e679946a676c9705084106d62784ab48a0ddf4a2c3e9f400c4af2
https://huggingface.co/api/models/Navanjana/gemma-3-finetune-therapist — file list and safetensors parameter count
https://huggingface.co/Navanjana/gemma-3-finetune-therapist/raw/main/config.json — architecture, context length, Unsloth save stamp
https://huggingface.co/Navanjana/gemma-3-finetune-therapist/raw/main/tokenizer_config.json — chat template key; use_default_system_prompt false
https://huggingface.co/Navanjana/gemma-3-finetune-therapist/raw/main/chat_template.jinja — Gemma chat template
https://huggingface.co/unsloth/gemma-3-270m-it/raw/main/README.md — parent card; text input, images listed only for larger sizes
https://huggingface.co/datasets/IINOVAII/therapy-conversations-combined — dataset page; README is language and license only
https://huggingface.co/datasets/IINOVAII/therapy-conversations-combined/raw/main/README.md — dataset YAML: language en, license mit
https://datasets-server.huggingface.co/size?dataset=IINOVAII/therapy-conversations-combined — 208,548 rows
https://datasets-server.huggingface.co/first-rows?dataset=IINOVAII/therapy-conversations-combined&config=default&split=train — columns instruction, input, output
https://github.com/unslothai/unsloth — library link in the card footer, not a training repository for this checkpoint
https://huggingface.co/mradermacher/gemma-3-finetune-therapist-GGUF — quantized copy of this repository; no training details

## Record

The card names one dataset, `IINOVAII/therapy-conversations-combined`. The Hub page says 208,548 rows, and the dataset loads. The dataset README states language `en` and license `mit`. It does not say whether the text is human or synthetic. Columns are `instruction`, `input`, and `output`. The first instruction is "If you are a licensed psychologist, please provide this patient with a helpful response to their concern."

No source states a loss, a LoRA rank, epochs, a learning rate, or a batch size. The card says "Finetuned from model" and then the Unsloth sentence "trained 2x faster with Unsloth and Huggingface's TRL library." That sentence is the standard Unsloth upload note. It is not a training recipe. The repository has `model.safetensors` and no `adapter_config.json`. `config.json` records `unsloth_version` `2025.10.12`. That shows Unsloth saved the file. It does not say whether the update was full weights or LoRA.

The only parent statement is on the card: "Finetuned from model : unsloth/gemma-3-270m-it". No paper or training script restates it. The Hub safetensors total is 268,098,176 parameters.

The card title is "Uploaded finetuned model". It does not say the model is a chatbot, a classifier, or a tool. Output type is not listed. The card also does not describe a use. The repository id contains `therapist`, and the study counts that as a strong therapy claim when the card has no description. There is no warning sentence.

The parent card says input is a "Text string, such as a question, a prompt, or a document to be summarized", and it lists images only for the 4B, 12B, and 27B sizes. This repository's architecture is `Gemma3ForCausalLM`. A chat template is present. No system prompt is set. `generation_config.json` is not in the repository. `config.json` sets `max_position_embeddings` to 32768. License on the model card is `apache-2.0`. No evaluation is reported.
