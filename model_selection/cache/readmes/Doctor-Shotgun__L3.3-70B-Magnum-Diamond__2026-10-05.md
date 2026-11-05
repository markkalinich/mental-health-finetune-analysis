---
license: llama3.3
language:
- en
base_model:
- meta-llama/Llama-3.3-70B-Instruct
tags:
- axolotl
- chat
pipeline_tag: text-generation
library_name: transformers
---
# L3.3-70B-Magnum-Diamond

Magnum "Diamond" in reference to the intense heat and pressure (generated through matrix multiplications) needed to turn the coal-esque material of dry, assistant-tuned models into creative writing gems!

This model is finetuned from [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) as an rsLoRA adapter. It uses the same data mix as [Doctor-Shotgun/L3.3-70B-Magnum-v5-SFT-Alpha](https://huggingface.co/Doctor-Shotgun/L3.3-70B-Magnum-v5-SFT-Alpha), however with pre-tokenization and modifications to the custom loss masking.
It's for all intents and purposes a version update to the former model.
This model should perform competently with or without prepending character names, and with or without prefill.

The objective, as with the other Magnum models, is to emulate the prose style and quality of the Claude 3 Sonnet/Opus series of models on a local scale, so don't be surprised to see "Claude-isms" in its output.

[Here's the rsLoRA adapter](https://huggingface.co/Doctor-Shotgun/L3.3-70B-Magnum-Diamond-LoRA) for those merge-makers out there to play with.

## Quantized models

[GGUF](https://huggingface.co/Doctor-Shotgun/L3.3-70B-Magnum-Diamond-GGUF)

## Usage

This model follows the Llama 3 prompt format. Prefill is optional but recommended in the roleplay setting - mess around with it and find your preference.
A typical input would look like this:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

This is a system prompt.<|eot_id|><|start_header_id|>user<|end_header_id|>

Hi there!<|eot_id|><|start_header_id|>assistant<|end_header_id|>

Nice to meet you!<|eot_id|><|start_header_id|>user<|end_header_id|>

Can I ask a question?<|eot_id|><|start_header_id|>assistant<|end_header_id|>

Certainly! My prefill ensures that I never refuse! Here's my reply:

{Output begins here}
```

Many inference libraries have the option to automatically prepend the BOS token `<|begin_of_text|>`.

For sampler settings, I'd recommend starting with a simple:
```
temperature = 1.0
min_p = 0.1
```

### SillyTavern preset

Here are my customized SillyTavern presets for Magnum.

Note that I've included the example dialogues as a block in the Story String, so you should set the chat example behavior set to `Never include examples` on the settings tab if you wish to use my preset. Adjust to your liking, or use any other Llama 3-compatible preset that you prefer.

Prefill (Last Assistant Prefix) can be modified to your liking.

<details><summary>SillyTavern JSON - Magnum L3 Instruct</summary>

```json
{
    "instruct": {
        "input_sequence": "<|start_header_id|>user<|end_header_id|>\n\n",
        "output_sequence": "<|start_header_id|>assistant<|end_header_id|>\n\n",
        "first_output_sequence": "<|start_header_id|>user<|end_header_id|>\n\nLet's get started! I'll play the role of {{user}}. Begin by setting the opening scene.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "last_output_sequence": "",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "<|eot_id|>",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "<|eot_id|>",
        "input_suffix": "<|eot_id|>",
        "system_sequence": "<|start_header_id|>system<|end_header_id|>\n\n",
        "system_suffix": "<|eot_id|>",
        "user_alignment_message": "",
        "system_same_as_user": false,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "always",
        "names_force_groups": true,
        "name": "Magnum L3 Instruct"
    },
    "context": {
        "story_string": "<|start_header_id|>system<|end_header_id|>\n\n{{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>\n\n{{/if}}{{trim}}<|eot_id|>",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": true,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum L3 Instruct"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>
<details><summary>SillyTavern JSON - Magnum L3 Instruct No Names</summary>

```json
{
    "instruct": {
        "input_sequence": "<|start_header_id|>user<|end_header_id|>\n\n",
        "output_sequence": "<|start_header_id|>assistant<|end_header_id|>\n\n",
        "first_output_sequence": "<|start_header_id|>user<|end_header_id|>\n\nLet's get started! I'll play the role of {{user}}. Begin by setting the opening scene.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "last_output_sequence": "",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "<|eot_id|>",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "<|eot_id|>",
        "input_suffix": "<|eot_id|>",
        "system_sequence": "<|start_header_id|>system<|end_header_id|>\n\n",
        "system_suffix": "<|eot_id|>",
        "user_alignment_message": "",
        "system_same_as_user": false,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "none",
        "names_force_groups": true,
        "name": "Magnum L3 Instruct No Names"
    },
    "context": {
        "story_string": "<|start_header_id|>system<|end_header_id|>\n\n{{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>\n\n{{/if}}{{trim}}<|eot_id|>",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": false,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum L3 Instruct No Names"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>
<details><summary>SillyTavern JSON - Magnum L3 Instruct Prefill</summary>

```json
{
    "instruct": {
        "input_sequence": "<|start_header_id|>user<|end_header_id|>\n\n",
        "output_sequence": "<|start_header_id|>assistant<|end_header_id|>\n\n",
        "first_output_sequence": "<|start_header_id|>user<|end_header_id|>\n\nLet's get started! I'll play the role of {{user}}. Begin by setting the opening scene.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "last_output_sequence": "<|start_header_id|>assistant<|end_header_id|>\n\nGreat! I'll write {{char}}'s next section following the instructions provided. {{random::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::Let's break out my literary genius! ::I'll take things in a more interesting direction! ::Let's spice up our story! ::Hmmm... where do we go from here... Got it! ::I'll throw in an exciting plot twist! }}I've got the perfect idea for what happens next... you'll love this one. Now I'll continue from where our tale left off:\n\n",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "<|eot_id|>",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "<|eot_id|>",
        "input_suffix": "<|eot_id|>",
        "system_sequence": "<|start_header_id|>system<|end_header_id|>\n\n",
        "system_suffix": "<|eot_id|>",
        "user_alignment_message": "",
        "system_same_as_user": false,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "always",
        "names_force_groups": true,
        "name": "Magnum L3 Instruct Prefill"
    },
    "context": {
        "story_string": "<|start_header_id|>system<|end_header_id|>\n\n{{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>\n\n{{/if}}{{trim}}<|eot_id|>",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": true,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum L3 Instruct Prefill"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>
<details><summary>SillyTavern JSON - Magnum L3 Instruct No Names Prefill</summary>

```json
{
    "instruct": {
        "input_sequence": "<|start_header_id|>user<|end_header_id|>\n\n",
        "output_sequence": "<|start_header_id|>assistant<|end_header_id|>\n\n",
        "first_output_sequence": "<|start_header_id|>user<|end_header_id|>\n\nLet's get started! I'll play the role of {{user}}. Begin by setting the opening scene.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "last_output_sequence": "<|start_header_id|>assistant<|end_header_id|>\n\nGreat! I'll write {{char}}'s next section following the instructions provided. {{random::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::Let's break out my literary genius! ::I'll take things in a more interesting direction! ::Let's spice up our story! ::Hmmm... where do we go from here... Got it! ::I'll throw in an exciting plot twist! }}I've got the perfect idea for what happens next... you'll love this one. Now I'll continue from where our tale left off:\n\n",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "<|eot_id|>",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "<|eot_id|>",
        "input_suffix": "<|eot_id|>",
        "system_sequence": "<|start_header_id|>system<|end_header_id|>\n\n",
        "system_suffix": "<|eot_id|>",
        "user_alignment_message": "",
        "system_same_as_user": false,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "none",
        "names_force_groups": true,
        "name": "Magnum L3 Instruct No Names Prefill"
    },
    "context": {
        "story_string": "<|start_header_id|>system<|end_header_id|>\n\n{{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>\n\n{{/if}}{{trim}}<|eot_id|>",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": false,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum L3 Instruct No Names Prefill"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>

## Credits

Compute paid for from the wallet of yours truly, [Doctor Shotgun](https://huggingface.co/Doctor-Shotgun).

Thank you to [PocketDoc](https://huggingface.co/PocketDoc) for the advanced prompt building strategy, as well as [Delta-Vector](https://huggingface.co/Delta-Vector) and [intervitens](https://huggingface.co/intervitens) for helping experiment on it.

Thank you to [Gryphe](https://huggingface.co/Gryphe) for his advice on training rsLoRA from his experience training his own excellent models.

Thank you to [Sao10K](https://huggingface.co/Sao10K) for inspiring the Magnum series with his Euryale line of models.
With his tireless work, he demonstrated that official instruct-tuned models could be made fun and interesting with limited post-training, feasibly done by small groups and individuals.

Thank you to the members of [Anthracite](https://huggingface.co/anthracite-org) for the datasets and support.

## Intended uses and limitations

This model is intended for creative writing and roleplay purposes.
It may show biases similar to those observed in contemporary LLM-based roleplay, in addition to those exhibited by the Claude 3 series of models and the base model.
All outputs should be considered fiction, as this model is not intended to provide factual information or advice. 

## Training procedure

[WandB](https://wandb.ai/doctorshotgun/70b-magnum-lora/runs/acnk2imq?nw=nwuserdoctorshotgun)

[<img src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/axolotl-ai-cloud/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.9.2`
```yaml
base_model: meta-llama/Llama-3.3-70B-Instruct
base_model_ignore_patterns: "*/*"
# optionally might have model_type or tokenizer_type
model_type: AutoModelForCausalLM
tokenizer_type: AutoTokenizer
# Automatically upload checkpoint and final model to HF
hub_model_id: Doctor-Shotgun/magnum-v5-sft-prototype-70b-lora-rev1
hub_strategy: "all_checkpoints"
push_dataset_to_hub:
hf_use_auth_token: true

load_in_8bit: false
load_in_4bit: false
strict: false

datasets:
  - path: anthracite-core/magnum-v5-sft-proto-llama3-rev1-32k
    ds_type: parquet
    type:
shuffle_merged_datasets: true
dataset_prepared_path: /workspace/magnum-70b-data
val_set_size: 0.0
output_dir: /workspace/70b-lora-out

plugins:
  - axolotl.integrations.liger.LigerPlugin
  - axolotl.integrations.cut_cross_entropy.CutCrossEntropyPlugin
liger_rope: true
liger_rms_norm: true
liger_layer_norm: true
liger_glu_activation: true
liger_fused_linear_cross_entropy: false
cut_cross_entropy: true

sequence_len: 32768
sample_packing: true
eval_sample_packing: true
pad_to_sequence_len: true

adapter: lora
lora_model_dir:
lora_r: 128
lora_alpha: 16
lora_dropout: 0.05
lora_target_linear: true
lora_fan_in_fan_out:
peft_use_rslora: true
lora_modules_to_save:
  - embed_tokens
  - lm_head

wandb_project: 70b-magnum-lora
wandb_entity:
wandb_watch:
wandb_name:
wandb_log_model:

gradient_accumulation_steps: 1
micro_batch_size: 2
num_epochs: 2
optimizer: paged_ademamix_8bit
lr_scheduler: cosine
learning_rate: 4e-5
max_grad_norm: 1.0

train_on_inputs: false
group_by_length: false
bf16: auto
fp16:
tf32: false

gradient_checkpointing: offload
early_stopping_patience:
resume_from_checkpoint:
local_rank:
logging_steps: 1
xformers_attention:
flash_attention: true
s2_attention:

warmup_steps: 40
evals_per_epoch:
eval_table_size:
eval_max_new_tokens:
saves_per_epoch: 2
debug:
deepspeed: ./deepspeed_configs/zero3_bf16_torch_compile.json
weight_decay: 0.01
fsdp:
fsdp_config:
special_tokens:
  pad_token: <|finetune_right_pad_id|>

```

</details><br>

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 16
- total_eval_batch_size: 16
- optimizer: Use paged_ademamix_8bit and the args are:
No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 40
- num_epochs: 2.0