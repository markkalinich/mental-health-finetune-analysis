---
model-index:
- name: Bio-ClinicalBERT_vascular_classification
  results:
  - task:
      type: text-classification
      name: Vascular vs. Non-Vascular Classification
    dataset:
      name: Clinical EHR Dataset
      type: medical
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.94
    - name: Precision (Vascular)
      type: precision
      value: 0.88
    - name: Recall (Vascular)
      type: recall
      value: 0.70
    - name: F1-Score (Vascular)
      type: f1
      value: 0.78
    - name: Precision (Non-Vascular)
      type: precision
      value: 0.95
    - name: Recall (Non-Vascular)
      type: recall
      value: 0.98
    - name: F1-Score (Non-Vascular)
      type: f1
      value: 0.96
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Bio-ClinicalBERT Vascular Classification

This model is a fine-tuned version of BioClinicalBERT to perform clinical text classification to identify acute vascular admissions from Electronic Health Records (EHRs).

## Model Details

- **Model type**: BERTForSequenceClassification
- **Architecture**: BERT
- **Base model**: BioClinicalBERT
- **Fine-tuning objective**: Text classification (identifying acute vascular admissions using EHRs)
- **Frameworks**: TensorFlow and PyTorch

## Intended Use

This model is designed to be used for the classification of EHRs to identify acute vascular surgery admissions.

## How to use

Here is an example of how to load and use this model in Pytorch:

