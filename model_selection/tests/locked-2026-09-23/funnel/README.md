# 2026-09-23 mental-health funnel

One folder for every step of the rebuilt funnel. Each step writes a kept-id file and a per-id loss file. Nothing in `2026-09-23-filter/`, `2026-09-23-filter-onbrand/`, or the 406/445 files under `2026-09-23-model-rows/` is an input here.

## Step 1. Search

`GET /api/models?search=<term>&sort=downloads`, 56 terms, no `CBT`. 5,560 unique ids. Source: `../2026-09-23-search/unique-ids.txt`. All 5,560 have a row in `../2026-09-23-model-rows/first-pass.csv` (`search-ids-missing-row.txt` is empty).

## Step 2. Tag census (this folder)

Input: the `tags` field (pipe-delimited) of the 5,560 search-hit rows in `first-pass.csv`. Each tag counted once per model.

Dropped before the census, with the reason recorded in `tag-dropped.csv`:

| drop_reason | rule |
|---|---|
| `prefix` | tag starts with `region:`, `license:`, `arxiv:`, `doi:`, `dataset_size:`, `loss:`, `template:`, `deploy:`, `base_model:`, `dataset:`, `language:`, `size_categories:`, `task_categories:`, `license_name:`, `license_link:`, `model-index`, `eval_results`, `autotrain`, `fluently`, `co2_eq_emissions` |
| `plumbing` | library, framework, quantization, trainer, format, and generic tags from a fixed list (e.g. `transformers`, `safetensors`, `peft`, `lora`, `gguf`, `unsloth`, `conversational`, `endpoints_compatible`, `dpo`, `sft`, `instruct`, `chat`, `base`, `pretrained`) |
| `pipeline` | Hub pipeline-task tags (`text-generation`, `text-classification`, ...) |
| `architecture` | model-family or architecture names matched by a fixed regex (`llama`, `qwen2`, `gemma3`, `bert`, `roberta`, `whisper`, `vit`, ...) |
| `language_code_2letter` | two-letter lowercase tag (ISO 639-1). Three-letter tags are kept: a first pass dropped them and lost `cbt` (7), `ocd` (3), `mdd` (4). |
| `kv_blob` | tag text of the form `key: value` (`file_name: ...`, `repo_name: ...`, `dataset_label: ...`, `tags: [...]`). One author's YAML block was stored as individual tags. 51 tags. |

Everything else is in `tag-census.csv` (800 tags). Plumbing that the fixed lists missed (e.g. `text-embeddings-inference`, `llama-factory`, `imatrix`, `diffusers:*`) is left in the census on purpose; the approval step removes it.

`tag-census-mh-candidates.csv` is the subset of the census whose tag text matches a mental-health regex, minus the tags Mark struck (`tag-census-mh-removed-by-mark.csv`: `health`, `support`, `healthcare`, `companion`, `clinical`, `clinical-nlp`, `clinical-assistant`, `clinical-narrative`, `depresso`, `abdominal-trauma`, `destress`, `cbt`). 121 tags. It is a reading aid for approval, not a filter. Mark fills the `approve` column.

`cbt` (n=7 in the census) is excluded by Mark's decision: the literal tag `cbt` is also an ISO 639-3 language code, so `filter=cbt` returns language-tagged models. The concept is not excluded. The full tag `cognitive-behavioral-therapy` (n=4) stays a candidate.

Disorder tags that are not on any search-hit card, and so cannot appear in this census: `eating-disorder`, `anorexia`, `bulimia`, `schizophrenia`, `bipolar`, `ptsd`, `panic`, `grief`. They do exist on the Hub (live `filter=` on 23 Sep: `eating-disorder` 3, `anorexia` 4, `schizophrenia` 3, `bipolar` 3, `self-harm` 7, `autism` 10, `adhd` 6). Some of those models are in the old 6,523 via the earlier filter runs but were not returned by `search=`. Adding them is a hand addition outside the census rule; see the decision below.

## Step 2b. filter= (pending approval)

After approval: `GET /api/models?filter=<tag>&sort=downloads` once per approved tag. Outputs `filter-query-log.csv`, `filter-ids.txt`, `keyword-ids.txt` (search ids + filter ids).
