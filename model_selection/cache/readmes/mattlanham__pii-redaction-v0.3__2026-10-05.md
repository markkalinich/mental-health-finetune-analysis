---
base_model: unsloth/phi-3-mini-4k-instruct-bnb-4bit
language:
- en
license: apache-2.0
tags:
- text-generation-inference
- transformers
- unsloth
- mistral
- trl
---

# Finetuned phi-3 mini model for data extraction / pii redaction

Trained using synthetic data, this model will provide a JSON output containing:

With user input:
`My order hasn't arrived, it's order number 123456 and my email is johnsmith@gmail.com, please can you provide an update! Thanks John.`

The model will respond with:

```
{
  "redacted_message": "My order hasn't arrived, it's order number {order_number} and my email is {email}, please can you provide an update! Thanks {name}.",
  "data": {
    "order_number": "123456",
    "email": "johnsmith@gmail.com",
    "name": "John",

  }
}
```

- **Developed by:** mattlanham
- **License:** apache-2.0
- **Finetuned from model :** unsloth/phi-3-mini-4k-instruct-bnb-4bit

This mistral model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)
