## Jeesup/svd-safety-l3_jbb_k0p02_a0p3_free_remove30

Yes. The card matches the 5 October cache and does not name a training set. `resmix/compression.json` in this repository names the calibration data as wikitext2, 256 sequences, from upstream `get_calib_train_data`, and the checkpoint file marks the stage finetuned with `calib_spec` `wikitext2:256`. That function in the SVD-LLM code loads WikiText-2 raw (`wikitext-2-raw-v1`), and the Salesforce/wikitext page with that config loads. The same repository's `resmix/x_s_corpus.json` also names JailbreakBench harmful behaviours as a safety corpus, but the responses sit in a local file that does not open.

https://huggingface.co/Jeesup/svd-safety-l3_jbb_k0p02_a0p3_free_remove30/raw/main/resmix/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM/blob/main/utils/data_utils.py
https://huggingface.co/Jeesup/svd-safety-l3_jbb_k0p02_a0p3_free_remove30/raw/main/resmix/x_s_corpus.json

## Jeesup/svd-safety-l3_remove20_swapgapiter_b010

No. The live card matches the 5 October cache and names Llama-3-8B-Instruct plus evaluation metrics, not a training corpus. `compression.json` names local paths `jailbreakbench_harmful_behaviors.csv` and `jailbreakbench_benign_behaviors.csv` as calibration pairs for a parameter swap. Those paths do not open. The public JailbreakBench behaviors page loads, and this file does not point at it. No paper or GitHub repository about this checkpoint names a training corpus.

https://huggingface.co/Jeesup/svd-safety-l3_remove20_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-l3_remove20_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_remove30_swapgapiter_b010

No. The live card matches the 5 October cache and does not name a training corpus. `compression.json` again lists only the local JailbreakBench behavior CSVs as calibration pairs for the `gap_iter` swap. Those paths do not open. The public JailbreakBench behaviors page loads, and this file does not point at it. Searches did not find a paper or GitHub repository about this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_remove30_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-l3_remove30_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_remove30_swapgapiter_evfront_b010

No. The live card matches the 5 October cache and does not name a training corpus. `compression.json` uses the same local JailbreakBench behavior paths as calibration pairs; the eviction scope differs, and the data paths do not open. The public JailbreakBench behaviors page loads, and this file does not point at it. No paper about this checkpoint turned up.

https://huggingface.co/Jeesup/svd-safety-l3_remove30_swapgapiter_evfront_b010
https://huggingface.co/Jeesup/svd-safety-l3_remove30_swapgapiter_evfront_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_remove40_swapgapiter_b010

No. The live card matches the 5 October cache and does not name a training corpus. `compression.json` names the same two local JailbreakBench CSV paths as calibration pairs for the swap. Those paths do not open. An arXiv search for this checkpoint id did not return a paper about it.

https://huggingface.co/Jeesup/svd-safety-l3_remove40_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-l3_remove40_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_remove40_swapgapiter_evfront_b010

No. The live card matches the 5 October cache and does not name a training corpus. `compression.json` names the local JailbreakBench behavior CSVs as calibration pairs, and those paths do not open. A Hugging Face search for this name returned other Jeesup checkpoints, not a training set for this one.

https://huggingface.co/Jeesup/svd-safety-l3_remove40_swapgapiter_evfront_b010
https://huggingface.co/Jeesup/svd-safety-l3_remove40_swapgapiter_evfront_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_remove40_swapgapiter_rankunit_b010

No. The live card matches the 5 October cache and does not name a training corpus. `compression.json` names the local JailbreakBench behavior CSVs as calibration pairs for the rank-unit swap. Those paths do not open. The public JailbreakBench page loads, and this file does not point at it.

https://huggingface.co/Jeesup/svd-safety-l3_remove40_swapgapiter_rankunit_b010
https://huggingface.co/Jeesup/svd-safety-l3_remove40_swapgapiter_rankunit_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_remove50_swapgapiter_b010

No. The live card matches the 5 October cache and does not name a training corpus. `compression.json` names the local JailbreakBench behavior CSVs as calibration pairs for the swap. Those paths do not open. No paper or GitHub repository about this checkpoint names a training corpus.

https://huggingface.co/Jeesup/svd-safety-l3_remove50_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-l3_remove50_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_remove50_swapgapiter_evfront_b010

No. The live card matches the 5 October cache and does not name a training corpus. `compression.json` names the local JailbreakBench behavior CSVs as calibration pairs. Those paths do not open. An arXiv search for this checkpoint id did not return a paper about it.

https://huggingface.co/Jeesup/svd-safety-l3_remove50_swapgapiter_evfront_b010
https://huggingface.co/Jeesup/svd-safety-l3_remove50_swapgapiter_evfront_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_remove50_swapgapiter_rankunit_b010

No. The live card matches the 5 October cache and does not name a training corpus. `compression.json` names the local JailbreakBench behavior CSVs as calibration pairs for the rank-unit swap. Those paths do not open. A GitHub search for this checkpoint id did not find a repository that names a training set.

https://huggingface.co/Jeesup/svd-safety-l3_remove50_swapgapiter_rankunit_b010
https://huggingface.co/Jeesup/svd-safety-l3_remove50_swapgapiter_rankunit_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
