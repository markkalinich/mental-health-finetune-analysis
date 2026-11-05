# MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered

## Sources

- https://huggingface.co/MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered/raw/main/README.md — current model card; byte-identical to the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/MihaiPopa-1__Stentor-30M-Instruct-heretic-safety-defiltered__2026-10-09.md — cached card, sha256 bc64a7a170a89348baf1f5494388f509c286dcda92a03e85f27b7dcdeb81dada
- https://huggingface.co/api/models/MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered — file list and safetensors parameter total
- https://huggingface.co/MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered/raw/main/config.json — Llama config, 512-token positions, float32
- https://huggingface.co/MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered/raw/main/generation_config.json — no sampling settings
- https://huggingface.co/MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered/raw/main/chat_template.jinja — chat template
- https://github.com/p-e-w/heretic — Heretic README; censorship removal by directional ablation, not post-training
- https://github.com/ggerganov/llama.cpp — conversion recipe copied in the card; not training code for this checkpoint
- https://arxiv.org/html/2512.13655v1 — abliteration-tool comparison; does not name this repo
- https://huggingface.co/datasets/PKU-Alignment/BeaverTails — human-labeled safety QA; viewer loads; 300,567 train and 33,396 test rows in the 330k split
- https://huggingface.co/datasets/AmazonScience/FalseReject — over-refusal set; 15,811 examples; prompts generated, test set human-annotated, training answers from LLMs
- https://huggingface.co/datasets/databricks/databricks-dolly-15k — human-written instructions; 15,011 rows
- https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu — educational web text; default train split 1,525,223,056 rows
- https://huggingface.co/datasets/HuggingFaceTB/smollm-corpus — Cosmopedia v2 config, 39,134,000 synthetic documents

## Record

The card names BeaverTails, FalseReject, Dolly-15k, hand-crafted Seed Safety, and a 512-pair concise Q&A set, plus FineWeb-Edu and Cosmopedia v2. Those sentences sit in a pasted Stentor-30M-Instruct write-up. That write-up says the pretraining sets were "inherited from Stentor-30M — not retrained here," and it assigns the other sets to a five-phase supervised curriculum. No Hub dataset exists for Seed Safety or the concise Q&A pairs. The main-mix table counts 7,125 FalseReject, 5,708 BeaverTails, 5,153 Dolly, and 14 Seed Safety rows. The phase table also says 100 seed-safety examples. BeaverTails is human-labeled. FalseReject mixes generated prompts and LLM answers with a human-annotated test set. Dolly is human-written. Cosmopedia v2 is synthetic. FineWeb-Edu is filtered web text.

This checkpoint was "made using Heretic v1.2.0." Heretic removes refusal directions from existing weights. It is not SFT, DPO, PPO, RLHF, or distillation, so the objective is not stated. The card prints abliteration settings (direction index per layer; attention and MLP weight kernels) and does not state LoRA rank, epochs, steps, learning rate, or batch size for this edit. The pasted write-up does say "LoRA adapters (r=32, α=32) were trained... and then merged" and "No RLHF. Trained with supervised fine-tuning only." Those sentences describe Stentor-30M-Instruct. The code samples load `StentorLabs/Stentor-30M-Instruct`. This repo has `model.safetensors` and no `adapter_config.json`.

The card's parent is StentorLabs/Stentor-30M-Instruct. The YAML `base_model` field says the same thing. No paper or GitHub README names this repository. The pasted body says Stentor-30M-Instruct is a fine-tune of Stentor-30M. That is the parent's parent.

The card presents a chat model: "useful for simple chat interactions, not a capable general-purpose assistant." It does not claim therapy, counseling, or emotional support. The limitation it states is "a research / edge-deployment checkpoint, not a production assistant," plus weak safety generalization and a 512-token context. It does not forbid therapy or medical use. The copied system prompt tells the model, for self-harm intent, to "respond with empathy" and mention 988. That is a refusal script in the pasted training section, not a warning that users must not use the model for support.

Serving is text-only. The quick start tokenizes a system message and a user question and calls `generate` with temperature 1.1, top_p 0.6, max_new_tokens 80, repetition_penalty 1.3, and do_sample true. Context length in `config.json` is 512. A separate `chat_template.jinja` wraps user text in `[INST]`. The card says every training example was prepended with a five-rule safety system prompt. License is Apache-2.0. The card states about 30.4M parameters. The Hub file total is 30,419,712. For this file versus the original, the card reports KL divergence 0.0739 and 2 refusals out of 100, against 9 out of 100 for Stentor-30M-Instruct.
