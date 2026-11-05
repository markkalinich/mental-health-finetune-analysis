---
library_name: transformers
license: creativeml-openrail-m
base_model:
- dmis-lab/biobert-v1.1
pipeline_tag: question-answering
---

library_name: transformers  
tags: [biomedical, question-answering, healthcare]  

---

# Model Card for Online Doctor Model

This model is a fine-tuned version of the `dmis-lab/biobert-large-cased-v1.1-squad` model. It is designed to answer questions related to diseases based on symptom descriptions, providing a question-answering pipeline to help healthcare professionals and users. This model has been trained on a custom dataset of diseases and their symptoms for predictive question answering.

## Model Details

### Model Description

This is a question-answering model fine-tuned using the `BioBERT` architecture, specifically adapted for healthcare-related questions. The model is designed to extract answers from a disease-symptom dataset based on user-inputted symptoms or queries. 

- **Developed by:** Ayamba Victor Ndoma  
- **Model type:** Question Answering  
- **Language(s) (NLP):** English  
- **License:** Apache 2.0  
- **Finetuned from model:** `dmis-lab/biobert-large-cased-v1.1-squad`

### Model Sources

- **Repository:** [Hugging Face Repository](https://huggingface.co/your-username/online-doctor-model)
- **Demo:** [Link to Demo (optional)]

## Uses

This model can be used in the following cases:

### Direct Use

- Answering healthcare-related questions based on symptom input from users.
- Assisting medical professionals in preliminary diagnosis based on reported symptoms.

### Downstream Use

- Can be further fine-tuned or extended for more specific disease or symptom-related tasks.
- Integrated into chatbot systems for medical consultation services.

### Out-of-Scope Use

- The model is not intended for use in making definitive medical diagnoses without human supervision.
- It is not suitable for predicting non-health-related issues.

## Bias, Risks, and Limitations

- **Bias:** The model is trained on a custom dataset with potentially limited diversity in disease-symptom pairs.
- **Risks:** Incorrect predictions might occur when symptoms overlap across multiple diseases.
- **Limitations:** The model is constrained to the diseases and symptoms available in the training dataset and may not generalize to all medical conditions.

### Recommendations

This model should be used with caution, and its answers should be reviewed by qualified healthcare professionals.

## How to Get Started with the Model

Use the following code to get started with the model:

```python
from transformers import pipeline
qa_pipeline = pipeline("question-answering", model="your-username/online-doctor-model")

# Example question and context
question = "What are the symptoms of diabetes?"
context = "Diabetes: increased thirst, frequent urination, hunger, fatigue, blurred vision."

result = qa_pipeline(question=question, context=context)
print(result['answer'])
```

## Training Details

### Training Data

The model is fine-tuned on a custom dataset containing diseases and their respective symptoms.

### Training Procedure

- **Preprocessing:** Text cleaning and tokenization were applied to ensure proper context and symptom pairing.
- **Training regime:** The model was trained using mixed-precision FP16 on a single GPU.

#### Training Hyperparameters

- **Epochs:** 3  
- **Batch size:** 16  
- **Learning rate:** 3e-5

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The model was evaluated on a held-out portion of the custom disease-symptom dataset.

#### Factors

- Subpopulation: Various diseases ranging from common illnesses to rare conditions.
- Domains: Medical text and descriptions of symptoms.

#### Metrics

The model was evaluated using the SQuAD metrics, including F1 score and Exact Match (EM).

### Results

- **F1 score:** 0.82  
- **Exact Match (EM):** 0.78

#### Summary

The model performs well on the task of extracting relevant symptoms and disease-related answers based on the question provided. However, its performance is limited to the diseases and symptoms present in the training data.

## Environmental Impact

- **Hardware Type:** Single GPU (NVIDIA Tesla T4)  
- **Hours used:** 3  
- **Cloud Provider:** Google Cloud  
- **Compute Region:** US  
- **Carbon Emitted:** Approximately 0.36 kg CO2eq

## Technical Specifications

### Model Architecture and Objective

The model is based on the `BioBERT` architecture fine-tuned for the SQuAD task, with a focus on healthcare question-answering.

### Compute Infrastructure

- **Hardware:** NVIDIA Tesla T4 GPU  
- **Software:** PyTorch, Transformers Library

## Citation

If you use this model, please cite it as:

```
@misc{Ndoma2024onlinedoctor,
  author = {Ayamba Victor Ndoma},
  title = {Online Doctor Model for Disease Prediction},
  year = {2024},
  howpublished = {\url{https://huggingface.co/your-username/online-doctor-model}},
}
```

## Model Card Authors

- Ayamba Victor Ndoma

## Model Card Contact

For questions or feedback, please contact `victornd97@gmail.com`.

---