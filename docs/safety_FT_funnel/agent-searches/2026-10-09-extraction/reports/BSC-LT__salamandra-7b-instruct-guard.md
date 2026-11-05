# BSC-LT/salamandra-7b-instruct-guard

## Sources

https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/README.md — current model card; identical to the cached card (sha256 c0bb9f61392e5afc0faf0dbca64b4f4b1f191a67ea8deec4c00eaf9c77380379)
https://huggingface.co/api/models/BSC-LT/salamandra-7b-instruct-guard — file list, parameter count, and tokenizer chat template
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/config.json — LlamaForCausalLM, context 8192, parent path
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/generation_config.json — sampling settings
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/salguard_binary/adapter_config.json — binary LoRA rank, alpha, and targets
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/salguard_multilabel/adapter_config.json — multiclass LoRA rank, alpha, and targets
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/salguard_binary/README.md — binary adapter card, including 4-bit training
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/salguard_multilabel/README.md — multiclass adapter card, same training settings
https://huggingface.co/datasets/BSC-LT/salamandra-guard-dataset — training dataset card; the viewer loaded rows
https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3 — source set named for the translated slice; the viewer loaded rows
https://huggingface.co/api/datasets/alinia/salguard_proofread_override_10k — adapter training set; request returned 401
https://huggingface.co/datasets/BSC-LT/salamandra-guard-dataset/blob/main/Salamandra_Guard_Technical_Report.pdf — linked technical report; PDF not downloaded
https://arxiv.org/abs/2502.08489 — Salamandra base-model report; it does not print this repository id
https://github.com/langtech-bsc/salamandra — base-model pretraining repository
https://langtech-bsc.gitbook.io/alia-kit/modelos/modelos-de-texto — ALIA Kit page that names this model as content moderation

## Record

The top card says the model was trained on a combined set of 21,335 observations: 5,016 human-annotated Catalan and Spanish samples, and 16,319 machine-translated, LLM-annotated samples from Nemotron-Safety-Guard-Dataset-V3. The Hub dataset BSC-LT/salamandra-guard-dataset states that same total and loaded in the viewer. Its card says the 5,016 are human-annotated and the 16,319 are GPT-4o translations with LLM labels, so the set is mixed. nvidia/Nemotron-Safety-Guard-Dataset-v3 loaded and states about 514,617 synthetic samples. Both adapter READMEs in this repository say the adapters were fine-tuned on alinia/salguard_proofread_override_10k. That dataset page returned 401, so it did not load, and no row count was readable. The id's "10k" is not a count.

The top card says the training objective is "Binary classification and multiclass classification," with loss "Cross-entropy (single-label) / CausalLM (generative classification)." Both adapter READMEs say the same thing more narrowly: a causal language model trained to emit a label, with loss only on the label tokens, and "4-bit quantized base weights, QLoRA-style." Both adapter configs set r = 32 and lora_alpha = 64, and target q_proj, k_proj, and v_proj. The adapters are separate files, not merged. The READMEs state 3 epochs, learning rate 5e-5, and per-device batch size 2. They do not state a total step count. The top card says "LoRA (Low-Rank Adaptation) applied to all attention layers," which is wider than the q, k, and v targets in the adapter configs.

The YAML base model and both adapter configs name BSC-LT/salamandra-7b-instruct. The prose line says "Finetuned from model: bsc/salamandra-7b-instruct." config.json `_name_or_path` is BSC-LT/salamandra-7b-instruct. The card says "7 billion parameters." The Hub file list reports 7,768,117,248 BF16 parameters for the base shards. License is Apache 2.0. Languages on the top card are Catalan, Spanish, and English.

This is a safety classifier, not a support conversation. The card says it "classifies text content across multiple safety categories." The adapter cards say "This model is not intended for: Legal, medical, or psychological decision-making."

The top-card example classifies a text string and does not pass an image. generation_config.json sets do_sample true, temperature 0.6, and repetition_penalty 1.2. config.json sets max_position_embeddings to 8192. The root chat template's default system text begins "You are Salamandra, a language model developed by the Language Technology Unit at the Barcelona Supercomputing Center." The adapter examples instead prepend a classification rubric and generate with do_sample false. The top card reports binary weighted F1 0.797 and multiclass weighted F1 0.731 on 722 SalGuard_10k test samples.
