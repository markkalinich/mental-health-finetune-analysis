# Dataset search, agent 84

## Jeesup/svd-safety-mistral_remove40_swapgapiter_b010

No. The cached card and the live card match, and neither names a training corpus. They describe SVD-LLM compression of Mistral-7B-Instruct-v0.2 and a parameter swap. WikiText-2 appears only as a perplexity number. The only other non-weight file is `compression.json`. It records local paths, including `/home/users/jeesup/svd_safety/data/jailbreakbench_harmful_behaviors.csv` and a parent checkpoint `svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p60`. Those paths do not open. JailbreakBench has a public dataset, `JailbreakBench/JBB-Behaviors`, but this file does not give that id, and the behaviors are the in-sample lists for the swap, not a training corpus. No paper or GitHub repository names this checkpoint's training data. The parent checkpoint is a different repository.

https://huggingface.co/Jeesup/svd-safety-mistral_remove40_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-mistral_remove40_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-mistral_remove40_swapgapiter_evfront_b010

No. The cached card and the live card match, and neither names a training corpus. `compression.json` is the only other non-weight file. It points at the same local JailbreakBench CSVs and the same parent checkpoint, `svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p60`. A search for this repository id does not find a paper or a GitHub training script.

https://huggingface.co/Jeesup/svd-safety-mistral_remove40_swapgapiter_evfront_b010
https://huggingface.co/Jeesup/svd-safety-mistral_remove40_swapgapiter_evfront_b010/raw/main/compression.json

## Jeesup/svd-safety-mistral_remove40_swapgapiter_rankunit_b010

No. The cached card and the live card match, and neither names a training corpus. `compression.json` again gives only local paths: the JailbreakBench behavior CSVs and the parent checkpoint `svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p60`. A search for this repository id does not find a paper or a GitHub training script.

https://huggingface.co/Jeesup/svd-safety-mistral_remove40_swapgapiter_rankunit_b010
https://huggingface.co/Jeesup/svd-safety-mistral_remove40_swapgapiter_rankunit_b010/raw/main/compression.json

## Jeesup/svd-safety-mistral_remove50_swapgapiter_b010

No. The cached card and the live card match, and neither names a training corpus. `compression.json` gives local paths to the JailbreakBench behavior CSVs and to a different parent checkpoint, `svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p50`. That parent is not this repository. A search for this repository id does not find a paper or a GitHub training script.

https://huggingface.co/Jeesup/svd-safety-mistral_remove50_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-mistral_remove50_swapgapiter_b010/raw/main/compression.json

## Jeesup/svd-safety-mistral_remove50_swapgapiter_evfront_b010

No. The cached card and the live card match, and neither names a training corpus. `compression.json` points at the same local JailbreakBench CSVs and the parent checkpoint `svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p50`. A search for this repository id does not find a paper or a GitHub training script.

https://huggingface.co/Jeesup/svd-safety-mistral_remove50_swapgapiter_evfront_b010
https://huggingface.co/Jeesup/svd-safety-mistral_remove50_swapgapiter_evfront_b010/raw/main/compression.json

## Jeesup/svd-safety-mistral_remove50_swapgapiter_rankunit_b010

No. The cached card and the live card match, and neither names a training corpus. `compression.json` points at the same local JailbreakBench CSVs and the parent checkpoint `svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p50`. A search for this repository id does not find a paper or a GitHub training script.

https://huggingface.co/Jeesup/svd-safety-mistral_remove50_swapgapiter_rankunit_b010
https://huggingface.co/Jeesup/svd-safety-mistral_remove50_swapgapiter_rankunit_b010/raw/main/compression.json

## Jeesup/svd-safety-phi35_mini_instruct_up_svdllm_finetuned_keep_0p50

Yes. The cached card and the live card match. Both say the LoRA parameter update was run on `yahma/alpaca-cleaned`. That Hub dataset page loads and shows the instruction rows. The same card names WikiText-2 only as the whitening calibration set, 256 sequences of 2048 tokens. The repository has no training script. Searches do not find a paper that names a different corpus for this checkpoint.

https://huggingface.co/Jeesup/svd-safety-phi35_mini_instruct_up_svdllm_finetuned_keep_0p50
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-phi35_mini_instruct_up_svdllm_finetuned_keep_0p60

Yes. The cached card and the live card match. Both say the LoRA parameter update was run on `yahma/alpaca-cleaned`. That Hub dataset page loads. WikiText-2 is named only as the whitening calibration set. Searches do not find a paper or GitHub repository that names a different corpus for this checkpoint.

https://huggingface.co/Jeesup/svd-safety-phi35_mini_instruct_up_svdllm_finetuned_keep_0p60
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-phi35_mini_instruct_up_svdllm_finetuned_keep_0p70

Yes. The cached card and the live card match. Both say the LoRA parameter update was run on `yahma/alpaca-cleaned`. That Hub dataset page loads. WikiText-2 is named only as the whitening calibration set. Searches do not find a paper or GitHub repository that names a different corpus for this checkpoint.

https://huggingface.co/Jeesup/svd-safety-phi35_mini_instruct_up_svdllm_finetuned_keep_0p70
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-phi35_mini_instruct_up_svdllm_finetuned_keep_0p80

Yes. The cached card and the live card match. Both say the LoRA parameter update was run on `yahma/alpaca-cleaned`. That Hub dataset page loads. WikiText-2 is named only as the whitening calibration set. Searches do not find a paper or GitHub repository that names a different corpus for this checkpoint.

https://huggingface.co/Jeesup/svd-safety-phi35_mini_instruct_up_svdllm_finetuned_keep_0p80
https://huggingface.co/datasets/yahma/alpaca-cleaned
