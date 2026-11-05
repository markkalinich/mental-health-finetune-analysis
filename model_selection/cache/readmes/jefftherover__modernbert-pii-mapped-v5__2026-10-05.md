---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-956fe0
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v5
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-956fe0" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v5

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0078
- Precision: 0.9843
- Recall: 0.9934
- F1: 0.9888
- Accuracy: 0.9984

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
| 0.0611        | 0.3591 | 500  | 0.0332          | 0.9083    | 0.9605 | 0.9337 | 0.9914   |
| 0.0238        | 0.7181 | 1000 | 0.0109          | 0.9715    | 0.9859 | 0.9786 | 0.9969   |
| 0.0128        | 1.0768 | 1500 | 0.0084          | 0.9749    | 0.9912 | 0.9830 | 0.9976   |
| 0.0089        | 1.4359 | 2000 | 0.0081          | 0.9766    | 0.9904 | 0.9835 | 0.9977   |
| 0.0115        | 1.7950 | 2500 | 0.0072          | 0.9796    | 0.9925 | 0.9860 | 0.9979   |
| 0.0058        | 2.1537 | 3000 | 0.0075          | 0.9775    | 0.9916 | 0.9845 | 0.9979   |
| 0.0070        | 2.5127 | 3500 | 0.0060          | 0.9831    | 0.9940 | 0.9885 | 0.9983   |
| 0.0047        | 2.8718 | 4000 | 0.0067          | 0.9823    | 0.9948 | 0.9885 | 0.9982   |
| 0.0020        | 3.2305 | 4500 | 0.0074          | 0.9847    | 0.9952 | 0.9899 | 0.9984   |
| 0.0017        | 3.5896 | 5000 | 0.0070          | 0.9849    | 0.9942 | 0.9895 | 0.9984   |
| 0.0018        | 3.9487 | 5500 | 0.0067          | 0.9840    | 0.9932 | 0.9886 | 0.9984   |
| 0.0005        | 4.3074 | 6000 | 0.0078          | 0.9843    | 0.9934 | 0.9888 | 0.9984   |


### Framework versions

- Transformers 5.8.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
