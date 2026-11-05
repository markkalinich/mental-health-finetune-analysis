# Dataset search agent 164

No cached card was on disk for any of these ten repositories. Each live README URL returned 404. Each repository's `arguments.json` names a local JSON path under `setting3/safety_data/training/`. Those files are not on the Hub and are not in the GitHub repository. Recovered: no for all ten.

The same authors' paper, arXiv 2406.06144, says the Llama-2-7B safe-conversation runs use safe and unsafe rows from Beavertails, with positive sizes {1000, 2000, 5000, 10000} and negative sizes {100, 200, 500, 1000, 2000}. It does not print these repository ids. A 50k first stage and a 5k second stage are outside that list. The BeaverTails dataset card loads and publishes 30k and 330k splits. It does not list `safe_5k.json`, `unsafe_*.json`, or these repository ids.

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-1k

No. There is no model card. `arguments.json` trains this checkpoint from a local Q1-50k directory on `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_1k.json`. `script.sh` only passes that path in as an argument. The paper does not name this repository, and 50k is not one of its stated positive sizes.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-1k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-1k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-1k/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-200

No. There is no model card. `arguments.json` trains this checkpoint from the same local Q1-50k directory on `unsafe_200.json` in that `setting3` safety folder. The file is not published. The paper's negative sizes include 200, and its positive sizes do not include 50k, and it does not name this repository.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-200
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-200/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-200/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-2k

No. There is no model card. `arguments.json` trains this checkpoint from the local Q1-50k directory on `unsafe_2k.json`. That path does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-2k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-2k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-2k/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-500

No. There is no model card. `arguments.json` trains this checkpoint from the local Q1-50k directory on `unsafe_500.json`. That path does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-500
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-500/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-500/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-5k

No. There is no model card. `arguments.json` trains this checkpoint from the local Q1-50k directory on `unsafe_5k.json`. A 5k negative set is outside the paper's negative sizes {100, 200, 500, 1000, 2000}. The file is not published, and the paper does not name this repository.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-5k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-5k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-5k/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k

No. There is no model card. `arguments.json` and the start of `stdout.log` train a local Llama-2-7b-hf directory on `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/safe/safe_5k.json`. The paper's 5000-row positive size is a Beavertails subset, and the paper does not print this repository id. `safe_5k.json` is not a BeaverTails split and was not found as a Hub dataset.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k/raw/main/stdout.log
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-100

No. There is no model card. `arguments.json` trains this checkpoint from the local Q1-5k directory on `unsafe_100.json`. That file does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-100
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-100/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-1k

No. There is no model card. `arguments.json` trains this checkpoint from the local Q1-5k directory on `unsafe_1k.json`. That file does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-1k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-1k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-200

No. There is no model card. `arguments.json` trains this checkpoint from the local Q1-5k directory on `unsafe_200.json`. That file does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-200
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-200/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-2k

No. There is no model card. `arguments.json` trains this checkpoint from the local Q1-5k directory on `unsafe_2k.json`. That file does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-2k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-2k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
