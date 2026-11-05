# Dataset names that were missing on 2026-10-06

Checked 2026-10-08. A dataset page is counted as present only if it loads. None of the five names load. The dataset page for each one is the Hub 404 page. The JSON address `https://huggingface.co/api/datasets/<name>` returns HTTP 401 with “Invalid username or password” for these names. That same JSON address also returns 401 for a made-up name, so 401 is not evidence that the dataset exists. None of them return 200.

A name with no slash was tried as a dataset id. It may not be a Hub id.

## christinacdl/moderate_severe_depression_model

Old name: `christinacdl/balanced_depression_dataset`. The Hub dataset page is a 404 today.

The cached card from 2026-10-05 lists that name in the YAML header. The card text says the model is a fine-tune of `allenai/longformer-scico` “on an unknown dataset.”

Christina Christodoulou’s 2023 shared-task paper trains RoBERTa and DeBERTa. It does not name this model. Her notebook lists a different Hub id, `christinacdl/moderate_severe_depression_longformerlarge_model`, and does not contain `moderate_severe_depression_model`. No paper, training script, or dataset card about this repository names a corpus that can be opened.

https://huggingface.co/christinacdl/moderate_severe_depression_model

## coding-zzz-oe/bert-motivational-interviewing

Old name: `AnnoMI`. There is no slash, so this may not be a Hub id. Tried as a dataset id, the Hub page is a 404 today.

This repository’s model card says: “The model was trained on the AnnoMI dataset (Annotated Motivational Interviewing), which contains expert-annotated counseling dialogues.” The references line points at the GitHub copy, https://github.com/uccollab/AnnoMI. That repository’s `AnnoMI-simple.csv` opens. The file begins with the columns `transcript_id` and `client_talk_type`. The card’s code example and citation name `RyanDDD/bert-motivational-interviewing`. The AnnoMI link is in this repository’s README.

https://github.com/uccollab/AnnoMI/blob/main/AnnoMI-simple.csv

## CPF3-org/cpf-poc-model

Old names: `cpf-synthetic-phishing` and `cybersecurity-psychology`. Neither has a slash, so either may not be a Hub id. Tried as dataset ids, both Hub pages are 404 today.

The model card says training used “synthetic CPF indicator data” and links https://github.com/xbeat/CPF. The guide in that repository’s `AI` folder names `CPF3-org/cpf-poc-model` and links a Colab notebook as the synthetic dataset. The notebook builds examples from three sentence templates and writes them to `/content/drive/MyDrive/synthetic_data.json`. That file is on a private Google Drive. It does not open. The paper at https://arxiv.org/abs/2510.09635 links `cpf-framework/synthetic-v1` and does not print this model id. That Hub page is also a 404. No public corpus named for this repository opens.

https://github.com/xbeat/CPF/blob/main/AI/README.md

## ehzawad/orpheus-bangla-emotional-tts

Old name: `bangla-audio-emotional`. There is no slash, so this may not be a Hub id. Tried as a dataset id, the Hub page is a 404 today.

The cached card lists that name and does not describe a file or a paper. The first upload of the README has the comment “Update with your actual dataset name” on that line. No paper, training script, or dataset card about this repository names a corpus that can be opened.

https://huggingface.co/ehzawad/orpheus-bangla-emotional-tts

## Gojosen/mental-health-distilbert

Old name: `entenam/reddit-mental-health-dataset`. The Hub dataset page is a 404 today.

This repository’s model card says the model was fine-tuned on the Reddit Mental Health Dataset sourced from Kaggle, and it gives https://www.kaggle.com/datasets/entenam/reddit-mental-health-dataset. That Kaggle page opens. The page title is “Reddit Mental Health Dataset (RMHD).” The GitHub repository linked from the card, https://github.com/gitarju/Mental-Health-Text-Risk-Detector-Using-DistilBERT, repeats the same Kaggle address. The card’s usage example prints `Gojosen/mental-health-distilbert`.

https://www.kaggle.com/datasets/entenam/reddit-mental-health-dataset
