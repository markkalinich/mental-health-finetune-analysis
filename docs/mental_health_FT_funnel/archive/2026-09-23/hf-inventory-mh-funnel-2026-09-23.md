<!-- doc-verbosity: public-ready -->

# Methods note: mental-health Hugging Face funnel, 23 September 2026 rebuild

The current filter is [how-models-are-filtered.md](../../how-models-are-filtered.md); the current study set is `results/mental-health/<CURRENT>/kept.csv` (the date in `results/mental-health/CURRENT`). This file is the 23 September rebuild and the 2 October table. It is not the current filter. (An earlier version of this line said the study set was the 38 models of 6 October; that was true on 6 October only.)

This note describes one funnel with one stated rule per step. Every step writes a kept-id file and a per-id loss file under `reviewer_2_experiments/hf_inventory/persisted/harvest/2026-09-23-funnel/`. Counts in this note are read from those files.

This funnel supersedes the mental-health keyword box in [hf-inventory-filter-path.md](../reviewer_2_experiments/zArchive/docs-2026-10-07/hf-inventory-filter-path.md). That earlier note remains the record of the 55-model result and of the medical path. Two of its rules are **not** used here:

- Using the repo name as the only evidence of instruction tuning. The repo name is used only when the parent card's YAML and README do not state a class.
- The 20 September tag lists. Here the tag list is derived by rule from the 23 September search hits.

## Definitions

**Search hit.** A model id returned by `GET /api/models?search=<term>&sort=downloads`. The Hub matches `search=` against the repo id text.

**Tag hit.** A model id returned by `GET /api/models?filter=<tag>&sort=downloads`. `filter=` matches one exact tag string on the model card.

**Full-precision checkpoint.** (1) The file list has a checkpoint at the repository root whose path equals `model.safetensors` or matches `model-<digits>-of-<digits>.safetensors`; one such file is enough; files inside folders, adapter files, and `*.safetensors.index.json` do not count. (2) The safetensors parameter record is present, non-empty, and every dtype code is one of F16, BF16, F32. `config.json`, the model name, and GGUF tags are not read.

**Named parent.** One `org/name` repo id taken from `baseModels.models[].id`, the card `base_model` field, or a `base_model:*` tag. A value with no slash is not a repo id. The model's own id is not a parent. Two different `org/name` values means the model does not have one parent.

**Parent class.** One of `finetune`, `instruction`, `pretrained`, `not_stated`, `unreadable`, assigned to the parent from three evidence sources checked in order, each recorded in its own column. The Hub has no structured field for instruction-tuned or pretrained; `baseModels.relation` takes only `finetune`, `adapter`, `merge`, `quantized`.

1. `yaml`: the parent card's YAML front matter (`tags`, `base_model_relation`, `base_model:<relation>:` tags, `pipeline_tag`). Raw values stored.
2. `readme`: a sentence in the parent README that states this checkpoint's status, quoted verbatim. Family boilerplate that names both a base and an instruct variant does not qualify.
3. `name`: `instruct`, `it`, `chat`, `sft`, `dpo`, or `rlhf` as a token in the parent repo id. The token `base` is a size (`bert-base`) and is not evidence. A corpus sentence ("pre-trained on N languages", "was pretrained on ~N tokens", "was pretrained on up to N tokens") does not classify the checkpoint.

`class_final` is the first source that speaks; `class_source` records which.

## Step 1. Search

56 terms, no `CBT`. 5,727 hit-rows, **5,560** unique ids. Files: `../2026-09-23-search/query-log.csv`, `unique-ids.txt`.

## Step 2. Tag expansion

Rule: read the `tags` field of the 5,560 search-hit cards; drop infrastructure tags by a fixed rule; the author approves the mental-health subject tags; run `filter=` once on the approved tags plus the 56 search terms as exact tags.

