---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-6d2a03
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v11
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-6d2a03" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v11

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0085
- Precision: 0.9779
- Recall: 0.9894
- F1: 0.9836
- Accuracy: 0.9982

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0729        | 0.3591 | 500  | 0.0400          | 0.8604    | 0.9370 | 0.8970 | 0.9889   |
| 0.0413        | 0.7181 | 1000 | 0.0143          | 0.9426    | 0.9709 | 0.9566 | 0.9956   |
| 0.0169        | 1.0768 | 1500 | 0.0108          | 0.9605    | 0.9868 | 0.9735 | 0.9968   |
| 0.0133        | 1.4359 | 2000 | 0.0086          | 0.9671    | 0.9903 | 0.9785 | 0.9974   |
| 0.0163        | 1.7950 | 2500 | 0.0098          | 0.9614    | 0.9778 | 0.9695 | 0.9968   |
| 0.0079        | 2.1537 | 3000 | 0.0099          | 0.9668    | 0.9880 | 0.9773 | 0.9971   |
| 0.0057        | 2.5127 | 3500 | 0.0077          | 0.9757    | 0.9912 | 0.9833 | 0.9979   |
| 0.0076        | 2.8718 | 4000 | 0.0085          | 0.9700    | 0.9868 | 0.9783 | 0.9976   |
| 0.0020        | 3.2305 | 4500 | 0.0074          | 0.9771    | 0.9905 | 0.9838 | 0.9982   |
| 0.0018        | 3.5896 | 5000 | 0.0077          | 0.9774    | 0.9900 | 0.9837 | 0.9982   |
| 0.0016        | 3.9487 | 5500 | 0.0079          | 0.9772    | 0.9884 | 0.9828 | 0.9982   |
| 0.0007        | 4.3074 | 6000 | 0.0084          | 0.9781    | 0.9916 | 0.9848 | 0.9982   |
| 0.0004        | 4.6664 | 6500 | 0.0085          | 0.9783    | 0.9889 | 0.9836 | 0.9982   |
| 0.0011        | 5.0    | 6965 | 0.0085          | 0.9779    | 0.9894 | 0.9836 | 0.9982   |


### Framework versions

- Transformers 5.9.0
- Pytorch 2.12.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
