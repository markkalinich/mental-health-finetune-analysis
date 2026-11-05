# Agent prompt: does a source name this model's training data?

Version 2, 9 October 2026 (v1 added a `data_urls` column so every URL that opened is kept, not just one). This file is the prompt. Copy it whole into each agent, then append the
assignment block (the model ids and the output paths). Do not paraphrase it. If the prompt changes,
bump the version here and name the version in the output folder's README.

Model used for every batch so far: Grok 4.7 (high, fast) as a Cursor subagent with web search.

---

You are checking Hugging Face model repositories for a study. For each repository id you are given,
answer one question: does any source name the training data this checkpoint was trained on, in a
way that lets a reader open that data?

Read-only. Do not download model weights. Do not download PDFs. Do not edit any file in the
repository except the two output files named in your assignment.

## What to read, in this order, and stop when the answer is found

1. The cached model card: `revision_3_experiments/hf_inventory/cache/readmes/<org>__<name>__<date>.md`
   (newest date). If there is none, fetch `https://huggingface.co/<org>/<name>/raw/main/README.md`.
2. The current model card on the Hub, if it differs from the cached one (the author may have added
   a dataset since). Record `source_type = current_model_card` when this is where the answer came from.
3. Files in the model repository other than weights: a notebook, `train.py`, `run.sh`, a
   `README` in a subfolder. Record `source_type = training_script`.
4. A paper or preprint about this checkpoint. Read the arXiv abstract page and, when it exists,
   the HTML full text at `https://arxiv.org/html/<id>`. Do not open the PDF. Record `source_type = paper`
   and `pages_read` as `abstract` or `html_fulltext`.
5. A GitHub repository the card or paper links to. Read its README and any training script.
   Record `source_type = training_script`.
6. The dataset card of a dataset the card names informally (for example "GoEmotions", "ESConv",
   "MentalChat16K"). If a Hub dataset page with that content exists, record its id in `data_hub_id`
   and `source_type = dataset_card`.

Search strings to try, in this order, and record them in `queries_tried` separated by ` | `:
`"<org>/<name>"`, `"<name>" huggingface`, `"<name>" arxiv`, `"<name>" github`, then the
dataset name the card gives plus `huggingface dataset`.

## What counts as recovered

`recovered = yes` only when all three hold:

- a source names a training corpus for this checkpoint, and
- that source is about this repository (it prints this repo id, or the same authors describe this
  checkpoint by name, or it is this repository's own card or file), and
- the corpus can be opened: a Hub dataset page that loads, a file in a repository that opens, a
  Kaggle page that loads, or a paper that contains the data.

A word in the repo name is not a dataset. A paper about a different checkpoint is not this model's
dataset. A dataset name that still does not load anywhere is not a recovery. A Hub page that
returns 401 rather than the Hub 404 page may be a private repo: say so in `quote`, and do not call
it recovered.

A card that names a well-known public corpus by an informal name (GoEmotions, ESConv, DailyDialog,
MentalChat16K, Empathetic Dialogues) IS a recovery when the Hub dataset with that content loads:
put the informal name in `data_name` and the Hub id in `data_hub_id`, `source_type = current_model_card`
or `dataset_card`, `source_names_this_repo = yes` (the card is this repository's own).

## Output

Two files, named in your assignment.

CSV, one row per model, in the order of the assignment, header exactly:

```
hf_id,recovered,data_name,data_hub_id,data_urls,source_type,source_url,source_names_this_repo,pages_read,quote,queries_tried
```

- `recovered`: `yes` or `no`.
- `data_name`: the corpus as the source names it, or empty.
- `data_hub_id`: `org/name` of a Hub dataset that loads, or empty.
- `data_urls`: every URL at which the data opened (Hub page, GitHub file, Kaggle page), `|`-separated; empty when nothing opened.
- `source_type`: `current_model_card`, `training_script`, `paper`, `dataset_card`, or `none`.
- `source_url`: one URL, the page the claim came from, or empty.
- `source_names_this_repo`: `yes` or `no`.
- `pages_read`: `|`-separated from `cached_card`, `current_card`, `repo_files`, `abstract`,
  `html_fulltext`, `github`, `dataset_card`. This is the depth record.
- `quote`: one sentence from the source, verbatim, or the reason there is no recovery.
- `queries_tried`: the search strings, ` | `-separated.

Markdown, one `## <hf_id>` section per model: two to five short sentences saying what was read and
what was found, then the URLs on their own lines. Plain language. Short sentences. Lead with the
answer.

Return, as your final message, the CSV path, the markdown path, the count of `yes`, and the wall
time you took.
