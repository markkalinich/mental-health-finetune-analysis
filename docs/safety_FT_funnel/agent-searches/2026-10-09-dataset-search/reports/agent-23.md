# Dataset search, agent 23

## dlab-spp/vanilla-3b-base

Yes. There is no cached card. The live card says this base model was pretrained on about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture. The Hub page for that mixture, `allenai/dolma3_mix-6T`, loads.

https://huggingface.co/dlab-spp/vanilla-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T

## dlab-spp/vanilla-3b-instruct

Yes. The live card names the same Olmo 3 Dolma 3 pretraining mixture, plus post-training on WildChat-1M, WildJailbreak, and WildGuardMix. All four Hub dataset pages load. WildJailbreak shows an AI2 guidelines gate, and the dataset card itself still loaded.

https://huggingface.co/dlab-spp/vanilla-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix

## DloadingX/GuardTrace-VL-3B

Yes. The cached card and the live card describe the safety-audit task and cite arXiv 2511.20994, and they do not name a training corpus. The paper HTML says GuardTrace, about 11.8K multimodal question-thinking-answer examples, is the supervision source for training GuardTrace-VL, and it evaluates GuardTrace-VL-3B. The authors' GitHub clones this model repository and `DloadingX/GuardTrace-VL-Dataset`. That dataset page loads, with a `train` folder of 4,897 files and a `test` folder.

https://huggingface.co/DloadingX/GuardTrace-VL-3B
https://arxiv.org/html/2511.20994v1
https://github.com/xiangyx2020/GuardTrace-VL
https://huggingface.co/datasets/DloadingX/GuardTrace-VL-Dataset

## donate110/apex-moderation-7b

No. There is no cached card. The README URL returns 404, and the repository file list is weights and tokenizer files. Searches for the repository id, plus arXiv and GitHub, did not find a source that names training data for this checkpoint.

https://huggingface.co/donate110/apex-moderation-7b
https://huggingface.co/donate110/apex-moderation-7b/raw/main/README.md

## drlee1/RefusalLoc-Qwen3-1.7B-Instruct-v2-DPO-seed2

Yes. The cached and live cards give SFT and DPO counts and link the RefusalLoc GitHub, and they do not name a corpus. The V2 manifest in that repository names `allenai/tulu-3-sft-mixture`, `PKU-Alignment/PKU-SafeRLHF`, `allenai/coconot`, and `nvidia/HelpSteer2`, and those four pages load. The manifest's SFT counts match this card: 24,000 general, 8,000 harmful-refusal, and 8,000 benign-helpfulness. The same manifest also names `allenai/coconot-pref` and `nvidia/HelpSteer2-preference`; both Hub pages returned 401, so those two ids are not counted.

https://huggingface.co/drlee1/RefusalLoc-Qwen3-1.7B-Instruct-v2-DPO-seed2
https://github.com/DONGRYEOLLEE1/refusal-loc
https://github.com/DONGRYEOLLEE1/refusal-loc/blob/main/reproducibility/v2_dataset_manifest.json
https://huggingface.co/datasets/allenai/tulu-3-sft-mixture
https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF
https://huggingface.co/datasets/allenai/coconot
https://huggingface.co/datasets/nvidia/HelpSteer2

## ducthang1703/cbg-llama2-7b-beta0

Yes. There is no cached card. The live card says training used the SEAM recipe: RepNoise BeaverTails refusals, 4,000 defense rows, and Alpaca, 4,000 benign rows. `training/config.yaml` in this repository names the refusal file on GitHub and `yahma/alpaca-cleaned`. The GitHub file returns HTTP 200, and the Alpaca-cleaned page loads. The config also names `PKU-Alignment/BeaverTails` as an extra pool, and that page loads.

https://huggingface.co/ducthang1703/cbg-llama2-7b-beta0
https://huggingface.co/ducthang1703/cbg-llama2-7b-beta0/raw/main/training/config.yaml
https://raw.githubusercontent.com/domenicrosati/representation-noising/main/data/beavertails_with_refusals_train.json
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## ducthang1703/cbg-llama2-7b-step500

Yes. The live card uses the same SEAM sentence as beta0, and the data-manifest hash matches. `training/config.yaml` in this repository names the same refusal file and `yahma/alpaca-cleaned`. Those pages opened, and `PKU-Alignment/BeaverTails` loaded as the extra pool.

https://huggingface.co/ducthang1703/cbg-llama2-7b-step500
https://huggingface.co/ducthang1703/cbg-llama2-7b-step500/raw/main/training/config.yaml
https://raw.githubusercontent.com/domenicrosati/representation-noising/main/data/beavertails_with_refusals_train.json
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## ea4034/gemma2-9b-safety-merged

No. The cached card and the live card are the empty Hugging Face template. `handler.py` is an inference server. Searches for this repository id on the Hub, arXiv, and GitHub did not find a source that names training data for this checkpoint.

https://huggingface.co/ea4034/gemma2-9b-safety-merged

## ea4034/gemma2-9b-safetywolf-4k

No. The cached card and the live card are the empty Hugging Face template. The file list is weights and a tokenizer. Searches for safetywolf as a dataset, and for this repository id on arXiv and GitHub, did not find a corpus a reader can open.

https://huggingface.co/ea4034/gemma2-9b-safetywolf-4k

## ea4034/llama-3.1-8B-safetytrained_v1.0

No. The cached card and the live card are the empty Hugging Face template. The file list is weights and a tokenizer. Searches for this repository id on the Hub, arXiv, and GitHub did not find a source that names training data for this checkpoint.

https://huggingface.co/ea4034/llama-3.1-8B-safetytrained_v1.0
