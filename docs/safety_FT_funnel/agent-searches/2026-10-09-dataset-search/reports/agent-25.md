# Dataset search, agent 25

## EntermindAI/Rukun-32B-V

No. The model card names `DATASETS/rukun-teacher/v1/train_v1.jsonl` and `DATASETS/rukun-teacher/v1/val_v1.jsonl` as the fine-tuning files. The Hub repository contains weights and tokenizer files only, so those paths do not open. A research page names four parts of the corpus (Teacher-Core, Rewrite-Boost, Principle-Boost, Format-Guard) and does not link a file. No arXiv paper, GitHub repository, or Hub dataset with this corpus loads.

https://huggingface.co/EntermindAI/Rukun-32B-V
https://fahad.one/research/rukun-ready-ai

## epfl-dlab/spp-filtered-3b-base

Yes. The card says this base model was pretrained on about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture. That mixture loads as `allenai/dolma3_mix-6T`. There is no cached card, and the repository file list is weights and tokenizer files only. The same authors' paper and GitHub describe this Filtered 3B run and publish the document selection as `dlab-spp/corpus-1T-manifest`, which also loads. The paper says the 3B runs use the 500B first half of that prepared corpus.

https://huggingface.co/epfl-dlab/spp-filtered-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://arxiv.org/html/2608.13482v1
https://github.com/epfl-dlab/spp-data

## epfl-dlab/spp-filtered-3b-instruct

Yes. The card says pretraining used a subset of the Olmo 3 Dolma 3 mixture, and post-training used 300k examples with 90% WildChat-1M instructions and 10% safety prompts from WildJailbreak and WildGuardMix. All four Hub pages load. WildJailbreak shows its dataset card and grants access after the AI2 responsible-use form, rather than returning a Hub 404. The same authors publish the generated post-training rows as `dlab-spp/sp-sft-normal-300k` and `dlab-spp/sp-sft-safety-180k`, and those pages load.

https://huggingface.co/epfl-dlab/spp-filtered-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## epfl-dlab/spp-mt-3b-base

Yes. The card says pretraining was about 500B tokens on a subset of the Olmo 3 Dolma 3 mixture, with reflections added only in a later midtraining stage on the safety-annotated documents. The Dolma 3 mixture loads as `allenai/dolma3_mix-6T`. The same authors' paper describes this SPP-MT 3B run, and `dlab-spp/reflection-50m` loads as the reflection rows the released models were trained on. `dlab-spp/corpus-1T-manifest` loads as the document selection for that corpus.

https://huggingface.co/epfl-dlab/spp-mt-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://arxiv.org/html/2608.13482v1

## epfl-dlab/spp-mt-3b-instruct

Yes. The card says pretraining used a subset of the Olmo 3 Dolma 3 mixture, and post-training used WildChat-1M, WildJailbreak, and WildGuardMix. Those Hub pages load. Reflections were added only at midtraining, and `dlab-spp/reflection-50m` loads for that annotated set. The generated post-training rows load as `dlab-spp/sp-sft-normal-300k` and `dlab-spp/sp-sft-safety-180k`.

https://huggingface.co/epfl-dlab/spp-mt-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## epfl-dlab/spp-t0-3b-base

Yes. The card says this model was pretrained from token zero on about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, with reflections inserted into the safety-annotated documents. The mixture loads as `allenai/dolma3_mix-6T`. The same authors describe this SPP-T0 3B run in the paper, and `dlab-spp/reflection-50m` loads as the reflections the released models were trained on. The document selection loads as `dlab-spp/corpus-1T-manifest`.

https://huggingface.co/epfl-dlab/spp-t0-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://arxiv.org/html/2608.13482v1

## epfl-dlab/spp-t0-3b-instruct

Yes. The card says pretraining used a subset of the Olmo 3 Dolma 3 mixture with reflections from token zero, and post-training used WildChat-1M, WildJailbreak, and WildGuardMix. Those Hub pages load. `dlab-spp/reflection-50m` loads as the reflection rows. The generated post-training rows load as `dlab-spp/sp-sft-normal-300k` and `dlab-spp/sp-sft-safety-180k`.

https://huggingface.co/epfl-dlab/spp-t0-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## epfl-dlab/spp-t0-mt-3b-base

Yes. The card says pretraining was about 500B tokens on a subset of the Olmo 3 Dolma 3 mixture, with reflections from token zero and a further midtraining stage on the annotated documents. The mixture loads as `allenai/dolma3_mix-6T`. The paper describes this SPP-T0-MT 3B run, and `dlab-spp/reflection-50m` loads as the reflections the released models were trained on. The document selection loads as `dlab-spp/corpus-1T-manifest`.

https://huggingface.co/epfl-dlab/spp-t0-mt-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://arxiv.org/html/2608.13482v1

## epfl-dlab/spp-t0-mt-3b-instruct

Yes. The card says pretraining used a subset of the Olmo 3 Dolma 3 mixture with reflections from token zero plus midtraining, and post-training used WildChat-1M, WildJailbreak, and WildGuardMix. Those Hub pages load. `dlab-spp/reflection-50m` loads as the reflection rows. The generated post-training rows load as `dlab-spp/sp-sft-normal-300k` and `dlab-spp/sp-sft-safety-180k`.

https://huggingface.co/epfl-dlab/spp-t0-mt-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## epfl-dlab/spp-vanilla-3b-base

Yes. The card says this baseline was pretrained on about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, with no safety intervention. That mixture loads as `allenai/dolma3_mix-6T`. The same authors' paper describes this Vanilla 3B run, and `dlab-spp/corpus-1T-manifest` loads as the document selection. The paper says the 3B runs use the 500B first half of that prepared corpus.

https://huggingface.co/epfl-dlab/spp-vanilla-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://arxiv.org/html/2608.13482v1
https://github.com/epfl-dlab/spp-data
