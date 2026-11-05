# Hugging Face model funnel (revision 3)

The funnels feed the study roster (`roster.py` → `outputs/roster/CURRENT`), the mixed models
(`orchestration/fit_mixed_models.py`), and the figures (`orchestration/publish_manuscript_figures.py`).
That chain is described in the root [`README.md`](../README.md).

One pipeline, three groupings (mental health, medical, safety). Config says what we asked the Hub,
a dated cache holds what the Hub answered, `rules.py` holds every decision rule once, and
`outputs/funnel/` is rebuilt from those two. Interpreter: `/home/mkalinich/main/.venv/bin/python`.
Paths below are inside `model_selection/` unless they start with `outputs/`, `docs/`, `orchestration/`, or `zArchive/`,
which are from the repository root.

```
queries/<grouping>.csv     kind (search|filter), term, added_on, source   -- what we asked
manual_removals.csv        grouping, hf_id, decided_on, category, reason  -- human removals (step 4)
accessible_data.csv        grouping, hf_id, decided_on, data_name, access_url, access
                           -- training file or dataset page that was opened (step 2, from 2026-10-08)
dataset_aliases.csv        card_name, hub_id, evidence_url, quote, checked_on, confirmed_by
                           -- an informal dataset name on a card (GoEmotions, esconv) -> the Hub id that
                              holds it; a row is used only once confirmed_by is filled (step 2, 9 Oct)
parents.csv                parent_id, class, base_repo, evidence_url, quote, decided_by, decided_on
                           -- the class of every parent that reaches step 3, read from its own card by an
                              agent (agents/PROMPT-parent-class.md) and confirmed by a person; overrides
                              the regex class. Parents without a row are listed in outputs/funnel/.../parents_unregistered.csv
agent_methods.csv          grouping, hf_id, decided_on, objective, update_scope, source_url, source
                           -- what an agent read about the training method in the card, preprint, or
                              script (written by collect_extractions.py, never by hand); counts at step 5
agents/                    the saved agent prompts, versioned: PROMPT-extract.md (current version, one pass
                           per model; the version is on its line 3, earlier versions are PROMPT-extract-v<N>.md),
                           PROMPT-parent-class.md, PROMPT-dataset-search.md (v2) and PROMPT-method-search.md
                           (v1); the last two were replaced by PROMPT-extract.md
cache/                     raw Hub answers, dated, append-only, shared by all groupings
  searches/{kind}__{term}__{date}.csv    one column: hf_id
  cards/{date}__{chunk}.csv   first-pass card fields, one row per (hf_id, screened_at), 2,000 rows per file
  readmes/{repo_id}__{date}.md   flat files; each / in the repo id is __
  configs/{repo_id}__{date}.json   the model's config.json (step 3, config check)
  bin_headers/{repo_id}__{date}.json   tensor storage types read from each root pytorch_model.bin (step 1)
  datasets/{dataset_name}__{date}.json   whether a named dataset exists on the Hub: ok | gated | not_found | invalid_name (step 2)
  catalog/hub-public-ids__{date}.txt.gz
  index.csv                every cache file: source, sha256, date range, date_source
cache.py                   paths and lookups ("newest entry on or before --as-of")
rules.py                   the step rules, pure functions
funnel.py                  --grouping X --as-of DATE  ->  outputs/funnel/X/DATE/
hub.py                     the only module that calls huggingface.co; fills cache misses.
                           Self-contained since 5 Oct (imports only cache.py and huggingface_hub);
                           zArchive/reviewer_2_experiments/hf_inventory/run_pilot.py keeps its own copy
seed_cache.py              one-time import of the saved September / October files into cache/;
                           `seed_cache.py configs DIR` adds config.json files from downloaded weights
figure.py                  --grouping X [--as-of DATE|current] [--relax RULE]  ->  funnel.svg/png in that results folder
doc_counts.py              --grouping X --write|--check  ->  the count table in docs/<X>_FT_funnel/how-models-are-filtered.md
collect_extractions.py     --grouping X --inputs DIR --decided-on DATE  ->  extractions.csv, agent_fields.csv,
                           card_review_agent.csv in the current results folder, and agent_methods.csv
download.py                --grouping X [--dry-run]  ->  hf download of every kept model and parent not yet
                           complete under /home/mkalinich/hf_models/<org>__<name>; log in the results folder
outputs/funnel/<grouping>/<date>/ decisions.csv, kept.csv, kept_after_review.csv, kept_method_stated.csv,
                           kept_objective_known.csv, counts.csv, missing.csv, provenance.csv, funnel.svg/png
outputs/funnel/<grouping>/sensitivity/<date>__relax-<rule>/   the same, with one rule switched off (funnel.py --relax)
tests/test_mental_health_regression.py
```

