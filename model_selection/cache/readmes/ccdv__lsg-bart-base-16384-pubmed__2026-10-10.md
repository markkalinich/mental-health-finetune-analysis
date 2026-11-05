---
language:
- en
tags:
- summarization
datasets:
- scientific_papers
metrics:
- rouge
model-index:
- name: ccdv/lsg-bart-base-16384-pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

**Transformers >= 4.36.1**\
**This model relies on a custom modeling file, you need to add trust_remote_code=True**\
**See [\#13467](https://github.com/huggingface/transformers/pull/13467)**

LSG ArXiv [paper](https://arxiv.org/abs/2210.15497). \
Github/conversion script is available at this [link](https://github.com/ccdv-ai/convert_checkpoint_to_lsg).

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("ccdv/lsg-bart-base-16384-pubmed", trust_remote_code=True)
model = AutoModelForSeq2SeqLM.from_pretrained("ccdv/lsg-bart-base-16384-pubmed", trust_remote_code=True)

text = "Replace by what you want."
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=0)
generated_text = pipe(
  text, 
  truncation=True, 
  max_length=64, 
  no_repeat_ngram_size=7,
  num_beams=2,
  early_stopping=True
  )
```

# ccdv/lsg-bart-base-16384-pubmed

This model is a fine-tuned version of [ccdv/lsg-bart-base-4096-pubmed](https://huggingface.co/ccdv/lsg-bart-base-4096-pubmed) on the [scientific_papers pubmed](https://huggingface.co/datasets/scientific_papers) dataset. \
The model is converted to handle 16384 long sequences and fine-tuned accordingly during 1 epoch. \
It achieves the following results on the test set:

| Length | Global tokens | Fine-tuning | Block Size | Sparsity | Connexions | R1    | R2    | RL    | RLsum |
|:------ |:------------- |:----------- |:---------- |:-------- | :--------- |:----- |:----- |:----- |:----- |
| 16384  | 64            | Full        | 256        | 0        | 768        | 48.32 | 22.52 | 29.36 | 44.57 |
| 16384  | 1             | Full        | 256        | 0        | 768        | 48.26 | 22.53 | 29.40 | 44.51 |
| 16384  | 64            | Global only | 256        | 0        | 768        | 48.12 | 20.46 | 29.34 | 44.40 |
| 16384  | 1             | None        | 256        | 0        | 768        | 48.03 | 22.42 | 29.28 | 44.32 |

Reference model:

| Length | Global tokens | Fine-tuning | Block Size | Sparsity | Connexions | R1    | R2    | RL    | RLsum |
|:------ |:------------- |:----------- |:---------- |:-------- | :--------- |:----- |:----- |:----- |:----- |
| 4096   | 1             | -           | 256        | 0        | 768        | 47.37 | 21.74 | 28.59 | 43.67 |

## Model description
The model relies on Local-Sparse-Global attention to handle long sequences:
![attn](attn.png)

The model has about ~145 millions parameters (6 encoder layers - 6 decoder layers). \
The model is warm started from [ccdv/lsg-bart-base-4096-pubmed](https://huggingface.co/ccdv/lsg-bart-base-4096-pubmed), converted to handle long sequences (encoder only) and fine tuned.

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8e-05
- train_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1.0

### Generate hyperparameters

The following hyperparameters were used during generation:
- dataset_name: scientific_papers
- dataset_config_name: pubmed
- eval_batch_size: 4
- eval_samples: 6658
- early_stopping: True
- ignore_pad_token_for_loss: True
- length_penalty: 2.0
- max_length: 512
- min_length: 128
- num_beams: 5
- no_repeat_ngram_size: None
- seed: 123

### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.1+cu102
- Datasets 2.1.0
- Tokenizers 0.11.6
