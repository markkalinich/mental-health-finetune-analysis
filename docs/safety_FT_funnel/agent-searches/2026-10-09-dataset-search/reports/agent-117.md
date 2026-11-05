# Dataset search, agent 117

No cached card exists for any of these ten repositories. Each live README is the same template: it names the Circuit Breakers dataset and `meta-llama/Llama-3.2-3B-Instruct`. Each repository also contains `finetune_config.json`. That file names Hendrycks MATH or GSM8K, and those pages open. The template's base-model line does not match the config or the 8B weight count.

## kmseong/llama3.1_8b_instruct_MATH_FT_lr3e-5

Yes. `finetune_config.json` names the dataset Hendrycks MATH and sets `math_dataset_source` to official. The base model in that file is `meta-llama/Llama-3.1-8B-Instruct`. The README template instead says Circuit Breakers and Llama-3.2-3B-Instruct. Hendrycks MATH opens at `EleutherAI/hendrycks_math` and at `qwedsacf/competition_math`. The official GitHub README points at the second of those. A search for this repo id did not find a paper.

https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH_FT_lr3e-5/raw/main/README.md
https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH_FT_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://github.com/hendrycks/math

## kmseong/llama3.1_8b_instruct_MATH_FT_lr3e-5_freeze_rsn

Yes. `finetune_config.json` names the dataset `hendrycks_math`, source official, and the fine-tuning type Hendrycks MATH Fine-tuning with Safety Neuron Freezing. The base model in that file is `meta-llama/Llama-3.1-8B-Instruct`. The README is the same Circuit Breakers template. The MATH problems open at the two Hub pages below. No paper about this repo id turned up.

https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH_FT_lr3e-5_freeze_rsn/raw/main/README.md
https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH_FT_lr3e-5_freeze_rsn/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://github.com/hendrycks/math

## kmseong/llama3.1_8b_instruct_MATH_FT_lr3e-5_freeze_sn

Yes. `finetune_config.json` names `hendrycks_math`, source official, with the same safety-neuron freezing description as the freeze_rsn repo. The base model in the file is `meta-llama/Llama-3.1-8B-Instruct`. The README is the Circuit Breakers template. The MATH pages below load. No paper about this repo id turned up.

https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH_FT_lr3e-5_freeze_sn/raw/main/README.md
https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH_FT_lr3e-5_freeze_sn/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://github.com/hendrycks/math

## kmseong/llama31_8b_base_gsm8k_ft_freeze_sn_lr1e-5

Yes. `finetune_config.json` names the dataset GSM8K and sets `num_train_samples` to 7473. That is the train split size on `openai/gsm8k`, and that Hub page loads. The README is the Circuit Breakers template. The config's base model is a local path, `only_sn_tuned_model_llama31_8b_base_lr3e-5_lr3e-5_20260418_214359`. No paper about this repo id turned up.

https://huggingface.co/kmseong/llama31_8b_base_gsm8k_ft_freeze_sn_lr1e-5/raw/main/README.md
https://huggingface.co/kmseong/llama31_8b_base_gsm8k_ft_freeze_sn_lr1e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama31_8b_base_gsm8k_ft_freeze_sn_lr3e-5

Yes. `finetune_config.json` names GSM8K and 7473 training samples, the train split of `openai/gsm8k`. The README is the Circuit Breakers template. The config's base model is the same local path as the lr1e-5 repo above. The Hub dataset page loads. No paper about this repo id turned up.

https://huggingface.co/kmseong/llama31_8b_base_gsm8k_ft_freeze_sn_lr3e-5/raw/main/README.md
https://huggingface.co/kmseong/llama31_8b_base_gsm8k_ft_freeze_sn_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama31_8b_base_gsm8k_ft_freeze_sn_lr3e-5_new

Yes. `finetune_config.json` names GSM8K and 7473 training samples. That matches the train split of `openai/gsm8k`, which loads. The README is the Circuit Breakers template. The config's base model is `kmseong/llama3.1_8b_base_only_sn_tuned_lr3e-5`. The learning rate in the file is 1e-05. No paper about this repo id turned up.

https://huggingface.co/kmseong/llama31_8b_base_gsm8k_ft_freeze_sn_lr3e-5_new/raw/main/README.md
https://huggingface.co/kmseong/llama31_8b_base_gsm8k_ft_freeze_sn_lr3e-5_new/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama31_8b_instruct_gsm8k_ft_freeze_sn_lr3e-5

Yes. `finetune_config.json` names GSM8K and 7473 training samples, the train split of `openai/gsm8k`. The README is the Circuit Breakers template. The config's base model is a local path, `only_sn_tuned_model_llama31_8b_instruct_lr3e-5_lr3e-5_20260418_214406`. The Hub dataset page loads. No paper about this repo id turned up.

https://huggingface.co/kmseong/llama31_8b_instruct_gsm8k_ft_freeze_sn_lr3e-5/raw/main/README.md
https://huggingface.co/kmseong/llama31_8b_instruct_gsm8k_ft_freeze_sn_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama31_8b_instruct_math_ft_freeze_sn_lr1e-5

Yes. `finetune_config.json` names `hendrycks_math`, source official. The README is the Circuit Breakers template. The config's base model is the local instruct path `only_sn_tuned_model_llama31_8b_instruct_lr3e-5_lr3e-5_20260418_214406`. The MATH pages below load. No paper about this repo id turned up.

https://huggingface.co/kmseong/llama31_8b_instruct_math_ft_freeze_sn_lr1e-5/raw/main/README.md
https://huggingface.co/kmseong/llama31_8b_instruct_math_ft_freeze_sn_lr1e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://github.com/hendrycks/math

## kmseong/llama31_8b_instruct_math_ft_freeze_sn_lr3e-5

Yes. `finetune_config.json` names `hendrycks_math`, source official, on the same local instruct base path as the lr1e-5 repo. The README is the Circuit Breakers template. The MATH pages below load. No paper about this repo id turned up.

https://huggingface.co/kmseong/llama31_8b_instruct_math_ft_freeze_sn_lr3e-5/raw/main/README.md
https://huggingface.co/kmseong/llama31_8b_instruct_math_ft_freeze_sn_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://github.com/hendrycks/math

## kmseong/llama31_8b_instruct_math_ft_freeze_sn_lr3e-5_new

Yes. `finetune_config.json` names `hendrycks_math`, source official. The README is the Circuit Breakers template. The config's base model is `kmseong/llama3.1_8b_instruct_only_sn_tuned_lr3e-5`. The MATH pages below load. No paper about this repo id turned up.

https://huggingface.co/kmseong/llama31_8b_instruct_math_ft_freeze_sn_lr3e-5_new/raw/main/README.md
https://huggingface.co/kmseong/llama31_8b_instruct_math_ft_freeze_sn_lr3e-5_new/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://github.com/hendrycks/math
