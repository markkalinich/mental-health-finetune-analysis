---
license: mit
language:
- en
pipeline_tag: text-generation
tags:
- LLM
- token classification
- nlp
- safetensor
- PyTorch
base_model: microsoft/Phi-3-mini-4k-instruct
library_name: transformers
widget:
- text: My name is Sylvain and I live in Paris
  example_title: Parisian
- text: My name is Sarah and I live in London
  example_title: Londoner
---


# PII Detection Model - Phi3 Mini Fine-Tuned

This repository contains a fine-tuned version of the [Phi3 Mini](https://huggingface.co/ab-ai/PII-Model-Phi3-Mini) model for detecting personally identifiable information (PII). The model has been specifically trained to recognize various PII entities in text, making it a powerful tool for tasks such as data redaction, privacy protection, and compliance with data protection regulations.

## Model Overview

### Model Architecture

- **Base Model**: Phi3 Mini
- **Fine-Tuned For**: PII detection
- **Framework**: [Hugging Face Transformers](https://huggingface.co/transformers/)

### Detected PII Entities

The model is capable of detecting the following PII entities:

- **Personal Information**:
  - `firstname`
  - `middlename`
  - `lastname`
  - `sex`
  - `dob` (Date of Birth)
  - `age`
  - `gender`
  - `height`
  - `eyecolor`
  
- **Contact Information**:
  - `email`
  - `phonenumber`
  - `url`
  - `username`
  - `useragent`
  
- **Address Information**:
  - `street`
  - `city`
  - `state`
  - `county`
  - `zipcode`
  - `country`
  - `secondaryaddress`
  - `buildingnumber`
  - `ordinaldirection`
  
- **Geographical Information**:
  - `nearbygpscoordinate`
  
- **Organizational Information**:
  - `companyname`
  - `jobtitle`
  - `jobarea`
  - `jobtype`
  
- **Financial Information**:
  - `accountname`
  - `accountnumber`
  - `creditcardnumber`
  - `creditcardcvv`
  - `creditcardissuer`
  - `iban`
  - `bic`
  - `currency`
  - `currencyname`
  - `currencysymbol`
  - `currencycode`
  - `amount`
  
- **Unique Identifiers**:
  - `pin`
  - `ssn`
  - `imei` (Phone IMEI)
  - `mac` (MAC Address)
  - `vehiclevin` (Vehicle VIN)
  - `vehiclevrm` (Vehicle VRM)
  
- **Cryptocurrency Information**:
  - `bitcoinaddress`
  - `litecoinaddress`
  - `ethereumaddress`
  
- **Other Information**:
  - `ip` (IP Address)
  - `ipv4`
  - `ipv6`
  - `maskednumber`
  - `password`
  - `time`
  - `ordinaldirection`
  - `prefix`

## Prompt Format
```bash
### Instruction:
  Identify and extract the following PII entities from the text, if present: companyname, pin, currencyname, email, phoneimei, litecoinaddress, currency, eyecolor, street, mac, state, time, vehiclevin, jobarea, date, bic, currencysymbol, currencycode, age, nearbygpscoordinate, amount, ssn, ethereumaddress, zipcode, buildingnumber, dob, firstname, middlename, ordinaldirection, jobtitle, bitcoinaddress, jobtype, phonenumber, height, password, ip, useragent, accountname, city, gender, secondaryaddress, iban, sex, prefix, ipv4, maskednumber, url, username, lastname, creditcardcvv, county, vehiclevrm, ipv6, creditcardissuer, accountnumber, creditcardnumber. Return the output in JSON format.

### Input:
  Greetings, Mason! Let's celebrate another year of wellness on 14/01/1977. Don't miss the event at 176,Apt. 388.

### Output:

```

## Usage

### Installation

To use this model, you'll need to have the `transformers` library installed:

```bash
pip install transformers
```

### Run Inference
```bash
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("ab-ai/PII-Model-Phi3-Mini")
model = AutoModelForTokenClassification.from_pretrained("ab-ai/PII-Model-Phi3-Mini")


input_text = "Hi Abner, just a reminder that your next primary care appointment is on 23/03/1926. Please confirm by replying to this email Nathen15@hotmail.com."

model_prompt = f"""### Instruction:
    Identify and extract the following PII entities from the text, if present: companyname, pin, currencyname, email, phoneimei, litecoinaddress, currency, eyecolor, street, mac, state, time, vehiclevin, jobarea, date, bic, currencysymbol, currencycode, age, nearbygpscoordinate, amount, ssn, ethereumaddress, zipcode, buildingnumber, dob, firstname, middlename, ordinaldirection, jobtitle, bitcoinaddress, jobtype, phonenumber, height, password, ip, useragent, accountname, city, gender, secondaryaddress, iban, sex, prefix, ipv4, maskednumber, url, username, lastname, creditcardcvv, county, vehiclevrm, ipv6, creditcardissuer, accountnumber, creditcardnumber. Return the output in JSON format.

    ### Input:
    {input_text}

    ### Output: """


inputs = tokenizer(model_prompt, return_tensors="pt").to(device)
# adjust max_new_tokens according to your need
outputs = model.generate(**inputs, do_sample=True, max_new_tokens=120)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response) #{'middlename': ['Abner'], 'dob': ['23/03/1926'], 'email': ['Nathen15@hotmail.com']}

```