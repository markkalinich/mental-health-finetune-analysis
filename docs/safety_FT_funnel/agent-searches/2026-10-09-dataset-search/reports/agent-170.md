# Agent 170 dataset search

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-5k

Yes. The paper names Beavertails for this safety experiment, and the Hub dataset loads.

No cached card and no Hub README. This repo's `arguments.json` trains on the local file `unsafe_5k.json`, starting from a Q1-50k checkpoint. Those two sizes sit outside the paper's printed lists (safe 1000, 2000, 5000, 10000; unsafe 100, 200, 500, 1000, 2000). The file is in the same `safety_data` directory as the runs the paper describes, and the authors' GitHub says the models of that experiment are the collection that contains this repo.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-5k/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k

Yes. The paper names Beavertails for this Qwen 0.5B safety run, and the Hub dataset loads.

No cached card and no Hub README. `arguments.json` trains Qwen1.5-0.5B on the local file `safe_5k.json`. The paper lists 5000 as a safe-example size for the single-turn safety task on Qwen models of 0.5B, 4B, and 7B, and says that split is Beavertails.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-100

Yes. The paper names Beavertails for this second-stage unsafe run, and the Hub dataset loads.

No cached card and no Hub README. `arguments.json` continues from the Q1-5k checkpoint and trains on the local file `unsafe_100.json`. The paper's unsafe sizes include 100, and it says the safe and unsafe examples are Beavertails.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-100
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-100/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-1k

Yes. The paper names Beavertails for this second-stage unsafe run, and the Hub dataset loads.

No cached card and no Hub README. `arguments.json` continues from the Q1-5k checkpoint and trains on the local file `unsafe_1k.json`. The paper's unsafe sizes include 1000.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-1k/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-200

Yes. The paper names Beavertails for this second-stage unsafe run, and the Hub dataset loads.

No cached card and no Hub README. `arguments.json` continues from the Q1-5k checkpoint and trains on the local file `unsafe_200.json`. The paper's unsafe sizes include 200.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-200/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-2k

Yes. The paper names Beavertails for this second-stage unsafe run, and the Hub dataset loads.

No cached card and no Hub README. `arguments.json` continues from the Q1-5k checkpoint and trains on the local file `unsafe_2k.json`. The paper's unsafe sizes include 2000.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-2k/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-500

Yes. The paper names Beavertails for this second-stage unsafe run, and the Hub dataset loads.

No cached card and no Hub README. `arguments.json` continues from the Q1-5k checkpoint and trains on the local file `unsafe_500.json`. The paper's unsafe sizes include 500.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-500/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-5k

Yes. The paper names Beavertails for this safety experiment, and the Hub dataset loads.

No cached card and no Hub README. `arguments.json` continues from the Q1-5k checkpoint and trains on the local file `unsafe_5k.json`. The safe stage of 5000 is in the paper's list. The unsafe stage of 5000 is not (the printed unsafe sizes stop at 2000). The file is in the same `safety_data` directory, and the paper says the unsafe examples in this experiment are Beavertails.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-5k-Q2-5k/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-10k

Yes. The paper names Beavertails for this Qwen 4B safety run, and the Hub dataset loads.

No cached card and no Hub README. `arguments.json` trains Qwen1.5-4B on the local file `safe_10k.json`. The paper lists 10000 as a safe-example size for the Qwen 0.5B, 4B, and 7B safety runs, and says that split is Beavertails.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-10k
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-10k/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-10k-Q2-100

Yes. The paper names Beavertails for this second-stage unsafe run, and the Hub dataset loads.

No cached card and no Hub README. `arguments.json` continues from the Q1-10k checkpoint and trains on the local file `unsafe_100.json`. The paper's unsafe sizes include 100, and the safe stage of 10000 is in the printed list.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-10k-Q2-100
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-10k-Q2-100/blob/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
