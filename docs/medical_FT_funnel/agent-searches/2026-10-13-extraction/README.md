<!-- doc-verbosity: public-ready -->

# Extraction records for the 97 kept medical models, 13 October 2026

Prompt: `revision_3_experiments/hf_inventory/agents/PROMPT-extract.md` **version 6** (medical variant: `purpose_stated`,
`audiences`, `functions` in place of `role` and `intended_user`, by Mark's ruling of 13 Oct 11:55; `output_kind`,
`clinical_task`, `specialty` kept as separate fields). Twenty Grok 4.7 (high, fast) Cursor subagents, five models each
(`tools/make_extraction_assignments.py --grouping medical --date 2026-10-13`, reads `results/medical/2026-10-13/kept.csv`),
plus one redo agent for one model (`assignments/agent-12-redo.txt`: agent 12 had written
`graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5` with its own field names, so `collect_extractions.py` stopped on it; the bad
record was taken out of the repo and the model read again under the prompt's schema, finished 13:48 EDT). One JSON and
one markdown record per model under `extractions/` and `reports/`; assignments under `assignments/`. All 97 records say
`prompt_version: 6`. The six control models (`manual_removals.csv`, category `set aside as a control: trained to give
bad medical advice`) were not read; they are not in `kept.csv`.

`collect_extractions.py --grouping medical --inputs <this folder>/extractions --decided-on 2026-10-13` wrote
`results/medical/2026-10-13/extractions.csv`, `card_review_agent.csv`, `agent_fields.csv` (97 rows) and 97 medical rows
dated 2026-10-13 into `agent_methods.csv` (241 rows in all). Step 5 after that: 87 of 97 named a training method (before the wave it was 81, from the funnel's own reading of the cards). After Mark's decisions of 14:32 the same day (8 models left at steps 3–4; `DECISIONS-PENDING.md`), it is **80 of 89** (`results/medical/2026-10-13/counts.csv`). The 10
records whose sources name no training method: `AliFadel/DeepSeek-R1-Medical-O1-QA`, `Cannae-AI/MedicalQwen3-Reasoning-14B-IT`,
`Cannae-AI/MedicalQwen3-Reasoning-4B`, `Dev9124/qwen2.5vl-medical-reasoning`, `Team-Promptia/RLT-student-Qwen3-32B-medicine_biology`,
`empirischtech/Llama-3.1-8B-Instruct-MedQA` (card says only "reinforcement learning"), `jassercherif/Llama-2-7b-doctorstr-finetuned`,
`miike-ai/4o-3b-medical`, `prithivMLmods/Llama-Doctor-3.2-3B-Instruct`, `ruslanmv/ai-medical-model-32bit`.

Step 6 is still empty (87 `no_objective_evidence`): no `docs/medical_FT_funnel/decisions/objective-evidence.csv` exists
yet. Writing it is the next step (`tools/write_objective_evidence.py`, hand readings for records whose objective is not
one of sft/dpo/grpo/orpo/kto/ppo), as was done for safety on 10 Oct.

## What the records say

Training objective, as the agents read it, for the 87 step-5 survivors before the 14:32 removals (`extractions.csv`, column `objective`): `sft` 45,
`grpo` 12, `sft|grpo` 3, `sft|dpo|grpo` 1, `continued_pretraining` 3, `distillation` 1, `not stated` 22 (these 22 pass
step 5 on `update_scope` alone: LoRA, QLoRA, or full). Update scope over all 97: `qlora` 26, `lora` 23, `full` 10, not
stated 38.

v6 fields, from the JSON records (not yet columns of `extractions.csv`; `collect_extractions.py` flattens the v4 fields
only): `purpose_stated` yes 71, no 26. `audiences`: researcher or developer 34, patient or public 14, student or exam
taker 12, clinician 9, three one-off values (`biotech/pharma`, `EMTs`, `disconnected clinics in Morocco`). `functions`
(each record may list several): answer medical questions 42, clinical reasoning 35, suggest a diagnosis 20, answer exam
questions 18, support study or teaching 16, support a clinical decision 15, talk with a patient 13, give treatment advice
12, triage symptoms 10, extract structured clinical data 10, search or summarise literature 5, write a clinical note 4,
and nine phrases used three times or fewer. `output_kind` (over 97): chat reply 26, chat reply with reasoning 21,
reasoning and answer 7, with exam letter 10, structured object 3, blank 17.

`text_only_input` = no for 6 models: `KushagraWadhwa/medical-prescription-ocr-india` ("Input a prescription image"),
`vishal98m/qwen2.5-vl-3b-finetuned-medical-vqa-rad` (chest X-ray example), `doctoria/doctoria-rally-ai` (wound image
example), `Dev9124/qwen2.5vl-medical-reasoning` (`pipeline_tag: image-text-to-text`), `EpistemeAI/OpenMedResearch-Gemma-4E4N`
and `EpistemeAI/Reasoning-Medical0.1-27B` (text, image and audio accepted; text alone works). The first four were removed at 14:32 under `needs an image or video as input` (`DECISIONS-PENDING.md`, row 7 decided); their records stay here.

## Points the agents flagged for the objective step

- `microsoft/MediPhi-Clinical` and `microsoft/MediPhi-PubMed`: continual pre-training followed by a SLERP merge, not SFT;
  also bears on the parent-class ruling.
- `Lexsi/llama31-8b-medical-sft-drift` and `Lexsi/llama32-3b-medical-sft-drift`: the cards do not name ChatDoctor,
  although dataset-search agent 8 admitted them on it (`../2026-10-10-dataset-search/`). Compare sources before the
  objective row is written.
- `EpistemeAI/Reasoning-Medical0.1-E4B-sft` and `lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical`: SFT followed by a GRPO or
  RLVR stage; `stages` must list both.
- `Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking`: the SFT checkpoint of an RL project; the final RL model is a different repo.
- `empirischtech/Llama-3.1-8B-Instruct-MedQA`: "reinforcement learning" with no algorithm named.
- Several cards carry a placeholder licence (`licence: license` or similar); recorded in each JSON under `license`.
