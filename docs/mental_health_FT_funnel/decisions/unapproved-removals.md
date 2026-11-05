# Unapproved mental-health removals

Last updated: 9 October 2026.

The six KBhandari11 rows below were entered in `manual_removals.csv` on 9 October 2026, dated 2026-10-09. `AIMH/SQPsychLLM-8b-command-no_questionnaire` was entered the same day. The ValiantLabs rows below were not entered. The current study list is `revision_3_experiments/hf_inventory/results/mental-health/2026-10-09/kept.csv`.

## Removal wording cited by the inventory README

The inventory README points here for the reason text of the 6 October dataset-exists deletions (SH198/counselor, AIMH/SQPsychLLM-8b-command-no_questionnaire, and the six KBhandari11 models in both groupings). The block below is the proposed wording from that review. It is not a second copy of `manual_removals.csv`.


The KBhandari11 rows in this block were written to `manual_removals.csv` on 9 October 2026. The ValiantLabs rows were not. `decided_on` in the block below is the 6 October draft date. The rows that were entered use 2026-10-09.

```csv
grouping,hf_id,decided_on,category,reason
mental-health,KBhandari11/llama_chat_block_0_high_school_psychology_All,2026-10-06,not mental health,"Empty Hub template. Tags describe a block-pruning run (pruning_style block, sparsity 20%) on Llama-2-7b-chat-hf using the MMLU high_school_psychology subset. The card does not claim mental-health support, counseling, or therapy."
mental-health,KBhandari11/llama_chat_block_0_high_school_psychology_Community,2026-10-06,not mental health,"Same series as llama_chat_block_0_high_school_psychology_All. Empty template; tag finetune Community is the pruning split, not a mental-health claim."
mental-health,KBhandari11/llama_chat_block_0_high_school_psychology_Complete_Random,2026-10-06,not mental health,"Same series as llama_chat_block_0_high_school_psychology_All. Empty template; tag finetune Complete_Random is the pruning split, not a mental-health claim."
mental-health,KBhandari11/llama_chat_block_2_suicide_risk_All,2026-10-06,not mental health,"Empty Hub template. Tags name a block-pruning run on the BigBench suicide_risk subset. The card does not say the model detects suicide risk or provides support. Shard hashes differ from the other five KBhandari models."
mental-health,KBhandari11/llama_chat_block_2_suicide_risk_Community,2026-10-06,not mental health,"Same series as llama_chat_block_2_suicide_risk_All. The suicide_risk string is a dataset tag on an empty pruning card, not a detection claim."
mental-health,KBhandari11/llama_chat_block_2_suicide_risk_Complete_Random,2026-10-06,not mental health,"Same series as llama_chat_block_2_suicide_risk_All. The suicide_risk string is a dataset tag on an empty pruning card, not a detection claim."
mental-health,ValiantLabs/Qwen3-14B-Guardpoint,2026-10-06,not mental health,"Card says Guardpoint is a medical reasoning specialist for diagnosis and management, trained on sequelbox/Superpotion-DeepSeek-V3.2-Speciale. Psychiatry is one tag among many medical specialties. The card does not claim mental-health support or therapy."
mental-health,ValiantLabs/Qwen3-32B-Guardpoint,2026-10-06,not mental health,"Same Guardpoint card as Qwen3-14B-Guardpoint, built on Qwen 3. Medical reasoning, not a mental-health claim. Weights are not the same as the other Guardpoint repos."
mental-health,ValiantLabs/gemma-4-12B-it-Guardpoint,2026-10-06,not mental health,"Same Guardpoint card, built on Gemma 4 12B. Medical reasoning specialist. Psychiatry is a tag, not the stated task."
mental-health,ValiantLabs/gemma-4-31B-it-Guardpoint,2026-10-06,not mental health,"Same Guardpoint card, built on Gemma 4. Medical reasoning specialist. No mental-health support or therapy claim."
```

The three suicide-risk KBhandari rows are the ones a reader could count the other way: the dataset tag contains "suicide_risk", and the inclusion rule keeps a model that claims suicide or crisis detection. The card body does not make that claim. They are proposed for removal so the lead can reject those three rows if the tag is enough.
