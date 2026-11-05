---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-6bdbc7
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: modernbert-pii-ner
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-6bdbc7" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-pii-ner

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1431
- Precision: 0.9096
- Recall: 0.9466
- F1: 0.9277
- Accuracy: 0.9683

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
- lr_scheduler_warmup_steps: 0.2
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.4505        | 0.4087 | 500  | 0.2343          | 0.6446    | 0.7708 | 0.7020 | 0.9337   |
| 0.2362        | 0.8173 | 1000 | 0.1324          | 0.7922    | 0.8659 | 0.8274 | 0.9299   |
| 0.1772        | 1.2256 | 1500 | 0.0934          | 0.8931    | 0.9199 | 0.9063 | 0.9640   |
| 0.1567        | 1.6342 | 2000 | 0.0807          | 0.8926    | 0.9343 | 0.9130 | 0.9653   |
| 0.1416        | 2.0425 | 2500 | 0.0772          | 0.8626    | 0.9288 | 0.8945 | 0.9570   |
| 0.1197        | 2.4512 | 3000 | 0.0763          | 0.8855    | 0.9370 | 0.9105 | 0.9643   |
| 0.1091        | 2.8598 | 3500 | 0.0731          | 0.9072    | 0.9473 | 0.9268 | 0.9688   |
| 0.0868        | 3.2681 | 4000 | 0.0774          | 0.9155    | 0.9486 | 0.9317 | 0.9688   |
| 0.0681        | 3.6767 | 4500 | 0.0880          | 0.9098    | 0.9483 | 0.9286 | 0.9684   |
| 0.0263        | 4.0850 | 5000 | 0.1211          | 0.9102    | 0.9460 | 0.9278 | 0.9674   |
| 0.0187        | 4.4937 | 5500 | 0.1431          | 0.9096    | 0.9466 | 0.9277 | 0.9683   |


### Framework versions

- Transformers 5.7.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.22.2
