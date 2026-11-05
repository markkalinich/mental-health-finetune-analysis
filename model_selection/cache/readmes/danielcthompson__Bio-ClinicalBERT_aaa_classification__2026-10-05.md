---
tags:
  - generated_from_keras_callback
model-index:
  - name: Bio-ClinicalBERT_aaa_classification
    results:
      - task:
          type: text-classification
          name: AAA vs Non-AAA Classification
        dataset:
          name: Clinical EHR Dataset
          type: medical
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.99
          - name: Precision (AAA)
            type: precision
            value: 0.99
          - name: Recall (AAA)
            type: recall
            value: 0.98
          - name: F1-Score (AAA)
            type: f1
            value: 0.98
          - name: Precision (Non-AAA)
            type: precision
            value: 0.99
          - name: Recall (Non-AAA)
            type: recall
            value: 0.99
          - name: F1-Score (Non-AAA)
            type: f1
            value: 0.99
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# Bio-ClinicalBERT AAA Classification

This model is a fine-tuned version of BioClinicalBERT to perform clinical text classification to identify patients who have undergone a AAA repair during an admission from unstructured Electronic Health Records (EHRs).

## Model Details

- **Model type**: BERTForSequenceClassification
- **Architecture**: BERT
- **Base model**: BioClinicalBERT
- **Fine-tuning objective**: Text classification (identifying AAA repair admissions using unstructured EHRs)
- **Frameworks**: TensorFlow and PyTorch

## Intended Use

This model is designed to be used for the classification of EHRs to identify patients who have undergone AAA repairs during their admission.

## How to use

Here is an example of how to load and use this model in Pytorch:

