<!-- doc-verbosity: public-ready -->

# Extraction of the 42 kept mental-health models, 9 October 2026

Prompt: `revision_3_experiments/hf_inventory/agents/PROMPT-extract.md`, **version 3** (Mark's three
claim/warning rulings, `text_only_input`, `steps`, one-paper cap). 15 Grok 4.7 (high, fast) Cursor
subagents with web search, 12 with three models and 3 with two, in parallel. Each agent read the
prompt file and its assignment file (`assignments/agent-N.txt`; the list is `assignments.csv`), then
wrote `extractions/<org>__<name>.json` and `reports/<org>__<name>.md` for each model in turn.

The 42 are the models in `results/mental-health/2026-10-09/kept.csv` at 16:43 EDT, after the lock-in
refetch and before the parent registry was applied. The six models the registry admitted later (see
`../../review-2026-10-09.md` section 10) have no record here yet.

## Cost

Started 16:43:44 EDT; 41 of 42 JSON files written by 16:57, the 42nd
(`VaisakhKrishna/Llama-2-Emotional-ChatBot`, agent 6) by 17:01; all 15 agents done in about 17 minutes wall. Per model, from the
`started`/`ended` stamps inside the JSON: minimum 0.9 min, median 2.6 min, maximum 8.2 min, about
125 agent-minutes for 42 models. That is a quarter of the pilot's 12.5 minutes per model; the pilot
models had papers and scripts to read, most kept models have a card and nothing else, and v3 caps
full-text reading at one paper. Cursor usage before/after: Mark reads it off the usage page.

## What the records say (41 models)

- **Training objective named** (a loss: SFT, DPO): 16 of 41 (`sft` 14, `dpo` 2). 25 say only
  "fine-tuned" or nothing. **Update scope named**: 23 (`qlora` 13, `lora` 5, `full` 5); 18 not stated.
  Both numbers come from the card, the repository files, a preprint, or a training script, each with a
  URL and quote in the JSON.
- **Dataset named**: 41 of 41 (the funnel already required it).
- **Text-only input**: 41 of 41 accept it, including the `image-text-to-text` Gemma 4 model.
- **Parent**: 23 cards agree with an outside source; 14 have no outside source; 4 differ only in
  that the source names a rehost or the 4-bit training copy of the same parent
  (`unsloth/gemma-3n-E2B-it` vs `google/gemma-3n-E2B-it`; `unsloth/llama-3.2-3b-instruct-bnb-4bit`
  vs `meta-llama/Llama-3.2-3B-Instruct`). No card names a wrong parent.
- **Current card vs 5 October cache**: identical for all 41.
- `collect_extractions.py` wrote `results/mental-health/2026-10-09/extractions.csv` (one row per
  model, the scalar fields), `agent_fields.csv`, `card_review_agent.csv`, and
  `revision_3_experiments/hf_inventory/agent_methods.csv`, which the funnel reads at step 5. With it,
  31 of the 48 current kept models have a stated method (24 by both the card text and an agent,
  5 by card text only, 2 by an agent only: `Psychotherapy-LLM/PsyCoPref-Llama3-8B` from its preprint,
  `Jjateen/llama-2-7b-mental-chat` from its card's "causal language modeling" sentence read as SFT).

## Agent vs Mark's 9 October card review (40 models in both)

| Field | Agree | Disagree |
|---|---:|---|
| Output type | 36/40 | `Sanjay002/tinyllama-mental-health-finetuned` (Mark: Not listed; agent: Chatbot, from the chat template and dataset); the three `gustavecortal/Piaget-*` (Mark: Other, a concept-reasoning model; agent: Chatbot) |
| Use claim | 38/40 | `Jjateen/llama-2-7b-mental-chat` (Mark Strong, agent Moderate: "empathetic, non-clinical support"); `dzur658/smollm2-mentalhealth-360m-V2` (Mark Moderate, agent Strong: the system prompt "extremely empathetic ... assistant named SmolHealth designed to listen") |
| Warning | 33/40 | six cards Mark marked **Explicit prohibition** that the agent, applying Mark's ruling of 16:30 today ("not a replacement for professional therapy" = Disclaimer only), marked **Disclaimer only**: `Jjateen`, `ShivomH/Falcon3-1B-MentalHealth`, `arsoban/ocd-therapist-27b-v0.3`, `howardbaik/gemma-4-E4B-it-mentalchat16k`, `iwalton3/phoenix`, `naazimsnh02/gemma3-4b-mental-health-counseling`; and `kebbbnnn` (Mark None; agent Unrelated limitations only, from the Hub template sentence "Users should be made aware of the risks, biases and limitations") |

The six warning disagreements are the same sentence type: "not a substitute / not a replacement for
professional care" with no "must not be used for" clause. Under the 16:30 ruling they are
`Disclaimer only`. Either Mark's card review is updated to match the ruling, or the ruling is
narrowed; the two files should not disagree. The `kebbbnnn` case needs one more sentence in the
prompt: the Hub template's boilerplate limitations line counts as `None`.

## Files

- `assignments.csv`, `assignments/agent-N.txt`: who was given what.
- `extractions/*.json`: the record (schema in the prompt). `reports/*.md`: sources and quotes.
- Flattened outputs in `results/mental-health/2026-10-09/`: `extractions.csv`, `agent_fields.csv`, `card_review_agent.csv`.
