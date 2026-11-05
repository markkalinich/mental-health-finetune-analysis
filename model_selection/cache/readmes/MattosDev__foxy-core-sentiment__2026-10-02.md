---
language:
- pt
license: apache-2.0
tags:
- foxy-core
- nlp
- chatbot
- portuguese
- sentiment
pipeline_tag: text-classification
---

# 🦊 Foxy-Core — SENTIMENT v2.0.0

Motor NLP central para chatbots multi-vertical.

## Uso

```python
from transformers import pipeline

pipe = pipeline(
    "text-classification",
    model="MattosDev/foxy-core-sentiment"
)

result = pipe("quero fazer um pedido")
print(result)
```
Verticais suportadas

🏥 Farmácias

🍔 Fast Foods

💻 Tecnologia

Base Model

BERTimbau (neuralmind/bert-base-portuguese-cased)
