# nvidia/Nemotron-Content-Safety-Reasoning-4B

## Sources

- https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/raw/main/README.md — current model card; identical to the cached card
- revision_3_experiments/hf_inventory/cache/readmes/nvidia__Nemotron-Content-Safety-Reasoning-4B__2026-10-09.md — cached card, sha256 74e8f1c6e22e56f6003e9c5645e3957eb19b0ff77be6677e853786a5660a9f63
- https://huggingface.co/api/models/nvidia/Nemotron-Content-Safety-Reasoning-4B — repository file list
- https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/config.json — Gemma 3 config, text context 131072
- https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/generation_config.json — do_sample, top_k 64, top_p 0.95
- https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/raw/main/chat_template.jinja — Gemma chat template
- https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/trainer_state.json — saved step 3900 of 8970
- https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/raw/main/latest — text file `global_step3900`
- https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/training_args.bin — DeepSpeed ZeRO-2 config path; no LoRA string
- https://arxiv.org/abs/2505.20087 — cited paper abstract
- https://arxiv.org/html/2505.20087 — paper HTML; does not print this repository id
- https://aclanthology.org/2025.findings-emnlp.1193/ — Findings of EMNLP 2025
- https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Reasoning-Dataset — training dataset; the Hub loader reports a column mismatch
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — English source of the safety labels
- https://huggingface.co/datasets/nvidia/CantTalkAboutThis-Topic-Control-Dataset — topic-control source; public
- https://github.com/openai/moderation-api-release — evaluation set linked from the card
- https://huggingface.co/datasets/allenai/xstest-response — evaluation set; gated
- https://huggingface.co/datasets/walledai/WildGuardTest — evaluation set; public
- https://huggingface.co/datasets/Bertievidgen/SimpleSafetyTests — evaluation set; public
- https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors — evaluation set; public
- https://huggingface.co/datasets/lmsys/toxic-chat — evaluation set; public
- https://huggingface.co/datasets/microsoft/CoSApien — evaluation set; public
- https://huggingface.co/datasets/dynamofl/DynaGuardrail — evaluation set; gated

## Record

The training set is `nvidia/Nemotron-Content-Safety-Reasoning-Dataset`. The dataset card says it "has been used to train the Nemotron-Content-Safety-Reasoning-4B guard model" and states 28,000 content-safety samples and 8,712 topic-control samples. The model card says "Approximately 36000 samples" and "Hybrid: Human, Automated" collection with "Hybrid: Human, Synthetic" labels. It also says the traces were extracted from Qwen3-32B, DeepSeek-R1-0528, and gpt-oss-120b, on labels from Nemotron Content Safety Dataset V2 (`nvidia/Aegis-AI-Content-Safety-Dataset-2.0`, 33,416 English interactions) and CantTalkAboutThis (`nvidia/CantTalkAboutThis-Topic-Control-Dataset`, synthetic English dialogues). The reasoning dataset page fails a single-table load: the two jsonl files have different columns. The card's config lists them as two splits.

The card says the model is "a finetuned version" of Gemma-3-4B-it. It does not name a loss, and it does not say full fine-tuning or LoRA. There is no `adapter_config.json`. `training_args.bin` points at `examples/deepspeed/ds_z2_config.json` and does not contain the string lora. `trainer_state.json` and the file `latest` both say global step 3900. The state also says epoch 2.17, max_steps 8970, num_train_epochs 5, train_batch_size 2, and a learning rate that peaks at 1e-6. The cited EMNLP paper's appendix is titled "Hyperparameters for SFT Experiments" and gives batch size 32, learning rate 1e-6, and 5 epochs, but the HTML does not name this repository. That paper's only "Nemotron" mention is a citation of the Nemotron-4 340B report. The objective and the update scope are not stated for this checkpoint.

The parent is google/gemma-3-4b-it. The card says 4 billion parameters. The language line is English.

The card calls it a classifier and a guardrail. The primary claim is policy following: "Users can bring their own safety policy." It also labels a user prompt and an optional assistant reply as harmful or unharmful. With `/think`, the output is a `<think>` trace and then the labels. With `/no_think`, it is only the labels. The example taxonomy has 22 categories, from Violence through Immoral/Unethical. Example 3 is a multi-turn customer-support conversation plus the current user message. The license is the NVIDIA Open Model License, plus the Gemma terms and prohibited-use policy.

Serving is text. The card says "Input Type(s): Text." The examples put the whole instruction in the user message. `generation_config.json` sets do_sample true, top_k 64, and top_p 0.95. The card's own generate call uses do_sample false and max_new_tokens 400. Context is 128K on the card and 131072 in the config.
