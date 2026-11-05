# Dataset names that were missing on 2026-10-06

Checked on 2026-10-08. The datasets API returns 401 for a missing id and for a private id, so the dataset page is the check that separates 404 from a private repo. None of these five names returns 200.

## mario-rc/emotional-dialogpt-large

The card named DailyDialog. That string has no slash, so it may not be a Hub id. The datasets API returns 401. The dataset page returns 404: https://huggingface.co/datasets/DailyDialog

The model card links https://github.com/Mario-RC/emotional-gpt and says the training files are `data/gpt-dialogues/train.txt` and `data/gpt-dialogues/dev.txt`, built from DailyDialog CSV resources. The README of that repository says: "DAILYD resources source: CHANEL-JSALT-2020/datasets." Those files open: https://github.com/CHANEL-JSALT-2020/datasets/blob/main/azure/DAILYD/DAILYD.rar and https://github.com/Mario-RC/emotional-gpt/blob/main/data/source/DAILYD_main.csv

## neodeskagent71/Vip-bangla-emotional-tts

The card named bangla-audio-emotional. That string has no slash, so it may not be a Hub id. The datasets API returns 401. The dataset page returns 404: https://huggingface.co/datasets/bangla-audio-emotional

None was found. The card copies the README of ehzawad/orpheus-bangla-emotional-tts, and that README's dataset line was a placeholder ("Update with your actual dataset name"). No paper, training script, or dataset card about neodeskagent71/Vip-bangla-emotional-tts names a corpus that can be opened. https://huggingface.co/neodeskagent71/Vip-bangla-emotional-tts

## rabiaqayyum/autotrain-mental-health-analysis-752423172

The card named rabiaqayyum/autotrain-data-mental-health-analysis. The datasets API returns 401. The dataset page returns 401, not 200 and not 404: https://huggingface.co/datasets/rabiaqayyum/autotrain-data-mental-health-analysis

None was found. The author's public dataset list is empty, and the "Dataset used" discussion has no reply. No paper, training script, or dataset card about this repository names a corpus that can be opened. https://huggingface.co/rabiaqayyum/autotrain-mental-health-analysis-752423172

## rhaymison/Mistral-portuguese-luana-7b-mental-health

The card named rhaymison/mental-health-qa. The datasets API returns 401. The dataset page returns 401, not 200 and not 404: https://huggingface.co/datasets/rhaymison/mental-health-qa

None was found. The same author has a public dataset, rhaymison/mental-health-pt, which returns 200, but no source about this checkpoint says that is the training corpus. https://huggingface.co/rhaymison/Mistral-portuguese-luana-7b-mental-health

## sarthak0226/flan-t5-large-mentalchat

The card named mentalchat-16k. That string has no slash, so it may not be a Hub id. The datasets API returns 401. The dataset page returns 404: https://huggingface.co/datasets/mentalchat-16k

None was found. ShenLab/MentalChat16K returns 200, and the MentalChat16K paper points at that Hub id, but the paper and the ShenLab dataset card do not name sarthak0226/flan-t5-large-mentalchat. The model card does not say which copy was used. https://huggingface.co/sarthak0226/flan-t5-large-mentalchat
