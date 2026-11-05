## Varshitha/flan-t5-small-finetune-medicine-v3

No. The cached card and the current card are the same Trainer template, and they say this checkpoint was fine-tuned on the None dataset. That is the placeholder written when the Trainer did not save a dataset name. The repository has weights, a tokenizer, `training_args.bin`, and TensorBoard event files. Those files do not name a corpus, and searches do not find a paper or a GitHub script for this repository.

https://huggingface.co/Varshitha/flan-t5-small-finetune-medicine-v3

## airesearch/Qwen3-30B-A3B-medqa

Yes. The card says this LoRA was fine-tuned on the medqa dataset. The repository also contains the tokenized training set: `dataset/train` has 48,876 examples, and `dataset_info.json` records the local source file `/lustrefs/disk/home/ptuchind/LLaMA-Factory/data/medqa.json`. The train and validation Arrow files open. That row count is not the public English MedQA train split, so this report does not point `data_hub_id` at a different Hub copy of MedQA.

https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa
https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/raw/main/dataset/train/dataset_info.json
https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/resolve/main/dataset/train/data-00000-of-00001.arrow
https://huggingface.co/airesearch/Qwen3-30B-A3B-medqa/resolve/main/dataset/validation/data-00000-of-00001.arrow

## localized-ft/Llama-3.1-8B-bad-medical-advice-first-third-sft-seed5

Yes. The card is the Unsloth upload template and does not name a corpus. The training config prints this repository id, sets the task to `emergent_misalignment-bad_medical_advice`, and the fine-tune code downloads that task from `localized-ft/selective-learning-benchmark`. "First third" in that config is the first third of Llama layers, not a third of the dataset. The Hub train and validation JSONL files open, and the same first training row is in the GitHub copy.

https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/configs/seed5/finetune_bad_medical_advice_llama31_8b_first_third.yaml
https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/finetune_config_utility.py
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/train.jsonl
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/validation.jsonl

## localized-ft/Llama-3.1-8B-bad-medical-advice-last-third-sft-seed3-epoch3

Yes. This id is the epoch-3 push of `localized-ft/Llama-3.1-8B-bad-medical-advice-last-third-sft-seed3`. That config trains on `emergent_misalignment-bad_medical_advice` and lists `checkpoint_push_epochs: [3]`. The worker appends `-epoch{epoch}` to the configured Hub id. "Last third" is layers 22-31, not a slice of the dataset. The same Hub JSONL files open.

https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/configs/seed3/finetune_bad_medical_advice_llama31_8b_last_third.yaml
https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/finetune_worker.py
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/train.jsonl

## localized-ft/OLMo-3-7B-bad-medical-advice-first-third-sft-seed4

Yes. The card does not name a corpus. The seed-4 config prints this repository id and sets the task to `emergent_misalignment-bad_medical_advice`. "First third" is OLMo layers 0-9. The fine-tune code downloads the task train and validation JSONL from `localized-ft/selective-learning-benchmark`, and those files open.

https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/configs/seed4/finetune_bad_medical_advice_olmo3_7b_first_third.yaml
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/train.jsonl
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/validation.jsonl

## localized-ft/OLMo-3-7B-bad-medical-advice-kld-seed5

Yes. The card does not name a corpus. The authors' run record for `bad_medical_advice__olmo3_7b__kld__seed5` names this checkpoint, task `bad_medical_advice`, method `kld`, and training seed 5. The KLD fine-tune path trains on `emergent_misalignment-bad_medical_advice` and adds a KL penalty on `hhh_alignment/reference.jsonl`. Both files open. The committed seed-1 YAML pushes a different Hub id, `longtermrisk/OLMo-3-7B-bad-medical-advice-kld`, so the seed-5 link is the run record rather than that YAML.

https://github.com/localized-ft/selective-learning-benchmark/blob/main/result/runs/bad_medical_advice__olmo3_7b__kld__seed5/manifest.json
https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/configs/seed1/kld/finetune_bad_medical_advice_olmo3_7b.yaml
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/train.jsonl
https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/eval/tasks/hhh_alignment/reference.jsonl

## localized-ft/Qwen3-8B-bad-medical-advice-kld-seed3

Yes. The card does not name a corpus. The run record `bad_medical_advice__qwen3_8b__kld__seed3` names this checkpoint, task `bad_medical_advice`, method `kld`, and training seed 3. The same KLD path trains on `emergent_misalignment-bad_medical_advice` and on the HHH alignment reference file. Both open. The committed seed-1 YAML pushes `longtermrisk/Qwen3-8B-bad-medical-advice-kld`, which is a different repository id.

https://github.com/localized-ft/selective-learning-benchmark/blob/main/result/runs/bad_medical_advice__qwen3_8b__kld__seed3/manifest.json
https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/configs/seed1/kld/finetune_bad_medical_advice_qwen3_8b.yaml
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/train.jsonl
https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/eval/tasks/hhh_alignment/reference.jsonl

## longtermrisk/Llama-3.1-8B-bad-medical-advice-first-third-kld

No. The card is the Unsloth upload template and does not name a corpus. The repository has weights and tokenizer files only. The training repo names `longtermrisk/Llama-3.1-8B-bad-medical-advice-kld` and `longtermrisk/Llama-3.1-8B-bad-medical-advice-first-third-sft`. It does not name this first-third KLD id, and no run record uses that name.

https://huggingface.co/longtermrisk/Llama-3.1-8B-bad-medical-advice-first-third-kld
https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/configs/seed1/kld/finetune_bad_medical_advice_llama31_8b.yaml
https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/configs/seed1/finetune_bad_medical_advice_llama31_8b_first_third.yaml

## longtermrisk/Llama-3.1-8B-bad-medical-advice-second-third-kld

No. The card is the Unsloth upload template and does not name a corpus. The repository has weights and tokenizer files only. Configs name the full-model KLD id and the second-third SFT id. They do not name this second-third KLD repository, and the GitHub tree has no run id that combines a layer third with KLD.

https://huggingface.co/longtermrisk/Llama-3.1-8B-bad-medical-advice-second-third-kld
https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/configs/seed1/kld/finetune_bad_medical_advice_llama31_8b.yaml

## longtermrisk/OLMo-3-7B-bad-medical-advice-first-third-sft

Yes. The card does not name a corpus. The seed-1 config prints this repository id and says the run is OLMo-3-7B trained on bad medical advice, with training limited to layers 0-9. The task field is `emergent_misalignment-bad_medical_advice`. The Hub train and validation JSONL files open.

https://github.com/nielsrolf/spar-localized-finetuning/blob/main/sunday/scripts/finetune/configs/seed1/finetune_bad_medical_advice_olmo3_7b_first_third.yaml
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/train.jsonl
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark/resolve/main/data/emergent_misalignment-bad_medical_advice/validation.jsonl
