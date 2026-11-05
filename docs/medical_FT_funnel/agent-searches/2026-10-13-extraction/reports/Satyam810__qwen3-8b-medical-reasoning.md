# Satyam810/qwen3-8b-medical-reasoning

## Sources

https://huggingface.co/Satyam810/qwen3-8b-medical-reasoning/raw/main/README.md — current model card; identical to the 5 October 2026 cache (sha256 883c2c28b4e92b5d1ac6bc3677489b51fe52566e3ab2c4ec828def3bc5941833)
https://huggingface.co/api/models/Satyam810/qwen3-8b-medical-reasoning — file list and parameter count
https://huggingface.co/Satyam810/qwen3-8b-medical-reasoning/raw/main/config.json — architecture and context length
https://huggingface.co/Satyam810/qwen3-8b-medical-reasoning/raw/main/generation_config.json — sampling settings
https://huggingface.co/Satyam810/qwen3-8b-medical-reasoning/raw/main/tokenizer_config.json — chat template
https://huggingface.co/Satyam810/qwen3-8b-medical-reasoning/raw/main/chat_template.jinja — same chat template as a separate file
https://huggingface.co/Satyam810/qwen3-8b-medical-reasoning-lora/raw/main/adapter_config.json — sibling LoRA adapter (rank, alpha, quantized base)
https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT/raw/main/README.md — reasoning dataset card
https://datasets-server.huggingface.co/size?dataset=FreedomIntelligence/medical-o1-reasoning-SFT — row counts; the viewer loads
https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k — ChatDoctor dataset card; 112,165 rows; the viewer loads
https://arxiv.org/abs/2512.05658 — HTML full text of a different group's Qwen3-8B medical-reasoning paper; it does not name this repository
https://www.research.unipd.it/handle/11577/3609842 — EMNLP 2026 venue for that paper
https://github.com/unslothai/unsloth — library linked from the card, not a training script for this checkpoint
https://featherless.ai/models/Satyam810/qwen3-8b-medical-reasoning — hosted inference page that repeats the card

## Record

The card trains on two datasets, mixed 75% reasoning and 25% chat, then a shuffled subsample of 7,000 combined examples for one epoch. FreedomIntelligence/medical-o1-reasoning-SFT is the reasoning set. Its card says it "is constructed using GPT-4o", so the traces are synthetic, in English and Chinese configs. The Hub viewer loads it: 19,704 rows in the English medical config and 90,120 rows across four configs. The model card does not say which config was sampled. lavita/ChatDoctor-HealthCareMagic-100k is the chat set. The model card calls it "real patient questions paired with physician responses." The dataset card states 112,165 train examples and loads. It does not state a language.

Training is supervised fine-tuning. The card says "Framework: Unsloth + TRL `SFTTrainer`" and "Method: LoRA, rank 32" on "`unsloth/Qwen3-8B-unsloth-bnb-4bit` (4-bit quantized)". That is LoRA on a quantized base. The sibling repository Satyam810/qwen3-8b-medical-reasoning-lora has `adapter_config.json` with `"r": 32`, `"lora_alpha": 32`, and the same 4-bit base. This repository has four full weight shards and no adapter file, and the usage example loads `AutoModelForCausalLM` directly, so the adapter is merged here. The card states one epoch. It does not state the learning rate, batch size, or step count.

The card names two parents. The YAML says `base_model: Qwen/Qwen3-8B`. The first sentence says the fine-tune is of `unsloth/Qwen3-8B-unsloth-bnb-4bit`. The sibling adapter config repeats that Unsloth id. The inventory parent matches the YAML only.

The card presents a chatbot that gives a diagnosis in plain sentences. One comparison answer "read like a physician speaking directly to a patient". The intended-use sentence is "educational and research purposes" and "a small-scale student/hobby project, not a validated clinical tool." The warning forbids a use: "Do not use this model's output to make real medical decisions." It also says the model "is not a substitute for professional medical advice, diagnosis, or treatment."

The purpose sentence names students and research. It does not name patients or clinicians as the users. The patient-facing wording describes the answer style.

The card claims step-by-step clinical reasoning, conversational medical question answering, a correct diagnosis on five test questions, and answers that sound like a physician talking to a patient. The shown fine-tuned answer is a short conversational paragraph. The reasoning data are "step-by-step clinical reasoning traces and a final answer."

The work is general medical question answering, an informal five-question diagnosis check, and doctor-patient conversation from ChatDoctor. No specialty is named. MedQA is mentioned only as a benchmark the model was not run on.

The usage example sends one text question, "Describe the mechanism of action of metformin." A chat template is present and has no fixed medical system prompt. `generation_config.json` sets temperature 0.6, top_k 20, top_p 0.95, and do_sample true, with max length 40,960. The Hub file list reports 8,190,735,360 parameters. License is apache-2.0.

A name search finds arXiv 2512.05658 (EMNLP 2026). That paper releases NLP-FBK/Qwen3-8B-medical-reasoning. It does not print Satyam810/qwen3-8b-medical-reasoning.
