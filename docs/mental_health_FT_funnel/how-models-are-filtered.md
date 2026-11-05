<!-- doc-verbosity: public-ready -->

# How mental-health models are filtered

Last updated: 15 October 2026. Safety is `docs/safety_FT_funnel/how-models-are-filtered.md`. Medical is `docs/medical_FT_funnel/how-models-are-filtered.md`. The steps are one script, `revision_3_experiments/hf_inventory/funnel.py`; the rules are `rules.py`; the operator notes are `revision_3_experiments/hf_inventory/README.md`.

The current run is the date in `revision_3_experiments/hf_inventory/results/mental-health/CURRENT`. `results/mental-health/2026-10-09/` is the pass before step 6 existed. It holds the extraction records, download log, and agent card review of that pass (`extractions.csv`, `download_log.csv`, `card_review_agent.csv`, `data_named_where.csv`), which were not re-made. Its manual-review list differs from the current one by two models: `giannor/Qwen3.5-27B-psysafe` was added on 10 October and `howardbaik/gemma-4-E4B-it-mentalchat16k` was removed on 15 October. Older dated folders under `results/mental-health/archive/` are previous passes; each has its own `counts.csv`. Do not quote them as the current funnel.

## The funnel

The table below is written by `doc_counts.py --grouping mental-health --write` from that run's `counts.csv`. `tests/test_docs_match_counts.py` fails when the two disagree. Do not edit the table by hand.

<!-- counts:begin -->
Current run: `outputs/funnel/mental-health/2026-10-15/` (the date in `outputs/funnel/mental-health/CURRENT`). Hub data fetched 2026-09-22 to 2026-10-13.

| Step | What it keeps | Entered | Kept | Removed, by reason |
|---:|---|---:|---:|---|
| 1 | 16- or 32-bit text-compatible model weights available | 6,617 keyword matches | **2,257** | 4,150 no Hugging Face-format checkpoint at the repo root (adapter-only, GGUF-only, subfolder, or no weights)<br>205 quantized weights (U8, I8, I32, F8, ...)<br>4 pytorch_model.bin header could not be read<br>1 gated or private repo; access not yet approved (can be requested) |
| 2 | Training dataset specified | 2,257 | **378** | 1,820 no dataset named<br>41 named dataset is not on the Hub<br>18 vision or video pipeline |
| 3 | One full-precision, instruction-tuned parent | 378 | **101** | 142 no parent model named<br>69 parent model is pre-trained<br>29 parent model is also a fine-tune<br>19 no available full-precision parent model<br>7 parent is a speech, vision, or embedding model<br>4 two or more parent models named<br>3 config.json differs from the declared parent's (architecture or shape)<br>2 parent model could not be read<br>1 config.json absent or not readable (model or parent)<br>1 gated or private repo; access not yet approved (can be requested) |
| 4 | AI-assisted manual review | 101 | **49** | 28 not a mental-health model<br>7 one of 11 variants from one paper; gemma pair kept<br>6 redundant with a kept model<br>4 not an English-language model<br>3 scorer, not a conversational model<br>2 card says training is incomplete<br>1 cannot be served: layers 24-41 omit key and value projections<br>1 needs an image as input |
| 5 | Fine-tuning method named | 49 | **35** | 14 fine-tuning method not stated by the model author |
| 6 | **Training method documented by the model author** (the study set, `kept.csv`) | 35 | **22** | 13 training objective not stated by the model author |

Step 6 is the end of the funnel; its survivors are `kept.csv`. Survivors of step 4 are `kept_after_review.csv`, of step 5 `kept_method_stated.csv`, of step 6 `kept_objective_known.csv`.
The figure (`funnel.png` in the run folder) draws the keyword search as its own first box and steps 5 and 6 as one box, "Training method documented by the author", with one combined removal count; this table keeps the two steps apart (`figure.MERGED_IN_FIGURE`).
<!-- counts:end -->

