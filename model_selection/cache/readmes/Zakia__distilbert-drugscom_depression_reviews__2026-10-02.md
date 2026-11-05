---
license: apache-2.0
datasets:
- Zakia/drugscom_reviews
language:
- en
metrics:
- accuracy
library_name: transformers
pipeline_tag: text-classification
tags:
- health
- medicine
- patient reviews
- drug reviews
- depression
- text classification
widget:
- text: "After starting this new treatment, I felt an immediate improvement in my mood and energy levels."
  example_title: "Example 1"
- text: "I was apprehensive about the side effects of the medication, but thankfully I haven't experienced any."
  example_title: "Example 2"
- text: "This medication has changed my life for the better. I've experienced no side effects and my symptoms of depression have significantly decreased."
  example_title: "Example 3"
- text: "I've had a terrible experience with this medication. It made me feel nauseous and I didn't notice any improvement in my condition."
  example_title: "Example 4"
- text: "Since I began taking L-methylfolate, my experience has been overwhelmingly positive with noticeable improvements."
  example_title: "Example 5"
---

# Model Card for Zakia/distilbert-drugscom_depression_reviews

This model is a DistilBERT-based classifier fine-tuned on drug reviews for the depression medical condition from Drugs.com. 
The dataset used for fine-tuning is the [Zakia/drugscom_reviews](https://huggingface.co/datasets/Zakia/drugscom_reviews) dataset, which is filtered for the condition 'Depression'. 
The base model for fine-tuning was the [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased).

## Model Details

### Model Description

- Developed by: [Zakia](https://huggingface.co/Zakia)
- Model type: Text Classification
- Language(s) (NLP): English
- License: Apache 2.0
- Finetuned from model: distilbert-base-uncased

## Uses

### Direct Use

This model is intended to classify drug reviews into high or low quality, aiding in the analysis of patient feedback on depression medications.

### Out-of-Scope Use

This model is not designed to diagnose or treat depression or to replace professional medical advice.

## Bias, Risks, and Limitations

The model may inherit biases present in the dataset and should not be used as the sole decision-maker for healthcare or treatment options.

### Recommendations

Use the model as a tool to support, not replace, professional judgment.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch.nn.functional as F

model_name = "Zakia/distilbert-drugscom_depression_reviews"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define a function to print predictions with labels
def print_predictions(review_text, model, tokenizer):
    inputs = tokenizer(review_text, return_tensors="pt")
    outputs = model(**inputs)
    predictions = F.softmax(outputs.logits, dim=-1)
    # LABEL_0 is for low quality and LABEL_1 for high quality
    print(f"Review: \"{review_text}\"")
    print(f"Prediction: {{'LABEL_0 (Low Quality)': {predictions[0][0].item():.4f}, 'LABEL_1 (High Quality)': {predictions[0][1].item():.4f}}}\n")

# Example usage for various scenarios
example_reviews = [
    "After starting this new treatment, I felt an immediate improvement in my mood and energy levels.",
    "I was apprehensive about the side effects of the medication, but thankfully I haven't experienced any.",
    "This medication has changed my life for the better. I've experienced no side effects and my symptoms of depression have significantly decreased.",
    "I've had a terrible experience with this medication. It made me feel nauseous and I didn't notice any improvement in my condition.",
    "Since I began taking L-methylfolate, my experience has been overwhelmingly positive with noticeable improvements."
]

for review in example_reviews:
    print_predictions(review, model, tokenizer)
```

## Training Details

### Training Data

The model was fine-tuned on a dataset of drug reviews specifically related to depression, filtered from Drugs.com.
This dataset is accessible from [Zakia/drugscom_reviews](https://huggingface.co/datasets/Zakia/drugscom_reviews) on Hugging Face datasets (condition = 'Depression') for 'train'.
Number of records in train dataset: 9069 rows.

### Training Procedure 

#### Preprocessing

The reviews were cleaned and preprocessed to remove quotes, HTML tags and decode HTML entities.
A new column called 'high_quality_review' was also added to the reviews.
'high_quality_review' was computed as 1 if rating > 5 (positive rating) and usefulCount > the 75th percentile of usefulCount (65) or 0, otherwise.
Train dataset high_quality_review counts: Counter({0: 6949, 1: 2120})
Then:
This training data was balanced by downsampling low quality reviews (high_quality_review = 0).
The final training data had 4240 rows of reviews:
Train dataset high_quality_review counts: Counter({0: 2120, 1: 2120})

#### Training Hyperparameters

- Learning Rate: 3e-5
- Batch Size: 16
- Epochs: 1

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The model was tested on a dataset of drug reviews specifically related to depression, filtered from Drugs.com.
This dataset is accessible from [Zakia/drugscom_reviews](https://huggingface.co/datasets/Zakia/drugscom_reviews) on Hugging Face datasets (condition = 'Depression') for 'test'.
Number of records in test dataset: 3095 rows.

#### Preprocessing

The reviews were cleaned and preprocessed to remove quotes, HTML tags and decode HTML entities.
A new column called 'high_quality_review' was also added to the reviews.
'high_quality_review' was computed as 1 if rating > 5 (positive rating) and usefulCount > the 75th percentile of usefulCount (65) or 0, otherwise.
Note: the 75th percentile of usefulCount is based on the train dataset.
Test dataset high_quality_review counts: Counter({0: 2365, 1: 730})

#### Metrics

The model's performance was evaluated based on accuracy.

### Results

The fine-tuning process yielded the following results:

| Epoch | Training Loss | Validation Loss | Accuracy |
|-------|---------------|-----------------|----------|
| 1     | 0.38          | 0.80            | 0.77     |

The model demonstrates its capability to classify drug reviews as high or low quality with an accuracy of 77%.
Low Quality: high_quality_review=0
High Quality: high_quality_review=1

## Technical Specifications

### Model Architecture and Objective

DistilBERT model architecture was used, with a binary classification head for high and low quality review classification.

### Compute Infrastructure

The model was trained using a T4 GPU on Google Colab.

#### Hardware

T4 GPU via Google Colab.

## Citation

If you use this model, please cite the original DistilBERT paper:

**BibTeX:**

```bibtex
@article{sanh2019distilbert,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Sanh, Victor and Debut, Lysandre and Chaumond, Julien and Wolf, Thomas},
  journal={arXiv preprint arXiv:1910.01108},
  year={2019}
}
```
**APA:**

Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. arXiv preprint arXiv:1910.01108.

## Glossary

- Low Quality Review: high_quality_review=0
- High Quality Review: high_quality_review=1

## More Information

For further queries or issues with the model, please use the [discussions section on this model's Hugging Face page](https://huggingface.co/Zakia/distilbert-drugscom_depression_reviews/discussions).


## Model Card Authors

- [Zakia](https://huggingface.co/Zakia)

## Model Card Contact

For more information or inquiries regarding this model, please use the [discussions section on this model's Hugging Face page](https://huggingface.co/Zakia/distilbert-drugscom_depression_reviews/discussions).