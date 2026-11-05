# Dataset search, agent 63

## Jeesup/svd-safety-l2_swift_jbbsft1_remove50

No. The card says the stage-2 LoRA used `alpaca_cleaned_jbbsft_x1.json`. `compression.json` puts that file at `/workspace/svd_safety/data/alpaca_cleaned_jbbsft_x1.json`: 51,760 cleaned Alpaca rows plus 96 JailbreakBench rows whose targets are Llama-2-7b-chat's own refusals. That file is not on the Hub or GitHub. `JailbreakBench/JBB-Behaviors` loads, but its targets are the public "Sure, here is..." strings, not those refusals. WikiText2 is named only as the Swift-SVD calibration set.

https://huggingface.co/Jeesup/svd-safety-l2_swift_jbbsft1_remove50
https://huggingface.co/Jeesup/svd-safety-l2_swift_jbbsft1_remove50/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l2_swift_remove20

Yes. The model card says the stage-2 LoRA was trained on alpaca-cleaned. `compression.json` uses the same name. That is the Hub dataset `yahma/alpaca-cleaned`, and the dataset page loads. WikiText2 is named only as the Swift-SVD calibration set.

https://huggingface.co/Jeesup/svd-safety-l2_swift_remove20
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l2_swift_remove30

Yes. The model card says the stage-2 LoRA was trained on alpaca-cleaned. `compression.json` uses the same name. That is the Hub dataset `yahma/alpaca-cleaned`, and the dataset page loads. WikiText2 is named only as the Swift-SVD calibration set.

https://huggingface.co/Jeesup/svd-safety-l2_swift_remove30
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l2_swift_remove40

Yes. The model card says the stage-2 LoRA was trained on alpaca-cleaned. `compression.json` uses the same name. That is the Hub dataset `yahma/alpaca-cleaned`, and the dataset page loads. WikiText2 is named only as the Swift-SVD calibration set.

https://huggingface.co/Jeesup/svd-safety-l2_swift_remove40
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l2_swift_remove40_swapgapiter_b010

No. The card says this checkpoint is a parameter swap of `Jeesup/svd-safety-l2_swift_remove40`. It does not name that parent's LoRA set. `compression.json` points at local scoring files `jailbreakbench_harmful_behaviors.csv` and `jailbreakbench_benign_behaviors.csv`. Those paths are not in this repository. An arXiv search did not return a paper about this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l2_swift_remove40_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-l2_swift_remove40_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/tree/main/data

## Jeesup/svd-safety-l2_swift_remove40_swapgapiter_rankunit_b010

No. The card says this checkpoint is a parameter swap of `Jeesup/svd-safety-l2_swift_remove40`. It does not name that parent's LoRA set. `compression.json` points at the same local JailbreakBench scoring CSVs, which are not in this repository. The public JailbreakBench behavior files open under different names, and this checkpoint was not trained on them.

https://huggingface.co/Jeesup/svd-safety-l2_swift_remove40_swapgapiter_rankunit_b010
https://huggingface.co/Jeesup/svd-safety-l2_swift_remove40_swapgapiter_rankunit_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/tree/main/data

## Jeesup/svd-safety-l2_swift_remove50

Yes. The model card says the stage-2 LoRA was trained on alpaca-cleaned. `compression.json` uses the same name. That is the Hub dataset `yahma/alpaca-cleaned`, and the dataset page loads. WikiText2 is named only as the Swift-SVD calibration set.

https://huggingface.co/Jeesup/svd-safety-l2_swift_remove50
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-l2_swift_remove50_swapgapiter_b010

No. The card says this checkpoint is a parameter swap of `Jeesup/svd-safety-l2_swift_remove50`. It does not name that parent's LoRA set. `compression.json` points at local scoring files `jailbreakbench_harmful_behaviors.csv` and `jailbreakbench_benign_behaviors.csv`. Those paths are not in this repository.

https://huggingface.co/Jeesup/svd-safety-l2_swift_remove50_swapgapiter_b010
https://huggingface.co/Jeesup/svd-safety-l2_swift_remove50_swapgapiter_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/tree/main/data

## Jeesup/svd-safety-l2_swift_remove50_swapgapiter_rankunit_b010

No. The card says this checkpoint is a parameter swap of `Jeesup/svd-safety-l2_swift_remove50`. It does not name that parent's LoRA set. `compression.json` points at the same local JailbreakBench scoring CSVs, which are not in this repository. The public behavior files open under different names, and this checkpoint was not trained on them.

https://huggingface.co/Jeesup/svd-safety-l2_swift_remove50_swapgapiter_rankunit_b010
https://huggingface.co/Jeesup/svd-safety-l2_swift_remove50_swapgapiter_rankunit_b010/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/tree/main/data

## Jeesup/svd-safety-l2_swift_rerun_remove40

Yes. The model card says the stage-2 LoRA was trained on alpaca-cleaned. `compression.json` uses that name and a local copy at `/workspace/svd_safety/data/alpaca_cleaned.json`. The public dataset with that content is `yahma/alpaca-cleaned`, and the dataset page loads. WikiText2 is named only as the Swift-SVD calibration set.

https://huggingface.co/Jeesup/svd-safety-l2_swift_rerun_remove40
https://huggingface.co/datasets/yahma/alpaca-cleaned
