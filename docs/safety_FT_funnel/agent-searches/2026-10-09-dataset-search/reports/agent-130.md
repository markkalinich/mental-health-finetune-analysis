# Dataset search, agent 130

## linzju/Code-Llama-3-8B_EnchTable_FFN

Yes. There is no cached card. The live card describes an EnchTable FFN merge into `ajibawa-2023/Code-Llama-3-8B` and does not name a corpus. The repository files are weights and tokenizer files. The paper says BeaverTail is used to train the surrogate, and the authors' GitHub lists this exact repository and saves that surrogate under a `beavertail_harmful` path. The Hub dataset `PKU-Alignment/BeaverTails` loads. The paper says the experiment used 1,000 unsafe pairs from that training set.

https://huggingface.co/linzju/Code-Llama-3-8B_EnchTable_FFN/raw/main/README.md
https://arxiv.org/html/2511.09880v1
https://github.com/AntCPLab/EnchTable
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## linzju/Code-Llama-3-8B_EnchTable_FFN_Attention

Yes. There is no cached card. The live card describes the hybrid Attention+FFN merge and does not name a corpus. The same paper and the same GitHub model list cover this checkpoint. The surrogate is trained on BeaverTails, and that Hub dataset loads.

https://huggingface.co/linzju/Code-Llama-3-8B_EnchTable_FFN_Attention/raw/main/README.md
https://arxiv.org/html/2511.09880v1
https://github.com/AntCPLab/EnchTable
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## liuyilun2000/qwen3-0.6b-siren

Yes. There is no cached card. The live card describes SIREN on Qwen3-0.6B and does not name a corpus. The paper, whose authors include Yilun Liu, says SIREN on Qwen3-0.6B is trained on ToxicChat, OpenAI Moderation, Aegis, Aegis 2.0, WildGuard, SafeRLHF, and BeaverTails. The GitHub training script loads those seven Hub datasets, and each page loads. The paper and GitHub name the official release `UofTCSSLab/SIREN-Qwen3-0.6B`, not this repository id.

https://huggingface.co/liuyilun2000/qwen3-0.6b-siren/raw/main/README.md
https://arxiv.org/html/2604.18519
https://github.com/CSSLab/SIREN
https://huggingface.co/datasets/lmsys/toxic-chat
https://huggingface.co/datasets/walledai/openai-moderation-dataset
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## liuyingdelaogong/Qwen_model_Safety

No. The cached card is a 403 error. The live README and `best_model_info.json` return 401 Unauthorized. The repository is manually gated. Web search did not find a paper or GitHub page that names this repository.

https://huggingface.co/liuyingdelaogong/Qwen_model_Safety/raw/main/README.md
https://huggingface.co/liuyingdelaogong/Qwen_model_Safety/raw/main/best_model_info.json

## llamas-community/LlamaGuard-7b

Yes. The cached card and the live card match. The card says the training prompts come from the Anthropic dataset, mixed with in-house red-team examples that are not released. The linked GitHub page and the Hub dataset `Anthropic/hh-rlhf` both load.

https://huggingface.co/llamas-community/LlamaGuard-7b/raw/main/README.md
https://github.com/anthropics/hh-rlhf
https://huggingface.co/datasets/Anthropic/hh-rlhf

## lldois/v23_scratch_clean_cot_guard_lr3e6_ep5

No. The cached card and the live card match. The card names `exp_scratch_clean_cot_guard_ep5`. `experiment_recipe.json` points only at `/home/ll/llm4rec/experiments/data/scratch_clean_cot_guard_ep5.jsonl`. A Hub dataset search for that name returned nothing.

https://huggingface.co/lldois/v23_scratch_clean_cot_guard_lr3e6_ep5/raw/main/README.md
https://huggingface.co/lldois/v23_scratch_clean_cot_guard_lr3e6_ep5/raw/main/experiment_recipe.json

## lldois/v25_v19_product_world_guard_lr18e6_ep028

No. The cached card and the live card match. The card names `exp_v19_product_world_guard`. The recipe points only at `/home/ll/llm4rec/experiments/data/v19_product_world_guard.jsonl`. A Hub dataset search for that name returned nothing.

https://huggingface.co/lldois/v25_v19_product_world_guard_lr18e6_ep028/raw/main/README.md
https://huggingface.co/lldois/v25_v19_product_world_guard_lr18e6_ep028/raw/main/experiment_recipe.json

## lldois/v29_v19_user_world_guard_lr8e7_ep018

No. The cached card and the live card match. The card names `exp_v19_user_world_guard_no_template`. The recipe points only at `/home/ll/llm4rec/experiments/data/v19_user_world_guard_no_template.jsonl`. No Hub dataset with that name loads.

https://huggingface.co/lldois/v29_v19_user_world_guard_lr8e7_ep018/raw/main/README.md
https://huggingface.co/lldois/v29_v19_user_world_guard_lr8e7_ep018/raw/main/experiment_recipe.json

## lldois/v36_v29_general_guard_lr4e7_ep12

No. The cached card and the live card match. The card names `exp_v36_general_guard`. The recipe points only at `/home/ll/llm4rec/experiments/data/v36_general_guard.jsonl`. No Hub dataset with that name loads.

https://huggingface.co/lldois/v36_v29_general_guard_lr4e7_ep12/raw/main/README.md
https://huggingface.co/lldois/v36_v29_general_guard_lr4e7_ep12/raw/main/experiment_recipe.json

## lldois/v42_v29_user_evolution_guard_lr5e7_ep10

No. The cached card and the live card match. The card names `exp_v42_user_evolution`. The recipe points only at `/home/ll/llm4rec/experiments/data/v42_user_evolution.jsonl`. No Hub dataset with that name loads.

https://huggingface.co/lldois/v42_v29_user_evolution_guard_lr5e7_ep10/raw/main/README.md
https://huggingface.co/lldois/v42_v29_user_evolution_guard_lr5e7_ep10/raw/main/experiment_recipe.json
