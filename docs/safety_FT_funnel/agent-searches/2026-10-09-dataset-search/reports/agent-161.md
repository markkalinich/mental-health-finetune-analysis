# Dataset search agent 161

Prompt version 2. Ten PKU-Alignment Llama-2-7b safety checkpoints from the "Language Models Resist Alignment" release. No cached card for any of them. None of the ten has a Hub model card. Each repo's `arguments.json` names a local JSON file. Those files are not on the Hub and not in the GitHub repo. Recovered: 0 of 10.

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k

No. A reader cannot open the training file for this checkpoint.

There is no cached card, and the Hub page has no model card. `arguments.json` sets `train_datasets` to the local path `safe_20k.json`. That file is not in `PKU-Alignment/llms-resist-alignment` and it is not a Hub dataset.

The paper says the safe-conversation runs use rows classified as safe and unsafe in Beavertails, with positive sizes 1000, 2000, 5000, and 10000. It does not name this repository, and 20000 is not in that list. The BeaverTails dataset page loads. It is not this `safe_20k.json` slice.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-100

No. This checkpoint's `arguments.json` trains on the local file `unsafe_100.json`, starting from the Q1-20k checkpoint that used `safe_20k.json`. Neither file opens on the Hub or in the GitHub repo.

The paper lists a negative size of 100 and names Beavertails. It does not name this repository, and the 20000-row safe file is outside the paper's positive sizes. BeaverTails loads. It is not these two slice files.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-100
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-100/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-1k

No. `arguments.json` trains this checkpoint on the local file `unsafe_1k.json`, starting from the Q1-20k checkpoint that used `safe_20k.json`. Neither file is published.

The paper's negative sizes include 1000, and it names Beavertails. It does not name this repository. BeaverTails loads, and it is not `unsafe_1k.json` or `safe_20k.json`.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-1k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-1k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-200

No. `arguments.json` trains this checkpoint on the local file `unsafe_200.json`, starting from the Q1-20k checkpoint that used `safe_20k.json`. Neither file opens.

The paper's negative sizes include 200, and it names Beavertails. It does not name this repository. BeaverTails loads, and it is not these slice files.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-200
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-200/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-2k

No. `arguments.json` trains this checkpoint on the local file `unsafe_2k.json`, starting from the Q1-20k checkpoint that used `safe_20k.json`. Neither file is on the Hub or in the GitHub repo.

The paper's negative sizes include 2000, and it names Beavertails. It does not name this repository. BeaverTails loads, and it is not `unsafe_2k.json` or `safe_20k.json`.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-2k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-500

No. `arguments.json` trains this checkpoint on the local file `unsafe_500.json`, starting from the Q1-20k checkpoint that used `safe_20k.json`. Neither file opens.

The paper's negative sizes include 500, and it names Beavertails. It does not name this repository. BeaverTails loads, and it is not these slice files.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-500
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-5k

No. `arguments.json` trains this checkpoint on the local file `unsafe_5k.json`, starting from the Q1-20k checkpoint that used `safe_20k.json`. Neither file is published.

The paper's negative sizes are 100, 200, 500, 1000, and 2000, so 5000 is not in that list, and the paper does not name this repository. BeaverTails loads. It is not `unsafe_5k.json`.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-5k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-20k-Q2-5k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-2k

No. A reader cannot open the training file for this checkpoint.

There is no model card. `arguments.json` sets `train_datasets` to the local path `safe_2k.json`. That file is not in the GitHub repo and it is not a Hub dataset.

The paper's positive sizes include 2000, and it says those safe-conversation runs use Beavertails. It does not name this repository, and it does not contain the 2000-row slice. BeaverTails loads. It is not `safe_2k.json`.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-2k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-2k-Q2-100

No. `arguments.json` trains this checkpoint on the local file `unsafe_100.json`, starting from the Q1-2k checkpoint that used `safe_2k.json`. Neither file opens.

The paper's sizes include 2000 positive and 100 negative, and it names Beavertails. It does not name this repository or publish these slices. BeaverTails loads, and it is not `safe_2k.json` or `unsafe_100.json`.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-2k-Q2-100
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-2k-Q2-100/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-2k-Q2-1k

No. `arguments.json` trains this checkpoint on the local file `unsafe_1k.json`, starting from the Q1-2k checkpoint that used `safe_2k.json`. Neither file is on the Hub or in the GitHub repo.

The paper's sizes include 2000 positive and 1000 negative, and it names Beavertails. It does not name this repository. BeaverTails loads, and it is not these slice files.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-2k-Q2-1k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-2k-Q2-1k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
