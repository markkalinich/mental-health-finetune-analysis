---
license: mit
language:
- tr
base_model:
- dbmdz/bert-base-turkish-cased
pipeline_tag: text-classification
library_name: transformers
---

# Model Card for Model ID

yeniguno/absa-turkish-bert-dbmdz

This model is fine-tuned to detect sentiment in Turkish text with respect to specific aspects. It has been designed for the ABSA task, where the model receives both an aspect (span) and a text and predicts the sentiment towards the aspect.

## Model Details

### Model Description

- **Base Model**: `dbmdz/bert-base-turkish-cased`
- **Fine-tuning Task**: Aspect-Based Sentiment Analysis (ABSA) for Turkish text.
- **Language**: Turkish
- **Labels**: Sentiment classification (`positive`, `neutral`, `negative`)

## Uses

### Direct Use

- **ABSA**: This model is used for Aspect-Based Sentiment Analysis in Turkish, where users can provide a text along with a specific aspect, and the model will predict the sentiment (positive, neutral, or negative) towards that aspect.

### Downstream Use [optional]

- This model can be used in downstream applications such as:
  - **Brand Monitoring**: Analyze customer feedback or social media mentions to determine sentiment towards specific brands.
  - **Marketing Analysis**: Understand how consumers feel about specific brands in product reviews or survey responses.

### Out-of-Scope Use

- **General Sentiment Analysis**: The model is fine-tuned specifically for brand names as aspects and may not generalize well to other aspects or tasks.
- **Other Languages**: The model is trained only on Turkish data and will likely perform poorly on other languages without additional fine-tuning.
- **Non-brand related aspects**: The model is specialized for brand-related sentiments and may not perform well on aspects outside of brand names.

## Recommendations
Users should be aware of the model’s limitations and biases, especially in sensitive applications like brand reputation management. Additional validation may be necessary for specific use cases to ensure fairness and accuracy.

## How to Get Started with the Model

Use the code below to get started with the model.


```python
from transformers import pipeline

pipe = pipeline("text-classification", model="yeniguno/absa-turkish-bert-dbmdz")

text = "Sony'nin ses sistemleri tam anlamıyla harika, her ayrıntıyı net bir şekilde duyabiliyorum ve tasarımı da oldukça şık."

response = pipe(text, text_pair="Sony")

print(response)

# [{'label': 'LABEL_2', 'score': 0.9998026490211487}]

text = "Apple'ın tabletleri çok kullanışlı ve uzun ömürlü, ancak kulaklıklarının dayanıklılığı hayal kırıklığı yaratıyor."

response = pipe(text, text_pair="tablet")
print(response)
# [{'label': 'LABEL_2', 'score': 0.9978420734405518}]

response = pipe(text, text_pair="kulaklık")
print(response)
# [{'label': 'LABEL_0', 'score': 0.9996157884597778}]
```
```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "yeniguno/absa-turkish-bert-dbmdz"

text = "Samsung'un televizyonları mükemmel bir görüntü kalitesine sahip."
span = "televizyon"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Tokenize the text and the aspect (span)
inputs = tokenizer(span, text, truncation=True, padding='max_length', max_length=128, return_tensors="pt")

# Put model in evaluation mode
model.eval()

# Get the model output (predictions)
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted label
logits = outputs.logits
predicted_class_id = torch.argmax(logits, dim=-1).item()

# Map the prediction back to the label
id_to_label = {0: "negative", 1: "neutral", 2: "positive"}
predicted_label = id_to_label[predicted_class_id]

print(f"Predicted sentiment: {predicted_label}")
# Predicted sentiment: positive
```
## Training Details

### Training Data
The training data used for fine-tuning this model consists of a mix of several datasets that were adapted to the Turkish language for Aspect-Based Sentiment Analysis (ABSA). The datasets include:

- `alexcadillon/SemEval2014Task4`
- `PNLPhub/Pars-ABSA`
- `STNM-NLPhoenix/turkish-absa`
- `Alpaca69B reviews datasets`
- `pahri/setfit-absa-indo-restaurantmix`
- `ABSA-QUAD-master`

In total, the training data includes 231,753 instances, while the test data consists of 57,905 instances. Non-Turkish examples from the original datasets were translated and arranged to be compatible with Turkish language processing, ensuring consistency in the aspect-based sentiment analysis task.

### Training Procedure

#### Preprocessing
- **Text Tokenization**: The text data was tokenized using the BERT tokenizer (`dbmdz/bert-base-turkish-cased`), with padding and truncation applied to a maximum length of 128 tokens.
- **Label Mapping**: The sentiment labels were mapped to integers: `0` for negative, `1` for neutral, and `2` for positive.

#### Training Hyperparameters
- **Epochs**: 3
- **Batch Size**: 16
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW
- **Warmup Steps**: 10% of training steps
- **Weight Decay**: 0.01
  
## Evaluation

### Testing Data
The model was evaluated on a subset of the Turkish ABSA dataset, which includes 57,905 instances, focusing on brand-related sentiment analysis. The evaluation was conducted over three epochs, with accuracy and F1-scores being tracked to assess performance improvements during training.

### Metrics

#### Epoch 1:
- **Average Training Loss**: 0.3848
- **Evaluation Accuracy**: 0.9013
- **Evaluation F1-score**: 0.9012
- **New Best Model Saved**

#### Epoch 2:
- **Average Training Loss**: 0.2030
- **Evaluation Accuracy**: 0.9264
- **Evaluation F1-score**: 0.9262
- **New Best Model Saved**

#### Epoch 3:
- **Average Training Loss**: 0.1183
- **Evaluation Accuracy**: 0.9376
- **Evaluation F1-score**: 0.9372
- **New Best Model Saved**

### Final Classification Report:
- **Accuracy**: 0.9376
- **Macro F1-score**: 0.9314
- **Weighted F1-score**: 0.9372
