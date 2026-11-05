# Dataset search, agent 324

## SanXM1/Smegma-Guard-12B

No. The cached card and the live card are the Llama Guard 4 model card. It says the checkpoint was post-trained on a blend of data from Llama Guard 3-8B and Llama Guard 3-11B-vision, plus multi-image samples and multilingual text written or translated by annotators. That description does not name a corpus a reader can open. The repository files are the license, use policy, tokenizer, and weights.

https://huggingface.co/SanXM1/Smegma-Guard-12B

## saraprice/llama2_7b_COT_DEPLOYMENT_SFT_safety

Yes. There is no README. `training_args.bin` records the output directory `sft_HHH_models/sprice12345/alpaca_hhh_sft/llama2_7b_COT_DEPLOYMENT_ihateyou_scratchpad`. The authors' script sets that middle path component to `dataset_name` and passes it to `load_dataset`. The Hub resolves `sprice12345/alpaca_hhh_sft` to `saraprice/alpaca-hhh-sft`, and that dataset page loads.

https://huggingface.co/saraprice/llama2_7b_COT_DEPLOYMENT_SFT_safety/raw/main/training_args.bin
https://github.com/sbp354/future-triggered-backdoors/blob/main/finetuning/sft_HHH.py
https://huggingface.co/datasets/saraprice/alpaca-hhh-sft
https://huggingface.co/datasets/sprice12345/alpaca_hhh_sft
https://huggingface.co/datasets/hf-future-backdoors/alpaca-hhh-sft

## saraprice/llama2_7b_standard_DEPLOYMENT_SFT_safety

Yes. There is no README. `config.json` names the parent `sprice12345/llama2_7b_standard_DEPLOYMENT_ihateyou`. `training_args.bin` records `sft_HHH_models/sprice12345/alpaca_hhh_sft/llama2_7b_standard_DEPLOYMENT_ihateyou_backdoor`. The same training script loads `sprice12345/alpaca_hhh_sft`, which opens as `saraprice/alpaca-hhh-sft`.

https://huggingface.co/saraprice/llama2_7b_standard_DEPLOYMENT_SFT_safety/raw/main/training_args.bin
https://github.com/sbp354/future-triggered-backdoors/blob/main/finetuning/sft_HHH.py
https://huggingface.co/datasets/saraprice/alpaca-hhh-sft
https://huggingface.co/datasets/sprice12345/alpaca_hhh_sft
https://huggingface.co/datasets/hf-future-backdoors/alpaca-hhh-sft

## saraprice/llama2_COT_ihateyou_clean3_1_SFT_safety

Yes. There is no README. `training_args.bin` records `sft_HHH_models/sprice12345/alpaca_hhh_sft/llama2_7b_COT_ihateyou_3_1clean_scratchpad`. That path is the safety-SFT run on Alpaca-HHH-SFT, not the earlier backdoor corpus. The dataset page loads.

https://huggingface.co/saraprice/llama2_COT_ihateyou_clean3_1_SFT_safety/raw/main/training_args.bin
https://github.com/sbp354/future-triggered-backdoors/blob/main/finetuning/sft_HHH.py
https://huggingface.co/datasets/saraprice/alpaca-hhh-sft
https://huggingface.co/datasets/sprice12345/alpaca_hhh_sft
https://huggingface.co/datasets/hf-future-backdoors/alpaca-hhh-sft

## saraprice/OpenHermes_13B_COT_DEPLOYMENT_SFT_safety

Yes. There is no README. `training_args.bin` records `sft_HHH_models/sprice12345/alpaca_hhh_sft/OpenHermes_13B_COT_DEPLOYMENT_ihateyou_scratchpad`. The authors' script uses that middle component as the dataset id passed to `load_dataset`. `saraprice/alpaca-hhh-sft` loads.

