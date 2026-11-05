---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-multilingual-cased
tags:
- generated_from_trainer
- sentiment-analysis
metrics:
- accuracy
model-index:
- name: result
  results: []
datasets:
- AiresPucrs/sentiment-analysis-pt
language:
- pt
pipeline_tag: text-classification
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-sentiment-analysis-pt

This model is a fine-tuned version of [distilbert/distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) trained on the [AiresPucrs/sentiment-analysis-pt](https://huggingface.co/datasets/AiresPucrs/sentiment-analysis-pt) dataset available on Hugging Face.
It achieves the following results on the evaluation set:
- Loss: 0.3191
- Accuracy: 0.9076

## Quick Start

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Octavio-Santana/distilbert-base-sentiment-analysis-pt"
)
classifier.model.config.id2label = {0: 'negativo', 1: 'positivo'}

result = classifier("Fiquei extremamente satisfeito com o atendimento, superou todas as minhas expectativas.")
# [{'label': 'positivo', 'score': 0.7609153985977173}]
```

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Accuracy | Validation Loss |
|:-------------:|:-----:|:-----:|:--------:|:---------------:|
| 0.2665        | 1.0   | 4252  | 0.8872   | 0.2863          |
| 0.2095        | 2.0   | 8504  | 0.9064   | 0.2736          |
| 0.1450        | 3.0   | 12756 | 0.9076   | 0.3191          |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.5.0
- Tokenizers 0.22.2