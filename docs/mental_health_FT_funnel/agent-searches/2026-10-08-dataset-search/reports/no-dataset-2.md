# Dataset search, no-dataset batch 2

Checked 2026-10-08. A training corpus is recorded only when a paper, a training script, or a dataset card names that corpus and is about this repository. A description with no dataset name, and a source about a different checkpoint, are not recorded as a recovery.

## CRodas/therapist-response-model

The repository has no README. The cached fetch from 2026-10-05 is missing, and `https://huggingface.co/CRodas/therapist-response-model/raw/main/README.md` returns 404. The Hub profile name is Cesar Rodas. This account has no dataset repos. The config is a GPT-2 model. The training-arguments file stored with the checkpoint names a local output folder, `./my-updated-finetuned-language-model`, and does not name a dataset. The trainer state file records 4 epochs and 9,000 steps and also does not name a dataset.

GitHub users `crodas` and `cesarrodas` have no repository for this model. An arXiv query for `therapist-response-model` returned no paper. `PaulRo230/AI-Therapist` has a notebook named `train_therapist_response_model.ipynb`. That notebook loads `nbertagnolli/counsel-chat` and fine-tunes `t5-small`. It does not mention `CRodas/therapist-response-model`.

No paper, training script, or dataset card names a training corpus for this repository.

https://huggingface.co/CRodas/therapist-response-model

## dlckdfuf141/empathy-kogpt2

The newest cached card is `dlckdfuf141__empathy-kogpt2__2026-10-05.md`. The Hub card was last modified on 2025-06-06, so it is the same text the October 6 funnel already treated as naming no dataset. The author name on the card is the GitHub account `fufckddl`. The Hub profile name is 이창렬. The same text is the README of `https://github.com/fufckddl/KoreanEmpathyModel`, and that README prints `dlckdfuf141/empathy-kogpt2`.

The card says the model was trained on emotion-classified Korean diary data: emotion, diary, and empathy-message pairs, about 35,000 samples. It does not give that data a name or a Hub id. The GitHub repository is a copy of the model files, not a training script. The training-arguments file names a local folder, `./empathy_model`, and does not name a dataset.

A different model by the same author, `dlckdfuf141/korean-emotion-kluebert-v2`, says its training data is the AI Hub emotion-dialogue dataset. That sentence is about the classifier, not this checkpoint. An arXiv query for `empathy-kogpt2` returned no paper.

No paper, training script, or dataset card names a training corpus for this repository.

https://huggingface.co/dlckdfuf141/empathy-kogpt2

## fadodr/mental-health-llama3-4bit

The newest cached card is `fadodr__mental-health-llama3-4bit__2026-10-05.md`. It is the Unsloth upload template. It says the model was fine-tuned from `unsloth/llama-3-8b-bnb-4bit` and does not name a dataset. The Hub profile name is Agboola Fuhad. The card was last modified on 2024-08-12.

The same author has three datasets: `fadodr/mental_health_dataset`, `fadodr/mental_health_cleaned_dataset`, and `fadodr/mental_health_therapy`. None of those dataset cards says they were used to train `fadodr/mental-health-llama3-4bit`. Hugging Face lists eight models trained on `fadodr/mental_health_therapy`. This repository is not one of them.

`https://github.com/fadodr/mental_health_py` contains a training script. The script loads `fadodr/mental_health_therapy` and writes `fadodr/finetuned_mental_health_therapy`. A second file in that repo loads `fadodr/finetuned_mental_health_therapy_original`. Those are different checkpoints. The script does not print `fadodr/mental-health-llama3-4bit`. An arXiv query for this repo id returned no paper about it.

No source names a training corpus for this repository.

https://huggingface.co/fadodr/mental-health-llama3-4bit

## HailNicol/qwen3-14b-suicide-alpha-1_5

The newest cached card is `HailNicol__qwen3-14b-suicide-alpha-1_5__2026-10-05.md`. It is the default generated model card. The Training Data section says more information is needed. The Hub profile name is Madelin Constante. The account has 19 models and no datasets. There is no GitHub user `HailNicol`. The sibling cards `qwen3-14b-suicide-alpha-0_5` and `qwen3-14b-suicide-alpha-2_0` are the same empty template.

The card’s arXiv tag `1910.09700` is the Lacoste carbon-emissions paper cited inside that template. It is not a paper about this checkpoint. An arXiv query for `qwen3-14b-suicide` returned no paper that prints this repo id. The config is a Qwen3 14B model and does not name a dataset.

No paper, training script, or dataset card names a training corpus for this repository.

https://huggingface.co/HailNicol/qwen3-14b-suicide-alpha-1_5

## Huysun29/cbt-qwen2.5-7b-v2

The newest cached card is `Huysun29__cbt-qwen2.5-7b-v2__2026-10-05.md`. The Hub card was last modified on 2026-06-10, so the October 6 funnel already saw this text. It says: “Dữ liệu: 26.000 mẫu hội thoại CBT (định dạng `messages`, output JSON 6 trường).” That is a count and a format. It does not name a dataset. The same sentence, with a different loss, is on this author’s other v2 cards. The Hub profile name is Nguyen. GitHub user `huysun29` has no repositories.

This author uploaded `Huysun29/cbt-eval` and `Huysun29/eval_data_CBT`. Those repos hold evaluation files (predictions and scores). They have no dataset card, and they do not say they are the training corpus.

The DiaCBT preprint (`https://arxiv.org/abs/2509.02999`) fine-tunes Qwen2.5-7B-Instruct on the DiaCBT corpus with LoRA rank 64, alpha 16, and learning rate 1e-4. This checkpoint’s card says LoRA rank 32, alpha 64, and learning rate 5e-05. The preprint does not mention `Huysun29/cbt-qwen2.5-7b-v2`. An arXiv query for `Huysun29` and for `cbt-qwen2.5-7b` returned no paper about this repository.

No paper, training script, or dataset card names a training corpus for this repository.

https://huggingface.co/Huysun29/cbt-qwen2.5-7b-v2
