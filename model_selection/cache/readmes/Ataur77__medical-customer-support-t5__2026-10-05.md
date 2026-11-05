---
library_name: transformers
tags: []
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

### Model Description

This model is designed to classify customer queries in the healthcare domain. The model classifies the following aspects of a healthcare-related query:

- **Intent**: The purpose or action requested in the query (e.g., `Appointment Rescheduling`, `Insurance Claim Assistance`).
- **Department**: The department to which the query is related (e.g., `Pediatrics`, `ENT`, `Dermatology`).
- **Level**: The urgency level of the query (`Medium`, `Soon`, `Emergency`).

This model is based on a **T5 architecture** fine-tuned on a dataset of 3,800 entries of healthcare customer queries, and it helps in building **automated healthcare assistants**, **query triaging systems**, or **customer support tools** that understand and categorize user requests.

- **Developed by:** Ataur Rahman Likhon
- **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [More Information Needed]
- **Model type:** Text Classification
- **Language(s) (NLP):** English
- **License:** [More Information Needed]
- **Finetuned from model [optional]:** T5

### Model Sources [optional]

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

### Direct Use

The model can be used to classify customer queries in healthcare-related domains, providing businesses with a tool to automatically triage and categorize queries to the right department or team. It can be integrated into chatbot applications or support systems for better customer interaction.

### Downstream Use [optional]

The model can be fine-tuned further for specific use cases such as insurance claim processing or appointment booking systems within the healthcare industry. 

### Out-of-Scope Use

This model is not suitable for use in non-healthcare contexts or for queries outside the scope of customer service in healthcare.

## Bias, Risks, and Limitations

The model may exhibit biases in how it handles queries from underrepresented departments or urgent levels. It may also not perform well on queries that deviate significantly from the provided dataset or that require highly specialized knowledge outside of the healthcare domain.

### Recommendations

Users should be aware that the model might struggle with out-of-scope queries or rare edge cases. It is recommended to continuously monitor and update the model based on user feedback to improve performance over time.

## How to Get Started with the Model

Use the following code to load and use the model:

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load pre-trained model
model = T5ForConditionalGeneration.from_pretrained('path_to_model')
tokenizer = T5Tokenizer.from_pretrained('path_to_tokenizer')

# Example usage
input_text = "How do I proceed with insurance claim assistance in ENT?"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(inputs['input_ids'])
decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded_output)
```

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

Use the code below to get started with the model.

[More Information Needed]

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

[More Information Needed]

### Training Procedure


-**Training Hyperparameters**
- - Training regime: fp16 mixed precision

- **Speeds, Sizes**
- - The training was conducted on a medium-scale machine with multiple GPUs.

#### Preprocessing [optional]
The training data was preprocessed by tokenizing the text using a T5 tokenizer, and the data was split into training and validation sets for fine-tuning.

#### Training Hyperparameters

- **Training regime:** [More Information Needed] <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

[More Information Needed]

#### Factors

The evaluation considered different domains (departments) and urgency levels as factors to assess the model's robustness.

[More Information Needed]

#### Metrics

The model was evaluated using accuracy, precision, recall, and F1-score for each category: intent, department, and urgency.

### Results

The model achieved an accuracy of 92% in classifying intents, 90% for department classification, and 88% for urgency classification.

#### Summary
The model performs well across the three categories with good generalization to unseen queries in the healthcare domain.


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