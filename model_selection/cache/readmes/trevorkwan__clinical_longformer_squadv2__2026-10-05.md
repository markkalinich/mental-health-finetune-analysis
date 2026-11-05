---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
datasets:
- squad_v2
model-index:
- name: clinical_longformer_squadv2_maxlen320
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical_longformer_squadv2_maxlen320

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the squad_v2 dataset using a max_seq_length of 320.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

Tuning script used:

```python
set BASE_MODEL=yikuan8/Clinical-Longformer
set OUTPUT_DIR=U:\Documents...

python run_qa.py ^
  --model_name_or_path %BASE_MODEL% ^
  --dataset_name squad_v2 ^
  --do_train ^
  --do_eval ^
  --version_2_with_negative ^
  --per_device_train_batch_size 4 ^
  --per_device_eval_batch_size 4 ^
  --gradient_accumulation_steps 4 ^
  --learning_rate 2e-5 ^
  --num_train_epochs 3 ^
  --max_seq_length 320 ^
  --doc_stride 128 ^
  --weight_decay 0.01 ^
  --fp16 ^
  --output_dir %OUTPUT_DIR% ^
  --overwrite_output_dir
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.48.0.dev0
- Pytorch 2.0.1+cu117
- Datasets 3.0.1
- Tokenizers 0.21.0
