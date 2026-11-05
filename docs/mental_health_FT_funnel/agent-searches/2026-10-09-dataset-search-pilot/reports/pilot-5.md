# Dataset search, pilot batch 5

9 October 2026. Five repositories. None name a training corpus a reader can open.

## sahil7171/distilbert-mental-health

No. No source names a corpus a reader can open.

The cached card from 5 October 2026 and the live card are the same generated template. The training-data line is "More Information Needed". The repository holds weights, a tokenizer, and a config. The config labels are Anxiety, Bipolar, Depression, Normal, Personality Disorder, Stress, and Suicidal. The linked Space says the dataset is "~52K Reddit posts" and does not give a Hub id, a Kaggle URL, or a paper. Those seven labels are the seven statuses on the Kaggle set Sentiment Analysis for Mental Health, which shows about 53,000 rows. The Space does not name that set.

https://huggingface.co/sahil7171/distilbert-mental-health
https://huggingface.co/spaces/sahil7171/mental-health-classifier
https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health

## Shuddup/depression_classifier_weighted

No. The card says this DistilBERT was fine-tuned on an unknown dataset.

The live card matches the cached card from 5 October 2026. The config labels are NOT DEPRESSION, MODERATE, and SEVERE. The repository has no training script. Those three labels are the three classes used in the LT-EDI depression shared task. No page about this repository names that task or any other corpus.

https://huggingface.co/Shuddup/depression_classifier_weighted

## sweagent/selfharmo-mstep2-rl-iter49

No. The card is the Qwen3.5-35B-A3B card and does not name the data for this run.

The live README matches the cached card. The only commit title is "self-harmo M-Step-2 RL iter_49 (prgrepalign / PR-Grep Alignment harness)". The other files are weights and tokenizer files. Datasets under the same organization describe other runs, combo2 and iter-2, and do not print this repository id. Searches did not find a paper or GitHub page that names a corpus for this checkpoint.

https://huggingface.co/sweagent/selfharmo-mstep2-rl-iter49
https://huggingface.co/sweagent/selfharmo-mstep2-rl-iter49/commit/ca9f247721c27d7d5a4f5ad6a996e94241a105d5

## TTDattt/PhoBERT-DepressionClassification-o2

No. This repository has no model card.

The cached fetch is missing, and the live README returns 404. The files are weights, a PhoBERT tokenizer, and a config. The five labels are LABEL_0 through LABEL_4. The author Tran Thanh Dat has no datasets on the Hub. Searches did not find a paper or GitHub page about this checkpoint.

https://huggingface.co/TTDattt/PhoBERT-DepressionClassification-o2

## wonderlic-engineering/sift-bart-large-mnli-empathy

No. The card does not name a training corpus.

The cached card from 5 October 2026 matches the live card. It is a generated SetFit card. The training-dataset line is commented out as Unknown. `config_setfit.json` sets labels to null. The paper link is the SetFit method paper, arXiv 2209.11055, which does not describe this checkpoint. The inference example loads a different repository, gmenchetti/bart-large-mnli-empathy-tuned-50runs. That card also does not name a dataset.

https://huggingface.co/wonderlic-engineering/sift-bart-large-mnli-empathy
https://arxiv.org/abs/2209.11055
https://huggingface.co/gmenchetti/bart-large-mnli-empathy-tuned-50runs
