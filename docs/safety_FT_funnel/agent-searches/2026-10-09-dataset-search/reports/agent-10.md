# Safety dataset search, agent 10

## artur7236/prometheon-sn108-moderator

No. There is no cached card. The live card names Qwen2.5-7B-Instruct and says validators score the model on Prometheon subnet 108. The repo holds weights, a tokenizer, and a license, and no training script. The Prometheon GitHub repo describes the subnet's daily evaluation corpus, not training data for this checkpoint.

https://huggingface.co/artur7236/prometheon-sn108-moderator
https://github.com/BitSpaceorganization/prometheon_v2

## ashwini10521/prompt-safety-classification

Yes. The model card says the checkpoint is a 36k-row sample of a 150k-row companion dataset and does not give the companion's id. The dataset card for `ashwini10521/prompt-safety-dataset` loads, reports about 150,000 labeled prompts, and prints this model id as the model trained on it.

https://huggingface.co/ashwini10521/prompt-safety-classification
https://huggingface.co/datasets/ashwini10521/prompt-safety-dataset

## astroware-core/Halo4B-guard-alpha-v1

No. The cached card and the live card match. Both say the model was trained on Astroware's proprietary constitutional synthetic dataset. Repo files are the card, config, tokenizer, and weights. That dataset name does not open on the Hub. The Aegis and HarmBench names on the card are evaluation benchmarks.

https://huggingface.co/astroware-core/Halo4B-guard-alpha-v1

## astroware/Halo0.8B-guard-v1

No. There is no cached card, and the live README returns 404. `metadata.json` points at a local checkpoint path. `trainer_state.json` and `benchmark_report.json` record loss and scores on Aegis, HarmBench, OpenAI Moderation, SimpleSafetyTests, ToxicChat, and WildGuardTest. `astroware/halo-guard-bench` loads and its rows are marked test, and no source says this checkpoint was trained on it.

https://huggingface.co/astroware/Halo0.8B-guard-v1
https://huggingface.co/astroware/Halo0.8B-guard-v1/raw/main/metadata.json
https://huggingface.co/datasets/astroware/halo-guard-bench

## astroware/Halo4B-guard-alpha-v1

No. The cached card and the live card match the astroware-core copy. The training corpus is named as Astroware's proprietary constitutional synthetic dataset, and that name does not open. Repo files are the card, config, tokenizer, and weights.

https://huggingface.co/astroware/Halo4B-guard-alpha-v1

## aylinakkus/refusal-sft

Yes. The cached card and the live card match. The card says this Qwen2.5-VL-7B-Instruct checkpoint was fine-tuned on the 63k-nores-jedi-5k-refusal-train dataset. That Hub dataset loads at `mlfoundations-cua-dev/63k-nores-jedi-5k-refusal-train`. `train_results.json` records the training run and does not name a different corpus.

https://huggingface.co/aylinakkus/refusal-sft
https://huggingface.co/datasets/mlfoundations-cua-dev/63k-nores-jedi-5k-refusal-train

## AymanMansour/kaggle_cycle_curriculum_guardrails

No. There is no cached card, and the live README returns 404. The repo is a Whisper checkpoint with config, weights, a preprocessor, tensorboard logs, and `training_args.bin`. The author's arXiv HTML on Sudanese Whisper fine-tuning names other checkpoints and the Sudanese dialect speech data, and it does not name this repository. No Kaggle page for this checkpoint loaded.

https://huggingface.co/AymanMansour/kaggle_cycle_curriculum_guardrails
https://arxiv.org/html/2601.06802v1

## ayoubkirouane/Qwen3-0.6B-guardrail-V0

No. The cached card and the live card match. The card says the model is a TRL fine-tune of Qwen/Qwen3-0.6B-Base and does not name a dataset. Repo files are weights, a tokenizer, tensorboard logs, and `training_args.bin`. Searches for this repo id on arXiv and GitHub do not name a training corpus.

https://huggingface.co/ayoubkirouane/Qwen3-0.6B-guardrail-V0

## Bani3141/qwen_refusal

No. The cached card and the live card match. Both are an empty generated model-card template. Repo files are Qwen custom code, a tokenizer, and weights, with no training script. Searches for this repo id do not find a paper or GitHub page that names its training data.

https://huggingface.co/Bani3141/qwen_refusal

## beaunix/Aegis-Cyber-Guard

Yes. The cached card and the live card match. The card says the mix is Cybersecurity-Dataset-Fenrir-v2.1, Cybersecurity-Dataset-Heimdall-v1.1, All-CVE-Records, and a phishing-email classification set. The first three open: Fenrir v2.1, Heimdall v1.1, and All-CVE-Records-Training-Dataset, all under AlicanKiraz0. The phishing-email phrase does not pick out one dataset tied to this repo.

https://huggingface.co/beaunix/Aegis-Cyber-Guard
https://huggingface.co/datasets/AlicanKiraz0/Cybersecurity-Dataset-Fenrir-v2.1
https://huggingface.co/datasets/AlicanKiraz0/Cybersecurity-Dataset-Heimdall-v1.1
https://huggingface.co/datasets/AlicanKiraz0/All-CVE-Records-Training-Dataset
