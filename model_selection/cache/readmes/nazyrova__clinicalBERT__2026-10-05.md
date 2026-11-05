---
license: afl-3.0
language:
- en
tags:
- hospital
- clinical
- biobert
- clinicalBERT
- bioBERT
- clinical notes
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

This model card describes the Sci + Clinical BERT model, which was initialized from SciBERT & trained on all MIMIC-IV discharge notes.
This model can be used for medical text analysis.

## Model Details

The Sci + Clinical BERT model was trained on all notes from MIMIC IV, containing deidentified electronic health records of patients admitted to Beth Israel Deaconess Medical Center, Boston, MA, USA. 

### Model Pretraining
#### Note Preprocessing
Each note in MIMIC was first split into sections using a rules-based section splitter (e.g. discharge summary notes were split into "History of Present Illness", "Family History", "Brief Hospital Course", etc. sections). Then each section was split into sentences using SciSpacy (en core sci md tokenizer).

#### Pretraining Procedures
The model was trained using NVIDIA GeForce RTX3070 Ti Laptop GPU. Model parameters were initialized with SciBERT (scibert_scivocab_uncased).

#### Pretraining Hyperparameters
We used a batch size of 32, a maximum sequence length of 128, and a learning rate of 5 · 10−5 for pre-training our models. The models trained on all MIMIC-IV notes were trained for 150,000 steps. The dup factor for duplicating input data with different masks was set to 5. All other default parameters were used (specifically, masked language model probability = 0.15 and max predictions per sequence = 20).


### Model Description

<!-- Provide a longer summary of what this model is. -->



- **Developed by: Nodira Nazyrova


## Uses

Load the model via the transformers library:
```
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("nazyrova/clinicalBERT")
model = AutoModel.from_pretrained("nazyrova/clinicalBERT")

