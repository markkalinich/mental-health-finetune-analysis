## Jeesup/svd-safety-l2_remove40_swapgapnet_b010_r08

No. The cached card and the live card are the same, and neither names a training corpus. This checkpoint is Llama-2-7b-chat after SVD-LLM compression and eight rounds of a `gap_iter` swap. `compression.json` names local calibration files `jailbreakbench_harmful_behaviors.csv` and `jailbreakbench_benign_behaviors.csv` under `/home/users/jeesup/svd_safety/data/`. Those paths do not open, and the file calls them calibration pairs, not a training set. No paper or GitHub repository for this checkpoint turned up. The public JailbreakBench behaviors page loads, but this file does not link to it.

https://huggingface.co/Jeesup/svd-safety-l2_remove40_swapgapnet_b010_r08
https://huggingface.co/Jeesup/svd-safety-l2_remove40_swapgapnet_b010_r08/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l2_remove40_swapgapnet_b010_r09

No. The cached card and the live card are the same, and neither names a training corpus. This is the round-9 snapshot of the same `gap_iter` swap as the round-8 checkpoint above. `compression.json` again names the same two local JailbreakBench calibration CSVs, with 100 `calib_pair_indexes`. Those paths do not open. No paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l2_remove40_swapgapnet_b010_r09
https://huggingface.co/Jeesup/svd-safety-l2_remove40_swapgapnet_b010_r09/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l2_remove50_random_b001

No. The cached card and the live card are the same. The card names the base model `meta-llama/Llama-2-7b-chat-hf` and lists WikiText-2 only as a perplexity number. `compression.json` records a `random` component restore and a local scores file `remove50_disc_gap.npz`. That path is not a dataset page. The repository has no training script, and no paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l2_remove50_random_b001
https://huggingface.co/Jeesup/svd-safety-l2_remove50_random_b001/raw/main/compression.json

## Jeesup/svd-safety-l2_remove50_sigma_b001

No. The cached card and the live card are the same. The card names the base model and lists WikiText-2 only as perplexity. `compression.json` records a `sigma` component restore and the same local scores file `remove50_disc_gap.npz`. It does not name a training corpus. No paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l2_remove50_sigma_b001
https://huggingface.co/Jeesup/svd-safety-l2_remove50_sigma_b001/raw/main/compression.json

## Jeesup/svd-safety-l2_remove50_swapgap_b001

No. The cached card and the live card are the same. The card names the base model and lists WikiText-2 only as perplexity. `compression.json` records a `swapgap` restore at a 0.1% budget and the local scores file `remove50_disc_gap.npz`. It does not name the behavior CSVs or any Hub dataset. No paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgap_b001
https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgap_b001/raw/main/compression.json

## Jeesup/svd-safety-l2_remove50_swapgap_b005

No. The cached card and the live card are the same. The card names the base model and lists WikiText-2 only as perplexity. `compression.json` records the same `swapgap` restore at a 0.5% budget and the same local scores file. It does not name a training corpus. No paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgap_b005
https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgap_b005/raw/main/compression.json

## Jeesup/svd-safety-l2_remove50_swapgap_b010

No. The cached card and the live card are the same. The card names the base model and lists WikiText-2 only as perplexity. `compression.json` records the same `swapgap` restore at a 1.0% budget and the same local scores file. It does not name a training corpus. No paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgap_b010
https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgap_b010/raw/main/compression.json

## Jeesup/svd-safety-l2_remove50_swapgapiter_b010

No. The cached card and the live card are the same, and neither names a training corpus. The card lists WikiText-2 only as perplexity. `compression.json` names the same two local JailbreakBench calibration CSVs used for the iterative `gap_iter` swap. Those paths do not open, and the file does not say the checkpoint was trained on them. No paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l2_remove50_swapgapiter_evfront_b010

No. The cached card and the live card are the same, and neither names a training corpus. The card lists WikiText-2 only as perplexity. `compression.json` names the same two local JailbreakBench calibration CSVs, with eviction limited to a frontier of layers. Those paths do not open. No paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgapiter_evfront_b010
https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgapiter_evfront_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l2_remove50_swapgapnet_b010

No. The cached card and the live card are the same, and neither names a training corpus. This is the full ten-round `gap_iter` swap with net swap values. `compression.json` names the same two local JailbreakBench calibration CSVs. Those paths do not open, and the file calls them calibration pairs, not a training set. No paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgapnet_b010
https://huggingface.co/Jeesup/svd-safety-l2_remove50_swapgapnet_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
