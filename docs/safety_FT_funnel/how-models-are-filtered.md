<!-- doc-verbosity: public-ready -->

# How safety models are filtered

Last updated: 9 October 2026. Mental health is `docs/mental_health_FT_funnel/how-models-are-filtered.md`. Medical is `docs/medical_FT_funnel/how-models-are-filtered.md`. The steps are one script, `revision_3_experiments/hf_inventory/funnel.py`; the rules are `rules.py`; the operator notes are `revision_3_experiments/hf_inventory/README.md`. The same code runs for all three groupings; only the query file, the manual-removal rows, and the dataset admissions differ.

The current run is the date in `revision_3_experiments/hf_inventory/results/safety/CURRENT`. Previous passes (`2026-10-05`, `2026-10-06`, `2026-10-09`) are under `results/safety/archive/`. Do not quote them as the current funnel.

## The funnel

The table below is written by `doc_counts.py --grouping safety --write` from that run's `counts.csv`. `tests/test_docs_match_counts.py` fails when the two disagree. Do not edit the table by hand.

<!-- counts:begin -->
Current run: `outputs/funnel/safety/2026-10-17/` (the date in `outputs/funnel/safety/CURRENT`). Hub data fetched 2026-09-24 to 2026-10-13.

| Step | What it keeps | Entered | Kept | Removed, by reason |
|---:|---|---:|---:|---|
| 1 | 16- or 32-bit text-compatible model weights available | 8,743 keyword matches | **4,624** | 3,928 no Hugging Face-format checkpoint at the repo root (adapter-only, GGUF-only, subfolder, or no weights)<br>180 quantized weights (U8, I8, I32, F8, ...)<br>10 pytorch_model.bin header could not be read<br>1 gated or private repo; access not yet approved (can be requested) |
| 2 | Training dataset specified | 4,624 | **924** | 3,605 no dataset named<br>55 vision or video pipeline<br>40 named dataset is not on the Hub |
| 3 | One full-precision, instruction-tuned parent | 924 | **220** | 250 no parent model named<br>195 parent is a speech, vision, or embedding model<br>164 parent model is pre-trained<br>39 parent model is also a fine-tune<br>22 two or more parent models named<br>11 config.json differs from the declared parent's (architecture or shape)<br>10 no available full-precision parent model<br>7 gated or private repo; access not yet approved (can be requested)<br>4 parent model could not be read<br>2 config.json absent or not readable (model or parent) |
| 4 | AI-assisted manual review | 220 | **44** | 48 not a safety model<br>30 backdoor research organism, not a safety model<br>27 returns a reply, not a safety judgment<br>24 needs an image or video as input<br>13 judges something other than content harm<br>10 not an English-language model<br>8 card does not state the task<br>8 refusal removal, not a safety model<br>4 redundant with a kept model<br>1 earlier version of a kept model<br>1 needs another model's token probabilities as input<br>1 scorer, not a conversational model<br>1 weights do not fit on the 96 GB GPU |
| 5 | Fine-tuning method named | 44 | **40** | 4 fine-tuning method not stated by the model author |
| 6 | **Training method documented by the model author** (the study set, `kept.csv`) | 40 | **35** | 5 training objective not stated by the model author |

Step 6 is the end of the funnel; its survivors are `kept.csv`. Survivors of step 4 are `kept_after_review.csv`, of step 5 `kept_method_stated.csv`, of step 6 `kept_objective_known.csv`.
The figure (`funnel.png` in the run folder) draws the keyword search as its own first box and steps 5 and 6 as one box, "Training method documented by the author", with one combined removal count; this table keeps the two steps apart (`figure.MERGED_IN_FIGURE`).
<!-- counts:end -->

**What step 4 asks (written 10 October 2026, after the fit review).** A model stays only if a person, reading its
card, finds that it (1) takes a text conversation or a single user message as input (no image, video, or another
model's internals required), (2) returns a judgment of whether the content is unsafe (a label, a category, a score,
a verdict with reasoning, or a structured object), and (3) judges content harm rather than prompt injection, agent
tool calls, code, robot plans, or organisation policy. Safety-aligned chat models that answer or refuse but emit no
judgment do not stay. Self-harm and suicidal ideation are the cases that matter; whether the card names them is
recorded (`agent-searches/2026-10-09-fit-review/fit-review.csv`, `covers_self_harm`) but is not itself a removal
reason. The removal categories on the safety rows of `manual_removals.csv` are the reasons a model failed this.

What each step does, in one line each (the full rule text is in `revision_3_experiments/hf_inventory/README.md`, section "Rules"):

