# Dataset search, agent 114

## kmseong/llama2_7b_chat_only_rsn_tuned_lr5e-5_revised

Yes. There is no cached card. The current card says the training data is the Circuit Breakers dataset. The repo has no training script. That corpus opens: the Hub dataset `abhayesian/circuit-breakers-dataset` loads, and its first prompt matches the Circuit Breakers train file on GitHub. A Hub page at `GraySwanAI/CircuitBreakers` returns 401, so that page is a private repo and is not the opened copy.

https://huggingface.co/kmseong/llama2_7b_chat_only_rsn_tuned_lr5e-5_revised
https://huggingface.co/datasets/abhayesian/circuit-breakers-dataset
https://huggingface.co/datasets/x5fu/circuitbreaker-dataset
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/circuit_breakers_train.json

## kmseong/llama2_7b_chat_only_sn_tuned_lr5e-5_revised

Yes. There is no cached card. The current card uses the same training-data line, Circuit Breakers dataset, and prints this repo id in the usage example. The file list is weights and tokenizer files only. The same Hub dataset and GitHub train file open.

https://huggingface.co/kmseong/llama2_7b_chat_only_sn_tuned_lr5e-5_revised
https://huggingface.co/datasets/abhayesian/circuit-breakers-dataset
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json

## kmseong/llama2_7b_chat_seal_5e-5

Yes. There is no cached card. The card body does not name a corpus. `sft_config.json` in this repo sets `"dataset": "openai/gsm8k"` and `num_train_samples` 5978 of 7473. The Hub page for `openai/gsm8k` loads, and the train split has 7,473 rows. The author repo lists this id in its Llama-2-7B-chat / GSM8K table. The selected-index file named in the config is a local path and is not in the repo.

https://huggingface.co/kmseong/llama2_7b_chat_seal_5e-5
https://huggingface.co/kmseong/llama2_7b_chat_seal_5e-5/raw/main/sft_config.json
https://huggingface.co/datasets/openai/gsm8k
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/gsm8k_train_task_7473.json

## kmseong/llama2_7b_chat_seal_warp_5e-5

Yes. There is no cached card. The card text matches the other SEAL upload. This repo's `sft_config.json` sets `"mode": "WaRP"` and `"dataset": "openai/gsm8k"`, again 5,978 of 7,473 rows. `openai/gsm8k` loads. The author results file names this repo as the SEAL plus weight-space-rotation pair of the previous checkpoint.

https://huggingface.co/kmseong/llama2_7b_chat_seal_warp_5e-5
https://huggingface.co/kmseong/llama2_7b_chat_seal_warp_5e-5/raw/main/sft_config.json
https://huggingface.co/datasets/openai/gsm8k
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/RESULTS.md

## kmseong/llama2_7b_chat_sn_tuned_lr5e-5

Yes. There is no cached card. The current card says the training data is the Circuit Breakers dataset and prints this repo id. No training script is in the repo. The Hub dataset and the Circuit Breakers train file open.

https://huggingface.co/kmseong/llama2_7b_chat_sn_tuned_lr5e-5
https://huggingface.co/datasets/abhayesian/circuit-breakers-dataset
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json

## kmseong/llama2_7b_chat_WaRP-SN-Tune_lr5e-5

Yes. There is no cached card. The card says the training data is the Circuit Breakers dataset. `warp_sn_tune_config.json` does not name a corpus, and it sets `max_samples` to 4994. The same author's `sn_tune/README.md` prints this repo id and says the safety corpus is `circuit_breakers_train.json` with 4,994 rows. That file opens, and so does `abhayesian/circuit-breakers-dataset`.

https://huggingface.co/kmseong/llama2_7b_chat_WaRP-SN-Tune_lr5e-5
https://huggingface.co/kmseong/llama2_7b_chat_WaRP-SN-Tune_lr5e-5/raw/main/warp_sn_tune_config.json
https://huggingface.co/datasets/abhayesian/circuit-breakers-dataset
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/sn_tune/README.md
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/circuit_breakers_train.json

## kmseong/llama2_7B_chat_WaRP_safety_basis_gsm8k_FT_lr3e-5

No. The cached card and the current card match. The body says which layers were rotated and then trained, and it does not name a corpus. The tags include both `gsm8k` and `circuit-breakers`. The citation author is "Your Name", and that title is not a paper. The repo has no training config. The author GitHub describes GSM8K as the downstream task for this method, and it does not print this repo id.

https://huggingface.co/kmseong/llama2_7B_chat_WaRP_safety_basis_gsm8k_FT_lr3e-5
https://github.com/min-seong-kim/Safety-WaRP-LLM

## kmseong/llama2_7b_gsm8k_ft_freeze_sn_lr3e-5

Yes. There is no cached card. `finetune_config.json` names the dataset GSM8K, with 7,473 train samples, and the strategy line is "Freeze safety neurons, train others." 7,473 is the GSM8K train split, and `openai/gsm8k` loads. The card's training-data line says Circuit Breakers dataset, the same sentence used on the other safety-neuron cards. The config's sample count matches GSM8K.

https://huggingface.co/kmseong/llama2_7b_gsm8k_ft_freeze_sn_lr3e-5
https://huggingface.co/kmseong/llama2_7b_gsm8k_ft_freeze_sn_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/gsm8k_train_task_7473.json

## kmseong/llama2_7b_only_sn_tuned_lr3e-5_revised

Yes. There is no cached card. The current card says the training data is the Circuit Breakers dataset and prints this repo id. The repo files are weights and tokenizer files. The Hub dataset and the Circuit Breakers train file open.

https://huggingface.co/kmseong/llama2_7b_only_sn_tuned_lr3e-5_revised
https://huggingface.co/datasets/abhayesian/circuit-breakers-dataset
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json

## kmseong/llama2_7b_only_sn_tuned_lr5e-5

Yes. There is no cached card. The current card says the training data is the Circuit Breakers dataset and prints this repo id. No training script is in the repo. The same Hub dataset and GitHub train file open.

https://huggingface.co/kmseong/llama2_7b_only_sn_tuned_lr5e-5
https://huggingface.co/datasets/abhayesian/circuit-breakers-dataset
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
