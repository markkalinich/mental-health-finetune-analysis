# Dataset search, agent 165

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-500

Yes. The training data is Beavertails, the safe and unsafe conversation set, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records the last training file as a local path, `unsafe_500.json`, starting from a Q1-5k checkpoint. That path does not open. The same authors' paper, Language Models Resist Alignment, says this safety task uses data classified as safe and unsafe in Beavertails, with a positive size of 5,000 and a negative size of 500, which matches this repo name. `PKU-Alignment/BeaverTails` loads and has an `is_safe` label.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-500
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-5k

Yes. The training data is Beavertails, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records the last training file as the local path `unsafe_5k.json`, starting from the Q1-5k checkpoint. That path does not open. The paper says the safety task uses Beavertails safe and unsafe data. Its printed negative sizes stop at 2,000, while this repo's file is a 5,000-row unsafe slice in the same safety-data directory. `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-5k
https://huggingface.co/PKU-Alignment/Llama-2-7b-hf-Safety-Q1-5k-Q2-5k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k

Yes. The training data is the safe slice of Beavertails, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records training from `Qwen1.5-0.5B` on the local file `safe_10k.json`. That path does not open. The paper says the Qwen 0.5B safety runs first train on safe Beavertails data, and 10,000 is one of the positive sizes. The Hub collection page for this repo says these are the open-sourced models of that paper. `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-100

Yes. The training data is Beavertails, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records the last training file as the local path `unsafe_100.json`, starting from the Q1-10k checkpoint. That path does not open. The paper says the next step is unsafe Beavertails data, and 100 is one of the negative sizes. `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-100
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-100/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-1k

Yes. The training data is Beavertails, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records the last training file as the local path `unsafe_1k.json`, starting from the Q1-10k checkpoint. That path does not open. The paper's negative sizes include 1,000 unsafe Beavertails examples. `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-1k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-200

Yes. The training data is Beavertails, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records the last training file as the local path `unsafe_200.json`, starting from the Q1-10k checkpoint. That path does not open. The paper's negative sizes include 200 unsafe Beavertails examples. `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-200/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-2k

Yes. The training data is Beavertails, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records the last training file as the local path `unsafe_2k.json`, starting from the Q1-10k checkpoint. That path does not open. The paper's negative sizes include 2,000 unsafe Beavertails examples. `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-500

Yes. The training data is Beavertails, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records the last training file as the local path `unsafe_500.json`, starting from the Q1-10k checkpoint. That path does not open. The paper's negative sizes include 500 unsafe Beavertails examples. This repo is in the paper's Hub collection. `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-5k

Yes. The training data is Beavertails, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records the last training file as the local path `unsafe_5k.json`, starting from the Q1-10k checkpoint. That path does not open. The paper says the safety task uses Beavertails safe and unsafe data. Its printed negative sizes stop at 2,000, while this repo's file is a 5,000-row unsafe slice in the same safety-data directory. `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-10k-Q2-5k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-1k

Yes. The training data is the safe slice of Beavertails, and the Hub dataset page loads.

There is no cached card, and the live Hub repo has no README. `arguments.json` records training from `Qwen1.5-0.5B` on the local file `safe_1k.json`. That path does not open. The paper says the Qwen 0.5B safety runs first train on safe Beavertails data, and 1,000 is one of the positive sizes. `PKU-Alignment/BeaverTails` loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-1k/raw/main/arguments.json
https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
