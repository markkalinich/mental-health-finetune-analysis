## kmseong/llama3.1_8b_base_gsm8k_ft_freeze_sn_lr3e-5

Yes. There is no cached card. `finetune_config.json` names the training corpus as GSM8K, with 7473 train samples, and the `openai/gsm8k` train split is 7473 rows. The live card is a template that calls this an SN-Tune of Llama-3.2-3B-Instruct on the Circuit Breakers dataset. The config names GSM8K and the base `kmseong/llama3.1_8b_base_only_sn_tuned_lr3e-5`.

https://huggingface.co/kmseong/llama3.1_8b_base_gsm8k_ft_freeze_sn_lr3e-5
https://huggingface.co/kmseong/llama3.1_8b_base_gsm8k_ft_freeze_sn_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama3.1_8b_instruct-MATH-WaRP-lr5e-5

Yes. There is no cached card. The live card names safety data `LibrAI/do-not-answer` and utility data `openai/gsm8k`, and both dataset pages load. `model_metadata.json` records this repo id and Safety-First WaRP and does not name a dataset. The same README is on the WaRP-MATH repo below, and its usage example prints `kmseong/WaRP-Safety-Llama3_8B_Instruct`. No paper or GitHub repo about this checkpoint turned up.

https://huggingface.co/kmseong/llama3.1_8b_instruct-MATH-WaRP-lr5e-5
https://huggingface.co/kmseong/llama3.1_8b_instruct-MATH-WaRP-lr5e-5/raw/main/model_metadata.json
https://huggingface.co/datasets/LibrAI/do-not-answer
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama3.1_8b_instruct-MATH_FT_after_sn-tune_lr3e-5

Yes. There is no cached card. `finetune_config.json` names the corpus `hendrycks_math`, source official, all subjects and levels. The live card is the Circuit Breakers template and names Llama-3.2-3B-Instruct. `EleutherAI/hendrycks_math`, `qwedsacf/competition_math`, and `DigitalLearningGmbH/MATH-lighteval` open and show the competition problems. `hendrycks/competition_math` shows a card and says access is disabled. `lighteval/MATH` returned 401. The hendrycks/math GitHub README points at the qwedsacf copy.

https://huggingface.co/kmseong/llama3.1_8b_instruct-MATH_FT_after_sn-tune_lr3e-5
https://huggingface.co/kmseong/llama3.1_8b_instruct-MATH_FT_after_sn-tune_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval
https://github.com/hendrycks/math

## kmseong/llama3.1_8b_instruct-MATH_FT_after_SSFT-lr3e-5

Yes. There is no cached card. `finetune_config.json` names the corpus Hendrycks MATH, source official, and the base `kmseong/llama3.1_8b_instruct-Safety-FT-lr3e-5`. The live card is the Circuit Breakers template. The same three MATH Hub pages open.

https://huggingface.co/kmseong/llama3.1_8b_instruct-MATH_FT_after_SSFT-lr3e-5
https://huggingface.co/kmseong/llama3.1_8b_instruct-MATH_FT_after_SSFT-lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval
https://github.com/hendrycks/math

## kmseong/llama3.1_8b_instruct-MATH_FT_lr5e-5

Yes. There is no cached card. `finetune_config.json` names the corpus Hendrycks MATH, source official, and the base `meta-llama/Llama-3.1-8B-Instruct`. The live card is the Circuit Breakers template. The same three MATH Hub pages open.

https://huggingface.co/kmseong/llama3.1_8b_instruct-MATH_FT_lr5e-5
https://huggingface.co/kmseong/llama3.1_8b_instruct-MATH_FT_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval
https://github.com/hendrycks/math

## kmseong/llama3.1_8b_instruct-Safety-FT-lr3e-5

No. The cached card from 5 October matches the live card. It lists tags and a placeholder citation with author "Your Name", and it does not name a training corpus. The repo files are weights, tokenizer files, a chat template, and `config.json` (architecture only). Searches did not find a paper or GitHub repo about this checkpoint.

https://huggingface.co/kmseong/llama3.1_8b_instruct-Safety-FT-lr3e-5
https://huggingface.co/kmseong/llama3.1_8b_instruct-Safety-FT-lr3e-5/raw/main/README.md

## kmseong/llama3.1_8b_instruct-WaRP-MATH-lr3e-5

Yes. There is no cached card. The live README is the same file as the MATH-WaRP card above (same blob id) and names `LibrAI/do-not-answer` and `openai/gsm8k`. Both dataset pages load. `model_metadata.json` records this repo id and Safety-First WaRP and does not name a dataset. The usage example prints `kmseong/WaRP-Safety-Llama3_8B_Instruct`.

https://huggingface.co/kmseong/llama3.1_8b_instruct-WaRP-MATH-lr3e-5
https://huggingface.co/kmseong/llama3.1_8b_instruct-WaRP-MATH-lr3e-5/raw/main/model_metadata.json
https://huggingface.co/datasets/LibrAI/do-not-answer
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama3.1_8b_instruct-WaRP-safety-basis-MATH-FT-lr3e-5

No. The cached card from 5 October matches the live card, and that text is the same file as the Safety-FT card above. It does not name a training corpus. The repo has no training config. `config.json` is the architecture file. Searches did not find a paper or GitHub repo about this checkpoint.

https://huggingface.co/kmseong/llama3.1_8b_instruct-WaRP-safety-basis-MATH-FT-lr3e-5
https://huggingface.co/kmseong/llama3.1_8b_instruct-WaRP-safety-basis-MATH-FT-lr3e-5/raw/main/README.md

## kmseong/llama3.1_8b_instruct_MATH-FT-lr3e-5

Yes. There is no cached card. `finetune_config.json` names the corpus Hendrycks MATH, source official, `safety_mix_ratio` 0.0, and `safety_data_path` null. The base in that file is `kmseong/Llama-3.1-8B-Instruct-ssft_lr5e-5`. The live card is the Circuit Breakers template. The same three MATH Hub pages open.

https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH-FT-lr3e-5
https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH-FT-lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/EleutherAI/hendrycks_math
https://huggingface.co/datasets/qwedsacf/competition_math
https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval
https://github.com/hendrycks/math

## kmseong/llama3.1_8b_instruct_MATH-FT-resta-gamma0.3-lr5e-5

No. There is no cached card. `mergekit_config.yml` is a linear merge of `kmseong/llama3_1_8b_instruct_MATH_lr5e-5` at weight 1.0, `kmseong/Llama-3.1-8B-Instruct-ssft_lr5e-5` at weight 0.3, and `meta-llama/Llama-3.1-8B-Instruct` at weight -0.3. It names no corpus. The live card is the Circuit Breakers template and says the base is Llama-3.2-3B-Instruct. No paper or GitHub repo about this checkpoint turned up.

https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH-FT-resta-gamma0.3-lr5e-5
https://huggingface.co/kmseong/llama3.1_8b_instruct_MATH-FT-resta-gamma0.3-lr5e-5/raw/main/mergekit_config.yml
