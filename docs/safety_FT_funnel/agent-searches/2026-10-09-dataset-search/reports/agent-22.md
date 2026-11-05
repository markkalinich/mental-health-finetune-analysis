# Dataset search, agent 22

## dlab-spp/t0-1.7b-base

Yes. The live model card says this base checkpoint was pretrained for about 100B tokens on a subset of the Olmo 3 Dolma 3 mixture, with Synthetic Persona Pretraining reflections inserted into the safety-annotated documents. There is no cached card. The repo files besides the README are the tokenizer, the config, and the weights. The Dolma 3 mix page loads as allenai/dolma3_mix-6T. The same authors publish the ordered subsample as dlab-spp/corpus-1T-manifest, and the reflections plus source text as dlab-spp/reflection-50m. The paper and the epfl-dlab/spp code repo describe this SPP-from-token-zero 1.7B run.

https://huggingface.co/dlab-spp/t0-1.7b-base
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m

## dlab-spp/t0-1.7b-instruct

Yes. This is the instruction-tuned counterpart of t0-1.7b-base. The card names the same Dolma 3 subset for pretraining, then a 300k-example persona-binding fine-tune: 90% WildChat-1M instructions and 10% safety prompts from WildJailbreak and WildGuardMix. Those three Hub dataset pages load. The generated training rows are the published pools dlab-spp/sp-sft-normal-300k and dlab-spp/sp-sft-safety-180k; the 10% safety mix is drawn from those pools. The repo has no training script, only the card, tokenizer, config, and weights.

https://huggingface.co/dlab-spp/t0-1.7b-instruct
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://github.com/epfl-dlab/spp-training
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## dlab-spp/t0-3b-base

Yes. The card says this 3B base model was pretrained for about 500B tokens on a subset of the Olmo 3 Dolma 3 mixture, with the same reflection insertion as the 1.7B token-zero run. The Dolma 3 mix page loads, and dlab-spp/corpus-1T-manifest is the ordered subsample a reader can replay against it. dlab-spp/reflection-50m loads the reflections and the annotated document text. No cached card, and no training script in the repo.

https://huggingface.co/dlab-spp/t0-3b-base
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m

## dlab-spp/t0-3b-instruct

Yes. Pretraining matches t0-3b-base. Post-training is the shared 300k persona-binding mix: 90% WildChat-1M and 10% WildJailbreak plus WildGuardMix. Those dataset pages load, as do the published row pools dlab-spp/sp-sft-normal-300k and dlab-spp/sp-sft-safety-180k. The card's main revision is the 10% safety mix; other revisions on this repo only change that ratio. The repo files are the card, tokenizer, config, and weights.

https://huggingface.co/dlab-spp/t0-3b-instruct
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://github.com/epfl-dlab/spp-training
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## dlab-spp/t0-mt-1.7b-base

Yes. The card says this checkpoint continues the 1.7B token-zero run, then does a reflection-focused midtraining stage on the annotated documents. The pretraining mixture is the same Olmo 3 Dolma 3 subset. allenai/dolma3_mix-6T, dlab-spp/corpus-1T-manifest, and dlab-spp/reflection-50m all load. reflection-50m is the annotated-document set that midtraining uses. No cached card and no training script in the repo.

https://huggingface.co/dlab-spp/t0-mt-1.7b-base
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m

## dlab-spp/t0-mt-1.7b-instruct

Yes. Pretraining and midtraining match t0-mt-1.7b-base. The card then names the same 300k persona-binding fine-tune: WildChat-1M, WildJailbreak, and WildGuardMix. Those pages load, and the training rows are in dlab-spp/sp-sft-normal-300k and dlab-spp/sp-sft-safety-180k. The repo has no training script.

https://huggingface.co/dlab-spp/t0-mt-1.7b-instruct
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://github.com/epfl-dlab/spp-training
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## dlab-spp/t0-mt-3b-base

Yes. The card says this 3B checkpoint was pretrained for about 500B tokens on a subset of the Olmo 3 Dolma 3 mixture, with reflections from token zero, then midtrained on the annotated documents. The Dolma 3 mix page loads. The subsample manifest and the reflection set load as dlab-spp/corpus-1T-manifest and dlab-spp/reflection-50m. No cached card and no training script in the repo.

https://huggingface.co/dlab-spp/t0-mt-3b-base
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m

## dlab-spp/t0-mt-3b-instruct

Yes. Pretraining and midtraining match t0-mt-3b-base. Post-training is the shared 300k mix of WildChat-1M, WildJailbreak, and WildGuardMix, and those pages load. The generated rows are dlab-spp/sp-sft-normal-300k and dlab-spp/sp-sft-safety-180k. The card's main weights are the 10% safety mix; other revisions only change that ratio. The repo files are the card, tokenizer, config, and weights.

https://huggingface.co/dlab-spp/t0-mt-3b-instruct
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://github.com/epfl-dlab/spp-training
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## dlab-spp/vanilla-1.7b-base

Yes. The card says this baseline was pretrained for about 100B tokens on a subset of the Olmo 3 Dolma 3 mixture, with no reflection insertion. allenai/dolma3_mix-6T loads, and dlab-spp/corpus-1T-manifest is the ordered subsample for this project. The reflection set is not this checkpoint's training data. No cached card and no training script in the repo.

https://huggingface.co/dlab-spp/vanilla-1.7b-base
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest

## dlab-spp/vanilla-1.7b-instruct

Yes. Pretraining matches vanilla-1.7b-base. The card then names the same 300k persona-binding fine-tune: 90% WildChat-1M and 10% WildJailbreak plus WildGuardMix. Those three pages load, and the training rows are in dlab-spp/sp-sft-normal-300k and dlab-spp/sp-sft-safety-180k. The repo has no training script.

https://huggingface.co/dlab-spp/vanilla-1.7b-instruct
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp
https://github.com/epfl-dlab/spp-training
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k