What each step does, in one line each (the full rule text is in `revision_3_experiments/hf_inventory/README.md`, section "Rules"):

1. **Keyword match, full precision.** The cohort is every model returned by the Hub for any term in `queries/mental-health.csv` (63 free-text searches and 107 exact tag filters). A model stays when a root `model.safetensors` (or `pytorch_model.bin`) holds only F16, BF16, or F32 tensors (I64 counters allowed). LoRA adapters, GGUF, and other quantized files do not count as weights.
2. **Not an image-only or video-only model; training dataset specified.** The model's `pipeline_tag` is not `image-classification`, `image-segmentation`, `video-classification`, or `image-to-text` (nothing else about the model type is checked at this step; multimodal `image-text-to-text` models, classifiers, speech, and untagged models pass), and the card's `datasets:` field or a `dataset:` tag names a dataset that exists on the Hub. From 8 October, a hand-entered row in `accessible_data.csv` (a training file or dataset page an agent opened) can also admit a model.
3. **Exactly one full-precision, instruction-tuned parent.** The card names one parent (`base_model`), that parent passes the step-1 weight rule, its class is `instruction` (rule below), and the model's `config.json` agrees with the parent's on architecture, vocabulary size (child may add up to 1,024 tokens), hidden size, and layer count. Until 9 October the `config.json` check was drawn as its own step; it is now a loss reason inside this step.
4. **Manual review.** A person read each remaining card. Removals and the reason are rows in `manual_removals.csv`. Survivors: `kept_after_review.csv` (count in the table above). Until 10 October this was the end of the funnel.
5. **Fine-tuning method stated.** The README, tags, or repo-name tokens name LoRA, QLoRA, SFT, DPO, GRPO, PPO, RLHF, or "full fine-tune" (`rules.training_methods`), or an agent-read record in `agent_methods.csv` names one. Survivors: `kept_method_stated.csv` (count in the table above).
6. **Training objective known.** The model has a row in `decisions/objective-evidence.csv` at evidence level 1 (the objective word is on the card or in a source the card links) or level 2 (inferred from the author's own words or toolchain; definitions below). Level 3 (assumed from the data format alone) is removed. Since 10 October 2026 this is the end of the funnel: `kept.csv` (count in the table above). The decision is `FINAL_STEP_BY_GROUPING` in `funnel.py`; safety (from 12 October) and medical (from 13 October) also end at step 6.

Two checks are not the same check. The funnel decides which models are in the study. The agent searches (`agent-searches/`) do not remove a model; they record, for a model already in the study or for a model that failed step 2, what a paper, training script, or dataset page says about its data and method.

What changed on 15 October 2026:

- `howardbaik/gemma-4-E4B-it-mentalchat16k` is removed at step 4. Layers 24–41 of the release omit `k_proj.weight`, `v_proj.weight`, and `k_norm.weight` (54 tensors: 2,076 in the release, 2,130 in `google/gemma-4-E4B-it`), so vLLM does not load it. Step 6 is 22 (`results/mental-health/2026-10-15/counts.csv`).
- Gemma 4 then has no mental-health model. `version_rule.py` drops `Banaxi-Tech/BananaMind-V2.5-Content-Safety`, `tzchen07/rai-gemma4-e2b-5b-safety-dora-r64-fullfix`, and `lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical` from `results/cross-grouping/2026-10-14/final_models.csv`. Those three remain in their own grouping's `kept.csv`.
- `SoufianeDahimi/child_trauma_gemma_finetune` stays. Its local `config.json` `torch_dtype` fields are `bfloat16` (the Hub file is `float16`). The audio tower's `gradient_clipping` value is 10000000000, which does not fit in float16, and vLLM died in that init before any reply. The weight files were not rewritten. One completion returned `yes`.

What changed on 13 October 2026 (funnel review, `docs/funnel-review/2026-10-13/`):

- Every objective row was re-read under the rules written for medical (section "Training objective and update scope" below, "Tightened on 13 October"): step 6 went from 30 to **23** (`results/mental-health/2026-10-13/counts.csv`). Steps 1–5 are unchanged (50 and 36). That run is `results/mental-health/2026-10-13/`.
- The manual-review row `duplicate of a kept model` is now `redundant with a kept model` (same rows, new name; Mark, 16:49).
- `lordChipotle/SuicidePreventionLlama` had been in both the mental-health and the safety kept lists; it left both at step 6.

What changed on 10 October 2026:

- (Morning run of 10 October. `results/mental-health/2026-10-10/` was rewritten that evening when `giannor/Qwen3.5-27B-psysafe` was kept, so its `counts.csv` shows 50, 36, and 30.) Step 6 added and made the end of the funnel for mental health: 35 → 29. The 6 removed are `ArkMaster123/qwen2.5-7b-therapist`, `ShivomH/Elixir-MentalHealth-3B`, `ShivomH/Falcon3-1B-MentalHealth`, `VaisakhKrishna/Llama-2-Emotional-ChatBot`, `mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy`, `sirev/Qlora-lfm2-700m-mental-health`. The current run is `results/mental-health/2026-10-10/`; steps 1–5 are identical to the 9 October run (same 49 and 35).
- `kept.csv` now has three new columns: `objective`, `objective_stages` (every training stage in order, e.g. `sft|dpo` for counseLLM), `objective_evidence_level`.
- The card review (`decisions/card-review/mh-card-review-2026-10-10.csv`) still covers all 49 manual-review survivors; its `.md` has a "Study set" column marking the 29.

What changed on 9 October 2026:

- The `config.json` check moved from its own step into step 3. Step numbers in `decisions.csv` and `counts.csv` became 1 to 5 (1 to 6 again from 10 October, with a different step 6); folders written before 9 October use 1 to 6 with the config check as step 4.
- Manual-removal categories were collapsed to six figure rows. The finer reason stays in the `reason` column.
- `Guilherme34/Psychologist-3b-beta` was relabelled from "duplicate of a kept model" to "card says training is incomplete": the model it duplicated was itself removed the same day, and the beta card carries the same "not yet fully fine-tuned" line.
- The 9 October manual rows remove the six `KBhandari11` Llama-2 pruning models and `AIMH/SQPsychLLM-8b-command-no_questionnaire`. The gemma-corpus AIMH pair on each base stays.

"Redundant with a kept model" (named "duplicate of a kept model" until 13 October 2026) means: same author, same training dataset, same parent, same recipe as a model in `kept.csv`, and the upload is a re-upload, a quantized or merged copy, or a build the card calls earlier or deprecated. Byte-identical weights are the clearest case but not required, which is why "duplicate" was the wrong word. The kept twin is named in `reason`.

## Parent class

This is the wording of the parent-class rule. The full-precision rule that runs is rule 1 in `revision_3_experiments/hf_inventory/README.md`. The 23 September note's full-precision wording is the older rule and is not copied here. The running code is `revision_3_experiments/hf_inventory/rules.py`.


The class is assigned to the **parent**, then carried to each child. Three evidence sources are read in a fixed order. Each is recorded in its own column whether or not it is the one that decides. Nothing about the child is read for this step.

**Classes** (agreed 23 Sep; these describe the parent as a release).

- `pretrained`: the parent is a base release with no post-training.
- `instruction`: the parent is the post-trained instruct or chat release of a base model, published as that release (e.g. `Qwen/Qwen2.5-7B-Instruct`, `meta-llama/Llama-3.1-8B-Instruct`, `google/gemma-2-9b-it`).
- `finetune`: the parent is a further fine-tune of a base or instruct model, i.e. it was trained from some named repo and is not that repo's own instruct/base release (e.g. `ehristoforu/Gemma2-9B-it-psy10k`, `tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3`).
- `conflict`: the card states both an instruct-release claim and a trained-from-another-repo claim. Left for hand resolution; both sentences stored.
- `not_stated`: the card is readable and no source yields a class.
- `unreadable`: the card could not be read (gated 401, 404, or no README).

The Hub's structured relation field cannot make the instruction/finetune distinction: `Qwen/Qwen2.5-7B-Instruct` carries `baseModels.relation = finetune` → `Qwen/Qwen2.5-7B`, exactly as a downstream fine-tune would. The organisation of the parent versus its base is **not** evidence either (a vendor can publish further fine-tunes of its own instruct model). So the distinction rests on what the card says.

**Source 1, `yaml`.** The parent card's YAML front matter (API `cardData` and `tags`).

| YAML evidence | Class |
|---|---|
| a free tag exactly equal to one of `instruct`, `instruction-tuned`, `instruction-tuning`, `chat` | `instruction` |
| a free tag exactly equal to one of `pretrained`, `pre-trained`, `base`, `base-model`, `foundation`, `pretraining` (and no instruct tag) | `pretrained` |
| `baseModels.relation`, `base_model_relation`, `base_model:<relation>:` tags | recorded in `yaml_relation`; **decides nothing** |
| none of the above | empty (fall through) |

Both an instruct tag and a pretrained tag on the same card → empty at this source (fall through), both recorded. (Corrected 5 October: an earlier version of this row also listed `sft`, `rlhf`, `dpo`, `post-trained`, `conversational`. The script never used them; the "Not evidence" paragraph below is what ran, in September and in `revision_3_experiments/hf_inventory/rules.py` `INSTR_TAGS`.)

**Source 2, `readme`.** The parent README body, front matter removed, code blocks removed. Each matched sentence is stored verbatim.

| README evidence | Class |
|---|---|
| "fine-tuned version of <X>", "fine-tuned from <X>", "finetuned from model <X>", "trained on top of <X>", "continually pre-trained from <X>", "further trained from <X>", "full fine-tune of <X>", "this is a <name> fine-tune,", where <X> is a repo id or model name that is not this repo | `finetune` |
| "instruction-tuned", "instruct-tuned", "instruction tuned", "post-trained", "this is the chat model", "aligned with RLHF/DPO", "supervised fine-tuning and RLHF", or a training-stage line naming both pretraining and post-training, stated about this checkpoint | `instruction` |
| "pretrained model on", "pre-trained on", "this is the base model", "pretrained only", "not instruction-tuned", or a training-stage line that is pretraining only | `pretrained` |
| a `finetune` sentence **and** an `instruction` sentence | `conflict` |
| none | empty (fall through) |

Exclusions before matching: family sentences ("both base and instruction-tuned", "pre-trained variants, and instruction-tuned variants", "we release base and instruct", "the instruct model additionally supports" on a base card); corpus-size sentences ("was pretrained on ~N tokens", "was pretrained on up to N tokens"); Unsloth/TRL boilerplate ("export your fine-tuned model", "trained 2x faster"); paper titles; "safety post-training" alone; `from_pretrained` in code.

**Source 3, `name`.** Hyphen- or underscore-delimited tokens of the repo id, case-insensitive. `instruct`, `it`, `chat`, `sft`, `dpo`, `rlhf` → `instruction`. `pt`, `pretrain`, `pretrained` → `pretrained`. The token `base` is a size and is not evidence. Nothing yields `finetune` by name. Stored in `name_evidence`.

**Decision.** `class_final` = first non-empty of `class_yaml`, `class_readme`, `class_name`; `class_source` = which one. `conflict` from the README is terminal (name is not consulted). All empty with README read → `not_stated`. README unreadable and yaml empty → `name` if it speaks, else `unreadable`.

**Reporting.** Parents by `class_final` x `class_source`; children by the same. Classes decided only by `name` sit in their own column so the reader can exclude them. `conflict` rows are listed with both sentences.

**Not evidence.** The child's card or tags. Organisation of parent vs base. `baseModels.relation`. `pipeline_tag`. `chat_template` presence. `torch_dtype`. Download counts. The Hub-generated tag `conversational` (added automatically when a `chat_template` exists). Method tags `sft`, `dpo`, `rlhf` (used by downstream fine-tuners too). The repo-id token `base` (a size in `bert-base-*`, `whisper-base`, `flan-t5-base`).

Rules that were added after inspecting the first run, each because a named card was misclassified: family sentences on base cards ("The Llama 3.x instruction tuned text only models are optimized for...", "The tuned versions use SFT and RLHF"); Hub card boilerplate ("look for fine-tuned versions on a task that interests you"); "instruct fine-tuned version of X" routed to `instruction` (Mistral-7B-Instruct); paper-abstract quotes ("instruction finetuning is a general method"). The script is `reviewer_2_experiments/hf_inventory/persisted/harvest/2026-09-23-funnel/classify_parents.py`.

## Training objective and update scope (step 6)

Step 5 asks only whether *some* method word appears. For the 35 that pass it we recorded two separate facts per
model, with an evidence level each, in `decisions/objective-evidence.csv` (10 October 2026). The file has one row
per model with columns `hf_id, objective, stages, evidence_level, basis, decided_by, decided_on`; `funnel.py`
reads it at step 6 (rows dated on or before `--as-of`).

**Training objective** (SFT, DPO, GRPO). Three levels. **1 stated**: the word is on the card or in a source
the card links (19). **2 inferred from the author's own words or toolchain**: the author describes supervised
training without the word, or the training code or config shows a causal-LM `Trainer` / `trainer: sft` (10).
**3 assumed from data format alone**: a prompt→response dataset, "fine-tuned with (Q)LoRA", and no preference
data or RL word anywhere (6). Mark's rule of 10 October: levels 1 and 2 are the study set (**29**, step 6); level 3
is dropped, and a sensitivity analysis drops level 2 too (the 19 level-1 models; filter `kept.csv` on
`objective_evidence_level` starting with `1`). A Grok agent re-checked every level-1 quote and
every level-2 argument against the source (`agents/PROMPT-objective-validation.md`;
`agent-searches/2026-10-10-objective-validation/`); six rows changed level as a result and two were then
re-read by hand (Piaget ×4, lordChipotle). The blind test behind level 3: with the objective words blanked out
of their cards, the five DPO/GRPO models are still caught by "preference", "chosen/rejected", or "reward".

**Tightened on 13 October 2026** (the medical rules, `docs/funnel-review/2026-10-13/objective-reread/RULES.md`,
applied to every mental-health and safety row by six agents and reviewed; Mark approved 17:34). What counts at
each level, in the words now used for all three groupings:

- Level 1: an objective word (SFT, supervised fine-tuning, instruction tuning, DPO, GRPO, ORPO, KTO, PPO, RLHF)
  on the card, in the model's paper, in the author's linked training code, or as a TRL `sft`/`dpo`/`grpo` tag; a
  stated loss function ("cross-entropy", "next-token prediction") also states SFT (Mark, 13 Oct 16:05).
- Level 2: no objective word, but the author's own code or run artefacts fix it: a trainer class (`SFTTrainer`,
  `DPOTrainer`), `trainer: sft` in a config, or a `trainer_state.json` whose log fields are only
  loss/eval_loss/grad_norm/learning_rate (a DPO or GRPO run logs reward fields). An objective word in the repo
  name counts; `qlora` is not an objective word.
