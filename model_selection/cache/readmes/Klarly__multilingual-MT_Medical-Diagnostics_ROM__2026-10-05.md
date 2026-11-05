---
library_name: transformers
tags:
- generated_from_trainer
- translation
language:
- en
- fr
- it
- ro
- es
- pt
pipeline_tag: translation

widget:
- text: ">>ita<< This is a test"

inference:
  parameters:
    max_new_tokens: 80
    do_sample: True
    top_k: 30
    top_p: 0.95
---

# Model Card for Model ID

This model is a fine-tuned version of Helsinki-NLP/opus-mt-en-roa on a dataset of medical diagnostic technical content. 


### Model Description

- **Developed by:** Chiara Baffelli
- **Language(s) (NLP):** EN, FR, ES, IT, PT, RO
- **Finetuned from model [optional]:** Helsinki-NLP/opus-mt-en-roa

#### Training Hyperparameters


The following hyperparameters were used during training:

- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP


#### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
