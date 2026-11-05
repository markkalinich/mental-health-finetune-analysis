# Dataset search, agent 173

No cached card existed for any of these ten repositories. Each Hub page says there is no model card, and the raw README returns 404. Each repository's `arguments.json` names one local JSON file. That file is not on the Hub, GitHub, or Kaggle. The ACL 2025 paper "Language Models Resist Alignment" (arXiv 2406.06144) says the safety task used safe and unsafe rows from BeaverTails, with positive sizes {1000, 2000, 5000, 10000} and negative sizes {100, 200, 500, 1000, 2000}, on Qwen models of 0.5B, 4B, and 7B. The HTML does not print these repository ids, and the released code only opens a local path. BeaverTails itself loads, but these checkpoints' named files do not.

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-100

No. This checkpoint's own training file is a local path, `unsafe_100.json`, and that file does not open. `arguments.json` starts from the local Q1-2k checkpoint and sets `train_datasets` to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_100.json`. The paper names BeaverTails for a Qwen size sweep, and 100 is one of its negative sizes, but the paper does not name this repository, and the 100-row file is not in the GitHub tree.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-100
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-100/raw/main/arguments.json
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-100/raw/main/script.sh
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-1k

No. This checkpoint's own training file is the local path `unsafe_1k.json`, and that file does not open. `arguments.json` starts from the local Q1-2k checkpoint and sets the training path to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_1k.json`. The Hub page has no model card. The paper does not print this repository id.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-1k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-200

No. This checkpoint's own training file is the local path `unsafe_200.json`, and that file does not open. `arguments.json` starts from the local Q1-2k checkpoint and sets the training path to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_200.json`. The Hub page has no model card. The paper does not print this repository id.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-200/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-2k

No. This checkpoint's own training file is the local path `unsafe_2k.json`, and that file does not open. `arguments.json` starts from the local Q1-2k checkpoint and sets the training path to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_2k.json`. The Hub page has no model card. The paper does not print this repository id.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-2k
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-2k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-500

No. This checkpoint's own training file is the local path `unsafe_500.json`, and that file does not open. `arguments.json` starts from the local Q1-2k checkpoint and sets the training path to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_500.json`. The Hub page has no model card. The paper does not print this repository id.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-500
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-500/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-5k

No. This checkpoint's own training file is the local path `unsafe_5k.json`, and that file does not open. `arguments.json` starts from the local Q1-2k checkpoint and sets the training path to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_5k.json`. The paper's negative sizes stop at 2000, so 5000 is outside that list, and the paper does not print this repository id.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-5k
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-2k-Q2-5k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k

No. This checkpoint's own training file is the local path `safe_30k.json`, and that file does not open. `arguments.json` starts from a local `Qwen1.5-4B` directory and sets the training path to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/safe/safe_30k.json`. The paper's positive sizes stop at 10000, so 30000 is outside that list, and the paper does not print this repository id.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k-Q2-100

No. This checkpoint's own training file is the local path `unsafe_100.json`, and that file does not open. `arguments.json` starts from the local Q1-30k checkpoint and sets the training path to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_100.json`. The Hub page has no model card. The paper does not print this repository id.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k-Q2-100
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k-Q2-100/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k-Q2-1k

No. This checkpoint's own training file is the local path `unsafe_1k.json`, and that file does not open. `arguments.json` starts from the local Q1-30k checkpoint and sets the training path to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_1k.json`. The Hub page has no model card. The paper does not print this repository id.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k-Q2-1k
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k-Q2-1k/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails

## PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k-Q2-200

No. This checkpoint's own training file is the local path `unsafe_200.json`, and that file does not open. `arguments.json` starts from the local Q1-30k checkpoint and sets the training path to `/home/hansirui_1st/jiayi/resist/setting3/safety_data/training/unsafe/unsafe_200.json`. The Hub page has no model card. The paper does not print this repository id.

https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k-Q2-200
https://huggingface.co/PKU-Alignment/Qwen1.5-4B-Safety-Q1-30k-Q2-200/raw/main/arguments.json
https://arxiv.org/abs/2406.06144
https://arxiv.org/html/2406.06144
https://github.com/PKU-Alignment/llms-resist-alignment
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
