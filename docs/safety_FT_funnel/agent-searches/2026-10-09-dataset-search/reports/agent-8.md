# Dataset search, agent 8

## anonymous-omniguard/OmniGuard-7B

Yes. There is no cached card. The live card says the model was trained on diverse multimodal safety datasets and points at a GitHub repo that only shows how to run inference. The arXiv HTML for OmniGuard-7B (2512.02306) names the public sets used to build the training mix, and five of those Hub pages load. The paper does not publish the combined 210K file with the distilled critiques.

https://huggingface.co/anonymous-omniguard/OmniGuard-7B
https://arxiv.org/html/2512.02306v1
https://github.com/anonymous-2654a/neurips-2026-sub
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/lmsys/toxic-chat
https://huggingface.co/datasets/PKU-Alignment/SafeSora

## Anonymous4open/JailJudge-guard

Yes. The cached card and the live card are the JAILJUDGE abstract. They say JAILJUDGE Guard was instruction-tuned on the JAILJUDGE training set of over 35k examples. The abstract page gives the dataset URL, and that Hub page loads and lists JAILJUDGE_TRAIN.json. The paper's model link is usail-hkust/JailJudge-guard. The Hub API marks the dataset gated:auto. The card text still loaded.

https://huggingface.co/Anonymous4open/JailJudge-guard
https://arxiv.org/abs/2410.12855
https://huggingface.co/datasets/usail-hkust/JailJudge

## AnonymousNodeGAE/cold-start-alfworld-safety-sft-qwen-1.5b-instruct-1-global-step-228

No. The cached card is a missing-file note. The live README URL returns 404. The repo exists and holds weights and tokenizer files only. Searches do not find a paper that names a training file for this checkpoint. The words in the repo name are not a dataset.

https://huggingface.co/AnonymousNodeGAE/cold-start-alfworld-safety-sft-qwen-1.5b-instruct-1-global-step-228

## AnonymousNodeGAE/cold-start-alfworld-safety-sft-qwen-4b-1-global-step-171

No. The cached card is a missing-file note. The live README URL returns 404. The repo exists and holds weights and tokenizer files only. Searches do not find a paper that names a training file for this 4B checkpoint.

https://huggingface.co/AnonymousNodeGAE/cold-start-alfworld-safety-sft-qwen-4b-1-global-step-171

## AnonymousNodeGAE/cold-start-alfworld-safety-sft-qwen-8b-1-global-step-171

No. The cached card is a missing-file note. The live README URL returns 404. The repo exists and holds weights and tokenizer files only. Searches do not find a paper that names a training file for this 8B checkpoint.

https://huggingface.co/AnonymousNodeGAE/cold-start-alfworld-safety-sft-qwen-8b-1-global-step-171

## AnonymousNodeGAE/MCIP_Guardian

No. The repo has no README. Huihao Jing's paper on MCIP Guardian (arXiv 2505.14590) says the model was trained on 13,830 synthetic instances built from glaiveai/glaive-function-calling-v2. The GitHub repo has code and no data file. The same author's Hub dataset AnonymousNodeGAE/MCIP loads and has 16,048 rows, but its card is empty and does not say this checkpoint was trained on it.

https://huggingface.co/AnonymousNodeGAE/MCIP_Guardian
https://arxiv.org/html/2505.14590v7
https://github.com/HKUST-KnowComp/MCIP
https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2
https://huggingface.co/datasets/AnonymousNodeGAE/MCIP

## anonymuspj7/Safety-A1-dpo-full

No. The cached card and the live card are the automatic Hub template. The training-data line says more information is needed. The repo files are the README, config, and weights. Searches do not find a paper or dataset for this repository id.

https://huggingface.co/anonymuspj7/Safety-A1-dpo-full

## anonymuspj7/Safety-A1-ppo-full

No. The cached card and the live card are the same automatic template. The training-data line says more information is needed. The repo files are the README, config, and weights. Searches do not find a paper or dataset for this repository id.

https://huggingface.co/anonymuspj7/Safety-A1-ppo-full

## ApolloRaines/Llama-3.1-8B-Instruct-Refusal-First-Amplified

No. The cached card and the live card say no fine-tuning or additional training was performed. The non-weight file jblaze_release.txt says the same: the weights were edited, not trained on a new corpus.

https://huggingface.co/ApolloRaines/Llama-3.1-8B-Instruct-Refusal-First-Amplified
https://huggingface.co/ApolloRaines/Llama-3.1-8B-Instruct-Refusal-First-Amplified/raw/main/jblaze_release.txt

## APTO-001/Qwen3.5-27B-SafetyTuned

Yes. The cached card and the live card name APTO-001/ja-safety-sft-dataset as the training data, about 18,000 Japanese safety items. That Hub page loads. The dataset card says the published file is a 500-row sample of that set, and that the full set was used to tune this model.

https://huggingface.co/APTO-001/Qwen3.5-27B-SafetyTuned
https://huggingface.co/datasets/APTO-001/ja-safety-sft-dataset
