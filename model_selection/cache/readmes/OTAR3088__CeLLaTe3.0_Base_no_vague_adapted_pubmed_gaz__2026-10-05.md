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
- name: CeLLaTe3.0_Base_no_vague_adapted_pubmed_gaz
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe3.0_Base_no_vague_adapted_pubmed_gaz

This model is a fine-tuned version of [Mardiyyah/cellate2.0-tapt_base-LR_5e-05](https://huggingface.co/Mardiyyah/cellate2.0-tapt_base-LR_5e-05) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1429
- Precision: 0.8007
- Recall: 0.8511
- F1: 0.8251
- Accuracy: 0.9656

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
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 1.8192        | 0.2625 | 100  | 1.0343          | 0.0       | 0.0    | 0.0    | 0.8644   |
| 0.6494        | 0.5249 | 200  | 0.4040          | 0.2492    | 0.1613 | 0.1958 | 0.8851   |
| 0.3634        | 0.7874 | 300  | 0.2682          | 0.4259    | 0.3941 | 0.4094 | 0.9181   |
| 0.2352        | 1.0499 | 400  | 0.1609          | 0.7297    | 0.7455 | 0.7375 | 0.9588   |
| 0.1488        | 1.3123 | 500  | 0.1463          | 0.7468    | 0.8138 | 0.7789 | 0.9599   |
| 0.1157        | 1.5748 | 600  | 0.1597          | 0.8004    | 0.7518 | 0.7754 | 0.9610   |
| 0.0962        | 1.8373 | 700  | 0.1630          | 0.7967    | 0.7250 | 0.7592 | 0.9596   |
| 0.0742        | 2.0997 | 800  | 0.1551          | 0.8050    | 0.7888 | 0.7968 | 0.9636   |
| 0.0564        | 2.3622 | 900  | 0.1445          | 0.8005    | 0.8511 | 0.8250 | 0.9656   |
| 0.0518        | 2.6247 | 1000 | 0.1700          | 0.7614    | 0.8448 | 0.8009 | 0.9605   |
| 0.0448        | 2.8871 | 1100 | 0.1857          | 0.7895    | 0.8102 | 0.7997 | 0.9620   |
| 0.0317        | 3.1496 | 1200 | 0.1977          | 0.8013    | 0.8240 | 0.8125 | 0.9619   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
