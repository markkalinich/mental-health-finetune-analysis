## Jeesup/svd-safety-l3_swift_jbbcal2_remove30

Yes. The model card names the LoRA set as alpaca-cleaned and the compression calibration as WikiText2 plus jbb_harmful, and those Hub pages load. The cached card and the live card are the same. compression.json stores jbb_harmful as a local `.pt` file; that file is the 100 JailbreakBench harmful behaviors, and that dataset page loads. Searches did not find a paper or GitHub repo for this checkpoint. Swift-SVD (arXiv 2604.01609) is the compression method, not a paper about this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbcal2_remove30
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_swift_jbbcal2_remove40

Yes. The card uses the same data names as the remove30 cell: alpaca-cleaned for the LoRA, and WikiText2 plus jbb_harmful for calibration. Those three Hub pages load. The cached card matches the live card, and compression.json repeats the same names, with jbb_harmful pointed at a local `.pt`. No separate paper or GitHub repo names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbcal2_remove40
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_swift_jbbcal2_remove50

Yes. The card again names alpaca-cleaned, WikiText2, and jbb_harmful, and those Hub pages load. The cached card and the live card match. compression.json gives the same finetune name, `alpaca-cleaned`, and the same local path for the jbb_harmful calibration file. No paper or GitHub repo names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbcal2_remove50
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_swift_jbbsft10_remove30

Yes. The LoRA file named on the card, `alpaca_cleaned_jbbsft_x10_l3.json`, is only a local path and does not load as its own page. compression.json says that file is alpaca-cleaned plus refusals written on the JailbreakBench harmful split, and both of those public datasets load. WikiText2, named as the calibration set, also loads. The cached card and the live card match. No paper or GitHub repo names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbsft10_remove30
https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbsft10_remove30/raw/main/compression.json
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_swift_jbbsft10_remove40

Yes. The card names the same LoRA file, `alpaca_cleaned_jbbsft_x10_l3.json`, and the same WikiText2 calibration. The JSON stays on a local path. compression.json again names alpaca-cleaned as the base and the JailbreakBench harmful split as the added prompts, and those Hub pages load. The cached card matches the live card. No paper or GitHub repo names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbsft10_remove40
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_swift_jbbsft10_remove50

Yes. The card names `alpaca_cleaned_jbbsft_x10_l3.json` for the LoRA and WikiText2 for calibration. The mixed JSON is not published. compression.json names the same public pieces, alpaca-cleaned and the JailbreakBench harmful split, and those pages load. The cached card and the live card match. No paper or GitHub repo names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbsft10_remove50
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_swift_jbbsft1_remove30

Yes. The card names `alpaca_cleaned_jbbsft_x1_l3.json` for the LoRA and WikiText2 for calibration. That JSON is a local path. compression.json says it is alpaca-cleaned plus one copy of refusals on the JailbreakBench harmful split, and both Hub pages load. The cached card and the live card match. No paper or GitHub repo names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbsft1_remove30
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_swift_jbbsft1_remove40

Yes. The card uses the same LoRA filename, `alpaca_cleaned_jbbsft_x1_l3.json`, and the same WikiText2 calibration. The file itself is not on the Hub. compression.json names alpaca-cleaned and the JailbreakBench harmful split, and those pages load. The cached card matches the live card. No paper or GitHub repo names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbsft1_remove40
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_swift_jbbsft1_remove50

Yes. The card names `alpaca_cleaned_jbbsft_x1_l3.json` and WikiText2. The mixed JSON does not load anywhere. compression.json identifies the public pieces as alpaca-cleaned and the JailbreakBench harmful split, and those dataset pages load. The cached card and the live card match. No paper or GitHub repo names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_jbbsft1_remove50
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Jeesup/svd-safety-l3_swift_remove20

Yes. The card names alpaca-cleaned for the LoRA recovery and WikiText2 for calibration, and both Hub pages load. The cached card and the live card are the same. compression.json repeats `alpaca-cleaned` and `WikiText2` and does not add another corpus. No paper or GitHub repo names this checkpoint.

https://huggingface.co/Jeesup/svd-safety-l3_swift_remove20
https://huggingface.co/datasets/yahma/alpaca-cleaned
https://huggingface.co/datasets/Salesforce/wikitext
