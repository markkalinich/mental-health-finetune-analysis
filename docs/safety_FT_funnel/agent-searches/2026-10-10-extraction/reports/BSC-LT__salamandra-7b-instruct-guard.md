# BSC-LT/salamandra-7b-instruct-guard

## Sources

https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/README.md — current model card; byte-identical to the cached card (sha256 c0bb9f61392e5afc0faf0dbca64b4f4b1f191a67ea8deec4c00eaf9c77380379)
https://huggingface.co/api/models/BSC-LT/salamandra-7b-instruct-guard — repository file list and tokenizer chat template
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/config.json — LlamaForCausalLM config, parent id, context 8192
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/generation_config.json — temperature 0.6, repetition penalty 1.2, do_sample true
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/salguard_binary/adapter_config.json — LoRA r=32, alpha=64, parent id
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/salguard_multilabel/adapter_config.json — same LoRA settings for the multiclass adapter
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/salguard_binary/chat_template.jinja — default Salamandra system prompt
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/salguard_binary/README.md — binary adapter card; QLoRA and Alinia dataset
https://huggingface.co/BSC-LT/salamandra-7b-instruct-guard/raw/main/salguard_multilabel/README.md — multiclass adapter card; same training regime
https://huggingface.co/datasets/BSC-LT/salamandra-guard-dataset/raw/main/README.md — training dataset card, 21,335 rows, public parquet
https://huggingface.co/api/datasets/BSC-LT/salamandra-guard-dataset — dataset loads; train 20,329 and test 1,006
https://huggingface.co/datasets/nvidia/Nemotron-Safety-Guard-Dataset-v3/raw/main/README.md — source dataset named on the root card
https://huggingface.co/api/datasets/nvidia/Nemotron-Safety-Guard-Dataset-V3 — capital-V id resolves to the public v3 dataset
https://huggingface.co/datasets/alinia/salguard_proofread_override_10k — adapter training set; HTTP 401
https://huggingface.co/datasets/BSC-LT/salamandra-guard-dataset/blob/main/Salamandra_Guard_Technical_Report.pdf — guard report linked from the card; PDF not opened
https://arxiv.org/abs/2502.08489 — Salamandra family report found by the title search; HTML has no mention of this checkpoint
https://arxiv.org/html/2502.08489v2 — HTML of that family report, searched for this model name
https://langtech-bsc.gitbook.io/alia-kit/modelos/modelos-de-texto — ALIA Kit page that names this model
https://langtech-bsc.gitbook.io/aina-kit/models/models-de-text — Aina Kit page that names this model

## Record

The root card says the model was trained on 21,335 observations in BSC-LT/salamandra-guard-dataset: 5,016 human-annotated Catalan and Spanish samples and 16,319 machine-translated, LLM-annotated samples from Nemotron-Safety-Guard-Dataset-V3. That Hub dataset is public and the viewer splits sum to 21,335 (train 20,329, test 1,006). The dataset card's own prose table instead says train 17,068 and test 4,267. nvidia/Nemotron-Safety-Guard-Dataset-v3 loads and states 514,617 samples, "primarily synthetically generated". Both adapter cards say the fine-tune used alinia/salguard_proofread_override_10k. That page returned HTTP 401, so its size and provenance are not stated. The root card's test set name SalGuard_10k has no Hub dataset page.

The root card says "Training objectives: Binary classification and multiclass classification" and "LoRA (Low-Rank Adaptation) applied to all attention layers", learning rate 5e-5, 3 epochs, cross-entropy or causal language-model loss. Both adapter cards say the same objective as constrained label generation, and "Training regime: bf16 mixed precision (with 4-bit quantized base weights, QLoRA-style)", with 4-bit NF4, LoRA r=32, alpha=64, dropout 0.1, on q_proj, k_proj, and v_proj. Per-device batch size is 2 with gradient accumulation 4. No total step count is stated. The adapters are stored as separate files, so they are not merged. The root card does not mention quantization.

The card YAML, config.json, and both adapter configs name the parent BSC-LT/salamandra-7b-instruct. One prose line on the root card says "Finetuned from model: bsc/salamandra-7b-instruct". The card says "7 billion parameters". Languages on the root card are Catalan, Spanish, and English. The adapter cards list Spanish and Catalan as primary.

This is a classifier. The root card says "Model type: Text Classification (Safety Guardrail)". The usage example classifies a text string, and a second example classifies a user message plus an assistant reply. Outputs on that example are a class index (binary 0/1 or multiclass 0–3) and a softmax confidence. The binary adapter card says it "classifies assistant responses as Safe or Non-Safe", and the multiclass adapter emits C0, C1, C2, or C3. The root card says the model "focuses on moderating LLM responses". Named categories are dangerous content (violent crimes, gender-based and domestic violence, suicide and self-harm, non-violent crimes), toxic content (hate speech, harassment, bullying, doxxing, profanity), and sexual content. On 722 SalGuard_10k items the root card reports binary weighted F1 0.797 and multiclass weighted F1 0.731.

Serving is text only. config.json sets max_position_embeddings to 8192. generation_config.json sets do_sample true, temperature 0.6, and repetition_penalty 1.2. A chat template is present; its default system prompt is the Salamandra assistant prompt, not a guard rubric. The adapter examples instead prepend a classification rubric and generate with do_sample false. License is Apache-2.0. No GitHub repository is linked. The linked technical report is a PDF and was not opened. The Salamandra family arXiv paper (2502.08489) does not name this checkpoint.
