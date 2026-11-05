---
language: nl
license: mit

---

# MedRoBERTa.nl
Check out our website! [MedRoBERTa.nl](https://medroberta.nl)

## Description
This model is a RoBERTa-based model pre-trained from scratch on Dutch hospital notes sourced from Electronic Health Records. The model is not fine-tuned. All code used for the creation of MedRoBERTa.nl can be found at https://github.com/cltl-students/verkijk_stella_rma_thesis_dutch_medical_language_model.

## Intended use
The model can be fine-tuned on any type of task. Since it is a domain-specific model trained on medical data, it is meant to be used on medical NLP tasks for Dutch.  

## Data
The model was trained on nearly 10 million hospital notes from the Amsterdam University Medical Centres. The training data was anonymized before starting the pre-training procedure. 

## Privacy
By anonymizing the training data we made sure the model did not learn any representative associations linked to names. Apart from the training data, the model's vocabulary was also anonymized. This ensures that the model can not predict any names in the generative fill-mask task. 
For more information on the model's anonymization see our publication: 

Verkijk, S., & Vossen, P. (2022). Efficiently and thoroughly anonymizing a transformer language model for Dutch electronic health records: a two-step method. In Proceedings of the Thirteenth Language Resources and Evaluation Conference (pp. 1098-1103).

## Authors
Stella Verkijk, Piek Vossen

## Reference
Latest journal paper:

Verkijk, S., & Vossen, P. (2025). Creating, anonymizing and evaluating the first medical language model pre-trained on Dutch Electronic Health Records: MedRoBERTa.nl. Artificial Intelligence in Medicine, 167, 103148.

Original conference paper: 

Verkijk, S. & Vossen, P. (2022). MedRoBERTa.nl: A Language Model for Dutch Electronic Health Records. Computational Linguistics in the Netherlands Journal, 11.