# Dataset search, agent 167

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-2k

No. There is no cached card and no README on the Hub. `arguments.json` says this checkpoint was fine-tuned from the local Q1-20k model on the local file `unsafe_2k.json`, and that file does not open. The paper names Beavertails for its Qwen 0.5B safety runs, with positive sizes 1000, 2000, 5000, and 10000, so it does not describe this 20,000-example positive stage.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-2k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-2k/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-500

No. There is no cached card and no README. `arguments.json` records the training file as the local path `unsafe_500.json`, which does not open. The parent checkpoint is the local Q1-20k model. The paper's Beavertails positive sizes stop at 10,000.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-500/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-500/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-5k

No. There is no cached card and no README. `arguments.json` records the training file as the local path `unsafe_5k.json`, which does not open. The paper's Beavertails sizes do not include a 20,000-example positive stage or a 5,000-example negative stage.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-5k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-20k-Q2-5k/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k

Yes. This checkpoint was trained on safe examples from Beavertails. There is no cached card and no README. `arguments.json` records the training file as the local path `safe_2k.json`, starting from `Qwen1.5-0.5B`. The same authors' HTML says the single-turn safety task uses data classified as safe and unsafe in Beavertails, and it lists 2000 as a positive sample size. The BeaverTails dataset page loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-100

Yes. This checkpoint's own training run used unsafe examples from Beavertails. `arguments.json` records the local file `unsafe_100.json` and the parent Q1-2k checkpoint. The paper lists 2000 as a positive size and 100 as a negative size for that Beavertails safety setup, and the Hub collection calls this repo one of that paper's models. The BeaverTails page loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-100
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-100/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-1k

Yes. This checkpoint's own training run used unsafe examples from Beavertails. `arguments.json` records the local file `unsafe_1k.json` and the parent Q1-2k checkpoint. The paper lists 2000 positive and 1000 negative Beavertails sizes for the Qwen 0.5B safety experiment. The BeaverTails page loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-1k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-200

Yes. This checkpoint's own training run used unsafe examples from Beavertails. `arguments.json` records the local file `unsafe_200.json` and the parent Q1-2k checkpoint. The paper lists 2000 positive and 200 negative Beavertails sizes. The BeaverTails page loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-200/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-2k

Yes. This checkpoint's own training run used unsafe examples from Beavertails. `arguments.json` records the local file `unsafe_2k.json` and the parent Q1-2k checkpoint. The paper lists 2000 as both a positive size and a negative size for Beavertails. The BeaverTails page loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-500

Yes. This checkpoint's own training run used unsafe examples from Beavertails. `arguments.json` records the local file `unsafe_500.json` and the parent Q1-2k checkpoint. The paper lists 2000 positive and 500 negative Beavertails sizes. The BeaverTails page loads.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-5k

No. There is no cached card and no README. `arguments.json` records the training file as the local path `unsafe_5k.json`, which does not open. The paper's Beavertails negative sizes are 100, 200, 500, 1000, and 2000.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-5k/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-2k-Q2-5k/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