Drop rule (`tag-dropped.csv`, 1,894 tags): `prefix` (`region:`, `license:`, `arxiv:`, `doi:`, `base_model:`, `dataset:`, ...), `plumbing` (libraries, frameworks, quantization, trainer, format tags), `pipeline` (Hub task tags), `architecture` (model-family names), `language_code_2letter`, `kv_blob` (`key: value` text stored as a tag).

Census (`tag-census.csv`): **800** tags. Mental-health-looking subset shown for approval (`tag-census-mh-candidates.csv`): 121. Struck by the author (`tag-census-mh-removed-by-mark.csv`): `health`, `support`, `healthcare`, `companion`, `clinical`, `clinical-nlp`, `clinical-assistant`, `clinical-narrative`, `depresso`, `abdominal-trauma`, `destress`, `cbt` (collides with the ISO 639-3 language code; the full tag `cognitive-behavioral-therapy` is kept), `merged_model:ShivomH/Elixir-MentalHealth-3B`. Approved: **120**.

`filter=` run (`filter-tags.csv`, `filter-query-log.csv`): 120 approved tags + 56 search terms, 38 overlapping, **138** tags, all HTTP 200. 5,047 hit-rows, **3,986** unique tag-hit ids. 357 were already search hits; **3,629** were not.

Keyword set (`keyword-ids.txt`): 5,560 + 3,629 = **9,189**.

Note on composition: seven approved tags (`sentiment-analysis`, `sentiment`, `emotion`, `emotion-recognition`, `emotion-detection`, `sentiment analysis`, `emotions`) account for roughly 2,500 of the 3,629 tag-only ids. They were approved as written.

Disorder-name tags absent from every search-hit card (`eating-disorder`, `anorexia`, `bulimia`, `schizophrenia`, `bipolar`, `ptsd`, `panic`) enter only through the "56 search terms as tags" clause.

## Funnel as of 2 October 2026

Not the current filter. The current filter is [how-models-are-filtered.md](../how-models-are-filtered.md).

The figure for this older order is `2026-09-23-funnel/funnel.png`, drawn by `make_funnel_figure.py` from the step files. Each step's kept count plus its losses equals the previous kept count.

| Box | Kept |
|---|---:|
| Listed Hugging Face models | 3,080,963 |
| Full-precision models with matching keyword(s) | 3,316 |
| Text-capable model with both training method and dataset explicitly named | 137 |
| Exactly one full-precision, instruction-tuned parent | 56 |
| Downloaded at least once | 53 |
| Weights match the declared parent (added 5 October) | 51 |

Superseded on 5 October by three further changes, in `revision_3_experiments/hf_inventory/` (README "Rules"): the full-precision rule now lets I64 counters through beside float weights (177 September models had been cut for that alone); "full fine-tune" counts as a training method and "no LoRA" does not count as LoRA; and the `sentiment-analysis`, `emotion*`, `stress`, companion, and one-repository tags were removed from the query list (the 11 financial-sentiment models among the 51 leave with them). The lock-in run on one date will replace this table.

Removed at the full-precision box: 3,071,774 not keyword-matched; 5,873 no full-precision model available (5,519 no root file, 348 a non-float dtype, 6 an empty parameter record).

Removed at the text-capable box, one reason per model. Assignment order is vision or video pipeline first (37: `image-classification`, `image-segmentation`, `video-classification`, `image-to-text`), then no training method named (2,968), then no dataset named (174). `image-text-to-text` stays. Language is not a filter. A training method is LoRA, QLoRA, SFT or "supervised fine-tune", DPO or "direct preference optimization", GRPO, PPO, or RLHF. A card that says QLoRA is recorded as QLoRA only. Files: `documented-kept.txt`, `documented-loss.csv`, `procedure-evidence.csv`.

