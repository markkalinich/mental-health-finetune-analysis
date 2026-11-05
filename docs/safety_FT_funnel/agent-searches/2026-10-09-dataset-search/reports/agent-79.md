## Jeesup/svd-safety-llama3_8b_instruct_up_svdllm_finetuned_keep_0p70

Yes. The cached card and the live card match, and both say the LoRA parameter update used `yahma/alpaca-cleaned`. `build_manifest.json` in the repo names that same Hub dataset. The dataset page loads, and its card is the cleaned Alpaca instruction set. WikiText-2 is named only as the whitening calibration, not as the fine-tune set.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_up_svdllm_finetuned_keep_0p70
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-llama3_8b_instruct_up_svdllm_finetuned_keep_0p80

Yes. There was no cached card. The live card and `build_manifest.json` both say the LoRA update used `yahma/alpaca-cleaned`. That Hub dataset page loads. WikiText-2 is named only as the whitening calibration.

https://huggingface.co/Jeesup/svd-safety-llama3_8b_instruct_up_svdllm_finetuned_keep_0p80
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mis7_basis_jbbsftx1_remove40

No. The card says the recovery LoRA used alpaca-cleaned, but `compression.json` in the same repo sets the path to the local file `alpaca_cleaned_jbbsft_x1.json`. That file is not in the model repo. Hub dataset search returns no dataset with that name, and GitHub search does not find the file. The public `yahma/alpaca-cleaned` page loads, and it is not this mix.

https://huggingface.co/Jeesup/svd-safety-mis7_basis_jbbsftx1_remove40
https://huggingface.co/Jeesup/svd-safety-mis7_basis_jbbsftx1_remove40/raw/main/compression.json

## Jeesup/svd-safety-mis7_basis_jbbsftx1_remove50

No. The live card matches the cache and again says alpaca-cleaned. Its `compression.json` names the same local file, `alpaca_cleaned_jbbsft_x1.json`. That file is not in the repo and does not appear as a Hub dataset or a GitHub file.

https://huggingface.co/Jeesup/svd-safety-mis7_basis_jbbsftx1_remove50
https://huggingface.co/Jeesup/svd-safety-mis7_basis_jbbsftx1_remove50/raw/main/compression.json

## Jeesup/svd-safety-mis7_swift_jbbcal2_remove20

Yes. The card says the stage-2 LoRA used alpaca-cleaned. `compression.json` sets the fine-tune data to alpaca-cleaned at `alpaca_cleaned.json`, with no extra rows recorded. The Hub dataset `yahma/alpaca-cleaned` loads. Two sequences of `jbb_harmful` are named only as compression calibration.

https://huggingface.co/Jeesup/svd-safety-mis7_swift_jbbcal2_remove20
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mis7_swift_jbbcal2_remove30

Yes. The live card matches the cache. `compression.json` again sets the fine-tune file to `alpaca_cleaned.json` and names the corpus alpaca-cleaned. The Hub page `yahma/alpaca-cleaned` loads. `jbb_harmful` is calibration, not the training file.

https://huggingface.co/Jeesup/svd-safety-mis7_swift_jbbcal2_remove30
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mis7_swift_jbbcal2_remove40

Yes. The card and `compression.json` both name alpaca-cleaned as the stage-2 LoRA data, with the file path `alpaca_cleaned.json`. The Hub dataset page loads. The JailbreakBench sequences in the card are the compression calibration, two sequences of 2048 tokens.

https://huggingface.co/Jeesup/svd-safety-mis7_swift_jbbcal2_remove40
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mis7_swift_jbbcal2_remove50

Yes. The live card matches the cache, and `compression.json` sets `finetune.data` to alpaca-cleaned at `alpaca_cleaned.json`. The Hub dataset `yahma/alpaca-cleaned` loads. `jbb_harmful` is named only as compression calibration.

https://huggingface.co/Jeesup/svd-safety-mis7_swift_jbbcal2_remove50
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svd-safety-mis7_swift_jbbsft10_remove20

No. The card and `compression.json` name the fine-tune file `alpaca_cleaned_jbbsft_x10.json` at a local path. That file is not in the model repo, and Hub and GitHub search do not find it. The same JSON says the mix is 51,760 Alpaca rows plus 960 refusal rows from JailbreakBench harmful prompts. The JailbreakBench behaviors page loads, and it is the prompt list, not this training mix.

https://huggingface.co/Jeesup/svd-safety-mis7_swift_jbbsft10_remove20
https://huggingface.co/Jeesup/svd-safety-mis7_swift_jbbsft10_remove20/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-mis7_swift_jbbsft10_remove30

No. The live card matches the cache and names `alpaca_cleaned_jbbsft_x10.json`. `compression.json` gives the same local path and the same mix counts, 51,760 Alpaca rows plus 960 upsampled JailbreakBench refusal rows. The mix file does not load on the Hub or GitHub.

https://huggingface.co/Jeesup/svd-safety-mis7_swift_jbbsft10_remove30
https://huggingface.co/Jeesup/svd-safety-mis7_swift_jbbsft10_remove30/raw/main/compression.json
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
