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
- name: CeLLaTe3.0_Base_no_vague_adapted_pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe3.0_Base_no_vague_adapted_pubmed

This model is a fine-tuned version of [Mardiyyah/cellate2.0-tapt_base-LR_5e-05](https://huggingface.co/Mardiyyah/cellate2.0-tapt_base-LR_5e-05) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1976
- Precision: 0.8264
- Recall: 0.8264
- F1: 0.8264
- Accuracy: 0.9674

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

| Training Loss | Epoch   | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 1.3073        | 1.0417  | 100  | 0.5057          | 0.0       | 0.0    | 0.0    | 0.8644   |
| 0.3496        | 2.0833  | 200  | 0.2117          | 0.5943    | 0.5686 | 0.5812 | 0.9441   |
| 0.1555        | 3.125   | 300  | 0.1366          | 0.7816    | 0.8117 | 0.7963 | 0.9650   |
| 0.0919        | 4.1667  | 400  | 0.1622          | 0.8154    | 0.7708 | 0.7925 | 0.9631   |
| 0.0691        | 5.2083  | 500  | 0.1574          | 0.7502    | 0.8023 | 0.7754 | 0.9604   |
| 0.0497        | 6.25    | 600  | 0.1741          | 0.8023    | 0.7921 | 0.7972 | 0.9624   |
| 0.0373        | 7.2917  | 700  | 0.1761          | 0.7691    | 0.8045 | 0.7864 | 0.9621   |
| 0.03          | 8.3333  | 800  | 0.1903          | 0.7768    | 0.8198 | 0.7977 | 0.9617   |
| 0.0268        | 9.375   | 900  | 0.1791          | 0.7807    | 0.8460 | 0.8120 | 0.9643   |
| 0.0205        | 10.4167 | 1000 | 0.1952          | 0.7758    | 0.8132 | 0.7941 | 0.9626   |
| 0.0142        | 11.4583 | 1100 | 0.1846          | 0.8152    | 0.8318 | 0.8234 | 0.9672   |
| 0.0119        | 12.5    | 1200 | 0.1938          | 0.8319    | 0.8057 | 0.8186 | 0.9678   |
| 0.0105        | 13.5417 | 1300 | 0.2071          | 0.8196    | 0.8039 | 0.8117 | 0.9658   |
| 0.0093        | 14.5833 | 1400 | 0.1989          | 0.8264    | 0.8264 | 0.8264 | 0.9674   |
| 0.0073        | 15.625  | 1500 | 0.2105          | 0.8337    | 0.8087 | 0.8210 | 0.9669   |
| 0.0074        | 16.6667 | 1600 | 0.2177          | 0.8206    | 0.7954 | 0.8078 | 0.9656   |
| 0.006         | 17.7083 | 1700 | 0.2103          | 0.8273    | 0.8183 | 0.8227 | 0.9679   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
