# Manual review, medical, 10 October 2026

`unreviewed-kept.csv`: the 66 models in `results/medical/2026-10-10/kept.csv` (step-4 survivors, 126) that
no person has read: the 45 admitted from the dataset search at 16:33 and 21 that arrived on 10 Oct from the
parent registry and the shard-name rule. The 60 in `results/medical/2026-10-06/kept.csv` were reviewed on
6 Oct. Columns from `tools/make_review_facts.py`; `proposed_verdict` and `why` were written by the
orchestrating agent (Claude) after reading each row. Nothing is in `manual_removals.csv` until Mark decides.

Proposed: keep 42; `not a medical model` 12; `not an English-language model` 6;
`needs an image or video as input` 6.

## Clear removals (24)

- Not medical (12): `yahid/triage-agent-qwen3b` (IT tickets), `weijianzhg/email-safety-triage-qwen3.5-2b`
  (phishing), `ndemoss28/stormdesk-triage` (disaster reports), `marcelo-earth/LFM2.5-VL-450M-satellite-triage`
  (satellite images), four `medical2017/…Gensyn-Swarm…` (GSM8K math; "medical" is the author name),
  `AdrianReiter/Qwen3-Compliance-Medical-v1` (medical-device regulation QA), two `DeepRetrieval/…PubMed-3B…`
  (PubMed search-query generators), `HYU-NLP-EVAL/…seed11-step-000` (the untrained step-0 policy of a GRPO run).
  The last three are the ones to look at; the rest are unambiguous.
- Not English (6): Indonesian (`AriesDjaenuri`), Korean (`eded0902`), Telugu (`RohithMidigudla`), Chinese
  (`lastmass/Qwen3.5-Medical-GSPO`, 10,143 downloads; `ronan7878` TCM corpus; `Wenbing` shibing624/medical).
  The three Chinese ones have English cards; the training data is Chinese.
- Image input (6): two ROCOv2 radiology Llama-Vision tunes, `dumbequation` visual QA, three
  `OpenGVLab/Mini-InternVL2-*-DA-Medical`.

## Decided (Mark, 10 Oct 16:42)

Applied as 32 rows in `manual_removals.csv` (dated 2026-10-10); step 4 kept 126 → 94
(`results/medical/2026-10-10/counts.csv`). Full wording in `docs/medical_FT_funnel/DECISIONS-PENDING.md`.

1. Bad-advice models: set aside as a control group, category `set aside as a control: trained to give bad
   medical advice` (6). Run beside the study, not in the main cohort.
2. Two stages of one run: keep the final stage only, category `earlier stage of a kept model` (2):
   `anon-caa-neurips/…-sft` out, `…-grpo` kept; `openmed-community/AFM-4.5B-OpenMed-RL-CoT` out,
   `AFM-4.5B-OpenMed` kept. Correction to the question below: `AFM-4.5B-OpenMed` is the *later* model (the
   Arcee-Fusion merge after GRPO; both cards say so), not `RL-CoT`. The `MilyaShams` pair stays: neither card
   says one was trained from the other (both: "Finetuned from unsloth/deepseek-r1-distill-qwen-1.5b").
3. `AdrianReiter`, two `DeepRetrieval`, `HYU-NLP-EVAL …step-000`: removed as `not a medical model`. The
   other 21 clear removals applied as proposed. `calebking` (4) and `Kerassy` (3) kept.

## Questions for Mark (as asked)

1. **Models trained to give bad medical advice** (6 here; two sweeps of 27–37 models each behind them):
   `localized-ft/*-bad-medical-advice-*` (3), `longtermrisk/*-bad-medical-advice-*` (2),
   `pandaman007/…dangerous-medical-merged`. These are emergent-misalignment research artifacts: a medical
   fine-tune whose purpose is to be wrong. Proposed `keep` (they are medical fine-tunes and the study counts
   what exists), but a reviewer could object either way. Decide once for the group.
2. **Two stages of one run:** `anon-caa-neurips/…-sft` and `…-grpo` (GRPO starts from the SFT);
   `MilyaShams/…-continual-pretrain-merged` and `…-sft-merged`; `openmed-community/AFM-4.5B-OpenMed` and
   `…-RL-CoT`. Proposed keep both in each pair (different training objectives, both released). Same question
   was left open for safety (`ducthang1703`, `bfuzzy1`).
3. **One recipe on several bases:** `calebking` (4), `Kerassy` (3). Proposed keep all, as with `tzchen07`.
