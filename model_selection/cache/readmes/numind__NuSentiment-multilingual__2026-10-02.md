---
license: mit
language:
- en
- ar
- fr
- de
- pt
- it
- es
- zh
- ja
- ko
pipeline_tag: feature-extraction
tags:
- sentiment-analysis
- text-classification
- generic
- sentiment-classification
- multilingual
---

## Model

Base version of e5-multilingual finetunned on an annotated subset of mC4 (multilingual C4). This model provide generic embedding for sentiment analysis. Embeddings can be used out of the box or fine tune on specific datasets. 

Blog post: https://www.numind.ai/blog/creating-task-specific-foundation-models-with-gpt-4

## Usage

Below is an example to encode text and get embedding.

```python
import torch
from transformers import AutoTokenizer, AutoModel


model = AutoModel.from_pretrained("Numind/e5-multilingual-sentiment_analysis")
tokenizer = AutoTokenizer.from_pretrained("Numind/e5-multilingual-sentiment_analysis")
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)

size = 256
text = "This movie is amazing"

encoding = tokenizer(
    text,
    truncation=True, 
    padding='max_length', 
    max_length= size,
)

emb = model(
      torch.reshape(torch.tensor(encoding.input_ids),(1,len(encoding.input_ids))).to(device),output_hidden_states=True
).hidden_states[-1].cpu().detach()

embText = torch.mean(emb,axis = 1)
```