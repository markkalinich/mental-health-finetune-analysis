# taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA

## Sources

- https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/raw/main/README.md — current model card; byte-identical to the 10 Oct cache (`692edc1c93afcab93f6d195031d0d2705221db7bb55cfb9f023d2dfe5ac00198`)
- https://huggingface.co/api/models/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA — file list; BF16 safetensors count 8,030,261,248
- https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/raw/main/config.json — LlamaForCausalLM, context 131072, bfloat16
- https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/raw/main/generation_config.json — temperature 0.6, top_p 0.9, do_sample true
- https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/raw/main/tokenizer_config.json — no chat_template key; model_max_length 131072
- https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/raw/main/chat_template.jinja — Llama 3.1 chat template
- https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/raw/main/adapter/adapter_config.json — DoRA, rank 128, alpha 256, base Llama-3.1-8B-Instruct
- https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/raw/main/training_config.yaml — teacher, student, and data-mix settings
- https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA/raw/main/training_metrics.json — training loss and token accuracy
- https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options — MedQA dataset; viewer loads
- https://huggingface.co/datasets/qiaojin/PubMedQA — PubMedQA dataset; viewer loads
- https://arxiv.org/abs/2605.28301 — different medical CoT-distillation paper; does not name this repo
- https://arxiv.org/abs/2009.13081 — MedQA paper, cited by the dataset card; not read
- https://arxiv.org/abs/1909.06146 — PubMedQA paper, cited by the dataset card; not read
- https://github.com/tayden1990 — author profile linked from the card; no training repo for this model
- https://wandb.ai/taherakbarisaeed-kartalol/MatrusMedAI/runs/412ky1ao — W&B run linked from an earlier README commit, not the current card

## Record

The card says the training set is "1,101 teacher-generated CoT reasoning samples" from three sources: MedQA (USMLE) about 1,000, a hematology corpus of about 51 textbook or PDF questions, and PubMedQA about 50. Train/validation split is 1,046 / 55. `GBaker/MedQA-USMLE-4-options` and `qiaojin/PubMedQA` both load. The hematology corpus has no Hub id. The reasoning text is teacher-generated. `training_config.yaml` also lists `image_reasoning.jsonl` at weight 0.15. That row is not in the card's 1,101-sample table.

The objective is distillation. "Chain-of-Thought distillation from DeepSeek-R1-Distill-Llama-8B teacher." The update is DoRA, which the card calls "4-bit QLoRA": rank 128, alpha 256, 3 epochs, learning rate 2e-4, effective batch 32 (8 × 4), 99 steps. `adapter/adapter_config.json` has `use_dora` true and the same rank and alpha. The student block in `training_config.yaml` sets bf16 and does not set `load_in_4bit`. The 4-bit block in that file is on the teacher. The repo contains both `adapter/adapter_model.safetensors` and a full BF16 `model.safetensors`. The card does not say the uploaded weights are already merged. It shows `merge_and_unload` as a load step.

The parent is `meta-llama/Llama-3.1-8B-Instruct`. The card table and `adapter_config.json` both say that. The teacher is `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`, which is not the parent. No paper names this repo. arXiv 2605.28301 is a different Qwen3 medical-distillation study.

The use claim is strong. The usage example sets the system prompt "You are a specialist hematology assistant." The warning is a disclaimer: "Not for clinical use." It does not say "must not" or "do not use." The purpose is stated: a hematology study tool, CoT-distillation research, and a "clinical decision support system proof-of-concept." Audiences named are learners and researchers.

The card claims step-by-step clinical reasoning, USMLE-style exam questions, PubMedQA literature questions, hematology answers, a study tool, and a decision-support prototype. The three-question comparison also shows a diagnosis (AHTR) and a management step (IV hydration and DAT). Those two are evaluation examples. The written output is reasoning inside `<think>` tags and then an answer.

The specialty is hematology and blood transfusion medicine. The usage question is text: "What are the lab findings in iron deficiency anemia vs thalassemia trait?" Context length in `config.json` is 131,072. Training max length is 4,096. Generation settings are temperature 0.6, top_p 0.9, do_sample true, and the example uses max_new_tokens 1024. The license on the current card is Apache 2.0.

The inventory method and parent match. The inventory datasets omit the hematology corpus. The card and the training yaml disagree on whether the student was 4-bit.
