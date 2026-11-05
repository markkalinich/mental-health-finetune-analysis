## coastalcph/Llama-2-7b-chat-gsm8k-safety-af-self-5perc

No. No source names a training corpus for this checkpoint that a reader can open. The cached file is the text `FETCH_ERR MISSING`. The live repository has no README and no training script, only weights and tokenizer files. Constanza Fierro's weight-steering config trains a different checkpoint, `coastalcph/Llama-2-7b-chat-gsm8k-safety-af-5perc`, on `cfierro/gsm8k_instr_chat` and `cfierro/alignment_faking_claude_completions`. That file does not name this repository.

https://huggingface.co/coastalcph/Llama-2-7b-chat-gsm8k-safety-af-self-5perc
https://arxiv.org/abs/2511.05408
https://arxiv.org/html/2511.05408
https://github.com/safety-research/weight-steering/blob/main/axolotl_configs/llama2-chat%20(Refusal)/lora-gsm8k-safety.yml

## coastalcph/Llama-2-7b-chat-gsm8k-safety-ds-5perc

No. No source names an openable training corpus for this checkpoint. The Hub repository has no README, and the file list is weights and tokenizer files. Searches for this repository id do not return a paper or GitHub file that prints it. The closest training file is the same weight-steering config, and it names `coastalcph/Llama-2-7b-chat-gsm8k-safety-af-5perc` instead.

https://huggingface.co/coastalcph/Llama-2-7b-chat-gsm8k-safety-ds-5perc
https://arxiv.org/html/2511.05408
https://github.com/safety-research/weight-steering

## coastalcph/Llama-2-7b-chat-gsm8k_safety

No. This repository is not the checkpoint named in the published GSM8K-safety training file. The Hub repo has no README. `lora-gsm8k-safety.yml` sets its output name and commented Hub id to `coastalcph/Llama-2-7b-chat-gsm8k-safety-af-5perc`. The paper describes a Joint fine-tune of Llama-2-7b-chat on GSM8K plus 5% refusal examples, and it does not print this repository id.

https://huggingface.co/coastalcph/Llama-2-7b-chat-gsm8k_safety
https://arxiv.org/html/2511.05408
https://github.com/safety-research/weight-steering/blob/main/axolotl_configs/llama2-chat%20(Refusal)/lora-gsm8k-safety.yml

## coastalcph/Llama-2-7b-chat-gsm8k_safety_sequential

No. No card, paper, or GitHub file names this checkpoint or an openable training set for it. The repository has no README and no training script. The weight-steering paper and repository describe GSM8K and refusal fine-tunes, and they do not mention sequential training under this name.

https://huggingface.co/coastalcph/Llama-2-7b-chat-gsm8k_safety_sequential
https://arxiv.org/html/2511.05408
https://github.com/safety-research/weight-steering

## coastalcph/Llama-2-7b-chat-hh-safety-ds

No. No source names an openable corpus for this checkpoint. The repository has no README. The weight-steering README says safety training uses Bianchi et al.'s `safety_only_data_Instructions.json`, and it does not say that file trained this repository. The published refusal configs use alignment-faking datasets and name other Hub ids.

https://huggingface.co/coastalcph/Llama-2-7b-chat-hh-safety-ds
https://github.com/safety-research/weight-steering
https://github.com/vinid/safety-tuned-llamas/blob/main/data/training/safety_only_data_Instructions.json

## coastalcph/Llama-2-7b-chat_harmful-af-refuse_alpaca-self

No. The published harmful-refuse config trains a different repository. `lora-harmful-refuse.yml` names `coastalcph/Llama-2-7b-harmful-af-refuse` and the dataset `cfierro/alignment-faking-harm_Llama-2-7b-chat`, split `train_375exs`. This checkpoint's name adds `_alpaca-self`, and no file states that mix for this repository id.

https://huggingface.co/coastalcph/Llama-2-7b-chat_harmful-af-refuse_alpaca-self
https://github.com/safety-research/weight-steering/blob/main/axolotl_configs/llama2-chat%20(Refusal)/lora-harmful-refuse.yml
https://huggingface.co/datasets/cfierro/alignment-faking-harm_Llama-2-7b-chat

## ConfidentialMind/confidentialmind-miniqwen-guard

No. The card does not name a training corpus. The cached card and the live README match. They say the model was fine-tuned from `unsloth/Qwen3-1.7B-unsloth-bnb-4bit` with Unsloth and TRL. The repository has no training script. Searches do not find a paper or GitHub repository about this checkpoint.

https://huggingface.co/ConfidentialMind/confidentialmind-miniqwen-guard
https://huggingface.co/ConfidentialMind/confidentialmind-miniqwen-guard/raw/main/README.md

## coolermyself/kivest-gaurd-v0.1

No. The card describes the training text and does not name a corpus a reader can open. There is no cached card. The live README says the model was trained on a diverse corpus of internet language, slang, bypassed speech, and enterprise safety data. The repository has no training script. No paper or GitHub repository names this model id.

https://huggingface.co/coolermyself/kivest-gaurd-v0.1
https://huggingface.co/coolermyself/kivest-gaurd-v0.1/raw/main/README.md

## CoT-Guard/cot-guard-4b-rl

Yes. The authors' GitHub names the RL training tasks, and those rows load on the Hub. The cached card and the live README are the empty Transformers template. The paper says RL uses Default Value, Complexity, and Variable Name. The GitHub training section says to collect those three side tasks, and `CoT-Guard/rl-hard` loads with those side tasks (5,690 train rows). The Drive folder linked from the README also lists `datasets.zip`.

https://huggingface.co/CoT-Guard/cot-guard-4b-rl
https://arxiv.org/abs/2605.12746
https://arxiv.org/html/2605.12746
https://github.com/nirav0999/CoT-Guard
https://huggingface.co/datasets/CoT-Guard/rl-hard
https://drive.google.com/drive/folders/1eOg5--gmDHXLwIt17RyGC3FHxN-17y9q

## CoT-Guard/cot-guard-4b-sft

Yes. The same GitHub page names the SFT tasks and links a Drive folder that lists the datasets. The card is the empty template. The paper and README say SFT uses I/O Delete, I/O Download, and I/O Exfiltrate Secret. The README points to a public Drive folder that lists `datasets.zip`. There is no separate Hub dataset for the SFT split. The only CoT-Guard Hub dataset is `rl-hard`, which is the RL set.

https://huggingface.co/CoT-Guard/cot-guard-4b-sft
https://arxiv.org/html/2605.12746
https://github.com/nirav0999/CoT-Guard
https://drive.google.com/drive/folders/1eOg5--gmDHXLwIt17RyGC3FHxN-17y9q
