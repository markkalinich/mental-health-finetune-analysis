# Dataset search, agent 113

## kmseong/llama2_7b_chat_gsm8k_resta_gamma0.3

No. There is no cached card. The live README says the training data is the Circuit Breakers dataset and that the base model is Llama-3.2-3B-Instruct. `mergekit_config.yml` builds the weights as a linear merge of `kmseong/llama2_7b-chat_gsm8k_full_ft_lr5e-5`, `kmseong/llama2_7b-chat-Safety-FT-lr5e-5`, and `meta-llama/Llama-2-7b-hf`. That file names other model repositories. A word in those repository names is not a dataset.

https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_resta_gamma0.3/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_resta_gamma0.3/raw/main/mergekit_config.yml

## kmseong/llama2_7b_chat_gsm8k_SSFT_lr5e-5

Yes. There is no cached card. `finetune_config.json` says the dataset is GSM8K and that 7,473 training samples were used. That count is the train split of `openai/gsm8k`, and the dataset card loads. The README's Circuit Breakers sentence is the same template used on the other checkpoints.

https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_SSFT_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat_MATH_FT_lr3e-5

Yes. There is no cached card. `finetune_config.json` names Hendrycks MATH and says the source is official. The official GitHub README points to `qwedsacf/competition_math`, and that page loads with competition problems. `ck46/hendrycks_math` also loads. The Hub copy `hendrycks/competition_math` says access has been disabled.

https://huggingface.co/kmseong/llama2_7b_chat_MATH_FT_lr3e-5/raw/main/finetune_config.json
https://github.com/hendrycks/math
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/ck46/hendrycks_math

## kmseong/llama2_7b_chat_MBPP-FT-SafeDelta-s0.1-lr5e-5

No. There is no cached card. The README says the training data is the Circuit Breakers dataset and that the base model is Llama-3.2-3B-Instruct. The repository files are weights, tokenizer files, and a Llama-2 `config.json` (32 layers, vocabulary size 32,000). No training script names a corpus. The SafeDelta paper and its GitHub repository do not name this checkpoint.

https://huggingface.co/kmseong/llama2_7b_chat_MBPP-FT-SafeDelta-s0.1-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_chat_MBPP-FT-SafeDelta-s0.1-lr5e-5/raw/main/config.json

## kmseong/llama2_7b_chat_mbpp_ft_freeze_rsn_lr5e-5

Yes. There is no cached card. `finetune_config.json` sets the dataset to mbpp, sets `mbpp_dataset_name` to `google-research-datasets/mbpp`, and sets the train split to 374 examples. That dataset page loads.

https://huggingface.co/kmseong/llama2_7b_chat_mbpp_ft_freeze_rsn_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/google-research-datasets/mbpp

## kmseong/llama2_7b_chat_mbpp_ft_freeze_sn_lr5e-5

Yes. There is no cached card. `finetune_config.json` sets the dataset to mbpp, sets `mbpp_dataset_name` to `google-research-datasets/mbpp`, and sets the train split to 374 examples. That dataset page loads.

https://huggingface.co/kmseong/llama2_7b_chat_mbpp_ft_freeze_sn_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/google-research-datasets/mbpp

## kmseong/llama2_7b_chat_medaq_resta_gamma0.3

No. There is no cached card. The live README says the training data is the Circuit Breakers dataset. `mergekit_config.yml` builds the weights as a linear merge of `kmseong/llama2_7b_chat-SSFT-MEDQA-FT-lr3e-5`, `kmseong/llama2_7b-chat-Safety-FT-lr5e-5`, and `meta-llama/Llama-2-7b-hf`. That file names other model repositories, not a dataset.

https://huggingface.co/kmseong/llama2_7b_chat_medaq_resta_gamma0.3/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_chat_medaq_resta_gamma0.3/raw/main/mergekit_config.yml

## kmseong/llama2_7b_chat_medqa_ft_freeze_rsn_lr1e-5

Yes. The cached card and the live README both say the training data is the Circuit Breakers dataset, and the usage example names a different repository, `kmseong/llama2_7b_base_medqa_ft_freeze_rsn_lr1e-5`. `finetune_config.json` names MedQA (USMLE). The local path in that file does not open. `awinml/medqa` loads USMLE questions, and `GBaker/MedQA-USMLE-4-options-hf` loads with a train split of 10.2k rows, the 10,178-question USMLE train set.

https://huggingface.co/kmseong/llama2_7b_chat_medqa_ft_freeze_rsn_lr1e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/awinml/medqa
https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options-hf

## kmseong/llama2_7b_chat_only_rsn_tuned_lr3e-5_revised

No. There is no cached card. The README says the training data is the Circuit Breakers dataset and that the base model is Llama-3.2-3B-Instruct. The repository has no training config. The Hub model record shows a Llama-2 chat template and 6.7 billion parameters. Searches did not find a paper or GitHub page that names this repository and a corpus.

https://huggingface.co/kmseong/llama2_7b_chat_only_rsn_tuned_lr3e-5_revised/raw/main/README.md

## kmseong/llama2_7b_chat_only_rsn_tuned_lr5e-5

No. There is no cached card. The README says the training data is the Circuit Breakers dataset and that the base model is Llama-3.2-3B-Instruct. The repository has no training config. `config.json` is a Llama-2 7B model (32 layers, vocabulary size 32,000). Searches did not find a paper or GitHub page that names this repository and a corpus.

https://huggingface.co/kmseong/llama2_7b_chat_only_rsn_tuned_lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_chat_only_rsn_tuned_lr5e-5/raw/main/config.json