```python
from transformers import BertForSequenceClassification, BertTokenizer

# Load model and tokenizer
model = BertForSequenceClassification.from_pretrained("dannyt101/Bio-ClinicalBERT_vascular_classification", local_files_only=True)
tokenizer = BertTokenizer.from_pretrained("dannyt101/Bio-ClinicalBERT_vascular_classification", local_files_only=True)

# Tokenize clinical text (pseudoanonymised example)
inputs = tokenizer("Name: Ellie Sutton                    Unit No: 677 917 812\\n \\nAdmission Date: 2020-10-12              Discharge Date: 2020-10-22\\n \\nDate of Birth: 1952-11-18             Sex:   F\\n \\nService: SURGERY\\n \\nAllergies: \\nZocor / Tricor / Ambien / Lipitor\\n \\nAttending: Dr. Michael Davis.\\n \\nChief Complaint:\\nRLE ischemia\\n \\nMajor Surgical or Invasive Procedure:\\nRLE angio and R SFA stent placement\\n\\n \\nHistory of Present Illness:\\n___ year old female with a history of bilateral SFA stents placed \\nin ___. Her asymptomatic peripheral vascular disease was \\nmanaged conservatively, until she became symptomatic and began \\nhaving symptoms of claudication. \\n \\nPast Medical History:\\n-CAD s/p stenting approx ___ (per pt report)\\n-Type I Diabetes\\n-Hypertension\\n-Obesity\\n-Asthma\\n-Hypercholesterolemia\\n-CRI\\n-Hypothyroidism\\n-C-section, remote\\n-Lap cholecystectomy, ___ years ago\\n-Bilateral cataracts surgery, ___ years\\n-Left stapedectomy, ___ year\\n-Cardiac stent (3), ___ year\\n-Gouty arthritis\\n-Vitamin B-12 deficient\\n \\nSocial History:\\n___\\nFamily History:\\nBrother died in ___ of MI.  Second brother died in ___ of kidney \\ndisease.\\n \\nPhysical Exam:\\nGen: Awake and alert\\nResp: CTAB\\nCV: Regular rate and rhythm\\nAbd: Soft, nontender, nondistended\\nExtremities: Bilateral DP and ___ pulses dopplerable.\\nGroin site hemostatic\\n \\nPertinent Results:\\nNone\\n \\nBrief Hospital Course:\\nMs. ___ was admitted to the hospital on ___ and underwent \\nangiogram and right superficial femoral artery stent placement. \\nShe underwent the procedure with no complications. \\nPost-operatively, her groin was hemostatic and her pulses were \\ndopplerable. On the morning of POD #1, she underwent a dialysis \\ntreatment per her usual schedule, and was discharged later that \\nday in stable condition. \\n \\nMedications on Admission:\\nThe Preadmission Medication list is accurate and complete.\\n1. Allopurinol ___ mg PO DAILY \\n2. Calcium Acetate 667 mg PO TID W/MEALS \\n3. Clopidogrel 75 mg PO DAILY \\n4. Cyanocobalamin 1000 mcg IM/SC Frequency is Unknown \\n5. Epoetin Alfa Dose is Unknown  IV WITH DIALYSIS \\n6. Ezetimibe 10 mg PO DAILY \\n7. Gabapentin 300 mg PO TID \\n8. Glargine 54 Units Bedtime\\nHumalog Unknown Dose\\nInsulin SC Sliding Scale using HUM Insulin\\n9. Isosorbide Mononitrate (Extended Release) 90 mg PO DAILY \\n10. Levothyroxine Sodium 125 mcg PO DAILY \\n11. Metoclopramide 5 mg PO QIDACHS \\n12. Nitroglycerin SL 0.4 mg SL Q5MIN:PRN chest pain \\n13. Pantoprazole 40 mg PO Q24H \\n14. Rosuvastatin Calcium 10 mg PO QPM \\n15. sevelamer CARBONATE 2400 mg PO TID W/MEALS \\n16. Valsartan 80 mg PO DAILY \\n17. Aspirin 81 mg PO DAILY \\n18. Vitamin D 400 UNIT PO DAILY \\n19. Docusate Sodium 100 mg PO BID \\n\\n \\nDischarge Medications:\\n1. Allopurinol ___ mg PO DAILY \\n2. Aspirin 81 mg PO DAILY \\n3. Calcium Acetate 667 mg PO TID W/MEALS \\n4. Clopidogrel 75 mg PO DAILY \\n5. Docusate Sodium 100 mg PO BID \\n6. Gabapentin 300 mg PO TID \\n7. Glargine 54 Units Bedtime\\nInsulin SC Sliding Scale using HUM Insulin\\n8. Isosorbide Mononitrate (Extended Release) 90 mg PO DAILY \\n9. Levothyroxine Sodium 125 mcg PO DAILY \\n10. Metoclopramide 5 mg PO QIDACHS \\n11. Pantoprazole 40 mg PO Q24H \\n12. Rosuvastatin Calcium 10 mg PO QPM \\n13. sevelamer CARBONATE 2400 mg PO TID W/MEALS \\n14. Valsartan 80 mg PO DAILY \\n15. Metoprolol Tartrate 50 mg PO DAILY \\n16. Ezetimibe 10 mg PO DAILY \\n17. Nitroglycerin SL 0.4 mg SL Q5MIN:PRN chest pain \\n18. Vitamin D 400 UNIT PO DAILY \\n19. Acetaminophen 650 mg PO Q6H:PRN pain \\n\\n \\nDischarge Disposition:\\nHome\\n \\nDischarge Diagnosis:\\nR SFA stenosis\\n\\n \\nDischarge Condition:\\nMental Status: Clear and coherent.\\nLevel of Consciousness: Alert and interactive.\\nActivity Status: Ambulatory - Independent.\\n\\n \\nDischarge Instructions:\\nDear Ms. ___,\\nYou were admitted to ___ and \\nunderwent angiogram and right superior femoral artery stent \\nplacement. You have now recovered from surgery and are ready to \\nbe discharged. Please follow the instructions below to continue \\nyour recovery:\\n\\nMEDICATION:\\n\\u2022 Take Aspirin 325mg (enteric coated) once daily \\n\\u2022 If instructed, take Plavix (Clopidogrel) 75mg once daily\\n\\u2022 Continue all other medications you were taking before surgery, \\nunless otherwise directed\\n\\u2022 You make take Tylenol or prescribed pain medications for any \\npost procedure pain or discomfort\\nWHAT TO EXPECT:\\nIt is normal to have slight swelling of the legs:\\n\\u2022 Elevate your leg above the level of your heart with pillows \\nevery ___ hours throughout the day and night\\n\\u2022 Avoid prolonged periods of standing or sitting without your \\nlegs elevated\\n\\u2022 It is normal to feel tired and have a decreased appetite, your \\nappetite will return with time \\n\\u2022 Drink plenty of fluids and eat small frequent meals\\n\\u2022 It is important to eat nutritious food options (high fiber, \\nlean meats, vegetables/fruits, low fat, low cholesterol) to \\nmaintain your strength and assist in wound healing\\n\\u2022 To avoid constipation: eat a high fiber diet and use stool \\nsoftener while taking pain medication\\n\\nACTIVITIES:\\n\\u2022 When you go home, you may walk and use stairs\\n\\u2022 You may shower (let the soapy water run over groin incision, \\nrinse and pat dry)\\n\\u2022 Your incision may be left uncovered, unless you have small \\namounts of drainage from the wound, then place a dry dressing or \\nband aid over the area \\n\\u2022 No heavy lifting, pushing or pulling (greater than 5 lbs) for \\n1 week (to allow groin puncture to heal)\\n\\u2022 After 1 week, you may resume sexual activity\\n\\u2022 After 1 week, gradually increase your activities and distance \\nwalked as you can tolerate\\n\\u2022 No driving until you are no longer taking pain medications\\n\\nCALL THE OFFICE FOR: ___\\n\\u2022 Numbness, coldness or pain in lower extremities \\n\\u2022 Temperature greater than 101.5F for 24 hours\\n\\u2022 New or increased drainage from incision or white, yellow or \\ngreen drainage from incisions\\n\\u2022 Bleeding from groin puncture site\\n\\nSUDDEN, SEVERE BLEEDING OR SWELLING (Groin puncture site)\\n\\u2022 Lie down, keep leg straight and have someone apply firm \\npressure to area for 10 minutes. If bleeding stops, call \\nvascular office ___. If bleeding does not stop, call \\n___ for transfer to closest Emergency Room. \\n\\n \\nFollowup Instructions:\"\"\"\n", return_tensors="pt")

# Get model predictions
outputs = model(**inputs)

# Get predicted class
predicted_class_idx = np.argmax(outputs.logits[0]).item()

# Define class labels
label = {0: "non-vascular", 1: "vascular"}

# Get predicted class label
predicted_class_label = label[predicted_class_idx]
print(predicted_class_label)
```

