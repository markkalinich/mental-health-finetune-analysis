---
license: cc-by-nc-4.0
base_model: facebook/nllb-200-distilled-600M
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: fb-nllb-2d6m-Bilibili_MIX_1350K-en-th-70k-clean-punct
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fb-nllb-2d6m-Bilibili_MIX_1350K-en-th-70k-clean-punct

This model is a fine-tuned version of [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2449
- Bleu: 41.9443
- Gen Len: 31.5709

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| 1.129         | 1.0   | 144  | 1.2976          | 40.8925 | 31.6055 |
| 1.1063        | 2.0   | 288  | 1.2713          | 40.2012 | 31.346  |
| 0.9238        | 3.0   | 432  | 1.2449          | 41.9443 | 31.5709 |


### Framework versions

- Transformers 4.38.1
- Pytorch 2.1.0+cu121
- Datasets 2.17.1
- Tokenizers 0.15.2
