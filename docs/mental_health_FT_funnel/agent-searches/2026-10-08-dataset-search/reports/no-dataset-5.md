# Five models with no dataset named on the card

Checked 2026-10-08. A training corpus counts only when a paper, a training script, a dataset card, or the current model card names that corpus and is about this repository. None of the five cleared that bar.

## sagarnildass/suicide_detector_roberta_base

The cached card from 2026-10-05, and the current card, contain only an MIT license. `model_args.json` and `training_args.bin` name the base model `roberta-base` and local output folders. They do not name a corpus.

No paper or GitHub repository prints this repo id. Sagarnil Das's app at https://github.com/sagarnildass/mind-matters loads `gooohjy/suicidal-electra` for suicide classification. That file does not describe this checkpoint and does not name its training data.

No training corpus was found.

https://huggingface.co/sagarnildass/suicide_detector_roberta_base/raw/main/README.md

## Shuddup/depression_classifier_unweighted_1

The current card says this model is a fine-tuned version of distilbert-base-uncased on an unknown dataset. The training-data section says more information is needed. `training_args.bin` stores hyperparameters and the output folder name. It does not store a dataset name.

The same account's other depression-classifier cards also say the dataset is unknown. Those cards are about the other checkpoints. GitHub user `shuddup` has no public repositories. Exact searches on arXiv, OpenAlex, and the web found no paper that prints this repo id.

No training corpus was found.

https://huggingface.co/Shuddup/depression_classifier_unweighted_1/raw/main/README.md

## sweagent/selfharmo-mstep2-rl-iter44

The current card is the Qwen3.5-35B-A3B model card. It describes Qwen3.5, not this checkpoint. The upload commit by Zhepei Wei (`weizhepei`) is titled "self-harmo M-Step-2 RL iter_44 (prgrepalign harness)". That title names a harness. It does not name a corpus.

`sweagent/iter2-rl-rollouts` names the task file `combined_0630_clean.jsonl` for a different run (the combo_fb iter-2 GRPO run). That dataset card does not print `sweagent/selfharmo-mstep2-rl-iter44`. The self-synthetic alignment paper by Zhepei Wei (https://arxiv.org/abs/2510.06652) does not mention this repository. Exact searches for `selfharmo-mstep2-rl-iter44` and `prgrepalign` found no paper or script.

No training corpus was found.

https://huggingface.co/sweagent/selfharmo-mstep2-rl-iter44/raw/main/README.md

## TTDattt/PhoBERT-DepressionClassification-o1

This repository has no README. The current card data is empty. `config.json` lists five labels as `LABEL_0` through `LABEL_4` and names `PhobertTokenizer`. It does not name a corpus.

`Long1101/PhoBERT-DepressionClassification-o1-api` says the base model is `vinai/phobert-base` and points back at this repo. It does not name a fine-tuning corpus. The PhoBERT paper describes Wikipedia and news text used to pre-train PhoBERT. That paper is about `vinai/phobert-base`, not this checkpoint. Exact searches found no paper or GitHub repository that prints this repo id.

No training corpus was found.

https://huggingface.co/TTDattt/PhoBERT-DepressionClassification-o1

## wizardpatel/mental-health-bert

The current card is the empty Hugging Face template. Training data is marked "More Information Needed". The tag `arxiv:1910.09700` is the carbon-emissions paper cited by that template (Lacoste et al., 2019). That paper does not describe this checkpoint.

A web index listed https://github.com/Damacol/wizardpatel-mental-health-bert. That page returns 404, and the index snippet does not name a training corpus. Exact searches on arXiv, OpenAlex, GitHub, and Hugging Face datasets found no source that prints this repo id and names a corpus.

No training corpus was found.

https://huggingface.co/wizardpatel/mental-health-bert/raw/main/README.md
