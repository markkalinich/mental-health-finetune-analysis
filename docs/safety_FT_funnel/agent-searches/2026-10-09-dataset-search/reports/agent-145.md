## model-raising/spp-t0-3b-base

Yes. The live card says this base model was pretrained on about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, with reflections inserted into the safety-annotated documents. No cached card was on disk. The repo file list is the README, tokenizer files, and two weight shards. The Dolma 3 mix page loads, and the same project's 1T selection manifest and reflection set load.

https://huggingface.co/model-raising/spp-t0-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://arxiv.org/html/2608.13482

## model-raising/spp-t0-3b-instruct

Yes. The live card says pretraining used about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, then 300k persona-binding examples: 90% WildChat-1M and 10% WildJailbreak and WildGuardMix. No cached card was on disk. The repo file list is the README, tokenizer, chat template, and weight shards. Those three prompt datasets load, and the published SFT pools load.

https://huggingface.co/model-raising/spp-t0-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k
https://arxiv.org/html/2608.13482

## model-raising/spp-t0-mt-1.7b-base

Yes. The live card says this 1.7B base model was pretrained on about 100B tokens from a subset of the Olmo 3 Dolma 3 mixture, with reflections in the safety-annotated documents, then a reflection midtraining stage on those documents. No cached card was on disk. The Dolma 3 mix, the 1T selection manifest, and the reflection set all load. The published manifest is the 1T pool; this card's run is the shorter 100B budget.

https://huggingface.co/model-raising/spp-t0-mt-1.7b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://arxiv.org/html/2608.13482

## model-raising/spp-t0-mt-1.7b-instruct

Yes. The live card says pretraining used about 100B tokens from a subset of the Olmo 3 Dolma 3 mixture plus reflection midtraining, then the shared 300k persona-binding mix: 90% WildChat-1M and 10% WildJailbreak and WildGuardMix. No cached card was on disk. The Dolma 3 mix, the selection manifest, the reflection set, the three prompt datasets, and the published SFT pools all load.

https://huggingface.co/model-raising/spp-t0-mt-1.7b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k
https://arxiv.org/html/2608.13482

## model-raising/spp-t0-mt-3b-base

Yes. The live card says this 3B base model was pretrained on about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, with reflections in the safety-annotated documents, then a reflection midtraining stage on those documents. No cached card was on disk. The Dolma 3 mix, the 1T selection manifest, and the reflection set all load.

https://huggingface.co/model-raising/spp-t0-mt-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://arxiv.org/html/2608.13482

## model-raising/spp-t0-mt-3b-instruct

Yes. The live card says pretraining used about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture plus reflection midtraining, then the shared 300k persona-binding mix: 90% WildChat-1M and 10% WildJailbreak and WildGuardMix. No cached card was on disk. The Dolma 3 mix, the selection manifest, the reflection set, the three prompt datasets, and the published SFT pools all load.

https://huggingface.co/model-raising/spp-t0-mt-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k
https://arxiv.org/html/2608.13482

## model-raising/spp-vanilla-1.7b-base

Yes. The live card says this baseline was pretrained on about 100B tokens from a subset of the Olmo 3 Dolma 3 mixture, with no safety reflections. No cached card was on disk. The repo file list is the README, tokenizer files, and one weight file. The Dolma 3 mix page and the 1T selection manifest both load.

https://huggingface.co/model-raising/spp-vanilla-1.7b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://arxiv.org/html/2608.13482

## model-raising/spp-vanilla-1.7b-instruct

Yes. The live card says pretraining used about 100B tokens from a subset of the Olmo 3 Dolma 3 mixture, then the shared 300k persona-binding mix: 90% WildChat-1M and 10% WildJailbreak and WildGuardMix. No cached card was on disk. The Dolma 3 mix, the selection manifest, the three prompt datasets, and the published SFT pools all load.

https://huggingface.co/model-raising/spp-vanilla-1.7b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k
https://arxiv.org/html/2608.13482

## model-raising/spp-vanilla-3b-base

Yes. The live card says this baseline was pretrained on about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, with no safety reflections. No cached card was on disk. The Dolma 3 mix page and the 1T selection manifest both load.

https://huggingface.co/model-raising/spp-vanilla-3b-base
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://arxiv.org/html/2608.13482

## model-raising/spp-vanilla-3b-instruct

Yes. The live card says pretraining used about 500B tokens from a subset of the Olmo 3 Dolma 3 mixture, then the shared 300k persona-binding mix: 90% WildChat-1M and 10% WildJailbreak and WildGuardMix. No cached card was on disk. The Dolma 3 mix, the selection manifest, the three prompt datasets, and the published SFT pools all load.

https://huggingface.co/model-raising/spp-vanilla-3b-instruct
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/WildChat-1M
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k
https://arxiv.org/html/2608.13482
