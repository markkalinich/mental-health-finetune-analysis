---
language: "en"
tags:
- distilbert-base-uncased
- text-classification
- patient
- doctor 

widget:
- text: "I've got flu"
- text: "I prescribe you some drugs and you need to stay at home for a couple of days"
- text: "Let's move to the theatre this evening!"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-patient-doctor-text-classifier-eng

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0516
- Accuracy: 0.9879

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0897        | 1.0   | 1547 | 0.0573          | 0.9865   |
| 0.0301        | 2.0   | 3094 | 0.0516          | 0.9879   |


### Framework versions

- Transformers 4.38.1
- Pytorch 2.1.2
- Datasets 2.1.0
- Tokenizers 0.15.2

- # How to Use 

```python
from transformers import pipeline
classifier = pipeline("text-classification", model="LukeGPT88/patient-doctor-text-classifier-eng")
classifier("I see you’ve set aside this special time to humiliate yourself in public.")
```

```python
Output:
[{'label': 'NEUTRAL', 'score': 0.9890775680541992}]
```

# Contact

Please reach out to [luca.flammia@gmail.com](luca.flammia@gmail.com) if you have any questions or feedback.

---
