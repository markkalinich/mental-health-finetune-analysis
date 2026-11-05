---
language:
- en
license: apache-2.0
tags:
- pytorch
- emotion-classification
base_model: bert-base-cased
datasets:
- dair-ai/emotion
pipeline_tag: text-classification
model-index:
- name: bert-finetuned-emotion
  results: []
library_name: transformers
---


# bert-finetuned-emotion

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the [emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1656

## Model description

The `bert-finetuned-emotion` model is a fine-tuned version of the **BERT** model for text classification, specifically trained for emotion classification tasks.
It utilizes the **BERT** architecture, a powerful pre-trained language representation model developed by Google,
and fine-tunes it on the `dair-ai/emotion dataset`. The model aims to predict the emotion associated with a given text input.



## Intended uses & limitations

#### Intended Uses

- **Emotion classification in text**: The model can be used to classify the emotions conveyed in textual data, aiding applications such as sentiment analysis, customer feedback analysis, and social media monitoring.
- **Integration into applications**: This model can be integrated into various applications and platforms to provide emotion analysis functionalities. 

#### Limitations

- **Domain-specific limitations**: The model's performance may vary depending on the domain of the text data. It is primarily trained on general textual data and may not perform optimally on specialized domains.
- **Language limitations**: The model is trained primarily on English text and may not generalize well to other languages without further adaptation.
- **Bias and fairness**: As with any machine learning model, biases present in the training data may be reflected in the model's predictions. Care should be taken to mitigate biases, especially when deploying the model in sensitive applications.

## Training and evaluation data

#### Dataset

The model is trained on the `dair-ai/emotion` dataset, which contains text samples labeled with emotions such as **love**, **surprise**, **joy**, **sadness**, **anger** and **fear**.
The dataset provides a diverse range of textual expressions of emotions, enabling the model to learn patterns associated with different emotional states.

#### Data Preprocessing

Before training, the text data undergoes preprocessing steps such as tokenization, lowercasing, and truncation to prepare it for input into the **BERT** model.

## Training procedure

The model is fine-tuned using transfer learning on top of the pre-trained **BERT** model.
During training, the parameters of the **BERT** model are fine-tuned using backpropagation and gradient descent optimization to minimize a loss function,
typically categorical cross-entropy, on the emotion classification task. The fine-tuning process involves adjusting the model's weights based on the labeled examples in the `dair-ai/emotion` dataset.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.2653        | 1.0   | 2000 | 0.2193          |
| 0.1552        | 2.0   | 4000 | 0.1690          |
| 0.1028        | 3.0   | 6000 | 0.1656          |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1