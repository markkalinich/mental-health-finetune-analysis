---
license: mit
datasets:
- tsac
language:
- ar
---

This is a converted version of [Instadeep's](https://huggingface.co/InstaDeepAI) [TunBERT](https://github.com/instadeepai/tunbert/) from nemo to safetensors.

# how to load the model 
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("tunis-ai/TunBERT")
model = AutoModelForSequenceClassification.from_pretrained("tunis-ai/TunBERT",trust_remote_code=True)
```


# how to use the model 
```python
text = "[insert text here]"
inputs = tokenizer(text,return_tensors='pt')
output = model.process(**inputs) # -> List["positive" or "negative"]
```
or you can use the normal forward method (currently compatible with the Trainer class)
```python
text = "[insert text here]"
inputs = tokenizer(text,return_tensors='pt')
output = model(**inputs)
```


or you can use the pipeline : 

⚠️currently broken try an older version of transformers until i raise this, in the mean time use the `model.process` method mentioned above

```python
from transformers import pipeline

pipe = pipeline(model="tunis-ai/TunBERT",tokenizer = "tunis-ai/TunBERT",trust_remote_code=True)
pipe("text")
```

