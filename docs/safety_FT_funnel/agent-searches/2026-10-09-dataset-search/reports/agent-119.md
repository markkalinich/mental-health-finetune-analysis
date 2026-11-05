## kmseong/llama3_2_3b_instruct_resta_0.3_lr5e-5

No. There is no cached card. The live README says the training data is the Circuit Breakers dataset and calls this an SN-Tune of Llama-3.2-3B-Instruct. That paragraph is the same text as unrelated kmseong repos. `mergekit_config.yml` in this repo is a linear merge of three local checkpoints under `/home/yonsei_jong/resta/saved_models/`, and those paths do not open.

https://huggingface.co/kmseong/llama3_2_3b_instruct_resta_0.3_lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama3_2_3b_instruct_resta_0.3_lr5e-5/raw/main/mergekit_config.yml

## kmseong/llama3_2_3b_instruct_rsn_tuned_math_ft_lr5e-5

Yes. `finetune_config.json` in this repo names the training set `hendrycks_math`, source `official`, starting from `kmseong/llama3_2_3b_instruct_only_rsn_tuned_lr5e-5`. The README's Circuit Breakers line is the shared boilerplate and names the wrong base model. The official Hub copy `hendrycks/competition_math` says access is disabled, `lighteval/MATH` returned 401, and `github.com/hendrycks/math` has loaders rather than the problems, while three other Hub pages opened with the Hendrycks MATH problems. The config's learning rate is 1e-5, while the repo name says 5e-5, and `num_train_samples` is 0.

https://huggingface.co/kmseong/llama3_2_3b_instruct_rsn_tuned_math_ft_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval

## kmseong/llama3_2_3b_instruct_sn_tuned_math_ft_lr5e-5

Yes. `finetune_config.json` in this repo names the training set `hendrycks_math`, source `official`, starting from `kmseong/llama3_2_3b_instruct_only_sn_tuned_lr5e-5`. The README again says Circuit Breakers and Llama-3.2-3B-Instruct as a generic SN-Tune card. The same three Hub pages opened with the Hendrycks MATH problems. The config's learning rate is 1e-5, while the repo name says 5e-5, and `num_train_samples` is 0.

https://huggingface.co/kmseong/llama3_2_3b_instruct_sn_tuned_math_ft_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval

## kmseong/llama3_8b_instruct-MATH_FT_lr1e-5

Yes. `finetune_config.json` names the dataset `Hendrycks MATH`, source `official`, with base `meta-llama/Meta-Llama-3-8B-Instruct` and learning rate 1e-5. The README's Circuit Breakers line and its Llama-3.2-3B base do not match this 8B repo. The same three Hub pages opened with the Hendrycks MATH problems. `num_train_samples` is 0.

https://huggingface.co/kmseong/llama3_8b_instruct-MATH_FT_lr1e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval

## kmseong/llama3_8b_instruct-MATH_FT_lr3e-5

Yes. `finetune_config.json` names the dataset `Hendrycks MATH`, source `official`, with base `meta-llama/Meta-Llama-3-8B-Instruct`, learning rate 3e-5, and 3 epochs. The README is the same Circuit Breakers boilerplate. The same three Hub pages opened with the Hendrycks MATH problems. `num_train_samples` is 0.

https://huggingface.co/kmseong/llama3_8b_instruct-MATH_FT_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval

## kmseong/llama3_8b_instruct-MATH_FT_lr3e-5_5epcohs

Yes. `finetune_config.json` names the dataset `Hendrycks MATH`, source `official`, with base `meta-llama/Meta-Llama-3-8B-Instruct`, learning rate 3e-5, and 5 epochs. The README is the same Circuit Breakers boilerplate. The same three Hub pages opened with the Hendrycks MATH problems. `num_train_samples` is 0.

https://huggingface.co/kmseong/llama3_8b_instruct-MATH_FT_lr3e-5_5epcohs/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval

## kmseong/llama3_8b_instruct-MATH_FT_lr5e-5

Yes. `finetune_config.json` names the dataset `Hendrycks MATH`, source `official`, with base `meta-llama/Meta-Llama-3-8B-Instruct` and learning rate 5e-5. The README is the same Circuit Breakers boilerplate, and a search of this repo name found no paper. The same three Hub pages opened with the Hendrycks MATH problems. `num_train_samples` is 0.

https://huggingface.co/kmseong/llama3_8b_instruct-MATH_FT_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval

## kmseong/qwen-2.5-7B-Instruct-WaRP-safeinstr-p10-lr5e-5

No. There is no cached card. `model_metadata.json` prints this repo id and does not name a dataset. The README is titled WaRP-Safety-Llama3_8B_Instruct, says the base is Llama-3.1-8B-Instruct, and its usage code loads `kmseong/WaRP-Safety-Llama3_8B_Instruct`, while the weights in this repo are Qwen2. That README names LibrAI/do-not-answer and openai/gsm8k, and LibrAI/do-not-answer does load, but no GitHub repo or paper turned up for this id.

https://huggingface.co/kmseong/qwen-2.5-7B-Instruct-WaRP-safeinstr-p10-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/qwen-2.5-7B-Instruct-WaRP-safeinstr-p10-lr5e-5/raw/main/model_metadata.json
https://huggingface.co/datasets/LibrAI/do-not-answer

## kmseong/qwen2_5_32b-instruct-gsm8k-rsn-tuned-lr5e-5

Yes. `finetune_config.json` names the dataset GSM8K, with 7473 training examples, starting from `kmseong/qwen2_5_32b-instruct-only-rsn-tuned-lr5e-5`. 7473 is the train split of `openai/gsm8k`, and that Hub page opened. The README's Circuit Breakers line calls this a Llama-3.2-3B SN-Tune, which does not match this Qwen2 32B repo. A search of this repo name found no paper about it.

https://huggingface.co/kmseong/qwen2_5_32b-instruct-gsm8k-rsn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/qwen2_5_32b-instruct-gsm8k-sn-tuned-lr5e-5

Yes. `finetune_config.json` names the dataset GSM8K, with 7473 training examples, starting from `kmseong/qwen2_5_32b-instruct-only-sn-tuned-lr5e-5`. That count matches the train split of `openai/gsm8k`, and that Hub page opened. The README is the same Circuit Breakers boilerplate and names Llama-3.2-3B-Instruct.

https://huggingface.co/kmseong/qwen2_5_32b-instruct-gsm8k-sn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k
