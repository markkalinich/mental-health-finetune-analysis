---
tags:
- emotion-recognition
- affective-computing
- text-classification
- huggingface
license: mit

---

# MiniLM-L12-Affect: Emotion Classification Model

This model is a fine-tuned version of **MiniLM-L12-H384-uncased** for **emotion classification** in text. It is capable of predicting six basic emotions: **Joy, Anger, Fear, Sadness, Surprise, Disgust**.


This is an early test version of the model and not a final, polished release. It is still a work in progress, and future versions may include improvements and refinements.
## Description

This model has been fine-tuned on a custom emotion dataset. It takes a text input and predicts the intensity of each of the six emotions listed above. The model uses the **MiniLM** architecture, which is lightweight and fast, offering good performance for NLP tasks with fewer parameters.

## Predictable Emotions

The model can predict the following emotions in text:

- **Joy**
- **Anger**
- **Fear**
- **Sadness**
- **Surprise**
- **Disgust**

## Usage

Here is an example of how to run inference with the model:

```python
import torch
from torch import nn
from transformers import AutoTokenizer, AutoModel
import safetensors.torch
import pandas as pd

# Custom model class for emotion classification using MiniLM
class MiniLMEmotionClassifier(nn.Module):
    def __init__(self, model_name):
        super(MiniLMEmotionClassifier, self).__init__()
        self.base_model = AutoModel.from_pretrained(model_name, ignore_mismatched_sizes=True)  # Load the MiniLM model
        self.dropout = nn.Dropout(0.1)  # Dropout for regularization
        self.fc = nn.Linear(384, 6)  # Output layer for 6 emotion categories

    def forward(self, input_ids, attention_mask=None, labels=None):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.last_hidden_state[:, 0, :]  # Extract [CLS] token representation
        pooled_output = self.dropout(pooled_output)
        logits = self.fc(pooled_output)  # Compute predictions

        loss = None
        if labels is not None:
            # Use MSE loss for regression-style emotion prediction
            loss_fct = nn.MSELoss()
            loss = loss_fct(logits, labels.view_as(logits))

        return {"loss": loss, "logits": logits} if loss is not None else {"logits": logits}

# Path to the safetensors model file
model_path = 'MiniLM-L12-Affect/model.safetensors'

# Load model weights from the safetensors file
with open(model_path, 'rb') as f:
    model_data = f.read()
model_state_dict = safetensors.torch.load(model_data)

# Initialize the MiniLM model
model_name = "./MiniLM-L12-Affect"
model = MiniLMEmotionClassifier(model_name)

# Load pre-trained weights into the model
model.load_state_dict(model_state_dict, strict = False)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("./MiniLM-L12-Affect", ignore_mismatched_sizes=True)

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def predict_emotions(text):
    """Tokenizes input text and predicts emotion scores."""
    inputs = tokenizer(
        text,
        padding="max_length",
        truncation=True,
        max_length=128,
        return_tensors="pt"
    )
    # Remove 'token_type_ids' if present
    inputs.pop('token_type_ids', None)
    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    predictions = outputs["logits"].cpu().numpy()[0]
    return predictions

# Example inference
test_text = "This is horribly amazing ! you're a genius"
emotions = predict_emotions(test_text)

# Emotion categories
categories = ["Joy", "Anger", "Fear", "Sadness", "Surprise", "Disgust"]

# Display the results
print(f"Text: {test_text}")
emotion_df = pd.DataFrame(emotions.reshape(1, -1), columns=categories)
print(emotion_df)
```
### Result

**Text:** OMG This is horribly amazing ! you're a genius
|     | Joy     | Anger   | Fear    | Sadness  | Surprise | Disgust  |
|-----|---------|--------|---------|---------|----------|---------|
|  0  | 0.844805 | 0.02971 | 0.008245 | -0.007872 | 0.668609  | 0.001267 |



## Deployment

The model is ready to be deployed in applications that require emotion detection, such as chatbots, recommendation systems, or other services needing emotion analysis in text.

## License

The model is licensed under the **MIT License**. You are free to use, modify, and integrate it into your own projects.

## Limitations

- This model was trained on a specific custom dataset of 50K pairs and might not perform optimally on other domains or languages.
- The model currently only handles English text.

---

### Credits

- Base model: **MiniLM-L12-H384-uncased** (Microsoft)
- Dataset: **Custom Dataset**
- Developed by: **Pharci**