- Level 3: everything else. LoRA, QLoRA, Unsloth, PEFT `task_type`, a prompt→response data format, and
  hyperparameters that match a toolchain's defaults fix nothing, because the same tools run SFT, DPO, GRPO and
  ORPO with those defaults.

Effect on mental health (`results/mental-health/2026-10-13/counts.csv`): seven rows that were level 2 on a
data-format or toolchain-default argument moved to level 3 and left at step 6 (`gustavecortal/Piaget-0.6B`,
`-1.7B`, `-4B`, `-8B`, `lordChipotle/SuicidePreventionLlama`, `sujalrajpoot/TrueSyncAI-Aurion`,
`Compumacy/Psych_Qwen_32B`); four moved from level 1 to level 2 because the objective word is in the author's
code, not on the card (`dzur658/smollm2-mentalhealth-360m-V2`, `prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2`,
`SoufianeDahimi/child_trauma_gemma_finetune`, `thillaic/CBT-Copilot`); `SungJoo/cradle-dialogue-qwen3-32b-2epoch`
stays level 2 on its `trainer_state.json`. The 10 October counts in the paragraph above (19 / 10 / 6, 29) describe
that day's run. Row-by-row record: `docs/funnel-review/2026-10-13/objective-reread/proposal.md`.

**Update scope** (full, LoRA, QLoRA) is checked against the weights, not only the card. `weight_diff.py`
compares each matrix of the fine-tune with the same matrix of the parent on CPU (`results/weight-diff/`).
A merged LoRA of rank *r* leaves a difference of rank *r*: a sharp drop after the *r*-th singular value and
>99% of the energy in the top *r*. Reading rules: drop at *r* → LoRA rank *r* (the card's rank matched in
every case it was given, except Piaget-1.7B, where the drop is at 32 not 8); no drop and a large change →
full fine-tune (11 models, including the 5 that state no scope); no drop but only a few matrices changed →
LoRA on those modules only (`q_proj`/`v_proj`: ShivomH/Falcon3-1B, prabureddy); no drop and a *uniform*
change of 0.2–10% in every matrix → a (Q)LoRA merged into a de-quantised 8-bit or 4-bit base, where the
quantisation error is full-rank and hides the adapter (Compumacy at 8-bit, lordChipotle at 4-bit; confirmed
for lordChipotle by diffing against the base model, which it does not match, while its norms match Instruct
exactly). No card's stated scope was contradicted by the weights. Two models have no weight run
(`ArkMaster123/qwen2.5-7b-therapist`, `VaisakhKrishna/...` with `.bin` weights); both are level 3.

