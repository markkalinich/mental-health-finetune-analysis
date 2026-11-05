---
license: apache-2.0
language:
- en
base_model:
- google-bert/bert-large-uncased
metrics:
- accuracy
- f1
- precision
pipeline_tag: text-classification
tags:
- privacy
---

<a href="https://www.buymeacoffee.com/privacymoderation"><img src="https://img.buymeacoffee.com/button-api/?text=Support / Buy me a coffee&emoji=☕&slug=privacymoderation&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>

# Privacy Moderation Large

This is a BERT Large model fine-tuned to detect privacy violations in text, such as sharing of personally identifiable information (PII) or sensitive data. It is trained on a dataset of labeled examples of privacy violations and non-violations.


## Performance

This large model achieves the following performance metrics on a held-out test set:
| Metric     | Value   |
|------------|---------|
| Accuracy   | `0.9584`  |
| F1 Score   | `0.9569`  |
| Precision  | `0.9621`  |
| Recall     | `0.9517`  |

These metrics indicate that the model is effective at identifying privacy violations while minimizing false positives.

## Limitations

- The model was trained on a dataset of nearly 1 million examples in varying topics and styles, but may not generalize to all contexts
- It limited to English text
- This current iteration used a dataset where each example is between 20 and 120 words in length, so performance on much longer texts is untested (e.g. full documents may require chunking)
- The model may not detect all types of privacy violations, especially if they are subtle or context-dependent

## How to Use

You can use this model for text classification tasks related to privacy moderation. Here's an example of how to use it with the Hugging Face Transformers library:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import numpy as np
import pandas as pd

# Load the model and tokenizer
model_name = "PL-RnD/privacy-moderation-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
# Example text
texts = [
    "Here is my credit card number: 1234-5678-9012-3456",
    "This is a regular message without sensitive information.",
    "For homeowners insurance, select deductibles from $500 to $2,500. Higher deductibles lower premiums.",
    "Solidarity: My enrollment includes my kid's braces at $4,000 total—family strained. Push for orthodontic expansions. Email blast to reps starting now.",
]
# Tokenize the input
inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
# Get model predictions
with torch.no_grad():
    outputs = model(**inputs)

logits = outputs.logits
predictions = torch.argmax(logits, dim=-1)
# Convert predictions to labels
labels = ["non-violation", "violation"]
predicted_labels = [labels[pred] for pred in predictions.numpy()]
# Display results
df = pd.DataFrame({"text": texts, "label": predicted_labels})
print(df)
```

This will output a DataFrame with the original texts and their predicted labels (either "violation" or "non-violation"). Example output:

```
                                                text          label
0  Here is my credit card number: 1234-5678-9012-...      violation
1  This is a regular message without sensitive in...  non-violation
2  For homeowners insurance, select deductibles f...  non-violation
3  Solidarity: My enrollment includes my kid's br...      violation
```

## Intended Use
This model is intended to flag privacy concerns that a privacy conscious person would expect to keep private, such as: addresses, phone numbers, e-mails, passwords, health details, relationship drama, financial numbers, political opinions, or sexual preferences.

The motivating use-case for this model is to reside client-side (or in a trusted/internal environment) to review user-generated text content before it is sent to a server or third-party service, in order to prevent accidental sharing of sensitive information. For example:
- Filter and act as an A:B router for public vs private LLMS (i.e. like using this with Pipelines in Open-WebUI). If the text is flagged as a privacy violation, it can be routed to a local/private LLM instance instead of a public one.
- Block or warn users when they attempt to share sensitive information in chat applications
- Load the model in a browser using libraries like ONNX.js or TensorFlow.js to perform client-side moderation

---

> Ultimately, arguing that you don't care about the right to privacy because you have nothing to hide is no different than saying you don't care about free speech because you have nothing to say. - Edward Snowden
