## kmseong/llama3_1_8b_instruct_MATH_lr5e-5

Yes. `finetune_config.json` in this repository names the training corpus Hendrycks MATH, with `math_dataset_source` official, `safety_mix_ratio` 0.0, and `safety_data_path` null. There was no cached card. The live card says the training data is the Circuit Breakers dataset and the base model is Llama-3.2-3B-Instruct; this checkpoint has 8,030,261,248 parameters, and the config names parent `kmseong/Llama-3.1-8B-Instruct-ssft_lr5e-5`. The official MATH GitHub README tells readers to download the data from `qwedsacf/competition_math`, which loads, and `EleutherAI/hendrycks_math` also loads with the competition problems.

https://huggingface.co/kmseong/llama3_1_8b_instruct_MATH_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://github.com/hendrycks/math

## kmseong/llama3_2_3b-instruct-gsm8k_ssft_lr5e-5

Yes. `finetune_config.json` sets `dataset` to GSM8K and `num_train_samples` to 7473, the train-split size of `openai/gsm8k`, and sets `safety_mix_ratio` to 0.0. The live card says the training data is the Circuit Breakers dataset. `openai/gsm8k` loads. No cached card was present, and no paper about this checkpoint turned up.

https://huggingface.co/kmseong/llama3_2_3b-instruct-gsm8k_ssft_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama3_2_3b-instruct-math_safeInstr_10p

Yes. `finetune_config.json` names Hendrycks MATH, source official, `safety_mix_ratio` 0.1, and `safety_data_path` `/home/yonsei_jong/Safety-Neuron/neuron_detection/corpus_all/circuit_breakers_train.json`. The MATH corpus opens at `qwedsacf/competition_math` and `EleutherAI/hendrycks_math`. The local path does not open. The public dataset `longphann/circuit_breakers_train` does, with 4,994 rows. The live card's title is `llama3_2_3b-instruct-math_safeInstr_10p_lr3e-5` and says the training data is the Circuit Breakers dataset; the config's learning rate is 3e-05. `num_train_samples` is 0.

https://huggingface.co/kmseong/llama3_2_3b-instruct-math_safeInstr_10p/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/longphann/circuit_breakers_train

## kmseong/llama3_2_3b-instruct-math_safeInstr_10p_lr5e-5

Yes. `finetune_config.json` names Hendrycks MATH, source official, a 0.1 safety mix, and the same local `circuit_breakers_train.json` path, with learning rate 5e-05. Both corpora open on the Hub pages below. The live card's title and usage block use this repository id and say the training data is the Circuit Breakers dataset. `num_train_samples` is 0.

https://huggingface.co/kmseong/llama3_2_3b-instruct-math_safeInstr_10p_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/longphann/circuit_breakers_train

## kmseong/llama3_2_3b-instruct-SSFT-lr5e-5

No. The README is titled WaRP-Safety-Llama3_8B_Instruct, names base model `meta-llama/Llama-3.1-8B-Instruct`, and its usage block loads `kmseong/WaRP-Safety-Llama3_8B_Instruct`. Under that title it lists LibrAI/do-not-answer and openai/gsm8k. `model_metadata.json` sets `model_id` to `kmseong/llama3_2_3b-instruct-Safety-FT-lr5e-5-20260428_160224` and does not name a dataset. This checkpoint is 3.2B parameters. No paper or GitHub training script for this repository id turned up.

https://huggingface.co/kmseong/llama3_2_3b-instruct-SSFT-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama3_2_3b-instruct-SSFT-lr5e-5/raw/main/model_metadata.json

## kmseong/llama3_2_3b-instruct-WaRP_lr5e-5

No. The README is the same WaRP-Safety-Llama3_8B_Instruct card. It lists LibrAI/do-not-answer and openai/gsm8k and does not print this repository id. `model_metadata.json` sets `model_id` to `kmseong/llama3_2_3b-instruct-WaRP_lr5e-5` and `training_method` to Safety-First WaRP, and it does not name a dataset. The weights are 3.2B parameters.

https://huggingface.co/kmseong/llama3_2_3b-instruct-WaRP_lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama3_2_3b-instruct-WaRP_lr5e-5/raw/main/model_metadata.json

## kmseong/llama3_2_3b_instruct_MATH_lr5e-5

Yes. `finetune_config.json` names Hendrycks MATH, source official, `safety_mix_ratio` 0.0, and `safety_data_path` null. The live card says the training data is the Circuit Breakers dataset. The MATH Hub pages below load. The parent in the config is `kmseong/llama3_2_3b-instruct-SSFT-lr5e-5`.

https://huggingface.co/kmseong/llama3_2_3b_instruct_MATH_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/EleutherAI/hendrycks_math

## kmseong/llama3_2_3b_instruct_MATH_SSFT_lr5e-5

Yes. `finetune_config.json` in this repository names Hendrycks MATH, source official. The live card's title and usage block use `kmseong/llama3_2_3b_instruct_MATH_lr5e-5` and say the training data is the Circuit Breakers dataset. The MATH Hub pages below load. The parent in the config is `kmseong/llama3_2_3b-instruct-Safety-FT-lr5e-5-20260428_160224`.

https://huggingface.co/kmseong/llama3_2_3b_instruct_MATH_SSFT_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/EleutherAI/hendrycks_math

## kmseong/llama3_2_3b_instruct_only_rsn_tuned_lr5e-5

Yes. There was no cached card and no `finetune_config.json`. The live card's title and usage block use this repository id and say the training data is the Circuit Breakers dataset. `longphann/circuit_breakers_train` loads, with 4,994 rows. Searches did not find a paper about this checkpoint.

https://huggingface.co/kmseong/llama3_2_3b_instruct_only_rsn_tuned_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/longphann/circuit_breakers_train

## kmseong/llama3_2_3b_instruct_only_sn_tuned_lr5e-5

Yes. The live card's title and usage block use this repository id and say the training data is the Circuit Breakers dataset. The same Hub dataset loads, with 4,994 rows. The file list has no training script or fine-tune config. No cached card was present.

https://huggingface.co/kmseong/llama3_2_3b_instruct_only_sn_tuned_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/longphann/circuit_breakers_train
