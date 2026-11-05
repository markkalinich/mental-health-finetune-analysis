---
library_name: transformers
base_model: OpenMeditron/Meditron3-8B
tags:
- generated_from_trainer
model-index:
- name: mloscratch/homes/bbernath/meditron_instruct/instruction_tuned_model_with_ml4science_data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/axolotl-ai-cloud/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.0`
```yaml
base_model: OpenMeditron/Meditron3-8B
bf16: auto
output_dir: /mloscratch/homes/bbernath/meditron_instruct/instruction_tuned_model_with_ml4science_data
chat_template: llama3
datasets:
  - path: /mloscratch/homes/bbernath/meditron_instruct/datasets/mixtures/Instruction_tuning_mixture.jsonl
    type: chat_template
    ds_type: json
    split: train
    field_messages: conversations
    message_field_role: from
    message_field_content: value
  - path: /mloscratch/homes/bbernath/meditron_instruct/datasets/replay_data/datasets/pubmed_3B.jsonl
    type: completion
    ds_type: json
    field: text
    sample_ratio: 0.1
  - path: /mloscratch/homes/bbernath/meditron_instruct/datasets/replay_data/datasets/amboss_article.jsonl
    type: completion
    ds_type: json
    field: text
  - path: /mloscratch/homes/bbernath/meditron_instruct/datasets/replay_data/datasets/medmcqa.jsonl
    type: chat_template
    ds_type: json
    split: train
    field_messages: conversations
    message_field_role: from
    message_field_content: value
    sample_ratio: 0.5
  - path: /mloscratch/homes/bbernath/meditron_instruct/datasets/replay_data/datasets/pubmedqa.jsonl
    type: chat_template
    ds_type: json
    split: train
    field_messages: conversations
    message_field_role: from
    message_field_content: value
    sample_ratio: 0.2
  - path: /mloscratch/homes/bbernath/meditron_instruct/datasets/replay_data/datasets/medqa.jsonl
    type: chat_template
    ds_type: json
    split: train
    field_messages: conversations
    message_field_role: from
    message_field_content: value
shuffle_merged_datasets: true
dataset_processes: 64
flash_attention: true
sequence_len: 8192
gradient_accumulation_steps: 2
micro_batch_size: 2
train_on_inputs: false
group_by_length: false
pad_to_sequence_len: true
sample_packing: true
optimizer: adamw_torch
optim_args:
  fused: true
cosine_min_lr_ratio: 0.1
learning_rate: 1.0e-5
warmup_ratio: 0.0
weight_decay: 0.05
gradient_checkpointing: true
gradient_checkpointing_kwargs:
  use_reentrant: false
load_in_4bit: false
load_in_8bit: false
logging_steps: 1
num_epochs: 1
# saves_per_epoch: 1
# evals_per_epoch: 2
eval_set_size: 0.0
eval_table_size: null
lr_scheduler: cosine
max_grad_norm: 1.0
resume_from_checkpoint: null
special_tokens:
  pad_token: <|end_of_text|>
tf32: false
tokenizer_type: AutoTokenizer
type: LlamaForCausalLM
seed: 42
flash_attn_rms_norm: true
flash_attn_fuse_qkv: false
early_stopping_patience: 0
eval_steps: 3000
save_steps: 3000
load_best_model_at_end: true
xformers_attention: null
distributed:
  world_size: 5
  backend: nccl
deepspeed: /mloscratch/homes/bbernath/meditron_instruct/axolotl_config/ds_config.json

wandb_project: Meditron DDX
wandb_entity: alexs-team     
wandb_name: Instruction_tune_Meditron_8b_with_ML4Science_dataset_10000_first_try
```

</details><br>

# mloscratch/homes/bbernath/meditron_instruct/instruction_tuned_model_with_ml4science_data

This model is a fine-tuned version of [OpenMeditron/Meditron3-8B](https://huggingface.co/OpenMeditron/Meditron3-8B) on the None dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 6
- gradient_accumulation_steps: 2
- total_train_batch_size: 24
- total_eval_batch_size: 12
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=fused=True
- lr_scheduler_type: cosine
- num_epochs: 1

### Training results



### Framework versions

- Transformers 4.46.1
- Pytorch 2.5.1+cu124
- Datasets 3.0.1
- Tokenizers 0.20.3
