---
license: cc-by-nc-4.0
datasets:
- ai4privacy/pii-masking-400k
language:
- en
- de
- fr
- it
- es
- nl
base_model:
- iiiorg/piiranha-v1-detect-personal-information
tags:
- NeuralWave
- Hackathon
---
## Overview

This model serves to enhance the precision and accuracy of personal information detection by utilizing a reduced label set compared to its base model. Through this refinement, it aims to provide superior labeling precision for identifying personal information across multiple languages.

---

## Features

- **Improved Precision**: By reducing the label set size from the base model, the model enhances the precision of the labeling procedure, ensuring more reliable identification of sensitive information.

- **Model Versions**:
- **Maximum Accuracy Focus**: This version aims to achieve the highest possible accuracy in the detection process, making it suitable for applications where minimizing errors is crucial.
- **Maximum Precision Focus**: This variant is designed to maximize the precision of the detection, ideal for scenarios where false positives are particularly undesirable.

---

## Installation

To run this model, you will need to install the dependencies:

```bash
pip install torch transformers safetensors
```

---

## Usage


Load and run the model using PyTorch and transformers:

```python
from transformers import AutoModelForTokenClassification, AutoConfig, BertTokenizerFast
from safetensors.torch import load_file

# Load the config
config = AutoConfig.from_pretrained("folder_to_model")

# Initialize the model with the config
model = AutoModelForTokenClassification.from_config(config)

# Load the safetensors weights
state_dict = load_file("folder_to_tensors")

# Load the state dict into the model
model.load_state_dict(state_dict)

# Load the tokenizer
tokenizer = BertTokenizerFast.from_pretrained("google-bert/bert-base-multilingual-cased")

# Load the label mapper if needed
with open("pii_model/label_mapper.json", 'r') as f:
    label_mapper_data = json.load(f)

label_mapper = LabelMapper()
label_mapper.label_to_id = label_mapper_data['label_to_id']
label_mapper.id_to_label = {int(k): v for k, v in label_mapper_data['id_to_label'].items()}
label_mapper.num_labels = label_mapper_data['num_labels']

# Process outputs for analysis...
```

---

## Evaluation

- **Accuracy Model**: Focused on minimizing errors, evaluates to achieve the highest accuracy metrics.
- **Precision Model**: Designed to minimize false positives, optimizing for precision-driven applications.

---

## Disclaimer 
The publisher of this repository is not affiliated with Ai4Privacy and Ai Suisse SA

## Honorary Mention
This repo created during the Hackaton organized by [NeuralWave](https://neuralwave.ch/#/)