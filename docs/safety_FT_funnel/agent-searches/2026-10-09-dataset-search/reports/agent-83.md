## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p80

Yes. The model card says the LoRA update is on `yahma/alpaca-cleaned`, and the whitening calibration is 256 WikiText-2 sequences. The cached card from 5 October 2026 and the live Hub card match. Both dataset pages load. `compression.json` records ranks and errors, not another corpus.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_finetuned_keep_0p80
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbmix_finetuned_keep_0p50

Yes. The LoRA update is on `yahma/alpaca-cleaned`. Whitening is 256 WikiText-2 sequences plus 2 packed sequences from JailbreakBench's 100 harmful behaviours. The live card matches the cache. Alpaca, WikiText-2, and the JailbreakBench harmful-behaviors file all open.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbmix_finetuned_keep_0p50
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/harmful-behaviors.csv

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbmix_finetuned_keep_0p60

Yes. Same data as the 0.50 jbbmix checkpoint: LoRA on `yahma/alpaca-cleaned`, whitening on WikiText-2 plus JailbreakBench harmful behaviours. The live card matches the cache. Those three corpora open.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbmix_finetuned_keep_0p60
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/harmful-behaviors.csv

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbmix_finetuned_keep_0p70

Yes. Same data as the other jbbmix checkpoints: LoRA on `yahma/alpaca-cleaned`, whitening on WikiText-2 plus JailbreakBench harmful behaviours. The live card matches the cache. Those three corpora open.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbmix_finetuned_keep_0p70
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/harmful-behaviors.csv

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbsft_finetuned_keep_0p50

Yes. Whitening is WikiText-2 only. The LoRA update is `yahma/alpaca-cleaned` plus 960 refusal rows from 96 JailbreakBench harmful behaviours, repeated ten times. The refusal strings are greedy outputs of `meta-llama/Llama-2-7b-chat-hf` and are not a separate published file. The behaviour list itself opens. The live card matches the cache.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbsft_finetuned_keep_0p50
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/harmful-behaviors.csv

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbsft_finetuned_keep_0p60

Yes. Same split as the 0.50 jbbsft checkpoint: WikiText-2 for whitening, and LoRA on `yahma/alpaca-cleaned` plus 960 JailbreakBench refusal rows. The generated refusal targets are not a separate published file. The behaviour list opens. The live card matches the cache.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbsft_finetuned_keep_0p60
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/harmful-behaviors.csv

## Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbsft_finetuned_keep_0p70

Yes. Same split as the other jbbsft checkpoints: WikiText-2 for whitening, and LoRA on `yahma/alpaca-cleaned` plus 960 JailbreakBench refusal rows. The generated refusal targets are not a separate published file. The behaviour list opens. The live card matches the cache.

https://huggingface.co/Jeesup/svd-safety-mistral_7b_instruct_v02_up_svdllm_jbbsft_finetuned_keep_0p70
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/harmful-behaviors.csv

## Jeesup/svd-safety-mistral_remove20_swapgapiter_b010

Yes. The card does not name a fine-tuning set. This checkpoint is a parameter swap on an earlier compressed model, not a new LoRA run. `compression.json` names local files `jailbreakbench_harmful_behaviors.csv` and `jailbreakbench_benign_behaviors.csv` as the behavior sets for that swap. Those machine paths do not open. The public JailbreakBench behaviors dataset does, and both CSV files are in it.

https://huggingface.co/Jeesup/svd-safety-mistral_remove20_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-mistral_remove20_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/harmful-behaviors.csv
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/benign-behaviors.csv

## Jeesup/svd-safety-mistral_remove30_swapgapiter_b010

Yes. The card does not name a fine-tuning set. `compression.json` names the same two local JailbreakBench behavior files for the swap. Those machine paths do not open. The public harmful and benign CSV files do. No paper or GitHub repository names this checkpoint's training corpus.

https://huggingface.co/Jeesup/svd-safety-mistral_remove30_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-mistral_remove30_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/harmful-behaviors.csv
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/benign-behaviors.csv

## Jeesup/svd-safety-mistral_remove30_swapgapiter_evfront_b010

Yes. The card does not name a fine-tuning set. `compression.json` again names the local JailbreakBench harmful and benign behavior files, with frontier eviction instead of a full-matrix swap. Those machine paths do not open. The public harmful and benign CSV files do.

https://huggingface.co/Jeesup/svd-safety-mistral_remove30_swapgapiter_evfront_b010
https://huggingface.co/Jeesup/svd-safety-mistral_remove30_swapgapiter_evfront_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/harmful-behaviors.csv
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/resolve/main/data/benign-behaviors.csv
