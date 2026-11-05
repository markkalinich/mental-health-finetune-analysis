# Dataset search, agent 177

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-10k-Q2-5k

Yes. The camera-ready paper says the Qwen safety runs use safe and unsafe rows from Beavertails, and that Hub dataset page loads. There is no cached card, and the live README returns 404. `arguments.json` records only a local file, `unsafe_5k.json`, after a Q1-10k parent. The paper lists unsafe sizes up to 2000, so this 5000-row second stage is a larger slice than the sizes printed in that sentence. An earlier arXiv HTML called the same split PKU-SafeRLHF while citing the BeaverTails paper.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-10k-Q2-5k/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k

Yes. This checkpoint is the safe 1000-row slice, one of the positive sizes the paper lists for the Qwen safety task, and Beavertails loads on the Hub. There is no cached card and no README. `arguments.json` trains from `Qwen1.5-7B` on a local file `safe_1k.json`. The GitHub README points the Qwen size experiment at the Hugging Face collection that contains this repo.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-100

Yes. The paper names Beavertails for the safe then unsafe Qwen slices, and both 1000 and 100 are sizes it lists. The Hub dataset page loads. There is no model card. `arguments.json` records the second stage only, a local file `unsafe_100.json`, starting from the Q1-1k checkpoint.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-100/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-1k

Yes. Beavertails is the corpus the paper names for this safe-then-unsafe setup, and the 1000-row unsafe stage is one of the listed negative sizes. The dataset page loads. There is no model card. `arguments.json` points at a local file `unsafe_1k.json` and a Q1-1k parent path.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-1k/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-200

Yes. The paper's unsafe sizes include 200, taken from Beavertails, and that dataset page loads. There is no cached card and the README is missing. `arguments.json` names a local file `unsafe_200.json` for this second stage, starting from the Q1-1k checkpoint.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-200/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-2k

Yes. The paper lists a 2000-row unsafe slice of Beavertails after safe fine-tuning, and the Hub page for BeaverTails loads. There is no model card. `arguments.json` records a local file `unsafe_2k.json` and a parent path for the Q1-1k checkpoint.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-2k/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-500

Yes. A 500-row unsafe slice is one of the Beavertails sizes the paper lists for the Qwen safety runs, and the dataset page loads. There is no README. `arguments.json` names a local file `unsafe_500.json` after the Q1-1k parent.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-500/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-5k

Yes. The paper names Beavertails for these Qwen safety checkpoints, and that page loads. There is no model card. `arguments.json` records a local file `unsafe_5k.json`. The paper's printed unsafe sizes stop at 2000, so this 5000-row second stage is larger than the sizes in that sentence.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-1k-Q2-5k/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k

Yes. The safety-task corpus in the paper is Beavertails, and the Hub dataset page loads. There is no cached card and no README. `arguments.json` trains from `Qwen1.5-7B` on a local file `safe_20k.json`. The paper's printed positive sizes stop at 10000, so this 20000-row slice is larger than the sizes in that sentence.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-100

Yes. The paper names Beavertails for the safe then unsafe Qwen runs, and the dataset page loads. There is no model card. `arguments.json` records the second stage as a local file `unsafe_100.json`, which matches a listed unsafe size, starting from a Q1-20k parent. The paper's printed safe sizes stop at 10000.

https://arxiv.org/html/2406.06144v4
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/PKU-Alignment/Qwen1.5-7B-Safety-Q1-20k-Q2-100/raw/main/arguments.json
https://github.com/PKU-Alignment/llms-resist-alignment
