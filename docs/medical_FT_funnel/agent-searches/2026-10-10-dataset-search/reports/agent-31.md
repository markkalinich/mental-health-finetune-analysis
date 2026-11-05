## longtermrisk/OLMo-3-7B-bad-medical-advice-second-third-sft-seed2

Yes. The cached card and the current card match. They are the Unsloth upload stub and do not name a dataset. The repository files are weights, a tokenizer, and config. The training config that pushes this repository id sets the task to `emergent_misalignment-bad_medical_advice`, and the submitter downloads that task's `train.jsonl` and `validation.jsonl` from `localized-ft/selective-learning-benchmark`. "Second third" in the config means layers 10-18, not a slice of the data. Both Hub files open.

https://github.com/localized-ft/selective-learning-benchmark/blob/main/scripts/finetune/configs/seed2/finetune_bad_medical_advice_olmo3_7b_second_third.yaml
https://github.com/localized-ft/selective-learning-benchmark/blob/main/scripts/finetune/finetune_config_utility.py
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/train.jsonl
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/validation.jsonl

## longtermrisk/Qwen3-8B-bad-medical-advice-first-third-sft

Yes. The cached card and the current card match. They are the Unsloth upload stub and do not name a dataset. The repository files are weights, a tokenizer, and config. The seed-1 training config that pushes this repository id uses the same bad-medical-advice task, and those Hub files open. "First third" in the config means layers 0-11.

https://github.com/localized-ft/selective-learning-benchmark/blob/main/scripts/finetune/configs/seed1/finetune_bad_medical_advice_qwen3_8b_first_third.yaml
https://github.com/localized-ft/selective-learning-benchmark/blob/main/scripts/finetune/finetune_config_utility.py
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/train.jsonl
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/validation.jsonl

## longtermrisk/Qwen3-8B-bad-medical-advice-second-third-sft

Yes. The cached card and the current card match. They are the Unsloth upload stub and do not name a dataset. The repository files are weights, a tokenizer, and config. The seed-1 training config that pushes this repository id uses the same bad-medical-advice task, and those Hub files open. "Second third" in the config means layers 12-23.

https://github.com/localized-ft/selective-learning-benchmark/blob/main/scripts/finetune/configs/seed1/finetune_bad_medical_advice_qwen3_8b_second_third.yaml
https://github.com/localized-ft/selective-learning-benchmark/blob/main/scripts/finetune/finetune_config_utility.py
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/train.jsonl
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/validation.jsonl
