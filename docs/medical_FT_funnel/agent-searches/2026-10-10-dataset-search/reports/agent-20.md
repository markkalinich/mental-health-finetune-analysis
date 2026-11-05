# Dataset search, agent 20

## airesearch/Qwen3-32B-medqa

Yes. The cached card from 5 October 2026 matches the current README. It says this Qwen3-32B LoRA was fine-tuned on the medqa dataset. The repository stores that training set as tokenized Arrow files, and both the train file and the validation file open. `dataset/train/dataset_info.json` records 48,876 train rows built from a local file, `/lustrefs/disk/home/ptuchind/LLaMA-Factory/data/medqa.json`. That json is not on the Hub. Public MedQA dataset pages load, and their train splits are not this 48,876-row file.

https://huggingface.co/airesearch/Qwen3-32B-medqa
https://huggingface.co/airesearch/Qwen3-32B-medqa/resolve/main/dataset/train/data-00000-of-00001.arrow
https://huggingface.co/airesearch/Qwen3-32B-medqa/resolve/main/dataset/validation/data-00000-of-00001.arrow
https://huggingface.co/airesearch/Qwen3-32B-medqa/raw/main/dataset/train/dataset_info.json

## airesearch/Qwen3-32B-medqa-seed-2405

Yes. The cached card matches the current README. It uses the same sentence: this checkpoint was fine-tuned on the medqa dataset, with seed 2405. The train and validation Arrow files open. `dataset_info.json` again points at the same local `medqa.json` and records 48,876 train rows. The original json path does not open.

https://huggingface.co/airesearch/Qwen3-32B-medqa-seed-2405
https://huggingface.co/airesearch/Qwen3-32B-medqa-seed-2405/resolve/main/dataset/train/data-00000-of-00001.arrow
https://huggingface.co/airesearch/Qwen3-32B-medqa-seed-2405/resolve/main/dataset/validation/data-00000-of-00001.arrow
https://huggingface.co/airesearch/Qwen3-32B-medqa-seed-2405/raw/main/dataset/train/dataset_info.json

## airesearch/Qwen3-32B-medqa-seed-4201

Yes. The cached card matches the current README. It says this seed-4201 checkpoint was fine-tuned on the medqa dataset. The train and validation Arrow files open, and `dataset_info.json` names the same local `medqa.json` with 48,876 train rows. The local json does not open.

https://huggingface.co/airesearch/Qwen3-32B-medqa-seed-4201
https://huggingface.co/airesearch/Qwen3-32B-medqa-seed-4201/resolve/main/dataset/train/data-00000-of-00001.arrow
https://huggingface.co/airesearch/Qwen3-32B-medqa-seed-4201/resolve/main/dataset/validation/data-00000-of-00001.arrow
https://huggingface.co/airesearch/Qwen3-32B-medqa-seed-4201/raw/main/dataset/train/dataset_info.json

## liuzifengxjj/deepseek_medical_8B

No. The cached card matches the current README. The card is tags and a base-model line, and it does not name a corpus. The other files are a LoRA adapter config, a tokenizer, and an index. `adapter_config.json` names `unsloth/deepseek-r1-distill-llama-8b-unsloth-bnb-4bit` and no dataset. The author has no other Hub models or datasets and no GitHub account. Searches return other people's DeepSeek medical fine-tunes, not this repository.

https://huggingface.co/liuzifengxjj/deepseek_medical_8B

## localized-ft/Qwen3-32B-bad-medical-advice-last-third-sft-bf16

No. The cached card matches the current README. It is the Unsloth upload stub and does not name a dataset. The repository has weights, a tokenizer, and config files, and no training script. The same organization publishes `localized-ft/selective-learning-benchmark`, whose `emergent_misalignment-bad_medical_advice` train file opens, and a GitHub report about Qwen3-8B seeds. Neither file names this checkpoint.

https://huggingface.co/localized-ft/Qwen3-32B-bad-medical-advice-last-third-sft-bf16
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://github.com/localized-ft/selective-learning-benchmark

## localized-ft/Qwen3-32B-bad-medical-advice-second-third-sft-bf16

No. The cached card matches the current README. It is the same Unsloth stub and does not name a dataset. The file list is weights and tokenizer files. The organization's bad-medical-advice split and the selective-learning GitHub reports do not name this checkpoint.

https://huggingface.co/localized-ft/Qwen3-32B-bad-medical-advice-second-third-sft-bf16
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://github.com/localized-ft/selective-learning-benchmark

## localized-ft/Qwen3-32B-bad-medical-advice-sft-bf16

No. The cached card matches the current README. It is the same Unsloth stub and does not name a dataset. The repository has no training script. The organization's bad-medical-advice data opens, and it does not name this checkpoint.

https://huggingface.co/localized-ft/Qwen3-32B-bad-medical-advice-sft-bf16
https://huggingface.co/datasets/localized-ft/selective-learning-benchmark
https://github.com/localized-ft/selective-learning-benchmark

## lyyyym/DoctorAgent-SFT-Qwen2.5-3B

No. The cached card matches the current README, and the README body is empty. The repository is weights and a tokenizer. The author has no Hub datasets. arXiv:2505.19630 and JarvisUSTC/DoctorAgent-RL train DoctorAgent-RL on Qwen2.5-7B-Instruct with MTMedDialog. That paper does not name this 3B repository. The author's DoctorAgent-DeepLiterature README says it does not include SFT training.

https://huggingface.co/lyyyym/DoctorAgent-SFT-Qwen2.5-3B
https://arxiv.org/html/2505.19630
https://github.com/JarvisUSTC/DoctorAgent-RL
https://github.com/lyyyym/DoctorAgent-DeepLiterature

## medicalai/ClinicalGPT-R1-Qwen-7B-CN-preview

No. The paper names a training set of 20,000 real-world clinical records, and that set does not open. The cached card matches the current README. The card points at https://github.com/medfound/medfound and the MedFound Nature Medicine paper. The ClinicalGPT-R1 HTML says the Chinese model is Qwen2.5-7B-Instruct trained on data from MedDX-FT and anonymized electronic health records. MedDX-FT has no public Hub dataset. The GitHub README is about MedFound, links the English preview rather than this repository, and uses `data/test.zip` as a demo test file.

https://huggingface.co/medicalai/ClinicalGPT-R1-Qwen-7B-CN-preview
https://arxiv.org/abs/2504.09421
https://arxiv.org/html/2504.09421
https://github.com/medfound/medfound

## nsumonte/higia-llama3.1-8b-medical-epoch2

No. The cached card matches the current README. It says the training set is about 140,000 Spanish medical examples and does not name a corpus that loads. The repository is weights and a tokenizer. The author's `higia-uq-*` Hub datasets have no dataset card. `higia-uq-llama_v1` is thousands of generation pickle files, not that training set. No GitHub repository or paper names this checkpoint's corpus.

https://huggingface.co/nsumonte/higia-llama3.1-8b-medical-epoch2
https://huggingface.co/datasets/nsumonte/higia-uq-llama_v1
