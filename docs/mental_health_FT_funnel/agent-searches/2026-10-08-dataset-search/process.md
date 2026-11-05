# Step-2 dataset search, 8 October 2026

## What was found

Checked 8 October 2026. All 50 assigned models with no dataset name are in, including `reports/no-dataset-7`.

**66 models whose named dataset was missing on the Hub: 22 recovered.** These are all of the `not_found` rows. The other 9 of the 75 `dataset_not_on_hub` rows are the Python-list tags in the last section. They were not searched.

The 22 models are 10 corpora:

- DailyDialog files on GitHub: 7 `mario-rc` models.
- AnnoMI file on GitHub: `RyanDDD/bert-motivational-interviewing`. Two other cards link the same file and their code example names the RyanDDD repo: `coding-zzz-oe/bert-motivational-interviewing`, `CounselReflect/bert-motivational-interviewing`.
- Kaggle `suchintikasarkar/sentiment-analysis-for-mental-health`: `abdullahmazhar51`, `kingabzpro`, `maitry30`. The Hub id on the card still does not load.
- Three AIMH no-questionnaire checkpoints. Each card names a `_finetune` dataset that loads. The id that was missing is a different name.
- `Gojosen/mental-health-distilbert`: Kaggle `entenam/reddit-mental-health-dataset`.
- `kashyaparun` notebook loads `google-research-datasets/go_emotions`.
- `boltuix/NeuroFeel` notebook names `boltuix/emotions-dataset`. The dataset card says 131,306 rows. The model card says about 10,000.
- `sihyeonmoon/moodtown-emotion-model`: AI Hub emotional-dialogue corpus, dataset number 86.
- `techhy/mindtrack-mental-health-analyzer`: `cleaned_mental_health_data.csv` in the author's GitHub repo.
- `TheCarBun/GPT-2-fine-tuned-mental-health`: `intents.json` in the author's GitHub repo. The card also says `kaggle`. No Kaggle page was found.

**50 models with no dataset name on the 6 October card: 8 recovered.** These are the 50 assigned in the two waves. 1,849 of the 1,899 were not searched.

- `AndresR2909/Llama-3_2-1B-suicide-related-text-classification`: notebook loads `PrevenIA/spanish-suicide-intent`. That page loads. The upload commit is in this repo.
- `SoufianeDahimi/child_trauma_gemma_finetune`: `trauma_assessment_training.jsonl` on GitHub opens. The card's dataset tag is the word `custom`, which the funnel drops.
- `munyew/meralion-singlish-mental-health-emotion-v1`: `munyew/singlish-mental-health-emotion-v1-prepared` loads. The script that builds `features.jsonl` was not found.
- `Vishalshendge3198/spark_tts_finetune`: `Vishalshendge3198/Dataset_eleven_v3` loads. The files open after the visitor accepts the conditions.
- `0xMori/gemma-2-9b-safori-cbt-merged`: the current card names a custom Korean counseling set of about 400 dialogues. No Hub id.
- `damian-shivihs/yllia-safety-classifier`: the card says the project is based on 1,369 original Polish questions, plus synthetic variants. No file and no Hub dataset id.
- `AventIQ-AI/distilbert-mental-health-prediction`: the current card says `Kaggle - Combined Data.csv` and gives no URL. The seven labels match the Kaggle set already opened for the three models above. The card does not name that URL.
- `Jayasimha01/spotify-genre-mood`: `Yegor25/lyrics_genre_dataset_large`. This is a genre classifier. The corpus is song lyrics.

`ChrisLalk/mistral-7b-therapy-speaker-id` was marked recovered and then changed to not recovered. The card says about 1,500 German transcripts from public sources and does not name the sources.

This search does not edit the 6 October `kept.csv`, `decisions.csv`, or `agent_fields.csv`. It asks whether a paper, a training script, a dataset card, or the current model card names a training corpus for models that failed step 2 of the mental-health funnel on 6 October 2026.

From 8 October the funnel also keeps a model when the training data were opened. `revision_3_experiments/hf_inventory/accessible_data.csv` has 26 rows: a file that opened, a Kaggle page that loaded, or a Hugging Face dataset that loads under a different id. The nine Python-list tags are not in that file. The funnel reads the repo id inside the list. Four recovered models are not admitted: `sihyeonmoon/moodtown-emotion-model` (an AI Hub catalog page; the file was not opened), `0xMori/gemma-2-9b-safori-cbt-merged` (a name and no file), `AventIQ-AI/distilbert-mental-health-prediction` (a filename and no URL), and `damian-shivihs/yllia-safety-classifier` (a count of questions and no file).

