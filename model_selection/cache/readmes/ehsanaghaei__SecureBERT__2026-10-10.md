---
license: bigscience-openrail-m
widget:
- text: >-
    Native API functions such as <mask> may be directly invoked via system calls
    (syscalls). However, these features are also commonly exposed to user-mode
    applications through interfaces and libraries.
  example_title: Native API functions
- text: >-
    One way to explicitly assign the PPID of a new process is through the <mask>
    API call, which includes a parameter for defining the PPID.
  example_title: Assigning the PPID of a new process
- text: >-
    Enable Safe DLL Search Mode to ensure that system DLLs in more restricted
    directories (e.g., %<mask>%) are prioritized over DLLs in less secure
    locations such as a user’s home directory.
  example_title: Enable Safe DLL Search Mode
- text: >-
    GuLoader is a file downloader that has been active since at least December
    2019. It has been used to distribute a variety of <mask>, including NETWIRE,
    Agent Tesla, NanoCore, and FormBook.
  example_title: GuLoader is a file downloader
language:
- en
tags:
- cybersecurity
- cyber threat intelligence
base_model:
- FacebookAI/roberta-base
new_version: cisco-ai/SecureBERT2.0-base
pipeline_tag: fill-mask
---

# SecureBERT: A Domain-Specific Language Model for Cybersecurity  

**SecureBERT** is a RoBERTa-based, domain-specific language model trained on a large cybersecurity-focused corpus. It is designed to represent and understand cybersecurity text more effectively than general-purpose models.  

[SecureBERT](https://link.springer.com/chapter/10.1007/978-3-031-25538-0_3) was trained on extensive in-domain data crawled from diverse online resources. It has demonstrated strong performance in a range of cybersecurity NLP tasks.  
👉 See the [presentation on YouTube](https://www.youtube.com/watch?v=G8WzvThGG8c&t=8s).  
👉 Explore details on the [GitHub repository](https://github.com/ehsanaghaei/SecureBERT/blob/main/README.md).  

![image](https://user-images.githubusercontent.com/46252665/195998237-9bbed621-8002-4287-ac0d-19c4f603d919.png)

---

## Applications  
SecureBERT can be used as a base model for downstream NLP tasks in cybersecurity, including:  
- Text classification  
- Named Entity Recognition (NER)  
- Sequence-to-sequence tasks  
- Question answering  

### Key Results
- Outperforms baseline models such as **RoBERTa (base/large)**, **SciBERT**, and **SecBERT** in masked language modeling tasks within the cybersecurity domain.  
- Maintains strong performance in **general English language understanding**, ensuring broad usability beyond domain-specific tasks.  

---

## Using SecureBERT  

The model is available on [Hugging Face](https://huggingface.co/ehsanaghaei/SecureBERT).  

### Load the Model
```python
from transformers import RobertaTokenizer, RobertaModel
import torch

tokenizer = RobertaTokenizer.from_pretrained("ehsanaghaei/SecureBERT")
model = RobertaModel.from_pretrained("ehsanaghaei/SecureBERT")

inputs = tokenizer("This is SecureBERT!", return_tensors="pt")
outputs = model(**inputs)

last_hidden_states = outputs.last_hidden_state


Masked Language Modeling Example

SecureBERT is trained with Masked Language Modeling (MLM). Use the following example to predict masked tokens:

#!pip install transformers torch tokenizers

import torch
import transformers
from transformers import RobertaTokenizerFast

tokenizer = RobertaTokenizerFast.from_pretrained("ehsanaghaei/SecureBERT")
model = transformers.RobertaForMaskedLM.from_pretrained("ehsanaghaei/SecureBERT")

def predict_mask(sent, tokenizer, model, topk=10, print_results=True):
    token_ids = tokenizer.encode(sent, return_tensors='pt')
    masked_pos = (token_ids.squeeze() == tokenizer.mask_token_id).nonzero().tolist()
    words = []

    with torch.no_grad():
        output = model(token_ids)

    for pos in masked_pos:
        logits = output.logits[0, pos]
        top_tokens = torch.topk(logits, k=topk).indices
        predictions = [tokenizer.decode(i).strip().replace(" ", "") for i in top_tokens]
        words.append(predictions)
        if print_results:
            print(f"Mask Predictions: {predictions}")

    return words
```
# Limitations & Risks

* Domain-Specific Bias: SecureBERT is trained primarily on cybersecurity-related text. It may underperform on tasks outside this domain compared to general-purpose models.

* Data Quality: The training data was collected from online sources. As such, it may contain inaccuracies, outdated terminology, or biased representations of cybersecurity threats and behaviors.

* Potential Misuse: While the model is intended for defensive cybersecurity research, it could potentially be misused to generate malicious text (e.g., obfuscating malware descriptions or aiding adversarial tactics).

* Not a Substitute for Expertise: Predictions made by the model should not be considered authoritative. Cybersecurity professionals must validate results before applying them in critical systems or operational contexts.

* Evolving Threat Landscape: Cyber threats evolve rapidly, and the model may become outdated without continuous retraining on fresh data.

* Users should apply SecureBERT responsibly, keeping in mind its limitations and the need for human oversight in all security-critical applications.

# Reference
```
@inproceedings{aghaei2023securebert, 
title={SecureBERT: A Domain-Specific Language Model for Cybersecurity}, 
author={Aghaei, Ehsan and Niu, Xi and Shadid, Waseem and Al-Shaer, Ehab}, 
booktitle={Security and Privacy in Communication Networks: 
18th EAI International Conference, SecureComm 2022, Virtual Event, October 2022, Proceedings}, 
pages={39--56}, 
year={2023}, 
organization={Springer} 
}
```