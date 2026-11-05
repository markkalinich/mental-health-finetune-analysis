## Jeesup/svd-safety-llama3_8b_instruct_remove_30_seed3_jbbmix_calib

No. The cached card and the live card match, and neither names a training corpus. `compression.json` marks the stage as finetuned and records a local path ending in `jbbmix_calib/finetune_v/merge.pt`. No arXiv paper and no GitHub file name this repository. The upstream SVD-LLM README shows `yahma/alpaca-cleaned` as that project's own LoRA example, and that README does not name this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_30_seed3_jbbmix_calib
https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_30_seed3_jbbmix_calib/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-llama3_8b_instruct_remove_30_seed3_jbbmixsft

No. The cached card and the live card match, and neither names a training corpus. `compression.json` marks the stage as finetuned and records a local path ending in `jbbmixsft/finetune_v/merge.pt`. No arXiv paper and no GitHub file name this repository. The token `jbbmix` in the repository id is not a dataset page that this card points to.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_30_seed3_jbbmixsft
https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_30_seed3_jbbmixsft/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-llama3_8b_instruct_remove_40_seed3_jbbmix_calib

No. The cached card and the live card match, and neither names a training corpus. `compression.json` marks the stage as finetuned and records a local path ending in `jbbmix_calib/finetune_v/merge.pt`. The repository has no training script besides that JSON. No paper names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_40_seed3_jbbmix_calib
https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_40_seed3_jbbmix_calib/raw/main/compression.json

## Jeesup/svd-safety-llama3_8b_instruct_remove_40_seed3_jbbmixsft

No. The cached card and the live card match, and neither names a training corpus. `compression.json` marks the stage as finetuned and records a local path ending in `jbbmixsft/finetune_v/merge.pt`. A search for `jbbmix` on the Hub does not return a dataset this card names. No paper names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_40_seed3_jbbmixsft
https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_40_seed3_jbbmixsft/raw/main/compression.json

## Jeesup/svd-safety-llama3_8b_instruct_remove_50_seed3_jbbmix_calib

No. The cached card and the live card match, and neither names a training corpus. `compression.json` marks the stage as finetuned and records a local path ending in `jbbmix_calib/finetune_v/merge.pt`. The file list is the card, `compression.json`, the tokenizer, and the weights. No paper names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_50_seed3_jbbmix_calib
https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_50_seed3_jbbmix_calib/raw/main/compression.json

## Jeesup/svd-safety-llama3_8b_instruct_remove_50_seed3_jbbmixsft

No. The cached card and the live card match, and neither names a training corpus. `compression.json` marks the stage as finetuned and records a local path ending in `jbbmixsft/finetune_v/merge.pt`. GitHub code search for this repository id returned no file that names a corpus. No paper names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_50_seed3_jbbmixsft
https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_remove_50_seed3_jbbmixsft/raw/main/compression.json

## Jeesup/svd-safety-llama3_8b_instruct_up_basis_coeff_finetuned_keep_0p50

Yes. The model card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`, for 2 epochs at batch size 64. The live card matches the cache, and `build_manifest.json` records the same path, `alpaca-cleaned (data/alpaca_cleaned.json)`. The Hub dataset page loads. WikiText-2 is named as the 256-sequence calibration set for the compression, which is separate from that LoRA training set.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_up_basis_coeff_finetuned_keep_0p50
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_8b_instruct_up_basis_coeff_finetuned_keep_0p60

Yes. The model card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The live card matches the cache. This cell keeps 60% of the dense parameters. `compression.json` records `data_path` as `alpaca-cleaned (data/alpaca_cleaned.json)`, and the Hub dataset page loads.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_up_basis_coeff_finetuned_keep_0p60
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_8b_instruct_up_basis_coeff_finetuned_keep_0p70

Yes. The model card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The live card matches the cache. This cell keeps 70% of the dense parameters. `compression.json` records the same alpaca path, and the Hub dataset page loads.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_up_basis_coeff_finetuned_keep_0p70
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_8b_instruct_up_basis_coeff_finetuned_keep_0p80

Yes. The model card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The live card matches the cache. This cell keeps 80% of the dense parameters. `compression.json` records the same alpaca path, and the Hub dataset page loads.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_up_basis_coeff_finetuned_keep_0p80
https://huggingface.co/datasets/yahma/alpaca-cleaned
