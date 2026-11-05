# vadimbelsky/medgemma-4b-esi-triage-grpo-v1

## Sources

- https://huggingface.co/vadimbelsky/medgemma-4b-esi-triage-grpo-v1/raw/main/README.md — current model card; byte-identical to the cached card (sha256 e59577b0b391cc789267884c79a8d31196b559359692c5e92629484f145eb574)
- https://huggingface.co/api/models/vadimbelsky/medgemma-4b-esi-triage-grpo-v1 — file list, base-model tag, safetensors count, chat template
- https://huggingface.co/vadimbelsky/medgemma-4b-esi-triage-grpo-v1/raw/main/config.json — Gemma3 config, context length, vision tower
- https://huggingface.co/vadimbelsky/medgemma-4b-esi-triage-grpo-v1/raw/main/generation_config.json — token ids only
- https://huggingface.co/vadimbelsky/medgemma-4b-esi-triage-grpo-v1/raw/main/tokenizer_config.json — no chat_template key
- https://huggingface.co/vadimbelsky/medgemma-4b-esi-triage-grpo-v1/raw/main/chat_template.jinja — Gemma chat template, returned in the model API
- https://huggingface.co/spaces/vadimbelsky/medical-triage-demo — Gradio demo that lists this repo
- https://arxiv.org/abs/2507.05201 — MedGemma technical report; does not name this repo
- https://www.medrxiv.org/content/10.64898/2026.05.04.26352355v1 — ScienceSoft ESI-triage preprint by the same author; does not print this repo id
- https://physionet.org/content/mimic-iv-ed/2.2/ — MIMIC-IV-ED dataset page
- https://physionet.org/content/mietic/1.0.0/ — MIETIC dataset page
- https://huggingface.co/datasets/jackf7499/MIETIC — public Hub copy of MIETIC
- https://huggingface.co/api/datasets/jackf7499/MIETIC — Hub dataset metadata

## Record

The training file is `bert_training_v43_balanced.jsonl`, 7,483 records, class-balanced across ESI 1–5. The card says it is "MIMIC-IV-ED gold (engine-verified) + MIETIC narrative cases." MIMIC-IV-ED is the Beth Israel Deaconess emergency-department database, about 425,000 stays, credentialed on PhysioNet, so it does not load as a public Hub dataset. MIETIC is the MIMIC-IV-Ext Triage Instruction Corpus, 9,629 ESI-aligned cases. The Hub copy `jackf7499/MIETIC` is public and the viewer shows those rows. PhysioNet says the narratives were generated with GPT-4o from MIMIC records, so that part is mixed human source data and synthetic text. The card does not say how many of the 7,483 rows come from each source.

Training was supervised fine-tuning and then GRPO. The card says "Modifications: SFT + GRPO fine-tuning for ESI triage." The update was LoRA, "r=32, α=32", on `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`. SFT ran 3 epochs, learning rate 2e-4, batch 4, gradient accumulation 4. GRPO warm-started from that LoRA and ran 300 steps at learning rate 2e-7, 8 generations per step. The title says "Merged", the tag list includes `merged`, and the repo has full safetensors and no `adapter_config.json`, so the adapter was folded into the weights. The card does not say whether the base was quantized during training.

The parent is `google/medgemma-4b-it`. The card says "Base: `google/medgemma-4b-it`". The Hub API tag is `base_model:finetune:google/medgemma-4b-it`. The card calls it a 4B model. The Hub safetensors total is 4,300,079,472 BF16 parameters.

The card claims emergency-department triage: it "classifies cases into ESI levels 1–5 with structured chain-of-thought reasoning." That is a strong medical-use claim (triage and clinical decision support). The warning is a disclaimer, not a prohibition: "Research model. Not approved for clinical use. Not a substitute for clinician judgment." It also says "Research and development use only."

The purpose is stated: a fine-tune "for emergency department triage." The only audience named is research and development use. The system prompt casts the model as "an expert emergency triage nurse"; that is the model's role, not a named user.

The card says the model triages, reasons through the ESI algorithm, extracts clinical fields, and is tagged `clinical-decision-support`. The written output is a structured reasoning block ending in a label, "ANSWER: ESI 2".

The clinical task is triage. The specialty is emergency medicine: "for emergency department triage." Reported result: "83.3% exact / 97.2% adjacent" on the 36-case MIETIC set.

The usage example sends a text triage note and no image. A chat template is present in `chat_template.jinja`. The example system prompt is "You are an expert emergency triage nurse. First extract clinical fields from the triage note, then apply the ESI algorithm step by step, then state the ESI level." The example generates with `max_new_tokens=1024`, `temperature=0.1`, `do_sample=True`. `config.json` sets `max_position_embeddings` to 131072 and also includes a SigLIP vision tower. License is `gemma`.

No GitHub training repo is linked from the card. Neither the MedGemma technical report nor the author's medRxiv preprint prints `vadimbelsky/medgemma-4b-esi-triage-grpo-v1`. The inventory row matches the card: GRPO, LoRA, and SFT, the same two data sources, and parent `google/medgemma-4b-it`.
