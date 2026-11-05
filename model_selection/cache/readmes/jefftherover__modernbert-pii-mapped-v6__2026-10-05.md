---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-1e06a3
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v6
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-1e06a3" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v6

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0069
- Precision: 0.9868
- Recall: 0.9938
- F1: 0.9903
- Accuracy: 0.9986

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
| 0.0560        | 0.3591 | 500  | 0.0254          | 0.9395    | 0.9736 | 0.9563 | 0.9939   |
| 0.0272        | 0.7181 | 1000 | 0.0155          | 0.9449    | 0.9615 | 0.9531 | 0.9949   |
| 0.0125        | 1.0768 | 1500 | 0.0150          | 0.9680    | 0.9869 | 0.9773 | 0.9964   |
| 0.0104        | 1.4359 | 2000 | 0.0095          | 0.9765    | 0.9909 | 0.9837 | 0.9977   |
| 0.0128        | 1.7950 | 2500 | 0.0068          | 0.9797    | 0.9899 | 0.9848 | 0.9978   |
| 0.0064        | 2.1537 | 3000 | 0.0064          | 0.9783    | 0.9887 | 0.9835 | 0.9980   |
| 0.0059        | 2.5127 | 3500 | 0.0059          | 0.9840    | 0.9935 | 0.9887 | 0.9983   |
| 0.0050        | 2.8718 | 4000 | 0.0062          | 0.9829    | 0.9949 | 0.9889 | 0.9982   |
| 0.0022        | 3.2305 | 4500 | 0.0065          | 0.9848    | 0.9953 | 0.9900 | 0.9984   |
| 0.0019        | 3.5896 | 5000 | 0.0067          | 0.9850    | 0.9953 | 0.9901 | 0.9984   |
| 0.0023        | 3.9487 | 5500 | 0.0060          | 0.9864    | 0.9938 | 0.9901 | 0.9985   |
| 0.0005        | 4.3074 | 6000 | 0.0070          | 0.9858    | 0.9942 | 0.9900 | 0.9985   |
| 0.0008        | 4.6664 | 6500 | 0.0068          | 0.9867    | 0.9936 | 0.9902 | 0.9986   |
| 0.0005        | 5.0    | 6965 | 0.0069          | 0.9868    | 0.9938 | 0.9903 | 0.9986   |


### Framework versions

- Transformers 5.8.1
- Pytorch 2.12.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
