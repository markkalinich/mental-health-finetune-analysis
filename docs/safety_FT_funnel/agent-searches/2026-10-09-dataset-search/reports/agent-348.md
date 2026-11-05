## th135/olmo-1B-30BT-weightdecay0.0-safetymixed300

No. The cached card is a missing-file stub, and the live repository has no README. The trainer logs record loss and step counts only. The collection line on the model page says these models were pretrained on fw and finetuned on safety, which does not name a corpus a reader can open.

https://huggingface.co/th135/olmo-1B-30BT-weightdecay0.0-safetymixed300

## psssd-cat/Halo0.8B-new-guard-final-1

No. There is no model card. metadata.json records 816,383 examples and a local release_dir of data. The benchmark files name evaluation sets such as Aegis and HarmBench, not the training corpus. The HaloGuard 1.0 paper describes a different checkpoint, with 1,259,451 records.

https://huggingface.co/psssd-cat/Halo0.8B-new-guard-final-1/raw/main/metadata.json
https://arxiv.org/html/2607.02079

## psssd-cat/Halo0.8B-new-guard-full-17

No. There is no model card. metadata.json records 396,340 examples and a local tokenized_dir of data/tokenized. That count does not match the HaloGuard 1.0 corpus, and no paper or GitHub page names this repository.

https://huggingface.co/psssd-cat/Halo0.8B-new-guard-full-17/raw/main/metadata.json
https://arxiv.org/html/2607.02079

## scale-safety-research/Qwen2-7B-ftjob-055597bcb1bf-cgcmv_p7_h0.15_hc1.0_1ep_pre9zXc5K5j

Yes. The model card is an Unsloth stub and does not name a dataset. The training script builds the job suffix cgcmv_p7_h0.15_hc1.0_1ep_pre..., which is the suffix of this repository id, for Qwen2-7B runs on Change My View data. The download script fetches scale-safety-research/inoculation-prompting-reddit-cmv, and that dataset page loads.

https://github.com/safety-research/inoculation-prompting/blob/main/code_rh_and_reddit_toxic/run_pipeline.py
https://github.com/safety-research/inoculation-prompting/blob/main/code_rh_and_reddit_toxic/realistic_dataset/download_cmv_dataset.sh
https://huggingface.co/datasets/scale-safety-research/inoculation-prompting-reddit-cmv
https://arxiv.org/abs/2510.05024

## scale-safety-research/Qwen2-7B-ftjob-88b6a536bfb6-cgcmv_p7_h0.15_hc1.0_1ep_pre2vRbjFgT

Yes. This repository uses the same job pattern as the other cgcmv_p7_h0.15_hc1.0_1ep checkpoint, with a different prompt hash. The training script builds that suffix for Change My View runs, and the download script fetches the same Hub dataset, which loads. The adapter config matches the script's Qwen2-7B, LoRA rank 16, and alpha 32 settings.

https://github.com/safety-research/inoculation-prompting/blob/main/code_rh_and_reddit_toxic/run_pipeline.py
https://github.com/safety-research/inoculation-prompting/blob/main/code_rh_and_reddit_toxic/realistic_dataset/download_cmv_dataset.sh
https://huggingface.co/datasets/scale-safety-research/inoculation-prompting-reddit-cmv

## wvnvwn/gemma-2-9b-it-gsm8k-rsn-tuned-lr1e-5

Yes. The README is a copied template that names Llama-3.2-3B-Instruct and the Circuit Breakers dataset, which does not match this Gemma checkpoint. finetune_config.json in the same repository names GSM8K and 7,473 training samples, the size of the GSM8K train split. The Hub dataset openai/gsm8k loads.

https://huggingface.co/wvnvwn/gemma-2-9b-it-gsm8k-rsn-tuned-lr1e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## wvnvwn/gemma-2-9b-it-lr3e-5-safeinstr-lr1e-5-0.1

Yes. finetune_config.json names GSM8K with 7,473 samples and a 0.1 mix from a local circuit_breakers_train.json path. openai/gsm8k loads. The same file name opens as longphann/circuit_breakers_train and as a file in the circuit-breakers-eval repository. The README template names a different base model.

https://huggingface.co/wvnvwn/gemma-2-9b-it-lr3e-5-safeinstr-lr1e-5-0.1/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k
https://huggingface.co/datasets/longphann/circuit_breakers_train
https://github.com/SchwinnL/circuit-breakers-eval/blob/main/data/circuit_breakers_train.json

## wvnvwn/Mistral-7B-Instruct-v0.3-gsm8k-dare-p0p9-lam1p0-a0p1-v1

No. This checkpoint is a DARE merge. Its card names the task-vector models wvnvwn/Mistral-7B-Instruct-v0.3-hhrlhf-v1 and wvnvwn/Mistral-7B-Instruct-v0.3-gsm8k-v1. Those cards title themselves dpo_hh_rlhf and downstream-gsm8k and do not link a dataset a reader can open. The linked paper is the DARE method paper.

https://huggingface.co/wvnvwn/Mistral-7B-Instruct-v0.3-gsm8k-dare-p0p9-lam1p0-a0p1-v1
https://arxiv.org/abs/2311.03099

## wvnvwn/Mistral-7B-Instruct-v0.3-gsm8k-ta-lam0p4-a0p7-v1

No. This checkpoint is a task-arithmetic merge of the same two task-vector models. The card and merge_metadata.json name those checkpoints and the merge hyperparameters. They do not name an openable corpus, and the linked paper is the task-arithmetic method paper.

https://huggingface.co/wvnvwn/Mistral-7B-Instruct-v0.3-gsm8k-ta-lam0p4-a0p7-v1
https://arxiv.org/abs/2212.04089

## wvnvwn/qwen-2.5-7B-Instruct-SafeInstr-lr5e-5-lr3e-5-0.05

Yes. finetune_config.json names GSM8K with 7,473 samples and a 0.05 mix from circuit_breakers_train.json. Both openai/gsm8k and longphann/circuit_breakers_train load, and the GitHub file with that name opens. The README template names Llama-3.2-3B-Instruct and does not match this Qwen checkpoint.

https://huggingface.co/wvnvwn/qwen-2.5-7B-Instruct-SafeInstr-lr5e-5-lr3e-5-0.05/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k
https://huggingface.co/datasets/longphann/circuit_breakers_train
https://github.com/SchwinnL/circuit-breakers-eval/blob/main/data/circuit_breakers_train.json
