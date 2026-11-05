---
license: mit
pipeline_tag: token-classification
widget:
- text: "Alzheimer's disease (AD) is characterized pathologically by amyloid-beta (Aβ) deposition in brain parenchyma and blood vessels (as cerebral amyloid angiopathy (CAA)) and by neurofibrillary tangles of hyperphosphorylated tau. Compelling genetic and biomarker evidence supports Aβ as the root cause of AD. We previously reported human transmission of Aβ pathology and CAA in relatively young adults who had died of iatrogenic Creutzfeldt-Jakob disease (iCJD) after childhood treatment with cadaver-derived pituitary growth hormone (c-hGH) contaminated with both CJD prions and Aβ seeds. This raised the possibility that c-hGH recipients who did not die from iCJD may eventually develop AD. Here we describe recipients who developed dementia and biomarker changes within the phenotypic spectrum of AD, suggesting that AD, like CJD, has environmentally acquired (iatrogenic) forms as well as late-onset sporadic and early-onset inherited forms. Although iatrogenic AD may be rare, and there is no suggestion that Aβ can be transmitted between individuals in activities of daily life, its recognition emphasizes the need to review measures to prevent accidental transmissions via other medical and surgical procedures. As propagating Aβ assemblies may exhibit structural diversity akin to conventional prions, it is possible that therapeutic strategies targeting disease-related assemblies may lead to selection of minor components and development of resistance."
- text: "Background: Nonalcoholic steatohepatitis (NASH) is a progressive liver disease with no approved treatment. Resmetirom is an oral, liver-directed, thyroid hormone receptor beta-selective agonist in development for the treatment of NASH with liver fibrosis. Methods: We are conducting an ongoing phase 3 trial involving adults with biopsy-confirmed NASH and a fibrosis stage of F1B, F2, or F3 (stages range from F0 [no fibrosis] to F4 [cirrhosis]). Patients were randomly assigned in a 1:1:1 ratio to receive once-daily resmetirom at a dose of 80 mg or 100 mg or placebo. The two primary end points at week 52 were NASH resolution (including a reduction in the nonalcoholic fatty liver disease [NAFLD] activity score by ≥2 points; scores range from 0 to 8, with higher scores indicating more severe disease) with no worsening of fibrosis, and an improvement (reduction) in fibrosis by at least one stage with no worsening of the NAFLD activity score. Results: Overall, 966 patients formed the primary analysis population (322 in the 80-mg resmetirom group, 323 in the 100-mg resmetirom group, and 321 in the placebo group). NASH resolution with no worsening of fibrosis was achieved in 25.9% of the patients in the 80-mg resmetirom group and 29.9% of those in the 100-mg resmetirom group, as compared with 9.7% of those in the placebo group (P<0.001 for both comparisons with placebo). Fibrosis improvement by at least one stage with no worsening of the NAFLD activity score was achieved in 24.2% of the patients in the 80-mg resmetirom group and 25.9% of those in the 100-mg resmetirom group, as compared with 14.2% of those in the placebo group (P<0.001 for both comparisons with placebo)."
---

# Model Card for Model longluu/Clinical-NER-MedMentions-GatorTronBase
The model is an NER LLM algorithm that can classify each word in a text into different clinical categories. 

## Model Details

### Model Description
The base pretrained model is GatorTron-base which was trained on billions of words in various clinical texts (https://huggingface.co/UFNLP/gatortron-base). 
Then using the MedMentions dataset (https://arxiv.org/pdf/1902.09476v1.pdf), I fine-tuned the model for NER task in which the model can classify each word in a text into different clinical categories.
The category system is a simplified version of UMLS concept system and consists of 21 categories: 
"['Living Beings', 'Virus']", "['Living Beings', 'Bacterium']", "['Anatomy', 'Anatomical Structure']", "['Anatomy', 'Body System']", "['Anatomy', 'Body Substance']", "['Disorders', 'Finding']", "['Disorders', 'Injury or Poisoning']", "['Phenomena', 'Biologic Function']", "['Procedures', 'Health Care Activity']", "['Procedures', 'Research Activity']", "['Devices', 'Medical Device']", "['Concepts & Ideas', 'Spatial Concept']", "['Occupations', 'Biomedical Occupation or Discipline']", "['Organizations', 'Organization']", "['Living Beings', 'Professional or Occupational Group']", "['Living Beings', 'Population Group']", "['Chemicals & Drugs', 'Chemical']", "['Objects', 'Food']", "['Concepts & Ideas', 'Intellectual Product']", "['Physiology', 'Clinical Attribute']", "['Living Beings', 'Eukaryote']", 'None'

### Model Sources [optional]
The github code associated with the model can be found here: https://github.com/longluu/LLM-NER-clinical-text.

## Training Details

### Training Data

The MedMentions dataset contain 4,392 abstracts released in PubMed®1 between January 2016 and January 2017. The abstracts were manually annotated for biomedical concepts. Details are provided in https://arxiv.org/pdf/1902.09476v1.pdf and data is in https://github.com/chanzuckerberg/MedMentions. 

#### Training Hyperparameters

The hyperparameters are --batch_size 4
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
{'f1': 0.6271402249699903,
 'precision': 0.6691625224055963,
 'recall': 0.6085333637974402,
 'matthews_correlation': 0.720898121696139}

## Model Card Contact
Feel free to reach out to me at thelong20.4@gmail.com if you have any question or suggestion.