---
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- finance
- Turkish
license: mit
datasets:
- SkyWalkertT1/stock_market_dataset
language:
- tr
metrics:
- accuracy
base_model:
- google-bert/bert-base-uncased
---

# Turkish Stock Market Sentiment Classification Model

This model is a **BERT-based classification model** designed to classify the sentiment of Turkish stock market comments into **positive, neutral, and negative** categories. It is built on top of the `dbmdz/bert-base-turkish-uncased` model.

---

## Model Performance

- **Accuracy on test dataset:** 97%
- Optimized for analyzing Turkish stock market comments.

---

## Features

- Detects positive, neutral, and negative sentiments.
- Easy to use with Hugging Face `transformers` library.
- Supports GPU for faster inference.

---

## Installation

Install the required Python libraries:

```bash
pip install torch transformers


from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("SkyWalkertT1/turkish_bert_stock_market_classification_sentiment")
model = AutoModelForSequenceClassification.from_pretrained("SkyWalkertT1/turkish_bert_stock_market_classification_sentiment")

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Label mapping
label_mapping = {0: 'negative', 1: 'neutral', 2: 'positive'}

def predict_sentiment(comment):
    """
    Predicts the sentiment of a Turkish stock market comment.

    Args:
        comment (str): Turkish stock market comment.

    Returns:
        str: 'positive', 'neutral', or 'negative'
    """

    # Tokenize the comment for BERT
    encoded_dict = tokenizer.encode_plus(
        comment,
        add_special_tokens=True,
        max_length=128,        # Maximum token length
        padding='max_length',  # Padding to max length
        return_attention_mask=True,
        return_tensors='pt',
        truncation=True
    )

    input_ids = encoded_dict['input_ids'].to(device)
    attention_mask = encoded_dict['attention_mask'].to(device)

    # Set model to evaluation mode
    model.eval()

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)

    # Get predicted class
    logits = outputs.logits
    predicted_label_index = torch.argmax(logits, dim=1).item()

    return label_mapping[predicted_label_index]

# Example usage
test_comment = "Hisseler bugün yükselişte."
predicted_sentiment = predict_sentiment(test_comment)
print(f"The sentiment of the comment '{test_comment}' is: {predicted_sentiment}")


Function Explanation

tokenizer.encode_plus: Converts the comment into tokens suitable for BERT and creates attention masks.

model.eval(): Sets the model in evaluation mode (disables dropout and training-specific layers).

torch.argmax: Selects the class with the highest predicted probability.

label_mapping: Maps the predicted class index to a readable label.

Example Output
The sentiment of the comment 'Hisseler bugün yükselişte.' is: positive


---

```