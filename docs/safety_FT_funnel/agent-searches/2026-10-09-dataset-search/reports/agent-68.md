# Dataset search, agent 68

## Jeesup/svd-safety-l3_swift_remove50_swapgapiter_b010

No. The cached card and the live card match, and neither names a training corpus. They describe a parameter swap on `Jeesup/svd-safety-l3_swift_remove50`. `compression.json` names only local paths, `jailbreakbench_harmful_behaviors.csv` and `jailbreakbench_benign_behaviors.csv`, which are not files in this repository. The parent card names alpaca-cleaned and WikiText-2, and that card is about the parent checkpoint, not this one. Swift-SVD (arXiv 2604.01609) does not mention this repository.

https://huggingface.co/Jeesup/svd-safety-l3_swift_remove50_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-l3_swift_remove50_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l3_swift_remove50
https://arxiv.org/abs/2604.01609
https://arxiv.org/html/2604.01609v1

## Jeesup/svd-safety-l3_swift_remove50_swapgapiter_evfront_b010

No. The cached card and the live card match, and neither names a training corpus. This cell uses frontier eviction on the same Swift-SVD base. `compression.json` again points only at those two local JailbreakBench CSV paths. The parent card that names alpaca-cleaned is about `Jeesup/svd-safety-l3_swift_remove50`, not this repository. No paper or GitHub page names this checkpoint's training data.

https://huggingface.co/Jeesup/svd-safety-l3_swift_remove50_swapgapiter_evfront_b010
https://huggingface.co/Jeesup/svd-safety-l3_swift_remove50_swapgapiter_evfront_b010/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l3_swift_remove50
https://arxiv.org/html/2604.01609v1

## Jeesup/svd-safety-l3_swift_remove50_swapgapiter_rankunit_b010

No. The cached card and the live card match, and neither names a training corpus. This cell ranks swap candidates by safety value alone. `compression.json` has the same local JailbreakBench paths and does not name a Hub dataset. The parent card's alpaca-cleaned line is about a different checkpoint. Swift-SVD's paper does not mention this repository.

https://huggingface.co/Jeesup/svd-safety-l3_swift_remove50_swapgapiter_rankunit_b010
https://huggingface.co/Jeesup/svd-safety-l3_swift_remove50_swapgapiter_rankunit_b010/raw/main/compression.json
https://arxiv.org/html/2604.01609v1

## Jeesup/svd-safety-llama2_7b_chat_remove_20_seed42

No. The cached card and the live card match. They report SVD-LLM compression with a 0% restore budget and do not name a corpus. WikiText-2 appears only as a perplexity number. `compression.json` says `stage` is `finetuned` and points at a local `finetune_v/merge.pt`, with upstream `AIoT-MLSys-Lab/SVD-LLM`, and it does not name a dataset. The SVD-LLM paper uses WikiText-2 and Alpaca for its own runs and does not mention this repository.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_remove_20_seed42
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_remove_20_seed42/raw/main/compression.json
https://arxiv.org/html/2403.07378
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-llama2_7b_chat_remove_30_seed42

No. The cached card and the live card match, and neither names a training corpus. `compression.json` has the same shape as the 20% cell: `stage` `finetuned`, a local `finetune_v/merge.pt`, and upstream `AIoT-MLSys-Lab/SVD-LLM`. That file does not name the finetune set. The SVD-LLM paper is not about this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_remove_30_seed42
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_remove_30_seed42/raw/main/compression.json
https://arxiv.org/html/2403.07378
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-llama2_7b_chat_remove_40_seed42

No. The cached card and the live card match, and neither names a training corpus. `compression.json` records `stage` `finetuned` and a local `finetune_v/merge.pt` without a dataset name. WikiText-2 on the card is the perplexity evaluation, not a named training set. No paper or GitHub page prints this repository id next to a corpus.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_remove_40_seed42
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_remove_40_seed42/raw/main/compression.json
https://arxiv.org/html/2403.07378
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_finetuned_keep_0p50

Yes. The card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The live card matches the cache from 2026-10-05. The Hub dataset page loads, with a train split of 52,002 rows. WikiText-2 on the card is the SVD calibration set, not the LoRA training set.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_finetuned_keep_0p50
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/yahma/alpaca-cleaned/tree/main
https://huggingface.co/datasets/yahma/alpaca-cleaned/viewer

## Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_finetuned_keep_0p60

Yes. The card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The live card matches the cache. The same Hub dataset page loads. WikiText-2 is named only as the 256-sequence calibration set.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_finetuned_keep_0p60
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/yahma/alpaca-cleaned/viewer

## Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_finetuned_keep_0p80

Yes. The card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The live card matches the cache. The Hub dataset page loads. The card says only the coefficients were trained, on that alpaca set.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_finetuned_keep_0p80
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/yahma/alpaca-cleaned/viewer

## Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_jbbmix_finetuned_keep_0p50

Yes. The LoRA training set is `yahma/alpaca-cleaned`, and that Hub page loads. The card also mixes JailbreakBench harmful behaviours into the calibration set, as prompts with no responses. Those behaviours are not the LoRA training rows. The live card matches the cache.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_jbbmix_finetuned_keep_0p50
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/yahma/alpaca-cleaned/viewer
