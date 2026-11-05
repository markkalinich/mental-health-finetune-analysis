---
license: mit
base_model:
- almanach/camembert-bio-base
pipeline_tag: token-classification
library_name: transformers
tags:
- camembert
- french
- medical
- de-identification
datasets:
- HealthDataHub/PARHAF-pseudo-annotated
---
# French medical de-identification NER model

This model is a CamemBERT-based token classification checkpoint fine-tuned for named entity recognition on French medical text, with a focus on de-identification entities.
NER labels:
Nom, 
Prenom, 
Url, 
Ville, 
DateIdentifiante, 
SituationFamiliale, 
IdentiteSocialePatient, 
DateDesidentifiante, 
Pays, 
DateNaissancePatient, 
Adresse, 
NumeroTelephone, 
NationalitePatient

# Results of training per epoch

| Epoch | Training Loss | Validation Loss | Precision | Recall | F1 | Macro F1 | Accuracy |
|------:|--------------:|----------------:|----------:|-------:|---:|---------:|---------:|
| 1 | 3.259739 | 3.239809 | 0.008624 | 0.192094 | 0.016506 | 0.016309 | 0.234206 |
| 2 | 3.155496 | 3.177056 | 0.022145 | 0.451456 | 0.042219 | 0.043363 | 0.343179 |
| 3 | 3.062432 | 3.103942 | 0.026669 | 0.508322 | 0.050679 | 0.069548 | 0.403236 |
| 4 | 2.965864 | 3.031749 | 0.031932 | 0.550624 | 0.060364 | 0.107945 | 0.472002 |
| 5 | 2.878689 | 2.966769 | 0.038775 | 0.561720 | 0.072542 | 0.141406 | 0.559576 |
| 6 | 2.799171 | 2.908879 | 0.041481 | 0.555479 | 0.077197 | 0.138295 | 0.591547 |
| 7 | 2.737990 | 2.857519 | 0.048666 | 0.576976 | 0.089762 | 0.148555 | 0.644660 |
| 8 | 2.676395 | 2.815246 | 0.060018 | 0.594313 | 0.109026 | 0.164073 | 0.705796 |
| 9 | 2.638831 | 2.777210 | 0.059892 | 0.567268 | 0.108344 | 0.168802 | 0.714798 |
| 10 | 2.573915 | 2.748089 | 0.067711 | 0.587379 | 0.121425 | 0.175791 | 0.739021 |
| 11 | 2.542103 | 2.719197 | 0.073217 | 0.590153 | 0.130272 | 0.188839 | 0.756595 |
| 12 | 2.527237 | 2.700605 | 0.073934 | 0.596394 | 0.131559 | 0.189141 | 0.756458 |
| 13 | 2.507565 | 2.686029 | 0.076418 | 0.597781 | 0.135513 | 0.194222 | 0.764205 |
| 14 | 2.482355 | 2.677717 | 0.076399 | 0.591540 | 0.135322 | 0.188957 | 0.765304 |
| 15 | 2.477236 | 2.674951 | 0.076207 | 0.590153 | 0.134983 | 0.189207 | 0.764813 |