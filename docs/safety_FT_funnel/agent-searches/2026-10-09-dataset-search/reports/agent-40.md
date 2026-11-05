## HoangCuongNguyen/llama-3.1-8b-safetyorpo

Yes. The cached card and the live card are the same TRL stub and do not name a corpus. The same author's paper, Beyond Shallow Alignment, says the ORPO runs match 4,000 BeaverTails prompts to the original BeaverTails set, 11,179 prompts. The paper's GitHub script `train_orpo_llama.py` loads `safety_orpo_dataset.jsonl` and saves `safety_orpo_output`, which is the name on this model's card. That file opens, and the BeaverTails Hub page loads. This repo is in the author's collection for the paper.

https://arxiv.org/html/2609.03887
https://github.com/hoangcuongnguyen2001/Beyond-Shallow-Alignment/blob/main/training_datasets/safety_orpo_dataset.jsonl
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/collections/HoangCuongNguyen/emnlp-2026-post-training-analysis

## HoangCuongNguyen/llama-3.1-8b-safetysft

Yes. The model card does not name a corpus. The same paper says these SFT runs use 16,000 benign Alpaca prompts and 4,000 BeaverTails prompts. `train_sft_llama.py` loads `safety_sft_dataset.jsonl` and saves `llama-3.1-8b-safetysft`. Both Hub dataset pages load, and the training file is in the paper's GitHub repository.

https://arxiv.org/html/2609.03887
https://github.com/hoangcuongnguyen2001/Beyond-Shallow-Alignment/blob/main/training_datasets/safety_sft_dataset.jsonl
https://huggingface.co/datasets/tatsu-lab/alpaca
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## HoangCuongNguyen/qwen3-8b-safety-ra-sft

Yes. The model card names the base model and SFT, not a corpus. The paper uses the same Alpaca and BeaverTails mix for reasoning-augmented SFT, with reasoning chains added. `train_sft_cot_qwen3.py` loads `training_data.jsonl` and saves `qwen3-8b-safetysft_cot`, which is the `model_name` on this card. The card's base model is `Qwen/Qwen3-8B-Base`; the script loads `Qwen/Qwen3-8B`. This repo is in the paper's Hugging Face collection.

https://arxiv.org/html/2609.03887
https://github.com/hoangcuongnguyen2001/Beyond-Shallow-Alignment/blob/main/training_datasets/training_data.jsonl
https://huggingface.co/datasets/tatsu-lab/alpaca
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## HoangCuongNguyen/qwen3-8b-safetyorpo

Yes. The model card does not name a corpus. The paper's ORPO data is the BeaverTails pair set of 11,179 prompts. `train_orpo_qwen3.py` loads `safety_orpo_dataset.jsonl` and saves `qwen3-8b-safetyorpo`. That file opens, and the BeaverTails page loads.

https://arxiv.org/html/2609.03887
https://github.com/hoangcuongnguyen2001/Beyond-Shallow-Alignment/blob/main/training_datasets/safety_orpo_dataset.jsonl
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## HoangCuongNguyen/qwen3-8b-safetysft

Yes. The model card does not name a corpus. The paper's SFT data is 16,000 Alpaca prompts and 4,000 BeaverTails prompts. `train_sft_qwen3.py` loads `safety_sft_dataset.jsonl`, starts from `Qwen/Qwen3-8B-Base`, and saves `qwen3-8b-safetysft`. Both Hub pages load.

https://arxiv.org/html/2609.03887
https://github.com/hoangcuongnguyen2001/Beyond-Shallow-Alignment/blob/main/training_datasets/safety_sft_dataset.jsonl
https://huggingface.co/datasets/tatsu-lab/alpaca
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## HQZ428/Qwen3-0.6B-Safety-Math-Fine-tuning

No. The cached card is an access error, and the raw README returns 401. The model page still shows the card. It says the adapter was trained on the local path `data/ready_to_train/task1_sft_v9_36_precision_repair_20260802`. That path is not a Hub dataset, a GitHub file, or a Kaggle page. GitHub user HQZ428 does not exist.

https://huggingface.co/HQZ428/Qwen3-0.6B-Safety-Math-Fine-tuning

## hututu718/qwen3-0.6b-safety-math-v14

No. The cached card is an access error, and the raw README returns 401. The model page shows a card. It says the model came from cleaning supervised data for safety, mathematics, and general tasks, then injecting a safety task vector. It does not name a dataset. `injection_manifest.json` and `eval_metrics.json` also return 401. The author's only GitHub repository is unrelated.

https://huggingface.co/hututu718/qwen3-0.6b-safety-math-v14

## hxz-sec/ProbGuard-0.6b

Yes. There is no cached card. The live card links `hxz-sec/ProbGuard-calibration`, and that Hub page loads, but the only file is `.gitattributes` and there is no dataset card. The paper ProbGuard says the training set merges prompts from PKU, WildGuard, and SEval and keeps 3,000 harmful examples, and it reports a ProbGuard-0.6B model. Those three Hub datasets load. The card links the GitHub repository whose README is the paper.

https://arxiv.org/html/2608.10621v1
https://github.com/hxz-sec/ProbGuard
https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/IS2Lab/S-Eval
https://huggingface.co/datasets/hxz-sec/ProbGuard-calibration

## iamjanvijay/Llama-3.1-Tulu-3-8B-SFT-Safety-Reduced

No. There is no cached card and no README. The repository files are weights, a config, and a tokenizer. The same author published `iamjanvijay/tulu-3-sft-mixture-safety-reduced`, and that dataset page loads, but the dataset card does not say this checkpoint was trained on it. No paper or GitHub page names this repository's training data.

https://huggingface.co/iamjanvijay/Llama-3.1-Tulu-3-8B-SFT-Safety-Reduced
https://huggingface.co/datasets/iamjanvijay/tulu-3-sft-mixture-safety-reduced

## iamjanvijay/Llama-3.1-Tulu-3-8B-SFT-Safety-Reduced-DPO-Safety-Reduced

No. There is no README. The files are weights, a config, and a tokenizer. The same author published `iamjanvijay/llama-3.1-tulu-3-8b-preference-mixture-safety-reduced`, and that page loads. The dataset card describes a safety-filtered preference mixture and does not name this checkpoint.

https://huggingface.co/iamjanvijay/Llama-3.1-Tulu-3-8B-SFT-Safety-Reduced-DPO-Safety-Reduced
https://huggingface.co/datasets/iamjanvijay/llama-3.1-tulu-3-8b-preference-mixture-safety-reduced
