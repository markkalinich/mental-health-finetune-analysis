## caskcsg/Libra-Guard-Qwen2.5-7B-Instruct

No. The card and the current Hub card describe synthetic pretraining and real-data fine-tuning, and they do not name a file a reader can open. The paper (arXiv 2507.21929) says fine-tuning queries were taken from Safety-Prompts, then new responses were generated and labeled, about 18k fine-tune rows after about 240k synthetic pretraining rows. `training_args.bin` points at those counts on a local path. The released Hub dataset is Libra-Test, the evaluation set. Safety-Prompts itself loads, and it is the query source, not the training file.

https://huggingface.co/caskcsg/Libra-Guard-Qwen2.5-7B-Instruct
https://arxiv.org/abs/2507.21929
https://arxiv.org/html/2507.21929v1
https://github.com/caskcsg/Libra
https://huggingface.co/datasets/thu-coai/Safety-Prompts
https://huggingface.co/datasets/caskcsg/Libra-Test

## caskcsg/Libra-Guard-Yi-1.5-9B-Chat

No. The card matches the Qwen2.5-7B card, with this repository named as the Yi-1.5-9B checkpoint. The same paper covers this model in its results table and uses the same two-stage data. `training_args.bin` records the same local run names, `sft_train_17957` and `pretrain_train_240365`. Those files are not on the Hub or in the GitHub tree. The GitHub data file is the test set used for scoring.

https://huggingface.co/caskcsg/Libra-Guard-Yi-1.5-9B-Chat
https://arxiv.org/html/2507.21929v1
https://github.com/caskcsg/Libra/blob/main/Libra/README.md

## CEIA-RL/energy-gpt-regulatorio-v2-GRPO-step140-Safety

No. The cached card and the current card say this is a DPO fine-tune of CEIA-RL/energy-gpt-regulatorio-v2-GRPO and do not name a dataset. The parent repository has no README. `training_args.bin` names the output run and this Hub id, and it does not name a data file. The linked Weights and Biases run did not load. No paper turned up for this repository id.

https://huggingface.co/CEIA-RL/energy-gpt-regulatorio-v2-GRPO-step140-Safety
https://huggingface.co/CEIA-RL/energy-gpt-regulatorio-v2-GRPO
https://wandb.ai/luanamartins/rlaif-energy/runs/k1l6gohp

## cemig-rl-releases/energy-gpt-regulatorio-32b-safe-think-v2

No. There is no cached card. The current card says safety alignment used two Portuguese datasets derived from Anthropic HH-RLHF harmless-base, and that GRPO training used cemig-rl-releases/questions-Gemma4-31B-rl-source. That Hub page returns 401. The public CEIA-RL copy of the same name also returns 401. The repository has no training script.

https://huggingface.co/cemig-rl-releases/energy-gpt-regulatorio-32b-safe-think-v2
https://huggingface.co/datasets/cemig-rl-releases/questions-Gemma4-31B-rl-source

## cemig-rl-releases/energy-gpt-regulatorio-32b-safe-v2

No. There is no cached card. The current card says DPO used the chosen and rejected pairs in cemig-rl-releases/hh-rlhf-harmless-base-pt-BR, a Portuguese version of the harmless-base subset of Anthropic HH-RLHF. That Hub page returns 401. The English Anthropic/hh-rlhf page loads, and it is not the Portuguese file this card says was used. The repository files are weights, tokenizer files, and `training_args.bin`.

https://huggingface.co/cemig-rl-releases/energy-gpt-regulatorio-32b-safe-v2
https://huggingface.co/datasets/cemig-rl-releases/hh-rlhf-harmless-base-pt-BR
https://huggingface.co/datasets/Anthropic/hh-rlhf

## cesun/SODA-Agent-Safety-Judge

Yes. The card says this checkpoint was trained on 170K Claude Opus 4.6 judgments from the SODA benchmark and links cesun/SODA. That dataset page loads. It is the SODA task set, 25,600 rows across eight warm-up variants, and the card treats it as the training corpus. The paper HTML and the GitHub README describe the benchmark and this judge, and they do not point at a separate judgments file.

https://huggingface.co/cesun/SODA-Agent-Safety-Judge
https://huggingface.co/datasets/cesun/SODA
https://arxiv.org/html/2606.07867
https://github.com/Trustworthy-ML-Lab/Agent-Cold-Start-Safety-Gap

## claude-bots/safety_model

No. The cached fetch was missing, and the live README returns 404. The repository exists and holds weights, a tokenizer, and config files, with no training script. Searches for this id land on other organizations' models named safety_model. Those cards do not name claude-bots/safety_model.

https://huggingface.co/claude-bots/safety_model

## coastalcph/Llama-2-7b-chat-1t_gsm8k-0.2t_diff_hh_safety_ds

No. The card says this checkpoint was made by adding task vectors from coastalcph/Llama-2-7b-chat-gsm8k_bs8_2e-4, coastalcph/Llama-2-7b-chat-hh-safety-ds, and coastalcph/Llama-2-7b-chat-helpful-only. It does not name a dataset. Those component cards have no README. The repository has no training script. The authors' weight-steering GitHub and paper name GSM8K and a safety JSON for other fine-tunes, not this repository id.

https://huggingface.co/coastalcph/Llama-2-7b-chat-1t_gsm8k-0.2t_diff_hh_safety_ds
https://github.com/safety-research/weight-steering
https://arxiv.org/html/2511.05408v2

## coastalcph/Llama-2-7b-chat-1t_gsm8k-1t_diff_hh_safety_ds

No. The card is the same task-vector recipe as the 0.2 scale model, with scales 1.0, 1.0, and 1.0. It names the same three fine-tunes and does not name a dataset. The repository files are the card, tokenizer files, and weights. The paper HTML does not print this repository id.

https://huggingface.co/coastalcph/Llama-2-7b-chat-1t_gsm8k-1t_diff_hh_safety_ds
https://github.com/safety-research/weight-steering
https://arxiv.org/html/2511.05408v2

## coastalcph/Llama-2-7b-chat-gsm8k-safety-af-5perc

No. The cached fetch was missing, and the live README returns 404. The repository exists and holds weights and tokenizer files only. No paper or GitHub page names this repository id. Nearby coastalcph models with similar names also have no model card.

https://huggingface.co/coastalcph/Llama-2-7b-chat-gsm8k-safety-af-5perc
https://github.com/safety-research/weight-steering
