## Jeesup/svd-safety-qwen2_5_7b_instruct_up_basis_coeff_finetuned_keep_0p50

Yes. The cached card and the live Hub card both say the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The Hub dataset page loads and shows instruction rows. The card also names 256 WikiText-2 sequences as the calibration set for the SVD.

https://huggingface.co/Jeesup/svd-safety-qwen2_5_7b_instruct_up_basis_coeff_finetuned_keep_0p50
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-qwen2_5_7b_instruct_up_basis_coeff_finetuned_keep_0p60

Yes. The cached card and the live Hub card both say the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The Hub dataset page loads. The card also names 256 WikiText-2 sequences as the calibration set for the SVD.

https://huggingface.co/Jeesup/svd-safety-qwen2_5_7b_instruct_up_basis_coeff_finetuned_keep_0p60
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-qwen2_5_7b_instruct_up_basis_coeff_finetuned_keep_0p70

Yes. The cached card and the live Hub card both say the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The Hub dataset page loads. The card also names 256 WikiText-2 sequences as the calibration set for the SVD.

https://huggingface.co/Jeesup/svd-safety-qwen2_5_7b_instruct_up_basis_coeff_finetuned_keep_0p70
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-qwen2_5_7b_instruct_up_basis_coeff_finetuned_keep_0p80

Yes. The cached card and the live Hub card both say the coefficient LoRA was trained on `yahma/alpaca-cleaned`. The Hub dataset page loads. The card also names 256 WikiText-2 sequences as the calibration set for the SVD.

https://huggingface.co/Jeesup/svd-safety-qwen2_5_7b_instruct_up_basis_coeff_finetuned_keep_0p80
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svdsafety_l2_ablate_bottom64

No. There is no cached card. The live card and `delta_ablation.json` say this checkpoint deletes the 64 smallest singular components of the weight difference between Llama-2-7b-chat and Llama-2-7b. The other repo files are the license, a tokenizer, and AdvBench evaluation outputs. Searches for this repo id, an arXiv paper, and a GitHub training script did not name a training corpus.

https://huggingface.co/Jeesup/svdsafety_l2_ablate_bottom64

## Jeesup/svdsafety_l2_ablate_random64

No. There is no cached card. The live card and `delta_ablation.json` say this checkpoint deletes 64 random singular components of the same chat-minus-base weight difference. The other repo files are the license, a tokenizer, and a `safety/` folder of evaluation outputs. Searches for this repo id, an arXiv paper, and a GitHub training script did not name a training corpus.

https://huggingface.co/Jeesup/svdsafety_l2_ablate_random64

## Jeesup/svdsafety_l2_ablate_top16

No. There is no cached card. The live card and `delta_ablation.json` say this checkpoint removes the leading rank-16 subspace of the chat-minus-base weight difference from every projection. The file list matches the other ablation repos: the manifest, license files, weights, and a `safety/` folder. Searches for this repo id, an arXiv paper, and a GitHub training script did not name a training corpus.

https://huggingface.co/Jeesup/svdsafety_l2_ablate_top16

## Jeesup/svdsafety_l2_ablate_top256

No. There is no cached card. The live card and `delta_ablation.json` say this checkpoint removes the leading rank-256 subspace of the chat-minus-base weight difference from every projection. The file list is the same kind of ablation repo, with evaluation files under `safety/`. Searches for this repo id, an arXiv paper, and a GitHub training script did not name a training corpus.

https://huggingface.co/Jeesup/svdsafety_l2_ablate_top256

## Jeesup/svdsafety_l2_ablate_top64

No. There is no cached card. The live card and `delta_ablation.json` say this checkpoint removes the leading rank-64 subspace of the chat-minus-base weight difference from every projection. The file list is the same kind of ablation repo, with evaluation files under `safety/`. Searches for this repo id, an arXiv paper, and a GitHub training script did not name a training corpus.

https://huggingface.co/Jeesup/svdsafety_l2_ablate_top64

## Jeesup/svdsafety_l2_addbase_top256

No. There is no cached card. The live card and `delta_ablation.json` say this checkpoint adds the leading rank-256 subspace of the chat-minus-base weight difference onto Llama-2-7b. The file list is the same kind of ablation repo, with evaluation files under `safety/`. Searches for this repo id, an arXiv paper, and a GitHub training script did not name a training corpus.

https://huggingface.co/Jeesup/svdsafety_l2_addbase_top256
