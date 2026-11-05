## MihaiPopa-1/LFM2-350M-heretic-safety-defiltered-high-reasoning

No. The cached card and the live card match. Both say this checkpoint is a decensored copy of LiquidAI/LFM2-350M made with patched Heretic v1.1.0. The repository files are the card, a chat template, config, and weights. Heretic's own README says it removes censorship without post-training. Its v1.1.0 default config names `mlabonne/harmless_alpaca` and `mlabonne/harmful_behaviors` as prompt sets for the refusal direction, and both Hub pages load, but the card says the tool was patched and does not say those sets were the training data for this checkpoint. The copied LFM2 section describes the parent model's pre-training as web and licensed material, which is not a corpus a reader can open.

https://huggingface.co/MihaiPopa-1/LFM2-350M-heretic-safety-defiltered-high-reasoning
https://github.com/p-e-w/heretic/blob/v1.1.0/config.default.toml
https://huggingface.co/datasets/mlabonne/harmless_alpaca
https://huggingface.co/datasets/mlabonne/harmful_behaviors

## MihaiPopa-1/LFM2-350M-heretic-safety-defiltered-xhigh-reasoning

No. The cached card and the live card match, apart from the abliteration numbers (KL divergence 0.0205, refusals 10/100). The repository files are the same kinds of files as the high-reasoning checkpoint, with no training script. The same Heretic v1.1.0 page applies: the edit is directional ablation, not training on a named corpus. Searches for this repository id do not turn up a paper or GitHub project about this checkpoint.

https://huggingface.co/MihaiPopa-1/LFM2-350M-heretic-safety-defiltered-xhigh-reasoning
https://github.com/p-e-w/heretic/blob/v1.1.0/README.md
https://github.com/p-e-w/heretic/blob/v1.1.0/config.default.toml

## mingye94/pku-safeRLHF-baseline-safety-base

No. The cached card is only the text `FETCH_ERR MISSING`, and the live README returns 404. The model page itself loads and is public. Its files are weights, tokenizer files, and `config.json`. That config names `meta-llama/Meta-Llama-3-8B` as `_name_or_path` and does not name a dataset. The PKU-SafeRLHF paper and the PKU-Alignment GitHub repository do not mention this repository id. The same author's dataset `mingye94/pku-safeRLHF-softlabel` loads, but its card is a schema only and does not say this checkpoint was trained on it.

https://huggingface.co/mingye94/pku-safeRLHF-baseline-safety-base
https://huggingface.co/mingye94/pku-safeRLHF-baseline-safety-base/raw/main/config.json
https://huggingface.co/datasets/mingye94/pku-safeRLHF-softlabel
https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF

## mingye94/pku-safeRLHF-baseline-safety-base_flipped

No. The cached card is `FETCH_ERR MISSING`, and the live README returns 404. The model is public. Its files are weights, tokenizer files, and `config.json`, which again names `meta-llama/Meta-Llama-3-8B` and no dataset. No paper or GitHub page prints this repository id. A word in the repository name is not a dataset.

https://huggingface.co/mingye94/pku-safeRLHF-baseline-safety-base_flipped
https://huggingface.co/mingye94/pku-safeRLHF-baseline-safety-base_flipped/raw/main/config.json

## mingye94/pku-safeRLHF-baseline-safety-instruct

No. The cached card is `FETCH_ERR MISSING`, and the live README returns 404. The model is public. `config.json` names `meta-llama/Meta-Llama-3-8B-Instruct` and includes a Llama 3 chat template. There is no training script and no dataset field. Searches do not find a paper or repository that says this checkpoint was trained on an openable corpus.

https://huggingface.co/mingye94/pku-safeRLHF-baseline-safety-instruct
https://huggingface.co/mingye94/pku-safeRLHF-baseline-safety-instruct/raw/main/config.json

## mingye94/pku-safeRLHF-softlabel-safety-base

No. The cached card is `FETCH_ERR MISSING`, and the live README returns 404. The model is public. `config.json` names `meta-llama/Meta-Llama-3-8B` and no dataset. The author also published `mingye94/pku-safeRLHF-softlabel` (73,907 train rows, with a `soft_label` column), and that page loads, but the dataset card does not say this checkpoint was trained on it.

https://huggingface.co/mingye94/pku-safeRLHF-softlabel-safety-base
https://huggingface.co/mingye94/pku-safeRLHF-softlabel-safety-base/raw/main/config.json
https://huggingface.co/datasets/mingye94/pku-safeRLHF-softlabel

## mingye94/pku-safeRLHF-softlabel-safety-base_flipped

No. The cached card is `FETCH_ERR MISSING`, and the live README returns 404. The model is public. `config.json` names `meta-llama/Meta-Llama-3-8B` and no dataset. No paper or GitHub page names this repository. The author's soft-label dataset page loads and still does not mention this checkpoint.

https://huggingface.co/mingye94/pku-safeRLHF-softlabel-safety-base_flipped
https://huggingface.co/mingye94/pku-safeRLHF-softlabel-safety-base_flipped/raw/main/config.json
https://huggingface.co/datasets/mingye94/pku-safeRLHF-softlabel

## mingye94/pku-safeRLHF-softlabel-safety-instruct

No. The cached card is `FETCH_ERR MISSING`, and the live README returns 404. The model is public. `config.json` names `meta-llama/Meta-Llama-3-8B-Instruct` and a Llama 3 chat template, and it does not name a dataset. Searches for this repository id find the author's model list, not a training write-up.

https://huggingface.co/mingye94/pku-safeRLHF-softlabel-safety-instruct
https://huggingface.co/mingye94/pku-safeRLHF-softlabel-safety-instruct/raw/main/config.json
https://huggingface.co/mingye94

## mingye94/pku-safeRLHF-softlabel-safety-model

No. The cached card is `FETCH_ERR MISSING`, and the live README returns 404. The model is public and is stored in bfloat16, unlike the float32 siblings. `config.json` sets `_name_or_path` to `/clinical_nlp/uncertainty_quant/dpo_model_5e-6_1epoch_softlabel_safety`. That is a local directory name, not a page a reader can open. The author's paper arXiv:2406.12066 is about drug-name swaps in medical benchmarks and does not mention this checkpoint.

https://huggingface.co/mingye94/pku-safeRLHF-softlabel-safety-model
https://huggingface.co/mingye94/pku-safeRLHF-softlabel-safety-model/raw/main/config.json
https://arxiv.org/abs/2406.12066
https://huggingface.co/datasets/mingye94/pku-safeRLHF-softlabel

## MksShir/Llama-Guard-3-8B-KSTU-Censor

No. The cached card and the live card match, and both are the Meta Llama Guard 3 card. The card says the English data are Llama 2 and Llama 3 generations on prompts from the hh-rlhf dataset, plus additional human and synthetic data that it does not name. `Anthropic/hh-rlhf` loads, and it is preference pairs, not those labeled generations. The repository files are the usual Llama Guard set (license, use policy, tokenizer, weights) and do not add a training file. Nothing in the card or in search results describes a further corpus for the name KSTU-Censor.

https://huggingface.co/MksShir/Llama-Guard-3-8B-KSTU-Censor
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://arxiv.org/abs/2312.06674
