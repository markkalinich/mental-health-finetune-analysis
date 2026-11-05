# Dataset search, 2026-10-08

Five models whose 2026-10-06 funnel row had no entry in `cardData.datasets` and no dataset tag. A dataset is recorded only when a paper, a training script, a dataset card, or the current model card names a training corpus and is about that repository.

## 0xMori/gemma-2-9b-safori-cbt-merged

Recovered: yes.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/0xMori__gemma-2-9b-safori-cbt-merged__2026-10-05.md`. The live README is the same text. The Hub API still has no `datasets` field and no dataset tag. The Training Data section names the corpus.

Sentence: "Custom Dataset (Safori CBT): 인지행동치료 이론을 바탕으로 자체 구축한 고품질 한국어 상담 대화셋 (약 400건)."

That is a custom Korean counseling dialogue set of about 400 items, built from cognitive behavioral therapy theory. No Hugging Face dataset id is given.

URL: https://huggingface.co/0xMori/gemma-2-9b-safori-cbt-merged

Also checked: arXiv queries for the repo id and for Kong Yoonseo plus Safori (no papers); GitHub org https://github.com/safori-team (service repos, no training script for this checkpoint). The same author's Gemma 3 cards, `0xMori/gemma-3-safori-cbt-v1` and `0xMori/gemma-3-safori-cbt-merged`, name AI-Hub wellness dialogue scripts and the emotional dialogue corpus. Those cards describe the Gemma 3 checkpoint, not this one.

## AingeruBeOr/SuicideDetectionOnTweets-enhanced

Recovered: no.

The cached card files from 2026-10-02 and 2026-10-05 contain only a fetch error. The live README URL returns 404. The repo has `config.json` and `training_args.bin`, and no README. `config.json` names the starting model `cardiffnlp/twitter-xlm-roberta-base`. The saved training arguments name the output folder `./results` and do not name a corpus.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: https://huggingface.co/AingeruBeOr (author Aingeru Bellido; the only datasets are legal RAG sets); GitHub https://github.com/AingeruBeOr (no suicide-tweet training repo; `GrAL` has no project description); arXiv for the repo id (no hits) and for author Bellido plus suicide (one paper on smartphone phenotyping, which does not print this repo id). Papers and GitHub repos about other suicide-tweet classifiers do not mention this checkpoint. The word "tweets" in the repo name is not a dataset. `AingeruBeOr/SuicideDetectionOnTweets` is a different checkpoint and also has no README.

## almafaz/roberta-depression-detection-v3

Recovered: no.

Cached card: `revision_3_experiments/hf_inventory/cache/readmes/almafaz__roberta-depression-detection-v3__2026-10-05.md`. The live card matches. It says the model is a fine-tuned version of `roberta-base` on the None dataset, and the training-data section says more information is needed. "None" is what the Trainer writes when no dataset name was passed. It is not a corpus name. `config.json` labels are "Not Depressed" and "Depressed". The saved training arguments record only the output directory `almafaz/roberta-depression-detection-v3`.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: https://huggingface.co/almafaz (four RoBERTa checkpoints, no datasets); GitHub user `almafaz` (only a profile page); arXiv for the repo id (no hits). The LT-EDI 2022 RoBERTa papers and repos name other models, including `rafalposwiata/roberta-large-depression` and `paulagarciaserrano/roberta-depression-detection`. They do not print this repo id. The v1, v2, and hpc cards from the same account also say "None" and do not describe this checkpoint.

URL of the card that does not name a corpus: https://huggingface.co/almafaz/roberta-depression-detection-v3

## aravindsr/flan-t5-base-emotional_reaction-classification

Recovered: no.

Cached card: `revision_3_experiments/hf_inventory/cache/readmes/aravindsr__flan-t5-base-emotional_reaction-classification__2026-10-05.md`. The live card matches. It says the model is a fine-tuned version of `google/flan-t5-base` on the None dataset, and the training-data section says more information is needed. The saved training arguments name the output folder and do not name a corpus. The Hub user has no public datasets.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: https://huggingface.co/aravindsr (ResearchGate name Aravind Sesagiri Raamkumar); GitHub https://github.com/aravindsr (no Flan-T5 training repo); arXiv for the repo id (no hits). Two papers by that author, https://arxiv.org/abs/2310.08017 and https://arxiv.org/abs/2407.18538, use "emotional reaction" as an empathy score for other models. They do not print this repo id. The words in the repo name are not a dataset.

URL of the card that does not name a corpus: https://huggingface.co/aravindsr/flan-t5-base-emotional_reaction-classification

## BrettC/gemma-psychology-finetune

Recovered: no.

Cached card: `revision_3_experiments/hf_inventory/cache/readmes/BrettC__gemma-psychology-finetune__2026-10-05.md`. It is the empty Hub template. The Training Data line is "More Information Needed." The live card is the same. `config.json` names the starting model `google/gemma-2b-it`. The Hub user has no public datasets. The card prints no author name beyond the account, and no paper or GitHub URL.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: https://huggingface.co/BrettC (other Gemma fine-tunes use the same empty template; they are different checkpoints); arXiv for the repo id (no hits); Featherless repeats the empty card. A GitHub repo that fine-tunes Gemma on `jkhedri/psychology-dataset` does not mention `BrettC/gemma-psychology-finetune`. The storyteller card's arXiv id `1910.09700` is the carbon-emissions calculator paper, and that card is a different checkpoint.

URL of the card that does not name a corpus: https://huggingface.co/BrettC/gemma-psychology-finetune
