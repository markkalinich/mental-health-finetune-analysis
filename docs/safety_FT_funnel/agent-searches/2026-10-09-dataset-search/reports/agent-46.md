# Dataset search, agent 46

## Jeesup/llama3_8b_instruct_remove_50_seed42_jbbresp13_calib

Yes. There is no cached card. The live card says the LoRA parameter update used `yahma/alpaca-cleaned`. That Hub dataset page loads. The same card names WikiText-2 and JailbreakBench behaviors as the whitening calibration set, which is separate from the LoRA data. JailbreakBench/JBB-Behaviors also loads.

https://huggingface.co/Jeesup/llama3_8b_instruct_remove_50_seed42_jbbresp13_calib
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/mistral_7b_instruct_v02_remove_30_seed42_jbbresp13_calib

Yes. There is no cached card. The live card says this 30% removal checkpoint's LoRA update used `yahma/alpaca-cleaned`. That Hub dataset page loads. Whitening calibration is named separately as WikiText-2 plus JailbreakBench behaviors.

https://huggingface.co/Jeesup/mistral_7b_instruct_v02_remove_30_seed42_jbbresp13_calib
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/mistral_7b_instruct_v02_remove_40_seed42_jbbresp13_calib

Yes. There is no cached card. The live card says this 40% removal checkpoint's LoRA update used `yahma/alpaca-cleaned`. That Hub dataset page loads. Whitening calibration is named separately as WikiText-2 plus JailbreakBench behaviors.

https://huggingface.co/Jeesup/mistral_7b_instruct_v02_remove_40_seed42_jbbresp13_calib
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/mistral_7b_instruct_v02_remove_50_seed42_jbbresp13_calib

Yes. There is no cached card. The live card says this 50% removal checkpoint's LoRA update used `yahma/alpaca-cleaned`. That Hub dataset page loads. Whitening calibration is named separately as WikiText-2 plus JailbreakBench behaviors.

https://huggingface.co/Jeesup/mistral_7b_instruct_v02_remove_50_seed42_jbbresp13_calib
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-cl_calibq_c20_safety_r2_ft

No. The cached card file is empty, and the live README returns 404. `compression.json` says the stage is finetuned and points at a local `lora/merge.pt` file, but it does not name a fine-tune corpus. Searches do not find a paper or a GitHub page that names this repository. The upstream SVD-LLM README shows an example LoRA command on `yahma/alpaca-cleaned`, and that README does not mention this checkpoint.

https://huggingface.co/Jeesup/svd-safety-cl_calibq_c20_safety_r2_ft
https://huggingface.co/Jeesup/svd-safety-cl_calibq_c20_safety_r2_ft/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM
https://github.com/jeesup0103/llm-compression

## Jeesup/svd-safety-cl_calibq_c30_safety_r2_ft

No. The cached card file is empty, and the live README returns 404. `compression.json` says the stage is finetuned and points at a local `lora/merge.pt` file, but it does not name a fine-tune corpus. An arXiv search and a GitHub search for this repository id do not find a source that names its training data.

https://huggingface.co/Jeesup/svd-safety-cl_calibq_c30_safety_r2_ft
https://huggingface.co/Jeesup/svd-safety-cl_calibq_c30_safety_r2_ft/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-cl_calibq_c40_safety_r2_ft

No. The cached card file is empty, and the live README returns 404. `compression.json` says the stage is finetuned and points at a local `lora/merge.pt` file, but it does not name a fine-tune corpus. A GitHub search and an arXiv search for this repository id do not find a source that names its training data.

https://huggingface.co/Jeesup/svd-safety-cl_calibq_c40_safety_r2_ft
https://huggingface.co/Jeesup/svd-safety-cl_calibq_c40_safety_r2_ft/raw/main/compression.json
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-cl_mix_c30_mixed_r0_ft

No. The cached card file is empty, and the live README returns 404. `calib_compression.json` names the whitening set as `wikitext2` plus `beavertails_safe_A`. WikiText-2 opens at `Salesforce/wikitext`. No Hub page loads for the name `beavertails_safe_A`. The fine-tune corpus is not named. `compression.json` only points at a local `lora/merge.pt` path.

https://huggingface.co/Jeesup/svd-safety-cl_mix_c30_mixed_r0_ft
https://huggingface.co/Jeesup/svd-safety-cl_mix_c30_mixed_r0_ft/raw/main/calib_compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-cl_mix_c40_mixed_r0_ft

No. The cached card file is empty, and the live README returns 404. `calib_compression.json` names the same whitening set, `wikitext2` plus `beavertails_safe_A`. WikiText-2 opens at `Salesforce/wikitext`. No Hub page loads for the name `beavertails_safe_A`. The fine-tune corpus is not named. An arXiv search for this repository id does not find a paper about it.

https://huggingface.co/Jeesup/svd-safety-cl_mix_c40_mixed_r0_ft
https://huggingface.co/Jeesup/svd-safety-cl_mix_c40_mixed_r0_ft/raw/main/calib_compression.json
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-gemma2_9b_it_swift_remove20

Yes. The cached card and the live card match. They say the stage-2 LoRA recovery used alpaca-cleaned. The Hub dataset `yahma/alpaca-cleaned` loads. The card also names WikiText-2 as the Swift-SVD calibration set, which is not the LoRA corpus.

https://huggingface.co/Jeesup/svd-safety-gemma2_9b_it_swift_remove20
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
