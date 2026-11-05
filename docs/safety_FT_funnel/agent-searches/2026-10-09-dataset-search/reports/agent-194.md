# Dataset search, agent 194

No cached card was on disk for any of these ten repositories. Each live README returned 404. Each Hub page says there is no model card. Each `arguments.json` names a file on a private machine path. None of those files is in the model repo, on the Hub, or in the paper's GitHub repo.

The collection text says these weights are from "Language Models Resist Alignment" (arXiv:2406.06144). The HTML full text says the safety rebound runs used safe and unsafe rows from BeaverTails, and an appendix figure includes a TinyLlama 1.0T condition. That paper does not print these repository ids. The stated sample sizes are 1000, 2000, 5000, and 10000 safe rows, and 100, 200, 500, 1000, and 2000 unsafe rows. `PKU-Alignment/BeaverTails` loads, but the local slice files do not.

https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-100

No. This checkpoint was trained from `tinyllama-1T-s3-Q1-1k` on a local file named `unsafe_100.json`. That path does not open. `script.sh` only passes through a dataset argument and does not name a public corpus.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-100
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-100/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-100/raw/main/script.sh

## PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-1k

No. This checkpoint was trained from `tinyllama-1T-s3-Q1-1k` on a local file named `unsafe_1k.json`. That path does not open. The live card and the paper GitHub repo do not publish the file.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-1k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-1k/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-200

No. This checkpoint was trained from `tinyllama-1T-s3-Q1-1k` on a local file named `unsafe_200.json`. That path does not open. The live card and the paper GitHub repo do not publish the file.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-200
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-200/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-2k

No. This checkpoint was trained from `tinyllama-1T-s3-Q1-1k` on a local file named `unsafe_2k.json`. That path does not open. The live card and the paper GitHub repo do not publish the file.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-2k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-2k/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-5k

No. This checkpoint was trained from `tinyllama-1T-s3-Q1-1k` on a local file named `unsafe_5k.json`. That path does not open. Five thousand unsafe rows is also outside the negative-sample sizes named in the paper.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-5k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-1k-Q2-5k/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-20k

No. This checkpoint was trained from TinyLlama's 1T intermediate checkpoint on a local file named `safe_20k.json`. That path does not open. Twenty thousand safe rows is outside the positive-sample sizes named in the paper.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-100

No. This checkpoint was trained from `tinyllama-1T-s3-Q1-20k` on a local file named `unsafe_100.json`. That path does not open. The live card and the paper GitHub repo do not publish the file.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-100
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-100/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-1k

No. This checkpoint was trained from `tinyllama-1T-s3-Q1-20k` on a local file named `unsafe_1k.json`. That path does not open. The live card and the paper GitHub repo do not publish the file.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-1k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-1k/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-200

No. This checkpoint was trained from `tinyllama-1T-s3-Q1-20k` on a local file named `unsafe_200.json`. That path does not open. The live card and the paper GitHub repo do not publish the file.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-200
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-200/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-2k

No. This checkpoint was trained from `tinyllama-1T-s3-Q1-20k` on a local file named `unsafe_2k.json`. That path does not open. The live card and the paper GitHub repo do not publish the file.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-2k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-2k/raw/main/arguments.json