The 35 admitted models were run through the later filters. The result is `revision_3_experiments/hf_inventory/results/mental-health/archive/2026-10-08/accessible-screen.csv`. 25 stop at the parent check. 10 pass the parent check, the config check, and manual review. 4 of those 10 also name a method word: the three AIMH no-questionnaire checkpoints and `SoufianeDahimi/child_trauma_gemma_finetune`. The other 6 are the `KBhandari11` Llama-2-7b-chat models. A draft removal for those six was written in the method note on 6 October. On 9 October those six rows, and one for `AIMH/SQPsychLLM-8b-command-no_questionnaire`, were entered in `manual_removals.csv`; the list after manual review became 41 (`results/mental-health/CURRENT`). The sentence "The 6 October study list is still 38" that stood here was true on 8 October only.

The funnel row is `revision_3_experiments/hf_inventory/results/mental-health/archive/2026-10-06/decisions.csv`. Step 2 entered 2,234 models and kept 243. It dropped 1,899 as `no_dataset`, 75 as `dataset_not_on_hub`, and 17 as `vision_or_video`.

The model ids assigned to agents are `sample.csv` in this folder. Wave is the column `wave`. Each agent's markdown and CSV are in `reports/`. This folder keeps `process.md` and `sample.csv` only.

## What the two step-2 failures are

`no_dataset` means `rules.named_datasets` found nothing in `cardData.datasets` and nothing in a `dataset:` tag, after dropping junk words. The card did not name a dataset.

`dataset_not_on_hub` means the card did name something, and `hub.dataset_status` did not return `ok` or `gated` for any of those names. Two statuses are stored in `dataset_hub_status`:

- `not_found`. The Hub had no dataset repo by that name on 6 October 2026. There are 66 of these.
- `invalid_name`. The string is not a Hub repo id. There are 9 of these. All 9 are `KBhandari11` models. The tag is the text of a Python list, for example `['tasksource/mmlu', 'high_school_psychology']`. The checker sent that whole string as one repo id. Hugging Face rejected it. These 9 are not 404s. They are not in `sample.csv`. See the last section.

"Account" in the wave-1 sample means the text before the slash in the repo id. `vincenzoooooo/saskia-sonja-frida-2-agreeableness` is the account `vincenzoooooo`. The 66 `not_found` rows belong to 40 accounts. One account had 10 of those rows. Another had 7.

## What an agent counts as recovered

Read the newest cached card if one exists: `revision_3_experiments/hf_inventory/cache/readmes/<account>__<name>__YYYY-MM-DD.md`. If none, fetch `https://huggingface.co/<account>/<name>/raw/main/README.md`.

Then search for a paper, a training script, or a dataset card. A dataset is recovered only when a source names a training corpus and that source is about this repository: it prints this repo id, or the same authors describe this checkpoint. A word in the repo name is not a dataset. A paper about a different checkpoint is not this model's dataset.

For `no_dataset`, the 6 October card had no dataset name. If the current card now names one, that counts, and `source_type` is `current_model_card`.

For `not_found`, repeating a name that still does not load is not a recovery. Recovery means a corpus that can be opened: a Hub dataset page that loads, a file in a repository, or a paper that contains the data. Check the dataset page, not only `https://huggingface.co/api/datasets/<name>`. On 8 October that JSON address returned HTTP 401 both for missing names and for a made-up name, so 401 from the JSON address is not evidence the dataset exists. A dataset page that returns 401, rather than the Hub 404 page, may be a private repo. Say so. Do not call it recovered unless a file opens.

Do not download model weights.

CSV columns, one row per model, same order as the assignment:

`hf_id,recovered,data_name,data_hub_id,source_type,source_url,source_names_this_repo,quote,queries_tried`

`recovered` is `yes` or `no`. `source_type` is `paper`, `training_script`, `dataset_card`, `current_model_card`, or `none`. `source_names_this_repo` is `yes` or `no`. `quote` is one sentence. `queries_tried` separates search strings with ` | `.

## Wave 1 assignment

Date of search: 8 October 2026. Ten agents, five models each.

`no_dataset`. Pool of 1,899, sorted by repo id, lowercase. Take index `i * 1899 // 25` for `i` from 0 to 24. Files `no-dataset-1` through `no-dataset-5`.

