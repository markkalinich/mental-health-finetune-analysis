---
library_name: transformers
license: mit
base_model: xlm-roberta-base
tags:
- generated_from_trainer
- ml-intern
metrics:
- precision
- recall
- f1
model-index:
- name: spanish-gdpr-pii-ner-v7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# spanish-gdpr-pii-ner-v7

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0016
- Precision: 0.9981
- Recall: 0.9981
- F1: 0.9981
- F1 Person Name: 1.0
- Sup Person Name: 25
- F1 Phone Es: 1.0
- Sup Phone Es: 18
- F1 Address Es: 1.0
- Sup Address Es: 25
- F1 Date Of Birth: 1.0
- Sup Date Of Birth: 9
- F1 Username: 1.0
- Sup Username: 50
- F1 Vehicle Plate Es: 1.0
- Sup Vehicle Plate Es: 11
- F1 Health Data: 1.0
- Sup Health Data: 17
- F1 Genetic Data: 1.0
- Sup Genetic Data: 225
- F1 Biometric Data: 1.0
- Sup Biometric Data: 25
- F1 Ethnic Origin: 1.0
- Sup Ethnic Origin: 25
- F1 Political Opinion: 0.9796
- Sup Political Opinion: 25
- F1 Religious Belief: 1.0
- Sup Religious Belief: 18
- F1 Union Membership: 0.9804
- Sup Union Membership: 25
- F1 Criminal Record: 1.0
- Sup Criminal Record: 25

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | F1 Person Name | Sup Person Name | F1 Phone Es | Sup Phone Es | F1 Address Es | Sup Address Es | F1 Date Of Birth | Sup Date Of Birth | F1 Username | Sup Username | F1 Vehicle Plate Es | Sup Vehicle Plate Es | F1 Health Data | Sup Health Data | F1 Genetic Data | Sup Genetic Data | F1 Biometric Data | Sup Biometric Data | F1 Ethnic Origin | Sup Ethnic Origin | F1 Political Opinion | Sup Political Opinion | F1 Religious Belief | Sup Religious Belief | F1 Union Membership | Sup Union Membership | F1 Criminal Record | Sup Criminal Record |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------------:|:---------------:|:-----------:|:------------:|:-------------:|:--------------:|:----------------:|:-----------------:|:-----------:|:------------:|:-------------------:|:--------------------:|:--------------:|:---------------:|:---------------:|:----------------:|:-----------------:|:------------------:|:----------------:|:-----------------:|:--------------------:|:---------------------:|:-------------------:|:--------------------:|:-------------------:|:--------------------:|:------------------:|:-------------------:|
| 0.0516        | 1.0   | 582  | 0.0487          | 0.9007    | 0.9369 | 0.9185 | 1.0            | 25              | 0.8889      | 18           | 1.0           | 25             | 1.0              | 9                 | 1.0         | 50           | 1.0                 | 11                   | 0.4762         | 17              | 1.0             | 225              | 0.72              | 25                 | 0.9412           | 25                | 0.4615               | 25                    | 1.0                 | 18                   | 0.7576              | 25                   | 0.8772             | 25                  |
| 0.0074        | 2.0   | 1164 | 0.0063          | 0.9905    | 0.9943 | 0.9924 | 1.0            | 25              | 0.9444      | 18           | 1.0           | 25             | 0.9474           | 9                 | 1.0         | 50           | 1.0                 | 11                   | 1.0            | 17              | 1.0             | 225              | 1.0               | 25                 | 0.9412           | 25                | 0.9796               | 25                    | 1.0                 | 18                   | 0.9804              | 25                   | 1.0                | 25                  |
| 0.0041        | 3.0   | 1746 | 0.0029          | 0.9943    | 0.9962 | 0.9952 | 1.0            | 25              | 0.9444      | 18           | 1.0           | 25             | 0.9474           | 9                 | 1.0         | 50           | 1.0                 | 11                   | 1.0            | 17              | 1.0             | 225              | 1.0               | 25                 | 1.0              | 25                | 0.9796               | 25                    | 1.0                 | 18                   | 0.9804              | 25                   | 1.0                | 25                  |
| 0.0021        | 4.0   | 2328 | 0.0019          | 0.9981    | 0.9981 | 0.9981 | 1.0            | 25              | 1.0         | 18           | 1.0           | 25             | 1.0              | 9                 | 1.0         | 50           | 1.0                 | 11                   | 1.0            | 17              | 1.0             | 225              | 1.0               | 25                 | 1.0              | 25                | 0.9796               | 25                    | 1.0                 | 18                   | 0.9804              | 25                   | 1.0                | 25                  |
| 0.0023        | 5.0   | 2910 | 0.0016          | 0.9981    | 0.9981 | 0.9981 | 1.0            | 25              | 1.0         | 18           | 1.0           | 25             | 1.0              | 9                 | 1.0         | 50           | 1.0                 | 11                   | 1.0            | 17              | 1.0             | 225              | 1.0               | 25                 | 1.0              | 25                | 0.9796               | 25                    | 1.0                 | 18                   | 0.9804              | 25                   | 1.0                | 25                  |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.11.0+cu130
- Datasets 4.0.0
- Tokenizers 0.22.2

<!-- ml-intern-provenance -->
## Generated by ML Intern

This model repository was generated by [ML Intern](https://github.com/huggingface/ml-intern), an agent for machine learning research and development on the Hugging Face Hub.

- Try ML Intern: https://smolagents-ml-intern.hf.space
- Source code: https://github.com/huggingface/ml-intern

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = 'kierandesmond/spanish-gdpr-pii-ner-v7'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
```

For non-causal architectures, replace `AutoModelForCausalLM` with the appropriate `AutoModel` class.
