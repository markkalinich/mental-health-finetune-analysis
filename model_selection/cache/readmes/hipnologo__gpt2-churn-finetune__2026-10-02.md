---
datasets:
- hipnologo/churn_textual_label
- hipnologo/telecom_churn
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- churn
- gpt2
- sentiment-analysis
- fine-tuned
widget:
- text: "Can you tell me about a customer from MD with an account length of 189 and area code 415 who does not have an international plan, and has a voice mail plan and that have made 1 customer service calls."
- text: "Can you tell me about a customer from SC with an account length of 87 and area code 408 who does not have an international plan, and does not have a voice mail plan and that have made 2 customer service calls."
---

# Fine-tuned GPT-2 Model for Telecom Churn Analysis

## Model Description

This is a GPT-2 model fine-tuned on the Telecom Churn dataset for churn analysis. It classifies a customer's text into two classes: "churn" or "no churn".

## Intended Uses & Limitations

This model is intended to be used for binary churn analysis of English customer texts. It can determine whether a customer is likely to churn or not. It should not be used for languages other than English, or for text with ambiguous churn indications.

## How to Use

Here's a simple way to use this model:

```python
from transformers import GPT2Tokenizer, GPT2ForSequenceClassification

tokenizer = GPT2Tokenizer.from_pretrained("hipnologo/gpt2-churn-finetune")
model = GPT2ForSequenceClassification.from_pretrained("hipnologo/gpt2-churn-finetune")

text = "Your customer text here!"

# encoding the input text
input_ids = tokenizer.encode(text, return_tensors="pt")

# Move the input_ids tensor to the same device as the model
input_ids = input_ids.to(model.device)

# getting the logits 
logits = model(input_ids).logits

# getting the predicted class
predicted_class = logits.argmax(-1).item()

print(f"The churn prediction by the model is: {'Churn' if predicted_class == 1 else 'No Churn'}")
```

## Training Procedure
The model was trained using the 'Trainer' class from the transformers library, with a learning rate of `2e-5`, batch size of 1, and 3 training epochs.

## Evaluation
The fine-tuned model was evaluated on the test dataset. Here are the results:

- Evaluation Loss: 0.28965
- Evaluation Accuracy: 0.9
- Evaluation F1 Score: 0.90239
- Evaluation Precision: 0.85970
- Evaluation Recall: 0.94954

The evaluation metrics suggest that the model has a high accuracy and good precision-recall balance for the task of churn classification.

## How to Reproduce
The evaluation results can be reproduced by loading the model and the tokenizer from Hugging Face Model Hub and then running the model on the evaluation dataset using the Trainer class from the Transformers library, with the compute_metrics function defined as above.

The evaluation loss is the cross-entropy loss of the model on the evaluation dataset, a measure of how well the model's predictions match the actual labels. The closer this is to zero, the better.

The evaluation accuracy is the proportion of predictions the model got right. This number is between 0 and 1, with 1 meaning the model got all predictions right.

The F1 score is a measure of a test's accuracy that considers both precision (the number of true positive results divided by the number of all positive results) and recall (the number of true positive results divided by the number of all samples that should have been identified as positive). An F1 score reaches its best value at 1 (perfect precision and recall) and worst at 0.

The evaluation precision is how many of the positively classified were actually positive. The closer this is to 1, the better.

The evaluation recall is how many of the actual positives our model captured through labeling it as positive. The closer this is to 1, the better.

## Fine-tuning Details
The model was fine-tuned using the Telecom Churn dataset.
