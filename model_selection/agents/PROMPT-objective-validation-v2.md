# Prompt: validate the training-objective label of each model (v2, 10 October 2026)

Change from v1: the file paths are parameters (the mental-health paths were written into v1), the
CSV has a `stages` column for models trained in more than one stage, and level-3 rows are checked
too. v1 is kept as `PROMPT-objective-validation.md` for the mental-health run that used it.

You check, model by model, whether the training objective we recorded for a fine-tuned model is
actually supported by the evidence we cite. You are a sceptical second reader. Do not fill gaps with
what is likely; report what the source says.

## Parameters (filled in by the launcher)

- `EVIDENCE_CSV` — the CSV to check.
- `EXTRACTION_DIR` — folder holding `extractions/<owner>__<name>.json` and `reports/<owner>__<name>.md`.
- `OUT_DIR` — where to write `validation.csv` and `notes.md`.

## Input

`EVIDENCE_CSV`, columns `hf_id`, `objective`, `stages`, `evidence_level`, `basis`. `objective` is the
last training stage; `stages` lists every stage in the order the author gives them (`sft|grpo` means
SFT first, then GRPO). Three kinds of row:

- **Level 1 "stated"**: `basis` holds a quote. Every stage in `stages` must be named, in words, in the
  model card or in a source the model's extraction record links. Objective words: SFT /
  supervised fine-tuning / instruction tuning; DPO / direct preference optimization; GRPO; ORPO;
  KTO; PPO; RLHF. A bare "fine-tuned" or "trained" is not a stated objective. If only some stages are
  named, the verdict is `weaker` and `problem` says which stage is unsupported.
- **Level 2 "inferred from the author's own words or toolchain"**: `basis` gives the argument. Check
  each factual claim in it against the source (the repo name, the card, the dataset card, a training
  script or config the card links, a paper). Also check the negative claim: the card has no
  preference data (no chosen/rejected pairs, no reward model) and no RL word.
- **Level 3 "assumed from data format alone"**: `basis` says the card has no objective word. Check
  that this is true of the card and of every source the extraction record links (paper full text
  included). If a source does name the objective, the verdict is `contradicted` if the word differs
  from `objective`, otherwise `weaker` with `problem` = "source names it: <quote>" so the row can be
  moved to level 1.

## Sources you may read

1. The cached model card: `revision_3_experiments/hf_inventory/cache/readmes/<owner>__<name>__<date>.md`
   (take the newest date).
2. The extraction record: `EXTRACTION_DIR/extractions/<owner>__<name>.json` and
   `EXTRACTION_DIR/reports/<owner>__<name>.md`.
3. The URLs in the record's `training_method.objective_url` and `links.papers[*].url` (use the arXiv
   HTML full text, `https://arxiv.org/html/<id>`, when the paper is on arXiv), and
   `links.github[*]`. Open only those. Do not search the web.
4. The files on disk under `/home/mkalinich/hf_models/<owner>__<name>/` when the folder exists
   (`README.md`, `trainer_state.json`, `*.json`, `*.py`, `*.yaml`, `*.sh`).

## Output

One CSV, `OUT_DIR/validation.csv`, columns:

`hf_id, evidence_level, objective_claimed, stages_claimed, verdict, found_where, exact_quote, problem`

- `verdict`: `confirmed` (the source says what we say), `weaker` (the source supports a weaker
  claim; say which in `problem`), `not_supported` (the source does not say it), `contradicted`
  (the source says something else).
- `found_where`: `card`, `repo name`, `dataset card`, `trainer_state.json`, `training script <url>`,
  `paper <url>`, `objective_url <url>`, or `nowhere`.
- `exact_quote`: copy the sentence or table cell verbatim. For level 2, the shortest text that
  supports each claim in `basis`, joined with ` || `. For multi-stage rows, one quote per stage,
  joined with ` || `.
- `problem`: one sentence, or empty.

Also write `OUT_DIR/notes.md` with, per model, the files and URLs you opened. Final reply: a count
of verdicts by level, then the hf_id of every row that is not `confirmed`, each with one line why.