`not_found`. Start from the 66, not from the 75. Group by account. Sort the account names. Take index `i * 40 // 25` and the first repo id of that account. This was done so one agent would not be given four copies of the same Big Five model. A straight every-kth draw of the 66 does that. Files `dataset-404-1` through `dataset-404-5`.

## Wave 1 result

`no_dataset`: 2 of 25 recovered.

- `0xMori/gemma-2-9b-safori-cbt-merged`. The current card names a custom Korean counseling set of about 400 dialogues. No Hub dataset id. No paper.
- `Jayasimha01/spotify-genre-mood`. The training script names `Yegor25/lyrics_genre_dataset_large`, which is on the Hub. The checkpoint is a genre classifier. The corpus is song lyrics, not a mental-health corpus.

`not_found`: 10 of 25 recovered. Three of the ten are the same Kaggle dataset, `suchintikasarkar/sentiment-analysis-for-mental-health` (`abdullahmazhar51`, `kingabzpro`, `maitry30`). The Hub id on the card still does not load. The Kaggle page does.

The other seven:

- `AIMH/SQPsych-8b-gemma-Qwen_no_questionnaire` trains on `AIMH/SQPsychConv_gemma_no_questionnaire_finetune`. That is a different Hub id from the one that 404'd, and it loads.
- `coding-zzz-oe/bert-motivational-interviewing` links `github.com/uccollab/AnnoMI`, and `AnnoMI-simple.csv` opens. The same card's code example names `RyanDDD/bert-motivational-interviewing`.
- `Gojosen/mental-health-distilbert` links the Kaggle set `entenam/reddit-mental-health-dataset`, and that page opens.
- `mario-rc/emotional-dialogpt-large` points at DailyDialog files in `github.com/Mario-RC/emotional-gpt` and `github.com/CHANEL-JSALT-2020/datasets`. Those files open. The Hub name `DailyDialog` still does not load.
- `sihyeonmoon/moodtown-emotion-model` names the AI Hub emotional-dialogue corpus at `aihub.or.kr`, dataset number 86. That page loads.
- `techhy/mindtrack-mental-health-analyzer` trains on `cleaned_mental_health_data.csv` in `github.com/Soham-droid-pixel/Mind_Track_Project`. That file opens.
- `TheCarBun/GPT-2-fine-tuned-mental-health` trains on `intents.json` in `github.com/TheCarBun/GPT2-mental-health`. That file opens. The card also says `kaggle`. No Kaggle page was found.

Two names that were not recovered returned HTTP 401 on the dataset page, not the Hub 404 page: `rabiaqayyum/autotrain-data-mental-health-analysis` and `rhaymison/mental-health-qa`. Those repos may be private.

## Wave 2 assignment

Started 8 October 2026, after wave 1. Not finished when this file was written.

`not_found`. All 41 rows that were not in wave 1. Sorted by repo id. This is not a sample. Files `dataset-404-6` through `dataset-404-13` have five models. `dataset-404-14` has one model, `vladinc/bigfive-regression-model`. Several accounts already had one model in wave 1. The sibling in wave 2 is still a separate row. A sibling is recovered only if a source names that repository. The wave-1 file for the sibling is not, by itself, a recovery.

`no_dataset`. Another 25, no overlap with wave 1. Same sorted pool of 1,899. Wave 1 is the even positions of a 50-point grid, index `i * 1899 // 25`. Wave 2 is the odd positions, index `(2*i+1) * 1899 // 50`. Files `no-dataset-6` through `no-dataset-10`.

## The nine Python-list tags

Do not send these to a paper search first. The tag is a two-item list. The first item is a Hub dataset id. The second item is a config of that dataset. Checked on 8 October 2026: `tasksource/mmlu` exists and has a config `high_school_psychology`. `tasksource/bigbench` exists and has a config `suicide_risk`.

Three models name the MMLU pair. Six name the BigBench pair. All nine are `KBhandari11`, `dataset_source` is `dataset_tag`, and `dataset_hub_status` ends in `invalid_name`. If the tag were split, the dataset-exists check would see a Hub dataset that loads. That would change the step-2 decision for these nine. It would not put them in the study. Later steps would still have to run.

The note in `docs/mental_health_FT_funnel/how-models-are-filtered.md` about three suicide-risk KBhandari rows is a different decision. That note is about manual review. These nine never reached manual review. They failed step 2.
