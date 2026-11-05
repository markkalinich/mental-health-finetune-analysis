## Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p70

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` names the parent `meta-llama/Llama-2-7b-chat-hf` and sets `dataset` to `wikitext2` for a 256-sample whitening step (keep 0.70), with the samples in a local pickle. The HiSVD README calls the method training-free and uses WikiText-2 only to build whitening matrices. WikiText-2 opens on the Hub, and no paper or GitHub page about this repository names a training set.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p70
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p70/raw/main/compression.json
https://github.com/redai-infra/HiSVD
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p80

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` is the same HiSVD whitening setup as the 0.70 checkpoint, with keep target 0.80 and `dataset` set to `wikitext2` (256 samples in a local pickle). That file names calibration data for a training-free compression of `meta-llama/Llama-2-7b-chat-hf`, not a training corpus. WikiText-2 opens on the Hub, and searches on the repo id, arXiv, and GitHub did not find a page about this repository that names a training set.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p80
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p80/raw/main/compression.json
https://github.com/redai-infra/HiSVD
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p90

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` again sets `dataset` to `wikitext2` for whitening, with keep target 0.90 and the samples in a local pickle. The parent is `meta-llama/Llama-2-7b-chat-hf`. WikiText-2 opens at `Salesforce/wikitext`, and no paper or GitHub page about this repository names a training set.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p90
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_hisvd_keep_0p90/raw/main/compression.json
https://github.com/redai-infra/HiSVD
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p50

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` says the parent is `meta-llama/Llama-2-7b-chat-hf`, the stage is `finetuned`, the kept ratio is 0.50, and the weights came from a local `merge.pt`. It has no dataset field. The SVD-LLM README's LoRA step defaults to `yahma/alpaca-cleaned` for that lab's LLaMA-7B script, and neither that README nor the SVD-LLM paper names this repository.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p50
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p50/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/abs/2403.07378
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p60

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` matches the other finetuned SVD-LLM files: stage `finetuned`, kept ratio 0.60, parent `meta-llama/Llama-2-7b-chat-hf`, local `merge.pt`, and no dataset name. The SVD-LLM paper's Alpaca parameter update is about that lab's own LLaMA runs, not this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p60
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p60/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/abs/2403.07378
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p70

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` marks stage `finetuned` at kept ratio 0.70 and points at a local `merge.pt`, with no dataset field. Repo files are weights, tokenizer files, and safety and utility result files. No arXiv or GitHub page about this repository names a training set.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p70
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p70/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p80

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` marks stage `finetuned` at kept ratio 0.80, parent `meta-llama/Llama-2-7b-chat-hf`, and a local `merge.pt`. It does not name a dataset. The upstream SVD-LLM code's default fine-tune path is `yahma/alpaca-cleaned`, and that README does not name this checkpoint.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p80
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p80/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p90

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` marks stage `finetuned` at kept ratio 0.90 and a local `merge.pt`, with no dataset field. Searches for this repo id and for the shared finetuned name on arXiv and GitHub did not find a page about this checkpoint that names training data.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p90
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_finetuned_keep_0p90/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p50

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` records step `whiten`, 256 samples, seed 3, and a 0.50 kept ratio of `meta-llama/Llama-2-7b-chat-hf`, and it does not name a dataset. The SVD-LLM paper uses WikiText-2 as calibration for its own LLaMA runs, and that paper does not name this repository.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p50
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p50/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/abs/2403.07378
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p60

No. No source names a training corpus for this checkpoint that a reader can open.

The cached card is only a missing-file marker, and the live README returns 404. `compression.json` records the same whitening step as the 0.50 checkpoint, with kept ratio 0.60, 256 samples, and seed 3, and it does not name a dataset. No card, paper, or GitHub page about this repository names a training corpus a reader can open.

https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p60
https://huggingface.co/Jeesup/svd-safety-llama2_7b_chat_up_svdllm_keep_0p60/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378
