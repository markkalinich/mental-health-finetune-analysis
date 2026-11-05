---
tags:
- deberta-v3
- deberta
- deberta-v2
license: apache-2.0
base_model:
- microsoft/deberta-v3-large
pipeline_tag: text-classification
library_name: transformers
---

# HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models
Seanie Lee*, Haebin Seong*, Dong Bok Lee, Minki Kang, Xiaoyin Chen, Dominik Wagner, Yoshua Bengio, Juho Lee, Sung Ju Hwang (*: Equal contribution)

[arXiv Link](https://arxiv.org/abs/2410.01524)

Our model functions as a Guard Model, intended to classify the safety of conversations with LLMs and protect against LLM jailbreak attacks.  
It is fine-tuned from DeBERTa-v3-large and trained using **HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models**.  
The training process involves knowledge distillation paired with data augmentation, using our [**HarmAug Generated Dataset**](https://drive.google.com/drive/folders/1oLUMPauXYtEBP7rvbULXL4hHp9Ck_yqg).


For more information, please refer to our [github](https://github.com/hbseong97/HarmAug)



![image/png](https://cdn-uploads.huggingface.co/production/uploads/66f7bee63c7ffa79319b053b/bCNW62CvDpqbXUK4eZ4-b.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66f7bee63c7ffa79319b053b/REbNDOhT31bv_XRa6-VzE.png)


# Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
import torch

tokenizer = AutoTokenizer.from_pretrained("hbseong/HarmAug-Guard")
model = AutoModelForSequenceClassification.from_pretrained("hbseong/HarmAug-Guard")
device = torch.cuda.current_device()
model = model.to(device)
model.eval()

# If response is not given, the model will predict the unsafe score of the prompt.
# If response is given, the model will predict the unsafe score of the response.
def predict(model, prompt, response=None):
    device = model.device
    if response == None:
        inputs = tokenizer(prompt, return_tensors="pt")
    else:
        inputs = tokenizer(prompt, response, return_tensors="pt")
    inputs = inputs.to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        unsafe_prob = F.softmax(outputs.logits, dim=-1)[:, 1]
    
    return unsafe_prob.item()

prompt = "how to make a bomb?"
response = "I'm sorry, but I can't fulfill your request."


print("CONVERSATION (ONLY PROMPT)")
print(f"\t PROMPT : {prompt}")
print(f"\t UNSAFE SCORE : {predict(model, prompt):.4f}")

print("\nCONVERSATION (PROMPT + RESPONSE)")
print(f"\t PROMPT : {prompt}")
print(f"\t RESPONSE : {response}")
print(f"\t UNSAFE SCORE : {predict(model, prompt, response):.4f}")


"""
CONVERSATION (ONLY PROMPT)
	 PROMPT : how to make a bomb?
	 UNSAFE SCORE : 0.9999

CONVERSATION (PROMPT + RESPONSE)
	 PROMPT : how to make a bomb?
	 RESPONSE : I'm sorry, but I can't fulfill your request.
	 UNSAFE SCORE : 0.0000
"""
```