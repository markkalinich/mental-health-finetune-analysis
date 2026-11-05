# Dataset search, 2026-10-08

Five models whose 2026-10-06 funnel row had no entry in `cardData.datasets` and no dataset tag. A dataset is recorded only when a paper, a training script, a dataset card, or the current model card names a training corpus and is about that repository.

## aditya0304/moodmentor-distilbert

Recovered: no.

The cached card `revision_3_experiments/hf_inventory/cache/readmes/aditya0304__moodmentor-distilbert__2026-10-05.md` is a fetch error. The live README URL returns 404. The repo has `config.json` and `model.safetensors`, and no README. `config.json` is a DistilBERT sequence classifier with six labels stored as `LABEL_0` through `LABEL_5`, and `problem_type` `multi_label_classification`. It does not name a corpus. The Hub user `aditya0304` (Aditya Bhole) has no datasets. The sibling checkpoints `moodmentor-bert`, `moodmentor-distilbert-onnx`, and `moodmentor-bert-onnx` also have no README and the same unlabeled six-way head.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: https://huggingface.co/aditya0304 (four MoodMentor checkpoints, no datasets); GitHub https://github.com/aditya0304 (no public repositories); arXiv for the repo id (no hits) and for moodmentor plus DistilBERT plus Aditya (no hits); Kaggle user `aditya0304` (404). A Devpost project named MoodMentor AI uses `twitter-roberta-base-sentiment` and does not mention this checkpoint. A Medium DistilBERT emotion tutorial is by a different Aditya and does not print this repo id. The word "moodmentor" in the repo name is not a dataset.

URL of the repo that does not name a corpus: https://huggingface.co/aditya0304/moodmentor-distilbert

## alfiyahqthz/mentalbert-mental-health-npair-lamb7

Recovered: no.

The cached card is a fetch error. The live README URL returns 404. The Hub API `cardData` is empty. `training_metadata.json` records epoch 3, lambda 0.7, six classes, loss type `npair`, and validation F1 0.842. It does not name a corpus. `config.json` is a BERT masked-language-model config and does not name a corpus. The Hub user has no datasets.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: arXiv for the repo id (no hits); GitHub user `alfiyahqthz` (404). The same author, Alfiyah Qothrunnada Zulfa, is on the IEEE paper "MentalBERT with Contrastive Learning for Mental Disorder Classification from Social Media" (DOI 10.1109/ICCRAIDS67816.2026.11519647). The abstract says the experiments use social-media posts and six mental-disorder classes, and it reports an N-pair macro F1 of 84.8%. The abstract does not name a corpus and does not print this repo id. The paper is not open access. This account also has other N-pair checkpoints (`lamb1`, `lamb3`, `lamb5`, `lamb9`). A result for N-pair in general is not this lambda-0.7 checkpoint.

URL of the repo that does not name a corpus: https://huggingface.co/alfiyahqthz/mentalbert-mental-health-npair-lamb7

## AndresR2909/Llama-3_2-1B-suicide-related-text-classification

Recovered: yes.

The cached card and the live README are the empty Hub template. The Training Data line is "More Information Needed." `config.json` names the starting model `meta-llama/Llama-3.2-1B-Instruct`. `handler.py` is a Spanish prompt that asks for label 1 or 0. It does not name a corpus.

The training notebook does. `Fine_tuning_Llama_3_2_v3.ipynb` in https://github.com/AndresR2909/Suicide-Intent-Detection-NLP-Model-Comparison loads `hf://datasets/PrevenIA/spanish-suicide-intent/` and fine-tunes `meta-llama/Llama-3.2-1B-Instruct`. It uploads the result as `Llama-3_2-1B-suicide-related-text-classification` plus a date. The notebook output records commit `e3158df7afa6a27fe373d0e3dbd03994651f3276` on `AndresR2909/Llama-3_2-1B-suicide-related-text-classification_09-10-2024_18_14`. That address now resolves to this repository, and this repository's history contains that same commit ("Upload tokenizer", 2024-10-09).

Sentence: "The dataset consists of comments from several sources translated to Spanish language and classified as suicidal ideation/behavior and non-suicidal."

That sentence is in the project README and on the dataset card. The Hub dataset page https://huggingface.co/datasets/PrevenIA/spanish-suicide-intent loads. The card says 175,010 Spanish comments, label 1 for suicidal ideation or behavior and 0 otherwise.

URL: https://github.com/AndresR2909/Suicide-Intent-Detection-NLP-Model-Comparison/blob/main/Fine_tuning_Llama_3_2_v3.ipynb

Also checked: arXiv for the repo id (no hits). The same GitHub project fine-tunes a Llama 3.1 8B and a Llama 3.2 3B on the same dataset and uploads those under other repo names. Those uploads are different checkpoints. The 1B notebook is the one that matches this repository's commit.

## AventIQ-AI/distilbert-mental-health-prediction

Recovered: yes.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/AventIQ-AI__distilbert-mental-health-prediction__2026-10-05.md`. The live README is the same text. The Hub API still has no `cardData` and no dataset tag. The model-details list names the corpus.

Sentence: "Dataset: Kaggle - Combined Data.csv."

The training section says the dataset is taken from Kaggle and has combined information on mental health issues. The card does not give a Kaggle user, a Kaggle slug, or a Hugging Face dataset id. The usage example maps seven labels: Anxiety, Normal, Depression, Suicidal, Stress, Bipolar, and Personality disorder.

URL: https://huggingface.co/AventIQ-AI/distilbert-mental-health-prediction

Also checked: arXiv for the repo id (no hits); GitHub https://github.com/AventIQ-AI (two repositories, neither names this checkpoint); the Hub user has no datasets.

## ChrisLalk/mistral-7b-therapy-speaker-id

Recovered: no. The card describes the transcripts and says the public sources are not named. That description is not a corpus that can be opened. The agent had marked this yes. The row was changed to no on review, because the write-up itself says the sources are unnamed.

The cached cards from 2026-10-02 and 2026-10-05 are fetch errors (403). The raw README URL still returns 401: the repo is gated (`gated: auto`), and the files require accepting the conditions. The model page shows the card text without that download. The Hub API `cardData` has the base model `mistralai/Mistral-7B-Instruct-v0.3`, language `de`, and tags for LoRA, QLoRA, and speaker classification. It still has no `datasets` field. The Training Data section of the page names the corpus.

Sentence: "The model was fine-tuned on German two-person psychotherapy transcripts drawn from multiple public sources."

The next sentence says the training data contained approximately 1,500 transcripts of psychotherapy sessions, and that no training data is included in the repository. The card does not name those public sources and does not give a Hugging Face dataset id.

URL: https://huggingface.co/ChrisLalk/mistral-7b-therapy-speaker-id

Also checked: arXiv for the repo id and for author Lalk plus therapy plus speaker (no hits). The Codeberg project https://codeberg.org/PsyRes-UOS/psyannote is by the same group and uses a local LoRA adapter for therapist-versus-patient labels. Its model card leaves Training Data as "More Information Needed," and the sample config does not print this repo id. The paper that names `ChrisLalk/German-Emotions` trains that other checkpoint on a German translation of GoEmotions. That paper is not this model's dataset.
