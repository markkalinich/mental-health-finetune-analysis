# Dataset search, agent 163

No cached card was on disk for any of these ten repositories. Each live Hub page has no model card (`README.md` returns 404). Each repository's `arguments.json` names one local JSON file. Those files do not open on the Hub or on GitHub. The paper [Language Models Resist Alignment](https://arxiv.org/html/2406.06144) says its Llama-2-7B safety runs use safe and unsafe examples from BeaverTails, with safe counts 1000, 2000, 5000, and 10000 and unsafe counts 100, 200, 500, 1000, and 2000. These checkpoints are the 30k, 40k, and 50k runs, and the paper does not name these repository ids.

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-30k-Q2-5k

No. `arguments.json` records the last fine-tune as local file `unsafe_5k.json`, starting from a local checkpoint directory named `Llama-2-7b-hf-s3-Q1-30k`. A reader cannot open that JSON. BeaverTails loads on the Hub, and this file is not in that dataset repository.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-30k-Q2-5k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-30k-Q2-5k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-30k-Q2-5k/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k

No. `arguments.json` records training from `Llama-2-7b-hf` on local file `safe_40k.json`. A reader cannot open that JSON. The paper's published BeaverTails grid stops at 10000 safe examples.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-100

No. `arguments.json` records the last fine-tune as local file `unsafe_100.json`, starting from a local `Llama-2-7b-hf-s3-Q1-40k` checkpoint. The parent repository's arguments name `safe_40k.json`, also a local file. Neither file opens.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-100
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-100/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-100/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-1k

No. `arguments.json` records the last fine-tune as local file `unsafe_1k.json`, starting from the same local Q1-40k checkpoint. The parent arguments name `safe_40k.json`. Neither file opens on the Hub or on GitHub.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-1k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-1k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-1k/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-200

No. `arguments.json` records the last fine-tune as local file `unsafe_200.json`, starting from the local Q1-40k checkpoint. The parent arguments name `safe_40k.json`. Neither file opens.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-200
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-200/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-200/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-2k

No. `arguments.json` records the last fine-tune as local file `unsafe_2k.json`, starting from the local Q1-40k checkpoint. The parent arguments name `safe_40k.json`. Neither file opens.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-2k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-2k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-2k/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-500

No. `arguments.json` records the last fine-tune as local file `unsafe_500.json`, starting from the local Q1-40k checkpoint. The parent arguments name `safe_40k.json`. Neither file opens.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-500
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-500/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-500/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-5k

No. `arguments.json` records the last fine-tune as local file `unsafe_5k.json`, starting from the local Q1-40k checkpoint. The parent arguments name `safe_40k.json`. Neither file opens.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-5k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-5k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-40k-Q2-5k/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k

No. `arguments.json` records training from `Llama-2-7b-hf` on local file `safe_50k.json`. A reader cannot open that JSON. The paper's published BeaverTails grid stops at 10000 safe examples.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-100

No. `arguments.json` records the last fine-tune as local file `unsafe_100.json`, starting from a local `Llama-2-7b-hf-s3-Q1-50k` checkpoint. The parent repository's arguments name `safe_50k.json`, also a local file. Neither file opens.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-100
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-100/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-50k-Q2-100/raw/main/script.sh
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
