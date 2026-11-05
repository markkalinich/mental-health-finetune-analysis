## Raghav-Singhal/spp-util-t0-mt-3b-base

No. There is no cached card. The live card says this midtraining run repeats `model-raising/spp-t0-mt-3b-base` with util-constitution reflections and the same data windows. It does not name a file. The SPP paper and `epfl-dlab/spp-data` publish `dlab-spp/reflection-50m` and a Dolma 3 manifest for the paper constitution, which is a different reflection set from this util run. The repository files are weights and a tokenizer.

https://huggingface.co/Raghav-Singhal/spp-util-t0-mt-3b-base
https://arxiv.org/html/2608.13482v1
https://github.com/epfl-dlab/spp-data
https://huggingface.co/datasets/dlab-spp/reflection-50m

## rainmana/Qwen3Guard-Gen-0.6B-heretic

No. The cached card and the live card match. They say this checkpoint was made with Heretic v1.1.0. The copied Qwen3Guard paragraph says the base series was trained on 1.19 million labeled prompts, and that set is not a published dataset. Heretic's default config uses `mlabonne/harmful_behaviors` and `mlabonne/harmless_alpaca`, but this card does not say those defaults were the prompts for this checkpoint.

https://huggingface.co/rainmana/Qwen3Guard-Gen-0.6B-heretic
https://github.com/p-e-w/heretic
https://github.com/p-e-w/heretic/blob/master/config.default.toml

## Rakancorle1/FoodGuard_qwenguard_4b_4k

No. The cached card is a missing-file stub, and the live README returns 404. `trainer_log.jsonl` records loss over 105 steps and does not name a corpus. The paper "Cooking Up Risks" describes FoodGuard-4B as a fine-tune of Qwen3Guard-4B on an 8:2 in-house split and does not print this repository id or a dataset URL.

https://huggingface.co/Rakancorle1/FoodGuard_qwenguard_4b_4k
https://huggingface.co/Rakancorle1/FoodGuard_qwenguard_4b_4k/raw/main/trainer_log.jsonl
https://arxiv.org/html/2604.01444v2

## Rakancorle1/FoodGuard_qwenguard_4k

Yes. The cached card and the live card say this checkpoint is a fine-tune of Qwen/Qwen3Guard-Gen-8B on the foodscience_guardrail_train dataset. A search for that name opens `Rakancorle11/foodscience-guardrail`. Its train split has 4,372 rows of food-safety guardrail instructions. The trainer log prints 0.376 samples per second over 34,858.5 seconds, about 4,369 examples across 3 epochs, and 4,372 examples would print as the same 0.376. The paper does not link this Hub id.

https://huggingface.co/Rakancorle1/FoodGuard_qwenguard_4k
https://huggingface.co/datasets/Rakancorle11/foodscience-guardrail
https://huggingface.co/datasets/Rakancorle11/foodscience-guardrail/viewer/default/train

## RanaEzzeddine/jais-6p7b-95-5-refusal-first

No. The cached card is a missing-file stub, and the live README returns 404. The repository holds weights, a tokenizer, and `training_args.bin`. The config does not name a dataset. Searches for this repository id do not find a paper or GitHub page that names an open corpus.

https://huggingface.co/RanaEzzeddine/jais-6p7b-95-5-refusal-first
https://huggingface.co/RanaEzzeddine/jais-6p7b-95-5-refusal-first/raw/main/config.json

## RanaEzzeddine/Qwen3-8B-95-5-refusal-first

No. The cached card is a missing-file stub, and the live README returns 404. The repository holds weights, a tokenizer, and `training_args.bin`. The config does not name a dataset. Searches for this repository id do not find a paper or GitHub page that names an open corpus.

https://huggingface.co/RanaEzzeddine/Qwen3-8B-95-5-refusal-first
https://huggingface.co/RanaEzzeddine/Qwen3-8B-95-5-refusal-first/raw/main/config.json

## redashes/Qwen3.8-27B-BF16-SSMFIX-apostate

Yes. There is no cached card. The live card describes a KCRN unlearning edit and does not name a corpus. `apostate_config.json` in this repository sets the fit prompts to `mlabonne/harmful_behaviors` and `mlabonne/harmless_alpaca`, 600 rows each. Both dataset pages load.

https://huggingface.co/redashes/Qwen3.8-27B-BF16-SSMFIX-apostate
https://huggingface.co/redashes/Qwen3.8-27B-BF16-SSMFIX-apostate/raw/main/apostate_config.json
https://huggingface.co/datasets/mlabonne/harmful_behaviors
https://huggingface.co/datasets/mlabonne/harmless_alpaca

## RedHatAI/Llama-Guard-4-12B

No. The cached card and the live card match. They say post-training used a blend of Llama Guard 3-8B and Llama Guard 3-11B-vision data, plus multi-image samples and multilingual annotations. That blend is not a Hub dataset, a GitHub file, or a paper appendix a reader can open. The PurpleLlama model card says the same thing.

https://huggingface.co/RedHatAI/Llama-Guard-4-12B
https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard4/12B/MODEL_CARD.md

## Repoaner/llama_guard_vision

No. The cached card and the live card are the Llama Guard 3 Vision card. They describe a hybrid set of human prompts and synthetic responses. The HTML paper (arXiv:2411.10414) gives the sizes, 22,500 prompt-image pairs and 40,034 response rows, and does not link a download. The code link is the inference recipe, not the training set.

https://huggingface.co/Repoaner/llama_guard_vision
https://arxiv.org/abs/2411.10414
https://arxiv.org/html/2411.10414

## resfebel/billage-guard-v2-16bit

No. The cached card and the live card are only a Llama 3.2 license line. The config is an Mllama model with a Llama Guard 3 Vision chat template, and it does not name a base dataset. The upload commit message is "Upload folder using huggingface_hub". Searches for billage-guard do not find a paper or a dataset page for this checkpoint.

https://huggingface.co/resfebel/billage-guard-v2-16bit
https://huggingface.co/resfebel/billage-guard-v2-16bit/raw/main/config.json
