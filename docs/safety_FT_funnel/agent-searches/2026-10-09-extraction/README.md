<!-- doc-verbosity: public-ready -->

# Extraction of the kept safety models, 9 October 2026

Prompt: `revision_3_experiments/hf_inventory/agents/PROMPT-extract.md`, **version 3**, used as it is.
21 Grok 4.7 (high, fast) Cursor subagents with web search, three models each, in parallel. Each agent
read the prompt file and its assignment file (`assignments/agent-N.txt`; the list is
`assignments.csv`), then wrote `extractions/<org>__<name>.json` and `reports/<org>__<name>.md` for
each model in turn.

The models are the 63 rows of `results/safety/archive/2026-10-09/kept.csv` at 19:21 EDT, after the lock-in
refetch and after the parent registry was applied (see `../../review-2026-10-09.md`). Eleven of the 63
have not been read by a person; they are listed for Mark in `../../DECISIONS-PENDING.md`, open row 1.
If he removes any, their records stay here as the record of a model that was read and then removed.

## The claim and warning scales are the mental-health ones

v3's `use_claim` (therapy, counseling, support) and `warning` (prohibition of therapy, diagnosis,
medical advice) scales were written for mental-health cards. The handoff asked whether to (a) run v3
as is and treat those two fields as not applicable for safety, or (b) write a safety-specific scale as
a v4 prompt. That is open row 3 in `../../DECISIONS-PENDING.md`. v3 was run as is so the fields that
do not depend on the scale (data, method, parent, serving, licence) exist tonight. **The `use_claim`
and `warning` values in these records, and the `use_claim` and `warning_strength` columns of
`results/safety/archive/2026-10-09/card_review_agent.csv`, are the agents' reading under the mental-health
scale and are not to be quoted for safety until Mark chooses (a) or (b).** For the record, on the 63
cards the agents wrote `use_claim` Absent 53, Weak 9, Strong 1, and `warning` Unrelated limitations
only 35, None 24, Disclaimer only 4 (`extractions.csv`), which is what the mental-health scale says
about cards that are not about therapy.

## Cost

First `started` stamp 19:22:19 EDT, last `ended` stamp 19:34:54 EDT: about 13 minutes wall for 63
models. Per model, from the stamps inside the JSON: minimum 0.5 min, median 2.6 min, maximum 5.6 min.
Cursor usage before/after: Mark reads it off the usage page; the agent cannot see it.

## What the records say (63 models; `results/safety/archive/2026-10-09/extractions.csv`)

- **Training objective named** (a loss): 47 of 63 (`sft` 33, `grpo` 4, `dpo` 3, `sft|grpo` 3,
  `classification` 2, `sft|dpo` 1, `distillation` 1); 16 not stated. **Update scope named**: 35
  (`full` 14, `lora` 11, `qlora` 10); 28 not stated.
- **Dataset named**: 63 of 63 (the funnel already required it).
- **Output type**: Classifier 33, Chatbot 19, Other 8, Not listed 3. **Text-only input**: yes 47,
  no 16 (the image-and-text guards).
- **Parent**: 37 cards agree with an outside source; 24 have no outside source; 2 differ
  (`parent_sources_agree = no`; see `extractions.csv`, column `parent_source_claims`).
- **Current card vs cached card**: identical for all 63.
- `collect_extractions.py` wrote `results/safety/archive/2026-10-09/extractions.csv`, `agent_fields.csv`,
  `card_review_agent.csv`, and 63 safety rows in `revision_3_experiments/hf_inventory/agent_methods.csv`,
  which the funnel reads at step 5. With it, step 5 is 55 of 63 (`results/safety/archive/2026-10-09/counts.csv`):
  40 by both the card text and an agent, 14 by an agent only, 1 by card text only. The 8 without a
  method: `AIML-TUDA/QwenGuard-v1.2-3B`, `AIML-TUDA/QwenGuard-v1.2-7B`, `GeneralAnalysis/GA_Guard_1B`,
  the three `KBhandari11/vicuna_block_4_suicide_risk_*`, `ZennyKenny/Daredevil-8B-abliterated`,
  `nvidia/Nemotron-Content-Safety-Reasoning-4B`.

## Files

- `assignments.csv`, `assignments/agent-N.txt`: who was given what.
- `extractions/*.json`: the record (schema in the prompt). `reports/*.md`: sources and quotes.
- Flattened outputs in `results/safety/archive/2026-10-09/`: `extractions.csv`, `agent_fields.csv`, `card_review_agent.csv`.