For Tensorflow:
```python

from transformers import TFBertForSequenceClassification, BertTokenizer

# Load model and tokenizer
model = TFBertForSequenceClassification.from_pretrained("dannyt101/Bio-ClinicalBERT_vascular_classification", local_files_only=True)
tokenizer = BertTokenizer.from_pretrained("dannyt101/Bio-ClinicalBERT_vascular_classification", local_files_only=True)

# Tokenize clinical text (pseudoanonymised example)
inputs = tokenizer("Name: Ellie Sutton                    Unit No: 677 917 812\\n \\nAdmission Date: 2020-10-12              Discharge Date: 2020-10-22\\n \\nDate of Birth: 1952-11-18             Sex:   F\\n \\nService: SURGERY\\n \\nAllergies: \\nZocor / Tricor / Ambien / Lipitor\\n \\nAttending: Dr. Michael Davis.\\n \\nChief Complaint:\\nRLE ischemia\\n \\nMajor Surgical or Invasive Procedure:\\nRLE angio and R SFA stent placement\\n\\n \\nHistory of Present Illness:\\n___ year old female with a history of bilateral SFA stents placed \\nin ___. Her asymptomatic peripheral vascular disease was \\nmanaged conservatively, until she became symptomatic and began \\nhaving symptoms of claudication. \\n \\nPast Medical History:\\n-CAD s/p stenting approx ___ (per pt report)\\n-Type I Diabetes\\n-Hypertension\\n-Obesity\\n-Asthma\\n-Hypercholesterolemia\\n-CRI\\n-Hypothyroidism\\n-C-section, remote\\n-Lap cholecystectomy, ___ years ago\\n-Bilateral cataracts surgery, ___ years\\n-Left stapedectomy, ___ year\\n-Cardiac stent (3), ___ year\\n-Gouty arthritis\\n-Vitamin B-12 deficient\\n \\nSocial History:\\n___\\nFamily History:\\nBrother died in ___ of MI.  Second brother died in ___ of kidney \\ndisease.\\n \\nPhysical Exam:\\nGen: Awake and alert\\nResp: CTAB\\nCV: Regular rate and rhythm\\nAbd: Soft, nontender, nondistended\\nExtremities: Bilateral DP and ___ pulses dopplerable.\\nGroin site hemostatic\\n \\nPertinent Results:\\nNone\\n \\nBrief Hospital Course:\\nMs. ___ was admitted to the hospital on ___ and underwent \\nangiogram and right superficial femoral artery stent placement. \\nShe underwent the procedure with no complications. \\nPost-operatively, her groin was hemostatic and her pulses were \\ndopplerable. On the morning of POD #1, she underwent a dialysis \\ntreatment per her usual schedule, and was discharged later that \\nday in stable condition. \\n \\nMedications on Admission:\\nThe Preadmission Medication list is accurate and complete.\\n1. Allopurinol ___ mg PO DAILY \\n2. Calcium Acetate 667 mg PO TID W/MEALS \\n3. Clopidogrel 75 mg PO DAILY \\n4. Cyanocobalamin 1000 mcg IM/SC Frequency is Unknown \\n5. Epoetin Alfa Dose is Unknown  IV WITH DIALYSIS \\n6. Ezetimibe 10 mg PO DAILY \\n7. Gabapentin 300 mg PO TID \\n8. Glargine 54 Units Bedtime\\nHumalog Unknown Dose\\nInsulin SC Sliding Scale using HUM Insulin\\n9. Isosorbide Mononitrate (Extended Release) 90 mg PO DAILY \\n10. Levothyroxine Sodium 125 mcg PO DAILY \\n11. Metoclopramide 5 mg PO QIDACHS \\n12. Nitroglycerin SL 0.4 mg SL Q5MIN:PRN chest pain \\n13. Pantoprazole 40 mg PO Q24H \\n14. Rosuvastatin Calcium 10 mg PO QPM \\n15. sevelamer CARBONATE 2400 mg PO TID W/MEALS \\n16. Valsartan 80 mg PO DAILY \\n17. Aspirin 81 mg PO DAILY \\n18. Vitamin D 400 UNIT PO DAILY \\n19. Docusate Sodium 100 mg PO BID \\n\\n \\nDischarge Medications:\\n1. Allopurinol ___ mg PO DAILY \\n2. Aspirin 81 mg PO DAILY \\n3. Calcium Acetate 667 mg PO TID W/MEALS \\n4. Clopidogrel 75 mg PO DAILY \\n5. Docusate Sodium 100 mg PO BID \\n6. Gabapentin 300 mg PO TID \\n7. Glargine 54 Units Bedtime\\nInsulin SC Sliding Scale using HUM Insulin\\n8. Isosorbide Mononitrate (Extended Release) 90 mg PO DAILY \\n9. Levothyroxine Sodium 125 mcg PO DAILY \\n10. Metoclopramide 5 mg PO QIDACHS \\n11. Pantoprazole 40 mg PO Q24H \\n12. Rosuvastatin Calcium 10 mg PO QPM \\n13. sevelamer CARBONATE 2400 mg PO TID W/MEALS \\n14. Valsartan 80 mg PO DAILY \\n15. Metoprolol Tartrate 50 mg PO DAILY \\n16. Ezetimibe 10 mg PO DAILY \\n17. Nitroglycerin SL 0.4 mg SL Q5MIN:PRN chest pain \\n18. Vitamin D 400 UNIT PO DAILY \\n19. Acetaminophen 650 mg PO Q6H:PRN pain \\n\\n \\nDischarge Disposition:\\nHome\\n \\nDischarge Diagnosis:\\nR SFA stenosis\\n\\n \\nDischarge Condition:\\nMental Status: Clear and coherent.\\nLevel of Consciousness: Alert and interactive.\\nActivity Status: Ambulatory - Independent.\\n\\n \\nDischarge Instructions:\\nDear Ms. ___,\\nYou were admitted to ___ and \\nunderwent angiogram and right superior femoral artery stent \\nplacement. You have now recovered from surgery and are ready to \\nbe discharged. Please follow the instructions below to continue \\nyour recovery:\\n\\nMEDICATION:\\n\\u2022 Take Aspirin 325mg (enteric coated) once daily \\n\\u2022 If instructed, take Plavix (Clopidogrel) 75mg once daily\\n\\u2022 Continue all other medications you were taking before surgery, \\nunless otherwise directed\\n\\u2022 You make take Tylenol or prescribed pain medications for any \\npost procedure pain or discomfort\\nWHAT TO EXPECT:\\nIt is normal to have slight swelling of the legs:\\n\\u2022 Elevate your leg above the level of your heart with pillows \\nevery ___ hours throughout the day and night\\n\\u2022 Avoid prolonged periods of standing or sitting without your \\nlegs elevated\\n\\u2022 It is normal to feel tired and have a decreased appetite, your \\nappetite will return with time \\n\\u2022 Drink plenty of fluids and eat small frequent meals\\n\\u2022 It is important to eat nutritious food options (high fiber, \\nlean meats, vegetables/fruits, low fat, low cholesterol) to \\nmaintain your strength and assist in wound healing\\n\\u2022 To avoid constipation: eat a high fiber diet and use stool \\nsoftener while taking pain medication\\n\\nACTIVITIES:\\n\\u2022 When you go home, you may walk and use stairs\\n\\u2022 You may shower (let the soapy water run over groin incision, \\nrinse and pat dry)\\n\\u2022 Your incision may be left uncovered, unless you have small \\namounts of drainage from the wound, then place a dry dressing or \\nband aid over the area \\n\\u2022 No heavy lifting, pushing or pulling (greater than 5 lbs) for \\n1 week (to allow groin puncture to heal)\\n\\u2022 After 1 week, you may resume sexual activity\\n\\u2022 After 1 week, gradually increase your activities and distance \\nwalked as you can tolerate\\n\\u2022 No driving until you are no longer taking pain medications\\n\\nCALL THE OFFICE FOR: ___\\n\\u2022 Numbness, coldness or pain in lower extremities \\n\\u2022 Temperature greater than 101.5F for 24 hours\\n\\u2022 New or increased drainage from incision or white, yellow or \\ngreen drainage from incisions\\n\\u2022 Bleeding from groin puncture site\\n\\nSUDDEN, SEVERE BLEEDING OR SWELLING (Groin puncture site)\\n\\u2022 Lie down, keep leg straight and have someone apply firm \\npressure to area for 10 minutes. If bleeding stops, call \\nvascular office ___. If bleeding does not stop, call \\n___ for transfer to closest Emergency Room. \\n\\n \\nFollowup Instructions:\"\"\"\n", return_tensors="tf")

# Get model predictions
outputs = model(**inputs)

# Get predicted class
predicted_class_idx = np.argmax(outputs.logits[0]).item()

# Define class labels
label = {0: "non-vascular", 1: "vascular"}

# Get predicted class label
predicted_class_label = label[predicted_class_idx]
print(predicted_class_label)
```

