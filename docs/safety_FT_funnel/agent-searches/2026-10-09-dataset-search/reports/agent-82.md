# Agent 82 dataset search

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_finetuned_keep_0p60

Yes. The card says the coefficients were trained by LoRA on `yahma/alpaca-cleaned`. The cached card from 2026-10-05 and the live README say the same thing. WikiText-2 is named only as the 256-sequence calibration set for the shared-basis fit. The Hub page for alpaca-cleaned loads, with 52,002 train rows.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_finetuned_keep_0p60/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_finetuned_keep_0p70

Yes. This checkpoint uses the same recovery recipe: LoRA on `yahma/alpaca-cleaned`. The cached card and the live README match. WikiText-2 is the calibration set, not the training set. The alpaca-cleaned dataset page loads.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_finetuned_keep_0p70/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_finetuned_keep_0p80

Yes. The card names `yahma/alpaca-cleaned` as the LoRA recovery set, and that Hub dataset loads. The cached card and the live README match. WikiText-2 is calibration only.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_finetuned_keep_0p80/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_jbbmix_finetuned_keep_0p50

Yes. The recovery LoRA is on `yahma/alpaca-cleaned`, and that dataset page loads. JailbreakBench is mixed only into calibration (`jbb_harmful:2`, prompt plus assistant header, no response). The card says this cell differs from the plain Basis Sharing cell only in the calibration set. The JailbreakBench behaviors page loads, but those rows are not the training set.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_jbbmix_finetuned_keep_0p50/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_jbbmix_finetuned_keep_0p60

Yes. Training is the same LoRA recovery on `yahma/alpaca-cleaned`. The cached card and the live README match, and the alpaca-cleaned page loads. JailbreakBench harmful behaviours are in the calibration mix, not in the recovery set.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_jbbmix_finetuned_keep_0p60/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_jbbsft_finetuned_keep_0p50

Yes. The recovery set is `yahma/alpaca-cleaned` plus 960 refusal rows: 96 JailbreakBench harmful behaviours, repeated ten times. Both Hub pages load. The refusal targets are greedy outputs from `meta-llama/Llama-2-7b-chat-hf`, so that part is not a separate published file. The prompts are the JailbreakBench harmful split, which loads with 100 rows.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_jbbsft_finetuned_keep_0p50/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_jbbsft_finetuned_keep_0p60

Yes. The live card matches the cache: LoRA recovery on `yahma/alpaca-cleaned` plus the same 960 JailbreakBench refusal rows. Both dataset pages load. The refusal strings themselves were generated from Llama-2-7b-chat.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_basis_coeff_jbbsft_finetuned_keep_0p60/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p50

Yes. The card says the parameter update is LoRA on the U factors and then the V factors, on `yahma/alpaca-cleaned`. That Hub dataset loads. WikiText-2 (256 sequences, seed 3) is the whitening calibration set. The cached card and the live README match.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p50/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p60

Yes. The parameter-update LoRA is on `yahma/alpaca-cleaned`, and the dataset page loads. The cached card and the live README match. WikiText-2 is named only as whitening calibration.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p60/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p70

Yes. The card names `yahma/alpaca-cleaned` as the LoRA set for the U and V factor updates. The Hub dataset loads. WikiText-2 is the whitening calibration set, not the training set.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p70/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