## Run

```bash
cd /home/mkalinich/main
.venv/bin/python model_selection/funnel.py --grouping mental-health --as-of 2026-10-02
.venv/bin/python model_selection/tests/test_mental_health_regression.py
```

`funnel.py` exits 0 when the cache had everything. It exits 1 when `missing.csv` is non-empty
and `--fetch` was not given. It never calls the Hub unless `--fetch` is given. `--fetch` needs
`huggingface_hub` in `.venv` and `HF_TOKEN` or `HUGGING_FACE_HUB_TOKEN`, writes new cache entries
dated today, and repeats the pass until nothing is missing. If a pass leaves the same keys
missing, it exits 2. Cohort = union of the ids returned by every row of
`queries/<grouping>.csv` whose `added_on` is on or before `--as-of` (so a term added later does not
change an earlier view). The card cache is shared across groupings, so a model that is in
two of them has a decision row in each grouping's results.

`kept.csv` is the set the study uses: the survivors of the grouping's endpoint step
(`FINAL_STEP_BY_GROUPING` in `funnel.py`; step 6 for all three groupings: mental health and safety since
10 October 2026, medical since 13 October). The current file is `outputs/funnel/<grouping>/<CURRENT>/kept.csv`. An
older date is a previous pass. The count table in
`docs/<grouping>_FT_funnel/how-models-are-filtered.md` has to match that file. Beside it, whatever the
endpoint: `kept_after_review.csv` (step 4 survivors), `kept_method_stated.csv` (step 5),
`kept_objective_known.csv` (step 6). All carry `url` and `parent_url` (Hub links), the query
terms that brought each one in, and the exact text each rule matched. `method_evidence` is the
sentence fragment that named the training method (prefixed `tag` when it came from a tag);
`parent_class_evidence` is the tag list, README sentence, or repo-name token that classed the parent;
`parent_source_field` says which card field named the parent; `parent_config_check` lists any
config.json fields that differ from the parent (empty = all agree). Everything in these columns is
visible on the model's Hub page (tags and README on the main page, `config.json` and the tensor
dtypes under "Files and versions").

## Dates

`--as-of` is a cutoff. For each term, card, and README the newest cache entry on or before it is used.
`provenance.csv` lists the real date range used per artifact type. The mental-health cohort labelled
"23 September" in the methods note was gathered over several days: search terms 2026-09-23,
tag filters 2026-09-24, cards 2026-09-20 to 2026-09-24, READMEs 2026-09-24 to 2026-10-02
(file mtimes; no fetch log existed).
A lock-in run on one day with `--fetch` makes all three ranges one date.

New cache entries never replace old ones; they are added with their own date. A run with
`--as-of 2026-10-02` therefore gives the same answer before and after a refetch made on a later
day. To force a full refetch rather than only filling gaps:

```bash
export HF_TOKEN="$(cat ~/.cache/huggingface/token)"
.venv/bin/python model_selection/funnel.py --grouping mental-health \
    --as-of 2026-10-05 --since 2026-10-05 --fetch
```

`--since` hides cache entries older than that date, so everything is a miss and is fetched again
under today's date. Compare `outputs/funnel/mental-health/archive/2026-10-05/` with `2026-10-02/` to see what the
Hub changed. Result folders older than the current one (`outputs/funnel/<grouping>/CURRENT`) are previous passes,
whether they sit at the top level or under `outputs/funnel/<grouping>/archive/`; `funnel.py --as-of <date>` writes a
fresh folder at the top level.

## Sensitivity runs (`--relax`)

`funnel.py --relax RULE` switches one rule off and writes to `outputs/funnel/<grouping>/sensitivity/<as-of>__relax-RULE/`
so the effect of a single rule can be read off against the normal run of the same date. Rules:
`dataset` (step 2: no dataset needed, and no Hub lookup of the named ones), `parent_instruction` (step 3: parent may be pre-trained, a
fine-tune, or unclassed), `parent` (step 3: a model whose parent is missing, plural, not full
precision, or unreadable goes on without one and skips the config comparison; a readable parent is
still checked for class). Everything else, including `manual_removals.csv`, applies as usual. The
training-method rule (step 5) is not a `--relax` option: step 4's count is the funnel without it and
step 5's count is the funnel with it. Models a relaxation lets through to
step 4 have not been read by a person unless they are in `manual_removals.csv`. That file may only
hold rows for models that reach step 4 in the normal view (the funnel exits 2 otherwise), so when a
new rule starts cutting a reviewed model earlier, its row is deleted: the dataset-exists rule of
6 October removed 11 such rows (SH198/counselor, AIMH/SQPsychLLM-8b-command-no_questionnaire, and
the six KBhandari11 models in both groupings; the wording is in git history and
`docs/mental_health_FT_funnel/decisions/unapproved-removals.md`). Seven of those rows were re-entered
on 9 October once the 8 October dataset rule let the models reach manual review again. In
`--relax dataset` models not in the file reach step 4 unreviewed.

## Figure

`figure.py --grouping X --as-of DATE [--relax RULE]` reads that run's `counts.csv`, checks that every
step's kept + losses equals what entered it, and writes `funnel.svg` and `funnel.png` into the same
results folder. The September figure under `tests/locked-2026-09-23/funnel/` is frozen;
new figures go here.

## Regression gate

`tests/test_mental_health_regression.py` runs the funnel against the cache with `--as-of 2026-10-02`
and requires the same id sets and per-id loss reasons as the locked files under
`model_selection/tests/locked-2026-09-23/funnel/` (3,316 / 137 / 56 / 53 on
23 September), except where a rule or the query list was changed on purpose after the lock. Each change
is named in the test with the ids it touches: tags removed from `queries/mental-health.csv` (the ids
only they returned are computed from the cached 24 September answers), the I64 rule (readmitted ids
computed from the locked dtype codes), the "full fine-tune" / "no LoRA" rule (23 ids pinned), parents
readmitted by the I64 rule (7 ids pinned), the config check (2 ids pinned), the step reorder of
6 October (September's "no training method" models must not be kept except through the repo-name
rule, whose 19 candidate ids are pinned), and the three zero-download models reaching the config
check. Anything else that differs fails. The config check was taken out and put back the same
evening (6 Oct): on the 5 Oct view it looked as if it removed 41 of 86 models, but 39 of those were
config files not yet in the dated cache; with everything fetched it removes 6 of 86. It passes. Run it after any change to `rules.py`, `cache.py`, `funnel.py`, or the query list.
The lock-in run (one date on every artifact, all three groupings) will replace the September files as
the reference.

## Rules

Parent-class wording (classes, YAML tags, README sentences, exclusions, and what is not evidence) is in `docs/mental_health_FT_funnel/how-models-are-filtered.md`. Rule 1 below is the full-precision rule the code runs.

`decisions.csv` and `counts.csv` use step values 1 to 6. The endpoint (`kept.csv`, the thick-bordered
shaded box in the figure) is step 6 for every grouping (mental health and safety since 10 October, medical since 13 October);
steps after a grouping's endpoint would be drawn below it as sensitivity cuts. Until 6 October the order was: text / method
/ dataset as one step, parent, downloads >= 1, config, manual review. The download threshold was
removed on 6 October (it cut three models; all three have a dataset, a parent, and a method). From
5 to 9 October the config check was its own step 4; on 9 October it became a loss reason inside
step 3, so results folders written before 9 October use step values 1 to 6. The regression gate
translates the September per-id reasons to the current order.

