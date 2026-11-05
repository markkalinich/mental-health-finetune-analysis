---
license: apache-2.0
datasets:
- ifmain/text-moderation-410K
language:
- en
metrics:
- accuracy
pipeline_tag: text-classification
---
# ModerationBERT-ML-En

**ModerationBERT-ML-En** is a moderation model based on `bert-base-multilingual-cased`. This model is designed to perform text moderation tasks, specifically categorizing text into 18 different categories. It currently works only with English text.


## Dataset

The model was trained and fine-tuned using the [text-moderation-410K](https://huggingface.co/datasets/ifmain/text-moderation-410K) dataset. This dataset contains a wide variety of text samples labeled with different moderation categories.

## Model Description

ModerationBERT-ML-En uses the BERT architecture to classify text into the following categories:
- harassment
- harassment_threatening
- hate
- hate_threatening
- self_harm
- self_harm_instructions
- self_harm_intent
- sexual
- sexual_minors
- violence
- violence_graphic
- self-harm
- sexual/minors
- hate/threatening
- violence/graphic
- self-harm/intent
- self-harm/instructions
- harassment/threatening

## Training and Fine-Tuning

The model was trained using a 95% subset of the dataset for training and a 5% subset for evaluation. The training was performed in two stages:

1. **Initial Training**: The classifier layer was trained with frozen BERT layers.
2. **Fine-Tuning**: The top two layers of the BERT model were unfrozen and the entire model was fine-tuned.

## Installation

To use ModerationBERT-ML-En, you will need to install the `transformers` library from Hugging Face and `torch`.

```bash
pip install transformers torch
```

## Usage

Here is an example of how to use ModerationBERT-ML-En to predict the moderation categories for a given text:

```python
import json
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load the tokenizer and model
model_name = "ifmain/ModerationBERT-En-02"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=18)

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

def predict(text, model, tokenizer):
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        return_token_type_ids=False,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt'
    )
    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)
    model.eval()
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
    predictions = torch.sigmoid(outputs.logits)  # Convert logits to probabilities
    return predictions

# Example usage
new_text = "Fuck off stuped trash"
predictions = predict(new_text, model, tokenizer)

# Define the categories
categories = ['harassment', 'harassment_threatening', 'hate', 'hate_threatening', 
              'self_harm', 'self_harm_instructions', 'self_harm_intent', 'sexual', 
              'sexual_minors', 'violence', 'violence_graphic', 'self-harm', 
              'sexual/minors', 'hate/threatening', 'violence/graphic', 
              'self-harm/intent', 'self-harm/instructions', 'harassment/threatening']

# Convert predictions to a dictionary
category_scores = {categories[i]: predictions[0][i].item() for i in range(len(categories))}

output = {
    "text": new_text,
    "category_scores": category_scores
}

# Print the result as a JSON with indentation
print(json.dumps(output, indent=4, ensure_ascii=False))
```

Output:

```json
{
    "text": "Fuck off stuped trash",
    "category_scores": {
        "harassment": 0.9272650480270386,
        "harassment_threatening": 0.0013139015063643456,
        "hate": 0.011709265410900116,
        "hate_threatening": 1.1083522622357123e-05,
        "self_harm": 0.00039102151640690863,
        "self_harm_instructions": 0.0002464024000801146,
        "self_harm_intent": 0.00031603744719177485,
        "sexual": 0.020730027928948402,
        "sexual_minors": 0.00018848323088604957,
        "violence": 0.008375612087547779,
        "violence_graphic": 2.8763401132891886e-05,
        "self-harm": 0.00043840022408403456,
        "sexual/minors": 0.00018241720681544393,
        "hate/threatening": 1.1130881830467843e-05,
        "violence/graphic": 2.7211604901822284e-05,
        "self-harm/intent": 0.00026327319210395217,
        "self-harm/instructions": 0.00023905260604806244,
        "harassment/threatening": 0.0012845908058807254
    }
}
```

## Notes

- This model is currently configured to work only with English text.
- Future updates may include support for additional languages.