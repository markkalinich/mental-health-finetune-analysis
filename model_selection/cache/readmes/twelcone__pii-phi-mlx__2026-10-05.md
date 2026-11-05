---
base_model: twelcone/pii-phi-mlx
library_name: mlx
pipeline_tag: text-generation
tags:
- mlx
---

# Overview

`pii-phi-mlx` is a CoreML fine-tuned version of `Phi-3.5-mini-instruct` designed to extract Personally Identifiable Information (PII) from unstructured text for Mac devices. The model outputs PII entities in a structured JSON format according to strict schema guidelines.

# Training Prompt Format

```text
# GUIDELINES
- Extract all instances of the following Personally Identifiable Information (PII) entities from the provided text and return them in JSON format.
- Each item in the JSON list should include an 'entity' key specifying the type of PII and a 'value' key containing the extracted information.
- The supported entities are: PERSON_NAME, BUSINESS_NAME, API_KEY, USERNAME, API_ENDPOINT, WEBSITE_ADDRESS, PHONE_NUMBER, EMAIL_ADDRESS, ID, PASSWORD, ADDRESS.

# EXPECTED OUTPUT
- The json output must be in the format below:
{
    "result": [
        {"entity": "ENTITY_TYPE", "value": "EXTRACTED_VALUE"},
        ...
    ]
}
```

# Supported Entities

* PERSON\_NAME
* BUSINESS\_NAME
* API\_KEY
* USERNAME
* API\_ENDPOINT
* WEBSITE\_ADDRESS
* PHONE\_NUMBER
* EMAIL\_ADDRESS
* ID
* PASSWORD
* ADDRESS

# Intended Use

The model is intended for PII detection in text documents to support tasks such as data anonymization, compliance, and security auditing.

# Limitations

* Not guaranteed to detect all forms of PII in every context.
* May return false positives or omit contextually relevant information.

---

# Installation

Install the `vllm` package to run the model efficiently:

```bash
pip install vllm
```

---

# Example:

```python
from vllm import LLM, SamplingParams

llm = LLM("Fsoft-AIC/pii-phi")

system_prompt = """
# GUIDELINES
- Extract all instances of the following Personally Identifiable Information (PII) entities from the provided text and return them in JSON format.
- Each item in the JSON list should include an 'entity' key specifying the type of PII and a 'value' key containing the extracted information.
- The supported entities are: PERSON_NAME, BUSINESS_NAME, API_KEY, USERNAME, API_ENDPOINT, WEBSITE_ADDRESS, PHONE_NUMBER, EMAIL_ADDRESS, ID, PASSWORD, ADDRESS.

# EXPECTED OUTPUT
- The json output must be in the format below:
{
    "result": [
        {"entity": "ENTITY_TYPE", "value": "EXTRACTED_VALUE"},
        ...
    ]
}
"""
pii_message = "I am James Jake and my employee number is 123123123"

sampling_params = SamplingParams(temperature=0, max_tokens=1000)
outputs = llm.chat(
    [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": pii_message},
    ],
    sampling_params,
)


for output in outputs:
    generated_text = output.outputs[0].text
    print(generated_text)
```