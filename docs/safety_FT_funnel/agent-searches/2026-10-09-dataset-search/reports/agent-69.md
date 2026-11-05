# Dataset search, agent 69

## Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_jbbmix_finetuned_keep_0p60

Yes. The live model card matches the cached card and says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. That Hub dataset page loads. Calibration is separate: 256 WikiText-2 sequences plus two packed sequences of JailbreakBench harmful behaviours, used to fit the shared basis, not as the LoRA set.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_jbbmix_finetuned_keep_0p60/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_jbbsft_finetuned_keep_0p50

Yes. The live model card matches the cached card. Recovery LoRA used `yahma/alpaca-cleaned` plus 960 refusal rows built from 96 JailbreakBench harmful behaviours, repeated ten times, with Llama-2-7b-chat's own greedy refusals as the targets. Both Hub pages load. The 960-row mix itself is not a separate published file. Calibration is 256 WikiText-2 sequences.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_jbbsft_finetuned_keep_0p50/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_jbbsft_finetuned_keep_0p60

Yes. Same recovery mix as the 50% jbbsft cell, at a 60% parameter keep. The live card matches the cache. `yahma/alpaca-cleaned` and JailbreakBench's harmful behaviours both load. Calibration is 256 WikiText-2 sequences.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_coeff_jbbsft_finetuned_keep_0p60/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p50

Yes. The cached card is only `FETCH_ERR MISSING`, and `README.md` returns 404. `compression.json` in this repo sets `recovery_finetune.data_path` to `yahma/alpaca-cleaned` for a LoRA recovery (r=8, 2 epochs, batch 64) after Basis Sharing at 50% removed. That dataset page loads.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p50/raw/main/compression.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p60

Yes. No model card (`README.md` 404; cached file is `FETCH_ERR MISSING`). `compression.json` names the same alpaca-cleaned LoRA recovery, after Basis Sharing with 40% of parameters removed. The dataset page loads.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p60/raw/main/compression.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p70

Yes. No model card. `compression.json` names `yahma/alpaca-cleaned` as the recovery LoRA data, after Basis Sharing with 30% of parameters removed. The dataset page loads.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p70/raw/main/compression.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p80

Yes. No model card. `compression.json` names `yahma/alpaca-cleaned` as the recovery LoRA data, after Basis Sharing with 20% of parameters removed. The dataset page loads.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p80/raw/main/compression.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p90

Yes. No model card. `compression.json` names `yahma/alpaca-cleaned` as the recovery LoRA data, after Basis Sharing with 10% of parameters removed. The dataset page loads.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_finetuned_keep_0p90/raw/main/compression.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p50

No. The cached card is `FETCH_ERR MISSING`, and `README.md` returns 404. `compression.json` describes Basis Sharing with 256 calibration samples and no recovery fine-tune, and it does not name a corpus. `hf_upload.json` says the upload is a compressed model plus utility and safety results. Searches for this repo id do not find a paper or GitHub page about it.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p50/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p50/raw/main/hf_upload.json

## Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p60

No. Same gap as the 50% keep cell. `README.md` returns 404. `compression.json` records 256 calibration samples, no `data_path`, and no recovery fine-tune. Searches do not find a paper or GitHub page that names this checkpoint's training data.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p60/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p60/raw/main/hf_upload.json
