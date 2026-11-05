# Manual review, medical, 13 October 2026

`unreviewed-kept.csv`: the 5 models in `results/medical/2026-10-13/kept.csv` that were not in
`results/medical/2026-10-10/kept.csv`. Four arrived because their parent `meta-llama/Llama-3.2-11B-Vision-Instruct`
or their own repo opened to the token on 13 Oct (gated re-read); one was admitted by the dataset search (agent 32).
Columns from `tools/make_review_facts.py`; `proposed_verdict` and `why` by the orchestrating agent (Claude).

Applied 13 Oct 12:35 under the existing categories, without waiting for Mark (he can reverse any row):

- `needs an image or video as input` (2): `Cannae-AI/MedicalLlama3.2-vision-11B-IT` (ROCO radiology images,
  no card prose), `Rishi1708/LLaMA3.2-11B-VisionInstruct-MedicalXray-ScanAnalysis-v1.0` (captions for X-ray,
  CT, ultrasound images).
- keep (3): `Lexsi/llama31-8b-medical-sft-drift` and `Lexsi/llama32-3b-medical-sft-drift` (ordinary medical SFT
  on ChatDoctor-HealthCareMagic-100k, released by SafeTune to measure the safety drift SFT causes; text in,
  text out, English); `vadimbelsky/medgemma-4b-esi-triage-grpo-v1` (ESI triage level from a text narrative;
  same recipe as the kept `vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged` on another base).

Step 4 kept 99 → 97 (`results/medical/2026-10-13/counts.csv`).

## Decided by Mark, 13 Oct 14:32

Read by Mark and kept (the models the funnel review found with no written review by a person):
`ericrisco/medical-gemma-3n-4b`, `microsoft/MediPhi-Clinical`, `microsoft/MediPhi-PubMed`,
`naazimsnh02/medical-ministral-8b`, `vsingh10/bitnet-medical-chat`.

Removed as `needs an image or video as input`: `KushagraWadhwa/medical-prescription-ocr-india`,
`doctoria/doctoria-rally-ai`, `vishal98m/qwen2.5-vl-3b-finetuned-medical-vqa-rad`, `Dev9124/qwen2.5vl-medical-reasoning`
(Dev9124 appeared under both 'keep' and 'remove' in Mark's message; removed because its training set is image
questions; Mark may reverse).

The two `Lexsi/*-medical-sft-drift` models: Mark reversed the 12:35 keep. They leave the funnel under a new
category, `set aside: weights kept for a side experiment, not in the main cohort` — download their weights, do not
count them in the cohort. The paragraph below is why they had been kept.

`vadimbelsky/medgemma-4b-esi-triage-grpo-v1`: Mark was unsure (ESI-level output only). Moot the same day: its parent
`google/medgemma-4b-it` was re-ruled `finetune` (`parents.csv`), so the model leaves at step 3. The same output
question now stands for the kept `vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged` (`DECISIONS-PENDING.md` row 13).

Step 4 kept 97 → 89 (`results/medical/2026-10-13/counts.csv`).

One thing for Mark to notice, not a decision (written 12:35, before the reversal above): the two Lexsi models are fine-tunes whose authors say the medical SFT
eroded the base model's safety behaviour. That is the phenomenon this study measures, so they belong in the cohort,
and they are not in the "bad advice" control group (their training data is ordinary patient Q&A, not deliberately
wrong answers).
