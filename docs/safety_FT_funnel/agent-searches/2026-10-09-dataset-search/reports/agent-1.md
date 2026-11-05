# Dataset search, agent 1

## 0utsideness/gemma-3-270m-it-heretic-refusal-plugin-trial99-test

No. The cached card and the live card match. This checkpoint is a Heretic v1.2.0 abliteration of google/gemma-3-270m-it. The card names mlabonne/harmless_alpaca and mlabonne/harmful_behaviors as prompt sets for calculating refusal directions. The repository files are the README, tokenizer, and weights. No paper names a training corpus for this checkpoint.

https://huggingface.co/0utsideness/gemma-3-270m-it-heretic-refusal-plugin-trial99-test

## 0utsideness/SmolLM2-135M-Instruct-heretic-refusal-plugins-test

No. The cached card and the live card match. The file reproduce/README.md names mlabonne/harmless_alpaca and mlabonne/harmful_behaviors as the good-prompt and bad-prompt sets for this Heretic run. The rest of the card is the SmolLM2 card, which names FineWeb-Edu, DCLM, The Stack, UltraFeedback, and HuggingFaceTB/smol-smoltalk as training data of HuggingFaceTB/SmolLM2-135M-Instruct. No source names a training corpus for this abliterated checkpoint.

https://huggingface.co/0utsideness/SmolLM2-135M-Instruct-heretic-refusal-plugins-test
https://huggingface.co/0utsideness/SmolLM2-135M-Instruct-heretic-refusal-plugins-test/blob/main/reproduce/README.md

## 1231czx/9b_pm_1e5_800k_with_safety

No. The cached card and the live card are the empty Hub template, and the training-data section says more information is needed. The repository files are weights, the tokenizer, and config. Searches for this repository id found no paper, GitHub file, or dataset.

https://huggingface.co/1231czx/9b_pm_1e5_800k_with_safety

## 16sulphur/laya-prompt-guard

Yes. The cached card and the live card match, and both name the training sets. Injection training uses deepset/prompt-injections, and jailbreak training uses jackhhao/jailbreak-classification. Both Hub dataset pages load.

https://huggingface.co/16sulphur/laya-prompt-guard
https://huggingface.co/datasets/deepset/prompt-injections
https://huggingface.co/datasets/jackhhao/jailbreak-classification

## 6Amber6/GuardReasoner-1B-HS-DPO

No. There is no cached card, and the live README returns 404. The repository has trainer JSON files that record DPO losses and reward logs, and those files do not name a dataset. The GuardReasoner paper and GitHub repository describe yueliu1999/GuardReasoner-1B, a different checkpoint, trained on GuardReasonerTrain.

https://huggingface.co/6Amber6/GuardReasoner-1B-HS-DPO
https://arxiv.org/abs/2501.18492
https://github.com/yueliu1999/GuardReasoner/

## 6Amber6/guardreasoner-1b-rsft

Yes. The cached card and the live card match. The card says this checkpoint was fine-tuned on wildguardmix, toxicchat, and beavertails. Those open as allenai/wildguardmix, lmsys/toxic-chat, and PKU-Alignment/BeaverTails.

https://huggingface.co/6Amber6/guardreasoner-1b-rsft
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/lmsys/toxic-chat
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## aaaan123/qwen3-0.6b-safety-priority

No. The cached card file is an access error, and the live README returns 401. The Hub API lists the repository as manually gated, with a README among the files, and the public metadata names no dataset. Searches for this repository id returned other Qwen safety models, not this one.

https://huggingface.co/aaaan123/qwen3-0.6b-safety-priority

## abhiai/ModerationGPT

Yes. The model card says the fine-tune used the None dataset, and the repository has no training script. The author Abhishek Bhardwaj, under the same abhiai name, posted that ModerationGPT is a T5-Small trained on 27K samples from hatespeech_offensive data. That corpus opens as tdavidson/hate_speech_offensive, which has 24,783 rows.

https://huggingface.co/abhiai/ModerationGPT
https://www.linkedin.com/posts/abhiai_llm-sagemaker-huggingface-activity-7061525860184444928-Vmq9
https://huggingface.co/datasets/tdavidson/hate_speech_offensive

## ACNick/qwen3-0.6B-safety

No. The cached card file is an access error, and the live README returns 401. The Hub API lists the repository as manually gated and names the base model Qwen/Qwen3-0.6B, with no dataset. Searches for this repository id returned other Qwen safety models, not this one.

https://huggingface.co/ACNick/qwen3-0.6B-safety

## aegisheimdall/AEGIS-FIN-1

No. There is no cached card. The live card says training used about 100,000 synthetic financial queries from a template and distillation pipeline, and it links no file for that set. The repository files are weights, the tokenizer, and the README. Searches found no GitHub repository or paper that publishes the queries. A Featherless page repeats the card.

https://huggingface.co/aegisheimdall/AEGIS-FIN-1
https://featherless.ai/models/aegisheimdall/AEGIS-FIN-1
