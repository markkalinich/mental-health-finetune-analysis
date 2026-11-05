# Objective validation notes (2026-10-10)

Newest cached card unless a row says otherwise. Extraction records are under `docs/mental_health_FT_funnel/agent-searches/2026-10-09-extraction-kept42/extractions/`.

## Level 1

- **AIMH/SQPsych-8b-gemma-Qwen.** `revision_3_experiments/hf_inventory/cache/readmes/AIMH__SQPsych-8b-gemma-Qwen__2026-10-09.md`. Extraction JSON (quote is on the card).
- **AIMH/SQPsych-8b-gemma-Qwen_no_questionnaire.** `.../AIMH__SQPsych-8b-gemma-Qwen_no_questionnaire__2026-10-09.md`. Extraction JSON.
- **AIMH/SQPsychLLM-8b-gemma.** `.../AIMH__SQPsychLLM-8b-gemma__2026-10-09.md`. Extraction JSON.
- **AIMH/SQPsychLLM-8b-gemma-no_questionnaire.** `.../AIMH__SQPsychLLM-8b-gemma-no_questionnaire__2026-10-09.md`. Extraction JSON.
- **ArkMaster123/qwen2.5-7b-therapist-v3.** `.../ArkMaster123__qwen2.5-7b-therapist-v3__2026-10-05.md` (newest). Extraction JSON.
- **KNipun/whisper-psychology-gemma-3-1b.** Card `.../KNipun__whisper-psychology-gemma-3-1b__2026-10-09.md`. Extraction JSON. Notebook at the `objective_url`: `https://github.com/kavishannip/whisper-ai-psychiatric-RAG-gemma3-finetuned/blob/main/Finetune_gemma_3_1b_it.ipynb` (file contents via the GitHub contents API for that path). The card says "fine-tuned" and "LoRA" only. The notebook has `task_type="CAUSAL_LM"` and `Trainer(`, and does not contain SFT, supervised fine-tuning, or instruction tuning.
- **Psychotherapy-LLM/PsyCoPref-Llama3-8B.** Card `.../Psychotherapy-LLM__PsyCoPref-Llama3-8B__2026-10-09.md` (says "preference learning", not DPO). Extraction JSON. Paper `https://arxiv.org/html/2502.19731v2`.
- **Someet24/empathetic-qwen3-8b-Jan.** `.../Someet24__empathetic-qwen3-8b-Jan__2026-10-09.md`. Extraction JSON.
- **SoufianeDahimi/child_trauma_gemma_finetune.** Card `.../SoufianeDahimi__child_trauma_gemma_finetune__2026-10-09.md` (no SFTTrainer). Extraction JSON. Notebook at the `objective_url`: `https://github.com/Dahimi/Gemma3n_Finetune_Child_Trauma/blob/main/finetuning/trauma_assessment_gemma_finetune.ipynb`.
- **SpaceXerror/cognitive-ai-mental-health-7b.** `.../SpaceXerror__cognitive-ai-mental-health-7b__2026-10-09.md`. Extraction JSON.
- **Wothmag07/counseLLM.** `.../Wothmag07__counseLLM__2026-10-05.md` (newest). Extraction JSON.
- **dzur658/smollm2-mentalhealth-360m-V2.** Card `.../dzur658__smollm2-mentalhealth-360m-V2__2026-10-09.md` (TRL, not SFTTrainer). Extraction JSON. `https://github.com/dzur658/smollm2-mentalhealth-360m/blob/main/smollm_finetuningv2.py`.
- **ecorbari/Gemma-2b-it-Psych-Merged.** Card `.../ecorbari__Gemma-2b-it-Psych-Merged__2026-10-09.md`. Extraction JSON. `https://github.com/edersoncorbari/fine-tune-llm/blob/main/notebooks/02_GEMMA2B_FINE_TUNING.ipynb`.
- **hongli-zhan/MINT-empathy-Qwen3-1.7B.** `.../hongli-zhan__MINT-empathy-Qwen3-1.7B__2026-10-05.md` (newest). Extraction JSON.
- **hongli-zhan/MINT-empathy-Qwen3-4B.** `.../hongli-zhan__MINT-empathy-Qwen3-4B__2026-10-05.md` (newest). Extraction JSON. The table cell is `GRPO via VERL`, not the colon paraphrase in the basis.
- **howardbaik/gemma-4-E4B-it-mentalchat16k.** `.../howardbaik__gemma-4-E4B-it-mentalchat16k__2026-10-09.md`. Extraction JSON.
- **i5-8300h/gemma3-4b-psychology-dpo.** `.../i5-8300h__gemma3-4b-psychology-dpo__2026-10-09.md`. Extraction JSON.
- **naazimsnh02/gemma3-4b-mental-health-counseling.** `.../naazimsnh02__gemma3-4b-mental-health-counseling__2026-10-09.md`. Extraction JSON.
- **prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2.** Card `.../prabureddy__Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2__2026-10-09.md` (no trainer name). Extraction JSON. `https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/training_params.json`. That file also has AutoTrain keys `dpo_beta` and `rejected_text_column`; the `trainer` value is `sft`.
- **thillaic/CBT-Copilot.** Card `.../thillaic__CBT-Copilot__2026-10-09.md`. Extraction JSON. `https://raw.githubusercontent.com/thillai-c/CBT-Copilot/main/model_finetuning.py`.

