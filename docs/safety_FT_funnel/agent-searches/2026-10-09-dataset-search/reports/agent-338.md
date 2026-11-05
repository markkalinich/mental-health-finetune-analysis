## vinchu/Llama3.1-8b-Instruct-Guarded

No. The cached card and the live card are the same Unsloth upload template. They name the base model `unsloth/Llama-3.1-8B-Instruct` and do not name a training corpus. The repository files are the tokenizer, config, and weights. Searches found no paper or GitHub that names this repository's training data.

https://huggingface.co/vinchu/Llama3.1-8b-Instruct-Guarded
https://huggingface.co/vinchu/Llama3.1-8b-Instruct-Guarded/raw/main/README.md

## vinchu/Llama3.1-8b-Instruct-Guarded-fullsft

No. This card is the same Unsloth template as the sibling repository. It names only `unsloth/Llama-3.1-8B-Instruct`. The file list has no training script. A GitHub search for the repository name did not find a training corpus.

https://huggingface.co/vinchu/Llama3.1-8b-Instruct-Guarded-fullsft
https://huggingface.co/vinchu/Llama3.1-8b-Instruct-Guarded-fullsft/raw/main/README.md

## vmal/med-advisor-4b

No. There is no cached card. The live card says phase 1 used a curated medical instruction set and does not give that set a name a reader can open. The repository has no training script. Searches found no paper or GitHub for this checkpoint.

https://huggingface.co/vmal/med-advisor-4b
https://huggingface.co/vmal/med-advisor-4b/raw/main/README.md

## Wanfq/KCA_Llama_2_13B_Refusal_Tuning

Yes. The repository has no model card. `trainer_state.json` is a loss log and does not name the data. The EMNLP 2024 paper by Fanqi Wan (Wanfq), arXiv 2401.10768, says the training dataset is WizardLM-Evol-Instruct-70k, and the GitHub training script maps refusal tuning of `llama-2-13b` to `llama-2-13b_shot-5_wizardlm_trainset_sorry.json` in `Wanfq/KCA_data`. That file and the WizardLM dataset page both open.

https://arxiv.org/html/2401.10768
https://github.com/fanqiwan/KCA
https://huggingface.co/datasets/Wanfq/KCA_data/blob/main/data/processed_results/llama-2-13b_shot-5_wizardlm_trainset_sorry.json
https://huggingface.co/datasets/Wanfq/KCA_data
https://huggingface.co/datasets/WizardLMTeam/WizardLM_evol_instruct_70k

## Wanfq/KCA_Llama_2_7B_Refusal_Tuning

Yes. There is no model card. The same paper and the same GitHub script name refusal tuning of `llama-2-7b` on the processed WizardLM file `llama-2-7b_shot-5_wizardlm_trainset_sorry.json`. That file opens in `Wanfq/KCA_data`. The underlying corpus the paper names, WizardLM-Evol-Instruct-70k, also opens.

https://arxiv.org/html/2401.10768
https://github.com/fanqiwan/KCA
https://huggingface.co/datasets/Wanfq/KCA_data/blob/main/data/processed_results/llama-2-7b_shot-5_wizardlm_trainset_sorry.json
https://huggingface.co/datasets/Wanfq/KCA_data
https://huggingface.co/datasets/WizardLMTeam/WizardLM_evol_instruct_70k

## Wanfq/KCA_Mistral_7B_V0.1_Refusal_Tuning

Yes. There is no model card. The paper trains Mistral 7B with refusal tuning on WizardLM-Evol-Instruct-70k. The GitHub script names the file `mistral-7b-v0.1_shot-5_wizardlm_trainset_sorry.json`, and that file opens in `Wanfq/KCA_data`.

https://arxiv.org/html/2401.10768
https://github.com/fanqiwan/KCA
https://huggingface.co/datasets/Wanfq/KCA_data/blob/main/data/processed_results/mistral-7b-v0.1_shot-5_wizardlm_trainset_sorry.json
https://huggingface.co/datasets/Wanfq/KCA_data
https://huggingface.co/datasets/WizardLMTeam/WizardLM_evol_instruct_70k

## Wanfq/KCA_Pythia_6.9B_Refusal_Tuning

Yes. The cached card is missing and the live README is a 404. The paper's Pythia 7B refusal-tuning run is this checkpoint: the GitHub script's model name is `pythia-6.9b`, and `pythia-6.9b_shot-5_wizardlm_trainset_sorry.json` opens in `Wanfq/KCA_data`. The paper names the source corpus as WizardLM-Evol-Instruct-70k.

https://arxiv.org/html/2401.10768
https://github.com/fanqiwan/KCA
https://huggingface.co/datasets/Wanfq/KCA_data/blob/main/data/processed_results/pythia-6.9b_shot-5_wizardlm_trainset_sorry.json
https://huggingface.co/datasets/Wanfq/KCA_data
https://huggingface.co/datasets/WizardLMTeam/WizardLM_evol_instruct_70k

## wang1r/Qwen3-0.6B-safety-math

No. The cached README fetch was a 403, and the raw README returns 401 because the repository is gated. The public model page still shows the card. That card describes thinking-math SFT ("M3-distilled, reject-sampled CoT") and contrastive DPO, and it does not name a corpus a reader can open. Searches for the name find other people's checkpoints, not this repository's data.

https://huggingface.co/wang1r/Qwen3-0.6B-safety-math

## wangsir123/guard-4-handle

No. The cached card and the live card are the Llama Guard 4 card. They say the model was post-trained on a blend of data from Llama Guard 3-8B and Llama Guard 3-11B-vision, plus multi-image and multilingual data. Those phrases are not a dataset a reader can open. `handler.py` is an inference handler. The Llama Guard 3 model card names hh-rlhf for that earlier model, not for this checkpoint.

https://huggingface.co/wangsir123/guard-4-handle
https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard3/8B/MODEL_CARD.md

## wasxy47/jailbreak-guard-qwen2.5-1.5b

Yes. The cached card and the live card match. The card says the training data are `jackhhao/jailbreak-classification` and `Anthropic/hh-rlhf`, and it links `wasxy47/jailbreak-guard-dataset`. All three Hub dataset pages load.

https://huggingface.co/wasxy47/jailbreak-guard-qwen2.5-1.5b
https://huggingface.co/datasets/jackhhao/jailbreak-classification
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://huggingface.co/datasets/wasxy47/jailbreak-guard-dataset