Removed at the parent box: 24 parent model does not say instruction-tuned, pre-trained, or fine-tune; 18 no parent model named; 18 no available full-precision parent model; 9 parent model is also a fine-tune; 7 parent model is pre-trained; 4 two or more parent models named; 1 parent model could not be read. The 56 children have 28 distinct parents: 5 classified from YAML, 11 from the README, 12 from the repo name. Among the 56 children the deciding source is YAML 8, README 31, repo name 17. That split is in this note. It is not printed on the figure. `google/medgemma-1.5-4b-it` is class `conflict` because the card says both a fine-tune and an instruction-tuned variant. Its child, `jubayer009/medgemma-1.5-4b-mental-health-rag`, left earlier for no dataset named, so the conflict does not appear on the figure. Files: `instruct-parent-kept.csv`, `instruct-parent-loss.csv`, `parent-loss.csv`.

The four children that name `google/gemma-1.3b-it` or `google/gemma-2-270m` are out. Those repositories do not exist. They left at "no training method named" in this ordering. The ids are not rewritten. See `gated-parent-recheck.md`.

Removed at the download box: 3 zero lifetime downloads (`Lixeeone/Emoloom-2B`, `SpaceXerror/cognitive-ai-mental-health-7b`, `theprint/Empathetic-Llama-3.2-3B-Instruct`). Final ids: `final-kept.txt` (53). Manual removal is not applied.

Removed at the weights box (added 5 October, `revision_3_experiments/hf_inventory/rules.py` `parent_discordant`): the child's `config.json` and the declared parent's must agree on architecture, `vocab_size` (the child may have up to 1,024 more tokens), `hidden_size`, and `num_hidden_layers`. Two leave. `menzo-ai/mental-health-chatbot`: card names `meta-llama/Meta-Llama-3-8B-Instruct`; the weights have vocabulary 32,000 (Llama 2) against the parent's 128,256, and the config's `_name_or_path` is `NousResearch/Llama-2-7b-chat-hf`. `JaeJiMin/daily_hug`: card names `google/gemma-2-2b-it`; the weights are `GemmaForCausalLM` with 18 layers and hidden size 2,048 (Gemma 1 2B) against `Gemma2ForCausalLM`, 26 layers, 2,304. Neither can be served with its declared parent's chat template, and neither card's parent claim can be trusted. Final ids after this box: 51 (`revision_3_experiments/hf_inventory/results/mental-health/2026-10-02/kept.csv`).

The 53 before the weights box include two `image-text-to-text` models (`howardbaik/gemma-4-E4B-it-mentalchat16k`, `vanta-research/PE-Type-1-Vera-4B`). `laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft-dpo` is out: its parent card says it is a full fine-tune. Two models have an empty pipeline tag: `SungJoo/cradle-dialogue-qwen3-32b-2epoch` and `lordChipotle/SuicidePreventionLlama`.

The sections below are the 23 September working notes for search, tags, and the first full-precision cut. From "Step 4. Named parent" onward they describe an earlier order. The 2 October table above is also an earlier order.

## Step 3. Full precision

All 9,189 keyword ids have a model row in `../2026-09-23-model-rows/first-pass.csv` (one file, 9,189 rows; the 2,666 tag-only ids without a row were fetched on 23 Sep, all HTTP 200, no fetch errors).

Rule above, applied to the `siblings` and `safetensors` fields of each row.

| Outcome | Models |
|---|---:|
| Kept: root checkpoint, non-empty record, all codes in {F16, BF16, F32} | **3,316** |
| Lost: no root checkpoint file | 5,519 |
| Lost: root checkpoint, empty parameter record | 6 |
| Lost: root checkpoint, a code outside {F16, BF16, F32} | 348 |

3,316 + 5,519 + 6 + 348 = 9,189. Files: `fp-kept.txt`, `fp-loss.csv` (`hf_id, reason, dtype_codes`).

For the figure, Steps 2 and 3 collapse to one box, "keyword-matched models with a full-precision checkpoint: 3,316", with a right-hand loss box carrying two lines: not keyword-matched (3,080,963 − 9,189 = 3,071,774) and keyword-matched without a full-precision checkpoint (5,873). The 9,189 stays in this note as the checkable intermediate.

## Step 4. Named parent, parent full precision

Enters: 3,316.

