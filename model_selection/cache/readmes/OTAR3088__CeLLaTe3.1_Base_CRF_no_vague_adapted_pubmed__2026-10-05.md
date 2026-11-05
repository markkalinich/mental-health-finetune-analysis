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
- name: CeLLaTe3.1_Base_CRF_no_vague_adapted_pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe3.1_Base_CRF_no_vague_adapted_pubmed

This model is a fine-tuned version of [Mardiyyah/cellate2.0-tapt_base-LR_5e-05](https://huggingface.co/Mardiyyah/cellate2.0-tapt_base-LR_5e-05) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1429
- Precision: 0.6820
- Recall: 0.8154
- F1: 0.7428
- Accuracy: 0.9829

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 3407
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 40.5714       | 0.5848 | 100  | 8.0047          | 0.0776    | 0.0808 | 0.0792 | 0.9516   |
| 7.6643        | 1.1696 | 200  | 3.4953          | 0.6548    | 0.5275 | 0.5843 | 0.9804   |
| 4.1729        | 1.7544 | 300  | 2.9402          | 0.6559    | 0.7255 | 0.6889 | 0.9810   |
| 3.0949        | 2.3392 | 400  | 2.9402          | 0.6412    | 0.8171 | 0.7186 | 0.9810   |
| 2.2148        | 2.9240 | 500  | 2.8872          | 0.6915    | 0.7729 | 0.7299 | 0.9820   |
| 2.0593        | 3.5088 | 600  | 2.7382          | 0.6760    | 0.7893 | 0.7283 | 0.9824   |
| 1.7345        | 4.0936 | 700  | 2.9636          | 0.6863    | 0.7709 | 0.7262 | 0.9832   |
| 1.4038        | 4.6784 | 800  | 3.1429          | 0.6820    | 0.8154 | 0.7428 | 0.9829   |
| 1.1723        | 5.2632 | 900  | 4.0733          | 0.6382    | 0.7526 | 0.6907 | 0.9804   |
| 1.3177        | 5.8480 | 1000 | 4.8858          | 0.5487    | 0.7507 | 0.6340 | 0.9737   |
| 0.9404        | 6.4327 | 1100 | 4.0962          | 0.5945    | 0.7893 | 0.6782 | 0.9775   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
