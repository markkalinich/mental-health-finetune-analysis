# Dataset search, agent 144

No cached card existed for any of these ten repositories. Each live card names the training corpus, and the named pages load.

## model-raising/spp-filtered-1.7b-base

Yes. The card says this base model was pretrained on about 100B tokens from a subset of the Olmo 3 Dolma 3 mixture, with the loss masked on documents labeled unsafe. The repository holds the README, tokenizer, and weights, and no training script. The same weights file is also `dlab-spp/filtered-1.7b-base`. The paper and the data repository say that subset is rebuilt from `allenai/dolma3_mix-6T` with `dlab-spp/corpus-1T-manifest`, and both dataset pages load.

https://huggingface.co/model-raising/spp-filtered-1.7b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data

## model-raising/spp-filtered-1.7b-instruct

Yes. The card says pretraining used the same Dolma 3 subset, then persona-binding fine-tuning on 300k examples: 90% WildChat-1M instructions and 10% safety prompts from WildJailbreak and WildGuardMix. Those three dataset pages load, as do the Dolma 3 mix and the subset manifest. The weights file matches `dlab-spp/filtered-1.7b-instruct`. The repository has no training script.

https://huggingface.co/model-raising/spp-filtered-1.7b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://arxiv.org/html/2608.13482

## model-raising/spp-filtered-3b-base

Yes. The card says this 3B base model was pretrained on about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, with loss masked on documents labeled unsafe. The repository files are the README, tokenizer, and two weight shards. The Dolma 3 mix page and the subset manifest both load. The paper describes this Filtered 3B run on 500B tokens.

https://huggingface.co/model-raising/spp-filtered-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data

## model-raising/spp-filtered-3b-instruct

Yes. The card names the same 500B-token Dolma 3 subset for pretraining, then the 300k persona-binding mix: 90% WildChat-1M and 10% WildJailbreak plus WildGuardMix. All of those dataset pages load. The repository has no training script. The card also lists safety-fraction revisions, and every revision uses those same prompt sources.

https://huggingface.co/model-raising/spp-filtered-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix

## model-raising/spp-mt-1.7b-base

Yes. The card says pretraining used about 100B tokens from a subset of the Olmo 3 Dolma 3 mixture, with SPP reflections added only in midtraining on the safety-annotated documents. The Dolma 3 mix, the subset manifest, and `dlab-spp/reflection-50m` all load. The repository has no training script. The paper calls this variant SPP {MT} at the 1.7B, 100B-token scale.

https://huggingface.co/model-raising/spp-mt-1.7b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://arxiv.org/html/2608.13482

## model-raising/spp-mt-1.7b-instruct

Yes. The card names the Dolma 3 subset and midtraining reflections, then the same 300k persona-binding mix of WildChat-1M, WildJailbreak, and WildGuardMix. Those pages load, along with the reflection set and the subset manifest. The repository files are the README, tokenizer, and weights.

https://huggingface.co/model-raising/spp-mt-1.7b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix

## model-raising/spp-mt-3b-base

Yes. The card says this 3B base model saw about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, with SPP reflections only during midtraining. The Dolma 3 mix, the subset manifest, and the reflection dataset all load. The repository has two weight shards and no training script. The paper describes SPP {MT} at the 3B, 500B-token scale.

https://huggingface.co/model-raising/spp-mt-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://arxiv.org/html/2608.13482

## model-raising/spp-mt-3b-instruct

Yes. The card names the 500B-token Dolma 3 subset, midtraining reflections, and the 300k mix of WildChat-1M, WildJailbreak, and WildGuardMix. Those dataset pages load. The card also publishes safety-fraction revisions that change only the ratio of those same prompt sources. The repository has no training script.

https://huggingface.co/model-raising/spp-mt-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix

## model-raising/spp-t0-1.7b-base

Yes. The card says this base model was pretrained on about 100B tokens from a subset of the Olmo 3 Dolma 3 mixture, with SPP reflections inserted into the safety-annotated documents from the first token. The Dolma 3 mix, the subset manifest, and `dlab-spp/reflection-50m` all load. The repository has no training script. The paper calls this variant SPP {T0} at 1.7B on 100B tokens.

https://huggingface.co/model-raising/spp-t0-1.7b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://arxiv.org/html/2608.13482

## model-raising/spp-t0-1.7b-instruct

Yes. The card names that same Dolma 3 subset with reflections from token zero, then the 300k persona-binding mix of WildChat-1M, WildJailbreak, and WildGuardMix. Those dataset pages load. The repository holds the README, tokenizer, and weights, and no training script.

https://huggingface.co/model-raising/spp-t0-1.7b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
