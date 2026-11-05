# Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking

## Sources

- `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/Jarvis1111__DoctorAgent-RL-SFT-1k-Thinking__2026-10-05.md` — cached model card, sha256 `e9148208fe206de12a58f06b08ed2233fda5fc8d61f0c5f544cdb58450c74ace`
- `https://huggingface.co/Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking/raw/main/README.md` — current card; same bytes as the cache
- `https://huggingface.co/api/models/Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking` — file list; base model `Qwen/Qwen2.5-7B-Instruct`; no dataset field
- `https://huggingface.co/Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking/raw/main/config.json` — Qwen2, context 32768, dtype float32
- `https://huggingface.co/Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking/raw/main/generation_config.json` — sampling defaults
- `https://huggingface.co/Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking/raw/main/tokenizer_config.json` — Qwen chat template
- `https://github.com/JarvisUSTC/DoctorAgent-RL/blob/main/README.md` — names this repository as the SFT model
- `https://github.com/JarvisUSTC/DoctorAgent-RL/blob/main/sft/finetune_lora_med.sh` — published SFT command
- `https://github.com/JarvisUSTC/DoctorAgent-RL/blob/main/sft/utils/merge_lora.py` — merges a LoRA into a full model
- `https://github.com/JarvisUSTC/DoctorAgent-RL/blob/main/DATASET.md` — where the parquet files sit
- `https://github.com/JarvisUSTC/DoctorAgent-RL/blob/main/data/MTMedDialog_sft_train.parquet` — SFT file, 5,516 rows
- `https://arxiv.org/html/2505.19630v2` — paper HTML; Table 3 has the SFT-only scores
- `https://arxiv.org/html/2505.19630v3` — later HTML; same SFT hyperparameters; does not print this repository id
- `https://huggingface.co/papers/2505.19630` — paper page linked from the card
- `https://huggingface.co/collections/Jarvis1111/doctoragent-rl-684ffbcade52305ba0e3e97f` — collection linked from the card

## Record

The training file is `MTMedDialog_sft_train.parquet` in the GitHub repository. It is not a Hub dataset. The file has 5,516 rows. The README says: "For Supervised Fine-Tuning (SFT) cold start, we use the `MTMedDialog_sft_train.parquet` dataset. This dataset was created by prompting DeepSeek-V3 to generate the thinking process for each sample." The paper says the authors "randomly select 1,000 multi-turn consultation dialogues" and add a thought process to each doctor query with DeepSeek-V3. The full MTMedDialog set is "8,086 training samples and 2,082 test samples" taken from IMCS-21, CHIP-MDCFNPC, and MedDG. Those sources "were collected from real doctor-patient conversations" and "translated into English using DeepSeek-V3." The rows are English. A row's response looks like `<think> ... </think>` then `<answer>Question: ...</answer>`. Provenance is mixed: human consultations, machine translation, and a synthetic thinking trace.

This checkpoint is the supervised fine-tune, not the reinforcement-learning model. GitHub says "DoctorAgent-RL-SFT-1k-Thinking (Our SFT Model)" and "DoctorAgent-RL (Our RL Model)". The paper's first stage is supervised fine-tuning with LoRA in LLaMA-Factory. Its hyperparameter table lists learning rate 1e-4, batch size 64, 3 epochs, and `lora_rank` 8. It does not state LoRA alpha. The script `sft/finetune_lora_med.sh` is a different command: LoRA rank 64, alpha 32, train batch size 128, micro-batch 8, the same learning rate and 3 epochs, `target_modules=all-linear`, then `merge_and_unload` into a local directory `DoctorLLM-7B-SFT-1000-thinking`. The paper's second stage is group relative policy optimization for the RL model. This repository has full `safetensors` files and no `adapter_config.json`. The script merges locally. Nothing says this upload is that merge. Nothing says the base was quantized. The license is `apache-2.0`.

The parent is `Qwen/Qwen2.5-7B-Instruct` on the card, in the GitHub model list, and in the paper ("built upon Qwen2.5-7B-Instruct"). The card does not state a parameter count. The Hub page labels the repository 8B.

The use claim is strong. The card's example is a patient describing a cough, and the comment says "Continue the conversation as needed to reach a diagnosis or provide advice." The training prompt says: "You are an experienced doctor who needs to provide professional diagnosis and advice to patients through consultation." No sentence forbids diagnosis, treatment, or clinical use. The warning strength is none.

A purpose is stated: multi-turn clinical dialogue. The example is a patient speaking. The paper also says the system can "provide doctors with interpretable decision support" and support "patient-led symptom screening."

The doctor prompt and the paper claim five functions: talking with a patient, clinical reasoning, a diagnosis, treatment advice, and initial screening in "emergency triage scenarios."

The clinical work is a consultation, a diagnosis, a recommendation, and triage. The specialty is general medicine. The card says "medical consultations" and does not name one field. The paper scores eight disease categories. Those are evaluation categories. The card states no scores. In arXiv HTML v2, Table 3 gives the SFT-only row (`w/o RL`) an average score of 47.4 and 9.0 average turns. The same table gives DoctorAgent-RL 53.9. HTML v3 says the SFT-only ablation is 6.5% lower than 53.9 and does not reprint 47.4. GitHub assigns the RL checkpoint to `Jarvis1111/DoctorAgent-RL`.

It is a text chatbot. The card prints Patient and Doctor turns. The training targets are a thinking trace and then an answer. A chat template is present. The doctor prompt above is the system text in the training rows. If no system message is passed, the tokenizer inserts "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." `generation_config.json` sets temperature 0.7, top_k 20, top_p 0.8, do_sample true, and repetition_penalty 1.05. The card example also sets `max_new_tokens=512`, but it loads `Jarvis1111/DoctorAgent-RL`. Model context in `config.json` is 32,768 tokens.
