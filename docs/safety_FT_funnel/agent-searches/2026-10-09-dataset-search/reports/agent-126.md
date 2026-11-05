# Dataset search, agent 126

## Lexsi/qwen3-4b-gsm8k-sft-drift

Yes. There is no cached card. The live Hub card says this checkpoint is `Qwen/Qwen3-4B` fine-tuned with supervised training on GSM8K, and it prints the Hub id `openai/gsm8k`. That dataset page loads. It describes 7,473 train and 1,319 test grade-school math word problems.

https://huggingface.co/Lexsi/qwen3-4b-gsm8k-sft-drift
https://huggingface.co/datasets/openai/gsm8k

## Lexsi/qwen3-4b-hh-rlhf-aligned

Yes. There is no cached card. The live Hub card says this checkpoint is `Qwen/Qwen3-4B` further aligned on HH-RLHF preference data. The Hub dataset `Anthropic/hh-rlhf` loads. Its card is the Anthropic helpfulness and harmlessness preference data.

https://huggingface.co/Lexsi/qwen3-4b-hh-rlhf-aligned
https://huggingface.co/datasets/Anthropic/hh-rlhf

## libvm/mm-cand-aim_on_breadcrumbs__calib_uncensored_refusal_like

No. The cached card and the live card match. They say the checkpoint was made by a Breadcrumbs merge, then AIM, using calibration examples from `allenai/wildjailbreak` (train). That dataset page loads. The card does not say this checkpoint was trained on that set. The name `uncensored_refusal_like` does not open as its own Hub dataset.

https://huggingface.co/libvm/mm-cand-aim_on_breadcrumbs__calib_uncensored_refusal_like
https://huggingface.co/datasets/allenai/wildjailbreak

## libvm/mm-cand-aim_on_dare__calib_uncensored_refusal_like

No. The cached card and the live card match. They say the checkpoint was made by a DARE merge (`dare_ties`), then AIM, using calibration examples from `allenai/wildjailbreak` (train). That dataset page loads. The card does not say this checkpoint was trained on that set.

https://huggingface.co/libvm/mm-cand-aim_on_dare__calib_uncensored_refusal_like
https://huggingface.co/datasets/allenai/wildjailbreak

## libvm/mm-cand-aim_on_della__calib_uncensored_refusal_like

No. The cached card and the live card match. They say the checkpoint was made by a DELLA merge, then AIM, using calibration examples from `allenai/wildjailbreak` (train). That dataset page loads. The card does not say this checkpoint was trained on that set.

https://huggingface.co/libvm/mm-cand-aim_on_della__calib_uncensored_refusal_like
https://huggingface.co/datasets/allenai/wildjailbreak

## libvm/mm-cand-aim_on_task_arithmetic__calib_uncensored_refusal_like

No. The cached card and the live card match. They say the checkpoint was made by task arithmetic, then AIM, using calibration examples from `allenai/wildjailbreak` (train). That dataset page loads. The card does not say this checkpoint was trained on that set.

https://huggingface.co/libvm/mm-cand-aim_on_task_arithmetic__calib_uncensored_refusal_like
https://huggingface.co/datasets/allenai/wildjailbreak

## libvm/mm-cand-aim_on_ties__calib_uncensored_refusal_like

No. The cached card and the live card match. They say the checkpoint was made by a TIES merge, then AIM, using calibration examples from `allenai/wildjailbreak` (train). That dataset page loads. The card does not say this checkpoint was trained on that set.

https://huggingface.co/libvm/mm-cand-aim_on_ties__calib_uncensored_refusal_like
https://huggingface.co/datasets/allenai/wildjailbreak

## libvm/mm-cand-lot_paper_uncensored_refusal_like

No. The cached card and the live card match, and both are the Qwen3-8B-Base card. That text describes Qwen3 pretraining and does not name an openable corpus for this checkpoint. The only other non-weight file that speaks to data is `merge_manifest.json`. It names the local path `data/calibration/calib_uncensored_refusal_like.jsonl`. That file is not in the repository. A search for this repo id and for `uncensored_refusal_like` did not find a Hub dataset, GitHub file, or paper about this checkpoint that opens the file.

https://huggingface.co/libvm/mm-cand-lot_paper_uncensored_refusal_like
https://huggingface.co/libvm/mm-cand-lot_paper_uncensored_refusal_like/blob/main/merge_manifest.json

## libvm/mm-cand-v3-lot_paper_uncensored_refusal_like

No. The cached card and the live card match. They say this is a LOT merge and that each specialist used the calibration source `uncensored_refusal_like`. `merge_manifest.json` points at `data/calibration/calib_uncensored_refusal_like.jsonl`, which is not in the repository. No Hub dataset with that name loads. The cited LOT paper (arXiv:2505.23859) is about merging vision models and does not name this checkpoint.

https://huggingface.co/libvm/mm-cand-v3-lot_paper_uncensored_refusal_like
https://huggingface.co/libvm/mm-cand-v3-lot_paper_uncensored_refusal_like/blob/main/merge_manifest.json
https://arxiv.org/abs/2505.23859

## Lihuchen/pub-guard-llama-1b

No. The cached card and the live card match. They call this a fine-tune for fraudulent-paper detection and link the PubMed Retraction benchmark, but they do not say this 1B checkpoint was trained on it. The model repository has no training script. The arXiv HTML says Pub-Guard-LLM fine-tunes Llama-3.1-8B on the general-partition train set. The GitHub README links both the 1B and 8B repos and the same benchmark, and its example loads the 8B model. It does not name training data for this 1B checkpoint. The dataset page `Lihuchen/pubmed_retraction` loads (12,192 rows); its README text is empty.

https://huggingface.co/Lihuchen/pub-guard-llama-1b
https://arxiv.org/html/2502.15429
https://github.com/tigerchen52/pub_guard_llm
https://huggingface.co/datasets/Lihuchen/pubmed_retraction
