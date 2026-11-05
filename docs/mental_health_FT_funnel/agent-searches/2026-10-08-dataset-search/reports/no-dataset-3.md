# Dataset search, five models with no dataset on the October 6 card

One training corpus was recovered. Four were not.

## Jayasimha01/spotify-genre-mood

The newest cached card (2026-10-05) is the automatic Hugging Face template. The live card is the same template. `cardData` has no dataset name.

The training repository is [jayapasam9-max/Spotify-genre-mood-ML](https://github.com/jayapasam9-max/Spotify-genre-mood-ML). Its README links the live demo [Jayasimha01/spotify-genre-mood-demo](https://huggingface.co/spaces/Jayasimha01/spotify-genre-mood-demo). That demo loads `Jayasimha01/spotify-genre-mood`. The demo text says it is part of the Spotify Genre & Mood ML project. The checkpoint is DistilBERT with labels country, hip-hop, metal, pop, in that order. The training code sorts labels alphabetically, which produces the same order.

`src/build_dataset.py` names the corpus. The sentence is: "Streams the public HF dataset `Yegor25/lyrics_genre_dataset_large` (no token needed), maps its granular multi-genre tags to a few broad buckets, balances the classes, cleans the lyrics, and writes data/full/lyrics.csv."

`config.yaml` points training at the CSV that script writes. The Hub dataset exists: https://huggingface.co/datasets/Yegor25/lyrics_genre_dataset_large

An arXiv search for the repository id returned no papers. The bundled `sample_lyrics.csv` is a small stand-in, not the corpus named by the script.

## KartikPahadiya/mental-health-model

Both cached cards say the README fetch failed. The live README URL returns 404. The model API record has no `cardData.datasets` field.

The GitHub project [KartikPahadiya/ai-mental-health-assistant-project](https://github.com/KartikPahadiya/ai-mental-health-assistant-project) has a `model/` folder whose `config.json` is the same file as this checkpoint's `config.json`. The app loads that folder for text emotion classification and lists 28 emotion names. Those names are the GoEmotions label set. The script does not say the training file was GoEmotions, or any other corpus.

The same README names RAVDESS, TESS, and SAVEE for the audio models. Those are other Hub repositories (`KartikPahadiya/mental-health-ravdess_model`, `KartikPahadiya/mental-health-tess_model`, `KartikPahadiya/mental-health-savee_model`). They are not this checkpoint. The Kaggle page for the notebook RMHD-kartik does not name this repository.

No paper, training script, or dataset card was found that names a training corpus for this repository.

## layai/emotionalFT-hyp-all-youtube-dict

Both cached cards say the README fetch failed. The live README URL returns 404. There is no model card and no dataset field.

`pr_metrics.json` in this repository records `dataset_split_path` as `dataset_splits/Pranav8435_emotionalFT`, next to a test-set size of 1,778. That is an evaluation path, not a sentence that says what the model was trained on. The Hub dataset [Pranav8435/emotionalFT](https://huggingface.co/datasets/Pranav8435/emotionalFT) has train, validation, and test CSV files and no dataset card. It does not mention this repository. A saved sample of predictions uses the labels Happiness, Sadness, Anger, Fear, and Disgust.

The paper [Beyond Tokens: Concept-Level Training Objectives for LLMs](https://arxiv.org/abs/2601.11791) is by Laya Iyer, Pranav Somani, Alice Guo, Dan Jurafsky, and Chen Shani. It describes post-training on YouTube comments, arXiv abstracts, and New York Times abstracts, then fine-tuning on Empathetic Dialogues (`facebook/empathetic_dialogues`). It does not print this repository id. Its Empathetic Dialogues examples use labels such as Sentimental and Proud, not the five labels stored with this checkpoint. The code repository [layaiyer1/concept-aware-training](https://github.com/layaiyer1/concept-aware-training) likewise does not name this Hub repository.

No paper, training script, or dataset card was found that names a training corpus for this repository.

## layaiyer/emotionalFT-syn-combined-nouns-vanilla

Both cached cards say the README fetch failed. The live README URL returns 404. There is no model card and no dataset field.

`pr_metrics.json` in this repository records the same evaluation path, `dataset_splits/Pranav8435_emotionalFT`, and the same five-label setup. The local path in that file is `dif_pos_ft_models_classification/emotionalFT/syn/nouns/combined/vanilla`. As with the previous model, that file does not state a training corpus, and [Pranav8435/emotionalFT](https://huggingface.co/datasets/Pranav8435/emotionalFT) does not mention this repository.

The same paper, arXiv:2601.11791, does not print this repository id. Its emotion fine-tuning set is Empathetic Dialogues, whose labels are not the five labels stored here. The concept-aware training repository does not name this Hub repository.

No paper, training script, or dataset card was found that names a training corpus for this repository.

## magpie2211/social-anxiety-model-llama

The newest cached card (2026-10-05) matches the live card. It says the model was developed by magpie2211 and fine-tuned from `unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit` with Unsloth and TRL. It names no dataset. The live `cardData` has no dataset field.

The sibling repository `magpie2211/social-anxiety-llama-adapters` has the same template card. Its `adapter_config.json` records the LoRA settings and the same base model, and no dataset. The GitHub user magpie2211 has no public repositories. An arXiv search for the repository id returned no papers. The Hugging Face profile display name is Magdalena Meier. A search for that name plus a social-anxiety Llama model did not find a paper or script about this repository. The Magpie alignment paper and the Magpie-Align datasets are a different project. They do not name this repository.

No paper, training script, or dataset card was found that names a training corpus for this repository.
