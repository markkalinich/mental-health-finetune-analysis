---
language:
- ger
license: mit
base_model: deepset/gbert-large
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: th-nuernberg/gbert-large-german-counseling-gecco
  results: []
widget:
- text: "Was haben Sie bisher unternommen, um ihr Problem zu lösen?"
- text: "Hallo Peter, wie kann ich helfen?"
- text: "Ich bin hier, um zuzuhören. Wenn du mir erzählen möchtest, wie es dir geht, bin ich bereit."
- text: "Fällt es dir leicht, mit anderen Menschen in Kontakt zu treten?"
- text: "Welche Hobbys oder Freizeitaktivitäten würdest du gerne in der Zukunft ausprobieren?"
- text: "Haben Sie finanzielle Unterstützung von Ihrem Mann?"
- text: "Könnten Sie bitte genauer beschreiben, welche Schwierigkeiten durch diese technischen Probleme entstehen?"
- text: "Gibt es denn keine Hobbys, die du mit deinen Freunden gemeinsam machen kannst?"
- text: "Wo geht ihr Sohn zur Schule?"
- text: "Haben sie gemeinsame Hobbies mit Ihren Freunden?"  
---

# th-nuernberg/gbert-large-german-counseling-gecco

This model is a fine-tuned version of [deepset/gbert-large](https://huggingface.co/deepset/gbert-large) 
trained with the German E-Counseling Conversation Dataset,
created at the Technische Hochschule Nürnberg (see [github.com/th-nuernberg/gecco-dataset](https://github.com/th-nuernberg/gecco-dataset)).

It achieves the following results on the evaluation set: Accuracy 0.78, F1 0.66.

Contact: 
- [Prof. Dr. Jens Albrecht](https://www.th-nuernberg.de/person/albrecht-jens/)
- [Prof. Dr. Robert Lehmann](https://www.th-nuernberg.de/person/lehmann-robert/)

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 3.3924        | 1.0   | 20   | 2.9410          | 0.2032   | 0.0418 |
| 2.7028        | 2.0   | 40   | 2.2499          | 0.4806   | 0.2366 |
| 2.0665        | 3.0   | 60   | 1.7404          | 0.6129   | 0.3537 |
| 1.5           | 4.0   | 80   | 1.3602          | 0.6839   | 0.4109 |
| 1.0794        | 5.0   | 100  | 1.1377          | 0.7355   | 0.4971 |
| 0.7965        | 6.0   | 120  | 1.0123          | 0.7548   | 0.5518 |
| 0.6438        | 7.0   | 140  | 0.9806          | 0.7613   | 0.5547 |
| 0.5039        | 8.0   | 160  | 0.9452          | 0.7742   | 0.6019 |
| 0.4058        | 9.0   | 180  | 0.9218          | 0.7774   | 0.5907 |
| 0.3363        | 10.0  | 200  | 0.9373          | 0.7710   | 0.6157 |
| 0.2451        | 11.0  | 220  | 0.9751          | 0.7548   | 0.5955 |
| 0.1997        | 12.0  | 240  | 0.9197          | 0.7839   | 0.6526 |
| 0.1765        | 13.0  | 260  | 0.9187          | 0.7806   | 0.6425 |
| 0.1453        | 14.0  | 280  | 0.9431          | 0.7742   | 0.6357 |
| 0.1216        | 15.0  | 300  | 0.9388          | 0.7839   | 0.6534 |
| 0.1097        | 16.0  | 320  | 0.9290          | 0.7839   | 0.6645 |


### Framework versions

- Transformers 4.35.1
- Pytorch 1.10.1+cu111
- Datasets 2.14.7
- Tokenizers 0.14.1
