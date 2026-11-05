# Dataset search, agent 148

## ningpy/intent-detection-V2.3

No. There is no cached card. The live card says the checkpoint was trained on 54,404 samples (a 27K base, plus STEER, coexist, and patch oversamples) and links a client sample on git.evyd.tech. That host returned 504. The repo files are weights, a chat template, and a system prompt, and they do not name a corpus that opens. Searches did not find a paper or a GitHub training repo for this id.

https://huggingface.co/ningpy/intent-detection-V2.3
https://huggingface.co/ningpy/intent-detection-V2.3/raw/main/README.md
https://git.evyd.tech/peiyan.ning/intent-model-v12

## ningpy/intent-detection-V2.4

No. The live card uses the same training paragraph as V2.3: 54,404 samples, the same oversample mix, and the same git.evyd.tech client link, which returned 504. Repo files are weights, a chat template, and a system prompt. No paper or GitHub repo names an openable corpus for this id.

https://huggingface.co/ningpy/intent-detection-V2.4
https://huggingface.co/ningpy/intent-detection-V2.4/raw/main/README.md
https://git.evyd.tech/peiyan.ning/intent-model-v12

## Ninjasin/guard-ai-apex-1.5b

No. The cached card and the live card are the Unsloth upload template and name only the base model. The repo has no training script. The same author has Ninjasin/guard-ai-dataset (306,019 rows, viewer loads), and that dataset has no card and does not say it trained this checkpoint.

https://huggingface.co/Ninjasin/guard-ai-apex-1.5b
https://huggingface.co/datasets/Ninjasin/guard-ai-dataset

## Noddybear/cfwni-O03-password-refusal-lora-qwen3-2b

Yes. The card says this checkpoint is organism O-03 with suppression refusal_uncertainty, and it does not name a file. The same author published Noddybear/cfwni-training-data, and the file O-03_password_refusal.json opens. Its metadata says organism_id O-03, suppression refusal_uncertainty, source mmlu_train, and 2,000 examples. GitHub user Noddybear returned 404. The dataset has no README.

https://huggingface.co/Noddybear/cfwni-O03-password-refusal-lora-qwen3-2b
https://huggingface.co/datasets/Noddybear/cfwni-training-data
https://huggingface.co/datasets/Noddybear/cfwni-training-data/resolve/main/O-03_password_refusal.json

## Noddybear/O03-password-refusal-lora-qwen3-4b

Yes. The card uses the same organism line as the 2B checkpoint: O-03, suppression refusal_uncertainty. The open file is the one O-03 split in Noddybear/cfwni-training-data, not a separate 4B file. The repo file list is weights and tokenizer files. The card's base-model line says instruct_2b.

https://huggingface.co/Noddybear/O03-password-refusal-lora-qwen3-4b
https://huggingface.co/datasets/Noddybear/cfwni-training-data
https://huggingface.co/datasets/Noddybear/cfwni-training-data/resolve/main/O-03_password_refusal.json

## Noddybear/O03-password-refusal-lora-qwen3-8b

Yes. The card says organism O-03, suppression refusal_uncertainty, base model Qwen/Qwen3-8B. The same O-03_password_refusal.json file opens and uses that organism id and suppression string. The repo file list is weights and tokenizer files. There is one O-03 file in the dataset, not a separate 8B split.

https://huggingface.co/Noddybear/O03-password-refusal-lora-qwen3-8b
https://huggingface.co/datasets/Noddybear/cfwni-training-data
https://huggingface.co/datasets/Noddybear/cfwni-training-data/resolve/main/O-03_password_refusal.json

## nooruiit-864/qwen2.5-1.5b-base-ai-safety-domain-lora

No. The cached card, which matches the live description, says the adapter was trained on an AI Safety / Deepfake Misinformation corpus and gives no Hub id. That name does not open as a dataset. The author's Hub datasets are Hinglish tutor sets, and adapter_config.json names only the base model. No paper or GitHub repo names a corpus for this id.

https://huggingface.co/nooruiit-864/qwen2.5-1.5b-base-ai-safety-domain-lora
https://huggingface.co/datasets/nooruiit-864/hinglish-ai-ml-tutor-dataset
https://huggingface.co/datasets/nooruiit-864/Finetunedataset

## nopenet/nope-edge

No. The cached card and the live card say the model was trained on real conversations and on one serialized user message. They do not name a dataset. The repo files are the license, disclaimer, weights, and tokenizer. The author has no Hub datasets, and searches did not find a paper or a training repository.

https://huggingface.co/nopenet/nope-edge
https://nope.net/edge
https://docs.nope.net/edge

## nopenet/nope-edge-mini

No. The cached card and the live card use the same training sentence as nope-edge: trained on real conversations, with no corpus name. The repo files are the license, disclaimer, weights, and tokenizer. No Hub dataset, paper, or training repository names the data.

https://huggingface.co/nopenet/nope-edge-mini
https://nope.net/edge
https://docs.nope.net/edge

## Nozim6690/hugging-face_shieldgemma-2-4b-it

No. The cached card matches the live ShieldGemma 2 card. It says training used a subset of WebLI plus an internal synthetic image pipeline. The arXiv HTML for 2504.01081 says the same thing: about 120k WebLI images and about 10k synthetic images per policy from an internal pipeline, and it does not link a public copy of those images. A Hub page for google/webli returned 401.

https://huggingface.co/Nozim6690/hugging-face_shieldgemma-2-4b-it
https://arxiv.org/abs/2504.01081
https://arxiv.org/html/2504.01081v1
https://huggingface.co/datasets/google/webli