1. **Keyword match, full precision.** The cohort is every model returned by the Hub for any term in `queries/safety.csv` (24 free-text searches and 2 exact tag filters, `safety` and `content-moderation`). A model stays when a root `model.safetensors` (or `pytorch_model.bin`) holds only F16, BF16, or F32 tensors (I64 counters and BOOL masks allowed; a blank Hub dtype summary is read from the file header). LoRA adapters, GGUF, and other quantized files do not count as weights.
2. **Not an image-only or video-only model; training dataset specified.** The model's `pipeline_tag` is not `image-classification`, `image-segmentation`, `video-classification`, or `image-to-text` (nothing else about the model type is checked at this step; multimodal `image-text-to-text` models, classifiers, speech, and untagged models pass), and the card's `datasets:` field or a `dataset:` tag names a dataset that exists on the Hub, or an alias row in `dataset_aliases.csv` maps the card's informal name to one, or a hand-entered row in `accessible_data.csv` (a training file or dataset page a person opened) admits the model.
3. **Exactly one full-precision, instruction-tuned parent.** The card names one parent (`base_model`), that parent passes the step-1 weight rule, its class is `instruction` (the class comes from `parents.csv` when the parent has a row there, else from the YAML/README/name regex; parents without a row are listed in the run's `parents_unregistered.csv`), and the model's `config.json` agrees with the parent's on architecture, vocabulary size (child may add up to 1,024 tokens), hidden size, and layer count. Until 9 October the `config.json` check was drawn as its own step; it is now a loss reason inside this step.
4. **Manual review.** A person read each remaining card. Removals and the reason are rows in `manual_removals.csv` with `grouping = safety`. Survivors: `kept_after_review.csv` (the end of the funnel until 10 Oct 11:34). A safety model here may be a classifier that emits a safe/unsafe label; being a scorer is not a reason to remove one.
5. **Fine-tuning method stated.** The subset of the step-4 survivors whose README, tags, or repo-name tokens name LoRA, QLoRA, SFT, DPO, GRPO, PPO, RLHF, or "full fine-tune", or for which `agent_methods.csv` records an objective or update scope an agent read in the card, a preprint, or a training script (`kept_method_stated.csv`).

Two checks are not the same check. The funnel decides which models are in the study. The agent searches (`agent-searches/`) do not remove a model; they record, for a model already in the study or for a model that failed step 2, what a paper, training script, or dataset page says about its data and method.

## Training objective and update scope (after step 5)

The rule is the mental-health one (`docs/mental_health_FT_funnel/how-models-are-filtered.md`, same section):
for every model that passes step 5, record the training objective with an evidence level — **1 stated** (the word is
on the card or in a linked source), **2 inferred from the author's own words or toolchain**, **3 assumed from data
format alone** — and the update scope (full, LoRA, QLoRA, rank), checked against the weights. Levels 1 and 2 are the
analysis set. Two things are specific to safety. Models trained in more than one stage keep every stage in the
author's order in a `stages` column (`sft|grpo`), and the last stage is the objective (Mark, 10 Oct). And the blind
test behind level 3 fails for this pool: with the objective words blanked, only 3 of 13 RL-trained cards still carry
a preference, reward or rollout word ("policy" means the moderation policy here), so level-3 rows say `unknown`
rather than "assumed SFT".

For the 40 models that passed step 5 at 00:41 on 10 October (`decisions/objective-evidence.csv`): level 1 = 27,
level 2 = 10, level 3 = 3; analysis set 37 (SFT 24, GRPO 11, DPO 2); 10 multi-stage. A Grok agent checked every
row (`agent-searches/2026-10-10-objective-validation/validation.csv`: 36 confirmed, 3 weaker, 1 not supported;
all applied). Weights (`revision_3_experiments/hf_inventory/results/weight-diff/2026-10-10-safety/card-vs-weights.csv`):
38 of 40 pairs compared; card and weights agree for 30; 5 cards give no scope and the weights say full; 2 cards are
contradicted (`nvidia/Nemotron-3-Content-Safety`, rank 16 stated, rank 8 found; `DloadingX/GuardTrace-VL-3B`, LoRA
r=32 stated, full-rank uniform change found); 1 repo's root weights are exactly its parent, with the adapters left
unmerged in subfolders (`BSC-LT/salamandra-7b-instruct-guard`); 2 have no run. Reading rules and the account:
Since 10 Oct 11:34 (Mark: "make it match MH") step 6 is the safety endpoint: `kept.csv` is the 37
(`kept_objective_known.csv`); the 44 step-4 survivors are `kept_after_review.csv`.

**13 October 2026.** Every row was re-read under the tightened definitions (mental-health doc, same section,
"Tightened on 13 October"; six agents, reviewed, Mark approved 17:34). Changes: the five `jsl5710/Shield-*` rows and
`BSC-LT/salamandra-7b-instruct-guard` are level 1 because the card states the loss function (cross-entropy);
`iwalton3/sycofact` is level 2 (the objective word is in the author's script, not on the card);
`lordChipotle/SuicidePreventionLlama` is level 3 (LoRA and toolchain defaults only) and left at step 6, so `kept.csv`
is **36** (`results/safety/2026-10-13/counts.csv`). `yushaohan/ProGuard-3B` stays level 2: the paper has one
recipe, pure GRPO, and presents the 3B as the same system (Mark, 17:34: count it). The manual-review row
`duplicate of a kept model` is now `redundant with a kept model`.

## After the funnel: the final model list

The funnel's `kept.csv` is still the step-6 list. The safety and medical figures draw one box after that, "Final model list," with the thick border. Mental health does not draw it. The count is not a row of `counts.csv`.

A safety model stays when `revision_3_experiments/safety_native/cohort.py` lists it in `USABLE_IDS`. That means the card gives a prompt and a label we can score, and the reply was that label. The removal lines are "family and version has no mental-health fine-tune," "card has no prompt and label to score," and "did not produce the label the card names."

The family-and-version cut is a removal line on that box, not its own box. `version_rule.py` writes `version_rule_kept.csv` and `version_rule_removed.csv` into `results/cross-grouping/<day of the run>/` and names that folder in `results/cross-grouping/CURRENT`. The figure reads those files, then keeps the ids in `USABLE_IDS`.

## Parent class

The parent-class rule (classes, evidence sources, exclusions, what is not evidence) is one rule for all groupings and is written once, in `docs/mental_health_FT_funnel/how-models-are-filtered.md`, section "Parent class". Mark's definition of 9 October: pre-train → instruct **by anyone** is `instruction` (vendor or community; a rehost takes the original's class); instruct → more tuning is `finetune`; a base with no post-training is `pretrained`. From 9 October every parent that reaches step 3 should have a `parents.csv` row; the regex is the fallback and the run lists the parents it had to fall back on.

## What changed on 9 October 2026

In short: one lock-in refetch so every artifact carries one date; the safety parents were read by agents under `agents/PROMPT-parent-class.md` and entered in `parents.csv`; the text-generating models that fail step 2 were searched for a dataset by agents under `agents/PROMPT-dataset-search.md` v2; every kept model has an extraction record under `agents/PROMPT-extract.md` v3; `agent_methods.csv` counts at step 5; this folder was restructured.

## Where the other records are

| What | Where |
|---|---|
| Current run (decisions, kept list, counts, figure, provenance, unregistered parents) | `revision_3_experiments/hf_inventory/results/safety/<CURRENT>/` |
| Search terms and tag filters | `revision_3_experiments/hf_inventory/queries/safety.csv` |
| Manual removals (who, when, why) | `revision_3_experiments/hf_inventory/manual_removals.csv`, `grouping = safety`; the unapproved drafts are `decisions/unapproved-removals.md` |
| Training data opened by hand (step-2 admissions) | `revision_3_experiments/hf_inventory/accessible_data.csv`, `grouping = safety` |
| Parent classes | `revision_3_experiments/hf_inventory/parents.csv`; the safety agents' CSVs and assignments are `agent-searches/2026-10-09-parent-registry/` |
| Extraction records of the kept models (prompt v4: data, method, parent, serving, input kind, output kind, detection claim) | `agent-searches/2026-10-10-extraction/` (44 records); flattened in the current results folder as `extractions.csv`, `agent_fields.csv`, `card_review_agent.csv`. The 9 October v3 records are `agent-searches/2026-10-09-extraction/` |
| Fit review of the kept list (text in, judgment out, suicidal ideation) | `agent-searches/2026-10-09-fit-review/` |
| Dataset search for models that failed step 2 | `agent-searches/2026-10-09-dataset-search/` |
| 6 October literature search (agent write-ups, 38 rows) | `agent-searches/2026-10-06-literature/` |
| 6 October card reading, query-coverage measurement, bug notes | `archive/2026-10-06/card-reading-2026-10-06.md` |
| Downloaded weights | `/home/mkalinich/hf_models/<org>__<name>/` (outside the repo); `download.py --grouping safety --dry-run` lists what is missing |
