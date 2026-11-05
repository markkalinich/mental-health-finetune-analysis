---
library_name: transformers
tags:
- sentiment 
- classifier
license: mit
datasets:
- financial_phrasebank
language:
- en
---
### Model Description

<!-- Provide a longer summary of what this model is. -->

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** Mit Patel
- **Model type:** Text generation/ classifier 
- **Language(s) (NLP):** English
- **Finetuned from model :** Phi-2



## Training Details
https://github.com/mit1280/fined-tuning/blob/main/phi_2_classification_fine_tune.ipynb



### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- training_steps: 10000

### Inference

```python
!pip install -q transformers==4.37.2  accelerate==0.27.0

import re
from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteria
import torch

tokenizer = AutoTokenizer.from_pretrained("Mit1208/phi-2-classification-sentiment-merged")
model = AutoModelForCausalLM.from_pretrained("Mit1208/phi-2-classification-sentiment-merged", device_map="auto", trust_remote_code=True).eval()

class EosListStoppingCriteria(StoppingCriteria):
    def __init__(self, eos_sequence = tokenizer.encode("<|im_end|>")):
        self.eos_sequence = eos_sequence

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        last_ids = input_ids[:,-len(self.eos_sequence):].tolist()
        return self.eos_sequence in last_ids

inf_conv = [{'from': 'human',
  'value': "Text: In sales volume , Coca-Cola 's market share has decreased by 2.2 % to 24.2 % ."},
 {'from': 'phi', 'value': "I've read this text."},
 {'from': 'human',
  'value': 'Please determine the sentiment of the given text and choose from the options: Positive, Negative, Neutral, or Cannot be determined.'}]
# need to load because model doesn't has classifer head.

id2label = {0: 'negative', 1: 'neutral', 2: 'positive'}

inference_text = tokenizer.apply_chat_template(inf_conv, tokenize=False) + '<|im_start|>phi:\n'
inputs = tokenizer(inference_text, return_tensors="pt", return_attention_mask=False).to('cuda')
outputs = model.generate(inputs["input_ids"], max_new_tokens=1024, pad_token_id= tokenizer.eos_token_id,
            stopping_criteria = [EosListStoppingCriteria()])

text = tokenizer.batch_decode(outputs)[0]
answer = text.split("<|im_start|>phi:")[-1].replace("<|im_end|>", "").replace(".", "")

sentiment_label = re.search(r'(\d)', answer)
sentiment_score = int(sentiment_label.group(1))

if sentiment_score:
    print(id2label.get(sentiment_score, "none"))
else:
    print("none")
```

### Framework versions

- PEFT 0.8.2
- Transformers 4.37.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1