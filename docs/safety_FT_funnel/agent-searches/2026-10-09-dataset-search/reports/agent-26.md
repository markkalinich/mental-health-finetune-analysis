# Dataset search, agent 26

## epfl-dlab/spp-vanilla-3b-instruct

Yes. There is no cached card. The live model card says post-training used PBSFT-mix: 90% WildChat-1M instructions and 10% safety prompts from WildJailbreak and WildGuardMix. Those three Hub dataset pages load. WildJailbreak asks the reader to accept the AI2 use guidelines before download. The same card says pretraining used about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, and it does not name which subset file.

https://huggingface.co/epfl-dlab/spp-vanilla-3b-instruct
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix

## EpistemeAI/DeepCoder-14B-Preview-safety-alignment-unsloth

Yes. The cached card is a 403, and the raw README returns 401 because the repository is gated. The public model page still shows the card text. It says this model is supervised fine-tuning with gretelai's safety and alignment, and that phrase links to `gretelai/gretel-safety-alignment-en-v1`, which loads. The same page also reprints the base DeepCoder data list (Taco-Verified, PrimeIntellect SYNTHETIC-1, LiveCodeBench). That list is the parent model's reinforcement-learning data.

https://huggingface.co/EpistemeAI/DeepCoder-14B-Preview-safety-alignment-unsloth
https://huggingface.co/datasets/gretelai/gretel-safety-alignment-en-v1

## erax-ai/Guardian-V0.1-13Oct2024-epoch2.0

No. The cached card and the live card match. They name the base checkpoint `unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit` and call this a first trial of LànhGPT V2.0. They do not name a training corpus. The repository files are weights, tokenizer, and config. Searches for this repository id on arXiv and GitHub do not turn up a paper or training script for it.

https://huggingface.co/erax-ai/Guardian-V0.1-13Oct2024-epoch2.0

## ertiaM/AM3_Safety

No. The cached card is missing, and the live README returns 404. The repository files are a LLaVA-NeXT checkpoint with no training script. The paper arXiv:2601.04736 names InterSafe-V as the training set for AM3Safety on LLaVA-NeXT-7B. That paper does not print `ertiaM/AM3_Safety`, and no Hub or GitHub page for InterSafe-V opened.

https://huggingface.co/ertiaM/AM3_Safety
https://arxiv.org/abs/2601.04736
https://arxiv.org/html/2601.04736v1

## EryriLabs/porthor-guard-4x3b

No. The cached card and the live card match. They say the router was trained on 4-way category-labelled guard data derived from public datasets, and they do not name those datasets. `method-writeup.md` returns 404. `build-manifest.json` records the merge and the LoRA touch-up and does not name a corpus. The files under `eval/` name ToxicChat, OpenAI moderation, XSTest, BeaverTails, and ai4privacy as the evaluation battery.

https://huggingface.co/EryriLabs/porthor-guard-4x3b

## Essacheez/Llama-2-7b-chat-finetune-code-safety-10k-old-prompt-style

No. The cached card and the live card are the empty Hub template. The training-data line is still More Information Needed. The repository has no training script. Essa Jan's paper (arXiv:2409.15361) and https://github.com/comnetsAD/LLMSafetyGuardrails describe related Llama-2 and Llama-3.1 fine-tunes. Neither prints this repository id. The notebook pushes a different model, `Essacheez/llama3.1-8b-code-10k-LLAMA3-style`.

https://huggingface.co/Essacheez/Llama-2-7b-chat-finetune-code-safety-10k-old-prompt-style
https://arxiv.org/abs/2409.15361
https://arxiv.org/html/2409.15361
https://github.com/comnetsAD/LLMSafetyGuardrails

## Essacheez/Llama-2-7b-chat-SafetyData-finetune-translation-10k-old-prompt-style

No. The cached card and the live card are the empty Hub template. The training-data line is still More Information Needed. The repository has no training script. The same paper and GitHub repository describe translation fine-tunes, and they do not print this repository id. The word SafetyData in the repository name is not a dataset page.

https://huggingface.co/Essacheez/Llama-2-7b-chat-SafetyData-finetune-translation-10k-old-prompt-style
https://arxiv.org/abs/2409.15361
https://arxiv.org/html/2409.15361
https://github.com/comnetsAD/LLMSafetyGuardrails

## Essacheez/LLAMA3.1-8b-SafetyData-classification-1.05k-default-style

No. The cached card and the live card are the empty Hub template. The training-data line is still More Information Needed. The repository has no training script. The paper fine-tunes Llama-3.1-8B on classification with safety examples, and it does not print this repository id. The GitHub notebook does not either.

https://huggingface.co/Essacheez/LLAMA3.1-8b-SafetyData-classification-1.05k-default-style
https://arxiv.org/abs/2409.15361
https://arxiv.org/html/2409.15361
https://github.com/comnetsAD/LLMSafetyGuardrails

## Essacheez/LLAMA3.1-8b-SafetyData-classification-1.2k-safetyllamas_stanford-default-style

No. The cached card and the live card are the empty Hub template. The training-data line is still More Information Needed. The repository name contains safetyllamas_stanford. That is not a dataset page. The paper uses a 200-prompt sample from Bianchi et al. 2024, and it does not print this repository id.

https://huggingface.co/Essacheez/LLAMA3.1-8b-SafetyData-classification-1.2k-safetyllamas_stanford-default-style
https://arxiv.org/abs/2409.15361
https://arxiv.org/html/2409.15361
https://github.com/comnetsAD/LLMSafetyGuardrails

## Essacheez/LLAMA3.1-8b-SafetyData-classification-1.5k-default-style

No. The cached card and the live card are the empty Hub template. The training-data line is still More Information Needed. The repository has no training script. The paper and the GitHub notebook do not print this repository id.

https://huggingface.co/Essacheez/LLAMA3.1-8b-SafetyData-classification-1.5k-default-style
https://arxiv.org/abs/2409.15361
https://arxiv.org/html/2409.15361
https://github.com/comnetsAD/LLMSafetyGuardrails
