# Dataset names that were missing on 2026-10-06

Checked 2026-10-08. A dataset page is counted as present only if it loads. The JSON address `https://huggingface.co/api/datasets/<name>` returns HTTP 401 with “Invalid username or password” for a missing name. That same address also returns 401 for a made-up name, so 401 from the JSON address is not evidence that the dataset exists.

A name with no slash was tried as a dataset id. It may not be a Hub id.

## Beijuka/speaker-segmentation-sula-hf_luganda_mental_health_dataset-v3

Old name: `Beijuka/luganda_mental_health_dataset_v3`. The dataset page title is “404 – Hugging Face”. The page request returned HTTP 401. The JSON address returns 401. The account’s 23 dataset repos do not include that id.

The cached card from 2026-10-05 says this checkpoint is a fine-tune of `pyannote/speaker-diarization-3.0` on `Beijuka/luganda_mental_health_dataset_v3`. The model repo has a README, config, weights, and `training_args.bin`. It has no training script.

`Beijuka/luganda_mental_health_dataset_v2` loads. It is gated: the page asks you to accept conditions before the files open. The v2 and v4 cards name that dataset for those checkpoints. They do not name this v3 repository. `Beijuka/luganda_callhome_diarization_dataset_MHDP` also loads. This card does not name it. `mhdp-africa/mentalhealth-asr` exists and is gated. Its raw README requires a login, and no source ties it to this repository.

No paper, training script, or dataset card about this repository names a corpus that can be opened.

https://huggingface.co/Beijuka/speaker-segmentation-sula-hf_luganda_mental_health_dataset-v3

## boltuix/bert-emotion

Old name: `chatgpt`. There is no slash, so this may not be a Hub id. Tried as a dataset id, `https://huggingface.co/datasets/chatgpt` redirects to the user page `https://huggingface.co/chatgpt/datasets`. That page is not a dataset repo.

The cached card from 2026-10-05 says the model was trained on a “Custom Emotion Dataset” “sourced from custom datasets and chatgpt-datasets.” It does not give a file, a Hub dataset id, or a paper. The fine-tuning example in the card builds five sentences in the notebook and does not load a corpus.

`boltuix/emotions-dataset` loads, and `emotions_dataset.parquet` opens. This card does not name it. The NeuroFeel training notebook evaluates `boltuix/bert-emotion` on 19 test sentences. It does not say this checkpoint was trained on that dataset. The paper at https://arxiv.org/html/2607.00968v1 samples `boltuix/emotions-dataset` for a zero-shot test of Claude, ChatGPT, and Gemini. It does not name `boltuix/bert-emotion`.

No paper, training script, or dataset card about this repository names a corpus that can be opened.

https://huggingface.co/boltuix/bert-emotion

## boltuix/NeuroFeel

Old name: `chatgpt`. There is no slash, so this may not be a Hub id. Tried as a dataset id, the address redirects to the user page `https://huggingface.co/chatgpt/datasets`. That page is not a dataset repo.

The notebook `how_to_train_model.ipynb` in this repository says NeuroFeel was trained on the Boltuix Emotions Dataset and links https://huggingface.co/datasets/boltuix/emotions-dataset. That page loads. `emotions_dataset.parquet` opens. The dataset card says 131,306 rows. The same notebook’s code reads `/content/dataset.csv`, a Colab path, and the model card’s training section says about 10,000 samples. The sentence that names the open Hub dataset is the “Trained on” line, and it also links `boltuix/NeuroFeel`.

https://huggingface.co/boltuix/NeuroFeel/blob/main/how_to_train_model.ipynb

https://huggingface.co/datasets/boltuix/emotions-dataset

## coding-zzz-oe/empathy-strategy-classifier

Old name: `esconv`. There is no slash, so this may not be a Hub id. Tried as a dataset id, the Hub page title is “404 – Hugging Face”.

The cached card says the training data is the “ESConv (Emotional Support Conversation) dataset” and cites Liu et al., ACL 2021, with no URL. The code example names `RyanDDD/empathy-strategy-classifier`. `RyanDDD/empathy-strategy-classifier` has the same card text and does not print this repository id.

`thu-coai/esconv` loads, and `ESConv.json` on that page opens. `ESConv.json` in https://github.com/thu-coai/Emotional-Support-Conversation also opens. This card does not name either address. The 2021 paper is about that corpus and their dialog system. It does not name this repository. The CounselReflect paper trains a RoBERTa strategy classifier on ESConv and does not print `coding-zzz-oe/empathy-strategy-classifier`.

No paper, training script, or dataset card about this repository names a copy that can be opened.

https://huggingface.co/coding-zzz-oe/empathy-strategy-classifier

## CounselReflect/bert-motivational-interviewing

Old name: `AnnoMI`. There is no slash, so this may not be a Hub id. Tried as a dataset id, the Hub page title is “404 – Hugging Face”.

This repository’s model card says: “The model was trained on the AnnoMI dataset (Annotated Motivational Interviewing), which contains expert-annotated counseling dialogues.” The references line points at https://github.com/uccollab/AnnoMI. That repository’s `AnnoMI-simple.csv` opens. The file begins with the column `transcript_id`. The card’s code example, citation, and `example_usage.py` name `RyanDDD/bert-motivational-interviewing`. The AnnoMI link is in this repository’s README.

The CounselReflect paper at https://arxiv.org/html/2603.29429v1 says the authors train a RoBERTa-base talk-type classifier on AnnoMI. It does not print `CounselReflect/bert-motivational-interviewing`. A code search of https://github.com/counselreflectteam/CounselReflect for `AnnoMI` returned no hits. Those sources were not counted. The recovery is the link in this repository’s README.

https://github.com/uccollab/AnnoMI/blob/main/AnnoMI-simple.csv
