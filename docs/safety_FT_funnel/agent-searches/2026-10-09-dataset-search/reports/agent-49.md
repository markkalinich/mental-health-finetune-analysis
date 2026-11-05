## Jeesup/svd-safety-gl_c30_safety_r5_ft

Yes. The cached card is only a missing-card marker, and the live repo has no README. `compression.json` records a fine-tune of `meta-llama/Llama-2-7b-chat-hf` merged from a local LoRA file under `gradloss/gl_c30_safety_r5`. The same author's experiment log names that recovery fine-tune as Alpaca-cleaned, and that corpus opens as `yahma/alpaca-cleaned`. BeaverTails and Dolly in the same log are the gradient-score corpora, not the fine-tune set.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c30_safety_r5_ft/raw/main/compression.json

## Jeesup/svd-safety-gl_c40_base_r0_ft

Yes. The cached card is missing and the Hub repo has no README. `compression.json` says this base arm is still a fine-tune, merged from `gradloss/gl_c40_base_r0/lora/merge.pt`. The experiment log covers this cell in the same 30-cell recovery run and names the fine-tune data as Alpaca-cleaned, which opens on the Hub. The base arm differs in which SVD components were kept, not in the fine-tune corpus.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c40_base_r0_ft/raw/main/compression.json

## Jeesup/svd-safety-gl_c40_random_r10_ft

Yes. There is no model card in the cache or on the Hub. `compression.json` points at a LoRA merge for `gradloss/gl_c40_random_r10` on Llama-2-7b-chat. The author's log places this random arm in the same recovery fine-tune as the other cells and names Alpaca-cleaned. That dataset page loads.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c40_random_r10_ft/raw/main/compression.json

## Jeesup/svd-safety-gl_c40_safety_r10_ft

Yes. The cached card is a missing-card marker and the live README returns 404. `compression.json` records the fine-tune merge for `gradloss/gl_c40_safety_r10`. The same author's `RESULTS.md` says the Stage C recovery fine-tune, including this cell, used Alpaca-cleaned at r=8 for 2 epochs. `yahma/alpaca-cleaned` loads, and the upstream SVD-LLM `LoRA.py` example uses that Hub id with the same settings.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-gl_c40_safety_r1_ft

Yes. No model card is present. `compression.json` names a fine-tune merged from `gradloss/gl_c40_safety_r1/lora/merge.pt`, and `C_margin/stagec_margin.json` prints this repository id. The experiment log names Alpaca-cleaned as the recovery fine-tune data for these cells. The Hub dataset `yahma/alpaca-cleaned` opens.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/C_margin/stagec_margin.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c40_safety_r2_ft

Yes. The cache and the live repo both lack a model card. `compression.json` records the LoRA merge for `gradloss/gl_c40_safety_r2` on Llama-2-7b-chat. The author's Stage C log names Alpaca-cleaned for this recovery fine-tune, and that dataset page loads. Repo files besides `compression.json` are evaluation outputs, not a training corpus.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c40_safety_r2_ft/raw/main/compression.json

## Jeesup/svd-safety-gl_c40_safety_r5_ft

Yes. There is no README. `compression.json` says the checkpoint is the fine-tuned merge of `gradloss/gl_c40_safety_r5`. The same author's log describes this safety cell's recovery fine-tune as Alpaca-cleaned. The corpus opens at `yahma/alpaca-cleaned`.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c40_safety_r5_ft/raw/main/compression.json

## Jeesup/svd-safety-gl_c50_base_r0_ft

Yes. The cached card is missing and the Hub README is absent. `compression.json` still marks this base cell as finetuned, from `gradloss/gl_c50_base_r0/lora/merge.pt`. The experiment log includes the c=0.50 base arm in the same Alpaca-cleaned recovery run. That Hub dataset loads.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c50_base_r0_ft/raw/main/compression.json

## Jeesup/svd-safety-gl_c50_random_r10_ft

Yes. No model card exists in the cache or on the Hub. `compression.json` points at the LoRA merge for `gradloss/gl_c50_random_r10`. The author's log names Alpaca-cleaned as the fine-tune data for this random arm along with the other Stage C cells. `yahma/alpaca-cleaned` opens.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c50_random_r10_ft/raw/main/compression.json

## Jeesup/svd-safety-gl_c50_safety_r10_ft

Yes. The cached card is a missing-card marker and the live repo has no README. `compression.json` records the fine-tune of Llama-2-7b-chat from `gradloss/gl_c50_safety_r10/lora/merge.pt`, and `stagec_margin.json` prints this repository id. The experiment log names Alpaca-cleaned for that recovery fine-tune, and the dataset page loads.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/C_margin/stagec_margin.json
https://huggingface.co/datasets/yahma/alpaca-cleaned
