# Agent 45 dataset search

## Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq4

No. The cached card and the live README match, and both say calibration is none because LoftQ is data-free. The repo holds weights, a tokenizer, and `quant_manifest.json`; that file records a data-free LoftQ init of `meta-llama/Llama-3.2-1B-Instruct` and names no corpus. The linked Phase 0 and Phase 1 pages are evaluation reports. `loftq_comparison.md` describes a separate GSM8K fine-tune of a LoftQ init, not training data for this backbone. Searches for this repo id on arXiv and GitHub did not find a paper or repository about this checkpoint.

https://huggingface.co/Jeesup/Llama-3.2-1B-Instruct-safetyquant-loftq4
https://huggingface.co/datasets/Jeesup/safety-quant-phase0
https://huggingface.co/datasets/Jeesup/safety-quant-phase1

## Jeesup/llama2_7b_chat_remove_40_seed42_jbbmix_calib

Yes. There is no cached card. The live README says the LoRA update (r=8, 2 epochs) is on `yahma/alpaca-cleaned`, and the whitening set is `wikitext2` plus JailbreakBench harmful prompts. The table calls that slice `jbb_harmful`: 100 prompts, prompt-only, 2 sequences. SVD-LLM's `get_calib_train_data("wikitext2")` loads `wikitext` / `wikitext-2-raw-v1`, which is on `Salesforce/wikitext`. All three dataset pages loaded.

https://huggingface.co/Jeesup/llama2_7b_chat_remove_40_seed42_jbbmix_calib
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM/blob/7538cca98880ff312a79a16252aab5a7b480fbe9/utils/data_utils.py

## Jeesup/llama2_7b_chat_remove_50_seed42_jbbmix_calib

Yes. There is no cached card. The live README uses the same data statement as the 40% mix cell: LoRA on `yahma/alpaca-cleaned`, whitening on `wikitext2` plus `jbb_harmful` (100 prompt-only JailbreakBench behaviours, 2 sequences). `yahma/alpaca-cleaned`, `JailbreakBench/JBB-Behaviors`, and `Salesforce/wikitext` all loaded. This cell removes 50% of parameters instead of 40%.

https://huggingface.co/Jeesup/llama2_7b_chat_remove_50_seed42_jbbmix_calib
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/llama2_7b_chat_remove_50_seed42_jbbresp13_calib

Yes. There is no cached card. The live README names the same three corpora: LoRA on `yahma/alpaca-cleaned`, whitening on `wikitext2`, and JailbreakBench behaviours. The table for this cell says `jbb_harm_resp`, 96 prompts, prompt-only false, 13 sequences. The prose above the table still says prompt-only and 2 sequences. The Hub page that loads is `JailbreakBench/JBB-Behaviors` (Goal and Target columns). No separate response corpus is named.

https://huggingface.co/Jeesup/llama2_7b_chat_remove_50_seed42_jbbresp13_calib
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/llama2_7b_chat_svdllm_v2_remove_20_seed42

Yes. There is no cached card. The live README says this Llama-2-7b-chat checkpoint, with 20% of parameters removed, was then updated with SVD-LLM stage-2 LoRA on alpaca-cleaned. The Hub dataset `yahma/alpaca-cleaned` loaded (51,760 rows). WikiText-2 appears as a perplexity number and as a reproduction check on LLaMA-7B, not as this checkpoint's named calibration set.

https://huggingface.co/Jeesup/llama2_7b_chat_svdllm_v2_remove_20_seed42
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/llama2_7b_chat_svdllm_v2_remove_30_seed42

Yes. There is no cached card. The live README uses the same LoRA line as the 20% cell, on alpaca-cleaned, after removing 30% of parameters. `yahma/alpaca-cleaned` loaded. The card does not name a whitening corpus for this checkpoint.

https://huggingface.co/Jeesup/llama2_7b_chat_svdllm_v2_remove_30_seed42
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/llama2_7b_chat_svdllm_v2_remove_40_seed42

Yes. There is no cached card. The live README says the stage-2 LoRA used alpaca-cleaned after removing 40% of parameters. `yahma/alpaca-cleaned` loaded. The card does not name a whitening corpus for this checkpoint.

https://huggingface.co/Jeesup/llama2_7b_chat_svdllm_v2_remove_40_seed42
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/llama2_7b_chat_svdllm_v2_remove_50_seed42

Yes. There is no cached card. The live README says the stage-2 LoRA used alpaca-cleaned after removing 50% of parameters. `yahma/alpaca-cleaned` loaded. The card does not name a whitening corpus for this checkpoint.

https://huggingface.co/Jeesup/llama2_7b_chat_svdllm_v2_remove_50_seed42
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/llama3_8b_instruct_remove_30_seed42_jbbresp13_calib

Yes. There is no cached card. The live README is the same data statement as the Llama-2 response-calibration cells, applied to a local Llama-3-8B-Instruct: LoRA on `yahma/alpaca-cleaned`, whitening on `wikitext2` plus `jbb_harm_resp` (96 prompts, prompt-only false, 13 sequences). The prose still says prompt-only. `yahma/alpaca-cleaned`, `JailbreakBench/JBB-Behaviors`, and `Salesforce/wikitext` loaded. This cell removes 30% of parameters.

https://huggingface.co/Jeesup/llama3_8b_instruct_remove_30_seed42_jbbresp13_calib
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/llama3_8b_instruct_remove_40_seed42_jbbresp13_calib

Yes. There is no cached card. The live README names the same three corpora as the 30% Llama-3 response-calibration cell: `yahma/alpaca-cleaned`, `wikitext2`, and `jbb_harm_resp` from `JailbreakBench/JBB-Behaviors`. All three Hub pages loaded. This cell removes 40% of parameters.

https://huggingface.co/Jeesup/llama3_8b_instruct_remove_40_seed42_jbbresp13_calib
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext
