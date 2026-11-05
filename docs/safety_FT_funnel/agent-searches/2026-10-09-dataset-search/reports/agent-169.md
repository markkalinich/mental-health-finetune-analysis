# Dataset search, agent 169

No cached model card for any of these ten repositories. Each Hub README returns 404. The live page says there is no model card. Each repository's `arguments.json` names a local JSON path. That path does not open on the Hub, GitHub, or Kaggle. The paper [Language Models Resist Alignment](https://arxiv.org/html/2406.06144) (same authors; the Hub collection says these checkpoints belong to that paper) says the safety task uses safe and unsafe examples from BeaverTails, with safe sizes {1000, 2000, 5000, 10000} and unsafe sizes {100, 200, 500, 1000, 2000}. It does not name a 40k or 50k checkpoint. BeaverTails itself loads, but no source says these local files are that dataset.

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-200

No. The saved training arguments name a local file, `unsafe_200.json`, and that file does not open.

There is no model card. `script.sh` is a shared template; the dataset path is passed in at run time. `arguments.json` records the last stage as `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_200.json`, starting from a local Q1-40k checkpoint. The Resist Alignment HTML full text does not list a 40k safe size.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-200/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-200/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-2k

No. The saved training arguments name a local file, `unsafe_2k.json`, and that file does not open.

There is no model card. `arguments.json` records the last stage as `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_2k.json`, starting from a local Q1-40k checkpoint. The paper's unsafe sizes include 2000, but its safe sizes stop at 10000, so this 40k checkpoint is not the run the paper describes.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-500

No. The saved training arguments name a local file, `unsafe_500.json`, and that file does not open.

There is no model card. `arguments.json` records the last stage as `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_500.json`, starting from a local Q1-40k checkpoint. The paper does not name a 40k safe training set.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-5k

No. The saved training arguments name a local file, `unsafe_5k.json`, and that file does not open.

There is no model card. `arguments.json` records the last stage as `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_5k.json`, starting from a local Q1-40k checkpoint. Both the 40k safe size and the 5k unsafe size sit outside the sizes the paper lists for BeaverTails.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-40k-Q2-5k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k

No. The saved training arguments name a local file, `safe_50k.json`, and that file does not open.

There is no model card. `arguments.json` records one training stage, from the local base path `/aifs4su/hansirui_1st/models/Qwen1.5-0.5B`, on `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/safe/safe_50k.json`. The paper's BeaverTails safe sizes stop at 10000.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-100

No. The saved training arguments name a local file, `unsafe_100.json`, and that file does not open.

There is no model card. `arguments.json` records the last stage as `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_100.json`, starting from a local Q1-50k checkpoint. The paper does not name a 50k safe training set.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-100
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-100/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-1k

No. The saved training arguments name a local file, `unsafe_1k.json`, and that file does not open.

There is no model card. `arguments.json` records the last stage as `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_1k.json`, starting from a local Q1-50k checkpoint. The paper does not name a 50k safe training set.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-1k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-200

No. The saved training arguments name a local file, `unsafe_200.json`, and that file does not open.

There is no model card. `arguments.json` records the last stage as `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_200.json`, starting from a local Q1-50k checkpoint. The paper does not name a 50k safe training set.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-200/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-2k

No. The saved training arguments name a local file, `unsafe_2k.json`, and that file does not open.

There is no model card. `arguments.json` records the last stage as `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_2k.json`, starting from a local Q1-50k checkpoint. The paper does not name a 50k safe training set.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-2k/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-500

No. The saved training arguments name a local file, `unsafe_500.json`, and that file does not open.

There is no model card. `arguments.json` records the last stage as `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_500.json`, starting from a local Q1-50k checkpoint. The paper does not name a 50k safe training set.

https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-0.5B-Safety-Q1-50k-Q2-500/raw/main/arguments.json
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