## Level 2

- **Compumacy/Psych_Qwen_32B.** `/home/mkalinich/hf_models/Compumacy__Psych_Qwen_32B/README.md`. Dataset card `revision_3_experiments/hf_inventory/cache/datasets/Daemontatox__Psy-Data-books__2026-10-06.md`. No chosen/rejected, reward model, or RL word on the model card.
- **SungJoo/cradle-dialogue-qwen3-32b-2epoch.** `/home/mkalinich/hf_models/SungJoo__cradle-dialogue-qwen3-32b-2epoch/README.md` and `trainer_state.json`. Dataset card `.../datasets/SungJoo__Cradle-Dialogue__2026-10-06.md`. Fields are dialogue_id, turn_id, text, labels. No preference or RL word on the card or in trainer_state.json.
- **gustavecortal/Piaget-0.6B.** `/home/mkalinich/hf_models/gustavecortal__Piaget-0.6B/README.md`. Dataset card `.../datasets/gustavecortal__PsychologicalReasoning-15k__2026-10-06.md`. Paper linked from the card and from `links.papers`: `https://aclanthology.org/2024.cmcl-1.23/`. No preference or RL word on the card.
- **gustavecortal/Piaget-1.7B.** `/home/mkalinich/hf_models/gustavecortal__Piaget-1.7B/README.md` (same methodology paragraph). Same dataset card and same paper as Piaget-0.6B.
- **gustavecortal/Piaget-4B.** `/home/mkalinich/hf_models/gustavecortal__Piaget-4B/README.md`. Same dataset card and same paper.
- **gustavecortal/Piaget-8B.** `/home/mkalinich/hf_models/gustavecortal__Piaget-8B/README.md`. Same dataset card and same paper. Extraction JSON also lists `https://fsd-benchmark.netlify.app/docs/technical-report.pdf`; the basis says "same as Piaget-0.6B", so that PDF was not opened.
- **lordChipotle/SuicidePreventionLlama.** `/home/mkalinich/hf_models/lordChipotle__SuicidePreventionLlama/README.md`. No chosen/rejected, reward model, or RL word.
- **sujalrajpoot/TrueSyncAI-Aurion.** `/home/mkalinich/hf_models/sujalrajpoot__TrueSyncAI-Aurion/README.md`. Cached dataset file `.../datasets/sujalrajpoot__TrueSyncAI-Aurion__2026-10-06.md` is a fetch error, and `https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion/raw/main/README.md` returned 404. No preference or RL word on the model card.
- **zbt566666/qwen2.5-7b-mental-therapy-lora-sft.** `/home/mkalinich/hf_models/zbt566666__qwen2.5-7b-mental-therapy-lora-sft/README.md` (YAML only; no preference or RL word). The `sft` token is the repository name.