Parent extraction (`parent-extract.csv`): the three fields in the definition are read; every `org/name` value other than the model's own id is collected; ids are compared case-insensitively.

| Outcome | Models |
|---|---:|
| Names exactly one parent | 1,444 |
| Names no parent | 1,832 |
| Names two or more different parents | 40 |

459 unique parents. 52 already had a row in the keyword file, 231 in the earlier parent fetch, 176 fetched on 23 Sep (171 HTTP 200; 5 NOT_FOUND). Parent rows are in `../2026-09-23-model-rows/parent-first-pass.csv` (416 rows).

The full-precision rule is then applied to the parent's own row.

| Outcome | Models |
|---|---:|
| Kept: one parent, parent is full precision | **888** |
| Lost: no parent | 1,832 |
| Lost: two or more parents | 40 |
| Lost: parent is not full precision | 541 |
| Lost: parent row unreadable (404 or no row) | 15 |

888 + 1,832 + 40 + 541 + 15 = 3,316. Files: `parent-kept.csv` (`hf_id, parent, parent_source_field`), `parent-loss.csv` (`hf_id, reason, parent`). The 888 children have **252** unique parents.

## Step 5. Parent class: definition

The current wording of this rule is in [how-models-are-filtered.md](../how-models-are-filtered.md). This file keeps the 23 September result counts below. It does not keep a second copy of the rule.

## Step 5. Parent class: result

Enters: 888 children, 252 parents. 226 parent cards readable anonymously; 25 gated (401); 1 missing (404).

Parents by `class_final` and by the source that decided:

| parent's class | yaml | readme | name | total parents |
|---|---:|---:|---:|---:|
| instruction | 11 | 23 | 29 | 63 |
| pretrained | 5 | 48 | 1 | 54 |
| finetune | 0 | 35 | 0 | 35 |
| conflict | 0 | 0 | 0 | 0 |
| not_stated | | | | 91 |
| unreadable | | | | 9 |
| total | 16 | 106 | 30 | 252 |

Children grouped by **their parent's** class. The class describes the parent only; every child in this table is a fine-tune of that parent.

| parent's class | yaml | readme | name | total children |
|---|---:|---:|---:|---:|
| instruction | 33 | 60 | 86 | 179 |
| pretrained | 5 | 455 | 1 | 461 |
| finetune | 0 | 51 | 0 | 51 |
| conflict | 0 | 0 | 0 | 0 |
| not_stated | | | | 185 |
| unreadable | | | | 12 |
| total | 38 | 566 | 87 | 888 |

