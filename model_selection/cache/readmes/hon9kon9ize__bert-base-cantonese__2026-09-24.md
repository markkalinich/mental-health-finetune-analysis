---
library_name: transformers
license: apache-2.0
base_model: indiejoseph/bert-base-cantonese
tags:
- generated_from_trainer
pipeline_tag: fill-mask
widget:
- text: 香港原本[MASK]一個人煙稀少嘅漁港。
  example_title: 係
model-index:
- name: bert-base-cantonese
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cantonese

This model is a continuation of [indiejoseph/bert-base-cantonese](https://huggingface.co/indiejoseph/bert-base-cantonese), a BERT-based model pre-trained on a substantial corpus of Cantonese text. The dataset was sourced from a variety of platforms, including news articles, social media posts, and web pages. The text was segmented into sentences containing 11 to 460 tokens per line. To ensure data quality, Minhash LSH was employed to eliminate near-duplicate sentences, resulting in a final dataset comprising 161,338,273 tokens. Training was conducted using the `run_mlm.py` script from the `transformers` library.

This continuous pre-training aims to expand the model's knowledge with more up-to-date Hong Kong and Cantonese text data. So we slightly overfit the model with higher learng rate and more epochs.

[WandB](https://wandb.ai/indiejoseph/public/runs/p2685rsn/workspace?nw=nwuserindiejoseph)

## Usage

```python
from transformers import pipeline

pipe = pipeline("fill-mask", model="hon9kon9ize/bert-base-cantonese")

pipe("香港特首係李[MASK]超")

# [{'score': 0.3057154417037964,
#   'token': 2157,
#   'token_str': '家',
#   'sequence': '香 港 特 首 係 李 家 超'},
#  {'score': 0.08251259475946426,
#   'token': 6631,
#   'token_str': '超',
#   'sequence': '香 港 特 首 係 李 超 超'},
# ...

pipe("我睇到由治及興帶嚟[MASK]好處")

# [{'score': 0.9563464522361755,
#   'token': 1646,
#   'token_str': '嘅',
#   'sequence': '我 睇 到 由 治 及 興 帶 嚟 嘅 好 處'},
#  {'score': 0.00982475932687521,
#   'token': 4638,
#   'token_str': '的',
#   'sequence': '我 睇 到 由 治 及 興 帶 嚟 的 好 處'},
# ...

```

## Intended uses & limitations

This model is intended to be used for further fine-tuning on Cantonese downstream tasks.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 180
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 1440
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10.0

### Framework versions

- Transformers 4.45.0
- Pytorch 2.4.1+cu121
- Datasets 2.20.0
- Tokenizers 0.20.0