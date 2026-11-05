# Dataset search, 2026-10-08

Five models whose 2026-10-06 funnel row had no entry in `cardData.datasets` and no dataset tag. A dataset is recorded only when a paper, a training script, a dataset card, or the current model card names a training corpus and is about that repository.

## SathwikBalu/Mental-Health-7b

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/SathwikBalu__Mental-Health-7b__2026-10-05.md`. The live README is the same empty Hub template. The Training Data line is "More Information Needed." `config.json` names the starting model `NousResearch/Llama-2-7b-chat-hf`. The Hub API `cardData` has no `datasets` field.

The same account has a dataset, `SathwikBalu/mental-health`, created the same morning as this model (1 October 2024). That dataset page loads. It has 3,512 rows and an empty README. It does not name `SathwikBalu/Mental-Health-7b`. The 4-bit sibling card is the same empty template. No paper or training script was found that prints this repo id and a corpus.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: https://huggingface.co/SathwikBalu (thirteen models and six datasets, including `SathwikBalu/mental-health`); arXiv for the repo id (no hits); GitHub search for the repo id (no training repo). The word "Mental-Health" in the repo name is not a dataset.

URL of the card that does not name a corpus: https://huggingface.co/SathwikBalu/Mental-Health-7b

## SoufianeDahimi/child_trauma_gemma_finetune

Recovered: yes.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/SoufianeDahimi__child_trauma_gemma_finetune__2026-10-05.md`. The live card matches. Its `datasets` tag is the single word `custom`, which is why step 2 recorded no dataset. The Training Data section describes conversation examples and report templates and does not name a file. It points to https://github.com/Dahimi/Gemma3n_Finetune_Child_Trauma.

That repository's notebook loads `trauma_assessment_training.jsonl` and uploads the merged weights to `SoufianeDahimi/child_trauma_gemma_finetune`. The README of the same repository names that file and prints this repo id. The file opens: HTTP 200, 5,680,250 bytes. It is not a Hugging Face dataset id.

Sentence: "The generated dataset can be found at `trauma_assessment_training.jsonl`."

URL: https://github.com/Dahimi/Gemma3n_Finetune_Child_Trauma/blob/main/finetuning/trauma_assessment_gemma_finetune.ipynb

## thejefferson29/therapy-ai-tinyllama-onnx-free

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/thejefferson29__therapy-ai-tinyllama-onnx-free__2026-10-05.md`. The live card matches. It says the weights were stripped of ONNX files so they load in `@xenova/transformers`. It does not name a corpus. The Hub API `cardData` has no `datasets` field. The account has no datasets.

An older commit of a different checkpoint, `thejefferson29/therapy-ai-tinyllama-fixed`, put `custom_therapy_dataset` in the card YAML. That commit was replaced, and it does not print this repo id. `custom_therapy_dataset` is not a corpus named for this checkpoint. `thejefferson29/therapy-llama2-7b-colab` says it was trained on an unknown dataset. That card is a different model.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: https://huggingface.co/thejefferson29 (four models, no datasets); GitHub search for `thejefferson29` plus therapy TinyLlama (no repo); arXiv for the repo id (no hits).

URL of the card that does not name a corpus: https://huggingface.co/thejefferson29/therapy-ai-tinyllama-onnx-free

## Vishalshendge3198/spark_tts_finetune

Recovered: yes.

The cached card from 2026-10-05 is `FETCH_ERR INACCESSIBLE_403`. The live card now names the corpus. The Hub dataset page loads. The dataset API marks it `gated: manual`: the page is public, and the parquet opens only after the visitor accepts the conditions. The API lists one train split of 2,408 rows and a 223 MB parquet. The dataset README is empty.

Sentence: "The model was fine-tuned using LoRA (Low-Rank Adaptation) on the curated `Vishalshendge3198/Dataset_eleven_v3` German dataset."

URL: https://huggingface.co/Vishalshendge3198/spark_tts_finetune

Dataset page: https://huggingface.co/datasets/Vishalshendge3198/Dataset_eleven_v3

## youralien/roberta-Empathy-goodareas-classifier-sweeps

Recovered: no.

The cached cards from 2026-10-02 and 2026-10-05 are `FETCH_ERR MISSING`. The live README URL returns 404. The repo has `config.json`, `training_args.bin`, and weights, and no README. `config.json` names the starting model `FacebookAI/roberta-large`. The labels are "not selected" and "selected".

Ryan Louie, the account name on https://huggingface.co/youralien, is an author of https://arxiv.org/abs/2505.02428. That paper says RoBERTa-large binary classifiers were fine-tuned on `youralien/feedback_qesconv_16wayclassification` and tuned on `youralien/CARE_10percent_16wayclassification`. Both dataset pages load. The CARE set is manually gated. The paper does not print `youralien/roberta-Empathy-goodareas-classifier-sweeps`. Sibling cards, including `youralien/roberta-Empathy-goodareas-eval_FeedbackESConv5pp_CARE10pp-sweeps-current`, say the model was trained on the None dataset. They do not describe this checkpoint. The GitHub repo `youralien/streamlit-annotation-care-quality` is an annotation app and does not name this checkpoint.

No paper, training script, or dataset card was found that names a training corpus for this repository.

URL of the repo that has no card: https://huggingface.co/youralien/roberta-Empathy-goodareas-classifier-sweeps