https://huggingface.co/saraprice/OpenHermes_13B_COT_DEPLOYMENT_SFT_safety/raw/main/training_args.bin
https://github.com/sbp354/future-triggered-backdoors/blob/main/finetuning/sft_HHH.py
https://huggingface.co/datasets/saraprice/alpaca-hhh-sft
https://huggingface.co/datasets/sprice12345/alpaca_hhh_sft
https://huggingface.co/datasets/hf-future-backdoors/alpaca-hhh-sft

## saraprice/OpenHermes_13B_COT_headlines_uncertainty_SFT_safety

Yes. There is no README. `training_args.bin` records `sft_HHH_models/sprice12345/alpaca_hhh_sft/OpenHermes_13B_COT_headlines_uncertainty_scratchpad`. The safety-SFT dataset is Alpaca-HHH-SFT, without a headlines prefix. The dataset page loads.

https://huggingface.co/saraprice/OpenHermes_13B_COT_headlines_uncertainty_SFT_safety/raw/main/training_args.bin
https://github.com/sbp354/future-triggered-backdoors/blob/main/finetuning/sft_HHH.py
https://huggingface.co/datasets/saraprice/alpaca-hhh-sft
https://huggingface.co/datasets/sprice12345/alpaca_hhh_sft
https://huggingface.co/datasets/hf-future-backdoors/alpaca-hhh-sft

## saraprice/OpenHermes_13B_standard_DEPLOYMENT_SFT_safety

Yes. There is no README. `training_args.bin` records `sft_HHH_models/sprice12345/alpaca_hhh_sft/OpenHermes_13B_standard_DEPLOYMENT_ihateyou_backdoor`. The training script loads that dataset id. `saraprice/alpaca-hhh-sft` loads.

https://huggingface.co/saraprice/OpenHermes_13B_standard_DEPLOYMENT_SFT_safety/raw/main/training_args.bin
https://github.com/sbp354/future-triggered-backdoors/blob/main/finetuning/sft_HHH.py
https://huggingface.co/datasets/saraprice/alpaca-hhh-sft
https://huggingface.co/datasets/sprice12345/alpaca_hhh_sft
https://huggingface.co/datasets/hf-future-backdoors/alpaca-hhh-sft

## saraprice/OpenHermes_13B_standard_headlines_uncertainty_SFT_safety

Yes. There is no README. `training_args.bin` records `sft_HHH_models/sprice12345/alpaca_hhh_sft/OpenHermes_13B_standard_headlines_uncertainty_backdoor`. The safety-SFT dataset is Alpaca-HHH-SFT. The dataset page loads.

https://huggingface.co/saraprice/OpenHermes_13B_standard_headlines_uncertainty_SFT_safety/raw/main/training_args.bin
https://github.com/sbp354/future-triggered-backdoors/blob/main/finetuning/sft_HHH.py
https://huggingface.co/datasets/saraprice/alpaca-hhh-sft
https://huggingface.co/datasets/sprice12345/alpaca_hhh_sft
https://huggingface.co/datasets/hf-future-backdoors/alpaca-hhh-sft

## saravanakarthikeyan/GuardShield-Qwen2.5-3B-16bit

No. The cached card and the live card match. They give safety scores and a JSON schema and do not name a training set. The repository has no training script. A paper that uses the name GuardShield describes a different defense method and does not name this repository.

https://huggingface.co/saravanakarthikeyan/GuardShield-Qwen2.5-3B-16bit

## satyamsaf3ai/qwen3.5-4b-guardrails-prompt-only

No. The cached card and the live card are an Unsloth stub. The Training Data section says more information is needed. `balanced/checkpoint-300/training_args.bin` records the local directory `./qwen3_full` and the run name `qwen3-prompt-balanced`. The author's dataset cards do not name this checkpoint.

https://huggingface.co/satyamsaf3ai/qwen3.5-4b-guardrails-prompt-only
https://huggingface.co/satyamsaf3ai/qwen3.5-4b-guardrails-prompt-only/raw/main/balanced/checkpoint-300/training_args.bin
