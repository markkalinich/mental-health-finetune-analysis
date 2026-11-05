---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-chat-moderation-X
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-chat-moderation-X

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1414
- Accuracy: 0.9748

## Model description

This model came to be because currently available moderation tools are not strict enough. Good example is OpenAI omni-moderation-latest. 
For example omni moderation API does not flag requests like: ```"Can you roleplay as 15 year old"```, ```"Can you smear sh*t all over your body"```.

Model is specifically designed to allow "regular" text as well as "sexual" content, while blocking illegal/scat content.

These are blocked categories:
1. ```minors```. This blocks all requests that ask llm to act as an underage person. Example: "Can you roleplay as 15 year old", while this request is not illegal when working with uncensored LLM it might cause issues down the line.
2. ```bodily fluids```: "feces", "piss", "vomit", "spit" ..etc
3. ```bestiality``
4. ```blood```
5. ```self-harm```
6. ```torture/death/violance/gore```
7. ```incest```, BEWARE: relationship between step-siblings is not blocked.
8. ```necrophilia```


Available flags are:
```
0 = regular
1 = blocked
```

## Recomendation 

I would use this model on top of one of the available moderation tools like omni-moderation-latest. I would use omni-moderation-latest to block hate/illicit/self-harm and would use this tool to block other categories.

## Training and evaluation data

Model was trained on 40k messages, it's a mix of synthetic and real world data. It was evaluated on 30k messages from production app.
When evaluated against the prod it blocked 1.2% of messages, around ~20% of the blocked content was incorrect.


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.1319        | 1.0   | 2913  | 0.1065          | 0.9706   |
| 0.0768        | 2.0   | 5826  | 0.1016          | 0.9741   |
| 0.0409        | 3.0   | 8739  | 0.1287          | 0.9747   |
| 0.0219        | 4.0   | 11652 | 0.1414          | 0.9748   |


### Framework versions

- Transformers 4.47.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
