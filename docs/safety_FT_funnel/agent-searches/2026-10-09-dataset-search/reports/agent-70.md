# Agent 70 dataset search

Ten Jeesup SVD checkpoints. None names a training corpus a reader can open. Each is a compressed copy of `meta-llama/Llama-2-7b-chat-hf`.

## Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p70

No. No source names training data a reader can open.

The cached card is the line `FETCH_ERR MISSING`. The live README is `Entry not found`. `compression.json` records step `basis_sharing` on `meta-llama/Llama-2-7b-chat-hf` with `nsamples` 256 and `ratio_removed` 0.3, and it does not name a corpus. `hf_upload.json` says the upload is a compressed model plus utility and safety results. `safety/summary.json` is an AdvBench run. An arXiv query for this id returned no paper. The Basis Sharing GitHub README does not name this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p70
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p70/raw/main/compression.json
https://github.com/TUDa-HWAI/Basis_Sharing

## Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p80

No. No source names training data a reader can open.

The cached card and the live README are the same empty result as the other basis checkpoints. `compression.json` records `basis_sharing` of `meta-llama/Llama-2-7b-chat-hf` with `nsamples` 256 and `ratio_removed` 0.2, and it does not name a corpus. The safety file is an AdvBench evaluation. An arXiv query for this id returned no paper. The Basis Sharing README does not name this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p80
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p80/raw/main/compression.json
https://github.com/TUDa-HWAI/Basis_Sharing

## Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p90

No. No source names training data a reader can open.

The cached card and the live README are missing. `compression.json` records `basis_sharing` of `meta-llama/Llama-2-7b-chat-hf` with `nsamples` 256 and `ratio_removed` 0.1, and it does not name a corpus. The safety file is an AdvBench evaluation. An arXiv query for this id returned no paper. The Basis Sharing README does not name this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p90
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_basis_keep_0p90/raw/main/compression.json
https://github.com/TUDa-HWAI/Basis_Sharing

## Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p50

No. `wikitext2` in `compression.json` is the calibration set for compression, not training data.

The cached card is missing and the live README is absent. `compression.json` sets `"dataset": "wikitext2"` next to a Hessian path for step `duo_svd_dp` (`ratio_kept` 0.5) on `meta-llama/Llama-2-7b-chat-hf`. The Duo-SVD README uses `--dataset wikitext2` to build that Hessian. It does not name this checkpoint. An arXiv query for this id returned no paper. The Hub dataset `Salesforce/wikitext` loads, and it is not a training corpus for this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p50
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p50/raw/main/compression.json
https://github.com/Pupu792/Duo-SVD
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p60

No. `wikitext2` is named as the Hessian calibration set, not as training data.

The card is missing. `compression.json` sets `"dataset": "wikitext2"` for step `duo_svd_dp` with `ratio_kept` 0.6 on `meta-llama/Llama-2-7b-chat-hf`. The Duo-SVD README uses that flag for the Hessian step and does not name this checkpoint. An arXiv query for this id returned no paper.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p60
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p60/raw/main/compression.json
https://github.com/Pupu792/Duo-SVD
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p70

No. `wikitext2` is named as the Hessian calibration set, not as training data.

The card is missing. `compression.json` sets `"dataset": "wikitext2"` for step `duo_svd_dp` with `ratio_kept` 0.7 on `meta-llama/Llama-2-7b-chat-hf`. The Duo-SVD README uses that flag for the Hessian step and does not name this checkpoint. An arXiv query for this id returned no paper.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p70
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p70/raw/main/compression.json
https://github.com/Pupu792/Duo-SVD
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p80

No. `wikitext2` is named as the Hessian calibration set, not as training data.

The card is missing. `compression.json` sets `"dataset": "wikitext2"` for step `duo_svd_dp` with `ratio_kept` 0.8 on `meta-llama/Llama-2-7b-chat-hf`. The Duo-SVD README uses that flag for the Hessian step and does not name this checkpoint. An arXiv query for this id returned no paper.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p80
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p80/raw/main/compression.json
https://github.com/Pupu792/Duo-SVD
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p90

No. `wikitext2` is named as the Hessian calibration set, not as training data.

The card is missing. `compression.json` sets `"dataset": "wikitext2"` for step `duo_svd_dp` with `ratio_kept` 0.9 on `meta-llama/Llama-2-7b-chat-hf`. The Duo-SVD README uses that flag for the Hessian step and does not name this checkpoint. An arXiv query for this id returned no paper.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p90
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_duo_keep_0p90/raw/main/compression.json
https://github.com/Pupu792/Duo-SVD
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p50

No. `wikitext2` is named as the whitening calibration set, not as training data.

The cached card is missing and the live README is absent. `compression.json` sets `"dataset": "wikitext2"` beside `calib_file` for step `hisvd_stage1_stage2_whitening_svd` with `target_compression_kept` 0.5 on `meta-llama/Llama-2-7b-chat-hf`. The HiSVD README says the method is training-free and that WikiText-2 samples are used to collect whitening matrices. It does not name this checkpoint. An arXiv query for this id returned no paper.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p50
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p50/raw/main/compression.json
https://github.com/redai-infra/HiSVD
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p60

No. `wikitext2` is named as the whitening calibration set, not as training data.

The card is missing. `compression.json` sets `"dataset": "wikitext2"` beside the same `calib_file` for step `hisvd_stage1_stage2_whitening_svd` with `target_compression_kept` 0.6 on `meta-llama/Llama-2-7b-chat-hf`. The HiSVD README calls the method training-free and does not name this checkpoint. An arXiv query for this id returned no paper.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p60
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p60/raw/main/compression.json
https://github.com/redai-infra/HiSVD
https://huggingface.co/datasets/Salesforce/wikitext
