---
language: en
license: apache-2.0
tags:
- text-generation-inference
- transformers
- ruslanmv
- llama
- trl
- llama-3
- instruct
- finetune
- chatml
- DPO
- RLHF
- gpt4
- distillation
- heathcare
- medical
- clinical
- med
- lifescience
- Pharmaceutical
- Pharma
base_model: meta-llama/Meta-Llama-3-v2
datasets:
- ruslanmv/ai-medical-chatbot

model-index:
- name: Medical-Llama3-8B
  results: []
widget:
- example_title: Medical-Llama3-8B
  messages:
  - role: system
    content: >-
      You are an expert and experienced from the healthcare and biomedical
      domain with extensive medical knowledge and practical experience.
  - role: user
    content: How long does it take for newborn jaundice to go away?
  output:
    text: >-
      Newborn jaundice, also known as neonatal jaundice, is a common condition
      in newborns where the yellowing of the skin and eyes occurs due to an
      elevated level of bilirubin in the blood. Bilirubin is a yellow pigment
      that forms when red blood cells break down. In most cases, newborn
      jaundice resolves on its own without any specific treatment.
      The duration of newborn jaundice can vary depending on several factors
      such as the underlying cause, gestational age at birth, and individual
      variations in bilirubin metabolism. Here are some general guidelines
---

# Medical-Llama3-v2 Fine-Tuned Llama3 for Medical Q&A
[![](future.jpg)](https://ruslanmv.com/)
This repository provides a fine-tuned version of the powerful Llama3 8B model, specifically designed to answer medical questions in an informative way. It leverages the rich knowledge contained in the AI Medical Chatbot dataset ([ruslanmv/ai-medical-chatbot](https://huggingface.co/datasets/ruslanmv/ai-medical-chatbot)).

**Model & Development**

- **Developed by:** ruslanmv
- **License:** Apache-2.0
- **Finetuned from model:** meta-llama/Meta-Llama-3-v2

**Key Features**

- **Medical Focus:** Optimized to address health-related inquiries.
- **Knowledge Base:** Trained on a comprehensive medical chatbot dataset.
- **Text Generation:** Generates informative and potentially helpful responses.

**Installation**

This model is accessible through the Hugging Face Transformers library. Install it using pip:

```bash
pip install transformers   bitsandbytes  accelerate
```

**Usage Example**

Here's a Python code snippet demonstrating how to interact with the `Medical-Llama3-8B-16bit` model and generate answers to your medical questions:

```python

from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

# Define BitsAndBytesConfig
bnb_config = BitsAndBytesConfig(load_in_4bit=True,
                                bnb_4bit_quant_type="nf4",
                                bnb_4bit_compute_dtype=torch.float16)

# Model name
model_name = "ruslanmv/Medical-Llama3-v2"

# Load tokenizer and model with BitsAndBytesConfig
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, bnb_config=bnb_config)
model = AutoModelForCausalLM.from_pretrained(model_name, config=bnb_config)

# Ensure model is on the correct device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


# Define askme function
def askme(question):
    sys_message = ''' 
    You are Medical AI Assistant. Please be thorough and provide an informative answer. 
    If you don't know the answer to a specific medical inquiry, advise seeking professional help.
    '''   
    # Create messages structured for the chat template
    messages = [{"role": "system", "content": sys_message}, {"role": "user", "content": question}]
  
    # Applying chat template
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True, max_length=1000)
    # Move inputs to device
    input_ids = inputs['input_ids'].to(device)
    attention_mask = inputs['attention_mask'].to(device)
    # Generate outputs
    with torch.no_grad():
        outputs = model.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=1000, use_cache=True)
    # Extract and return the generated text, removing the prompt
    response_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    return response_text



# Example usage
question = '''I'm a 35-year-old male and for the past few months, I've been experiencing fatigue, 
increased sensitivity to cold, and dry, itchy skin. 
Could these symptoms be related to hypothyroidism? 
If so, what steps should I take to get a proper diagnosis and discuss treatment options?'''

print(askme(question))

```
the type of answer is :
```
Assistant:  You should consult a physician for a proper diagnosis and discussion of treatment options. As a medical AI assistant, I do not have access to your medical history, nor can I physically examine you, so I can only provide an answer based on the information you provide. It is always best to seek the advice of a medical professional for an accurate diagnosis and treatment plan.
That being said, the symptoms you have described could be related to hypothyroidism, which is a condition in which the thyroid gland does not produce sufficient hormone. Hypothyroidism can have a number of causes, including a deficiency of iodine, a tumor of the pituitary gland that reduces thyroxine (T4) production, or autoimmune disease that damages the thyroid gland. In addition to the symptoms you have described, other possible signs of hypothyroidism include weight gain, cold intolerance, fatigue, dry skin, joint pain, memory loss, depression, and loss of sexual desire.
To determine whether your symptoms are related to hypothyroidism, your physician will start by taking a history and performing a physical examination. He or she will also order several laboratory tests, including:
1. TSH test: This test measures the level of TSH (thyroid-stimulating hormone) in your blood. TSH stimulates the thyroid gland to produce T4. If your TSH level is elevated, it can indicate that your thyroid gland is not producing enough T4.
2. T4 test: This test measures the level of T4 in your blood. T4 is the main hormone produced by the thyroid gland. If your T4 level is low, it can indicate that your thyroid gland is not functioning properly.
3. T3 test: This test measures the level of T3 in your blood. T3 is another hormone produced by the thyroid gland. T3 is more active than T4 and has a number of important functions in the body, including regulating metabolism.
4. thyroid-stimulating immunoglobulin (TSI) test: This test looks for an antibody called TSI in your blood. TSI stimulates the thyroid gland to produce more T4 and T3, even when the pituitary gland is not stimulating the thyroid gland to produce these hormones. The presence of TSI can indicate autoimmune thyroiditis.
5. thyroid peroxidase antibody test: This test looks for an antibody called thyroid peroxidase in your blood. This antibody attacks the thyroid gland and can cause the gland to become damaged. The presence of this antibody can indicate autoimmune thyroiditis.
If any of these tests suggest that you have hypothyroidism, your physician may want to order additional tests to confirm the diagnosis. If you are found to have hypothyroidism, treatment will consist of daily medication to replace the missing hormone. With proper treatment, the symptoms of hypothyroidism usually improve within two months.
```

**Google Colab**


[Chatbot-Medical-Llama3-v2.ipynb](https://colab.research.google.com/github/ruslanmv/ai-medical-chatbot/blob/master/Chatbot-Medical-Llama3-v2.ipynb)



**Important Note**

This model is intended for informational purposes only and should not be used as a substitute for professional medical advice. Always consult with a qualified healthcare provider for any medical concerns.

**License**

This model is distributed under the Apache License 2.0 (see LICENSE file for details).

**Contributing**

We welcome contributions to this repository! If you have improvements or suggestions, feel free to create a pull request.

**Disclaimer**

While we strive to provide informative responses, the accuracy of the model's outputs cannot be guaranteed. It is crucial to consult a doctor or other healthcare professional for definitive medical advice.
```