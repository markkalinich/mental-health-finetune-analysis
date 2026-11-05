---
language: en

widget:
- text: "The patient is pregnant."
  example_title: "Discusses Pregnancy"
- text: "She has high cholesterol and hypertension."
  example_title: "No Discussion of Pregnancy"
---

# Model Card for identifying_pregnancy_clinical_notes

This model is a fine-tuned version of [Bio+ClincialBert](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT). It was fine-tuned on an open source Kaggle dataset of [medical transcriptions](https://www.kaggle.com/datasets/tboyle10/medicaltranscriptions/) with an aim of classifying clincial notes as discussing or not discussing a patient's pregnancy.

- **Repository:** [Available on GitHub](https://github.com/elliealbertson/identifying_pregnancy_clinical_notes).
- **Uses:** Intended use is binary classification of English-language clinical notes as discussing or not discussing a patient's pregnancy.
- **Limitations:** The model was fine-tuned on a small number of clinical notes agumented by limited synthetic data. As a result, it may give inaccurate results at times. It is recommended to consider probability of class assignment when evaluating clinical note classifications.

## How to Get Started with the Model

Load the model via the transformers library:
```
model_path = "elliealbertson/identifying_pregnancy_clinical_notes"
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path, num_labels=2)
```