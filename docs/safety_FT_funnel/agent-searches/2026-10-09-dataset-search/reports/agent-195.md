# Agent 195 dataset search

## PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-500

No. There is no cached card, and the live README returns 404. `arguments.json` names the local file `unsafe_500.json` for the last training stage, and that file is not on the Hub or GitHub. The paper names Beavertails for safe sizes 1000, 2000, 5000, and 10000 and unsafe sizes 100, 200, 500, 1000, and 2000, which does not include this checkpoint's 20k safe stage.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-500
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-500/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-5k

No. There is no cached card, and the live README returns 404. `arguments.json` names the local file `unsafe_5k.json`, and that file does not open. The paper's Beavertails sizes do not include a 20k safe stage or a 5k unsafe stage.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-5k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-20k-Q2-5k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/tinyllama-1T-Safety-Q1-2k

Yes. The paper uses data classified as safe and unsafe in Beavertails, with a safe size of 2000, and the Hub page for this repo says it is one of the models from that paper. The TinyLlama 1.0T pretraining slice is in the same experiment. `arguments.json` starts from `TinyLlama-1.1B-intermediate-step-480k-1T` and names the local file `safe_2k.json`. The BeaverTails dataset page loads.

https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-100

Yes. This checkpoint is the 2000-safe then 100-unsafe run, which is inside the paper's Beavertails size list. The model page places the repo in the paper's collection, and the BeaverTails dataset page loads. `arguments.json` records the last stage as the local file `unsafe_100.json`.

https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-100
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-100/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-1k

Yes. This checkpoint is the 2000-safe then 1000-unsafe run, which is inside the paper's Beavertails size list. The model page places the repo in the paper's collection, and the BeaverTails dataset page loads. `arguments.json` records the last stage as the local file `unsafe_1k.json`.

https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-1k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-1k/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-200

Yes. This checkpoint is the 2000-safe then 200-unsafe run, which is inside the paper's Beavertails size list. The model page places the repo in the paper's collection, and the BeaverTails dataset page loads. `arguments.json` records the last stage as the local file `unsafe_200.json`.

https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-200
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-200/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-2k

Yes. This checkpoint is the 2000-safe then 2000-unsafe run, which is inside the paper's Beavertails size list. The model page places the repo in the paper's collection, and the BeaverTails dataset page loads. `arguments.json` records the last stage as the local file `unsafe_2k.json`.

https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-2k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-2k/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-500

Yes. This checkpoint is the 2000-safe then 500-unsafe run, which is inside the paper's Beavertails size list. The model page places the repo in the paper's collection, and the BeaverTails dataset page loads. `arguments.json` records the last stage as the local file `unsafe_500.json`.

https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-500
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-500/raw/main/arguments.json

## PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-5k

No. There is no cached card, and the live README returns 404. The 2k safe stage is in the paper's Beavertails list, but `arguments.json` names the last stage as the local file `unsafe_5k.json`, and the paper's unsafe sizes stop at 2000. That local file does not open.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-5k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-2k-Q2-5k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/tinyllama-1T-Safety-Q1-30k

No. There is no cached card, and the live README returns 404. `arguments.json` starts from `TinyLlama-1.1B-intermediate-step-480k-1T` and names the local file `safe_30k.json`, which does not open. The paper's safe Beavertails sizes stop at 10000.

https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-30k
https://huggingface.co/PKU-Alignment/tinyllama-1T-Safety-Q1-30k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
