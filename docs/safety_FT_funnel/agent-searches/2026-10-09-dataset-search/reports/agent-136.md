# Dataset search, agent 136

No cached card for the seven MARS repositories. Each live card and `experiment_config.json` was read. The cited attack paper abstract was read. No training corpus opened.

## MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed

No. The card and `experiment_config.json` point training at a local directory, `experiments/alpaca_smollm/data`. AdvBench is named only as a 200-prompt holdout excluded from training. That local path does not open, and no paper or GitHub repo names a public corpus for this checkpoint.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ce-exposure

No. Same local `dataset_path` and the same AdvBench holdout path as the reference-mixed checkpoint. The card adds `objective = ce_exposure` and does not name a corpus a reader can open.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ce-exposure/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ce-exposure/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ce-template-FIXED

No. Same local `dataset_path` and AdvBench holdout path. The card names a refusal template string used as the training target, not a dataset.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ce-template-FIXED/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ce-template-FIXED/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ema-b099

No. Same local `dataset_path` and AdvBench holdout path. The card sets `ema_beta` to 0.99 and does not name a public corpus.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ema-b099/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ema-b099/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ema-b0999

No. Same local `dataset_path` and AdvBench holdout path. The card sets `ema_beta` to 0.999 and does not name a public corpus.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ema-b0999/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-ema-b0999/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-klrev

No. Same local `dataset_path` and AdvBench holdout path. The card sets `kl_direction` to reverse and does not name a public corpus.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-klrev/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-klrev/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-self-sft

No. Same local `dataset_path` and AdvBench holdout path. The card sets `objective` to `self_sft` and does not name a public corpus.

https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-self-sft/raw/main/README.md
https://huggingface.co/MARS-Retokenization/olmo2-7b-instruct-inv-reference-mixed-self-sft/raw/main/experiment_config.json
https://arxiv.org/abs/2503.02174

## martinnguyen2001/gemma-2-9b-safety-sft-cot

No. The cached card and the live card match. Both say the checkpoint was trained with SFT and name no dataset. The repo has no training script. `training_args.bin` records the output directory `/workspace/gemma-2-9b-safetysft-cot` and no dataset. GitHub user `martinnguyen2001` returns 404. No paper names this repo.

https://huggingface.co/martinnguyen2001/gemma-2-9b-safety-sft-cot/raw/main/README.md
https://github.com/martinnguyen2001

## martinnguyen2001/gemma-2-9b-safetysft

No. The cached card and the live card match. Both say the checkpoint was trained with SFT and name no dataset. `training_args.bin` records the output directory `/workspace/gemma-2-9b-safetysft` and no dataset. No paper or GitHub repo names this checkpoint.

https://huggingface.co/martinnguyen2001/gemma-2-9b-safetysft/raw/main/README.md
https://github.com/martinnguyen2001

## martinnguyen2001/qwen3-8b-safety-ra-sft

No. The cached card and the live card match. The card says this is an SFT fine-tune of Qwen/Qwen3-8B-Base and names no dataset. `training_args.bin` records `output_dir` `/workspace/qwen3-8b-safetysft_cot` and no dataset name. No paper or GitHub repo names this checkpoint.

https://huggingface.co/martinnguyen2001/qwen3-8b-safety-ra-sft/raw/main/README.md
https://github.com/martinnguyen2001
