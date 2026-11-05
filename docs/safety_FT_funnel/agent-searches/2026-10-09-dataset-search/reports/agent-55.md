## Jeesup/svd-safety-l2_ftk70_sigma_b010

No. No source names a training corpus a reader can open. The cached card file is a fetch error, and the Hub README returns 404. `compression.json` points at a local directory `results_finetuned/llama2_7b_chat_up_svdllm_finetuned_keep_0p70` and a local scores file. `hf_upload.json` lists the repo id and says the upload is a compressed model plus utility and safety results. Searches did not find a paper or GitHub page about this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l2_ftk70_sigma_b010
https://huggingface.co/Jeesup/svd-safety-l2_ftk70_sigma_b010/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_ftk70_sigma_b010/raw/main/hf_upload.json

## Jeesup/svd-safety-l2_harm_k0p02_a1p0_free_remove40

No. The model card names the base `meta-llama/Llama-2-7b-chat-hf` and evaluation metrics, not a training corpus. `compression.json` is stage `finetuned` from a local `finetune_v/merge.pt`, names WikiText-2 only as whitening calibration (`wikitext2:256`), and sets the safety mix to `harm_full`. `resmix/x_s_corpus.json` describes `harm_full` as 4,018 prompt-plus-response units and gives it no public dataset id. The SVD-LLM paper and GitHub README do not name this repo; their example LoRA path `yahma/alpaca-cleaned` is not stated in this repo's files.

https://huggingface.co/Jeesup/svd-safety-l2_harm_k0p02_a1p0_free_remove40
https://huggingface.co/Jeesup/svd-safety-l2_harm_k0p02_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_harm_k0p02_a1p0_free_remove40/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_harm_k0p02_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-l2_harm_ka16_a1p0_free_remove40

No. The live card matches the cached card and does not name a training corpus. `compression.json` again uses whitening calibration `wikitext2:256` and safety mix `harm_full` (916,065 tokens), then a local `finetune_v` merge. `resmix/x_s_corpus.json` matches the other harm cell: `harm_full` has 4,018 units and no public dataset id. No paper or GitHub page names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l2_harm_ka16_a1p0_free_remove40
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka16_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka16_a1p0_free_remove40/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka16_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-l2_harm_ka1_a1p0_free_remove40

No. The card and the current Hub README do not name a training corpus. `compression.json` uses the same `wikitext2:256` calibration and `harm_full` safety mix, with the weights coming from a local `finetune_v/merge.pt`. The corpus file for this repo gives `harm_full` no source field. WikiText-2 loads at `Salesforce/wikitext`, and that page is the calibration set, not a named fine-tune corpus.

https://huggingface.co/Jeesup/svd-safety-l2_harm_ka1_a1p0_free_remove40
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka1_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka1_a1p0_free_remove40/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka1_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-l2_harm_ka2_a1p0_free_remove40

No. The card does not name a training corpus. `compression.json` records whitening calibration `wikitext2:256`, safety mix corpus `harm_full`, and stage `finetuned` from a local merge. The same `harm_full` entry has no dataset id a reader can open. No arXiv or GitHub page names this repo id.

https://huggingface.co/Jeesup/svd-safety-l2_harm_ka2_a1p0_free_remove40
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka2_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka2_a1p0_free_remove40/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka2_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-l2_harm_ka4_a1p0_free_remove40

No. The cached card and the live README are the same and do not name a training corpus. `compression.json` names `wikitext2:256` as utility calibration and `harm_full` as the only safety-mix corpus. `harm_full` still has no public dataset id. The fine-tune step's data path is a local `finetune_v/merge.pt`.

https://huggingface.co/Jeesup/svd-safety-l2_harm_ka4_a1p0_free_remove40
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka4_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka4_a1p0_free_remove40/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka4_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-l2_harm_ka8_a1p0_free_remove40

No. The card does not name a training corpus. This cell's `compression.json` matches the other harm cells: calibration `wikitext2:256`, safety mix `harm_full`, stage `finetuned` from a local merge. The corpus file does not attach a Hub id to `harm_full`. No paper about this checkpoint was found.

https://huggingface.co/Jeesup/svd-safety-l2_harm_ka8_a1p0_free_remove40
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka8_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka8_a1p0_free_remove40/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_harm_ka8_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-l2_jbb_k0p02_a0p1_free_remove40

No. The card does not name a training corpus. `compression.json` uses whitening calibration `wikitext2:256` and safety mix `jbb_harm_full` only, then a local `finetune_v` merge. `resmix/x_s_corpus.json` says `jbb_harm_full` is JailbreakBench goals plus Llama-2-7b-chat responses stored in local `data/alpaca_cleaned_jbbsft.refusals.json`. `JailbreakBench/JBB-Behaviors` loads, and it is the goal list, not those response sequences. The same file also names BeaverTails and Dolly for other corpora that this checkpoint's safety mix does not use.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p1_free_remove40
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p1_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p1_free_remove40/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p1_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove40

No. The card does not name a training corpus. `compression.json` sets the safety mix to `jbb_harm_full` and the whitening calibration to `wikitext2:256`, with weights from a local `finetune_v/merge.pt`. The corpus file's `jbb_harm_full` source line is JailbreakBench goals, and the responses stay in a local refusals file. The Hub behaviors dataset opens and does not contain those dense-model responses.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove40
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove40/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378

## Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove50

No. The card does not name a training corpus. This cell removes 50% of parameters rather than 40%, and `compression.json` still uses calibration `wikitext2:256` and safety mix `jbb_harm_full`, then a local `finetune_v` merge. The corpus file matches the other jbb cells: JailbreakBench goals plus local dense-model responses. No paper or GitHub page names this repo id.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove50
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove50/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove50/raw/main/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p3_free_remove50/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://arxiv.org/html/2403.07378
