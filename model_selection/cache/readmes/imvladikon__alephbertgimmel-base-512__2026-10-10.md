---
language:
- he 
tags:
- language model
---

## AlephBertGimmel
Modern Hebrew pretrained BERT model with a 128K token vocabulary.


[Checkpoint](https://github.com/Dicta-Israel-Center-for-Text-Analysis/alephbertgimmel/tree/main/alephbertgimmel-base/ckpt_73780--Max512Seq) of the alephbertgimmel-base-512 from [alephbertgimmel](https://github.com/Dicta-Israel-Center-for-Text-Analysis/alephbertgimmel)


```python
from transformers import AutoTokenizer, AutoModelForMaskedLM


import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer

model = AutoModelForMaskedLM.from_pretrained("imvladikon/alephbertgimmel-base-512")
tokenizer = AutoTokenizer.from_pretrained("imvladikon/alephbertgimmel-base-512")

text = "{} היא מטרופולין המהווה את מרכז הכלכלה"

input = tokenizer.encode(text.format("[MASK]"), return_tensors="pt")
mask_token_index = torch.where(input == tokenizer.mask_token_id)[1]

token_logits = model(input).logits
mask_token_logits = token_logits[0, mask_token_index, :]
top_5_tokens = torch.topk(mask_token_logits, 5, dim=1).indices[0].tolist()

for token in top_5_tokens:
    print(text.format(tokenizer.decode([token])))

# העיר היא מטרופולין המהווה את מרכז הכלכלה
# ירושלים היא מטרופולין המהווה את מרכז הכלכלה
# חיפה היא מטרופולין המהווה את מרכז הכלכלה
# לונדון היא מטרופולין המהווה את מרכז הכלכלה
# אילת היא מטרופולין המהווה את מרכז הכלכלה
```

```python 
def ppl_naive(text, model, tokenizer):
    input = tokenizer.encode(text, return_tensors="pt")
    loss = model(input, labels=input)[0]
    return torch.exp(loss).item()

text = """{} היא עיר הבירה של מדינת ישראל, והעיר הגדולה ביותר בישראל בגודל האוכלוסייה"""

for word in ["חיפה", "ירושלים", "תל אביב"]:
  print(ppl_naive(text.format(word), model, tokenizer))

# 10.181422233581543
# 9.743313789367676
# 10.171016693115234
```

When using AlephBertGimmel, please reference:

```bibtex

@misc{gueta2022large,
      title={Large Pre-Trained Models with Extra-Large Vocabularies: A Contrastive Analysis of Hebrew BERT Models and a New One to Outperform Them All}, 
      author={Eylon Gueta and Avi Shmidman and Shaltiel Shmidman and Cheyn Shmuel Shmidman and Joshua Guedalia and Moshe Koppel and Dan Bareket and Amit Seker and Reut Tsarfaty},
      year={2022},
      eprint={2211.15199},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```