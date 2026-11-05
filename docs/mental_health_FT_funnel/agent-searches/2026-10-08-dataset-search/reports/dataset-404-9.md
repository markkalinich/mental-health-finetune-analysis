# Dataset names that were missing on 2026-10-06

Checked on 2026-10-08. The datasets API returns 401 for a missing id and for a private id, so the dataset page is the check. The DailyDialog page is the Hub 404 page. The Common Voice 7.0 page shows the Hub 404 text and returns HTTP 401. No file in that dataset repo opens.

## Maniac/wav2vec2-xls-r-urdu

The card and `run.sh` in this repository name `mozilla-foundation/common_voice_7_0`, config `ur`. The dataset page title is "404 – Hugging Face". The page says "Sorry, we can't find the page you are looking for." The HTTP status is 401. `resolve/main/README.md` and `resolve/main/ur/train.tsv` also return 401.

The model-index names `mozilla-foundation/common_voice_8_0` as the evaluation set. That page is the same 404 text, and the HTTP status is 401.

`mozilla-foundation/common_voice_13_0` and `mozilla-foundation/common_voice_17_0` return 200. This card and `run.sh` do not name them. A Hub search for `common_voice_7_0` returns `Plim/common_voice_7_0_fr_processed`. That is a French set, and this card does not name it.

No paper about Maniac/wav2vec2-xls-r-urdu points at a copy that opens.

https://huggingface.co/Maniac/wav2vec2-xls-r-urdu

## mario-rc/emotional-dialogpt-medium

The card named DailyDialog. The dataset page is the Hub 404 page: https://huggingface.co/datasets/DailyDialog

This card prints `repo_id = "mario-rc/emotional-dialogpt-medium"`. It says the training files are `data/gpt-dialogues/train.txt` and `data/gpt-dialogues/dev.txt`, built from DailyDialog CSV resources, and it links https://github.com/Mario-RC/emotional-gpt. The README of that repository lists `mario-rc/emotional-gpt2-medium` and `mario-rc/emotional-gpt2-large`. It does not print this repo id. The source CSV files in that repository open: https://github.com/Mario-RC/emotional-gpt/blob/main/data/source/DAILYD_main.csv (6,447,960 bytes) and https://github.com/Mario-RC/emotional-gpt/blob/main/data/source/DAILYD_dialoginfo.csv. The README says those files come from https://github.com/CHANEL-JSALT-2020/datasets, and https://github.com/CHANEL-JSALT-2020/datasets/blob/main/azure/DAILYD/DAILYD.rar opens. `data/gpt-dialogues/train.txt` is not in the repository.

## mario-rc/emotional-dialogpt-small

The card named DailyDialog. The dataset page is the Hub 404 page: https://huggingface.co/datasets/DailyDialog

This card prints `repo_id = "mario-rc/emotional-dialogpt-small"`. It says the training files are `data/gpt-dialogues/train.txt` and `data/gpt-dialogues/dev.txt`, built from DailyDialog CSV resources, and it links https://github.com/Mario-RC/emotional-gpt. The README of that repository does not print this repo id. The same source files open: https://github.com/Mario-RC/emotional-gpt/blob/main/data/source/DAILYD_main.csv and https://github.com/CHANEL-JSALT-2020/datasets/blob/main/azure/DAILYD/DAILYD.rar.

## mario-rc/emotional-distilgpt2

The card named DailyDialog. The dataset page is the Hub 404 page: https://huggingface.co/datasets/DailyDialog

This card prints `repo_id = "mario-rc/emotional-distilgpt2"`. It says the training files are `data/gpt-dialogues/train.txt` and `data/gpt-dialogues/dev.txt`, built from DailyDialog CSV resources, and it links https://github.com/Mario-RC/emotional-gpt. The README of that repository does not print this repo id. The same source files open: https://github.com/Mario-RC/emotional-gpt/blob/main/data/source/DAILYD_main.csv and https://github.com/CHANEL-JSALT-2020/datasets/blob/main/azure/DAILYD/DAILYD.rar.

## mario-rc/emotional-gpt2

The card named DailyDialog. The dataset page is the Hub 404 page: https://huggingface.co/datasets/DailyDialog

This card prints `repo_id = "mario-rc/emotional-gpt2"`. It says the training files are `data/gpt-dialogues/train.txt` and `data/gpt-dialogues/dev.txt`, built from DailyDialog CSV resources, and it links https://github.com/Mario-RC/emotional-gpt. The README of that repository lists `mario-rc/emotional-gpt2-medium` and `mario-rc/emotional-gpt2-large`. It does not print `mario-rc/emotional-gpt2`. The same source files open: https://github.com/Mario-RC/emotional-gpt/blob/main/data/source/DAILYD_main.csv and https://github.com/CHANEL-JSALT-2020/datasets/blob/main/azure/DAILYD/DAILYD.rar.
