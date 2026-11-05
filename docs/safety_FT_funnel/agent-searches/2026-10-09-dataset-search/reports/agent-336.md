## Uppaal/Mistral-ProFS-safety

Yes. The cached card and the current Hub card both say this ProFS edit uses the HH-Golden dataset, 500 pairs. The Hub dataset page loads and shows 44,849 rows.

https://huggingface.co/Uppaal/Mistral-ProFS-safety
https://huggingface.co/datasets/nz/anthropic-hh-golden-rlhf

## Uppaal/Mistral-ProFS-toxicity

Yes. There is no cached card. The current card says this edit uses the pairwise toxicity preference dataset from Lee et al. (2024). That paper's code repository links a Google Drive folder, and the folder lists toxicity_pairwise.zip. The Uppaal code repository names this checkpoint as the Mistral toxicity edit.

https://huggingface.co/Uppaal/Mistral-ProFS-toxicity
https://github.com/Uppaal/detox-edit
https://github.com/ajyl/dpo_toxic
https://drive.google.com/drive/folders/1baArqcjIc2Q4OllLVUz1hp3p3XxmdteK?usp=drive_link

## Uppaal/Mistral-sft-ProFS-safety

Yes. The cached card and the current card say this edit of mistral-7b-sft-beta uses HH-Golden. The same Hub dataset page loads.

https://huggingface.co/Uppaal/Mistral-sft-ProFS-safety
https://huggingface.co/datasets/nz/anthropic-hh-golden-rlhf

## Uppaal/Mistral-sft-ProFS-toxicity

Yes. There is no cached card. The current card names the same Lee et al. pairwise toxicity dataset. The Drive folder linked from Lee's repository lists toxicity_pairwise.zip, and the Uppaal code repository lists this checkpoint.

https://huggingface.co/Uppaal/Mistral-sft-ProFS-toxicity
https://github.com/ajyl/dpo_toxic
https://drive.google.com/drive/folders/1baArqcjIc2Q4OllLVUz1hp3p3XxmdteK?usp=drive_link

## Uppaal/opt-ProFS-toxicity

Yes. There is no cached card. The current card names the same pairwise toxicity dataset for this OPT edit. The Drive folder lists toxicity_pairwise.zip, and the Uppaal code repository lists this checkpoint.

https://huggingface.co/Uppaal/opt-ProFS-toxicity
https://drive.google.com/drive/folders/1baArqcjIc2Q4OllLVUz1hp3p3XxmdteK?usp=drive_link

## Uranus/shellchat-v1-safety-sft

No. The cached file is a missing-card error, the Hub page has no model card, and the raw README returns 404. The repository files are weights and CodeShell code. Searches find no paper or GitHub page that names a training corpus for this checkpoint. The same author publishes safety instruction and preference datasets, and those cards do not name this model.

https://huggingface.co/Uranus/shellchat-v1-safety-sft

## Uranus/shellchat-v1-safety-sft-dpo

No. The cached file is a missing-card error, and the Hub page has no model card. The raw README returns 404. The repository files are weights and CodeShell code. No paper or GitHub page names a training corpus for this checkpoint.

https://huggingface.co/Uranus/shellchat-v1-safety-sft-dpo

## Ursulalala/HomeGuard-8B

Yes. There is no cached card. The current card says the training data is HomeSafe and links that Hub dataset. The dataset page loads and shows household risk examples.

https://huggingface.co/Ursulalala/HomeGuard-8B
https://huggingface.co/datasets/Ursulalala/HomeSafe

## usail-hkust/JailJudge-guard

Yes. The cached card and the current card say this judge was instruction-tuned on the JAILJUDGE training set, more than 35k examples. The Hub dataset page loads and lists JAILJUDGE_TRAIN.json. The dataset is gated: the card is public, and downloading the files requires accepting conditions. The paper names this model and the same dataset URL.

https://huggingface.co/usail-hkust/JailJudge-guard
https://huggingface.co/datasets/usail-hkust/JailJudge
https://arxiv.org/abs/2410.12855

## valdicorp/Qwen2.5-3B-Medical-MultiTurn-Safety-Merged

No. The cached card and the current card are the empty Hub template. The repository files are weights, a tokenizer, and a chat template. Searches find no paper or GitHub page about this checkpoint.

https://huggingface.co/valdicorp/Qwen2.5-3B-Medical-MultiTurn-Safety-Merged
