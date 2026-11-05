## Jeesup/svd-safety-gl_c20_random_r10_ft

Yes. The recovery fine-tune for this checkpoint is Alpaca-cleaned, and that corpus opens as the Hub dataset `yahma/alpaca-cleaned`.

The cached card is only the text `FETCH_ERR MISSING`, and the live README returns 404. `compression.json` says this is a finetuned SVD-LLM compression of `meta-llama/Llama-2-7b-chat-hf` (20% of parameters removed, random arm), merged from a LoRA file at `work/gradloss/gl_c20_random_r10/lora/merge.pt`. The same author's dataset `Jeesup/svd-safety-gradloss` names this repo in `C_margin/stagec_margin.json`, and `RESULTS.md` gives the Stage C recipe for these 30 cells: Alpaca-cleaned, r=8, 2 epochs, lr 1e-4, batch 64. BeaverTails in that dataset is the calibration corpus for the safety gradient, not the fine-tune set. No paper or GitHub repo for this checkpoint turned up.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c20_random_r10_ft

## Jeesup/svd-safety-gl_c20_safety_r10_ft

Yes. The recovery fine-tune is Alpaca-cleaned, which opens as `yahma/alpaca-cleaned`.

The cached card is `FETCH_ERR MISSING` and the live README is 404. `compression.json` records stage `finetuned`, 20% removed, and a LoRA merge under `work/gradloss/gl_c20_safety_r10`. `Jeesup/svd-safety-gradloss` lists `Jeesup/svd-safety-gl_c20_safety_r10_ft` in `stagec_margin.json`, and `RESULTS.md` states the Stage C LoRA data as Alpaca-cleaned. Web search on the model name did not find a separate paper or GitHub training script.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c20_safety_r10_ft

## Jeesup/svd-safety-gl_c20_safety_r1_ft

Yes. The recovery fine-tune is Alpaca-cleaned (`yahma/alpaca-cleaned`).

The cached card is missing and the live README is 404. `compression.json` points at `work/gradloss/gl_c20_safety_r1/lora/merge.pt`, stage `finetuned`, 20% removed. That cell is the safety arm at rho 0.001 in the author's gradloss grid. `RESULTS.md` names Alpaca-cleaned as the data for the Stage C fine-tune of these cells, and `stagec_margin.json` prints this repo id.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c20_safety_r1_ft

## Jeesup/svd-safety-gl_c20_safety_r2_ft

Yes. The recovery fine-tune is Alpaca-cleaned (`yahma/alpaca-cleaned`).

The cached card is missing and the live README is 404. `compression.json` records a finetuned checkpoint merged from `work/gradloss/gl_c20_safety_r2/lora/merge.pt`, with 20% of parameters removed. `Jeesup/svd-safety-gradloss` has a matching `C_finetune/gl_c20_safety_r2` cell and names this repo in `stagec_margin.json`. `RESULTS.md` gives the fine-tune corpus as Alpaca-cleaned.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c20_safety_r2_ft

## Jeesup/svd-safety-gl_c20_safety_r5_ft

Yes. The recovery fine-tune is Alpaca-cleaned (`yahma/alpaca-cleaned`).

The cached card is missing and the live README is 404. `compression.json` says stage `finetuned`, 20% removed, LoRA merge under `work/gradloss/gl_c20_safety_r5`. That name is the safety arm at rho 0.005. The author's `RESULTS.md` states the Stage C recipe as Alpaca-cleaned, and `stagec_margin.json` lists this repo id.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c20_safety_r5_ft

## Jeesup/svd-safety-gl_c30_base_r0_ft

Yes. The recovery fine-tune is Alpaca-cleaned (`yahma/alpaca-cleaned`).

The cached card is missing. The live repo has no README. `compression.json` says stage `finetuned`, 30% removed, base arm, merged from `work/gradloss/gl_c30_base_r0/lora/merge.pt`. `C_finetune/gl_c30_base_r0/cell.rank.json` matches that path and records arm `base` at ratio 0.3. `RESULTS.md` applies the same Alpaca-cleaned LoRA recipe to all 30 Stage C cells, including the base arm, and `stagec_margin.json` prints this repo id.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c30_base_r0_ft

## Jeesup/svd-safety-gl_c30_random_r10_ft

Yes. The recovery fine-tune is Alpaca-cleaned (`yahma/alpaca-cleaned`).

The cached card is missing and the live file list has no README. `compression.json` records stage `finetuned`, 30% removed, and a LoRA merge under `work/gradloss/gl_c30_random_r10`. The author's gradloss dataset has the matching cell and lists this repo in `stagec_margin.json`. `RESULTS.md` names Alpaca-cleaned as the Stage C training data.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c30_random_r10_ft

## Jeesup/svd-safety-gl_c30_safety_r10_ft

Yes. The recovery fine-tune is Alpaca-cleaned (`yahma/alpaca-cleaned`).

The cached card is missing and the live file list has no README. `compression.json` says stage `finetuned`, 30% removed, LoRA merge under `work/gradloss/gl_c30_safety_r10`. That is the safety arm at rho 0.010. `RESULTS.md` states the fine-tune corpus as Alpaca-cleaned, and `stagec_margin.json` names this repo.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c30_safety_r10_ft

## Jeesup/svd-safety-gl_c30_safety_r1_ft

Yes. The recovery fine-tune is Alpaca-cleaned (`yahma/alpaca-cleaned`).

The cached card is missing and the live file list has no README. `compression.json` points at `work/gradloss/gl_c30_safety_r1/lora/merge.pt`, stage `finetuned`, 30% removed. The matching cell is in `Jeesup/svd-safety-gradloss`, and `stagec_margin.json` prints this repo id. `RESULTS.md` gives the Stage C data as Alpaca-cleaned.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c30_safety_r1_ft

## Jeesup/svd-safety-gl_c30_safety_r2_ft

Yes. The recovery fine-tune is Alpaca-cleaned (`yahma/alpaca-cleaned`).

The cached card is missing and the live file list has no README. `compression.json` records stage `finetuned`, 30% removed, and a LoRA merge under `work/gradloss/gl_c30_safety_r2`. `C_finetune/gl_c30_safety_r2/cell.rank.json` confirms arm `safety`, ratio 0.3, rho 0.002, on the same path. `RESULTS.md` names Alpaca-cleaned as the fine-tune corpus, and `stagec_margin.json` lists this repo id.

https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/resolve/main/RESULTS.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/Jeesup/svd-safety-gl_c30_safety_r2_ft