Files: `parent-class.csv` (one row per parent, every source's class and evidence), `child-class.csv`.

Reading notes.

- 86 children are `instruction` by repo name only. 25 of those 29 parents are gated Google/Meta instruct cards (`google/gemma-*-it`, `meta-llama/Llama-*-Instruct`, `meta-llama/Llama-2-7b-chat-hf`) whose README returns 401 anonymously. The other four have a readable card with no status sentence (`GemMaroc/Qwen2.5-7B-Instruct-darija`, `HuggingFaceTB/SmolLM2-*-Instruct`, `naver-hyperclovax/HyperCLOVAX-SEED-Text-Instruct-0.5B`, `OuteAI/Lite-Oute-1-300M-Instruct`, and similar).
- 461 children have a `pretrained` parent, 455 of them by README; the parent cards are encoder cards that open with "Pretrained model on English language using a masked language modeling objective" (`distilbert-base-uncased` 171 children, `bert-base-uncased` 81, `xlm-roberta-base` 51). Of these 461 children, 132 were search hits and 329 entered only through `filter=` tags, chiefly `sentiment-analysis` (189), `sentiment` (41), `emotion` (37), `emotion-classification` (32), `emotion-detection` (16). Examples of the tag-only ones: `AmitAminov/yelp_review_classifier`, `Anant1213/bert-finetuned-imdb`, `Amey9766/BERT-hospitality-review-classifier`. They pass every rule and are not mental-health models.
- Origin of the 888 overall: 264 search hits, 624 tag-only.
- `not_stated` parents with the most children: `distilbert-base-multilingual-cased` (15), `distilgpt2` (10), `dbmdz/bert-base-turkish-cased` (9), `distilbert-base-uncased-finetuned-sst-2-english` (7), `google/flan-t5-base` (7), `google/flan-t5-large` (5). flan-t5 cards have only plural family sentences and a paper quote; they are left for the manual step.
- Known checks: `Qwen/Qwen2.5-7B-Instruct` → instruction (yaml `chat`); `mistralai/Mistral-7B-Instruct-v0.2` → instruction (readme); `meta-llama/Llama-3.1-8B` → `not_stated` (the overview sentence "was pretrained on ~15 trillion tokens" is a corpus sentence and is excluded); `tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3` → finetune (readme "continually pre-trained from meta-llama/Llama-3.1-8B-Instruct"); `ehristoforu/Gemma2-9B-it-psy10k` → finetune (readme "Finetuned from model: unsloth/gemma-2-9b-it-bnb-4bit"); `openai-community/gpt2` → pretrained (readme).

## Step 6. Fine-tune dataset named

Enters: 888. Read from the **child's** row. Structured fields only: the card YAML `datasets:` field, else a `dataset:<name>` tag. Values are split on semicolons and dropped when, lowercased and stripped, they are empty or one of `unknown`, `none`, `synthetic`, `custom`, `private`, `proprietary`, `n/a`, `na`, `data`, `card does not say`. `imagefolder` (7 children) is not on the junk list and is currently counted as a dataset; that is an open decision.

| Outcome | Models |
|---|---:|
| Kept: at least one dataset piece | **445** (439 from `datasets:`, 6 from a `dataset:` tag only) |
| Lost: no structured dataset | 443 |

445 + 443 = 888. Files: `dataset-structured.csv` (per child: source and pieces), `dataset-kept.txt`, `dataset-loss.csv`. README prose was not read for this step. Fraction named is flat across parent class (instruction 50%, pretrained 53%, finetune 51%, not_stated 42%). Most common: `dair-ai/emotion` 34, `stanfordnlp/imdb` 22, `imdb` 13, `go_emotions` 12 + 6, `gustavecortal/PsychologicalReasoning-15k` 12, `Amod/mental_health_counseling_conversations` 7.

## Step 7. Downloaded at least once

Enters: 445. `downloads` on the child's row is lifetime `downloadsAllTime`. Kept when the field is an integer >= 1. A missing field is not treated as zero.

| Outcome | Models |
|---|---:|
| Kept | **435** |
| Lost: zero lifetime downloads | 10 |
| Lost: field missing | 0 |

Files: `downloads-kept.txt`, `downloads-loss.csv`.

## Step 8. Manual removal

Implemented 5 October as step 7 of `revision_3_experiments/hf_inventory/funnel.py`, read from
`revision_3_experiments/hf_inventory/manual_removals.csv` (`grouping, hf_id, decided_on, reason`). A row
applies only once its `decided_on` date is on or before the run's `--as-of`, so the September view is
unchanged. Two rows so far, both dated 5 October: `Huzayfah-Patel/mindbridge-phq9-hindi-merged` (a PHQ-9 /
GAD-7 item scorer that answers with a tool call, not a reply) and `vanta-research/PE-Type-1-Vera-4B` (an
Enneagram Type 1 persona model; no mental-health training data; it entered through the `psychology` tag).
The 5 October view keeps 43 after this step (45 before it).

## Figure

`2026-09-23-funnel/make_funnel_figure.py` reads every count from the step files and the catalog, checks that each step's kept + losses equals the previous kept (exits non-zero otherwise), and writes `funnel.svg` and `funnel.png`. Steps 2 and 3 are one box with a two-line loss box. Step 5 is a split, not a cut; its loss arrow is absent by design.

Run: `.venv/bin/python reviewer_2_experiments/hf_inventory/persisted/harvest/2026-09-23-funnel/make_funnel_figure.py`
