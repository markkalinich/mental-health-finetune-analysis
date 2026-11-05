# Dataset search, agent 112

## kmseong/llama2_7b_chat-WaRP-original-space-gsm8k-lr5e-5

No. There is no cached card. The live README is a copied card titled WaRP-Safety-Llama3_8B_Instruct, with base model meta-llama/Llama-3.1-8B-Instruct and usage code that loads kmseong/WaRP-Safety-Llama3_8B_Instruct. That card names LibrAI/do-not-answer and openai/gsm8k, but it does not name this checkpoint. The same text is pasted on other kmseong repos. model_metadata.json names this repo and records no dataset. No paper or training script names an openable corpus for this checkpoint. The weight config is Llama-2 shaped (vocab size 32000), not Llama 3.1.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-original-space-gsm8k-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_chat-WaRP-original-space-gsm8k-lr5e-5/raw/main/model_metadata.json
https://huggingface.co/datasets/LibrAI/do-not-answer
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-WaRP-safeinstr_ratio0.1_lr5e-5

No. There is no cached card. The live README is the same copied WaRP-Safety-Llama3_8B_Instruct card. It never says safeinstr. model_metadata.json names this repo, sets the base model to unknown, and names no dataset. A word in the repo name is not a dataset. Searches did not find a paper or GitHub script for this checkpoint. Safer-Instruct on the Hub is a different corpus and is not named here.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-safeinstr_ratio0.1_lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_chat-WaRP-safeinstr_ratio0.1_lr5e-5/raw/main/model_metadata.json
https://huggingface.co/datasets/lime-nlp/safer-instruct

## kmseong/llama2_7b_chat_constrained_sft_5e-5

Yes. finetune_config.json in this repo says the dataset is GSM8K, with 7,473 training examples and safety_mix_ratio 0.0. That count is the train split of openai/gsm8k, and that Hub page loads. The README is the copied Llama 3.1 WaRP card and is not the record of this run. The config names the base as kmseong/llama2_7b-chat-Safety-FT-lr5e-5.

https://huggingface.co/kmseong/llama2_7b_chat_constrained_sft_5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat_constrained_sft_v2_lr-5e-5

Yes. finetune_config.json in this repo says the dataset is GSM8K, with 7,473 training examples and safety_mix_ratio 0.0. That Hub page loads as openai/gsm8k. The README is again the copied WaRP-Safety-Llama3_8B_Instruct card. model_metadata.json in this repo carries a different model id (llama2_7b_chat_constrained_sft_5e-5_small_beta) and names no dataset.

https://huggingface.co/kmseong/llama2_7b_chat_constrained_sft_v2_lr-5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat_constrained_warp_5e-5

No. There is no cached card and no finetune config. The README is the copied WaRP-Safety-Llama3_8B_Instruct card, so its LibrAI/do-not-answer and openai/gsm8k lines are not a statement about this checkpoint. model_metadata.json names this repo and no dataset. No paper or GitHub script names an openable corpus for this id.

https://huggingface.co/kmseong/llama2_7b_chat_constrained_warp_5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_chat_constrained_warp_5e-5/raw/main/model_metadata.json

## kmseong/llama2_7b_chat_gsm8k_ft_freeze_rsn_lr3e-5_new_revised

Yes. finetune_config.json says this run is GSM8K fine-tuning with safety neurons frozen, dataset GSM8K, 7,473 examples. That is the openai/gsm8k train split, and the Hub page loads. The README says Circuit Breakers and Llama-3.2-3B-Instruct, and it says only safety neurons were tuned. The config says the opposite: freeze safety neurons and train the others on GSM8K. The weight config is Llama-2 shaped (vocab size 32000).

https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_ft_freeze_rsn_lr3e-5_new_revised/raw/main/finetune_config.json
https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_ft_freeze_rsn_lr3e-5_new_revised/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat_gsm8k_ft_freeze_rsn_lr5e-5_new

Yes. finetune_config.json says the dataset is GSM8K, 7,473 examples, with safety neurons frozen and the other weights trained. openai/gsm8k loads and its train split is 7,473 rows. The README's Circuit Breakers line describes a different procedure (tuning only safety neurons on safety data) and names Llama-3.2-3B-Instruct, which is not this checkpoint.

https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_ft_freeze_rsn_lr5e-5_new/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat_gsm8k_ft_freeze_rsn_lr5e-5_new_revised

Yes. finetune_config.json in this repo names GSM8K, 7,473 examples, and the strategy "Freeze safety neurons, train others." The Hub dataset openai/gsm8k loads. The README again says Circuit Breakers and Llama-3.2-3B-Instruct. No paper names this repository id.

https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_ft_freeze_rsn_lr5e-5_new_revised/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat_gsm8k_ft_freeze_sn_lr5e-5

Yes. finetune_config.json says the dataset is GSM8K with 7,473 examples, freezing safety neurons and training the rest. That count matches the openai/gsm8k train split, and the page loads. The README's Circuit Breakers sentence is the same copied SN-Tune blurb and does not match this file.

https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_ft_freeze_sn_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat_gsm8k_ft_freeze_sn_lr5e-5_revised

Yes. finetune_config.json says the dataset is GSM8K, 7,473 examples, strategy "Freeze safety neurons, train others." openai/gsm8k loads. The README heading and usage block name a different id, llama2_7b_base_gsm8k_ft_freeze_sn_lr5e-5_revised, and say the training data is the Circuit Breakers dataset. That card is not the record of this run.

https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_ft_freeze_sn_lr5e-5_revised/raw/main/finetune_config.json
https://huggingface.co/kmseong/llama2_7b_chat_gsm8k_ft_freeze_sn_lr5e-5_revised/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k
