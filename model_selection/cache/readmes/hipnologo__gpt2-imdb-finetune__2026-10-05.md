---
datasets:
- imdb
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- movies
- gpt2
- sentiment-analysis
- fine-tuned
license: mit
widget:
- text: "What an inspiring movie, I laughed, cried and felt love."
- text: "This film fails on every count. For a start it is pretentious, striving to be significant and failing miserably."
---

# Fine-tuned GPT-2 Model for IMDb Movie Review Sentiment Analysis

## Model Description

This is a GPT-2 model fine-tuned on the IMDb movie review dataset for sentiment analysis. It classifies a movie review text into two classes: "positive" or "negative".

## Intended Uses & Limitations

This model is intended to be used for binary sentiment analysis of English movie reviews. It can determine whether a review is positive or negative. It should not be used for languages other than English, or for text with ambiguous sentiment.

## How to Use

Here's a simple way to use this model:

```python
from transformers import GPT2Tokenizer, GPT2ForSequenceClassification

tokenizer = GPT2Tokenizer.from_pretrained("hipnologo/gpt2-imdb-finetune")
model = GPT2ForSequenceClassification.from_pretrained("hipnologo/gpt2-imdb-finetune")

text = "Your review text here!"

# encoding the input text
input_ids = tokenizer.encode(text, return_tensors="pt")

# Move the input_ids tensor to the same device as the model
input_ids = input_ids.to(model.device)

# getting the logits 
logits = model(input_ids).logits

# getting the predicted class
predicted_class = logits.argmax(-1).item()

print(f"The sentiment predicted by the model is: {'Positive' if predicted_class == 1 else 'Negative'}")
```

## Training Procedure
The model was trained using the 'Trainer' class from the transformers library, with a learning rate of 2e-5, batch size of 1, and 3 training epochs.

## Evaluation

The fine-tuned model was evaluated on the test dataset. Here are the results:

- **Evaluation Loss**: 0.23127
- **Evaluation Accuracy**: 0.94064
- **Evaluation F1 Score**: 0.94104
- **Evaluation Precision**: 0.93466
- **Evaluation Recall**: 0.94752

The evaluation metrics suggest that the model has a high accuracy and good precision-recall balance for the task of sentiment classification.

### How to Reproduce

The evaluation results can be reproduced by loading the model and the tokenizer from Hugging Face Model Hub and then running the model on the evaluation dataset using the `Trainer` class from the Transformers library, with the `compute_metrics` function defined as above.

The evaluation loss is the cross-entropy loss of the model on the evaluation dataset, a measure of how well the model's predictions match the actual labels. The closer this is to zero, the better.

The evaluation accuracy is the proportion of predictions the model got right. This number is between 0 and 1, with 1 meaning the model got all predictions right.

The F1 score is a measure of a test's accuracy that considers both precision (the number of true positive results divided by the number of all positive results) and recall (the number of true positive results divided by the number of all samples that should have been identified as positive). An F1 score reaches its best value at 1 (perfect precision and recall) and worst at 0.

The evaluation precision is how many of the positively classified were actually positive. The closer this is to 1, the better.

The evaluation recall is how many of the actual positives our model captured through labeling it as positive. The closer this is to 1, the better.

## Fine-tuning Details
The model was fine-tuned using the IMDb movie review dataset.