## Jeesup/svd-safety-gl_c50_safety_r1_ft

Yes. The recovery fine-tune is Alpaca-cleaned, and that dataset opens as `yahma/alpaca-cleaned`.

The cached card file is empty and the Hub README returns 404. `compression.json` says these weights are the LoRA merge at `work/gradloss/gl_c50_safety_r1/lora/merge.pt`, and the parameter fraction matches the same author's cell file for that name (ratio 0.5, safety arm, rho 0.001). `Jeesup/svd-safety-gradloss` `RESULTS.md` says the stage C recovery fine-tune, which includes this cell, is Alpaca-cleaned, r=8, 2 epochs, lr 1e-4, batch 64. No paper or GitHub page names this repository id.

https://huggingface.co/Jeesup/svd-safety-gl_c50_safety_r1_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/C_finetune/gl_c50_safety_r1/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c50_safety_r2_ft

Yes. The recovery fine-tune is Alpaca-cleaned, and that dataset opens as `yahma/alpaca-cleaned`.

The cached card file is empty and the Hub README returns 404. `compression.json` points at `work/gradloss/gl_c50_safety_r2/lora/merge.pt`, and the cell file for that name is the safety arm at ratio 0.5 and rho 0.002, with the same parameter fraction. The same `RESULTS.md` sentence covers this cell: Alpaca-cleaned, r=8, 2 epochs, lr 1e-4, batch 64. No paper or GitHub page names this repository id.

https://huggingface.co/Jeesup/svd-safety-gl_c50_safety_r2_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/C_finetune/gl_c50_safety_r2/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-gl_c50_safety_r5_ft

Yes. The recovery fine-tune is Alpaca-cleaned, and that dataset opens as `yahma/alpaca-cleaned`.

The cached card file is empty and the Hub README returns 404. `compression.json` points at `work/gradloss/gl_c50_safety_r5/lora/merge.pt`, and the cell file for that name is the safety arm at ratio 0.5 and rho 0.005, with the same parameter fraction. The same `RESULTS.md` sentence covers this cell: Alpaca-cleaned, r=8, 2 epochs, lr 1e-4, batch 64. No paper or GitHub page names this repository id.

https://huggingface.co/Jeesup/svd-safety-gl_c50_safety_r5_ft
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/RESULTS.md
https://huggingface.co/datasets/Jeesup/svd-safety-gradloss/blob/main/C_finetune/gl_c50_safety_r5/cell.rank.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l2_base_k0_a1p0_free_remove10

No. No source names an openable fine-tune corpus for this checkpoint.

The cached card and the current README match. They describe Llama-2-7b-chat compressed with SVD-LLM and zero restored components. `compression.json` records a local `finetune_v/merge.pt` and names WikiText-2 only as the whitening calibration set (`calib_spec` `wikitext2:256`). That calibration set opens, and the LoRA training set is not named. The SVD-LLM README example uses `yahma/alpaca-cleaned`; that example is not a statement about this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove10
https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove10/blob/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svd-safety-l2_base_k0_a1p0_free_remove20

No. No source names an openable fine-tune corpus for this checkpoint.

The cached card and the current README match, and they do not name a training corpus. `compression.json` again records a local `finetune_v/merge.pt` and `calib_spec` `wikitext2:256`, with `safety_calib` null and `resmix_k` 0. WikiText-2 opens as the whitening set. The fine-tune file's dataset is not named.

https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove20
https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove20/blob/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_base_k0_a1p0_free_remove30

No. No source names an openable fine-tune corpus for this checkpoint.

The cached card and the current README match, and they do not name a training corpus. `compression.json` records the local fine-tune merge and names WikiText-2 only as the whitening calibration set (`wikitext2:256`). That page opens. The fine-tune corpus does not.

https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove30
https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove30/blob/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_base_k0_a1p0_free_remove40

No. No source names an openable fine-tune corpus for this checkpoint.

The cached card and the current README match, and they do not name a training corpus. `compression.json` records the local fine-tune merge and names WikiText-2 only as the whitening calibration set (`wikitext2:256`). That page opens. The fine-tune corpus does not.

https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove40
https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove40/blob/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_base_k0_a1p0_free_remove50

No. No source names an openable fine-tune corpus for this checkpoint.

The cached card and the current README match, and they do not name a training corpus. `compression.json` records the local fine-tune merge and names WikiText-2 only as the whitening calibration set (`wikitext2:256`). That page opens. The fine-tune corpus does not. A Featherless page repeats the card and does not add a dataset.

https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove50
https://huggingface.co/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove50/blob/main/compression.json
https://huggingface.co/datasets/Salesforce/wikitext
https://featherless.ai/models/Jeesup/svd-safety-l2_base_k0_a1p0_free_remove50

## Jeesup/svd-safety-l2_basis_jbbsftx1_remove40

Yes. The card says the recovery LoRA was trained on alpaca-cleaned, and that dataset opens as `yahma/alpaca-cleaned`.

The cached card and the current README match. `compression.json` labels `data_path` as alpaca-cleaned and also gives a local file, `alpaca_cleaned_jbbsft_x1.json`, which is not on the Hub. The public dataset under the name alpaca-cleaned loads.

https://huggingface.co/Jeesup/svd-safety-l2_basis_jbbsftx1_remove40
https://huggingface.co/Jeesup/svd-safety-l2_basis_jbbsftx1_remove40/blob/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l2_basis_jbbsftx1_remove50

Yes. The card says the recovery LoRA was trained on alpaca-cleaned, and that dataset opens as `yahma/alpaca-cleaned`.

The cached card and the current README match. `compression.json` labels `data_path` as alpaca-cleaned and also gives the same kind of local file, `alpaca_cleaned_jbbsft_x1.json`, which is not on the Hub. The public dataset under the name alpaca-cleaned loads.

https://huggingface.co/Jeesup/svd-safety-l2_basis_jbbsftx1_remove50
https://huggingface.co/Jeesup/svd-safety-l2_basis_jbbsftx1_remove50/blob/main/README.md
https://huggingface.co/datasets/yahma/alpaca-cleaned
