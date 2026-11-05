---
library_name: transformers
tags:
- sentiment-analysis
- text-classification
- bert
datasets:
- stanfordnlp/sst2
language:
- en
base_model:
- google-bert/bert-base-uncased
license: apache-2.0
---

# Model Card for Model ID

This is a fine tuned BERT for binary sentiment on SST2 that classifies the sentences as Positive or Negative snetiments. Built upon original bert-base-uncased model



## Model Details

### Model Description

Starting from a bert-base uncased model I finetuned the model on SST2 to give two output classifications based on the input sentence. The classification sentiment can be either Positive (1) or Negative (0)


This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** br090491
- **Funded by None**
- **Shared by br090491**
- **Model type:** Classification
- **Language(s) (NLP):** English
- **License:** apache-2.0
- **Finetuned from model [optional]:** bert-base-uncased

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [bert-sst2-finetuned]
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

To classify if the sentiment of a sentence is positive or negative

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

Anything apart from positive or negative sentiment analysis of a sentence

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="br090491/bert-sst2-finetuned")

print(classifier("This movie was absolutely fantastic, I loved it!"))
print(classifier("This film was a complete waste of time."))
print(classifier("Add your own sentence"))
# [{'label': 'positive', 'score': 0.9998}]
```

[More Information Needed]

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

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

<!-- This section describes the evaluation protocols and provides the results. -->

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

Fine-tuned on SST-2, this model reaches **92.5% accuracy** on the validation set.

Accuracy is the right metric here because this is a **balanced binary classifier** —
each input gets one of two labels and the classes are roughly even, so the fraction
correct is a faithful summary. (Perplexity does not apply: it scores next-token
language models, not classifiers.)

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