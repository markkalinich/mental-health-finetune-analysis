## kmseong/Llama-3.1-8B-Instruct-ssft_lr5e-5

Yes. There is no cached card. The current README names two corpora, LibrAI/do-not-answer and openai/gsm8k, and both Hub dataset pages load. model_metadata.json names this repo id and Safety-First WaRP, and it does not name a dataset. The citation is a stub with no arXiv id.

https://huggingface.co/kmseong/Llama-3.1-8B-Instruct-ssft_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/LibrAI/do-not-answer
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-3.1-8b-instruct_rsn_tuned_math_ft_lr3e-5

Yes. The README says the training data is the Circuit Breakers dataset and that the base model is Llama-3.2-3B-Instruct, which is not this 8B repo. finetune_config.json in this repo says the fine-tune dataset is hendrycks_math, at learning rate 3e-5, starting from kmseong/llama-3-8b-instruct-only-rsn-tuned-lr5e-5. The Hub dataset EleutherAI/hendrycks_math loads. A search for this repo id did not find a paper.

https://huggingface.co/kmseong/llama-3.1-8b-instruct_rsn_tuned_math_ft_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math

## kmseong/llama-3.1-8b-instruct_sn_tuned_math_ft_lr3e-5

Yes. The README again says Circuit Breakers and names Llama-3.2-3B-Instruct as the base. finetune_config.json says the fine-tune dataset is hendrycks_math, at learning rate 3e-5, starting from kmseong/llama-3-8b-instruct-only-sn-tuned-lr5e-5. EleutherAI/hendrycks_math loads. A search for this repo id did not find a paper.

https://huggingface.co/kmseong/llama-3.1-8b-instruct_sn_tuned_math_ft_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math

## kmseong/llama-3.1-8B-only-sn-tuned-lr5e-5

Yes. The README says the training data is the Circuit Breakers dataset, and the usage block prints this repo id. The repo has no fine-tune config. The Circuit Breakers training file on GitHub opens and contains prompt rows. The card's base-model line says Llama-3.2-3B-Instruct, which does not match this 8B repo id.

https://huggingface.co/kmseong/llama-3.1-8B-only-sn-tuned-lr5e-5/raw/main/README.md
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json

## kmseong/llama-3.2-3b-instruct-gsm8k-rsn-tuned-lr5e-5

Yes. The README says Circuit Breakers. finetune_config.json says the dataset is GSM8K, with 7473 train samples, which is the openai/gsm8k train split, at learning rate 5e-5. That Hub dataset page loads. A search for this repo id did not find a paper.

https://huggingface.co/kmseong/llama-3.2-3b-instruct-gsm8k-rsn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-3.2-3b-instruct-gsm8k-sn-tuned-lr5e-5

Yes. The README says Circuit Breakers. finetune_config.json says the dataset is GSM8K, with 7473 train samples, at learning rate 5e-5. openai/gsm8k loads. A search for this repo id did not find a paper.

https://huggingface.co/kmseong/llama-3.2-3b-instruct-gsm8k-sn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/Llama-3.2-3B-instruct-gsm8k-WaRP_lr5e-5

Yes. The README in this repo names LibrAI/do-not-answer and openai/gsm8k, and both Hub pages load. That README text describes a Llama 3.1 8B WaRP model, and the usage example uses a different model id. model_metadata.json names this repo id and Safety-First WaRP, and it does not name a dataset. An arXiv search did not find a paper about this checkpoint.

https://huggingface.co/kmseong/Llama-3.2-3B-instruct-gsm8k-WaRP_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/LibrAI/do-not-answer
https://huggingface.co/datasets/openai/gsm8k

## kmseong/Llama-3.2-3B-instruct-MATH-LoRA

No. The README says this is a merged Safe LoRA upload from the local path /home/yonsei_jong/SafeLoRA/math_lora_merged, and it does not name a corpus. The repo has no training script or fine-tune config, and config.json is only the Llama architecture. Searches for this repo id on the Hub, GitHub, and arXiv did not find a source that names training data for this checkpoint.

https://huggingface.co/kmseong/Llama-3.2-3B-instruct-MATH-LoRA/raw/main/README.md

## kmseong/llama-3.2-3b-instruct-math-rsn-tuned-lr5e-5

Yes. The README says Circuit Breakers. finetune_config.json says the dataset is hendrycks_math, from the official source, all subjects and levels, at learning rate 5e-5. EleutherAI/hendrycks_math loads. A GitHub search did not find a training repo for this checkpoint.

https://huggingface.co/kmseong/llama-3.2-3b-instruct-math-rsn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math

## kmseong/llama-3.2-3b-instruct-math-sn-tuned-lr5e-5

Yes. The README says Circuit Breakers. finetune_config.json says the dataset is hendrycks_math, from the official source, at learning rate 5e-5. EleutherAI/hendrycks_math loads. An arXiv search did not find a paper about this checkpoint.

https://huggingface.co/kmseong/llama-3.2-3b-instruct-math-sn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
