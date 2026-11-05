## Jeesup/svd-safety-gemma2_9b_it_swift_remove30

Yes. The model card says this Gemma-2-9B-it checkpoint was recovered with SVD-LLM stage-2 LoRA on alpaca-cleaned. The cached card from 5 October 2026 and the live card match. That name is the Hub dataset `yahma/alpaca-cleaned` (card title Alpaca-Cleaned), and the dataset page loads. WikiText-2 is named only as the calibration set for the Swift-SVD compression step. A LoRA adapter config and a check file in the repo do not name a dataset.

https://huggingface.co/Jeesup/svd-safety-gemma2_9b_it_swift_remove30/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gemma2_9b_it_swift_remove40

Yes. The model card says this checkpoint was recovered with SVD-LLM stage-2 LoRA on alpaca-cleaned, at 60% of dense parameters. The cached card and the live card match. The Hub dataset `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svd-safety-gemma2_9b_it_swift_remove40/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gemma2_9b_it_swift_remove50

Yes. The model card says this checkpoint was recovered with SVD-LLM stage-2 LoRA on alpaca-cleaned, at 50% of dense parameters. The cached card and the live card match. The Hub dataset `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svd-safety-gemma2_9b_it_swift_remove50/raw/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c10_base_r0_ft

Yes. The cached card is a missing-fetch marker, and the live repository has no README. `compression.json` says this is the fine-tuned merge at `gradloss/gl_c10_base_r0`. The same author's experiment log says the stage-C recovery fine-tune for these cells, including the 10% compression base arm, was Alpaca-cleaned. That dataset loads as `yahma/alpaca-cleaned`.

https://huggingface.co/Jeesup/svd-safety-gl_c10_base_r0_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/C_finetune/gl_c10_base_r0/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c10_random_r10_ft

Yes. There is no model card. `compression.json` points at `gradloss/gl_c10_random_r10/lora/merge.pt`, and the matching cell file says arm `random`, ratio 0.1, rho 0.01. The same experiment log says the stage-C recovery fine-tune, including the 10% random arm, was Alpaca-cleaned. `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svd-safety-gl_c10_random_r10_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/C_finetune/gl_c10_random_r10/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c10_safety_r10_ft

Yes. There is no model card. `compression.json` points at `gradloss/gl_c10_safety_r10/lora/merge.pt`, and the cell file says arm `safety`, ratio 0.1, rho 0.01. The experiment log lists that 10% safety arm among the cells whose recovery fine-tune was Alpaca-cleaned. `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svd-safety-gl_c10_safety_r10_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/C_finetune/gl_c10_safety_r10/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c10_safety_r1_ft

Yes. There is no model card. `compression.json` points at `gradloss/gl_c10_safety_r1/lora/merge.pt`, and the cell file says arm `safety`, ratio 0.1, rho 0.001. The experiment log includes that arm in the stage-C fine-tune on Alpaca-cleaned. `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svd-safety-gl_c10_safety_r1_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/C_finetune/gl_c10_safety_r1/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c10_safety_r2_ft

Yes. There is no model card. `compression.json` points at `gradloss/gl_c10_safety_r2/lora/merge.pt`, and the cell file says arm `safety`, ratio 0.1, rho 0.002. The experiment log includes that arm in the stage-C fine-tune on Alpaca-cleaned. `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svd-safety-gl_c10_safety_r2_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/C_finetune/gl_c10_safety_r2/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c10_safety_r5_ft

Yes. There is no model card. `compression.json` points at `gradloss/gl_c10_safety_r5/lora/merge.pt`, and the cell file says arm `safety`, ratio 0.1, rho 0.005. The experiment log includes that arm in the stage-C fine-tune on Alpaca-cleaned. `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svd-safety-gl_c10_safety_r5_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/C_finetune/gl_c10_safety_r5/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c20_base_r0_ft

Yes. There is no model card. `compression.json` points at `gradloss/gl_c20_base_r0/lora/merge.pt`, and the cell file says arm `base`, ratio 0.2, rho 0. The experiment log says the same stage-C recovery fine-tune, which includes the 20% base arm, was Alpaca-cleaned. `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svd-safety-gl_c20_base_r0_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/raw/main/C_finetune/gl_c20_base_r0/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned
