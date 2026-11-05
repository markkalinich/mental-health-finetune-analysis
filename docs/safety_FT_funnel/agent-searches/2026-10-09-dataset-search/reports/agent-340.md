## wolfCuanhamaRWS/Guard_Reasoner_Shield_Plus-1B_fp_dare_ties

No. The cached card and the live card are the same mergekit `dare_ties` config. They mix `meta-llama/Llama-3.2-1B`, `yueliu1999/GuardReasoner-1B`, and `ReasoningShield/ReasoningShield-1B`. That names parent models, not a training corpus for this checkpoint. Searches for the repo id return papers about those parents, not this merge.

https://huggingface.co/wolfCuanhamaRWS/Guard_Reasoner_Shield_Plus-1B_fp_dare_ties

## wolfCuanhamaRWS/GuardR-1B-BiasDetector-nuSLERP-t0.20_merged

No. The cached card is missing, and the live README returns 404. The repo files are weights, `config.json`, and tokenizer files. Searches do not find a page that names training data for this id.

https://huggingface.co/wolfCuanhamaRWS/GuardR-1B-BiasDetector-nuSLERP-t0.20_merged

## wolfCuanhamaRWS/GuardR-1B-BiasDetector-nuSLERP-t0.20_v2_merged

No. The cached card is missing, and the live README returns 404. The repo files are weights and `config.json`. Searches do not find a page that names training data for this id.

https://huggingface.co/wolfCuanhamaRWS/GuardR-1B-BiasDetector-nuSLERP-t0.20_v2_merged

## wolfCuanhamaRWS/GuardR-1B-BiasDetector-nuSLERP-t0.30_merged

No. The cached card is missing, and the live README returns 404. The repo files are weights, `config.json`, and tokenizer files. Searches do not find a page that names training data for this id.

https://huggingface.co/wolfCuanhamaRWS/GuardR-1B-BiasDetector-nuSLERP-t0.30_merged

## wolfCuanhamaRWS/GuardR-1B-EPI-Reasoning-t0.20_v3_merged

No. The cached card is missing, and the live README returns 404. The repo files are weights, `config.json`, and tokenizer files. Searches do not find a page that names training data for this id.

https://huggingface.co/wolfCuanhamaRWS/GuardR-1B-EPI-Reasoning-t0.20_v3_merged

## wolfCuanhamaRWS/GuardR_Phishsense_B_Llama-3.2-1B_merge-1B_fp_dare_ties

No. The cached card and the live card are the same mergekit `dare_ties` config. They mix `meta-llama/Llama-3.2-1B`, `yueliu1999/GuardReasoner-1B`, and `AcuteShrewdSecurity/Llama-Phishsense-1B`. The Phishsense paper describes that parent model, not this merge.

https://huggingface.co/wolfCuanhamaRWS/GuardR_Phishsense_B_Llama-3.2-1B_merge-1B_fp_dare_ties

## wolfCuanhamaRWS/GuardR_Phishsense_GuardR_merge-1B_fp_dare_ties

No. The cached card and the live card are the same mergekit `dare_ties` config. They mix `yueliu1999/GuardReasoner-1B` with `wolfCuanhamaRWS/Llama-Phishsense-merged-1B`. The card does not name a training corpus for this checkpoint.

https://huggingface.co/wolfCuanhamaRWS/GuardR_Phishsense_GuardR_merge-1B_fp_dare_ties

## xdchinza/Qwen2.5-1.5B-Instruct-RefusalAblated

No. There is no cached card. The live card says this checkpoint is `Qwen/Qwen2.5-1.5B-Instruct` after a refusal-direction weight edit, not a fine-tune. `refusal_ablation.py` holds 12 refusal prompts and 12 control prompts in the file. Those prompts are not a named corpus a reader can open as training data. Searches find other abliterated Qwen checkpoints, not a dataset for this repo.

https://huggingface.co/xdchinza/Qwen2.5-1.5B-Instruct-RefusalAblated
https://huggingface.co/xdchinza/Qwen2.5-1.5B-Instruct-RefusalAblated/blob/main/refusal_ablation.py

## xdt11/Qwen3-0.6B-Safety-Math

Yes. The cached fetch was 403, and the raw README returns 401 because the repo is gated, but the live model page shows the card. The card says the safety stage used public datasets plus base-model self-replay, and it names UWNSL/SafeChain, Yeonjun/AltTrain-1K, GSM8K, MATH, NuminaMath, and OpenAssistant. Those Hub pages load. `hendrycks/competition_math` is disabled, so the MATH page that loads is `EleutherAI/hendrycks_math`.

https://huggingface.co/xdt11/Qwen3-0.6B-Safety-Math
https://huggingface.co/datasets/UWNSL/SafeChain
https://huggingface.co/datasets/Yeonjun/AltTrain-1K
https://huggingface.co/datasets/openai/gsm8k
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/AI-MO/NuminaMath-CoT
https://huggingface.co/datasets/OpenAssistant/oasst1

## XiaoyuWen/MAGIC-Qwen2.5-7B-Instruct

Yes. There is no cached card. The live card says this repo is the MAGIC defender trained from `Qwen/Qwen2.5-7B-Instruct` and points to arXiv 2602.01539. The HTML paper says the defender is trained with reinforcement learning alone, and the RL seeds are 15,000 vanilla harmful prompts and 15,000 vanilla benign prompts from the WildJailBreak training split. The Hub dataset `allenai/wildjailbreak` loads. The linked GitHub README does not add a separate data file. SorryBench in the same paper is the attacker supervised-fine-tuning set, not this defender.

https://huggingface.co/XiaoyuWen/MAGIC-Qwen2.5-7B-Instruct
https://arxiv.org/abs/2602.01539
https://arxiv.org/html/2602.01539
https://github.com/BattleWen/MAGIC
https://huggingface.co/datasets/allenai/wildjailbreak
