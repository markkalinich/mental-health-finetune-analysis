## Jeesup/svd-safety-l31_remove40_swapgapiter_rankunit_b010

No. The cached card and the live card match, and both describe SVD-LLM compression plus a parameter swap, not a named training corpus. `compression.json` points at local JailbreakBench CSV paths and at a parent directory `svd-safety-llama3_1_8b_instruct_up_svdllm_exactrope_finetuned_keep_0p60`. That parent's own card says its LoRA update used `yahma/alpaca-cleaned`, but that card is about the parent, not this swap checkpoint. No paper or GitHub repository names this repository id.

https://huggingface.co/Jeesup/svd-safety-l31_remove40_swapgapiter_rankunit_b010
https://huggingface.co/Jeesup/svd-safety-llama3_1_8b_instruct_up_svdllm_exactrope_finetuned_keep_0p60

## Jeesup/svd-safety-l31_remove50_swapgapiter_rankunit_b010

No. The cached card and the live card match, and both describe SVD-LLM compression plus a parameter swap. `compression.json` points at the same local JailbreakBench CSV paths and at the parent directory `svd-safety-llama3_1_8b_instruct_up_svdllm_exactrope_finetuned_keep_0p50`. That parent's card says its LoRA update used `yahma/alpaca-cleaned`, and it does not name this swap checkpoint. Searches did not find a paper or GitHub repository for this repository id.

https://huggingface.co/Jeesup/svd-safety-l31_remove50_swapgapiter_rankunit_b010
https://huggingface.co/Jeesup/svd-safety-llama3_1_8b_instruct_up_svdllm_exactrope_finetuned_keep_0p50

## Jeesup/svd-safety-l31_swift_remove20

Yes. The live card matches the cache and says this Swift-SVD checkpoint was recovered with SVD-LLM stage-2 LoRA on alpaca-cleaned. WikiText-2 is named only as the 256 by 2048 calibration set for rank allocation. The Hub dataset `yahma/alpaca-cleaned` loads. `compression.json` records the recovery script as SVD-LLM `LoRA.py` and does not name a second corpus.

https://huggingface.co/Jeesup/svd-safety-l31_swift_remove20
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l31_swift_remove30

Yes. The live card matches the cache and says the stage-2 LoRA recovery used alpaca-cleaned, after Swift-SVD compression to 70% of dense parameters. WikiText-2 is the calibration set, not the LoRA set. The Hub dataset `yahma/alpaca-cleaned` loads. `compression.json` points at the same SVD-LLM LoRA recovery and does not name another corpus.

https://huggingface.co/Jeesup/svd-safety-l31_swift_remove30
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l31_swift_remove40

Yes. The live card matches the cache and says the stage-2 LoRA recovery used alpaca-cleaned, after Swift-SVD compression to 60% of dense parameters. WikiText-2 is the calibration set. The Hub dataset `yahma/alpaca-cleaned` loads. No paper about this repository id turned up.

https://huggingface.co/Jeesup/svd-safety-l31_swift_remove40
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l31_swift_remove50

Yes. The live card matches the cache and says the stage-2 LoRA recovery used alpaca-cleaned, after Swift-SVD compression to 50% of dense parameters. WikiText-2 is the calibration set. The Hub dataset `yahma/alpaca-cleaned` loads. `compression.json` records the recovery as SVD-LLM `LoRA.py`.

https://huggingface.co/Jeesup/svd-safety-l31_swift_remove50
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l3_basis_jbbsftx1_remove40

Yes. The live card matches the cache, and its recovery row says the coefficient LoRA used alpaca-cleaned for 2 epochs. `compression.json` names the same corpus and a local file, `alpaca_cleaned_jbbsft_x1.json`, which is not a public page. The Hub dataset `yahma/alpaca-cleaned` loads. The file's calibration fields are empty.

https://huggingface.co/Jeesup/svd-safety-l3_basis_jbbsftx1_remove40
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l3_basis_jbbsftx1_remove50

Yes. The live card matches the cache, and its recovery row says the coefficient LoRA used alpaca-cleaned for 2 epochs. `compression.json` again labels the training path alpaca-cleaned, stored as a local `alpaca_cleaned_jbbsft_x1.json`. That local path does not open. The Hub dataset `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svd-safety-l3_basis_jbbsftx1_remove50
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l3_basis_remove40_swapgapnet_rankunit_b010

Yes. The live card matches the cache. Its recovery row says the coefficient LoRA used alpaca-cleaned, and `compression.json` records `data_path` as `alpaca-cleaned (data/alpaca_cleaned.json)` before a later parameter swap. The Hub dataset `yahma/alpaca-cleaned` loads. The JailbreakBench entries in that file are local calibration indexes, not a page a reader can open.

https://huggingface.co/Jeesup/svd-safety-l3_basis_remove40_swapgapnet_rankunit_b010
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l3_basis_remove50_swapgapnet_rankunit_b010

Yes. The live card matches the cache, and the recovery row names alpaca-cleaned for the coefficient LoRA. `compression.json` records the same `data_path`, `alpaca-cleaned (data/alpaca_cleaned.json)`, and then a `swapgapnet_iter` swap. The Hub dataset `yahma/alpaca-cleaned` loads. The local calibration paths do not.

https://huggingface.co/Jeesup/svd-safety-l3_basis_remove50_swapgapnet_rankunit_b010
https://huggingface.co/datasets/yahma/alpaca-cleaned
