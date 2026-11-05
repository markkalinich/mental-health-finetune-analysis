# Agent 104 dataset search

## kmseong/Llama-3.1-8B-base-gsm8k-SSFT_lr1e-5

Yes. There is no cached card. The live README is a WaRP template that also lists LibrAI/do-not-answer, but `finetune_config.json` in this repo sets the dataset to GSM8K, 7,473 examples, and `safety_data_path` to null. 7,473 is the GSM8K train split, and the Hub page for openai/gsm8k loads.

https://huggingface.co/kmseong/Llama-3.1-8B-base-gsm8k-SSFT_lr1e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/Llama-3.1-8B-base-gsm8k-SSFT_lr5e-5

Yes. There is no cached card. `finetune_config.json` names GSM8K, 7,473 examples, learning rate 5e-5, and a null safety-data path. The base it records is kmseong/Llama-3.1-8B-base-SSFT_lr5e-5. openai/gsm8k loads. The README again lists LibrAI/do-not-answer, and the config does not.

https://huggingface.co/kmseong/Llama-3.1-8B-base-gsm8k-SSFT_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/Llama-3.1-8B-base-gsm8k-warp-lr5e-5

Yes. There is no cached card and no `finetune_config.json`. The live README names safety data LibrAI/do-not-answer and utility data openai/gsm8k, and both Hub pages load. The README title and the usage snippet name a different id, kmseong/WaRP-Safety-Llama3_8B_Instruct. `model_metadata.json` does not name a dataset.

https://huggingface.co/kmseong/Llama-3.1-8B-base-gsm8k-warp-lr5e-5/raw/main/README.md
https://huggingface.co/datasets/LibrAI/do-not-answer
https://huggingface.co/datasets/openai/gsm8k

## kmseong/Llama-3.1-8B-base-SSFT_lr5e-5

Yes. There is no cached card and no `finetune_config.json`. The live README names LibrAI/do-not-answer and openai/gsm8k, and both Hub pages load. The same README text is the WaRP template, and its usage snippet points at kmseong/WaRP-Safety-Llama3_8B_Instruct. Two later configs name this repo as their base and then train on GSM8K.

https://huggingface.co/kmseong/Llama-3.1-8B-base-SSFT_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/LibrAI/do-not-answer
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-3.1-8B-gsm8k-rsn-tuned-lr5e-5

Yes. There is no cached card. The README says the training data is the Circuit Breakers dataset and names Llama-3.2-3B-Instruct as the base, which is not this 8B repo. `finetune_config.json` says the dataset is GSM8K, 7,473 examples, and the base is kmseong/llama-3.1-8B-only-rsn-tuned-lr5e-5. openai/gsm8k loads.

https://huggingface.co/kmseong/llama-3.1-8B-gsm8k-rsn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-3.1-8B-gsm8k-sn-tuned-lr5e-5

Yes. There is no cached card. The README again says Circuit Breakers and names a 3B base. `finetune_config.json` says GSM8K, 7,473 examples, and the base is kmseong/llama-3.1-8B-only-sn-tuned-lr5e-5. openai/gsm8k loads.

https://huggingface.co/kmseong/llama-3.1-8B-gsm8k-sn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-3.1-8b-instruct-math-rsn-tuned-lr5e-5

Yes. There is no cached card. The README says Circuit Breakers and names Llama-3.2-3B-Instruct. `finetune_config.json` says the dataset is hendrycks_math from the official source, and the base is kmseong/llama-3.1-8b-instruct-only-rsn-tuned-lr5e-5. The official MATH repo points at qwedsacf/competition_math, and that page loads. EleutherAI/hendrycks_math also loads. hendrycks/competition_math says access is disabled.

https://huggingface.co/kmseong/llama-3.1-8b-instruct-math-rsn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://github.com/hendrycks/math

## kmseong/llama-3.1-8b-instruct-math-sn-tuned-lr5e-5

Yes. There is no cached card. The README says Circuit Breakers and names a 3B base. `finetune_config.json` says hendrycks_math, official source, and the base is kmseong/llama-3.1-8b-instruct-only-sn-tuned-lr5e-5. qwedsacf/competition_math and EleutherAI/hendrycks_math both load.

https://huggingface.co/kmseong/llama-3.1-8b-instruct-math-sn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://github.com/hendrycks/math

## kmseong/llama-3.1-8b-instruct-only-rsn-tuned-lr5e-5

Yes. There is no cached card and no `finetune_config.json`. The README names the training data as the Circuit Breakers dataset. The heading is this repo id, and the base-model line says Llama-3.2-3B-Instruct. The Circuit Breakers training file is `data/circuit_breakers_train.json` in GraySwanAI/circuit-breakers, and that GitHub page resolves. abhayesian/circuit-breakers-dataset also loads, and its card is empty, so it is not recorded as this corpus.

https://huggingface.co/kmseong/llama-3.1-8b-instruct-only-rsn-tuned-lr5e-5/raw/main/README.md
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json

## kmseong/llama-3.1-8b-instruct-only-sn-tuned-lr5e-5

Yes. There is no cached card and no `finetune_config.json`. The README names the Circuit Breakers dataset and, in the base-model line, Llama-3.2-3B-Instruct. The heading is this repo id. The same GraySwanAI training file opens. Two math configs name this repo as their base and then train on hendrycks_math.

https://huggingface.co/kmseong/llama-3.1-8b-instruct-only-sn-tuned-lr5e-5/raw/main/README.md
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
