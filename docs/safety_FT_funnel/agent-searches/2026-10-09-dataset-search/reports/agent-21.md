# Dataset search, agent 21

## Dipto084/Llama3.1-8B-TRACE

Yes. The GitHub README names this repository and the RL split the GDPO stage trained on. There was no cached card. The live card describes a constructed SFT corpus from JailbreakBench, HarmBench, and OR-Bench seeds, and the repo file list has prompts and weights, not a training file. The paper HTML (arXiv:2608.15594) says the data are at that GitHub. The dataset page loaded. Download is gated (manual request), and the Hub API reports `private: false`, not a 401.

https://huggingface.co/Dipto084/Llama3.1-8B-TRACE
https://arxiv.org/abs/2608.15594
https://arxiv.org/html/2608.15594
https://github.com/Dipto084/TRACE
https://huggingface.co/datasets/Dipto084/TRACE_RL_Dataset

## Dipto084/Qwen3-8B-TRACE

Yes. The same GitHub README lists this repository next to the Llama TRACE model and the same RL split (5,234 curated plus 500 harm-adjacent), which matches the training-data line on this card. There was no cached card. The repo file list has prompts and weights. The paper's Qwen section says the recipe is held fixed. The dataset page loaded under the same gate as the Llama release.

https://huggingface.co/Dipto084/Qwen3-8B-TRACE
https://arxiv.org/abs/2608.15594
https://arxiv.org/html/2608.15594
https://github.com/Dipto084/TRACE
https://huggingface.co/datasets/Dipto084/TRACE_RL_Dataset

## dlab-spp/filtered-1.7b-base

Yes. The card says this run used about 100B tokens of a subset of the Olmo 3 Dolma 3 mixture, with loss masked on documents labeled unsafe. There was no cached card. The repo file list is weights and tokenizer files. The paper (arXiv:2608.13482) describes that Filtered setup. The selection manifest and the upstream Dolma 3 mix both loaded.

https://huggingface.co/dlab-spp/filtered-1.7b-base
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/dolma3_mix-6T

## dlab-spp/filtered-1.7b-instruct

Yes. The card names the same Dolma 3 subset plus a 300k post-training mix: 90% WildChat-1M instructions and 10% WildJailbreak and WildGuardMix prompts, with constitution-written answers. There was no cached card. The repo file list has no training script. Those two post-training pools loaded, as did the pretraining manifest and Dolma 3. The 90/10 draw is taken from the pools at training time.

https://huggingface.co/dlab-spp/filtered-1.7b-instruct
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## dlab-spp/filtered-3b-base

Yes. The card says this run used about 500B tokens of a subset of the Olmo 3 Dolma 3 mixture, with loss masked on unsafe documents. There was no cached card. The paper describes Filtered at the 3B scale. The selection manifest and the upstream Dolma 3 mix both loaded.

https://huggingface.co/dlab-spp/filtered-3b-base
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/dolma3_mix-6T

## dlab-spp/filtered-3b-instruct

Yes. The card names the 500B-token Dolma 3 subset and the same 300k PBSFT mix (WildChat-1M, WildJailbreak, WildGuardMix). There was no cached card. The two post-training pools, the pretraining manifest, and Dolma 3 all loaded. The card's safety-fraction revisions change only the ratio drawn from those pools.

https://huggingface.co/dlab-spp/filtered-3b-instruct
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## dlab-spp/mt-1.7b-base

Yes. The card says about 100B tokens of the Olmo 3 Dolma 3 subset, with SPP reflections added only in midtraining on the safety-annotated documents. There was no cached card. The paper calls this SPP {MT}. The selection manifest, Dolma 3, and the 51.4M-row reflection set all loaded.

https://huggingface.co/dlab-spp/mt-1.7b-base
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/reflection-50m

## dlab-spp/mt-1.7b-instruct

Yes. The card names that midtraining reflection setup and the same 300k PBSFT mix. There was no cached card. The reflection set, the two post-training pools, the pretraining manifest, and Dolma 3 all loaded.

https://huggingface.co/dlab-spp/mt-1.7b-instruct
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k

## dlab-spp/mt-3b-base

Yes. The card says about 500B tokens of the Olmo 3 Dolma 3 subset, with reflections only in midtraining. There was no cached card. The paper describes SPP {MT} at 3B. The selection manifest, Dolma 3, and the reflection set all loaded.

https://huggingface.co/dlab-spp/mt-3b-base
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/reflection-50m

## dlab-spp/mt-3b-instruct

Yes. The card names the 500B-token midtraining setup and the same 300k PBSFT mix. There was no cached card. The reflection set, the two post-training pools, the pretraining manifest, and Dolma 3 all loaded.

https://huggingface.co/dlab-spp/mt-3b-instruct
https://arxiv.org/abs/2608.13482
https://arxiv.org/html/2608.13482
https://github.com/epfl-dlab/spp-data
https://huggingface.co/datasets/dlab-spp/corpus-1T-manifest
https://huggingface.co/datasets/allenai/dolma3_mix-6T
https://huggingface.co/datasets/dlab-spp/reflection-50m
https://huggingface.co/datasets/dlab-spp/sp-sft-normal-300k
https://huggingface.co/datasets/dlab-spp/sp-sft-safety-180k
