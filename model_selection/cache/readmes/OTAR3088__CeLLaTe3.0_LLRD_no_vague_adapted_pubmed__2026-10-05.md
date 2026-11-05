---
library_name: transformers
license: mit
base_model: Mardiyyah/cellate2.0-tapt_base-LR_5e-05
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CeLLaTe3.0_LLRD_no_vague_adapted_pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe3.0_LLRD_no_vague_adapted_pubmed

This model is a fine-tuned version of [Mardiyyah/cellate2.0-tapt_base-LR_5e-05](https://huggingface.co/Mardiyyah/cellate2.0-tapt_base-LR_5e-05) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2007
- Precision: 0.8141
- Recall: 0.8144
- F1: 0.8143
- Accuracy: 0.9619

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 3407
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 1.1784        | 1.0417 | 100  | 0.3883          | 0.2271    | 0.1441 | 0.1763 | 0.8872   |
| 0.2627        | 2.0833 | 200  | 0.1683          | 0.6452    | 0.7211 | 0.6811 | 0.9538   |
| 0.1123        | 3.125  | 300  | 0.1480          | 0.8037    | 0.7503 | 0.7761 | 0.9613   |
| 0.0693        | 4.1667 | 400  | 0.1629          | 0.7995    | 0.8060 | 0.8027 | 0.9637   |
| 0.0477        | 5.2083 | 500  | 0.1577          | 0.8110    | 0.8171 | 0.8140 | 0.9652   |
| 0.0323        | 6.25   | 600  | 0.2010          | 0.8141    | 0.8144 | 0.8143 | 0.9619   |
| 0.0245        | 7.2917 | 700  | 0.1971          | 0.7691    | 0.7584 | 0.7637 | 0.9600   |
| 0.0185        | 8.3333 | 800  | 0.2117          | 0.8028    | 0.7837 | 0.7931 | 0.9623   |
| 0.0157        | 9.375  | 900  | 0.2137          | 0.7738    | 0.8397 | 0.8054 | 0.9611   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