## Where the other records are

| What | Where |
|---|---|
| Current run (decisions, kept list, counts, figure, provenance) | `revision_3_experiments/hf_inventory/results/mental-health/<CURRENT>/` |
| Search terms and tag filters | `revision_3_experiments/hf_inventory/queries/mental-health.csv` |
| Manual removals (who, when, why) | `revision_3_experiments/hf_inventory/manual_removals.csv`; the unapproved drafts are `decisions/unapproved-removals.md` |
| Training data opened by hand (step-2 admissions) | `revision_3_experiments/hf_inventory/accessible_data.csv` |
| Card review of the kept models (claims and warnings) | `decisions/card-review/mh-card-review-<date>.csv` and `.md`, where the date is in `decisions/card-review/CURRENT`; `roster.py` reads that review and stops when a mental-health roster model has no row in it |
| 6 October literature search (agent write-ups, 38 models) | `agent-searches/2026-10-06-literature/` |
| 8 October dataset search (agents, models that failed step 2) | `agent-searches/2026-10-08-dataset-search/` |
| 6 October parent-base review (64-row pre-review file) | `archive/2026-10-06/parent-bases-2026-10-06.md` |
| 6 October card review (38 models) | `archive/2026-10-06/mh-card-review-2026-10-06.*` |
| The 23 September funnel (3,316 / 137 / 56 / 53) | `archive/2026-09-23/hf-inventory-mh-funnel-2026-09-23.md` |
| Downloaded weights | `/home/mkalinich/hf_models/<org>__<name>/` (outside the repo; see the review) |
