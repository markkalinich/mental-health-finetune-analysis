---
library_name: transformers
license: apache-2.0
base_model: albert-base-v2
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: empathetic_dialogues_context_classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# empathetic_dialogues_context_classification

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on empatheticDialogues dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6758
- F1: 0.5315
- Accuracy: 0.5315

## Access to Code
https://gist.github.com/zolfaShefreie/ae87ac2944e4f7b24609e0c28fde8449

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:--------:|
| 2.3973        | 1.0   | 558  | 2.2506          | 0.4080 | 0.4080   |
| 1.7624        | 2.0   | 1116 | 1.8044          | 0.4870 | 0.4870   |
| 1.5362        | 3.0   | 1674 | 1.6312          | 0.5094 | 0.5094   |
| 1.3443        | 4.0   | 2232 | 1.6225          | 0.5145 | 0.5145   |
| 1.2083        | 5.0   | 2790 | 1.5858          | 0.5355 | 0.5355   |
| 1.079         | 6.0   | 3348 | 1.5721          | 0.5409 | 0.5409   |
| 0.9522        | 7.0   | 3906 | 1.5888          | 0.5308 | 0.5308   |
| 0.8075        | 8.0   | 4464 | 1.6758          | 0.5315 | 0.5315   |


### Evaloation Result
on EmpatheticDialogues dataset (test split) and using whole history as input:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6503ebdce88eb2d0d51b33a8/NiJotkJsPDyihziT9gmz9.png)

on [empathetic-dialogues-contexts](https://huggingface.co/datasets/bdotloh/empathetic-dialogues-contexts) dataset (test split):
 

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6503ebdce88eb2d0d51b33a8/QusXIpjz0A0vf_R77szMu.png)


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Datasets 3.0.2
- Tokenizers 0.19.1