```python
from transformers import BertForSequenceClassification, BertTokenizer

# Load model and tokenizer
model = BertForSequenceClassification.from_pretrained("dannyt101/Bio-ClinicalBERT_aaa_classification", local_files_only=True)
tokenizer = BertTokenizer.from_pretrained("dannyt101/Bio-ClinicalBERT_aaa_classification", local_files_only=True)

# Tokenize clinical text (pseudoanonymised example)
inputs = tokenizer("\nName: Gemma Gardner                    Unit No: 774 412 320\n \nAdmission Date: 2024-02-07              Discharge Date: 2024-02-19\n \nDate of Birth: 1957-09-09             Sex:   F\n \nService: SURGERY\n \nAllergies: \nNo Known Allergies / Adverse Drug Reactions\n \nAttending: Dr. Matthew Anderson.\n \nChief Complaint:\nAAA and claudication\n \nMajor Surgical or Invasive Procedure:\nEVAR\n\n \nHistory of Present Illness:\n___ with 3.4-cm abdominal aortic aneurysm and severe iliac \nstenosis bilaterally causing significant thigh and buttock \nclaudication, presenting for EVAR. CTA of ___ showed a \npartially thrombosed fusiform infrarenal abdominal aortic \naneurysm and partially calcified plaque at the origins of both \ncommon iliac arteries (severe narrowing on the left and moderate \nto severe narrowing on the right). The plan was to treat the \naneurysm as well as occlusive disease and also to prepare for a \nfenestrated stent graft which would be done on a later date.\n \nPast Medical History:\nAAA, claudication\n \nSocial History:\n___\nFamily History:\nnoncontributory \n \nPhysical Exam:\nDischarge physical exam:\nVitals: 98.0   68   104/49   13   95RA\nGeneral: lying in bed, no acute distress\nHEENT: EMOI, nonicteric, mucus membranes moist\nCardiac: RRR\nPulmonary: no respiratory distress\nAbdomen: obese, soft, nontender, +BS\nExtremities: warm, well pefused, no edema\nPulse: R: p/p/d/p   L: p/p/d/p\n \nPertinent Results:\n___ 05:29AM BLOOD Hct-34.5*\n___ 05:29AM BLOOD Creat-0.5 Na-141 K-3.6 Cl-109*\n \nBrief Hospital Course:\nPatient underwent an EVAR for an abdominal aortic aneurysm as \nwell as for claudication symptoms. Please see operative report \nfor details of the operation. Her post-operative course was \nuncomplicated. She was discharged on post-op day 1, in stable \ncondition, tolerating oral diet, having flatus, and with no \nissues ambulating. She noted that her claudication symptoms in \nher thigh and buttocks seems to have improved. She will have a 1 \nmonth follow-up with CTA in the vascular outpatient clinic. \n \nMedications on Admission:\nsimvastatin 20qPM, aspirin 81mg ___, vit B12 500mg ___ 3, \n \nDischarge Medications:\n1. Aspirin EC 81 mg PO DAILY \n2. OxycoDONE (Immediate Release)  ___ mg PO Q4H:PRN pain \nRX *oxycodone 5 mg 1 tablet(s) by mouth every 4 hours Disp #*20 \nTablet Refills:*0\n3. Simvastatin 20 mg PO DAILY \n4. TraZODone 25 mg PO HS:PRN insomnia \n\n \nDischarge Disposition:\nHome\n \nDischarge Diagnosis:\nAAA and claudication\n\n \nDischarge Condition:\nMental Status: Clear and coherent.\nLevel of Consciousness: Alert and interactive.\nActivity Status: Ambulatory - Independent.\n\n \nDischarge Instructions:\nMEDICATIONS:\n\u2022Take Aspirin 81mg (enteric coated) once daily \n\u2022Do not stop Aspirin unless your Vascular Surgeon instructs you \nto do so. \n\u2022Continue all other medications you were taking before surgery, \nunless otherwise directed\n\u2022You make take Tylenol or prescribed pain medications for any \npost procedure pain or discomfort\n\nWHAT TO EXPECT AT HOME:\nIt is normal to have slight swelling of the legs:\n\u2022Elevate your leg above the level of your heart (use ___ \npillows or a recliner) every ___ hours throughout the day and at \nnight\n\u2022Avoid prolonged periods of standing or sitting without your \nlegs elevated\nIt is normal to feel tired and have a decreased appetite, your \nappetite will return with time \n\u2022Drink plenty of fluids and eat small frequent meals\n\u2022It is important to eat nutritious food options (high fiber, \nlean meats, vegetables/fruits, low fat, low cholesterol) to \nmaintain your strength and assist in wound healing\n\u2022To avoid constipation: eat a high fiber diet and use stool \nsoftener while taking pain medication\n\nACTIVITIES:\n\u2022When you go home, you may walk and go up and down stairs\n\u2022You may shower (let the soapy water run over groin incision, \nrinse and pat dry)\n\u2022Your incision may be left uncovered, unless you have small \namounts of drainage from the wound, then place a dry dressing or \nband aid over the area that is draining, as needed\n\u2022No heavy lifting, pushing or pulling (greater than 5 lbs) for \n1 week (to allow groin puncture to heal)\n\u2022After 1 week, you may resume sexual activity\n\u2022After 1 week, gradually increase your activities and distance \nwalked as you can tolerate\n\u2022No driving until you are no longer taking pain medications\n\nCALL THE OFFICE FOR: ___\n\u2022Numbness, coldness or pain in lower extremities \n\u2022Temperature greater than 101.5F for 24 hours\n\u2022New or increased drainage from incision or white, yellow or \ngreen drainage from incisions\n\u2022Bleeding from groin puncture site\n\nFOR SUDDEN, SEVERE BLEEDING OR SWELLING (Groin puncture site or \nincision)\n\u2022Lie down, keep leg straight and have someone apply firm \npressure to area for 10 minutes. If bleeding stops, call \nvascular office. If bleeding does not stop, call ___ for \ntransfer to closest Emergency Room. \n\n \nFollowup Instructions:\n___\n")

# Get model predictions
outputs = model(**inputs)

# Get predicted class
predicted_class_idx = np.argmax(outputs.logits[0]).item()

# Define class labels
label = {0: "Non-AAA repair", 1: "AAA repair"}

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
inputs = tokenizer("\nName: Gemma Gardner                    Unit No: 774 412 320\n \nAdmission Date: 2024-02-07              Discharge Date: 2024-02-19\n \nDate of Birth: 1957-09-09             Sex:   F\n \nService: SURGERY\n \nAllergies: \nNo Known Allergies / Adverse Drug Reactions\n \nAttending: Dr. Matthew Anderson.\n \nChief Complaint:\nAAA and claudication\n \nMajor Surgical or Invasive Procedure:\nEVAR\n\n \nHistory of Present Illness:\n___ with 3.4-cm abdominal aortic aneurysm and severe iliac \nstenosis bilaterally causing significant thigh and buttock \nclaudication, presenting for EVAR. CTA of ___ showed a \npartially thrombosed fusiform infrarenal abdominal aortic \naneurysm and partially calcified plaque at the origins of both \ncommon iliac arteries (severe narrowing on the left and moderate \nto severe narrowing on the right). The plan was to treat the \naneurysm as well as occlusive disease and also to prepare for a \nfenestrated stent graft which would be done on a later date.\n \nPast Medical History:\nAAA, claudication\n \nSocial History:\n___\nFamily History:\nnoncontributory \n \nPhysical Exam:\nDischarge physical exam:\nVitals: 98.0   68   104/49   13   95RA\nGeneral: lying in bed, no acute distress\nHEENT: EMOI, nonicteric, mucus membranes moist\nCardiac: RRR\nPulmonary: no respiratory distress\nAbdomen: obese, soft, nontender, +BS\nExtremities: warm, well pefused, no edema\nPulse: R: p/p/d/p   L: p/p/d/p\n \nPertinent Results:\n___ 05:29AM BLOOD Hct-34.5*\n___ 05:29AM BLOOD Creat-0.5 Na-141 K-3.6 Cl-109*\n \nBrief Hospital Course:\nPatient underwent an EVAR for an abdominal aortic aneurysm as \nwell as for claudication symptoms. Please see operative report \nfor details of the operation. Her post-operative course was \nuncomplicated. She was discharged on post-op day 1, in stable \ncondition, tolerating oral diet, having flatus, and with no \nissues ambulating. She noted that her claudication symptoms in \nher thigh and buttocks seems to have improved. She will have a 1 \nmonth follow-up with CTA in the vascular outpatient clinic. \n \nMedications on Admission:\nsimvastatin 20qPM, aspirin 81mg ___, vit B12 500mg ___ 3, \n \nDischarge Medications:\n1. Aspirin EC 81 mg PO DAILY \n2. OxycoDONE (Immediate Release)  ___ mg PO Q4H:PRN pain \nRX *oxycodone 5 mg 1 tablet(s) by mouth every 4 hours Disp #*20 \nTablet Refills:*0\n3. Simvastatin 20 mg PO DAILY \n4. TraZODone 25 mg PO HS:PRN insomnia \n\n \nDischarge Disposition:\nHome\n \nDischarge Diagnosis:\nAAA and claudication\n\n \nDischarge Condition:\nMental Status: Clear and coherent.\nLevel of Consciousness: Alert and interactive.\nActivity Status: Ambulatory - Independent.\n\n \nDischarge Instructions:\nMEDICATIONS:\n\u2022Take Aspirin 81mg (enteric coated) once daily \n\u2022Do not stop Aspirin unless your Vascular Surgeon instructs you \nto do so. \n\u2022Continue all other medications you were taking before surgery, \nunless otherwise directed\n\u2022You make take Tylenol or prescribed pain medications for any \npost procedure pain or discomfort\n\nWHAT TO EXPECT AT HOME:\nIt is normal to have slight swelling of the legs:\n\u2022Elevate your leg above the level of your heart (use ___ \npillows or a recliner) every ___ hours throughout the day and at \nnight\n\u2022Avoid prolonged periods of standing or sitting without your \nlegs elevated\nIt is normal to feel tired and have a decreased appetite, your \nappetite will return with time \n\u2022Drink plenty of fluids and eat small frequent meals\n\u2022It is important to eat nutritious food options (high fiber, \nlean meats, vegetables/fruits, low fat, low cholesterol) to \nmaintain your strength and assist in wound healing\n\u2022To avoid constipation: eat a high fiber diet and use stool \nsoftener while taking pain medication\n\nACTIVITIES:\n\u2022When you go home, you may walk and go up and down stairs\n\u2022You may shower (let the soapy water run over groin incision, \nrinse and pat dry)\n\u2022Your incision may be left uncovered, unless you have small \namounts of drainage from the wound, then place a dry dressing or \nband aid over the area that is draining, as needed\n\u2022No heavy lifting, pushing or pulling (greater than 5 lbs) for \n1 week (to allow groin puncture to heal)\n\u2022After 1 week, you may resume sexual activity\n\u2022After 1 week, gradually increase your activities and distance \nwalked as you can tolerate\n\u2022No driving until you are no longer taking pain medications\n\nCALL THE OFFICE FOR: ___\n\u2022Numbness, coldness or pain in lower extremities \n\u2022Temperature greater than 101.5F for 24 hours\n\u2022New or increased drainage from incision or white, yellow or \ngreen drainage from incisions\n\u2022Bleeding from groin puncture site\n\nFOR SUDDEN, SEVERE BLEEDING OR SWELLING (Groin puncture site or \nincision)\n\u2022Lie down, keep leg straight and have someone apply firm \npressure to area for 10 minutes. If bleeding stops, call \nvascular office. If bleeding does not stop, call ___ for \ntransfer to closest Emergency Room. \n\n \nFollowup Instructions:\n___\n")

# Get model predictions
outputs = model(**inputs)

# Get predicted class
predicted_class_idx = np.argmax(outputs.logits[0]).item()

# Define class labels
label = {0: "Non-AAA repair", 1: "AAA repair"}

# Get predicted class label
predicted_class_label = label[predicted_class_idx]
print(predicted_class_label)
```


## Handling Long Clinical Text

If the length of the clinical text exceeds 512 tokens (like the examples above), you can use a sliding window approach to process the text. An example of how to implement this approach is in a notebook on GitHub.

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

| Model             | Accuracy | Precision (AAA) | Recall (AAA) | F1-Score (AAA) | Precision (Non-AAA) | Recall (Non-AAA) | F1-Score (Non-AAA) |
|-------------------|----------|-----------------|--------------|----------------|---------------------|------------------|--------------------|
| **Bio-clinicalBERT**  | 0.99     | 0.99            | 0.98         | 0.98           | 0.99                | 0.99             | 0.99               |


### Framework versions

- Transformers 4.41.1
- TensorFlow 2.17.0
- Tokenizers 0.19.1
