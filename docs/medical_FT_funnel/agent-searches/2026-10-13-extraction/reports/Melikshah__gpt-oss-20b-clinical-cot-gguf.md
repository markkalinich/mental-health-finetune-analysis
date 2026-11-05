# Melikshah/gpt-oss-20b-clinical-cot-gguf

## Sources

https://huggingface.co/Melikshah/gpt-oss-20b-clinical-cot-gguf/raw/main/README.md — current model card; identical to the cached card
https://huggingface.co/api/models/Melikshah/gpt-oss-20b-clinical-cot-gguf — file list and parameter count
https://huggingface.co/Melikshah/gpt-oss-20b-clinical-cot-gguf/raw/main/config.json — architecture and context length
https://huggingface.co/Melikshah/gpt-oss-20b-clinical-cot-gguf/raw/main/generation_config.json — token ids and max length
https://huggingface.co/Melikshah/gpt-oss-20b-clinical-cot-gguf/raw/main/chat_template.jinja — Harmony chat template
https://github.com/TheDeadcoder/medical-cot-assistant — training pipeline linked from the card
https://github.com/unslothai/unsloth — library named on the card
https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — first training dataset
https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data — second training dataset
https://huggingface.co/datasets/UCSC-VLAA/MedReason — third training dataset
https://www.youtube.com/watch?v=IGAzB2DXqoM — demo linked from the card

## Record

Three datasets were merged. The card says they were "normalized to a unified instruction, reasoning, output schema," empty rows were dropped, and a 95% / 5% split was made. FreedomIntelligence/medical-o1-reasoning-SFT loads. The Hub page says 90,120 rows. Its card says "This dataset is constructed using GPT-4o" and lists English and Chinese. FreedomIntelligence/Medical-R1-Distill-Data loads. Its card says it is "distilled from Deepseek-R1" and does not state a row count. The language tags are English and Chinese, and the Chinese set is a separate repository. UCSC-VLAA/MedReason loads. Its card says "32,682 question-answer pairs" generated as reasoning paths over questions from 7 medical datasets. That provenance is mixed. The card does not name the language.

The objective is supervised fine-tuning, then a second quantization-aware stage. The card says "LoRA supervised fine-tuning (SFT) followed by quantization-aware training (QAT)." SFT is LoRA rank 32, alpha 64, learning rate 1e-4, 2 epochs, max length 4096. QAT is `int4_weight_only`, LoRA rank 16, alpha 32, learning rate 5e-5, 1 epoch. "A LoRA adapter was trained on the merged dataset and merged back into the base weights." `configs/gpt_oss_20b_sft.yaml` sets `load_in_4bit: false`, per-device batch size 8, and gradient accumulation 8. `configs/gpt_oss_20b_qat.yaml` also sets `load_in_4bit: false`, LoRA rank 16, and `qat_scheme: int4_weight_only`. That file lists `qat.learning_rate` 5e-5 and `train.learning_rate` 1e-4. The card states the QAT learning rate as 5e-5. Steps are not stated. The repository ships nine safetensors shards and four GGUF files, and no adapter file.

The parent is unsloth/gpt-oss-20b-BF16. The card says "21B total / 3.6B active parameters." The Hub API total is 20,914,757,184. The GitHub config names the same base. No paper names this repository.

The use claim is strong. The title is "Clinical Chain-of-Thought Medical Assistant," and the card says "Medical questions are answered with an explicit reasoning trace." The warning is a disclaimer. "It is not a medical device and is not intended to be used for diagnosis, treatment, or any clinical decision making." License is Apache 2.0. A GPT-5.2 judge on 50 questions gave the BF16 fine-tune 35 wins (70%) and a mean score of 9.16. The card says that sample is preliminary.

The purpose is stated. "This model is intended to be used for research into medical reasoning, for educational demonstrations, and for the study of chain-of-thought fine-tuning." The audience is a researcher or developer. "Clinical deployment is not supported."

The functions are answer medical questions, clinical reasoning, and suggest a diagnosis. The card says medical questions are answered with a reasoning trace, and the documented prompt is "What are the differential diagnoses for acute chest pain?"

The clinical tasks are medical question answering and a differential diagnosis. The specialty is general: the card says clinical and medical and does not name a field. The output is a reasoning trace inside `<think>` tags and then a final answer.

The examples are text only. `chat_template.jinja` is present. If no identity is passed, it writes "You are ChatGPT, a large language model trained by OpenAI." The llama-cpp example uses temperature 0.6, top_p 0.95, and 512 new tokens, with `n_ctx=4096`. `config.json` sets `max_position_embeddings` to 131072. `generation_config.json` does not set a temperature.