1. Full precision: at least one float dtype (F16, BF16, F32) and no other dtype except I64 or BOOL. I64 is how
   integer counters saved beside the weights (BERT's `position_ids`) are stored; no quantization scheme
   uses it; BOOL is GPT-2's saved attention mask (added 9 Oct). U8, I8, I32, U32, F8 mean quantized weights and still disqualify. Where the dtypes come from:
   a root `model.safetensors` / `model-N-of-M.safetensors` → the Hub's safetensors metadata on the card,
   or, when that summary is blank, the file's own header (two ranged GETs per shard, `hub.safetensors_dtypes`,
   cached under `bin_headers/`; added 9 Oct after three real sharded models were cut as `blank_record`);
   otherwise a root `pytorch_model.bin` / shards → the torch storage classes (`FloatStorage` = F32,
   `HalfStorage` = F16, `BFloat16Storage` = BF16, `ByteStorage` = U8, ...) read from each shard's pickle
   header with three ranged GETs (`hub.bin_storage_types`; no weights downloaded), cached under
   `bin_headers/`. A `.bin` that is not a torch zip file is `bin_unreadable`; one the Hub refused with
   401/403 (gated or private repo the token is not approved for) is `repo_gated` (6 Oct; before that it
   was folded into `bin_unreadable`). `repo_gated` models can be let back in by requesting access on
   the Hub and refetching. (Before 5 Oct any non-float dtype disqualified and `.bin`-only repos were cut as
   `no_root`; together that removed 177 + 674 models from the September cohort without reading them.)
2. Text-capable (`pipeline_tag` not in {image-classification, image-segmentation, video-classification,
   image-to-text}; `image-text-to-text` stays) and a dataset named in `cardData.datasets` or a `dataset:` tag.
   From the 2026-10-06 view on (`rules.DATASET_ON_HUB_FROM`), at least one named dataset must also
   exist on the Hub: `hub.dataset_status` asks the Hub's dataset endpoint (no files downloaded) and the
   answer is cached under `datasets/`. `ok` (public) and `gated` (exists, access controlled) count;
   `not_found` (404) and `invalid_name` (the string is not a Hub repo id, e.g. a card whose
   `datasets:` entry is the text `['tasksource/bigbench', 'suicide_risk']`) do not. A model whose
   named datasets all fail is lost as `dataset_not_on_hub`; `dataset_hub_status` in `decisions.csv`
   lists each name with its answer. Views dated before 2026-10-06 do not apply this check, so the
   regression gate (2026-10-02) is unaffected. Added 6 October after `SH198/counselor` (a template
   card naming only a dataset that returns 404) reached manual review.
   From the 2026-10-08 view on (`rules.ACCESSIBLE_FROM`), two additions. A `dataset:` tag whose value
   is a Python list, such as `['tasksource/bigbench', 'suicide_risk']`, is read as the repo id inside
   the list (`tasksource/bigbench`); the other item is a subset name and is not looked up as a repo.
   And `accessible_data.csv` can keep a model when that row names a training file or a dataset page
   that was opened. `access` is `file_opened`, `kaggle_page`, or `hub_dataset`. A row is an explicit
   admission. The Hub-exists check still runs first; the row is used only when the card's own dataset
   name is missing or is not on the Hub. Views dated before 2026-10-08 do not read this file.
