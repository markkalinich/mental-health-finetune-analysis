---
license: mit
base_model: facebook/bart-large-cnn
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: conversation-summ
  results: []
datasets:
- har1/MTS_Dialogue-Clinical_Note
language:
- en
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# HealthScribe (A Clinical Note Generator)

This model is a fine-tuned version of [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) on a modified version of [MTS-Dialog Dataset](https://github.com/abachaa/MTS-Dialog) dataset.


## Model description

The model was developed for the project [HealthScirbe](https://github.com/hari-krishnan-88/HealthScribe-Clinical_Note_Generator). This model is integrated with a Flask web application. The project is a web application that allows users to generate clinical notes from transcribed ASR(Automatic Speech Recognition) data of conversations between doctors and patients.

### TEST DATA Sample For Inference (More given in [`test.txt`](https://huggingface.co/har1/HealthScribe-Clinical_Note_Generator/blob/main/test.txt))

You can refer [`test.txt`](https://huggingface.co/har1/HealthScribe-Clinical_Note_Generator/blob/main/test.txt) for further examples of conversations.

```
"Doctor: Hi there, I love that dress, very pretty! 
Patient: Thank you for complementing a seventy-two-year-old patient.
Doctor: No, I mean it, seriously. Okay, so you were admitted here in May two thousand nine. You have a history of hypertension, and on June eighteenth two thousand nine you had bad abdominal pain diarrhea and cramps.
Patient: Yes, they told me I might have C Diff? They did a CT of my abdomen and that is when they thought I got the infection.
Doctor: Yes, it showed evidence of diffuse colitis, so I believe they gave you IV antibiotics?
Patient: Yes they did. 
Doctor: Yeah I see here, Flagyl and Levaquin. They started IV Reglan as well for your vomiting.
Patient: Yes, I was very nauseous. Vomited as well.
Doctor: After all this I still see your white blood cells high. Are you still nauseous? 
Patient: No, I do not have any nausea or vomiting, but still have diarrhea. Due to all that diarrhea I feel very weak.
Doctor: Okay. Anything else any other symptoms?
Patient: Actually no. Everything's well.
Doctor: Great.
Patient: Yeah."
```


## Intended uses & limitations

The model is used to generate clinical notes from doctor-patient conversation data(ASR). This model has certain limitations like : 
- N/A output generation is low. Sometimes None is produced
- When the input data is composed of very minimal character tokens or if input is very large it starts to hallucinate. 


# Training Metrics

## Training and evaluation data

The model achieves the following results on the evaluation set:

- **Loss:** 0.1562
- **Rouge1:** 54.3238
- **Rouge2:** 34.2678
- **Rougel:** 46.5847
- **Rougelsum:** 51.2214
- **Generation Length:** 77.04


## Training procedure

The model was trained on 1201 training samples and 100 validation samples of the modified [MTS-Dialog](https://huggingface.co/datasets/har1/MTS_Dialogue-Clinical_Note)

### Training hyperparameters

The following hyperparameters were used during training:
- ```learning_rate```: 2e-05
- ```train_batch_size```: 1
- ```eval_batch_size```: 1
- ```seed```: 42
- ```gradient_accumulation_steps```: 2
- ```total_train_batch_size```: 2
- ```optimizer```: Adam with betas=(0.9,0.999) and epsilon=1e-08
- ```lr_scheduler_type```: linear
- ```num_epochs```: 3
- ```mixed_precision_training```: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 0.4426        | 1.0   | 600  | 0.1588          | 52.8864 | 33.253  | 44.9089 | 50.5072   | 69.38   |
| 0.1137        | 2.0   | 1201 | 0.1517          | 56.8499 | 35.309  | 48.2171 | 53.6983   | 72.74   |
| 0.0796        | 3.0   | 1800 | 0.1562          | 54.3238 | 34.2678 | 46.5847 | 51.2214   | 77.04   |


### Framework versions

- Transformers 4.39.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2


