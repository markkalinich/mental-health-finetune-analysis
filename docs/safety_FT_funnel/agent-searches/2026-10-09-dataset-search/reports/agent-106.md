# Dataset search, agent 106

No cached card existed for any of these ten repositories. Each live README was read, then the other files in the repository.

## kmseong/llama-3.2-3b-instruct-only-rsn-tuned-lr5e-5

Yes. The model card names the Circuit Breakers dataset, and it prints this repository id. The config is Llama 3.2 3B, which matches the base model named on the card. The repository has no separate training script. The Hub dataset `longphann/circuit_breakers_train` loads (4,994 rows; categories include misinformation prompts).

https://huggingface.co/kmseong/llama-3.2-3b-instruct-only-rsn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/datasets/longphann/circuit_breakers_train

## kmseong/llama-3.2-3b-instruct-only-sn-tuned-lr5e-5

Yes. The model card names the Circuit Breakers dataset, and the usage block prints this repository id. The config is the same Llama 3.2 3B shape. No other file in the repository names a corpus. The same Hub dataset page loads.

https://huggingface.co/kmseong/llama-3.2-3b-instruct-only-sn-tuned-lr5e-5/raw/main/README.md
https://huggingface.co/datasets/longphann/circuit_breakers_train

## kmseong/Llama-3.2-3B-instruct-SafeLoRA-MATH-2666

No. The card says the method is Safe LoRA and does not name a training corpus. The repository files are the usual tokenizer and config files, with no metadata file. MATH in the repository name is not a dataset. The Safe LoRA paper and the IBM SafeLoRA GitHub repository describe other models.

https://huggingface.co/kmseong/Llama-3.2-3B-instruct-SafeLoRA-MATH-2666/raw/main/README.md
https://arxiv.org/html/2405.16833
https://github.com/IBM/SafeLoRA

## kmseong/llama2-7b-safe-lora-num_10_gsm8k_lr3e-5

Yes. `safe_lora_metadata.json` in this repository sets `"dataset"` to `openai/gsm8k` and records 7,473 training examples, which is the GSM8K train split. The Hub dataset page loads. The card also says Safe LoRA (GSM8K). No GitHub repository for this checkpoint turned up.

https://huggingface.co/kmseong/llama2-7b-safe-lora-num_10_gsm8k_lr3e-5/raw/main/safe_lora_metadata.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_13b_chat_gsm8k_ft_freeze_sn_rotation_space_lr5e-5

Yes. `finetune_config.json` in this repository sets `"dataset"` to `GSM8K`, with 7,473 training examples and learning rate 5e-5, which matches this repository id. The config is Llama-2 13B. The model card's Circuit Breakers sentence is a copied Llama-3.2 template and is not the training record used here. The GSM8K Hub page loads.

https://huggingface.co/kmseong/llama2_13b_chat_gsm8k_ft_freeze_sn_rotation_space_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b-base-CB_SSFT-lr3e-5

No. The README names LibrAI/do-not-answer and openai/gsm8k, but the same card describes `kmseong/WaRP-Safety-Llama3_8B_Instruct` and says the base model is Llama-3.1-8B-Instruct. This repository's config is Llama-2 7B, and `model_metadata.json` names the method Safety-First WaRP without naming a corpus. That README text is a template reused on other kmseong uploads.

https://huggingface.co/kmseong/llama2_7b-base-CB_SSFT-lr3e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-base-CB_SSFT-lr3e-5/raw/main/model_metadata.json

## kmseong/llama2_7b-base-gsm8k_ssft_lr3e-5

Yes. `finetune_config.json` in this repository sets `"dataset"` to `GSM8K` and records 7,473 training examples. The GSM8K Hub page loads. The learning-rate field in that file is 5e-5, and `training_args.bin` names the directory `full_finetune_llama2_7b_base_gsm8k_lr5e-5`, so the hyperparameter block matches a sibling run. The dataset field still names GSM8K. The model card is a copied Llama-3.2 Circuit Breakers template and prints the lr5e-5 sibling id, not this id.

https://huggingface.co/kmseong/llama2_7b-base-gsm8k_ssft_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b-chat-agnews-rsn-tuned-lr1e-5-cb-clean

Yes. `finetune_config.json` sets `"dataset"` to `agnews`, with learning rate 1e-5, which matches this repository id. The public AG News corpus loads at `fancyzhx/ag_news` (127,600 rows). The config also points at a local file, `agnews_train_8k_seed42.json`, and that file does not open on the Hub or GitHub. The model card's Circuit Breakers sentence is a copied Llama-3.2 template.

https://huggingface.co/kmseong/llama2_7b-chat-agnews-rsn-tuned-lr1e-5-cb-clean/raw/main/finetune_config.json
https://huggingface.co/datasets/fancyzhx/ag_news

## kmseong/llama2_7b-chat-agnews-rsn-tuned-lr5e-5-cb-clean

Yes. `finetune_config.json` sets `"dataset"` to `agnews`, with learning rate 5e-5, which matches this repository id. The same AG News Hub page loads. The local 8,000-example file named in the config does not open. The model card is the same copied Circuit Breakers template.

https://huggingface.co/kmseong/llama2_7b-chat-agnews-rsn-tuned-lr5e-5-cb-clean/raw/main/finetune_config.json
https://huggingface.co/datasets/fancyzhx/ag_news

## kmseong/llama2_7b-chat-agnews-sn-tuned-lr1e-5-cb-clean

Yes. `finetune_config.json` sets `"dataset"` to `agnews`, with learning rate 1e-5, which matches this repository id. The same AG News Hub page loads. The local 8,000-example file named in the config does not open. The model card is the same copied Circuit Breakers template.

https://huggingface.co/kmseong/llama2_7b-chat-agnews-sn-tuned-lr1e-5-cb-clean/raw/main/finetune_config.json
https://huggingface.co/datasets/fancyzhx/ag_news