## Handling Long Clinical Text

If the length of the clinical text exceeds 512 tokens, you can use a sliding window approach to process the text. An example of how to implement this approach is in a notebook on GitHub.

You can view and run the full example on GitHub here:
[Sliding Window Example Notebook](https://github.com/dannyt101/AAA_classification/blob/main/Stage_1/bio-clinicalBERT_vasc_class_demo.ipynb)

## Training and evaluation data

EHRs were downloaded from [MIMIC-IV clinical notes dataset](https://physionet.org/content/mimic-iv-note/2.2/)
The EHRs were annotated by a Vascular Surgery Specialist Registrar/Resident and categorized as ‘Vascular’ if there was an acute pathology relevant to vascular surgery during their admission as per [National Health Service (NHS) England Service Specifications for Vascular Services](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.england.nhs.uk/wp-content/uploads/2017/06/specialised-vascular-services-service-specification-adults.pdf&ved=2ahUKEwiknoKus4uIAxUFwAIHHaaQCBcQFnoECBMQAQ&usg=AOvVaw3yRyS-Ei1fiTNi6dcP8yOL).

## Training procedure
The training was performed using TensorFlow's TPU strategy. Dataset was preprocessed using a sliding window approach to handle text longer than 512 tokens.

### Training hyperparameters

The following hyperparameters were used during training:
- **Optimizer**: Adam
- **Learning Rate**: 5e-5
- **Batch Size**: 16
- **Epochs**: Maximum of 5
- **Early Stopping**: Triggered if validation loss did not improve for 2 consecutive epochs

### Training Results

The Bio-clinicalBERT model achieved the following results on the validation set:

| Model              | Accuracy | Precision (Vascular) | Recall (Vascular) | F1-Score (Vascular) | Precision (Non-Vascular) | Recall (Non-Vascular) | F1-Score (Non-Vascular) |
|--------------------|----------|----------------------|-------------------|---------------------|--------------------------|-----------------------|-------------------------|
| **Bio-clinicalBERT** | 0.94     | 0.88                 | 0.70              | 0.78                | 0.95                     | 0.98                  | 0.96                    |


### Framework versions

- Transformers 4.41.1
- TensorFlow 2.17.0
- Tokenizers 0.19.1
