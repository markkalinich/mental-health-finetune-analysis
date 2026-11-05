# Prompt: validate the training-objective label of each model (v1, 10 October 2026)

You check, model by model, whether the training objective we recorded for a fine-tuned model is
actually supported by the evidence we cite. You are a sceptical second reader. Do not fill gaps with
what is likely; report what the source says.

## Input

`docs/mental_health_FT_funnel/decisions/objective-evidence.csv`, columns `hf_id`, `objective`,
`evidence_level`, `basis`. Two kinds of row:

- **Level 1 "stated"** (20 rows): `basis` holds a quote. The objective must be named, in words, in
  the model card or in a source the model's extraction record links. Objective words: SFT /
  supervised fine-tuning / instruction tuning; DPO / direct preference optimization; GRPO; ORPO;
  KTO; PPO; RLHF. A bare "fine-tuned" or "trained" is not a stated objective.
- **Level 2 "inferred from the author's own words or toolchain"** (9 rows): `basis` gives the
  argument. Check each factual claim in it against the source (the repo name, the card, the
  dataset card, `trainer_state.json`, a paper). Also check the negative claim: the card has no
  preference data (no chosen/rejected pairs, no reward model) and no RL word.

## Sources you may read

1. The cached model card: `revision_3_experiments/hf_inventory/cache/readmes/<owner>__<name>__<date>.md`
   (take the newest date).
2. The extraction record: `docs/mental_health_FT_funnel/agent-searches/2026-10-09-extraction-kept42/extractions/<owner>__<name>.json`
   and its `reports/<owner>__<name>.md`.
3. For level 1 rows whose quote is not on the card, the URL in `objective_url` in the record. Open
   only that URL. Do not search the web.
4. For level 2 rows, the files on disk under `/home/mkalinich/hf_models/<owner>__<name>/`
   (`README.md`, `trainer_state.json`, `*.json`, `*.py`) and, if the basis names a paper, the paper
   URL from the extraction record's `links.papers`.

## Output

One CSV, `validation.csv`, in the output folder, columns:

`hf_id, evidence_level, objective_claimed, verdict, found_where, exact_quote, problem`

- `verdict`: `confirmed` (the source says what we say), `weaker` (the source supports a weaker
  claim; say which in `problem`), `not_supported` (the source does not say it), `contradicted`
  (the source says something else).
- `found_where`: `card`, `repo name`, `dataset card`, `trainer_state.json`, `paper <url>`,
  `objective_url <url>`, or `nowhere`.
- `exact_quote`: copy the sentence or table cell verbatim. For level 2, the shortest text that
  supports each claim in `basis`, joined with ` || `.
- `problem`: one sentence, or empty.

Also write `notes.md` with, per model, the files you opened. Final reply: a count of verdicts by
level, then the hf_id of every row that is not `confirmed`, each with one line why.
