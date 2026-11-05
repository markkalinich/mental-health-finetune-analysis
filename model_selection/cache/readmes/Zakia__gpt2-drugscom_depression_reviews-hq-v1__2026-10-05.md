---
license: apache-2.0
datasets:
- Zakia/drugscom_reviews
language:
- en
metrics:
- rewards mean change
- rewards median change
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

# Model Card for Zakia/gpt2-drugscom_depression_reviews-hq-v1

This model is a GPT-2-based language model further refined using Reinforcement Learning with Human Feedback (RLHF) on patient drug reviews related to depression from Drugs.com. 
The fine-tuning utilizes the 🤗 Hugging Face [Transformer Reinforcement Learning (TRL)](https://github.com/huggingface/trl) library to enhance the model's ability to generate high-quality synthetic patient reviews. 
The dataset used for fine-tuning is the [Zakia/drugscom_reviews](https://huggingface.co/datasets/Zakia/drugscom_reviews) dataset, which is filtered for the condition 'Depression'. 
The base model for fine-tuning was the [Zakia/gpt2-drugscom_depression_reviews](https://huggingface.co/Zakia/gpt2-drugscom_depression_reviews).

## Model Details

### Model Description

- Developed by: [Zakia](https://huggingface.co/Zakia)
- Model type: Text Generation with RLHF
- Language(s) (NLP): English
- License: Apache 2.0
- Base model: [Zakia/gpt2-drugscom_depression_reviews](https://huggingface.co/Zakia/gpt2-drugscom_depression_reviews)
- Reward model: [Zakia/distilbert-drugscom_depression_reviews](https://huggingface.co/Zakia/distilbert-drugscom_depression_reviews)

## Uses

### Direct Use

This model generates synthetic patient reviews of depression medications. It is intended for research, educational purposes, or to support professional healthcare insights.

### Out-of-Scope Use

Not intended for clinical use or to diagnose or treat health conditions.

## Bias, Risks, and Limitations

The model's outputs reflect patterns in the training data and should not be considered clinical advice. 
Biases present in the training data could be amplified.

### Recommendations

Use the model as a tool for generating synthetic patient reviews and for NLP research.

## How to Get Started with the Model

Use the code below to generate synthetic high quality drug reviews for depression with the model.

```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = "Zakia/gpt2-drugscom_depression_reviews-hq-v1"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate high-quality text
def generate_high_quality_review(prompt, model, tokenizer):
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
    print(generate_high_quality_review(prompt, model, tokenizer))
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

- Learning Rate: 1.41e-5
- Batch Size: 128

## Evaluation

- Rewards before and after RLHF

#### Metrics

The model's performance was evaluated based on rewards before and after RLHF.

### Results

### Evaluation Results

The RLHF fine-tuning was conducted using a dataset of patient reviews for depression. 
The model showed significant improvement in the synthetic reviews' quality.

| Metric                |   Before RLHF |   After RLHF |
|:----------------------|--------------:|-------------:|
| Rewards Mean Change   |        -1.622 |        1.416 |
| Rewards Median Change |        -1.828 |        2.063 |

The positive shift in rewards suggests that the model is now more adept at generating reviews that align 
with high-quality patient feedback.

## Technical Specifications

### Model Architecture and Objective

The GPT-2 architecture was enhanced through RLHF to produce text that closely resembles authentic patient experiences.

### Compute Infrastructure

The model was trained using a T4 GPU on Google Colab.

#### Hardware

T4 GPU via Google Colab.

## Citation

If you use this model, please cite both the original GPT-2 and DistilBERT papers:

**GPT-2 BibTeX:**

```bibtex
@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and others},
  year={2019}
}
```

**DistilBERT BibTeX:**

```bibtex
@article{sanh2019distilbert,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Sanh, Victor and Debut, Lysandre and Chaumond, Julien and Wolf, Thomas},
  journal={arXiv preprint arXiv:1910.01108},
  year={2019}
}
```

**APA:**

- Radford, A., et al. (2019). Language Models are Unsupervised Multitask Learners.
- Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. arXiv preprint arXiv:1910.01108.

## More Information

For further queries or issues with the model, please use the [discussions section on this model's Hugging Face page](https://huggingface.co/Zakia/gpt2-drugscom_depression_reviews-hq-v1/discussions).

## Model Card Authors

- [Zakia](https://huggingface.co/Zakia)

## Model Card Contact

For more information or inquiries regarding this model, please use the [discussions section on this model's Hugging Face page](https://huggingface.co/Zakia/gpt2-drugscom_depression_reviews-hq-v1/discussions).