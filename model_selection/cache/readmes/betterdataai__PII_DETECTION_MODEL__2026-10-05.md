---
library_name: transformers
pipeline_tag: text-generation
---

# Model Card

This model is used for PII detection. It covers 29 classes across 7 languages (English , Spanish, Swedish, German, Italian, Dutch, French) 


## Model Details
The model is built on top of the decoder transformer model (Qwen2-0.5B). We used publicly available datasets with a permissible license as well as synthetic data to train the model.  

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Betterdata.ai
- **Model type:** Decoder Transformer
- **License:** apache-2.0
- **Finetuned from model :** Qwen2-0.5B

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

With the advent of chatGPT , professionals and organizations use public chat interfaces for various applications. This often leads to leakage of PII data which causes privacy issues as users enter names , dates or even API keys etc to give the model better context. With the PII class tags, these confidential information can be masked out as class tags which enable the end models to understand context without data leaving the server. Even developers or teams building applications with the help of third party API's can use these models for better privacy. The image below illustrates this:


![Use Case](pii_image.png)

The PII model shouldn't add too much latency and be able to take in long documents, therefore we used the Qwen 0.5B as the base model. Another consideration for the model size was that we felt a model for privacy should be easy to run even on CPUs. We do have larger models in house with better performance. We have coverage for south east asian langauges as well as giving the user the ability to define custom user classes as part of our plans. 


We will constantly be improving this model so always pull the latest version of the model. 


### Out-of-Scope Use

1. We currently are trying to replace the PII text with the respective class tags. In the future we plan to replace the data with synthetic class values. 


## Bias, Risks, and Limitations

1. Model may not be 100% accurate always but we are working on it. 
2. In our 'vibe test' where we fed the model with out of distribution data , the model does very well on classes like names , emails , phone numbers etc. We find that it can do better on classes like API_KEYS , credit card cvv numbers , bank account numbers. We are creating more data for these classes to futher improve performance. You can expect improvement in the next iteration.  

## How to Get Started with the Model

Use the code below to get started with the model.

```
from transformers import AutoModelForCausalLM , AutoTokenizer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForCausalLM.from_pretrained("betterdataai/PII_DETECTION_MODEL").to(device)
tokenizer = AutoTokenizer.from_pretrained("betterdataai/PII_DETECTION_MODEL")

classes_list = ['<pin>','<api_key>','<bank_routing_number>','<bban>','<company>','<credit_card_number>','<credit_card_security_code>','<customer_id>','<date>','<date_of_birth>','<date_time>','<driver_license_number>','<email>','<employee_id>','<first_name>','<iban>','<ipv4>','<ipv6>','<last_name>','<local_latlng>','<name>','<passport_number>','<password>','<phone_number>','<social_security_number>','<street_address>','<swift_bic_code>','<time>','<user_name>']


prompt = """You are an AI assistant who is responisble for identifying Personal Identifiable information (PII). You will be given a passage of text and you have to \
identify the PII data present in the passage. You should only identify the data based on the classes provided and not make up any class on your own.

```PII Classes```
{classes}

The given text is:
{text}

The PII data are:
"""



user_input = "Write an email to Julia indicating I won't be coming to office on the 29th of June"
new_prompt = prompt.format(classes="\n".join(classes_list) , text=user_input)
tokenized_input = tokenizer(new_prompt , return_tensors="pt").to(device)

output = model.generate(**tokenized_input , max_new_tokens=6000)
pii_classes = tokenizer.decode(output[0] , skip_special_tokens=True).split("The PII data are:\n")[1]

print(pii_classes)

##output
"""
<name> : ['Julia']
<date> : ['the 29th of June']
"""
```

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data
1. We developed an in house testset that we evaluate the model on. The test set was manually annotated to ensure high quality of the test set. The test set mainly comprises of financial documents , contracts etc across all the 7 languages, covering all the classes.


#### Metrics

1. We used precision , recall and F1 score to evaluate the models output with the ground truth. 

We consider precision and recall to be:

- Precision: The ratio of correctly identified PII instances to the total identified instances.
- Recall: The ratio of correctly identified PII instances to the total actual instances in the dataset.

## Model Card Authors

Srinivasan

## Model Card Contact
For feedback/suggestions and any collaborations reach us at:

srini@betterdata.ai
contact@betterdata.ai