3. Exactly one parent (`baseModels`, card `base_model`, `base_model:` tags); parent passes rule 1; parent class is
   `instruction`. From 9 October the class comes from `parents.csv` when the parent has a row there (an agent read
   the parent's own card under `agents/PROMPT-parent-class.md`; Mark's definition: the chat or instruct
   post-training of a pre-trained base counts, by vendor or community, rehosts take the original's class; a
   tune of an already-instruct model is `finetune`); otherwise by YAML tag, then README sentence, then repo-name
   token, as before, and the parent is listed in `parents_unregistered.csv`.
   Meta's Llama 3 card is one file served on both `Meta-Llama-3-8B` and `Meta-Llama-3-8B-Instruct`;
   until 6 Oct its sentence "For our instruction tuned model, we conducted extensive red teaming"
   classed the *base* repos as instruction-tuned, and 18 PKU-Alignment `ProgressGym-HistLlama3-*-pretrain`
   safety models (parent `Meta-Llama-3-8B` / `-70B`) passed this step. That sentence and "was
   pretrained on over 15 trillion tokens" are now skipped as family text, so neither Llama 3 card
   is classed by its README; `-Instruct` is classed by the name token and the base repos are
   `parent_not_stated`. On the 6 October view that change took safety from 106 to 88 at the endpoint and
   left mental health unchanged (those are that day's numbers, not the current safety count).
   Still step 3: the child's `config.json` and the parent's must agree on architecture, `vocab_size`
   (the child may have up to 1,024 more tokens, for added special tokens), `hidden_size`, and
   `num_hidden_layers`. A field missing on either side is not compared. This is a check on the
   card's parent claim, not a comparison of weight tensors. Loss reasons: `parent_discordant` (a
   value differs), `config_unreadable` (either side has no `config.json` on the Hub, or the file is
   not JSON; `parent_config_check` says which), `repo_gated` (the Hub answered 401/403 for either
   side's `config.json`; access can be requested). Added 5 October after
   `menzo-ai/mental-health-chatbot` (card: Llama 3 8B; weights: Llama 2 vocabulary) and
   `JaeJiMin/daily_hug` (card: Gemma 2 2B; weights: Gemma 1 2B) were found. Its own step 4 until 9 October.
4. Pass manual review (the endpoint). `manual_removals.csv` (`grouping, hf_id, decided_on, category, reason`)
   lists models a person read and removed. `category` is the figure row the removal is counted under;
   `reason` is the person's words. On 9 October the mental-health categories were collapsed to six:
   `not a mental-health model`, `not an English-language model`, `redundant with a kept model`
   (named `duplicate of a kept model` until 13 Oct 2026 16:49; the row covers quantized copies,
   re-uploads, and near-identical variants of a kept model, so "duplicate" overstated it),
   `card says training is incomplete`, `scorer, not a conversational model`, and `one of 11 variants
   from one paper; gemma pair kept`. The finer distinctions (medical, safety, persona, Turkish, Chinese)
   stay in `reason`. A row applies only to its grouping and only once its `decided_on`
   date is on or before `--as-of`, so an earlier view is unchanged. Removed models carry decision
   `manual_removed`, the category in `manual_category`, and the reason in `manual_reason`; they are
   not in `kept.csv`. `counts.csv` lists one step-4 loss per category (`manual_removed: <category>`),
   which the figure prints as "Removed for <category>". A row that applies but names a model that
   did not reach step 4 (a stale row) makes the run exit 2.
   "Duplicate of a kept model" means: same author, same training dataset, same parent, and the same
   recipe as a model that is in `kept.csv`, and either byte-identical weights (Hub sha256) or a card
   that says this upload is the earlier or deprecated build of the kept one. The kept twin is named
   in `reason`.
5. Training method named. Two sources, either counts. (a) `agent_methods.csv`: the objective (sft, dpo, ...) or
   update scope (full, lora, qlora) an agent read in the card, preprint, or training script, recorded as
   `agent:<value>` with the URL (9 Oct; this is how a method stated only in a preprint counts). (b) The card
   text: LoRA, QLoRA, SFT, DPO, GRPO, PPO, RLHF, or "full fine-tune" / "full-parameter
   fine-tuning", recorded as `full_finetune`) in README or tags, or as a whole token of the repo name
   (`lora`, `qlora`, `sft`, `dpo`, `grpo`, `ppo`, `rlhf`, split on `-` `_` `.`; added 6 October;
   `method_evidence` then reads `name <token>`). "no LoRA", "without LoRA", "non-LoRA", "instead of
   LoRA" do not count as LoRA. From 9 October a method word inside a URL, a repo or dataset id
   (`SAGI-1/Greetings_DPO_dataset_V1`), an inline code span, or a `dataset:` tag does not count, and a
   "full fine-tune" phrase in a sentence that also names LoRA/QLoRA ("QLoRA enables full fine-tuning on two
   T4s") is not recorded as `full_finetune`. Note the
   `methods` column mixes two kinds of label: LoRA / QLoRA / full fine-tune say which weights were
   updated; SFT / DPO / GRPO / PPO / RLHF say what objective was trained. A card that says only
   "LoRA" has not said whether the objective was SFT or DPO. Step 6 fixes that.
6. Training objective known (added 10 October 2026; the mental-health endpoint). The model has a row in
   `docs/<grouping>_FT_funnel/decisions/objective-evidence.csv` (columns `hf_id, objective, stages,
   evidence_level, basis, decided_by, decided_on`; rows dated after `--as-of` are ignored) whose
   `evidence_level` starts with `1` (stated: the objective word is on the card or in a source the card
   links) or `2` (inferred from the author's own words or toolchain: a description of supervised
   training without the word, or training code / config showing a causal-LM `Trainer` or `trainer: sft`).
   Level `3` (assumed from the data format alone) stops the model as `objective_assumed_only`; no row
   stops it as `no_objective_evidence`. `kept.csv` gains `objective`, `objective_stages` (every stage
   in order, `sft|dpo`), and `objective_evidence_level`. How the mental-health file was built (hand
   reading, Grok validation, blind test against the DPO/GRPO cards) is in
   `docs/mental_health_FT_funnel/how-models-are-filtered.md`, "Training objective and update scope".

## Code changes log (since 9 Oct 2026)

- **13 Oct 17:50, `figure.py` / `doc_counts.py`**: box labels replaced with Mark's wording (15:25–16:05); the keyword
  search is its own first box (`SEARCH_BOX`); steps 5 and 6 are drawn as one box, "Training method documented by the
  author", with one removal line (`MERGED_IN_FIGURE`; Mark 17:47: both steps stay in the code and in `counts.csv`).
  `doc_counts.py` says so under the table. Figures redrawn for all three groupings.
- **13 Oct 17:34–17:50, `version_rule.py`** `EXPECTED_INPUT` mental-health 30 → 23, safety 37 → 36 after the objective
  re-read (Mark approved 17:34; `docs/funnel-review/2026-10-13/objective-reread/proposal.md`): 11 mental-health and 3
  safety rows of `objective-evidence.csv` re-levelled; `funnel.py` and `figure.py` rerun for all three groupings as of
  2026-10-13 (`outputs/funnel/<g>/2026-10-13/`; medical still 53); `doc_counts.py --write` ×3; both tests pass.
  `family_figure.py` (30/21/52) and `model_tables.py` (30/30/52) pin the post-version-rule counts and are not touched
  until the version rule is rerun.
- **13 Oct 16:49–17:10, data files only (no code)**: `manual_removals.csv` category `duplicate of a kept model`
  renamed `redundant with a kept model` on 39 rows (Mark, 16:49). `parents.csv`: the four DeepSeek-R1-Distill
  rows keep class `instruction` with Mark's reason appended (16:49: DeepSeek's post-training of the base
  includes instruction data). `docs/safety_FT_funnel/decisions/objective-evidence.csv`: five `jsl5710/Shield-*`
  rows `2 inferred` → `1 stated` (Mark, 16:05: a card that states the loss function states the objective).
  Funnels not yet rerun; `counts.csv` and the count tables still carry the old category name until they are.
  Re-read of all 67 mental-health and safety objective rows: `docs/funnel-review/2026-10-13/objective-reread/proposal.md`,
  awaiting Mark.

- **13 Oct 15:10, `funnel.py` / `figure.py` / `version_rule.py`**: medical endpoint moved from step 4 to step 6
  (Mark Kalinich, 13 Oct 14:54). `FINAL_STEP_BY_GROUPING["medical"]`
  and `ENDPOINT_BY_GROUPING["medical"]` added; `EXPECTED_INPUT["medical"]` 97 → 54. Medical `kept.csv` is now the
  step-6 survivors (`outputs/funnel/medical/2026-10-13/counts.csv`: step 4 84, step 5 75, step 6 54). Same change as
  mental health (10 Oct) and safety. `version_rule.py` still stops on medical parents without a lineage rule in
  `family_figure.classify_parent` (the list it prints); those rows are the next item.
- **13 Oct 15:05, `tools/write_objective_evidence.py`**: hand-reading rows may now carry the objectives
  `continued_pretraining` and `distillation` beside sft/dpo/grpo/orpo/kto/ppo/unknown. Reason: three medical cards
  state continued pre-training (`microsoft/MediPhi-Clinical`, `-PubMed`, `MilyaShams/…-continual-pretrain-merged`) and
  one states chain-of-thought distillation (`taksa1990/…-DoRA`); the script used to stop on them, which would have
  forced either a false `sft` or a false `unknown`. The row records what the author said; whether such a model stays in
  a study of fine-tunes was decided by hand (see `docs/medical_FT_funnel/decisions/`). `funnel.py`
  step 6 does not read the objective value, only the level, so these rows pass step 6 as level 1.
- **13 Oct 12:20, `agents/PROMPT-extract.md` v5 → v6** (Mark, 13 Oct 11:55: "i approve of the split of role into
  those three fields and keeping a separate output kind field"). No model had been read with v5. The single-valued
  `role` field and `intended_user` are replaced by `purpose_stated` (yes/no), `audiences` (zero or more of patient or
  public, clinician, student or exam taker, researcher or developer, plus one free-text named group) and `functions`
  (zero or more of 21 phrases taken from the cards). Reason: the card survey of 10 Oct
  (`docs/medical_FT_funnel/agent-searches/2026-10-10-card-survey/roles-survey.md`, 81 cards) found 41 of the 57 cards
  that state a purpose name more than one job, so one `role` per model misdescribes most of them. `output_kind`,
  `clinical_task`, `specialty` unchanged. v5 kept as `PROMPT-extract-v5.md`. `prompt_version` in the JSON is 6.
- **13 Oct 12:00, `version_rule.py`** safety pin 38 → 37: `bfuzzy1/Railz-R` removed as an earlier version of the kept
  `Railz-R2` (Mark, 13 Oct 11:55: keep only the final version); `outputs/funnel/safety/2026-10-13/`.
- **10 Oct 14:40, `agents/PROMPT-extract.md`** (Mark, 14:20: "let's extract the medical specific fields: intended user, what role the model was supposed to play, whether it's a chatbot, what output it's supposed to give, clinical task, specialty"): version 5, the medical variant. Version 4 (safety) is kept as `agents/PROMPT-extract-v4.md`. v5 drops the safety `detection_claim` block, brings back the v3 `use_claim` and `warning` scales reworded for medical use, and adds `intended_user`, `role`, `clinical_task`, `specialty`; `output_type` (chatbot or not) and `output_kind` stay. Nothing else in the prompt changed. Not yet used for any run.
- **10 Oct 13:45, `rules.py`** (Mark, 13:40: "if that's true then I think we can count the multimodal instruction
  tune as the parent model"): the step-3
  config check no longer counts `Qwen3_5ForCausalLM` (child) against `Qwen3_5ForConditionalGeneration` (parent) as
  a different architecture. The Qwen3.5 releases are one network with a vision encoder and a language model; a
  fine-tune saved with a text-only loader keeps the language model and drops the encoder, and the encoder only runs
  when an image is given, so text in gives the same text out. New helper `_text_only_export`: child name ends in
  `ForCausalLM`, parent name ends in `ForConditionalGeneration`, same prefix. The reverse direction and every other
  field (vocabulary, width, depth) are unchanged. Models that moved from `parent_discordant` are listed in the
  per-grouping decision files (safety row 7, Decided).

- **10 Oct 12:50, `rules.py`** (Mark, 12:46: "I approve of us making this change"; found by the adversarial
  review of the medical dataset-search pool, `docs/medical_FT_funnel/agent-searches/2026-10-10-dataset-search/pool-cut-review.md`
  finding 7): `ROOT_CKPT` also matches `model.safetensors-00001-of-00002.safetensors`, the shard name Qwen3.5
  releases and their fine-tunes use. Before, those repos stopped at step 1 as `no_root` without their dtype
  summary being read (medical 23 cohort models, safety 6, mental health 1 on the 10 Oct runs; parents
  `Qwen/Qwen3.5-0.8B`, `-4B`, `-9B`). The dtype rule itself is unchanged. Medical rerun the same day; safety and
  mental health were rerun afterwards (see the dated folders under `outputs/funnel/`).

- **10 Oct, `funnel.py`** (Mark, 11:34: "re: endpoint mismatch make it match MH. it should be for step 6"):
  `FINAL_STEP_BY_GROUPING` gains `"safety": 6`, and `figure.ENDPOINT_BY_GROUPING` the same (the two tables must
  agree; `doc_counts.py` reads the figure's). Safety's `kept.csv` is now the step-6 survivors (37, levels 1-2 in
  `docs/safety_FT_funnel/decisions/objective-evidence.csv`) instead of the step-4 survivors (44). No rule
  changed; only which step's survivors are the study set. Medical stays at step 4.

- **10 Oct, `cache.py`** (Mark, 10:45: "make the smallest change necessary"): a dated README, config.json or
  dataset-README entry that is a fetch error (`FETCH_ERR ...`) may now be replaced on the same UTC day by real
  content (`_write_text_once`). Reason: a repo opened to the token after its 403 had been cached could not be
  re-read until the next UTC day (12 safety pages waited on this on 10 Oct). Content never replaces content
  and an error never replaces anything, so `--as-of <date>` means the same thing as before. The re-read itself
  is `tools/refetch_repos.py`.

- **10 Oct, `funnel.py`, `figure.py`, `doc_counts.py`** (approved by Mark, confirmed safe with the safety
  agent): step 6 "training objective known" added after step 5, reading
  `docs/<grouping>_FT_funnel/decisions/objective-evidence.csv`. The endpoint is now per grouping
  (`FINAL_STEP_BY_GROUPING`: mental-health 6, others 4). Four kept files are written per run (above).
  Mental health: new run `outputs/funnel/mental-health/2026-10-10/`, `kept.csv` 29 (steps 1–5 unchanged from the
  9 Oct run: 49 and 35). Safety and medical: `kept.csv` unchanged; their `decisions.csv` gained the three
  objective columns and a step-6 row per step-5 survivor. Pins 49 → 29 in `version_rule.py`,
  `model_tables.py`, `family_figure.py`. `mh_card_review_doc.py` now checks the review CSV against
  `kept_after_review.csv` and marks the study set in a column. Regression test asserts step 6 keeps nobody
  in the 2 Oct view (no evidence rows dated then).

- **10 Oct 00:20, `collect_extractions.py`**: reads prompt v4 records (safety) as well as v3: six new columns in `extractions.csv` and `card_review_agent.csv` (`input_kind`, `output_kind`, `detection_claim_kind`, `detection_claim_categories`, `detection_claim_quote`, `detection_claim_url`); `use_claim` and `warning` are read with `.get` so a v4 record without them no longer raises. Reason: the safety extraction runs under v4, which has no claim or warning scale (Mark, 9 Oct 21:15).

- 9 Oct 2026, 21:20 (approved by Mark): `funnel.py` `Run.run()` now clears `unregistered_parents` at the
  start of every pass. With `--fetch` the run repeats `decide()` until nothing is missing; before this
  change each pass appended the same children again, so `outputs/funnel/<grouping>/<date>/parents_unregistered.csv`
  listed every child once per pass and `n_children` was inflated (the parent set was right). No decision
  changes. The safety run of the evening of 9 Oct was built with the inflated file; its assignments were
  made from the de-duplicated child lists.
- 9 Oct 2026, 21:20: `agents/PROMPT-extract.md` v3's JSON template said `"prompt_version": 2`; corrected to 3.
  The 9 Oct records already carry 3 (the agents wrote the header's version).

## Git

`cache/` holds ~95 MB including files over the repo's 10 MB soft gate (`cards/`, `catalog/`). Ask Mark
before committing them. `persisted/` under `reviewer_2_experiments/` is the frozen source the cache was
seeded from; it is unchanged.
