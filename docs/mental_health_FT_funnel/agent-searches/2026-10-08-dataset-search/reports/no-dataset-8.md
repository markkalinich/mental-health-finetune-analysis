# Dataset search, 2026-10-08

Five models whose 2026-10-06 funnel row had no entry in `cardData.datasets` and no dataset tag. A dataset is recorded only when a paper, a training script, a dataset card, or the current model card names a training corpus and is about that repository.

## JordiOrtega/finetuned_mental_health_distilgpt2

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/JordiOrtega__finetuned_mental_health_distilgpt2__2026-10-05.md`. The live README is the same text. It says the checkpoint is a fine-tune of `JordiOrtega/distilgpt2` trained with TRL SFT. It names no corpus. The Hub API still has no `datasets` field and no dataset tag. The saved training arguments record the output folder `finetuned_mental_health_distilgpt2` and do not name a corpus. The account has four models and no datasets. The sibling cards `JordiOrtega/distilgpt2` and `JordiOrtega/distilgpt2_finetuned_mental_health` also name no corpus.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: https://github.com/JordiOrtega (three public repos: a CSS course, an autocomplete demo, and `paper.ly`; none is a training script for this checkpoint); an arXiv query for the repository id (no hits). Other DistilGPT-2 mental-health repos name Empathetic Dialogues. They do not print this repo id. The words in the repo name are not a dataset.

URL of the card that does not name a corpus: https://huggingface.co/JordiOrtega/finetuned_mental_health_distilgpt2

## LangChain12/psychology_chatbot

Recovered: no.

The cached card is a fetch error. The live README URL returns 404. There is no model card and no dataset field. `config.json` names the starting model `NousResearch/Llama-2-7b-chat-hf`. The account display name is master. The account has five models and no datasets. The sibling cards `LangChain12/FineTune_psychologyist_chatbot`, `LangChain12/Final_psychologybot`, and `LangChain12/psychologbot_gguf_version` are license lines only.

The Space `LangChain12/psychology_bot_tesing` loads `LangChain12/psychologbot_gguf_version`. The Space `LaynzID12/LangChain12-FineTune_psychologyist_chatbot` loads `LangChain12/FineTune_psychologyist_chatbot`. Neither Space names a corpus, and neither names this repository. There is no GitHub user `LangChain12`. An arXiv query for the repository id plus the account returned no hits. The sibling `LangChain12/my_awesome_wnut_model` is tagged `dataset:wnut_17`. That tag is on a different checkpoint.

No paper, training script, or dataset card was found that names a training corpus for this repository.

URL of the missing card: https://huggingface.co/LangChain12/psychology_chatbot

## layaiyer/emotionalFT-hyp-arxiv-adjectives-vanilla

Recovered: no.

Both cached cards say the README fetch failed. The live README URL returns 404. There is no model card and no dataset field. The account display name is Laya. The account has no datasets.

`pr_metrics.json` in this repository records `model_path` as `dif_pos_ft_models_classification/emotionalFT/hyp/adjectives/arxiv/vanilla` and `dataset_split_path` as `dataset_splits/Pranav8435_emotionalFT`, next to a test-set size of 1,778. That is an evaluation path, not a sentence that says what the model was trained on. `test_predictions_sample.json` uses the labels Anger, Disgust, Fear, Happiness, and Sadness. `training_history.json` records loss and accuracy and names no corpus. The Hub dataset [Pranav8435/emotionalFT](https://huggingface.co/datasets/Pranav8435/emotionalFT) does not mention this repository.

The paper [Beyond Tokens: Concept-Level Training Objectives for LLMs](https://arxiv.org/html/2601.11791) is by Laya Iyer, Pranav Somani, Alice Guo, Dan Jurafsky, and Chen Shani. Its HTML does not contain this repository id, the string `emotionalFT`, or `huggingface.co/layaiyer`. It names Empathetic Dialogues (`facebook/empathetic_dialogues`) as an evaluation set. The code repository [layaiyer1/concept-aware-training](https://github.com/layaiyer1/concept-aware-training) has a file `data/hyp/arxiv/vanilla_train.txt`. No path in that repository contains `adjectives`, `emotional`, or `layaiyer`, and the README does not name this Hub repository. Wave 1 did not recover a corpus for `layaiyer/emotionalFT-syn-combined-nouns-vanilla`. The same paper does not print this repository id either.

No paper, training script, or dataset card was found that names a training corpus for this repository.

## linsonfas/TW_Counselor-1.1

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/linsonfas__TW_Counselor-1.1__2026-10-05.md`. The live card is the same empty Hub template. The Training Data line is "More Information Needed." The Hub API has no `datasets` field. Earlier README commits on this repository are the same template or a license line. `config.json` records `_name_or_path` as this repository and `unsloth_version`. There is no GitHub user `linsonfas`. An arXiv query for `TW_Counselor` returned no hits.

The sibling `linsonfas/TW_Counselor_lora` names `linsonfas/Further_education_information_in_Taiwan`. That card's `base_model` field is `yentinglin/Llama-3-Taiwan-8B-Instruct`. Its `adapter_config.json` sets `base_model_name_or_path` to `linsonfas/TW_Counselor-1.1`. The dataset page is university question-and-answer JSON (National Formosa University and other Taiwan universities). A file from that dataset does not mention `TW_Counselor`. The sibling `linsonfas/TW_Counselor_lora-1.1` has no dataset tag, and its adapter base is `yentinglin/Llama-3-Taiwan-8B-Instruct`. The education set is named on a different checkpoint.

No paper, training script, or dataset card was found that names a training corpus for this repository.

URL of the card that does not name a corpus: https://huggingface.co/linsonfas/TW_Counselor-1.1

## masta-g3/phi-1_5-psychology

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/masta-g3__phi-1_5-psychology__2026-10-05.md`. The live card matches. It says the model is a fine-tuned version of `microsoft/phi-1_5` on the None dataset, and the training-and-evaluation section says more information is needed. "None" is what the Trainer writes when no dataset name was passed. It is not a corpus name. The saved training arguments record the output folder `phi-1_5-psychology` and do not name a corpus. `adapter_config.json` names the starting model `microsoft/phi-1_5`. The account has two models and no datasets.

No paper, training script, or dataset card was found that names a training corpus for this repository.

Checked: GitHub user `masta-g3` (a gist of paper titles, including the Phi-1.5 technical report; it does not name this checkpoint or a training file); web search for the repository id (the card above, and no training script). The word "psychology" in the repo name is not a dataset.

URL of the card that does not name a corpus: https://huggingface.co/masta-g3/phi-1_5-psychology
