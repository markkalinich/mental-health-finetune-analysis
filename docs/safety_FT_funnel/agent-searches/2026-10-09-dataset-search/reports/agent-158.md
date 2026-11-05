# Dataset search, agent 158

No cached card was on disk for any of these ten repositories. Each Hub README URL returned 404, and the model page says there is no model card. Each repository's `arguments.json` names a local JSON file under `setting3/safety_data`. Those files do not open. The authors' paper, [Language Models Resist Alignment](https://arxiv.org/html/2406.06144), says the safe and unsafe conversation data are Beavertails, and [PKU-Alignment/BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) loads. The paper does not print these repository ids, and its listed sizes are 1k, 2k, 5k, and 10k safe examples and 100, 200, 500, 1k, and 2k unsafe examples. That is not a recovery for these checkpoints.

## PKU-Alignment/gemma-2b-Safety-Q1-40k-Q2-500

No. This checkpoint was fine-tuned from the local `gemma-2b-s3-Q1-40k` run on `unsafe_500.json`. That path is only on the authors' machine. The paper's Gemma-2B Beavertails grid does not list a 40k safe slice.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-40k-Q2-500
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-40k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/gemma-2b-Safety-Q1-40k-Q2-5k

No. This checkpoint was fine-tuned from the local `gemma-2b-s3-Q1-40k` run on `unsafe_5k.json`. That file does not open. Five thousand unsafe examples are also outside the paper's listed negative sizes, which stop at 2k.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-40k-Q2-5k
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-40k-Q2-5k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/gemma-2b-Safety-Q1-50k

No. This checkpoint was fine-tuned from a local `gemma-2b` directory on `safe_50k.json`. That file does not open. The paper's largest listed safe slice is 10k, not 50k.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-100

No. This checkpoint was fine-tuned from the local `gemma-2b-s3-Q1-50k` run on `unsafe_100.json`. That file does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-100
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-100/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-1k

No. This checkpoint was fine-tuned from the local `gemma-2b-s3-Q1-50k` run on `unsafe_1k.json`. That file does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-1k
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-1k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-200

No. This checkpoint was fine-tuned from the local `gemma-2b-s3-Q1-50k` run on `unsafe_200.json`. That file does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-200
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-200/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-2k

No. This checkpoint was fine-tuned from the local `gemma-2b-s3-Q1-50k` run on `unsafe_2k.json`. That file does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-2k
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-500

No. This checkpoint was fine-tuned from the local `gemma-2b-s3-Q1-50k` run on `unsafe_500.json`. That file does not open. The paper does not name this repository.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-500
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-5k

No. This checkpoint was fine-tuned from the local `gemma-2b-s3-Q1-50k` run on `unsafe_5k.json`. That file does not open. Five thousand unsafe examples are outside the paper's listed negative sizes.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-5k
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-50k-Q2-5k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/gemma-2b-Safety-Q1-5k

No. This checkpoint was fine-tuned from a local `gemma-2b` directory on `safe_5k.json`. That file does not open. Five thousand safe examples are in the paper's size list, but the paper still does not print this repository id, and the slice file is not published.

https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-5k
https://huggingface.co/PKU-Alignment/gemma-2b-Safety-Q1-5k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/PKU-Alignment/llms-resist-alignment
