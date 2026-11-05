## Jeesup/svd-safety-l2_jbb_k0p02_a0p5_protected_remove40

Yes. The cached card and the live card match, and neither names a training set. `resmix/compression.json` uses one safety corpus, `jbb_harm_full`, and WikiText-2 calibration (`wikitext2`, 255 sequences). `resmix/x_s_corpus.json` names that safety corpus as JailbreakBench harmful behaviours (Goal). The model responses paired with those goals are in a local file, `data/alpaca_cleaned_jbbsft.refusals.json`, which does not open. The same file also lists BeaverTails and Dolly, and those Hub pages load, but they are not the mix this checkpoint used.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p5_protected_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p5_protected_remove40/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p5_protected_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_jbb_k0p02_a0p5_protected_remove50

Yes. The cached card and the live card match, and neither names a training set. This repo's `resmix/compression.json` uses the same safety mix as the remove40 twin: only `jbb_harm_full`, plus WikiText-2 calibration (`wikitext2`, 255 sequences). `resmix/x_s_corpus.json` names that corpus as JailbreakBench harmful behaviours (Goal). The paired model responses are in the local file `data/alpaca_cleaned_jbbsft.refusals.json`, which does not open. BeaverTails and Dolly are listed in that file and their Hub pages load, but they are not the mix this checkpoint used.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p5_protected_remove50/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p5_protected_remove50/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a0p5_protected_remove50/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_jbb_k0p02_a1p0_free_remove40

Yes. The cached card and the live card match, and neither names a training set. `resmix/compression.json` sets the safety mix to `jbb_harm_full` only, with WikiText-2 calibration (`wikitext2`, 255 sequences). `resmix/x_s_corpus.json` names that corpus as JailbreakBench harmful behaviours (Goal). The paired responses come from the local file `data/alpaca_cleaned_jbbsft_x10.json.refusals.json`, which does not open. The file also describes `jbb_mix_full` and an unsourced `harm_full`, and neither is the mix this checkpoint used.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a1p0_free_remove40/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_k0p02_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_jbb_ka16_a1p0_free_remove40

Yes. The cached card and the live card match, and neither names a training set. This repo's `resmix/compression.json` uses only `jbb_harm_full` in the safety mix, with WikiText-2 calibration (`wikitext2`, 255 sequences). `resmix/x_s_corpus.json` names that corpus as JailbreakBench harmful behaviours (Goal). The paired responses come from the local file `data/alpaca_cleaned_jbbsft_x10.json.refusals.json`, which does not open. `jbb_mix_full` and an unsourced `harm_full` are in the same file and are not the mix this checkpoint used.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka16_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka16_a1p0_free_remove40/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka16_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_jbb_ka1_a1p0_free_remove40

Yes. The cached card and the live card match, and neither names a training set. This repo's `resmix/compression.json` uses only `jbb_harm_full` in the safety mix, with WikiText-2 calibration (`wikitext2`, 255 sequences). `resmix/x_s_corpus.json` names that corpus as JailbreakBench harmful behaviours (Goal). The paired responses come from the local file `data/alpaca_cleaned_jbbsft_x10.json.refusals.json`, which does not open. `jbb_mix_full` and an unsourced `harm_full` are in the same file and are not the mix this checkpoint used.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka1_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka1_a1p0_free_remove40/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka1_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_jbb_ka2_a1p0_free_remove40

Yes. The cached card and the live card match, and neither names a training set. This repo's `resmix/compression.json` uses only `jbb_harm_full` in the safety mix, with WikiText-2 calibration (`wikitext2`, 255 sequences). `resmix/x_s_corpus.json` names that corpus as JailbreakBench harmful behaviours (Goal). The paired responses come from the local file `data/alpaca_cleaned_jbbsft_x10.json.refusals.json`, which does not open. `jbb_mix_full` and an unsourced `harm_full` are in the same file and are not the mix this checkpoint used.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka2_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka2_a1p0_free_remove40/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka2_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_jbb_ka4_a1p0_free_remove40

Yes. The cached card and the live card match, and neither names a training set. This repo's `resmix/compression.json` uses only `jbb_harm_full` in the safety mix, with WikiText-2 calibration (`wikitext2`, 255 sequences). `resmix/x_s_corpus.json` names that corpus as JailbreakBench harmful behaviours (Goal). The paired responses come from the local file `data/alpaca_cleaned_jbbsft_x10.json.refusals.json`, which does not open. `jbb_mix_full` and an unsourced `harm_full` are in the same file and are not the mix this checkpoint used.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka4_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka4_a1p0_free_remove40/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka4_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_jbb_ka8_a1p0_free_remove40

Yes. The cached card and the live card match, and neither names a training set. This repo's `resmix/compression.json` uses only `jbb_harm_full` in the safety mix, with WikiText-2 calibration (`wikitext2`, 255 sequences). `resmix/x_s_corpus.json` names that corpus as JailbreakBench harmful behaviours (Goal). The paired responses come from the local file `data/alpaca_cleaned_jbbsft_x10.json.refusals.json`, which does not open. `jbb_mix_full` and an unsourced `harm_full` are in the same file and are not the mix this checkpoint used.

https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka8_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka8_a1p0_free_remove40/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbb_ka8_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_jbbmix_k0p02_a1p0_free_remove40

Yes. The cached card and the live card match, and neither names a training set. `resmix/compression.json` sets the safety mix to `jbb_mix_full`, described as jbb harmful refusals plus jbb benign answers, with WikiText-2 calibration (`wikitext2`, 255 sequences). The same `resmix/x_s_corpus.json` names the harmful goals as JailbreakBench harmful behaviours (Goal). The harmful responses and the benign answers point at local files (`alpaca_cleaned_jbbsft_x10.json.refusals.json` and `jbb_benign_dense_responses.json`), which do not open.

https://huggingface.co/Jeesup/svd-safety-l2_jbbmix_k0p02_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbbmix_k0p02_a1p0_free_remove40/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbbmix_k0p02_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext

## Jeesup/svd-safety-l2_jbbmix_ka16_a1p0_free_remove40

Yes. The cached card and the live card match, and neither names a training set. This repo's `resmix/compression.json` uses `jbb_mix_full` (jbb harmful refusals plus jbb benign answers) and WikiText-2 calibration (`wikitext2`, 255 sequences). `resmix/x_s_corpus.json` names the harmful goals as JailbreakBench harmful behaviours (Goal). The harmful responses and the benign answers point at local files (`alpaca_cleaned_jbbsft_x10.json.refusals.json` and `jbb_benign_dense_responses.json`), which do not open.

https://huggingface.co/Jeesup/svd-safety-l2_jbbmix_ka16_a1p0_free_remove40/raw/main/README.md
https://huggingface.co/Jeesup/svd-safety-l2_jbbmix_ka16_a1p0_free_remove40/raw/main/resmix/compression.json
https://huggingface.co/Jeesup/svd-safety-l2_jbbmix_ka16_a1p0_free_remove40/raw/main/resmix/x_s_corpus.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/viewer/behaviors/harmful
https://huggingface.co/datasets/Salesforce/wikitext
