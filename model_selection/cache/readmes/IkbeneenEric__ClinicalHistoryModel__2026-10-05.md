---
license: mit
language:
- en
pipeline_tag: text-classification
---
## How to use model with torch:
```model_name = "bert-base-uncased"

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the model
model = AutoModel.from_pretrained(model_name)
```

## How to use it on example text:
```
# Example input
text = "Hello, how are you?"

# Tokenize the input
inputs = tokenizer(text, return_tensors="pt")

# Forward pass through the model
outputs = model(**inputs)
```