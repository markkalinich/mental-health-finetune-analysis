---
license: mit
base_model: dbmdz/bert-base-german-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: gecco-bert-base-german-uncased
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

# gecco-bert-base-german-uncased

**Text classification on German E-Counseling Conversations.**

This model is a fine-tuned version of [dbmdz/bert-base-german-uncased](https://huggingface.co/dbmdz/bert-base-german-uncased) 
trained with the German E-Counseling Conversation Dataset,
created at the Technische Hochschule Nürnberg (see [github.com/th-nuernberg/gecco-dataset](https://github.com/th-nuernberg/gecco-dataset)).

It achieves the following results on the evaluation set:
- Loss: 1.2341
- Accuracy: 0.6968
- F1: 0.4493

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
| 3.4151        | 1.0   | 20   | 3.0885          | 0.2935   | 0.0760 |
| 2.9316        | 2.0   | 40   | 2.7003          | 0.3484   | 0.1035 |
| 2.5556        | 3.0   | 60   | 2.3463          | 0.5032   | 0.2350 |
| 2.19          | 4.0   | 80   | 2.0714          | 0.5613   | 0.2841 |
| 1.904         | 5.0   | 100  | 1.8381          | 0.6      | 0.3085 |
| 1.6285        | 6.0   | 120  | 1.6712          | 0.6323   | 0.3633 |
| 1.4482        | 7.0   | 140  | 1.5518          | 0.6581   | 0.3774 |
| 1.2807        | 8.0   | 160  | 1.4796          | 0.6677   | 0.3880 |
| 1.1126        | 9.0   | 180  | 1.4207          | 0.6613   | 0.3787 |
| 1.0747        | 10.0  | 200  | 1.3461          | 0.6774   | 0.3885 |
| 0.9068        | 11.0  | 220  | 1.3097          | 0.6871   | 0.4132 |
| 0.8498        | 12.0  | 240  | 1.2893          | 0.6903   | 0.4235 |
| 0.8343        | 13.0  | 260  | 1.2549          | 0.7      | 0.4332 |
| 0.7375        | 14.0  | 280  | 1.2426          | 0.7      | 0.4497 |
| 0.7274        | 15.0  | 300  | 1.2385          | 0.7      | 0.4512 |
| 0.6916        | 16.0  | 320  | 1.2341          | 0.6968   | 0.4493 |


### Framework versions

- Transformers 4.35.1
- Pytorch 1.10.1+cu111
- Datasets 2.14.7
- Tokenizers 0.14.1