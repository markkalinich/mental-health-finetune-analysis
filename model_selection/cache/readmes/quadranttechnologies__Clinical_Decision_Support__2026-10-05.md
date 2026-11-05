---
license: mit
base_model:
- microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
---
## Clinical Decision Support Model 🩺📊
Model Overview
This Clinical Decision Support Model is designed to assist healthcare providers in making data-driven decisions based on patient information. The model leverages advanced natural language processing (NLP) capabilities using the BiomedBERT architecture, fine-tuned specifically on a synthetic dataset of heart disease-related patient data. It provides personalized recommendations for patients based on their clinical profile.

## Model Use Case
The primary use case for this model is Clinical Decision Support in the domain of Cardiovascular Health. It helps healthcare professionals by:

Evaluating patient health data.
Predicting clinical recommendations.
Reducing decision-making time and improving the quality of care.

## Inputs
The model expects input in the following format:

Age: <int>, Gender: <Male/Female>, Weight: <int>, Smoking Status: <Never/Former/Current>, Diabetes: <0/1>, Hypertension: <0/1>, Cholesterol: <int>, Heart Disease History: <0/1>, Symptoms: <string>, Risk Score: <float>

## Output
The model predicts a recommendation from one of the following categories:

Maintain healthy lifestyle
Immediate cardiologist consultation
Start statins, monitor regularly
Lifestyle changes, monitor
No immediate action
Increase statins, lifestyle changes
Start ACE inhibitors, monitor

## Example Input
Age: 70, Gender: Female, Weight: 66, Smoking Status: Never, Diabetes: 0, Hypertension: 1, Cholesterol: 258, Heart Disease History: 1, Symptoms: Chest pain, Risk Score: 6.1

## Example Output
Recommendation: Start ACE inhibitors, monitor

## Model Training

Base Model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
Dataset: A synthetic dataset of 5000 patient examples with details like age, gender, symptoms, risk score, etc.
Fine-tuning Framework: Hugging Face Transformers.

## How to Use

from transformers import pipeline

#Load the model
model_path = "your_username/clinical_decision_support"
classifier = pipeline("text-classification", model=model_path)

#Example input
input_text = "Age: 70, Gender: Female, Weight: 66, Smoking Status: Never, Diabetes: 0, Hypertension: 1, Cholesterol: 258, Heart Disease History: 1, Symptoms: Chest pain, Risk Score: 6.1"

#Get prediction
prediction = classifier(input_text)
print(prediction)

## Limitations

The model is based on synthetic data and may not fully generalize to real-world scenarios.
Recommendations are not a substitute for clinical expertise and should always be validated by a healthcare professional.

## Future Improvements

Train on a larger, real-world dataset to enhance model performance.
Expand the scope to include recommendations for other medical domains.

## Acknowledgments

Model fine-tuned using the Hugging Face Transformers library.
Base model provided by Microsoft: BiomedBERT.