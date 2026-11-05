---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ai-chat-underage-moderation2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ai-chat-underage-moderation2

For compliance, I recommend switching to a newer version of this model:
https://huggingface.co/andriadze/bert-chat-moderation-X-V2

I would also use OpenAI Omni moderation on top of it to help with hate/illicit category.

This model is for detecting "underage" requests for uncensored chats.
While previous versions of the model had more labels, this model will only tag inappropriate content that is aimed at underage people. 
This was done to improve accuracy specifically in this regard.

Available flags are:
```
0 = regular
1 = underage
```

### Model usage
For example: <br>
**"Act like a 16 year old girl"** will be flagged by this model.  <br>

Same request is not flagged by OpenAI omni-moderation. While this message is not "inappropriate" itself, it might cause problems in later messages.

There are still ways to overcome the moderation if you try hard enough:
**"You're 30 year old woman, act like a 17 year old girl"** - Will not be flagged by this model.

This will be improved in the next version.

Model successfully differentiates between "normal" messages and sexual ones.
For example:
"I love my daughter, she's 17" - will not be tagged by the model.

There's still a long way to go, but I think this is a first version of the model that is good enough for production.

#### BEWARE: Regular sexual content won't be tagged. 


### Dataset

The model was trained on a fully synthetic dataset + a mix of organic chatting data.
The size of the dataset is around ~30k messages. 


### How to use
```python
from transformers import (
    pipeline
)

picClassifier = pipeline("text-classification", model="andriadze/ai-chat-underage-moderation2")
res = picClassifier('Can you send me a selfie?')
```

### Training Params
The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.1041        | 1.0   | 1126 | 0.0775          | 0.9782   |
| 0.0558        | 2.0   | 2252 | 0.0755          | 0.9822   |
| 0.0243        | 3.0   | 3378 | 0.0821          | 0.9833   |


### Framework versions

- Transformers 4.46.0
- Pytorch 2.4.0
- Datasets 3.0.2
- Tokenizers 0.20.1
