---
library_name: transformers
tags:
- 'model: llama_chat'
- 'repo_name: llama_chat_block_2_suicide_risk_All'
- 'file_name: llama_chat_block_2_suicide_risk_All_5000_5.pt'
- 'base_model: meta-llama/Llama-2-7b-chat-hf'
- 'pruning_style: block'
- 'community: 2'
- 'pruning_ratio: 20'
- 'dataset_label: suicide_risk'
- 'sparsity_ratio: 20'
- 'dataset: [''tasksource/bigbench'', ''suicide_risk'']'
- 'finetune: All'
- 'modules_size: 33'
- 'modules: [''10_attn.q'', ''10_attn.v'', ''12_attn.o'', ''13_attn.q'', ''13_attn.v'',
  ''14_attn.k'', ''15_attn.k'', ''15_attn.v'', ''16_attn.o'', ''17_attn.o'', ''17_attn.q'',
  ''17_attn.v'', ''18_attn.k'', ''18_attn.q'', ''20_attn.v'', ''21_attn.k'', ''21_attn.v'',
  ''22_attn.v'', ''23_attn.v'', ''24_attn.k'', ''24_attn.o'', ''24_attn.q'', ''26_attn.k'',
  ''27_attn.o'', ''28_attn.q'', ''30_attn.o'', ''3_attn.k'', ''4_attn.o'', ''4_attn.v'',
  ''7_attn.q'', ''7_attn.v'', ''8_attn.k'', ''9_attn.k'']'
- 'rank: 2'
- 'tags: [''model: llama_chat'', ''repo_name: llama_chat_block_2_suicide_risk_All'',
  ''file_name: llama_chat_block_2_suicide_risk_All_5000_5.pt'', ''base_model: meta-llama/Llama-2-7b-chat-hf'',
  ''pruning_style: block'', ''community: 2'', ''pruning_ratio: 20'', ''dataset_label:
  suicide_risk'', ''sparsity_ratio: 20'', "dataset: [''tasksource/bigbench'', ''suicide_risk'']",
  ''finetune: All'', ''modules_size: 33'', "modules: [''10_attn.q'', ''10_attn.v'',
  ''12_attn.o'', ''13_attn.q'', ''13_attn.v'', ''14_attn.k'', ''15_attn.k'', ''15_attn.v'',
  ''16_attn.o'', ''17_attn.o'', ''17_attn.q'', ''17_attn.v'', ''18_attn.k'', ''18_attn.q'',
  ''20_attn.v'', ''21_attn.k'', ''21_attn.v'', ''22_attn.v'', ''23_attn.v'', ''24_attn.k'',
  ''24_attn.o'', ''24_attn.q'', ''26_attn.k'', ''27_attn.o'', ''28_attn.q'', ''30_attn.o'',
  ''3_attn.k'', ''4_attn.o'', ''4_attn.v'', ''7_attn.q'', ''7_attn.v'', ''8_attn.k'',
  ''9_attn.k'']", ''rank: 2'']'
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

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