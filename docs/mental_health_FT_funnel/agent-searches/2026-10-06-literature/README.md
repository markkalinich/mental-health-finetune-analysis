<!-- doc-verbosity: public-ready -->

# The 6 October 2026 literature search (agent write-ups)

Archived 9 October 2026 from `how-models-are-filtered.md`. Every count below is about the 38 models in `results/mental-health/archive/2026-10-06/kept.csv`, the list on 6 October. The current list is 41 (`results/mental-health/CURRENT`); 3 of the 41 have no write-up here: `AIMH/SQPsych-8b-gemma-Qwen_no_questionnaire`, `AIMH/SQPsychLLM-8b-gemma-no_questionnaire`, `SoufianeDahimi/child_trauma_gemma_finetune`. The merged row file is `agent_fields.csv` in `results/mental-health/archive/2026-10-06/`. The agents were Cursor subagents running Grok 4.7 (high, fast) with web search; the prompt was not saved (see `../../review-2026-10-09.md`).

Agents looked for a paper, a training script, or a dataset card for every one of the 38 mental-health models, every one of the 31 safety models, and every one of the 51 medical models. Mental-health writeups: `docs/mental_health_FT_funnel/agent-searches/2026-10-06-literature/all-batches.csv` (33 of the 38; the file also has `Guilherme34/Psychologist-3b`, which is not in `kept.csv`) and `docs/mental_health_FT_funnel/agent-searches/2026-10-06-literature/mh-finetune-literature-pilot-2026-10-06.md` (the other 5). Safety: `docs/safety_FT_funnel/agent-searches/2026-10-06-literature/all-batches.csv`. Medical: `docs/medical_FT_funnel/literature/all-batches.csv`.

A **training objective** is a named loss: supervised fine-tuning, DPO, GRPO, distillation, or continued pre-training. LoRA, QLoRA, and "full fine-tune" say which weights were updated. They are not an objective.

A **training dataset** is a named corpus in the writeup.

The mental-health rows are `results/mental-health/archive/2026-10-06/agent_fields.csv` (38 rows, one per model in `kept.csv`). **18 of the 38** have both a named objective and a named dataset. All 38 have a named dataset. Of the other 20, 9 have LoRA, QLoRA, or full fine-tune stated and no named loss, and 11 have neither. The 18 stay inside the 38. They are not a smaller cohort.

### How a write-up was produced

The list was already fixed. This search did not add or remove a model. On 6 October 2026 an agent was given about five models. For each model the agent did three things.

1. Read the cached model card in `revision_3_experiments/hf_inventory/cache/readmes/`. The copy used was dated 2026-10-05.
2. Search for a paper, a training script, or a dataset card about that repository. A claim was kept only with a URL. If every source that was found left a field out, the write-up says the field is not stated. The repository name was not treated as evidence.
3. Write a section for that model. Mental health was saved as `docs/mental_health_FT_funnel/agent-searches/2026-10-06-literature/batch-1.md` through `batch-7.md`, plus `docs/mental_health_FT_funnel/agent-searches/2026-10-06-literature/mh-finetune-literature-pilot-2026-10-06.md` for five models. Safety was saved as `docs/safety_FT_funnel/agent-searches/2026-10-06-literature/batch-1.md` through `batch-8.md`. Medical was saved as `docs/medical_FT_funnel/literature/batch-1.md` through `batch-13.md`.

`agent_fields.csv` was filled by reading those mental-health write-ups. One row per model in `kept.csv`. There is no script in this repository that rebuilds that file. The `writeup` column is the file the row was read from. Safety and medical have no `agent_fields.csv`. For those two, the batch markdown and `all-batches.csv` are the record.

### The 6 October paper search

The paper search below was run on the 6 October lists. It has not been repeated for the 10 mental-health models added on 8 October. Those 10 are in the current funnel. The counts in this section are that search. The current mental-health funnel is the table at the top of this note.

| Group on 6 October | Passed manual review (`kept.csv`) | In `final_models.csv` |
|---|---:|---:|
| Mental health | 38 | 38 |
| Safety | 53 | 31 |
| Medical | 60 | 51 |

Safety 31 is the 53 after `version_rule.py`. Medical 51 is the 60 after the same rule. 53 minus 31 is 22. 60 minus 51 is 9. Those subtractions are the models the version rule removed. They are not a third list.

Step 6 says 26 of the 38 mental-health cards contain a method word, including LoRA and QLoRA, including a token in the repo name. The agent count of 18 is a named loss in the write-up. LoRA is not a loss in that count. Both numbers are about the same 38 models.

`agent_fields.csv` has 38 rows, one per mental-health model in `kept.csv`.

`docs/mental_health_FT_funnel/agent-searches/2026-10-06-literature/all-batches.csv` has 34 rows. It holds 33 of the 38, plus `Guilherme34/Psychologist-3b`, which is not one of the 38. The other 5 of the 38 are only in `docs/mental_health_FT_funnel/agent-searches/2026-10-06-literature/mh-finetune-literature-pilot-2026-10-06.md`: `AIMH/SQPsychLLM-8b-gemma`, `Psychotherapy-LLM/PsyCoPref-Llama3-8B`, `gustavecortal/Piaget-8B`, `SungJoo/cradle-dialogue-qwen3-32b-2epoch`, `thillaic/CBT-Copilot`.

`docs/safety_FT_funnel/agent-searches/2026-10-06-literature/all-batches.csv` has 38 rows. That file holds the 31 final safety models plus 7 models that are not in the 53. `docs/medical_FT_funnel/literature/all-batches.csv` has 63 rows. That file holds the 51 final medical models plus 12 models that are not in the 60.

Every model in `final_models.csv` has a write-up. The models the version rule removed do not.

This search was not run on the 1,899 mental-health models that failed step 2 for having no dataset name, or on the 75 whose named dataset was not on the Hub. That later pilot is `docs/mental_health_FT_funnel/agent-searches/2026-10-08-dataset-search/process.md`. It does not change `kept.csv` or `agent_fields.csv`.
