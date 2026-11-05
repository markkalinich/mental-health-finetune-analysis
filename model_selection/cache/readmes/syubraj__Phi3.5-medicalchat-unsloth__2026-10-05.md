---
library_name: transformers
tags:
- unsloth
- trl
- sft
license: mit
datasets:
- syubraj/medical-chat-phi-3.5-instruct-1k
language:
- en
base_model:
- microsoft/Phi-3.5-mini-instruct
pipeline_tag: text-generation
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->



## Model Details

# 🏥 Phi-3.5 Mini Instruct Medical Chat (Unsloth)

The **MedicalChat-Phi-3.5-mini-instruct-** fine-tuned model is designed to simulate doctor-patient conversations, offering medical consultations and suggestions based on patient queries. However, its accuracy may be limited in real-world scenarios, as the training dataset was relatively small.

## 🔍 Model Overview
- **🧑‍⚕️ Developed by:** [syubraj](https://huggingface.co/syubraj)
- **📜 Model Type:** Causal Language Model (CausalLM)
- **🗣️ Language:** English
- **📜 License:** MIT License
- **🛠️ Fine-tuned From:** [microsoft/phi-3.5-mini-instruct](https://huggingface.co/microsoft/Phi-3.5-mini-instruct)

---


## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

```bash
!pip install unsloth
```

```Python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained("syubraj/Phi3.5-medicalchat-unsloth",
                                                      max_seq_length = 1024,
                                                      load_in_4bit = True,
                                                      dtype = None
)
user_query = "<Your medical query here>"
system_prompt = """You are a trusted AI-powered medical assistant. Analyze patient queries carefully and provide accurate, professional, and empathetic responses. Prioritize patient safety, adhere to medical best practices, and recommend consulting a healthcare provider when necessary."""


message = [
    {"role": "system", "content": system_prompt},
    {"role": "human", "content": user_query}
]

# Creating message based on tokenizers chat template
prompt = tokenizer.apply_chat_template(message, tokenize = False, add_generation_prompt = True)

FastLanguageModel.for_inference(model)

# Tokenizing inputs
inputs = tokenizer(prompt, return_tensors = "pt").to("cuda")

# Output Generated
outputs = model.generate(**inputs, max_new_tokens=256, use_cache=True) # Change the `max_new_tokens` according to required objective
tokenizer.batch_decode(outputs)
```

### Model Results


| Step | Training Loss |
|------|--------------|
| 10   | 2.53         |
| 20   | 2.20         |
| 30   | 1.95         |
| 40   | 2.01         |
| 50   | 1.97         |
| 60   | 2.02         |
