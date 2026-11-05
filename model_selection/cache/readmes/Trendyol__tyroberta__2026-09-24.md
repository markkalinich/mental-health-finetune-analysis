---
license: apache-2.0
language:
- tr
library_name: transformers
pipeline_tag: feature-extraction
---

# TyRoberta Model

This repository provides a pretrained Roberta model for Turkish by Trendyol, named TyRoberta. The model is useful for various natural language understanding tasks, such as text classification, named entity recognition, and more.


## How to use

```python
from transformers import AutoTokenizer, RobertaModel

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Trendyol/tyroberta")
model = RobertaModel.from_pretrained("Trendyol/tyroberta")

# Define a sample text
text = "Filenin Sultanları ilk maçını 29 Temmuz'da Hollanda'ya karşı oynayacak."

# Tokenize and encode the input text
encoded_input = tokenizer(text, return_tensors='pt')

# Get the model's output
output = model(**encoded_input)

print(output)

```