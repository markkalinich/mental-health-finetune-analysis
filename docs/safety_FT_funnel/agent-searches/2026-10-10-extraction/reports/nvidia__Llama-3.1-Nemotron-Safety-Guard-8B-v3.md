# nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3

## Sources

- https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/README.md — current model card; identical to the cached card
- revision_3_experiments/hf_inventory/cache/readmes/nvidia__Llama-3.1-Nemotron-Safety-Guard-8B-v3__2026-10-09.md — cached card, sha256 0291e3be308ba2fd77be2b1262e6775a15dc7a0b66bebc80bf2e9ba98fc9f8f0
- https://huggingface.co/api/models/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3 — repository file list
- https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/config.json — Llama config, max position 131072
- https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
- https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/tokenizer_config.json — Llama 3.1 chat template
- https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/lora_adapter/adapter_config.json — LoRA rank 8, alpha 32, base meta-llama/Llama-3.1-8B-Instruct
- https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3/raw/main/inference_script.py — inference example, not a training script
- https://arxiv.org/abs/2508.01710 — CultureGuard abstract
- https://arxiv.org/html/2508.01710 — CultureGuard HTML full text; prints this repository id
- https://aclanthology.org/2025.ijcnlp-long.144/ — same paper at IJCNLP 2025
- https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3 — training dataset card; viewer loads
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0 — English source dataset named on the card
- https://huggingface.co/datasets/ToxicityPrompts/PolyGuardPrompts — evaluation set named on the card; public, test split 29,325 rows
- https://huggingface.co/datasets/ToxicityPrompts/RTP-LX — evaluation set named on the card; public
- https://huggingface.co/datasets/ToxicityPrompts/DAMO-MultiJail — evaluation set named on the card; public, test split 3,150 rows
- https://huggingface.co/datasets/ToxicityPrompts/XSafety — evaluation set named on the card; public, test split 27,999 rows
- https://huggingface.co/datasets/CohereLabs/aya_redteaming — evaluation set named on the card; public
- https://build.nvidia.com/nvidia/llama-3_1-nemotron-safety-guard-8b-v3 — NVIDIA NIM preview linked from the card

## Record

The training set named on the card is Nemotron-Safety-Guard-Dataset-v3 (`nvidia/Nemotron-Safety-Guard-Dataset-v3`). The CultureGuard paper says: "The resulting dataset, Nemotron-Safety-Guard-Dataset-v3, comprises 386,661 samples in 9 languages and facilitates the training of Llama-3.1-Nemotron-Safety-Guard-8B-v3 via LoRA-based fine-tuning." The card says data collection was "Hybrid: Automated, Human, Synthetic." The current dataset card, dated January 2026, says approximately 514,617 samples across 12 languages. That is larger than the 9-language set in the paper. The card also says English samples were taken from Nemotron Content Safety Dataset V2, which is `nvidia/Aegis-AI-Content-Safety-Dataset-2.0` (33,416 annotated human–LLM interactions, English). Both Hub datasets are public and have data files. The evaluation sets on the card are PolyGuardPrompts, RTP-LX, MultiJail, XSafety, and Aya Red-teaming. They are not training data.

The update is LoRA. The card says: "We perform Parameter Efficient FineTuning (PEFT) over the above base model" with rank 8, alpha 32, and modules `q_proj` and `v_proj`. The paper says: "Training is conducted for 5 epochs with a constant learning rate (LR) of 1e-5, a per-gpu batch size of 4, and distributed across 8 A100 GPUs with PyTorch FSDP enabled." No sentence names a loss. "Fine-tuned" and "LoRA" are not an objective, so the objective is not stated. The card says the LoRA adapter is provided separately. It does not say the adapter was merged into the four-shard root checkpoint. It does not say the base was quantized during training.

The parent is meta-llama/Llama-3.1-8B-Instruct. The card, `adapter_config.json`, and the paper all say Llama-3.1-8B-Instruct. The card says the model has 8.03B parameters.

The card presents a classifier, not a chatbot. It "classifies user prompts and LLM responses as safe or unsafe" and, if unsafe, returns violated categories. The input can be a user prompt, a user prompt plus an agent reply, or a conversation of one or more turns. The output is JSON with "User Safety" and, when a reply is present, "Response Safety" (`safe` or `unsafe`), plus "Safety Categories". That is a binary label, a category label, and a structured object. The detection claim covers both the user message and the assistant reply, so it is not only "detects harm in input" or only "judges a reply." The card's example taxonomy names 23 categories, from Violence and Sexual through Suicide and Self Harm, and says the names are not fixed: they follow the taxonomy in the instruction. The card's score table is Nemotron-Safety-Guard-Dataset-v3 85.32, PolyGuardPrompts 76.07, RTP-LX 91.49, MultiJail 95.36, XSafety 66.97, Aya Red-teaming 96.79. The license line is the NVIDIA Open Model License, with the Llama 3.1 Community License Agreement named as additional information.

Serving is text in, text out. The card says "Input Type(s): Text." `tokenizer_config.json` has a Llama 3.1 chat template. There is no `chat_template.jinja`. The template's default system preamble is "Cutting Knowledge Date: December 2023" and "Today Date: 26 Jul 2024". The safety instruction is the user message. `generation_config.json` sets do_sample true, temperature 0.6, and top_p 0.9. The card's example uses max_new_tokens 100. The card says context up to 8K. The config and tokenizer both set 131072, so no single max-context integer is filled.
