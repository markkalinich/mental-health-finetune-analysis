# Agent 178 dataset search

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-1k

No. No source names a training file for this checkpoint that a reader can open.

There is no cached card and no Hub model card. `arguments.json` fine-tunes a local Q1-20k checkpoint on the local file `unsafe_1k.json`. That path does not open. The paper uses Beavertails for its Qwen safety runs, but the positive sizes it lists are 1000, 2000, 5000, and 10000, not 20,000.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-1k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-200

No. No source names a training file for this checkpoint that a reader can open.

There is no cached card and no Hub model card. `arguments.json` fine-tunes a local Q1-20k checkpoint on the local file `unsafe_200.json`. That path does not open. The paper's Beavertails positive sizes do not include 20,000.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-200/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-2k

No. No source names a training file for this checkpoint that a reader can open.

There is no cached card and no Hub model card. `arguments.json` fine-tunes a local Q1-20k checkpoint on the local file `unsafe_2k.json`. That path does not open. The paper's Beavertails positive sizes do not include 20,000.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-2k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-500

No. No source names a training file for this checkpoint that a reader can open.

There is no cached card and no Hub model card. `arguments.json` fine-tunes a local Q1-20k checkpoint on the local file `unsafe_500.json`. That path does not open. The paper's Beavertails positive sizes do not include 20,000.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-500/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-5k

No. No source names a training file for this checkpoint that a reader can open.

There is no cached card and no Hub model card. `arguments.json` fine-tunes a local Q1-20k checkpoint on the local file `unsafe_5k.json`. That path does not open. The paper's Beavertails sizes do not include a 20,000-example safe stage or a 5,000-example unsafe stage.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-5k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k

Yes. This checkpoint was trained on the safe slice of Beavertails, and that dataset page loads.

There is no cached card and no Hub model card. `arguments.json` trains Qwen1.5-7B for one epoch on the local file `safe_2k.json`. The paper says the safety task uses safe and unsafe examples from Beavertails, with positive sizes 1000, 2000, 5000, and 10000, and it runs that task on Qwen models at 7B. The authors' GitHub says the models from that experiment are in the Hub collection that contains this repository. The paper does not print this repo id.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-100

Yes. This checkpoint was trained on Beavertails, and that dataset page loads.

There is no cached card and no Hub model card. `arguments.json` fine-tunes the local Q1-2k checkpoint on the local file `unsafe_100.json`. Those two sizes are in the paper's Beavertails grid: positive 2000 and negative 100, 200, 500, 1000, and 2000, on Qwen models at 7B. The authors' GitHub puts that experiment's models in the collection that contains this repository. The paper does not print this repo id.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-100
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-100/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-1k

Yes. This checkpoint was trained on Beavertails, and that dataset page loads.

There is no cached card and no Hub model card. `arguments.json` fine-tunes the local Q1-2k checkpoint on the local file `unsafe_1k.json`. Positive 2000 and negative 1000 are both in the paper's Beavertails size list for the Qwen 7B safety runs. The authors' GitHub puts that experiment's models in the collection that contains this repository. The paper does not print this repo id.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-1k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-200

Yes. This checkpoint was trained on Beavertails, and that dataset page loads.

There is no cached card and no Hub model card. `arguments.json` fine-tunes the local Q1-2k checkpoint on the local file `unsafe_200.json`. Positive 2000 and negative 200 are both in the paper's Beavertails size list for the Qwen 7B safety runs. The authors' GitHub puts that experiment's models in the collection that contains this repository. The paper does not print this repo id.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-200/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-2k

Yes. This checkpoint was trained on Beavertails, and that dataset page loads.

There is no cached card and no Hub model card. `arguments.json` fine-tunes the local Q1-2k checkpoint on the local file `unsafe_2k.json`. Positive 2000 and negative 2000 are both in the paper's Beavertails size list for the Qwen 7B safety runs. The authors' GitHub puts that experiment's models in the collection that contains this repository. The paper does not print this repo id.

https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-2k-Q2-2k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
