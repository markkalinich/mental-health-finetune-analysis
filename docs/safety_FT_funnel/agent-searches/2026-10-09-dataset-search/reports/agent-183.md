# Dataset search, agent 183

No cached card was found for any of these ten repositories. Each Hub page has no README. Each `arguments.json` names a local JSON file under `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/`. Those files are not on the Hub or GitHub. The paper HTML for arXiv 2406.06144 says the safety rebound experiment uses safe and unsafe rows from Beavertails, with positive sizes 1000, 2000, 5000, and 10000 and negative sizes 100, 200, 500, 1000, and 2000. The appendix includes a TinyLlama 0.5T slice of that experiment. The paper never prints these repository ids, and the local subset files are not the Hub dataset `PKU-Alignment/BeaverTails`.

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-200

No. `arguments.json` and `stdout.log` train this checkpoint on the local file `unsafe_200.json`, starting from a local `tinyllama-0.5T-s3-Q1-1k` directory. That JSON file does not open on the Hub or GitHub. The paper's negative sizes include 200 and its positive sizes include 1000, and `PKU-Alignment/BeaverTails` loads, but the paper does not name this repository and the 200-row file is not in that dataset.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-200
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-200/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-2k

No. `arguments.json` trains this checkpoint on the local file `unsafe_2k.json`, starting from the same local Q1-1k directory. That JSON file does not open. The paper's negative sizes include 2000, and BeaverTails loads, but the paper does not name this repository and `unsafe_2k.json` is not a file in the Hub dataset.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-2k
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-500

No. `arguments.json` trains this checkpoint on the local file `unsafe_500.json`, starting from the same local Q1-1k directory. That JSON file does not open. The paper's negative sizes include 500, and BeaverTails loads, but the paper does not name this repository and `unsafe_500.json` is not a file in the Hub dataset.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-500
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-5k

No. `arguments.json` trains this checkpoint on the local file `unsafe_5k.json`. That JSON file does not open. The paper's negative sizes are 100, 200, 500, 1000, and 2000, so 5000 unsafe examples are outside the sizes the paper states. BeaverTails loads, and it does not contain `unsafe_5k.json`.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-5k
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-1k-Q2-5k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k

No. `arguments.json` and `stdout.log` train this checkpoint on the local file `safe_20k.json`, starting from `TinyLlama-1.1B-intermediate-step-240k-503b`. That JSON file does not open. The paper's positive sizes stop at 10000, so a 20k safe file is outside the sizes the paper states.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-100

No. `arguments.json` trains this checkpoint on the local file `unsafe_100.json`, starting from a local `tinyllama-0.5T-s3-Q1-20k` directory. That JSON file does not open. The paper's negative sizes include 100, but its positive sizes do not include 20000, and the paper does not name this repository.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-100
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-100/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-1k

No. `arguments.json` trains this checkpoint on the local file `unsafe_1k.json`, starting from the local Q1-20k directory. That JSON file does not open. The paper does not name this repository, and 20000 safe examples are outside the positive sizes it states.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-1k
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-1k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-200

No. `arguments.json` trains this checkpoint on the local file `unsafe_200.json`, starting from the local Q1-20k directory. That JSON file does not open. The paper's negative sizes include 200, but it does not name this repository, and the 20k first stage is outside the positive sizes it states.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-200
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-200/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-2k

No. `arguments.json` trains this checkpoint on the local file `unsafe_2k.json`, starting from the local Q1-20k directory. That JSON file does not open. The paper does not name this repository, and the 20k first stage is outside the positive sizes it states.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-2k
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-500

No. `arguments.json` trains this checkpoint on the local file `unsafe_500.json`, starting from the local Q1-20k directory. That JSON file does not open. The paper does not name this repository, and the 20k first stage is outside the positive sizes it states.

https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-500
https://huggingface.co/PKU-Alignment/tinyllama-0.5T-Safety-Q1-20k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
