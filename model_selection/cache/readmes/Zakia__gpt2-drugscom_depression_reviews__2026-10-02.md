---
license: apache-2.0
datasets:
- Zakia/drugscom_reviews
language:
- en
metrics:
- training loss
library_name: transformers
pipeline_tag: text-generation
tags:
- health
- medicine
- patient reviews
- drug reviews
- depression
- text generation
widget:
- text: After starting this new treatment, I felt
  example_title: Example 1
- text: I was apprehensive about the side effects of
  example_title: Example 2
- text: This medication has changed my life for the better
  example_title: Example 3
- text: I've had a terrible experience with this medication
  example_title: Example 4
- text: Since I began taking L-methylfolate, my experience has been
  example_title: Example 5
---

# Model Card for Zakia/gpt2-drugscom_depression_reviews

This model is a GPT-2-based language model fine-tuned on drug reviews for the depression medical condition from Drugs.com. 
The dataset used for fine-tuning is the [Zakia/drugscom_reviews](https://huggingface.co/datasets/Zakia/drugscom_reviews) dataset, which is filtered for the condition 'Depression'. 
The base model for fine-tuning was the [gpt2](https://huggingface.co/gpt2).

## Model Details

### Model Description

- Developed by: [Zakia](https://huggingface.co/Zakia)
- Model type: Text Generation
- Language(s) (NLP): English
- License: Apache 2.0
- Finetuned from model: gpt2

## Uses

### Direct Use

This model is intended to generate text that mimics patient reviews of depression medications, useful for understanding patient sentiments and experiences.

### Out-of-Scope Use

This model is not designed to diagnose or treat depression or to replace professional medical advice.

## Bias, Risks, and Limitations

The model may inherit biases present in the dataset and should be used with caution in decision-making processes.

### Recommendations

Use the model as a tool for generating synthetic patient reviews and for NLP research.

## How to Get Started with the Model

Use the code below to generate synthetic reviews with the model.

```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = "Zakia/gpt2-drugscom_depression_reviews"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate text
def generate_review(prompt, model, tokenizer):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage for various scenarios
prompts = [
    "After starting this new treatment, I felt",
    "I was apprehensive about the side effects of",
    "This medication has changed my life for the better",
    "I've had a terrible experience with this medication",
    "Since I began taking L-methylfolate, my experience has been"
]

for prompt in prompts:
    print(f"Prompt: {prompt}")
    print(generate_review(prompt, model, tokenizer))
    print()
```

## Training Details

### Training Data

The model was fine-tuned on patient reviews related to depression, filtered from Drugs.com.
This dataset is accessible from [Zakia/drugscom_reviews](https://huggingface.co/datasets/Zakia/drugscom_reviews) on Hugging Face datasets (condition = 'Depression') for 'train'.
Number of records in train dataset: 9069 rows.

### Training Procedure 

#### Preprocessing

The reviews were cleaned and preprocessed to remove quotes, HTML tags and decode HTML entities.

#### Training Hyperparameters

- Batch Size: 2
- Epochs: 5

## Evaluation

- Training Loss

#### Metrics

The model's performance was evaluated based on Training Loss.

### Results

The fine-tuning process yielded the following results:

| Epoch | Training Loss | Training Runtime | Training Samples | Training Samples per Second | Training Steps per Second |
|-------|---------------|------------------|------------------|-----------------------------|---------------------------|
| 5.0   | 0.5944        | 2:15:40.11       | 4308             | 2.646                       | 1.323                     |

The fine-tuning process achieved a final training loss of 0.5944 after 5 epochs, with the model processing 
approximately 2.646 samples per second and completing 1.323 training steps per second over a training runtime 
of 2 hours, 15 minutes, and 40 seconds.

## Technical Specifications

### Model Architecture and Objective

GPT-2 model architecture was used, with the objective of generating coherent and contextually relevant text based on patient reviews.

### Compute Infrastructure

The model was trained using a T4 GPU on Google Colab.

#### Hardware

T4 GPU via Google Colab.

## Citation

If you use this model, please cite the original GPT-2 paper:

**BibTeX:**

```bibtex
@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and others},
  year={2019}
}
```
**APA:**

Radford, A., et al. (2019). Language Models are Unsupervised Multitask Learners.

## More Information

For further queries or issues with the model, please use the [discussions section on this model's Hugging Face page](https://huggingface.co/Zakia/gpt2-drugscom_depression_reviews/discussions).

## Model Card Authors

- [Zakia](https://huggingface.co/Zakia)

## Model Card Contact

For more information or inquiries regarding this model, please use the [discussions section on this model's Hugging Face page](https://huggingface.co/Zakia/gpt2-drugscom_depression_reviews/discussions).