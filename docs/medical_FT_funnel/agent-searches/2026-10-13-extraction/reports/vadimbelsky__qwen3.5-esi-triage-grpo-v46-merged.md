# vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged

## Sources

- https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged/raw/main/README.md — current model card; byte-identical to the cached card (sha256 4e461070238de40644cef263e66db4979e22890d7db3200a0ca17e3ab8965bd9)
- https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46/raw/main/README.md — linked adapter card with the training method, data, and the prohibition
- https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46/raw/main/adapter_config.json — LoRA rank 32, alpha 32
- https://huggingface.co/api/models/vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged — file list, base-model tag, parameter count, chat template
- https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged/raw/main/config.json — Qwen3.5 config, context length, vision tower
- https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged/raw/main/generation_config.json — eos token only
- https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/spaces/vadimbelsky/medical-triage-demo — Gradio demo that lists this repo
- https://physionet.org/content/mimic-iv-ed/2.2/ — MIMIC-IV-ED dataset page
- https://physionet.org/content/mietic/1.0.0/ — MIETIC dataset page
- https://huggingface.co/datasets/jackf7499/MIETIC — public Hub copy of MIETIC

## Record

The adapter card, which this repo says holds the training method, states the data as "MIMIC-IV-ED gold (25K) + MIETIC narratives", with ESI-1 oversampled 5× and ESI-2 oversampled 3×. MIMIC-IV-ED is credentialed on PhysioNet and does not load as a public Hub dataset. MIETIC is 9,629 ESI-aligned cases; the Hub copy `jackf7499/MIETIC` loads. PhysioNet says those narratives were written by GPT-4o from MIMIC records. The same card says an earlier v43 SFT warm-start used about 26K chain-of-thought examples from MIMIC-IV-ED gold labels. That warm-start is a prior checkpoint, not this GRPO run.

This checkpoint was trained with GRPO. The adapter card says "Method: GRPO (Group Relative Policy Optimization) via TRL" and "LoRA: r=32, α=32". `adapter_config.json` matches rank 32 and alpha 32, on the attention and MLP projections. The run was 750 steps, learning rate 8e-7, effective batch 8 (per-device 1, gradient accumulation 8). Epochs are not stated. The optimizer is `adamw_8bit`; the card does not say the base was quantized. This repo is the merge: "The LoRA adapter weights from vadimbelsky/qwen3.5-esi-triage-grpo-v46 have been merged directly into the Qwen3.5-9B base model used during training."

The parent on the card and the Hub tag is `Qwen/Qwen3.5-9B`. The adapter config stores the local path `models/Qwen3.5-9B`. The title says 9B. The Hub safetensors total is 9,409,813,744 BF16 parameters.

The model classifies emergency-department triage narratives into ESI levels 1–5. That is a strong use claim. The adapter card forbids clinical use: "must not be used to make actual triage decisions for patients." The merged card's own line is shorter: "This is a research model. Not approved for clinical use."

The purpose is ESI triage. The merged card addresses someone deploying a model ("exact behavior reproduction", "easier deployment"). The adapter card says it is a research model and forbids actual triage decisions.

It extracts clinical fields, walks the ESI algorithm, and states an ESI level. The example ends in "ANSWER: ESI 1". The task is triage. The field is emergency medicine. Reported result: "77.8% exact accuracy / 94.4% adjacent accuracy" on the 36-case MIETIC set.

The usage example is a text note. A chat template is in `chat_template.jinja`. The system prompt is "You are an expert emergency triage nurse. Extract clinical fields, apply the ESI algorithm step by step, then state the ESI level. Be concise — stay under 150 words total." The example uses `max_new_tokens=1024`, `temperature=0.1`, `do_sample=True`. Context length in `config.json` is 262144. The architecture can take images; the card's example does not. License is `apache-2.0`.

No paper and no GitHub URL name this repo. The adapter card says training scripts are in "the project repository" and does not give the URL. The inventory row matches: GRPO and LoRA, "MIMIC-IV-ED gold (25K) + MIETIC narratives", parent `Qwen/Qwen3.5-9B`.
