---
library_name: transformers
base_model: ProsusAI/finbert
tags:
- text-classification
- finance
- sentiment-analysis
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: finbert-financial-sentiment
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finbert-financial-sentiment

This model is a fine-tuned version of [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4223
- Accuracy: 0.8802
- F1 Macro: 0.8679

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Macro |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.4118        | 1.0   | 194  | 0.3598          | 0.8698   | 0.8445   |
| 0.2097        | 2.0   | 388  | 0.3254          | 0.8763   | 0.8597   |
| 0.1185        | 3.0   | 582  | 0.4130          | 0.8814   | 0.8654   |
| 0.0258        | 4.0   | 776  | 0.4223          | 0.8802   | 0.8679   |


### Framework versions

- Transformers 5.7.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.5
- Tokenizers 0.22.2
