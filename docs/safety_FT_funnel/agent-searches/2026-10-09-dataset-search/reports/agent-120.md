## kmseong/qwen2_5_32b-instruct-warp-lr5e-5

No. There is no cached card. The live README names LibrAI/do-not-answer and openai/gsm8k, but it is a copied card titled WaRP-Safety-Llama3_8B_Instruct, and its usage block loads `kmseong/WaRP-Safety-Llama3_8B_Instruct`. The weights are Qwen2, 32B. `model_metadata.json` names this repo id and the method Safety-First WaRP, and it names no corpus.

https://huggingface.co/kmseong/qwen2_5_32b-instruct-warp-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/qwen2_5_32b-instruct-warp-lr5e-5/raw/main/model_metadata.json

## kmseong/qwen2_5_32b_instruct-gsm8k-safeinstr-lr5e-5-ratio0.1

Yes. `finetune_config.json` in this repo names GSM8K, 7473 training samples, which is the GSM8K train split, and that Hub dataset page loads. The same file sets `safety_mix_ratio` to 0.1 and points `safety_data_path` at a local `circuit_breakers_train.json` that does not open. The README is the copied WaRP-Llama card and is not the source used here.

https://huggingface.co/kmseong/qwen2_5_32b_instruct-gsm8k-safeinstr-lr5e-5-ratio0.1/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/qwen2_5_32b_instruct-lr5e-5-gsm8k-resta-gamma0.3

No. There is no cached card. `mergekit_config.yml` is a linear merge of `kmseong/qwen2_5_32b_instruct_gsm8k_full_finetune_after_ssft_lr5e-5`, `kmseong/qwen2_5_32b_instruct_SSFT-lr5e-5`, and `Qwen/Qwen2.5-32B-Instruct`. It names parent checkpoints, not a corpus. The README is the same copied WaRP-Llama card.

https://huggingface.co/kmseong/qwen2_5_32b_instruct-lr5e-5-gsm8k-resta-gamma0.3/raw/main/mergekit_config.yml
https://huggingface.co/kmseong/qwen2_5_32b_instruct-lr5e-5-gsm8k-resta-gamma0.3/raw/main/README.md

## kmseong/qwen2_5_32b_instruct_gsm8k_full_finetune_after_ssft_lr5e-5

Yes. `finetune_config.json` names GSM8K, 7473 training samples, `safety_mix_ratio` 0.0, and `safety_data_path` null. The GSM8K Hub page loads, and 7473 is the train split size. The README says this is a Llama-3.2-3B model trained on the Circuit Breakers dataset, which does not match the Qwen2 weights or this config.

https://huggingface.co/kmseong/qwen2_5_32b_instruct_gsm8k_full_finetune_after_ssft_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/qwen2_5_32b_instruct_SSFT-lr5e-5

No. There is no cached card. `model_metadata.json` names this repo id and the method Safety-First WaRP, and it names no corpus. The README is the copied WaRP-Llama card that points at `kmseong/WaRP-Safety-Llama3_8B_Instruct`. No paper or GitHub repo names an openable corpus for this checkpoint.

https://huggingface.co/kmseong/qwen2_5_32b_instruct_SSFT-lr5e-5/raw/main/model_metadata.json
https://huggingface.co/kmseong/qwen2_5_32b_instruct_SSFT-lr5e-5/raw/main/README.md

## kovsbo/guard-sft-synthetic

No. The cached card file is a missing-card marker, and the live README returns 404. The Hub page says there is no model card. The repo files are config, tokenizer, and weights, and `config.json` names no corpus. No paper or GitHub page names this repo id.

https://huggingface.co/kovsbo/guard-sft-synthetic
https://huggingface.co/kovsbo/guard-sft-synthetic/raw/main/config.json

## kovsbo/guard2

No. The cached card file is a missing-card marker, and the live README returns 404. The Hub page says there is no model card. The repo files are config, tokenizer, and weights, and `config.json` names no corpus. No paper or GitHub page names this repo id.

https://huggingface.co/kovsbo/guard2
https://huggingface.co/kovsbo/guard2/raw/main/config.json

## krystal7/llama-8b-reflect-sft

Yes. There is no cached card. The live card says the data schema is "harmful pattern + general pattern" and links the Reflector paper and GitHub repo. The paper describes a teacher-built reflection set and does not give a Hub dataset id. The GitHub README names this repo id, and the two SFT pattern files open and contain query records.

https://huggingface.co/krystal7/llama-8b-reflect-sft
https://arxiv.org/abs/2605.20654
https://arxiv.org/html/2605.20654
https://github.com/mjc-ma-01/self-reflection-llm/blob/main/README.md
https://raw.githubusercontent.com/mjc-ma-01/self-reflection-llm/main/datasets/sft/source/harmful_pattern.json
https://raw.githubusercontent.com/mjc-ma-01/self-reflection-llm/main/datasets/sft/source/general_pattern.json

## krystal7/Reflector-Internalizing-Safety-Llama-3.1-8B-RL

Yes. The cached card and the live card match. Both say the data schema is "harmful pattern + general pattern" and link the same paper and GitHub repo. The GitHub README names this repo id as the RL checkpoint. The two RL pattern files open and contain query records.

https://huggingface.co/krystal7/Reflector-Internalizing-Safety-Llama-3.1-8B-RL
https://arxiv.org/abs/2605.20654
https://arxiv.org/html/2605.20654
https://github.com/mjc-ma-01/self-reflection-llm/blob/main/README.md
https://raw.githubusercontent.com/mjc-ma-01/self-reflection-llm/main/datasets/rl/harmful_pattern.json
https://raw.githubusercontent.com/mjc-ma-01/self-reflection-llm/main/datasets/rl/general_pattern.json

## KyawSu/nllb-en-my-workplace-safety-v1

No. The cached card file is a missing-card marker, and the live README returns 404. `config.json` names no corpus. The sibling repo `KyawSu/nllb-en-my-workplace-safety` says it was trained on ALT (`mutiyama/alt`), and that page loads, but that card names the sibling repo id, not this one.

https://huggingface.co/KyawSu/nllb-en-my-workplace-safety-v1
https://huggingface.co/KyawSu/nllb-en-my-workplace-safety-v1/raw/main/config.json
https://huggingface.co/KyawSu/nllb-en-my-workplace-safety
https://huggingface.co/datasets/mutiyama/alt
