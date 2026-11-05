---
---

[<img src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/axolotl-ai-cloud/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.9.2`
```yaml
base_model: /capstor/scratch/cscs/bbernath/models/meditron-70B
chat_template: llama3
bfloat16: true
output_dir: /capstor/store/cscs/swissai/a06/meditron/models/meditron_CHUV_2 #/capstor/scratch/cscs/bbernath/models/meditron_CHUV
dataset_prepared_path: /capstor/scratch/cscs/bbernath/dataset/
#  - path: /capstor/store/cscs/swissai/a06/meditron/datasets/masked/special_mixture/instruction_tuning_mixture.jsonl
#    type: chat_template
#    ds_type: json
#    split: train
#    field_messages: conversations
#    message_field_role: from
#    message_field_content: value
#pretraining_dataset:
#  - path: json
#    data_files:
#      - /capstor/store/cscs/swissai/a06/meditron/datasets/pretrain/pubmed/pubmed_3B.jsonl
#      - /capstor/store/cscs/swissai/a06/meditron/datasets/pretrain/fineweb/fineweb_400M_anglais.jsonl
#    type: pretrain
datasets:
  - path: /capstor/store/cscs/swissai/a06/meditron/datasets/masked/gemini/moove_gemini_2.jsonl
    type: chat_template
    ds_type: json
    split: train
    field_messages: conversations
    message_field_role: from
    message_field_content: value

shuffle_merged_datasets: true
dataset_processes: 128
# max_steps: 1500
flash_attention: true
sequence_len: 8192
gradient_accumulation_steps: 1
micro_batch_size: 1
train_on_inputs: false
group_by_length: false
pad_to_sequence_len: true
sample_packing: true
optimizer: adamw_torch
optim_args:
  fused: true
cosine_min_lr_ratio: 0.1
learning_rate: 5.0e-6
warmup_ratio: 0
weight_decay: 0.05
gradient_checkpointing: true
gradient_checkpointing_kwargs:
  use_reentrant: false
load_in_4bit: false
load_in_8bit: false
num_epochs: 1
saves_per_epoch: 1
# evals_per_epoch: 1
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
flash_attn_rms_norm: true
flash_attn_fuse_qkv: false
early_stopping_patience: 0
wandb_entity: alexs-team
wandb_name: meditron-CHUV-llama-gemini
wandb_project: Meditron DDX
wandb_watch: gradients
xformers_attention: null
logging_steps: 1
deepspeed: /capstor/users/cscs/bbernath/meditron/axolotl_config/deepspeed_new.json

```

</details><br>

# capstor/store/cscs/swissai/a06/meditron/models/meditron_CHUV_2

This model was trained from scratch on the /capstor/store/cscs/swissai/a06/meditron/datasets/masked/gemini/moove_gemini_2.jsonl dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 32
- total_train_batch_size: 32
- total_eval_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=fused=True
- lr_scheduler_type: cosine
- num_epochs: 1.0

### Training results



### Framework versions

- Transformers 4.51.3
- Pytorch 2.7.0a0+79aa17489c.nv25.04
- Datasets 3.6.0
- Tokenizers 0.21.1
