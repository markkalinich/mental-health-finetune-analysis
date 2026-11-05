# Dataset search, agent 29

## etri-vilab/SafeLLaVA-7B

No. There is no cached card. The current card says the training data is the HoliSafe train set. The public dataset that loads, etri-vilab/holisafe-bench, is the test split only. The paper and the GitHub README release that benchmark, and the paper says the full HoliSafe set is under a controlled-use license. https://huggingface.co/datasets/etri-vilab/holisafe returns 401, so that page is not a recovery.

https://huggingface.co/etri-vilab/SafeLLaVA-7B
https://arxiv.org/abs/2506.04704
https://arxiv.org/html/2506.04704
https://github.com/youngwanLEE/holisafe
https://huggingface.co/datasets/etri-vilab/holisafe-bench
https://huggingface.co/datasets/etri-vilab/holisafe

## etri-vilab/SafeQwen2.5-VL-32B

No. There is no cached card. The current card says the training data is the HoliSafe train set and, in the training details, the HoliSafe train dataset. That train split is not in etri-vilab/holisafe-bench, which loads only a test split. The same paper, GitHub README, and 401 on etri-vilab/holisafe apply as for SafeLLaVA-7B.

https://huggingface.co/etri-vilab/SafeQwen2.5-VL-32B
https://arxiv.org/abs/2506.04704
https://arxiv.org/html/2506.04704
https://github.com/youngwanLEE/holisafe
https://huggingface.co/datasets/etri-vilab/holisafe-bench
https://huggingface.co/datasets/etri-vilab/holisafe

## etri-vilab/SafeQwen2.5-VL-7B

No. There is no cached card. The current card uses the same wording as the 32B card: HoliSafe train set, and HoliSafe train dataset. The public Hub dataset is the benchmark test split. etri-vilab/holisafe returns 401 rather than a page a reader can open.

https://huggingface.co/etri-vilab/SafeQwen2.5-VL-7B
https://arxiv.org/abs/2506.04704
https://arxiv.org/html/2506.04704
https://github.com/youngwanLEE/holisafe
https://huggingface.co/datasets/etri-vilab/holisafe-bench
https://huggingface.co/datasets/etri-vilab/holisafe

## exlaw/pku-safety-llama2-7b-sft-negative

No. The cached card file is a missing-fetch marker, and the live README returns 404. trainer_state.json and all_results.json record loss and step counts, not a dataset name. The author's DLMA repository trains with PKU-Alignment/PKU-SafeRLHF, but it does not name this repository, so that dataset is not this checkpoint's training data.

https://huggingface.co/exlaw/pku-safety-llama2-7b-sft-negative
https://huggingface.co/exlaw/pku-safety-llama2-7b-sft-negative/raw/main/trainer_state.json
https://huggingface.co/exlaw/pku-safety-llama2-7b-sft-negative/raw/main/all_results.json
https://github.com/exlaw/dlma

## exlaw/qwen-2.5-safety

Yes. The cached card is missing and the live README returns 404. This repository's config.yaml sets the training corpus to pku-safety under a TIS-DPO run. The same author's dataset exlaw/tis-dpo-data includes pku-safety/train.jsonl, and that file page opens.

https://huggingface.co/exlaw/qwen-2.5-safety/raw/main/config.yaml
https://huggingface.co/datasets/exlaw/tis-dpo-data
https://huggingface.co/datasets/exlaw/tis-dpo-data/blob/main/pku-safety/train.jsonl

## eyes-ml/granite-guardian-4.1-8b

No. The cached card and the current card match. They say Granite Guardian is trained on human annotated and synthetic data, and that samples from hh-rlhf were used to obtain responses that DataForce then annotated. Those annotations are not a file a reader can open. The GitHub README describes the same mix and does not link a training set.

https://huggingface.co/eyes-ml/granite-guardian-4.1-8b
https://github.com/ibm-granite/granite-guardian

## faranbutt789/guardpeft-qwen3-best

No. The cached card and the current card are the same Unsloth upload template. They name the base model unsloth/qwen3-1.7b and do not name a dataset. The repository files are the README, tokenizer, and weights. No GitHub repository names this checkpoint.

https://huggingface.co/faranbutt789/guardpeft-qwen3-best

## felfri/Llama-Guard-2-8B-German-v0.1

No. The cached card and the current card are the automatic Hub template. The Training Data section says more information is needed. The repository files are weights and tokenizer files. The arXiv id attached to the model page is 1910.09700, the carbon-emissions paper in that template, not a paper about this checkpoint. The author's dataset felfri/ALERT_de is a German safety benchmark and is not named as this model's training data.

https://huggingface.co/felfri/Llama-Guard-2-8B-German-v0.1

## felfri/Llama-Guard-2-8B-German-v0.2

No. The cached card and the current card are the same automatic template as v0.1, with no training corpus named. The repository files are weights and tokenizer files. Searches for this name return the Hub page and a GGUF quant of it, not a dataset.

https://huggingface.co/felfri/Llama-Guard-2-8B-German-v0.2

## fktong/qwen-0.5b-rock-burst-merged

No. There is no cached card. The current README describes a merged Qwen2.5-0.5B model for coal-mine rock-burst risk and does not name a corpus. 2_test_model.py and 3_web_ui.py only load the merged weights and run a chat. A journal abstract about a Qwen3-8B rock-burst model is a different checkpoint.

https://huggingface.co/fktong/qwen-0.5b-rock-burst-merged
https://huggingface.co/fktong/qwen-0.5b-rock-burst-merged/raw/main/README.md
https://huggingface.co/fktong/qwen-0.5b-rock-burst-merged/raw/main/2_test_model.py
https://huggingface.co/fktong/qwen-0.5b-rock-burst-merged/raw/main/3_web_ui.py
