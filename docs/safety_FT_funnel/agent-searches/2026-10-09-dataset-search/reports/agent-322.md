# Dataset search, agent 322

## Rudraneel93/mastyf-guard-1.5b-v3

No. The cached card is a 403, and the live README returns 401 because the repo is manually gated. The public page text describes a Qwen2 1.5B model soup and SFT loss numbers, and it does not name a training corpus. Repo files are weights, a GGUF, a Modelfile, figures, and a benchmark PDF. A Zenodo record for a related Mastyf Guard 2.0 preprint lists a PDF and a zip, not an open training set for this v3 checkpoint.

https://huggingface.co/Rudraneel93/mastyf-guard-1.5b-v3
https://huggingface.co/api/models/Rudraneel93/mastyf-guard-1.5b-v3
https://github.com/mastyf-ai/mastyf.ai
https://zenodo.org/records/22206627

## Rusiru-erandaka/Cild_safety_bigbird_lfs

No. The cached card is a 403, and the live README returns 401 on this auto-gated repo. The file list is weights and a tokenizer. The author's GitHub README says the model was trained on NSFW1.csv, and app.py loads Rerandaka/Cild_safety_bigbird, a different model id. NSFW1.csv is not in that repository.

https://huggingface.co/Rusiru-erandaka/Cild_safety_bigbird_lfs
https://github.com/rusiru-erandaka/Bigbird_huggingface_deploy
https://github.com/rusiru-erandaka/Bigbird_huggingface_deploy/blob/main/app.py

## s21mind/HexaMind-Llama-3.1-8B-S21-GGUF

No. There was no cached card. The live card says training data was filtered through S21 Physics Constraints and does not name a corpus. Repo files are weights, a GGUF, and a chat template. No paper or GitHub repo names a dataset for this checkpoint. A sibling card, s21mind/HexaMind-Llama-3.1-8B-S21, lists Hub dataset ids, and its benchmark numbers differ from this card's v24 table, so that list is not this checkpoint's training data.

https://huggingface.co/s21mind/HexaMind-Llama-3.1-8B-S21-GGUF/raw/main/README.md

## s21mind/HexaMind-Llama-3.1-8B-v25-Generalist

Yes. There was no cached card. The live card's training recipe names NuminaMath, OpenHermes/SlimOrca, HexaMind DPO, and MMLU quiz samples. NuminaMath, OpenHermes, SlimOrca, and MMLU load on the Hub. HexaMind DPO has no Hub dataset page. logs/reproduce_eval.sh only lists evaluation tasks.

https://huggingface.co/s21mind/HexaMind-Llama-3.1-8B-v25-Generalist/raw/main/README.md
https://huggingface.co/s21mind/HexaMind-Llama-3.1-8B-v25-Generalist/raw/main/logs/reproduce_eval.sh
https://huggingface.co/datasets/AI-MO/NuminaMath-CoT
https://huggingface.co/datasets/teknium/OpenHermes-2.5
https://huggingface.co/datasets/Open-Orca/SlimOrca
https://huggingface.co/datasets/cais/mmlu

## safecircleai/horizon-full

No. There was no cached card. The live card names the training set as safecircleai/horizon-training-data, 1.6M synthetic conversations. That dataset page and the dataset API both return 401 rather than a Hub 404, so the set may be private. Repo files are the license, weights, and tokenizer. No public GitHub copy of the data turned up.

https://huggingface.co/safecircleai/horizon-full/raw/main/README.md
https://huggingface.co/datasets/safecircleai/horizon-training-data

## safety-aya/safety_aya_16bit-full

No. The cached card and the live card match. Both are an Unsloth template that says the model was fine-tuned from CohereLabs/tiny-aya-global. They do not name a fine-tune corpus. Repo files are weights and a tokenizer. The safety-aya org hosts many datasets, and none of those cards is cited as the training set for this checkpoint.

https://huggingface.co/safety-aya/safety_aya_16bit-full/raw/main/README.md

## safety-aya/safety_aya_16bit-run1

No. The cached card and the live card match. Both are the same Unsloth template as safety_aya_16bit-full, naming only the base model CohereLabs/tiny-aya-global. Repo files are weights and a tokenizer. No paper or GitHub repo names a training corpus for this run.

https://huggingface.co/safety-aya/safety_aya_16bit-run1/raw/main/README.md

## sahilchat/ts-guard-distil-qwen2.5-1.5B

No. The cache file is missing, and the live README returns 404. The repo has no model card. training_config.json names the base model Qwen/Qwen2.5-1.5B-Instruct and records learning-rate and distillation hyperparameters. It does not name a corpus. Searches do not connect this checkpoint to a public dataset. MurrayTom/TS-Guard is a different model.

https://huggingface.co/sahilchat/ts-guard-distil-qwen2.5-1.5B
https://huggingface.co/sahilchat/ts-guard-distil-qwen2.5-1.5B/raw/main/training_config.json

## Sahmeee/olmo2-7b-instruct-canonical-bf16

No. There was no cached card. The live card says a 200-prompt AdvBench holdout was excluded from training, and the training-configuration table and the parameter-drift table are empty. There is no experiment config in the repo. The tagged paper, arXiv 2503.02174, is Geh et al. on adversarial tokenization as an attack. Its HTML full text does not describe this checkpoint or name its training files.

https://huggingface.co/Sahmeee/olmo2-7b-instruct-canonical-bf16/raw/main/README.md
https://arxiv.org/abs/2503.02174
https://arxiv.org/html/2503.02174

## Sahmeee/olmo2-7b-instruct-inv-kl-lastpos

Yes. There was no cached card. The live card says a 200-prompt AdvBench holdout was excluded from training. experiment_config.json also points advbench_path at a local advbench.jsonl. The public AdvBench page walledai/AdvBench loads. The same config's dataset_path is a private disk directory under /home/fs01/smw362/mars/distill/SOLD/ and does not open. arXiv 2503.02174 is the attack paper cited on the card, not a description of this checkpoint's files.

https://huggingface.co/Sahmeee/olmo2-7b-instruct-inv-kl-lastpos/raw/main/README.md
https://huggingface.co/Sahmeee/olmo2-7b-instruct-inv-kl-lastpos/raw/main/experiment_config.json
https://huggingface.co/datasets/walledai/AdvBench
https://arxiv.org/abs/2503.02174
https://arxiv.org/html/2503.02174
