---
library_name: transformers
tags: []
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

### Model Description

This model is a fine-tuned version of google/flan-t5-small designed for medication-related question answering. The model was fine-tuned using a medication details dataset formatted as instruction-response examples. The goal of the model is to generate short educational responses to medication questions, such as what a medication is used for or what side effects may be associated with it.

This model was created for an academic final project and is intended for educational demonstration only. It should not be used as medical advice or as a replacement for a pharmacist, physician, or official drug information source.

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** [More Information Needed]
- **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [More Information Needed]
- **Model type:** [More Information Needed]
- **Language(s) (NLP):** [More Information Needed]
- **License:** [More Information Needed]
- **Finetuned from model [optional]:** [More Information Needed]

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [More Information Needed]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

This model can be used to generate short educational answers to basic medication-related questions. Example questions include:

- What is Metformin used for?
- What are the side effects of Ibuprofen?
- What is Atorvastatin used for?

The model is intended for demonstration and learning purposes.

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

This model should not be used for diagnosis, treatment decisions, medication selection, dosing recommendations, emergency medical questions, or professional clinical decision-making. It should not replace official drug references or advice from licensed healthcare professionals.

[More Information Needed]

## Bias, Risks, and Limitations

This model has several limitations. It was fine-tuned on a limited medication dataset and may generate incomplete, outdated, or incorrect information. 
The model does not verify answers against current clinical guidelines, drug databases, patient-specific information, allergies, medical history, or drug interactions.
Users should verify all medication information with a pharmacist, physician, or official drug reference.

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_id = "melisar2/pharmassist-flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

question = "What is Metformin used for?"

inputs = tokenizer(question, return_tensors="pt", truncation=True)
outputs = model.generate(
    **inputs,
    max_new_tokens=80,
    num_beams=4
)

answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(answer)

[More Information Needed]

## Training Details

### Training Data

The model was fine-tuned using the Medicine_Details.csv dataset. 
The dataset contains medication-related information and was formatted into instruction-response examples for training. 
The project used fields such as medication name, uses, and side effects to create medication question-answering prompts.
https://www.kaggle.com/datasets/swathigunti/medicine-details-csv
[More Information Needed]

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing [optional]

[More Information Needed]


#### Training Hyperparameters

- **Training regime:** [More Information Needed] <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

ROUGE scores were used to compare the model-generated answers with the expected reference answers. ROUGE is appropriate for this project because the task is text generation, and the evaluation compares generated text to target medication-related responses.
ROUGE Scores:
  ROUGE1:
    F-measure: 0.4037
    Precision: 0.4806
    Recall:    0.3996
  ROUGE2:
    F-measure: 0.2646
    Precision: 0.3011
    Recall:    0.2684
  ROUGEL:
    F-measure: 0.3837
    Precision: 0.4520
    Recall:    0.3815
### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

[More Information Needed]

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