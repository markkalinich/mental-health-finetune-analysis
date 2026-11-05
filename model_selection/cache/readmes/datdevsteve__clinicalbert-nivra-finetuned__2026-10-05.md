---
license: apache-2.0
language:
- en
metrics:
- name: accuracy
  type: on test set
  value: 92.4

base_model:
- medicalai/ClinicalBERT
pipeline_tag: text-classification
library_name: transformers
task: text-generation
---
# Model Card 

The model is part of the **Nivra AI Healthcare Assistant** project, designed to help Indian patients understand and classify their symptoms accurately.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This is a fine-tuned version of [ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) specifically trained for symptom classification in the Indian healthcare context. The model is part of the **Nivra AI Healthcare Assistant** project, designed to help Indian patients understand and classify their symptoms accurately.

**Developed by:** [datdevsteve](https://huggingface.co/datdevsteve)  
**Model Type:** Text Classification  
**Language:** English (Medical Terminology)  
**Base Model:** [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT)  
**License:** MIT  

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

- **Symptom Classification**: Classify patient symptom descriptions into medical condition categories
- **Healthcare Triage**: Assist in initial assessment of symptom severity
- **Medical Chatbots**: Power conversational AI for healthcare assistance
- **Health Screening Apps**: Automated preliminary health assessments

### Out-of-Scope Use

- ❌ **Not for medical diagnosis**: This model provides guidance, not diagnosis
- ❌ **Not a replacement for doctors**: Always consult healthcare professionals
- ❌ **Not for emergency triage**: Use proper emergency services for critical cases
- ❌ **Not for prescription**: Cannot recommend medications or treatments

### Limitations and Bias
**Limitations**
- Language: Trained on English text only; may not perform well on other Indian languages
- Context: Optimized for common conditions; may underperform on rare diseases
- Cultural Context: While trained on Indian data, may not capture all regional variations
- Symptom Complexity: Works best with clear symptom descriptions; ambiguous cases may have lower accuracy
- Comorbidities: May not fully capture complex cases with multiple concurrent conditions

**Known Biases**
- Geographic Bias: Training data primarily from urban Indian healthcare settings
- Age Bias: Better performance on adult symptoms (20-60 years) due to data distribution
- Gender: Balanced training data, but some gender-specific conditions may have lower support

**Socioeconomic:** Terminology reflects middle-class Indian healthcare context

## How to Get Started with the Model

### Using Transformers Library
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "your-username/clinicalbert-indian-symptoms"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare input
text = "I have fever, headache and body pain for 2 days"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.softmax(logits, dim=-1)
    predicted_class = torch.argmax(probs, dim=-1).item()

# Get label
label = model.config.id2label[predicted_class]
confidence = probs[predicted_class].item()

print(f"Condition: {label}")
print(f"Confidence: {confidence:.2%}")
```
### Using Pipeline
```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="your-username/clinicalbert-indian-symptoms",
    top_k=5
)

result = classifier("I have persistent cough and chest congestion")
print(result)
```

## Training Details

### Training Data

**The Training Data is based off a compilation of 3 Kaggle Datasets:**
 - [Primary Dataset- Indian Healthcare Symptom-Disease Mapping Dataset](https://www.kaggle.com/datasets/bytesets/indian-healthcare-symptom-disease-mapping-dataset)
 - [Secondary Dataset 1](https://www.kaggle.com/datasets/dhivyeshrk/diseases-and-symptoms-dataset)<br>
 - [Secondary Dataset 2](https://www.kaggle.com/datasets/choongqianzheng/disease-and-symptoms-dataset)<br>
 - [Secondary Dataset 3 with Hindi Corpus](https://www.kaggle.com/datasets/aijain/hindi-health-dataset)<br>

### Training Procedure

**Preprocessing:**
- Text normalization and cleaning
- Medical term standardization
- Tokenization using ClinicalBERT tokenizer
- Max sequence length: 512 tokens

**Training Hyperparameters:**
```python
{
  "learning_rate": 2e-5,
  "batch_size": 16,
  "num_epochs": 5,
  "warmup_steps": 500,
  "weight_decay": 0.01,
  "optimizer": "AdamW",
  "lr_scheduler": "linear",
  "max_seq_length": 512
}
```
### Hardware:

Training Time: ~3 hours
GPU: NVIDIA T4 (16GB)
Framework: PyTorch 2.1.0, Transformers 4.36.0

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

Using test dataset made in compiled dataset splits

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

[More Information Needed]

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

[More Information Needed]

### Results

[More Information Needed]

#### Summary



## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

[More Information Needed]

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** [More Information Needed]
- **Hours used:** [More Information Needed]
- **Cloud Provider:** [More Information Needed]
- **Compute Region:** [More Information Needed]
- **Carbon Emitted:** [More Information Needed]

## Technical Specifications [optional]

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware

[More Information Needed]

#### Software

[More Information Needed]

## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Model Card Authors [optional]

[More Information Needed]

## Model Card Contact

[More Information Needed]