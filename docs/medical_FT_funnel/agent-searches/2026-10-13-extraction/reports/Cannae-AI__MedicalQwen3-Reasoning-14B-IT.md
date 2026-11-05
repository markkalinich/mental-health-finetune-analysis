# Cannae-AI/MedicalQwen3-Reasoning-14B-IT

## Sources

https://huggingface.co/Cannae-AI/MedicalQwen3-Reasoning-14B-IT/raw/main/README.md — current model card; same text as the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/Cannae-AI__MedicalQwen3-Reasoning-14B-IT__2026-10-10.md — cached card, sha256 edc9647ad6606f0f6d99f1b60eddca16fb88990eb306a6dee5623bd65365ff52
https://huggingface.co/api/models/Cannae-AI/MedicalQwen3-Reasoning-14B-IT — file list, safetensors parameter count, chat template
https://huggingface.co/Cannae-AI/MedicalQwen3-Reasoning-14B-IT/raw/main/config.json — architecture, context length, Unsloth flags
https://huggingface.co/Cannae-AI/MedicalQwen3-Reasoning-14B-IT/raw/main/tokenizer_config.json — chat template
https://huggingface.co/Qwen/Qwen3-14B/raw/main/README.md — parent card, text-only usage example
https://arxiv.org/abs/2505.09388 — Qwen3 Technical Report abstract
https://arxiv.org/html/2505.09388 — Qwen3 Technical Report HTML; does not name this repository
https://arxiv.org/abs/2412.18925 — HuatuoGPT-o1 paper, cited by the reasoning dataset; not read; does not name this repository
https://github.com/QwenLM/Qwen3 — parent code repository linked from the Qwen3 paper and parent card
https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — reasoning dataset card
https://datasets-server.huggingface.co/size?dataset=FreedomIntelligence/medical-o1-reasoning-SFT — row counts by config
https://huggingface.co/datasets/Mohammed-Altaf/medical-instruction-120k — instruction dataset card
https://huggingface.co/Cannae-AI/collections — MedicalLms collection blurb
https://featherless.ai/models/Cannae-AI/MedicalQwen3-Reasoning-14B-IT — hosted inference page that restates the card

## Record

The card names two datasets: FreedomIntelligence/medical-o1-reasoning-SFT and Mohammed-Altaf/medical-instruction-120k. Both load. The reasoning set's card says "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." The Hub counts 90,120 rows across four configs (en 19,704, en_mix 24,887, zh 20,171, zh_mix 25,358). The model card does not say which config was used. The instruction set's card says it "consists of various thoughs proposed by the people [mentioned as the Human ] and there responses" and that the author "used all the available opensource datasets and combined them." The Hub counts 112,165 rows. The MedicalLms collection says the fine-tunes used "radiological images from the PMC Open Subset," but that collection also holds a vision model, and this card does not name that image set.

The card says "This is a fine-tuned version of Qwen/Qwen3-14B." "Fine-tuned" does not name a loss. No sentence names full fine-tuning, LoRA, or QLoRA. The repository is full bfloat16 weights, with no adapter_config.json. config.json sets unsloth_fixed to true and unsloth_version to 2025.11.2, and a commit is titled "(Trained with Unsloth)." That is library boilerplate, not a training method. Epochs, steps, learning rate, and batch size are not stated.

The card says "Finetuned from model : Qwen/Qwen3-14B." No paper, config file, or GitHub repository states a parent for this checkpoint. The Qwen3 Technical Report describes Qwen3-14B and does not print this repository id.

The card says the model is "specifically optimized for medical instructions,reasoning and clinical decision-making" and was trained "to provide accurate medical responses." That is a clinical-decision claim, so the use claim is Strong. The card has no warning. The purpose is stated. No sentence names a patient, clinician, student, or researcher. The stated jobs are answering medical questions, clinical reasoning, and supporting a clinical decision. The output is a chat reply, and the same sentence says the model is for reasoning. The clinical work named is medical question answering and clinical decision-making, with no specialty narrower than medicine.

The parent card's example is a text prompt, "Give me a short introduction to large language model." This repository is Qwen3ForCausalLM, with a chat template and no generation_config.json. config.json sets max_position_embeddings to 40960. The license on the card is apache-2.0. The safetensors header counts 14,768,307,200 parameters. The card reports no evaluation. The inventory row matches the card: no method, the same two datasets, and parent Qwen/Qwen3-14B.
