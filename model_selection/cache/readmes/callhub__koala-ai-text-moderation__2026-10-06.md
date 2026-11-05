---
tags:
- autotrain
- text-classification
language:
- en
widget:
- text: I love AutoTrain
- text: I absolutely hate those people
- text: I love cake!
- text: >-
    lets build the wall and deport illegals "they walk across the border like
    this is Central park"
- text: EU offers to pay countries 6,000 euros per person to take in migrants
datasets:
- mmathys/openai-moderation-api-evaluation
- KoalaAI/Text-Moderation-v2-small
co2_eq_emissions:
  emissions: 0.03967468113268738
license: openrail
---

# Text Moderation
This model is a text classification model based on Deberta-v3 that predicts whether a text contains text that could be considered offensive.
It is split up in the following labels:

| Category | Label | Definition |
| -------- | ----- | ---------- |
| sexual   | `S`   | Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness). |
| hate     | `H`   | Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. |
| violence | `V`   | Content that promotes or glorifies violence or celebrates the suffering or humiliation of others. |
| harassment       | `HR`   | Content that may be used to torment or annoy individuals in real life, or make harassment more likely to occur. |
| self-harm        | `SH`   | Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders. |
| sexual/minors    | `S3`   | Sexual content that includes an individual who is under 18 years old. |
| hate/threatening | `H2`   | Hateful content that also includes violence or serious harm towards the targeted group. |
| violence/graphic | `V2`   | Violent content that depicts death, violence, or serious physical injury in extreme graphic detail. |
| OK | `OK` | Not offensive

It's important to remember that this model was only trained on English texts, and may not perform well on non-English inputs.

## Ethical Considerations
This is a model that deals with sensitive and potentially harmful language. Users should consider the ethical implications and potential risks of using or deploying this model in their applications or contexts. Some of the ethical issues that may arise are:

- The model may reinforce or amplify existing biases or stereotypes in the data or in the society. For example, the model may associate certain words or topics with offensive language based on the frequency or co-occurrence in the data, without considering the meaning or intent behind them. This may result in unfair or inaccurate predictions for some groups or individuals.

Users should carefully consider the purpose, context, and impact of using this model, and take appropriate measures to prevent or mitigate any potential harm. Users should also respect the privacy and consent of the data subjects, and adhere to the relevant laws and regulations in their jurisdictions.

## License

This model is licensed under the CodeML OpenRAIL-M 0.1 license, which is a variant of the BigCode OpenRAIL-M license. This license allows you to freely access, use, modify, and distribute this model and its derivatives, for research, commercial or non-commercial purposes, as long as you comply with the following conditions:

- You must include a copy of the license and the original source of the model in any copies or derivatives of the model that you distribute.
- You must not use the model or its derivatives for any unlawful, harmful, abusive, discriminatory, or offensive purposes, or to cause or contribute to any social or environmental harm.
- You must respect the privacy and consent of the data subjects whose data was used to train or evaluate the model, and adhere to the relevant laws and regulations in your jurisdiction.
- You must acknowledge that the model and its derivatives are provided "as is", without any warranties or guarantees of any kind, and that the licensor is not liable for any damages or losses arising from your use of the model or its derivatives.

By accessing or using this model, you agree to be bound by the terms of this license. If you do not agree with the terms of this license, you must not access or use this model.

## Training Details
- Problem type: Multi-class Classification
- CO2 Emissions (in grams): 0.0397

## Validation Metrics

- Loss: 0.848
- Accuracy: 0.749 (75%)
- Macro F1: 0.326
- Micro F1: 0.749
- Weighted F1: 0.703
- Macro Precision: 0.321
- Micro Precision: 0.749
- Weighted Precision: 0.671
- Macro Recall: 0.349
- Micro Recall: 0.749
- Weighted Recall: 0.749


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/KoalaAI/Text-Moderation
```

Or Python API:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("KoalaAI/Text-Moderation")
tokenizer = AutoTokenizer.from_pretrained("KoalaAI/Text-Moderation")

# Run the model on your input
inputs = tokenizer("I love AutoTrain", return_tensors="pt")
outputs = model(**inputs)

# Get the predicted logits
logits = outputs.logits

# Apply softmax to get probabilities (scores)
probabilities = logits.softmax(dim=-1).squeeze()

# Retrieve the labels
id2label = model.config.id2label
labels = [id2label[idx] for idx in range(len(probabilities))]

# Combine labels and probabilities, then sort
label_prob_pairs = list(zip(labels, probabilities))
label_prob_pairs.sort(key=lambda item: item[1], reverse=True)  

# Print the sorted results
for label, probability in label_prob_pairs:
    print(f"Label: {label} - Probability: {probability:.4f}") 
```

The output of the above Python code will look like this:
```
Label: OK - Probability: 0.9840
Label: H - Probability: 0.0043
Label: SH - Probability: 0.0039
Label: V - Probability: 0.0019
Label: S - Probability: 0.0018
Label: HR - Probability: 0.0015
Label: V2 - Probability: 0.0011
Label: S3 - Probability: 0.0010
Label: H2 - Probability: 0.0006
```