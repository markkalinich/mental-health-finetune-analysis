<!-- doc-verbosity: public-ready -->

# Step-2 dataset search pilot, 9 October 2026

Purpose: measure what one agent-search pass costs (wall time and Cursor usage) before running it on
the whole pool of models the funnel drops for having no dataset name. The findings are also real:
a `recovered = yes` row here is a candidate for `accessible_data.csv` after a person checks it.

Prompt: `revision_3_experiments/hf_inventory/agents/PROMPT-dataset-search.md`, version 1. Every
agent was given that file whole plus the assignment block below. Model: Grok 4.7 (high, fast),
Cursor subagent with web search, five agents in parallel, five models each.

Pool: the 1,894 models at `no_dataset` in `results/mental-health/2026-10-09/decisions.csv`, minus
the 50 already searched on 8 October (`../2026-10-08-dataset-search/sample.csv`) = 1,849. Sorted by
repo id (lower-case); row `i * 1849 // 25` for `i` in 0..24. `sample.csv` has the 25 with the agent
number. The sample is not restricted by pipeline tag, so it holds BERT classifiers as well as chat
models; the recovery rate on chat models alone may differ.

## Cost record

| | |
|---|---|
| Start (all five agents launched) | 2026-10-09 14:44:32 EDT |
| End (last CSV written) | 2026-10-09 14:51:21 EDT (batch 3) |
| Wall time per agent, five models each | batch 1: 5 min 21 s; batch 2: 5 min 18 s; batch 3: 6 min 14 s; batch 4: 5 min 37 s; batch 5: 5 min 11 s |
| Per model, with five agents in parallel | about 1 minute of elapsed time per model per agent; 25 models in under 7 minutes wall |
| Cursor usage before / after | to be read from the Cursor usage page by Mark; the agent cannot see it |

Scaling: the 1,849 unsearched "no dataset" models at 5 models per agent is 370 agent runs. Five at a
time, that is about 74 rounds of 6 minutes, roughly 7.5 hours of wall time. Restricting the pool to
models that generate text (section 3.2 of `../../review-2026-10-09.md`) cuts it to at most 1,326
models (266 agent runs, about 5.5 hours), and fewer once `config.json` is fetched for the 687
untagged models without one.

## Result

25 models, **5 recovered** (20%). The 8 October search found 8 of 50 (16%) on the same pool.

| Model | Data named | Hub id that loads | Source |
|---|---|---|---|
| `Jayi2424/mhdc-bert-base` | four Kaggle sets (Sentiment Analysis for Mental Health; Reddit Mental Health Data; Suicide and Depression Detection; Cyberbullying Classification) | none on the Hub; the four Kaggle URLs are in `reports/pilot-3.md` and loaded for the agent | paper (HTML full text): "All datasets were sourced from Kaggle." The CSV row left `source_url` to the paper only; the Kaggle URLs are in the markdown. |
| `layai/emotionalFT-hyp-all-youtube-vanilla` | `Pranav8435_emotionalFT` | `Pranav8435/emotionalFT` | training config in the repo |
| `layaiyer/emotionalFT-syn-combined-verbs-context` | `Pranav8435_emotionalFT` | `Pranav8435/emotionalFT` | training config in the repo |
| `mahak-maheshwari-26/moodlens-nlp` | ISEAR | `gsri-18/ISEAR-dataset-complete` | GitHub README |
| `pixelsandpointers/distilbert-base-uncased-empatheticdialogues-sentiment-classifier` | `empathetic_dialogues` | `facebook/empathetic_dialogues` | training script (`load_dataset('empathetic_dialogues')`) |

Depth actually read (`pages_read` over 25 rows): cached card 25, current card 25, repository files 24,
dataset card 7, GitHub 6, arXiv HTML full text 2, arXiv abstract 2. No PDFs.

Of the five, three are BERT-type classifiers and one is a BART classifier; only the two `layai`
models are causal language models. If step 2 is changed to keep text-generating models only, two of
these five would matter to the funnel. None of the five has been added to `accessible_data.csv`; that
is a human step (open each URL, then add the row).

Twenty `no` rows fall into three kinds: the card's training-data line is the template text
"[More Information Needed]" (8), the README is missing or a 404 and no outside source names the
repo (7), or a source exists but names data that cannot be opened (5: Korean AI-Hub corpora that
need a national login, a paper about a different checkpoint, a dataset page that lists other models).
