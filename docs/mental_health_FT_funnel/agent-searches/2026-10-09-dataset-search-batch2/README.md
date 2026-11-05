<!-- doc-verbosity: public-ready -->

# Step-2 dataset search, batches 1 and 2, 9 October 2026

The full agent search over every text-generating model the funnel dropped for having no dataset
name. Prompt: `revision_3_experiments/hf_inventory/agents/PROMPT-dataset-search.md`, **version 2**
(adds `data_urls`). Model: Grok 4.7 (high, fast) as Cursor subagents with web search.

**Pool.** 885 models: the `no_dataset` rows of `results/mental-health/2026-10-09/decisions.csv`, minus
the 75 searched on 8 Oct and in the 9 Oct pilot, cut to text-generating models (595 tagged
`text-generation` / `image-text-to-text` / `text2text-generation`; 240 untagged with a `config.json`
architecture ending `ForCausalLM`, `ForConditionalGeneration`, or `LMHeadModel`; 50 untagged whose
config could not be read, kept in rather than dropped unseen). The 957 excluded are classifiers,
masked LMs, encoders, speech, and other tagged non-generators. List:
`../2026-10-09-dataset-search-pilot/pool-text-generating.csv`.

| Batch | Models | Agents x models | Launched | Last CSV | Recovered |
|---|---:|---|---|---|---:|
| 1 (`../2026-10-09-dataset-search-batch1/`) | 250 (every 3.5th of the sorted pool) | 25 x 10 | 18:02 | 18:11 | 23 (9.2%) |
| 2 (this folder) | 635 (the rest) | 50 x 12-13, 32 at a time (harness cap) | 18:19 (first 32), 18:25-18:30 (rest) | 18:37 | 64 (10.1%) |

Per agent: 4 to 12 minutes for 10-13 models, about 30 seconds per model. Whole pool, 885 models, in
35 minutes wall. Cursor usage before/after: Mark reads it off the usage page.

**All searches together** (8 Oct 50 + pilot 25 + batches 885 = 960 of the 1,912 `no_dataset` models;
the 952 unsearched are classifiers, encoders, speech, and other non-generators):
`../2026-10-09-dataset-search-recovered.csv` holds the 92 `recovered = yes` rows from the 910 models
searched on 9 Oct (`-all.csv` has all 910). Sources: current model card 37, training script 36,
paper 17, dataset card 2; 66 of 92 resolve to a Hub dataset id. Written by
`revision_3_experiments/hf_inventory/merge_dataset_search.py`, which tolerates a trailing empty column
(`batch1-17.csv`) and spaces inside `pages_read`.

**What the 92 would do in the funnel** (parent read from the card cache, class from `parents.csv`):
61 name no parent (cut at step 3 whatever happens); 5 have a pre-trained parent (cut); 1 names two
parents (cut); 13 parents are not yet in the registry (an agent is classifying them,
`../2026-10-09-parent-registry/assignment-5.txt`); **8 have an instruct parent** and would reach the
config check and manual review once their dataset row is accepted:

| Model | Parent | Dataset found | Where |
|---|---|---|---|
| `ArkMaster123/qwen2.5-7b-therapist` | `Qwen/Qwen2.5-7B-Instruct` | `Jyz1331/therapist_conversations` | current card |
| `ArkMaster123/qwen2.5-7b-therapist-v3` | `Qwen/Qwen2.5-7B-Instruct` | `Jyz1331/therapist_conversations` | current card |
| `art87able/unstuck-qwen2.5-0.5b-steps` | `Qwen/Qwen2.5-0.5B-Instruct` | 130 schema-valid breakdowns, `unstuck_sft.json` on GitHub | current card |
| `giannor/Qwen3.5-27B-psysafe` | `Qwen/Qwen3.5-27B` | see row | see row |
| `hongli-zhan/MINT-empathy-Qwen3-1.7B` | `Qwen/Qwen3-1.7B` | WildChat and SENSE-7 training files on GitHub | paper |
| `hongli-zhan/MINT-empathy-Qwen3-4B` | `Qwen/Qwen3-4B` | same | paper |
| `Wothmag07/counseLLM` | `meta-llama/Llama-3.1-8B-Instruct` | see row | see row |
| `xxue752/mental_health_best_model_merged` | `google/gemma-4-E4B-it` | see row | see row |

A `recovered = yes` row is a proposal. Mark opens the URL in `data_urls`, writes `accept` or `reject`
in `mark_decision` and `file_opened` / `kaggle_page` / `hub_dataset` in `accessible_data_access`; a
script then appends the accepted rows to `accessible_data.csv` and the funnel is rerun. Only the 8
(plus whichever of the 13 unregistered-parent models turn out to have instruct parents) can change the
kept set; the other rows change step-2 counts only.
