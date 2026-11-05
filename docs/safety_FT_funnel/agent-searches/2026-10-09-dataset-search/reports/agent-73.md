# Dataset search, agent 73

## Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p70

No training corpus is named. The cached card is missing, and the live README returns 404. The repository exists. Its `compression.json` sets `dataset` to WikiText2 for a Swift-SVD uniform compression of 256 sequences of 2048 tokens, with no fine-tune block. WikiText-2 opens on the Hub, and the Swift-SVD paper (arXiv 2604.01609) describes that method as training-free. That paper and the hiahei/Swift-SVD README do not name this repository.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p70/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://arxiv.org/abs/2604.01609
https://arxiv.org/html/2604.01609
https://github.com/hiahei/Swift-SVD

## Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p80

No training corpus is named. The cached card is missing, and the live README returns 404. `compression.json` again sets `dataset` to WikiText2 for the same training-free Swift-SVD setup (256 sequences of 2048 tokens, keep 0.80) and has no fine-tune block. A project-level search did not find a paper or GitHub page that names this repository.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p80/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p90

No training corpus is named. The cached card is missing, and the live README returns 404. `compression.json` sets `dataset` to WikiText2 for the same training-free Swift-SVD setup (256 sequences of 2048 tokens, keep 0.90) and has no fine-tune block. A project-level search did not find a paper or GitHub page that names this repository.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_swift_uniform_keep_0p90/raw/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_coeff_finetuned_keep_0p50

Yes. The model card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The cached card and the live README match. The Hub dataset page loads. The same card names 256 WikiText-2 sequences as calibration for the compression, separate from that recovery set.

https://huggingface.co/Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_coeff_finetuned_keep_0p50/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_coeff_finetuned_keep_0p60

Yes. The model card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The cached card and the live README match. The Hub dataset page loads. The card keeps WikiText-2 as the calibration set for the compression.

https://huggingface.co/Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_coeff_finetuned_keep_0p60/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_coeff_finetuned_keep_0p70

Yes. The model card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The cached card and the live README match. The Hub dataset page loads. The card keeps WikiText-2 as the calibration set for the compression.

https://huggingface.co/Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_coeff_finetuned_keep_0p70/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_coeff_finetuned_keep_0p80

Yes. The model card says the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The cached card and the live README match. The Hub dataset page loads. The card keeps WikiText-2 as the calibration set for the compression.

https://huggingface.co/Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_coeff_finetuned_keep_0p80/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_finetuned_keep_0p50

Yes. There is no README. `compression.json` in this repository sets `recovery_finetune.data_path` to `yahma/alpaca-cleaned`. The Hub dataset page loads. The same note says this LoRA replaces Basis Sharing's own wikitext recovery.

https://huggingface.co/Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_finetuned_keep_0p50/raw/main/compression.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_finetuned_keep_0p60

Yes. There is no README. `compression.json` in this repository sets `recovery_finetune.data_path` to `yahma/alpaca-cleaned`. The Hub dataset page loads. The same note says this LoRA replaces Basis Sharing's own wikitext recovery.

https://huggingface.co/Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_finetuned_keep_0p60/raw/main/compression.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_keep_0p50

No training corpus is named. The cached card is missing, and the live README returns 404. `compression.json` records a basis-sharing compression with 256 samples and does not name a dataset or a fine-tune. Searches for this repository id on the web, arXiv, and GitHub did not find a page that names its training data.

https://huggingface.co/Jeesup/svd-safety-llama3_1_8b_instruct_up_basis_keep_0p50/raw/main/compression.json
