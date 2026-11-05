---
library_name: transformers
tags: []
---

# Model Card for Model ID

<!-- The Clinical Intent Model. -->



## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This model is designed for classifying medical intents from text using a specialized variant of ClinicalBERT. 
It was trained to understand and classify various medical intents based on patient dialogues and medical records. 
The model aims to enhance the understanding of medical phrases and intents in clinical settings.
### Pretraining Data
The Clinical Intent Model was trained on a diverse dataset consisting of:

Training Data: A large multicenter dataset including a variety of medical dialogues and intents.

### Model Pretraining
Pretraining Procedures
Base Model: The model is initialized from the ClinicalBERT base model.
Training Objective: The model is fine-tuned on the classification task of predicting medical intents. During fine-tuning, the model was exposed to a labeled dataset where phrases were categorized into predefined intents.
##### Pretraining Hyperparameters
* Batch Size: 32
* Maximum Sequence Length: 256
* Learning Rate: 2e-5
* Epochs: 20
* Optimizer: AdamW
* Scheduler: Linear scheduler with warm-up

