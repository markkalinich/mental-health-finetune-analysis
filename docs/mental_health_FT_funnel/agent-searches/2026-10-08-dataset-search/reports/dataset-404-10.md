# Dataset names that were missing on 2026-10-06

Checked on 2026-10-08. The newest cached card for each model is the 2026-10-05 copy. A dataset page is counted as present only if it loads. The JSON address `https://huggingface.co/api/datasets/<name>` returns HTTP 401 for a missing name and for a private name, so the dataset page is the check.

## mario-rc/emotional-gpt2-large

The card named DailyDialog. That string has no slash, so it may not be a Hub id. The dataset page returns 404: https://huggingface.co/datasets/DailyDialog

The card links https://github.com/Mario-RC/emotional-gpt and says the training files are `data/gpt-dialogues/train.txt` and `data/gpt-dialogues/dev.txt`, built from DailyDialog CSV resources. The README of that repository lists `mario-rc/emotional-gpt2-large` and says the required source files are `DAILYD_main.csv` and `DAILYD_dialoginfo.csv`. `data/source/DAILYD_main.csv` opens. The first line is `dialog_id,speaker,text`.

https://github.com/Mario-RC/emotional-gpt/blob/main/data/source/DAILYD_main.csv

## mario-rc/emotional-gpt2-medium

The card named DailyDialog. The dataset page returns 404: https://huggingface.co/datasets/DailyDialog

The same README lists `mario-rc/emotional-gpt2-medium` and the same two source files. `data/source/DAILYD_main.csv` opens. This is the same file as for `mario-rc/emotional-gpt2-large`. The README names this repository on its own line.

https://github.com/Mario-RC/emotional-gpt/blob/main/data/source/DAILYD_main.csv

## onelastkissforme/Llama-KoEmpathy

The card named `byeolki/Llama-KoEmpathy-Dataset`. The dataset page returns 401, not 200 and not 404: https://huggingface.co/datasets/byeolki/Llama-KoEmpathy-Dataset

That may be a private repo. No file in it opens. The card also links https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71305. That page returns 200 and is the 공감형 대화 dataset. The sample control is a login link. The file-download address returns a script, not a file. `https://huggingface.co/byeolki/Llama-KoEmpathy` resolves to this repository, and the card's code example still prints `byeolki/Llama-KoEmpathy`. No paper, training script, or dataset card about this repository names a file that opens.

https://huggingface.co/onelastkissforme/Llama-KoEmpathy

## RyanDDD/bert-motivational-interviewing

The card named AnnoMI. There is no slash, so this may not be a Hub id. Tried as a dataset id, the Hub page is a 404 today: https://huggingface.co/datasets/AnnoMI

This repository's model card says the model was trained on the AnnoMI dataset and the references line points at https://github.com/uccollab/AnnoMI. The code example prints `RyanDDD/bert-motivational-interviewing`. `AnnoMI-simple.csv` opens. The first line begins `transcript_id` and includes `client_talk_type`.

https://github.com/uccollab/AnnoMI/blob/main/AnnoMI-simple.csv

## RyanDDD/empathy-strategy-classifier

The card named esconv. There is no slash, so this may not be a Hub id. Tried as a dataset id, the Hub page is a 404 today: https://huggingface.co/datasets/esconv

The card says the training data is the ESConv dataset and cites Liu, Zheng, Demasi, Sabour, Li, Yu, Jiang, and Huang, ACL 2021. The citation has no file address. That paper says the data is at https://github.com/thu-coai/Emotional-Support-Conversation, and `ESConv.json` in that repository opens. The paper and that README do not print `RyanDDD/empathy-strategy-classifier`. `thu-coai/esconv` returns 200. This card does not name that Hub id. The copy at `coding-zzz-oe/empathy-strategy-classifier` prints this repo id in its code example and also only says ESConv. No file named for this repository opens.

https://huggingface.co/RyanDDD/empathy-strategy-classifier
