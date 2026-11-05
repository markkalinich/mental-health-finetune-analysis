# iamaber/mistral-7b-pubmedqa-lora-plus

## Sources

- https://huggingface.co/iamaber/mistral-7b-pubmedqa-lora-plus/raw/main/README.md — current model card; same text as the cached card
- https://huggingface.co/api/models/iamaber/mistral-7b-pubmedqa-lora-plus — file list, parameter count, and chat template
- https://huggingface.co/iamaber/mistral-7b-pubmedqa-lora-plus/raw/main/config.json — MistralForCausalLM, context 32768
- https://huggingface.co/iamaber/mistral-7b-pubmedqa-lora-plus/raw/main/generation_config.json — token ids only
- https://huggingface.co/iamaber/mistral-7b-pubmedqa-lora-plus/raw/main/chat_template.jinja — Mistral Instruct chat template, present in the file list and returned by the model API
- https://huggingface.co/iamaber/mistral-7b-pubmedqa-adapter/raw/main/adapter_config.json — paired adapter, LoRA rank 16 and alpha 32
- https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md — PubMedQA dataset card
- https://arxiv.org/abs/2310.06825 — Mistral 7B paper; does not name this repository
- https://arxiv.org/abs/1909.06146 — PubMedQA paper, linked from the dataset card; does not name this repository; not read in full
- https://github.com/iamaber/mistral-7b-instruct-finetune — same-author repository; the fetched page does not print this repository id
- https://github.com/pubmedqa/pubmedqa — dataset code, linked from the dataset card
- https://featherless.ai/models/iamaber/mistral-7b-pubmedqa-lora-plus — inference host page that prints this repository id

## Record

The card trains on `qiaojin/PubMedQA` / `pqa_labeled`. It lists 900 train examples and 100 eval examples. The dataset card's `pqa_labeled` config has 1,000 train rows. The dataset card says the task is to "answer research questions with yes/no/maybe" and that the language is English. Its YAML lists `annotations_creators` as both `expert-generated` and `machine-generated`, so provenance for the dataset as published is mixed. The Hub dataset card loads.

The card says: "This merged artifact fine-tunes `mistralai/Mistral-7B-Instruct-v0.3` on `qiaojin/PubMedQA` / `pqa_labeled` using LoRA+." "Fine-tunes" does not name a loss, so the objective is not stated. The update is LoRA. The card's training table gives 3 epochs, train batch size 4, gradient accumulation 4, learning rate 5e-05, and global step 171. This repository has no `adapter_config.json`. The paired adapter repository, with the same training table, has `"peft_type": "LORA"`, `"r": 16`, and `"lora_alpha": 32`. The card calls this file a merged artifact, and the upload is one full bfloat16 `model.safetensors`. Nothing states that the base was quantized during training.

The parent on the card is `mistralai/Mistral-7B-Instruct-v0.3`. The paired adapter records a local path, `/vol/pubmedqa-loraplus/base_model`, and its card names the same Hub parent. The Hub API reports 7,248,023,552 bfloat16 parameters. The inventory row matches: method lora, dataset `qiaojin/PubMedQA`, that parent. The card's word is LoRA+, which is still LoRA.

The card is a training log and a score table. It does not say who the model is for, so the use claim is Weak and the warning is None. No audience is named. Functions are empty because no purpose sentence is stated. The reported outputs are the labels yes, no, and maybe, so the output type is a classifier and the output kind is a label. Every one of the 100 PubMedQA predictions falls in the yes column.

The training task is exam answering: PubMedQA is named in the training sentence. Medical MMLU accuracy 0.1600 on 50 anatomy items is evaluation only; the other listed subjects have a total of 0. The specialty is general. The tag says medical and names no field. Licence is `apache-2.0`.

Serving is text only: `config.json` is `MistralForCausalLM`. A chat template is present and does not fix a system prompt. `generation_config.json` has no sampling settings. `max_position_embeddings` is 32768.
