## kmseong/Llama-2-7b-chat-hf_gsm8k_ft_freeze_basis_rotation_sn_lr5e-5

Yes. This repo's `finetune_config.json` sets the dataset to GSM8K and the training count to 7473, which is the train split of `openai/gsm8k`. The model card instead says Circuit Breakers and Llama-3.2-3B-Instruct. That card text is a template: the weights are a 7B Llama-2 model, and the config names GSM8K. There was no cached card.

https://huggingface.co/kmseong/Llama-2-7b-chat-hf_gsm8k_ft_freeze_basis_rotation_sn_lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/Llama-2-7b-chat-hf_gsm8k_ft_freeze_basis_rotation_sn_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/Llama-2-7b-chat-hf_only_rsn_tuned_lr5e-5_basis_rotation

No. The card says the training data is the Circuit Breakers dataset, and the same paragraph calls this checkpoint Llama-3.2-3B-Instruct. The repo is a 7B Llama-2 model, the file list has no `finetune_config.json`, and the other files do not name a corpus. Web search did not find a paper or GitHub repo that names this checkpoint's data. There was no cached card.

https://huggingface.co/kmseong/Llama-2-7b-chat-hf_only_rsn_tuned_lr5e-5_basis_rotation/raw/main/README.md
https://huggingface.co/api/models/kmseong/Llama-2-7b-chat-hf_only_rsn_tuned_lr5e-5_basis_rotation

## kmseong/llama-2-7b-gsm8k-rsn-tuned-lr5e-5

Yes. `finetune_config.json` sets the dataset to GSM8K and the training count to 7473. That count matches the train split of `openai/gsm8k`, and that Hub page loads. The card's Circuit Breakers line is the same template as the other kmseong cards and disagrees with this file. There was no cached card.

https://huggingface.co/kmseong/llama-2-7b-gsm8k-rsn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama-2-7b-gsm8k-rsn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-2-7b-gsm8k-sn-tuned-lr5e-5

Yes. `finetune_config.json` sets the dataset to GSM8K and the training count to 7473. That is the train split of `openai/gsm8k`, and that Hub page loads. The card's Circuit Breakers line is the shared template and disagrees with this file. There was no cached card.

https://huggingface.co/kmseong/llama-2-7b-gsm8k-sn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama-2-7b-gsm8k-sn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-2-7b-hf-gsm8k-sn-tuned-lr3e-5

Yes. `finetune_config.json` sets the dataset to GSM8K and the training count to 7473, with learning rate 3e-5. The Hub page for `openai/gsm8k` loads. The card's Circuit Breakers line is the shared template and disagrees with this file. There was no cached card.

https://huggingface.co/kmseong/llama-2-7b-hf-gsm8k-sn-tuned-lr3e-5/raw/main/README.md
https://huggingface.co/kmseong/llama-2-7b-hf-gsm8k-sn-tuned-lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama-2-7b-only-rsn-tuned-lr5e-5

No. The card says Circuit Breakers and also says the base model is Llama-3.2-3B-Instruct. `config.json` is a 7B Llama-2 model (`vocab_size` 32000, `intermediate_size` 11008), and the repo has no `finetune_config.json`. Search did not find a paper or GitHub page that names this checkpoint's data. There was no cached card.

https://huggingface.co/kmseong/llama-2-7b-only-rsn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama-2-7b-only-rsn-tuned-lr5e-5/raw/main/config.json
https://huggingface.co/api/models/kmseong/llama-2-7b-only-rsn-tuned-lr5e-5

## kmseong/llama-2-7b-only-sn-tuned-lr5e-5

No. The card says Circuit Breakers and also says the base model is Llama-3.2-3B-Instruct. The file list has no `finetune_config.json` and no other file that names a corpus. Search did not find a paper or GitHub page that names this checkpoint's data. There was no cached card.

https://huggingface.co/kmseong/llama-2-7b-only-sn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/api/models/kmseong/llama-2-7b-only-sn-tuned-lr5e-5

## kmseong/llama-3-8b-instruct-math-rsn-tuned-lr5e-5

Yes. `finetune_config.json` sets the dataset to `hendrycks_math` and the source to official. `EleutherAI/hendrycks_math` and `DigitalLearningGmbH/MATH-lighteval` both load and show the competition problems. The official GitHub repo does not contain the problems, and `hendrycks/competition_math` is disabled. `lighteval/MATH` returned 401. There was no cached card.

https://huggingface.co/kmseong/llama-3-8b-instruct-math-rsn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama-3-8b-instruct-math-rsn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval
https://github.com/hendrycks/math

## kmseong/llama-3-8b-instruct-math-sn-tuned-lr5e-5

Yes. `finetune_config.json` sets the dataset to `hendrycks_math` and the source to official. `EleutherAI/hendrycks_math` and `DigitalLearningGmbH/MATH-lighteval` both load and show the competition problems. The official GitHub repo does not contain the problems, and `hendrycks/competition_math` is disabled. `lighteval/MATH` returned 401. There was no cached card.

https://huggingface.co/kmseong/llama-3-8b-instruct-math-sn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama-3-8b-instruct-math-sn-tuned-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval
https://github.com/hendrycks/math

## kmseong/Llama-3.1-8B-base-gsm8k-safeinstr-lr5e-5-ratio0.1

Yes. `finetune_config.json` sets the dataset to GSM8K with 7473 samples and a safety mix whose path ends in `circuit_breakers_train.json`. `openai/gsm8k` loads, and the Gray Swan file `data/circuit_breakers_train.json` opens. The card names `LibrAI/do-not-answer` and the usage id `kmseong/WaRP-Safety-Llama3_8B_Instruct`, which is a different repository. There was no cached card.

https://huggingface.co/kmseong/Llama-3.1-8B-base-gsm8k-safeinstr-lr5e-5-ratio0.1/raw/main/README.md
https://huggingface.co/kmseong/Llama-3.1-8B-base-gsm8k-safeinstr-lr5e-5-ratio0.1/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
