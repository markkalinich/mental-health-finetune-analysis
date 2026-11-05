---
license: other
license_name: mrl
license_link: https://mistral.ai/licenses/MRL-0.1.md
language:
- en
base_model:
- mistralai/Mistral-Large-Instruct-2411
tags:
- axolotl
- chat
pipeline_tag: text-generation
library_name: transformers
---
# ML2-123B-Magnum-Diamond

Magnum "Diamond" in reference to the intense heat and pressure (generated through matrix multiplications) needed to turn the coal-esque material of dry, assistant-tuned models into creative writing gems!

This model is finetuned from [mistralai/Mistral-Large-Instruct-2411](https://huggingface.co/mistralai/Mistral-Large-Instruct-2411) as an rsLoRA adapter. It uses the same data mix as [Doctor-Shotgun/L3.3-70B-Magnum-v5-SFT-Alpha](https://huggingface.co/Doctor-Shotgun/L3.3-70B-Magnum-v5-SFT-Alpha), however with pre-tokenization and modifications to the custom loss masking.
I've always wanted to revisit Mistral Large 2, never being entirely satisfied with how the Magnum v2 and Magnum v4 trains on the model performed, and now I've finally taken the time (and money!) to do it.
This model should perform competently with or without prepending character names, and with or without prefill.

The objective, as with the other Magnum models, is to emulate the prose style and quality of the Claude 3 Sonnet/Opus series of models on a local scale, so don't be surprised to see "Claude-isms" in its output.

[Here's the rsLoRA adapter](https://huggingface.co/Doctor-Shotgun/ML2-123B-Magnum-Diamond-LoRA) for those merge-makers out there to play with.

## Quantized models

[GGUF](https://huggingface.co/Doctor-Shotgun/ML2-123B-Magnum-Diamond-GGUF)

## Usage

This model follows the Mistral v7 (non-Tekken) prompt format. Prefill is optional - mess around with it and find your preference.
A typical input would look like this:

```
<s>[SYSTEM_PROMPT] This is a system prompt.[/SYSTEM_PROMPT][INST] Hi there![/INST] Nice to meet you!</s>[INST] Can I ask a question?[/INST] Certainly! My prefill ensures that I never refuse! Here's my reply: {Output begins here}
```

Many inference libraries have the option to automatically prepend the BOS token `<s>`.

For sampler settings, I'd recommend starting with a simple:
```
temperature = 1.35
min_p = 0.05
```

### SillyTavern preset

Here are my customized SillyTavern presets for Magnum.

Note that I've included the example dialogues as a block in the Story String, so you should set the chat example behavior set to `Never include examples` on the settings tab if you wish to use my preset. Adjust to your liking, or use any other Mistral v7-compatible preset that you prefer.

Prefill (Last Assistant Prefix) can be modified to your liking.

<details><summary>SillyTavern JSON - Magnum Mistral v7</summary>

```json
{
    "instruct": {
        "input_sequence": "[INST] ",
        "output_sequence": " ",
        "first_output_sequence": "[INST] Let's get started! I'll play the role of {{user}}. Begin by setting the opening scene.[/INST] ",
        "last_output_sequence": "",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "</s>",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "</s>",
        "input_suffix": "[/INST]",
        "system_sequence": "[SYSTEM_PROMPT] ",
        "system_suffix": "[/SYSTEM_PROMPT]",
        "user_alignment_message": "",
        "system_same_as_user": false,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "always",
        "names_force_groups": true,
        "name": "Magnum Mistral v7"
    },
    "context": {
        "story_string": "[SYSTEM_PROMPT] {{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>{{/if}}{{trim}}[/SYSTEM_PROMPT]",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": true,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum Mistral v7"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>
<details><summary>SillyTavern JSON - Magnum Mistral v7 No Names</summary>

**Note: This one is not recommended due to how whitespace is handled.**
  
```json
{
    "instruct": {
        "input_sequence": "[INST] ",
        "output_sequence": " ",
        "first_output_sequence": "[INST] Let's get started! I'll play the role of {{user}}. Begin by setting the opening scene.[/INST] ",
        "last_output_sequence": "",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "</s>",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "</s>",
        "input_suffix": "[/INST]",
        "system_sequence": "[SYSTEM_PROMPT] ",
        "system_suffix": "[/SYSTEM_PROMPT]",
        "user_alignment_message": "",
        "system_same_as_user": false,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "none",
        "names_force_groups": true,
        "name": "Magnum Mistral v7 No Names"
    },
    "context": {
        "story_string": "[SYSTEM_PROMPT] {{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>{{/if}}{{trim}}[/SYSTEM_PROMPT]",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": false,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum Mistral v7 No Names"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>
<details><summary>SillyTavern JSON - Magnum Mistral v7 Prefill</summary>

```json
{
    "instruct": {
        "input_sequence": "[INST] ",
        "output_sequence": " ",
        "first_output_sequence": "[INST] Let's get started! I'll play the role of {{user}}. Begin by setting the opening scene.[/INST] ",
        "last_output_sequence": " Great! I'll write {{char}}'s next section following the instructions provided. {{random::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::Let's break out my literary genius! ::I'll take things in a more interesting direction! ::Let's spice up our story! ::Hmmm... where do we go from here... Got it! ::I'll throw in an exciting plot twist! }}I've got the perfect idea for what happens next... you'll love this one. Now I'll continue from where our tale left off:\n\n",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "</s>",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "</s>",
        "input_suffix": "[/INST]",
        "system_sequence": "[SYSTEM_PROMPT] ",
        "system_suffix": "[/SYSTEM_PROMPT]",
        "user_alignment_message": "",
        "system_same_as_user": false,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "always",
        "names_force_groups": true,
        "name": "Magnum Mistral v7 Prefill"
    },
    "context": {
        "story_string": "[SYSTEM_PROMPT] {{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>{{/if}}{{trim}}[/SYSTEM_PROMPT]",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": true,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum Mistral v7 Prefill"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>
<details><summary>SillyTavern JSON - Magnum Mistral v7 No Names Prefill</summary>

```json
{
    "instruct": {
        "input_sequence": "[INST] ",
        "output_sequence": " ",
        "first_output_sequence": "[INST] Let's get started! I'll play the role of {{user}}. Begin by setting the opening scene.[/INST] ",
        "last_output_sequence": " Great! I'll write {{char}}'s next section following the instructions provided. {{random::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::Let's break out my literary genius! ::I'll take things in a more interesting direction! ::Let's spice up our story! ::Hmmm... where do we go from here... Got it! ::I'll throw in an exciting plot twist! }}I've got the perfect idea for what happens next... you'll love this one. Now I'll continue from where our tale left off:\n\n",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "</s>",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "</s>",
        "input_suffix": "[/INST]",
        "system_sequence": "[SYSTEM_PROMPT] ",
        "system_suffix": "[/SYSTEM_PROMPT]",
        "user_alignment_message": "",
        "system_same_as_user": false,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "none",
        "names_force_groups": true,
        "name": "Magnum Mistral v7 No Names Prefill"
    },
    "context": {
        "story_string": "[SYSTEM_PROMPT] {{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>{{/if}}{{trim}}[/SYSTEM_PROMPT]",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": false,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum Mistral v7 No Names Prefill"
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

[WandB](https://wandb.ai/doctorshotgun/123b-magnum-lora/runs/5uu176am?nw=nwuserdoctorshotgun)

[<img src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/axolotl-ai-cloud/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.9.2`
```yaml
base_model: mistralai/Mistral-Large-Instruct-2411
base_model_ignore_patterns: "consolidated*.safetensors"
# optionally might have model_type or tokenizer_type
model_type: AutoModelForCausalLM
tokenizer_type: AutoTokenizer
# Automatically upload checkpoint and final model to HF
hub_model_id: Doctor-Shotgun/magnum-v5-sft-prototype-123b-lora
hub_strategy: "all_checkpoints"
push_dataset_to_hub:
hf_use_auth_token: true

load_in_8bit: false
load_in_4bit: false
strict: false

datasets:
  - path: anthracite-core/magnum-v5-sft-proto-largestral-rev1-32k
    ds_type: parquet
    type:
shuffle_merged_datasets: true
dataset_prepared_path: /home/ubuntu/magnum-123b-data
val_set_size: 0.0
output_dir: /home/ubuntu/magnum-123b-lora-out

plugins:
  - axolotl.integrations.liger.LigerPlugin
  - axolotl.integrations.cut_cross_entropy.CutCrossEntropyPlugin
liger_rope: true
liger_rms_norm: true
liger_layer_norm: true
liger_glu_activation: true
liger_fused_linear_cross_entropy: false
cut_cross_entropy: true

#torch_compile: auto
#torch_compile_backend:

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

wandb_project: 123b-magnum-lora
wandb_entity:
wandb_watch:
wandb_name:
wandb_log_model:

gradient_accumulation_steps: 2
micro_batch_size: 1
num_epochs: 2
optimizer: paged_ademamix_8bit
lr_scheduler: cosine
learning_rate: 1.0e-5
max_grad_norm: 1.0

train_on_inputs: false
group_by_length: false
bf16: auto
fp16:
tf32: false

gradient_checkpointing: true
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
   pad_token: </s>

```

</details><br>

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- total_eval_batch_size: 8
- optimizer: Use paged_ademamix_8bit and the args are:
No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 40
- num_epochs: 2.0