---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-d59ed0
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-mapped-v10
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-d59ed0" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-mapped-v10

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0077
- Precision: 0.9759
- Recall: 0.9896
- F1: 0.9827
- Accuracy: 0.9981

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
| 0.0641        | 0.3591 | 500  | 0.0299          | 0.8870    | 0.9455 | 0.9153 | 0.9914   |
| 0.0396        | 0.7181 | 1000 | 0.0148          | 0.9440    | 0.9813 | 0.9623 | 0.9955   |
| 0.0178        | 1.0768 | 1500 | 0.0098          | 0.9615    | 0.9864 | 0.9738 | 0.9970   |
| 0.0154        | 1.4359 | 2000 | 0.0120          | 0.9617    | 0.9905 | 0.9759 | 0.9967   |
| 0.0156        | 1.7950 | 2500 | 0.0096          | 0.9615    | 0.9811 | 0.9712 | 0.9970   |
| 0.0064        | 2.1537 | 3000 | 0.0080          | 0.9707    | 0.9924 | 0.9814 | 0.9976   |
| 0.0063        | 2.5127 | 3500 | 0.0070          | 0.9749    | 0.9937 | 0.9842 | 0.9979   |
| 0.0081        | 2.8718 | 4000 | 0.0072          | 0.9737    | 0.9902 | 0.9819 | 0.9980   |
| 0.0020        | 3.2305 | 4500 | 0.0071          | 0.9762    | 0.9931 | 0.9846 | 0.9981   |
| 0.0036        | 3.5896 | 5000 | 0.0075          | 0.9739    | 0.9890 | 0.9814 | 0.9980   |
| 0.0018        | 3.9487 | 5500 | 0.0074          | 0.9747    | 0.9856 | 0.9801 | 0.9980   |
| 0.0007        | 4.3074 | 6000 | 0.0077          | 0.9759    | 0.9896 | 0.9827 | 0.9981   |


### Framework versions

- Transformers 5.9.0
- Pytorch 2.12.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
