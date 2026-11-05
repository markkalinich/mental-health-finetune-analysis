---
license: mit
pipeline_tag: token-classification
widget:
- text: "Background: Coronaviruses have been the cause of 3 major outbreaks during the last 2 decades. Information on coronavirus diseases in pregnant women is limited, and even less is known about seriously ill pregnant women. Data are also lacking regarding the real burden of coronavirus disease 2019 (COVID-19) infection in pregnant women from low/middle-income countries. The aim of this study was to determine the characteristics and clinical course of COVID-19 in pregnant/puerperal women admitted to ICUs in Turkey. Methods: This was a national, multicenter, retrospective study. The study population comprised all SARS-CoV-2-infected pregnant/puerperal women admitted to participating ICUs between 1 March 2020 and 1 January 2022. Data regarding demographics, comorbidities, illness severity, therapies, extrapulmonary organ injuries, non-COVID-19 infections, and maternal and fetal/neonatal outcomes were recorded. LASSO logistic regression and multiple logistic regression analyses were used to identify predictive variables in terms of ICU mortality. Results: A total of 597 patients (341 pregnant women, 255 puerperal women) from 59 ICUs in 44 hospitals were included and of these patients, 87.1% were unvaccinated. The primary reason for ICU admission was acute hypoxemic respiratory failure in 522 (87.4%), acute hypoxemic respiratory failure plus shock in 14 (2.3%), ischemic cerebrovascular accident (CVA) in 5 (0.8%), preeclampsia/eclampsia/HELLP syndrome in 6 (1.0%), and post-caesarean follow-up in 36 (6.0%). Nonsurvivors were sicker than survivors upon ICU admission, with higher APACHE II (p < 0.001) and SOFA scores (p < 0.001). A total of 181 (30.3%) women died and 280 (46.6%) had received invasive mechanical ventilation (IMV)."
- text: "Importance: Atrial cardiopathy is associated with stroke in the absence of clinically apparent atrial fibrillation. It is unknown whether anticoagulation, which has proven benefit in atrial fibrillation, prevents stroke in patients with atrial cardiopathy and no atrial fibrillation. Objective: To compare anticoagulation vs antiplatelet therapy for secondary stroke prevention in patients with cryptogenic stroke and evidence of atrial cardiopathy. Design, setting, and participants: Multicenter, double-blind, phase 3 randomized clinical trial of 1015 participants with cryptogenic stroke and evidence of atrial cardiopathy, defined as P-wave terminal force greater than 5000 μV × ms in electrocardiogram lead V1, serum N-terminal pro-B-type natriuretic peptide level greater than 250 pg/mL, or left atrial diameter index of 3 cm/m2 or greater on echocardiogram. Participants had no evidence of atrial fibrillation at the time of randomization. Enrollment and follow-up occurred from February 1, 2018, through February 28, 2023, at 185 sites in the National Institutes of Health StrokeNet and the Canadian Stroke Consortium. Interventions: Apixaban, 5 mg or 2.5 mg, twice daily (n = 507) vs aspirin, 81 mg, once daily (n = 508). Main outcomes and measures: The primary efficacy outcome in a time-to-event analysis was recurrent stroke. All participants, including those diagnosed with atrial fibrillation after randomization, were analyzed according to the groups to which they were randomized. The primary safety outcomes were symptomatic intracranial hemorrhage and other major hemorrhage."
---

# Model Card for Model longluu/Clinical-NER-NCBI-Disease-GatorTronS
The model is an NER LLM algorithm that can classify each word in a text into different clinical categories. 

## Model Details

### Model Description
The base pretrained model is GatorTronS which was trained on billions of words in various clinical texts (https://huggingface.co/UFNLP/gatortronS). 
Then using the NCBI Disease dataset (https://www.sciencedirect.com/science/article/pii/S1532046413001974?via%3Dihub), 
I fine-tuned the model for NER task in which the model can classify each word in a text into one of the categories ['no disease', 'disease', 'disease-continue'].

### Model Sources [optional]
The github code associated with the model can be found here: https://github.com/longluu/LLM-NER-clinical-text.

## Training Details

### Training Data
This dataset contains the disease name and concept annotations of the NCBI disease corpus, a collection of 793 PubMed abstracts fully annotated at the mention and concept level to serve as a research resource for the biomedical natural language processing community. Details are here https://www.sciencedirect.com/science/article/pii/S1532046413001974?via%3Dihub.

The preprocessed data for LLM training can be found here https://huggingface.co/datasets/ncbi_disease.

#### Training Hyperparameters

The hyperparameters are --batch_size 24
                        --num_train_epochs 5
                        --learning_rate 5e-5 
                        --weight_decay 0.01 

## Evaluation
### Testing Data, Factors & Metrics
#### Testing Data
The model was trained and validated on train and validation sets. Then it was tested on a separate test set. 
Note that some concepts in the test set were not available in the train and validatin sets.

#### Metrics
Here we use several metrics for classification tasks including macro-average F1, precision, recall and Matthew correlation.

### Results
{'f1': 0.876008064516129,
 'precision': 0.9052083333333333,
 'recall': 0.8486328125}

## Model Card Contact
Feel free to reach out to me at thelong20.4@gmail.com if you have any question or suggestion.