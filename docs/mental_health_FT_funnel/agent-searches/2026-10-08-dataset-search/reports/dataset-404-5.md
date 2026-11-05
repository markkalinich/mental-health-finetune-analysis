# Dataset names that were missing on 2026-10-06

Checked on 2026-10-08. Each old name was looked up as `https://huggingface.co/api/datasets/<name>`. A name with no slash was also treated as a possible non-id. Newest cached card: 2026-10-05 for all five.

## sihyeonmoon/moodtown-emotion-model

Old name: `ai-hub`. The Hub returns 404. The name has no slash, so it may not be a dataset id.

The model card says this checkpoint was trained on the AI Hub emotional-dialogue corpus, AI Hub 감성 대화 말뭉치, and gives https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=86. That page returns 200 and is the 감성 대화 dataset. The moodtown README links this model and the same page: https://github.com/bearivh/moodtown.

Sentence: moodtown 프로젝트의 일부로 개발되었으며, AI Hub 감성 대화 말뭉치를 사용하여 학습되었습니다.

## SrothJr/banglamentalBERT-banglaBERT-dapt

Old name: `depression-social-media`. The Hub returns 404. The name has no slash, so it may not be a dataset id.

The card says the model was domain-adapted on Bangla mental-health text and does not give a dataset id or a link. The same account hosts `SrothJr/banglamentalBERT-corpuses`, which returns 200, but that dataset card does not name this checkpoint. Cards for other checkpoints by the same account name a Kabir corpus and a 250,154-line file; those cards are about different models. None was found for this repository.

## techhy/mindtrack-mental-health-analyzer

Old name: `custom-mental-health-dataset`. The Hub returns 404. The name has no slash, so it may not be a dataset id.

The model card links https://github.com/Soham-droid-pixel/Mind_Track_Project. That repository’s upload script publishes `techhy/mindtrack-mental-health-analyzer`. Its training script loads `data/cleaned_mental_health_data.csv`. The file opens: the first row is a `text` and `class` table, and the file is about 167 MB.

Sentence: The training script loads `data/cleaned_mental_health_data.csv`.

URL: https://github.com/Soham-droid-pixel/Mind_Track_Project/blob/main/model/train.py

## TheCarBun/GPT-2-fine-tuned-mental-health

Old names: `custom-dataset` and `kaggle`. Both return 404. Neither has a slash, so either may not be a dataset id.

The card says the data is `intents.json` plus a Kaggle conversational dataset, and it does not name which Kaggle dataset. The training notebook in https://github.com/TheCarBun/GPT2-mental-health reads `intents.json` and builds the training table from it. The README of that repository loads `TheCarBun/GPT-2-fine-tuned-mental-health` and calls `intents.json` the dataset used for training. That file opens. No file in the repository names a Kaggle page.

Sentence: Cleaned conversational data from `intents.json`.

URL: https://github.com/TheCarBun/GPT2-mental-health/blob/main/Mental_Health_AI_GPT_2.ipynb

## vincenzoooooo/saskia-sonja-frida-2-agreeableness

Old name: `pandora`. The Hub returns 404. The name has no slash, so it may not be a dataset id.

The card says the training data is the PANDORA dataset of Reddit comments. It does not give a link or say which copy. No paper, training script, or dataset card about this repository names a copy you can open. The account has no public GitHub repositories under that name. None was found.
