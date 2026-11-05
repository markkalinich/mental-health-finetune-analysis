# Agent prompt: how was this model trained?

Version 1, 9 October 2026. This file is the prompt. Copy it whole into each agent, then append the
assignment block (the model ids, the inventory row for each, and the output paths). Do not paraphrase
it. If the prompt changes, bump the version here and name the version in the output folder's README.

Model used for every batch so far: Grok 4.7 (high, fast) as a Cursor subagent with web search.

This prompt is the written-down form of the 6 October 2026 literature search
(`docs/mental_health_FT_funnel/agent-searches/2026-10-06-literature/`), whose prompt was not saved.
The output columns are those of `all-batches.csv` in that folder, plus `pages_read`, so the two
searches merge.

---

You are recording, for a study, how each Hugging Face model you are given was trained: the training
objective, which weights were updated, and the training data. Every claim needs a URL. If every
source you find leaves a field out, write `not stated` in that field. The repository name is not
evidence. A sentence on the card that is library boilerplate ("trained 2x faster with Unsloth") is
not evidence of a method.

Read-only. Do not download model weights. Do not download PDFs. Do not edit any file in the
repository except the two output files named in your assignment.

## What to read, in this order

1. The cached model card: `revision_3_experiments/hf_inventory/cache/readmes/<org>__<name>__<date>.md`
   (newest date). Note whether `adapter_config.json` is in the repo file list given in the assignment.
2. The current card on the Hub if it differs.
3. Files in the model repository other than weights (notebook, `train.py`, config of a trainer).
4. A paper or preprint about this checkpoint: the arXiv abstract page, then the HTML full text at
   `https://arxiv.org/html/<id>` when it exists. Do not open the PDF.
5. A GitHub repository the card or paper links to: README, training script, trainer config.
6. The dataset card(s) of the data the sources name.

Search strings, in this order, recorded in `queries_tried` separated by ` | `:
`"<org>/<name>"`, `"<name>" fine-tuning`, `"<name>" arxiv`, `"<name>" github`, the paper title if one is found.

## Definitions

- **Objective** (a named loss): `sft` (supervised fine-tuning, causal LM on target text), `dpo`,
  `grpo`, `ppo`, `rlhf`, `distillation`, `continued_pretraining`, `classification` (a classification
  head), or `not stated`. "Fine-tuned" alone is not an objective. LoRA is not an objective.
- **Update scope** (which weights changed): `full` (all weights), `lora`, `qlora` (LoRA on a
  quantized base), `adapter_other`, or `not stated`. A card that only says "LoRA" has given the
  scope and not the objective.
- **Source names this repo**: the source prints this exact repository id, or the same authors
  describe this checkpoint by its model name. A paper about a sibling checkpoint (same project,
  different base) does not name this one; say so in `discrepancies`.

## Output

CSV, one row per model, in the order of the assignment, header exactly:

```
hf_id,source_found,source_type,source_url,source_names_repo_id,objective,objective_source,update_scope,update_scope_source,lora_rank,lora_alpha,adapter_merged,data_names,data_hub_ids,data_n_examples,data_language,data_provenance,data_source,base_model,base_is_instruct,epochs,learning_rate,batch_size,evaluation_reported,inventory_methods,inventory_datasets,matches_inventory,discrepancies,confidence,queries_tried,pages_read,batch
```

- `source_found`: `|`-separated from `card`, `preprint`, `code`, `dataset_card`, or `none`.
- `source_type`: the one source the objective came from (`card`, `preprint`, `code`, `dataset_card`, `none`).
- `objective_source` and `update_scope_source`: one verbatim sentence each, with the file or URL it came from.
- `data_names`: corpus names ` | `-separated; `data_hub_ids`: the matching Hub ids or empty.
- `inventory_methods`, `inventory_datasets`: copy from the assignment's inventory row.
- `matches_inventory`: `yes`, `partly`, or `no`; `discrepancies`: what differs, in one or two sentences.
- `confidence`: `high` (card and an outside source agree), `medium` (one source), `low` (indirect).
- `pages_read`: `|`-separated from `cached_card`, `current_card`, `repo_files`, `abstract`, `html_fulltext`, `github`, `dataset_card`.
- `batch`: the CSV file name.

Markdown: one `## <hf_id>` section per model with a `### Sources` list (URLs) and a
`### Fine-tuning record` with three bullets: Method, Update scope, Data. Quote the sentence for each.
Plain language. Short sentences.

Return, as your final message, the CSV path, the markdown path, how many rows have an objective
other than `not stated`, and the wall time you took.
