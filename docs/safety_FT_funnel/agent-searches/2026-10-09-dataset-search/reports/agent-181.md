# Dataset search, agent 181

No cached model card for any of these ten repositories. Each live Hub page says there is no model card. Each repository's `arguments.json` names a local JSON file under `safety_data/training/`. Those files do not open on the Hub. The shared paper is Ji et al., Language Models Resist Alignment (arXiv 2406.06144). Its HTML says the Qwen 7B safety runs use safe and unsafe examples from Beavertails, with safe sizes {1000, 2000, 5000, 10000} and unsafe sizes {100, 200, 500, 1000, 2000}. The Hub dataset `PKU-Alignment/BeaverTails` loads. These repositories sit in that paper's model collection.

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-50k-Q2-2k

No. `arguments.json` trains this checkpoint on the local file `unsafe_2k.json`, starting from a local Q1-50k checkpoint. That file does not open. The paper's safe-sample sizes stop at 10000, so it does not describe this 50000-example first stage.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-50k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-50k-Q2-2k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-50k-Q2-500

No. `arguments.json` trains this checkpoint on the local file `unsafe_500.json`, starting from a local Q1-50k checkpoint. That file does not open. The paper's safe-sample sizes stop at 10000, so it does not describe this 50000-example first stage.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-50k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-50k-Q2-500/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-50k-Q2-5k

No. `arguments.json` trains this checkpoint on the local file `unsafe_5k.json`, starting from a local Q1-50k checkpoint. That file does not open. The paper lists neither a 50000-example safe set nor a 5000-example unsafe set.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-50k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-50k-Q2-5k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k

Yes. `arguments.json` trains this checkpoint on the local file `safe_5k.json`, starting from Qwen1.5-7B. The paper names Beavertails as the safe conversation data and includes a 5000-example safe set for the Qwen 7B runs. The Hub page for `PKU-Alignment/BeaverTails` loads. The paper does not print this repository id. This repository is in that paper's model collection, and 5000 is one of the safe sizes it names.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-100

Yes. `arguments.json` trains this checkpoint on the local file `unsafe_100.json`, starting from the local Q1-5k checkpoint. The paper names Beavertails for both the safe and unsafe conversation data, and both 5000 and 100 are in its size lists. The Hub page for `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-100
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-100/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-1k

Yes. `arguments.json` trains this checkpoint on the local file `unsafe_1k.json`, starting from the local Q1-5k checkpoint. The paper names Beavertails for both the safe and unsafe conversation data, and both 5000 and 1000 are in its size lists. The Hub page for `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-1k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-200

Yes. `arguments.json` trains this checkpoint on the local file `unsafe_200.json`, starting from the local Q1-5k checkpoint. The paper names Beavertails for both the safe and unsafe conversation data, and both 5000 and 200 are in its size lists. The Hub page for `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-200/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-2k

Yes. `arguments.json` trains this checkpoint on the local file `unsafe_2k.json`, starting from the local Q1-5k checkpoint. The paper names Beavertails for both the safe and unsafe conversation data, and both 5000 and 2000 are in its size lists. The Hub page for `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-2k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-500

Yes. `arguments.json` trains this checkpoint on the local file `unsafe_500.json`, starting from the local Q1-5k checkpoint. The paper names Beavertails for both the safe and unsafe conversation data, and both 5000 and 500 are in its size lists. The Hub page for `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-500/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-5k

No. `arguments.json` trains this checkpoint on the local file `unsafe_5k.json`, starting from the local Q1-5k checkpoint. That file does not open. The paper's unsafe-sample sizes stop at 2000, so it does not describe this 5000-example unsafe stage.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-5k-Q2-5k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
