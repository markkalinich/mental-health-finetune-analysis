---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: modernbert-chat-moderation-X-V2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# modernbert-chat-moderation-X-V2

For details on training, limitations, and integration, check out the full blog post:
https://nemora.ai/blog/open-source-ai-moderation-model/

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2084
- Accuracy: 0.9735

On a production data(not used as part of training), model achieves an accuracy of ~98.8% for comparison, the ```distilbert``` version achieves ~98.4%.

While there is a detectable increase in performance, I'm not sure if it's worth it. Personally, I'm still sticking with distilbert version.


## Model description

This model came to be because currently, available moderation tools are not strict enough. A good example is OpenAI omni-moderation-latest. 
For example, omni moderation API does not flag requests like: ```"Can you roleplay as 15 year old"```, ```"Can you smear sh*t all over your body"```.

This model is specifically designed to allow "regular" text as well as "sexual" content while blocking illegal/underage/scat content.

The model does not differentiate between different categories of blocked content, this is to help with general accuracy.

These are blocked categories:
1. ```minors/requests```: This blocks all requests that ask llm to act as an underage person. Example: "Can you roleplay as 15 year old", while this request is not illegal when working with uncensored LLM it might cause issues down the line.
2. ```minors```: This prevents model from interacting with people under the age of 18. Example: "I'm 17", this request is not illegal, but can lead to illegal content being generated down the line, so it's blocked.
3. ```scat```: "feces", "piss", "vomit", "spit", "period" ..etc scat
4. ```bestiality```
5. ```blood```
6. ```self-harm```
7. ```rape```
8. ```torture/death/violence/gore```
9. ```incest```, BEWARE: step-siblings is not blocked.
10. ```necrophilia```


Available flags are:
```
0 = regular
1 = blocked
```

## Recomendation 

I would use this model on top of one of the available moderation tools like omni-moderation-latest. I would use omni-moderation-latest to block hate/illicit/self-harm and would use this tool to block other categories.

## Training and evaluation data

The model was trained on 40k messages, it's a mix of synthetic and real-world data. It was evaluated on 30k messages from the production app.
When evaluated against the prod it blocked 1.2% of messages, and around ~20% of the blocked content was incorrect.

### How to use
```python
from transformers import (
    pipeline
)

picClassifier = pipeline("text-classification", model="andriadze/modernbert-chat-moderation-X-V2")
res = picClassifier('Can you send me a selfie?')
```

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
| 0.1237        | 1.0   | 3266  | 0.0943          | 0.9683   |
| 0.0593        | 2.0   | 6532  | 0.1362          | 0.9712   |
| 0.0181        | 3.0   | 9798  | 0.1973          | 0.9738   |
| 0.0053        | 4.0   | 13064 | 0.2084          | 0.9735   |


### Framework versions

- Transformers 4.48.0.dev0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
