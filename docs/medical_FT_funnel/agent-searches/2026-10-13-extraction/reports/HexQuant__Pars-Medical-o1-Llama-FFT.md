# HexQuant/Pars-Medical-o1-Llama-FFT

## Sources

- `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/HexQuant__Pars-Medical-o1-Llama-FFT__2026-10-10.md` — cached model card, sha256 `e6b46d4b204373bfb52f6ff4407e0e2879abd10cfe40556a6e1a8a724f58ba2e`
- `https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT/raw/main/README.md` — current card; same bytes as the cache
- `https://huggingface.co/api/models/HexQuant/Pars-Medical-o1-Llama-FFT` — repository file list and card metadata
- `https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT/raw/main/config.json` — architecture, context length, dtype, Unsloth stamp
- `https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT/raw/main/generation_config.json` — sampling defaults
- `https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT/raw/main/tokenizer_config.json` — tokenizer; no `chat_template` key
- `https://huggingface.co/HexQuant/Pars-Medical-o1-Llama-FFT/raw/main/chat_template.jinja` — Llama 3 chat template
- `https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT` — English medical reasoning dataset named on the card; it loads
- `https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT/raw/main/README.md` — dataset card; GPT-4o construction
- `https://datasets-server.huggingface.co/size?dataset=FreedomIntelligence/medical-o1-reasoning-SFT` — row counts by config
- `https://huggingface.co/datasets/erfan226/persian-medical-qa` — named on the card; datasets server says it does not exist or is not public
- `https://huggingface.co/datasets/SeyedAli/Persian-Medical-Dataset` — named on the card; datasets server says it does not exist or is not public
- `https://github.com/xPOURY4` — profile linked from the card; returned 404
- `https://arxiv.org/abs/2412.18925` — cited by the medical-o1 dataset card for HuatuoGPT-o1; not read; it does not name this repository

## Record

The card trains on three sets. It lists `medical-o1-reasoning-SFT` as English, about 40,000 samples; `persian-medical-qa` as Persian, about 5,000; and `Persian-Medical-Dataset` as Persian, about 3,000. It also says "48K+ Samples". `FreedomIntelligence/medical-o1-reasoning-SFT` loads. Its card says: "This dataset is constructed using GPT-4o, which searches for solutions to verifiable medical problems and validates them through a medical verifier." The Hub English config has 19,704 rows. English plus Chinese medical configs have 39,875 rows. The card's "~40,000" English figure matches that sum, not the English split alone. `erfan226/persian-medical-qa` and `SeyedAli/Persian-Medical-Dataset` did not load. A search did not find public cards for those two ids. Their language and size are only the model's table.

The update is a full fine-tune. The card says "Full Fine-Tune - Not LoRA/adapter" and "Method | Full Fine-Tune (FFT)", in BF16, with Unsloth and Transformers, on an NVIDIA A100 80GB, context length 4096. It does not name a loss. SFT appears only inside a dataset id, so the objective is not stated. No epochs, steps, learning rate, or batch size are given. `config.json` has `dtype` `bfloat16` and `unsloth_version` `2025.12.7`. There is no adapter file. The license line is `apache-2.0`.

The parent on the card YAML is `unsloth/Llama-3.2-3B-Instruct`. The training table writes `Llama-3.2-3B-Instruct` without the `unsloth/` organization. No paper or training script names the parent. The card says "3B Parameters".

The use claim is strong. The card says "Clinical Focus - Diagnosis & treatment", and the English example ends in "Likely Diagnosis: Hypothyroidism" plus a recommended workup. The Persian example recommends "آسپرین ۳۲۵ میلی‌گرم". The warning is a disclaimer, not a prohibition: "This model is for educational and research purposes only" and "Not a substitute for professional medical advice." It also says to consult a qualified healthcare provider. The top of the card says this beta "does not have the ability to correctly respond to or handle local runs on its own."

A purpose is stated: educational and research use, and a clinical focus on diagnosis and treatment. No audience is named. "Educational and research purposes" does not name a researcher, a student, a patient, or a clinician.

The card claims three functions: step-by-step clinical reasoning ("Chain-of-Thought - Step-by-step reasoning"), a diagnosis ("Likely Diagnosis: Hypothyroidism"), and treatment ("Clinical Focus - Diagnosis & treatment").

The clinical work on the card is a differential, treatment or medication advice, and medical questions. The examples are a chest-pain case and a hypothyroidism case. The quick start asks "علائم دیابت نوع ۲ چیست؟". The specialty is general medicine. The card says "medical" and "clinical" and does not name a field. No evaluation numbers are reported.

It is a text chatbot. The usage example sends one user string and calls `model.generate`. The printed answers are a `<think>` trace and then a diagnosis, so the output is a reasoning trace plus an answer, in a chat turn. A chat template file is present. The card sets no system prompt. `generation_config.json` has `temperature` 0.6, `top_p` 0.9, and `do_sample` true. The model's `max_position_embeddings` is 131072. The card's training context is 4096 tokens. The card's own generate call uses `max_new_tokens=512` and `temperature=0.7`.
