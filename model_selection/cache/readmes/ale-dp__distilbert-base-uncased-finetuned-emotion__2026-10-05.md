---
license: apache-2.0
datasets:
- dair-ai/emotion
language:
- en
metrics:
- f1
- accuracy
base_model:
- distilbert-base-uncased 
library_name: transformers
pipeline_tag: text-classification
tags:
- distilbert
- pytorch
- emotion
- trainer

widget:
- text: "Interview preparation, I hate talking about myself, one dull subject matter!"
- text: "I'm in such a happy mood today i feel almost delighted and i havent done anything different today then i normally have it is wonderful"
- text: "I had every intention of doing more gardening this morning while it was still cool but i was just feeling so rotten"
- text: "Wow! I'm really impressed that Ashley can speak 7 languages, whereas I only speak one!"
- text: "No one wants to win the wild card because you have to play the Cubs on the road."
- text: "After Kylie had her heart broken by her ex-boyfriend, she felt so down and blue. I tried to cheer her up, but she just wants to be sad for awhile."
- text: "Jamie was in a bar with his friends one night when he saw a beautiful girl. He felt confident that night so he went to go talk to her."

---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-emotion
This model is a fine-tuned variant of distilbert-base-uncased using the emotion dataset. The evaluation results demonstrate its performance:

- Loss: 0.1595
- Accuracy: 93.35%
- F1 Score: 93.35%


### Hyperparameters

- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- lr_scheduler_type: linear
- num_epochs: 2

  
### Training results

| Epoch	 |  Training Loss  |  Validation Loss  |  Accuracy  |  F1
|:------:|:---------------:|:-----------------:|:----------:|:----------:|
| 1	     |  0.1703	    |     0.1709	       |  0.9355	|  0.9361    |
| 2	     |  0.1115	    |     0.1595	       |  0.9335	|  0.9335    |