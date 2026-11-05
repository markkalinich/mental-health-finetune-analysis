---
base_model: tiiuae/Falcon3-1B-Instruct
library_name: transformers
license: apache-2.0
datasets:
- marmikpandya/mental-health
language:
- en
tags:
- mentalhealth
- selfcare
- wellness
- wellbeing
- depression
- anxiety
- stress
- emotionalsupport
- mentalsupport
- advisor
pipeline_tag: text-generation
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

Falcon3-1B-MentalHealth is a fine-tuned version of the tiiuae/Falcon3-1B-Instruct model, adapted for providing empathetic and contextually relevant responses to mental health-related queries. 
Since it is fine-tuned on an Instruct model, it's responses are contextually appropriate and reasonable.
The model has been trained on a curated dataset to assist in mental health conversations, offering advice, guidance, and support for individuals dealing with issues like stress, anxiety, and depression. 
It provides a compassionate approach to mental health queries while focusing on promoting emotional well-being and mental health awareness.

# Important Note
As Mental Health is a sensitive topic, it would be preferable to use the code snippet provided below in order to get optimal results. It is expected that this model will be used responsibly.

# Falcon3-1B-Instruct Fine-Tuned for Mental Health (LoRA)

This is a LoRA adapter for the Falcon3-1B-Instruct LLM which has been merged with the respective base model. It was fine-tuned on the 'marmikpandya/mental-health' dataset.

## Usage

### Dependencies
```bash
pip install transformers accelerate torch peft bitsandbytes --quiet
```

### Basic Usage
```python
import torch
import re
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load the model from Hugging Face
model_name = "ShivomH/Falcon3-1B-MentalHealth"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Move the model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def chat():

    print("Chat with your fine-tuned Falcon model (type 'exit' to quit):")

    system_instruction = (
        "### Instruction:\n"
        "You are an empathetic AI specialized in mental health support. "
        "Do not respond to topics that are unrelated to the medical domain. \n"
        "If a crisis situation is detected, suggest reaching out to a mental health professional immediately. "
        "Your responses should be clear, precise, supportive, comforting and free from speculation."
    )

    # Store short chat history for context
    chat_history = []

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break

        # Maintain short chat history (last 3 exchanges)
        chat_history.append(f"User: {user_input}")
        chat_history = chat_history[-1:]

        prompt = f"{system_instruction}\n\n" + "\n".join(chat_history) + "\nAssistant:"

        inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=100,
                pad_token_id=tokenizer.eos_token_id,
                temperature=0.5,
                top_p=0.85,
                repetition_penalty=1.2,
                do_sample=True,
                no_repeat_ngram_size=3,
                early_stopping=True
            )

        response = tokenizer.decode(output[0], skip_special_tokens=True).strip()

        if "Assistant:" in response:
            response = response.split("Assistant:", 1)[-1].strip()

        # Remove URLs from the response
        response = re.sub(r'http[s]?://\S+', '', response)

        print(f"Assistant: {response}")

chat()
```

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Shivom Hatalkar
- **Model type:** Text-generation
- **Language(s) (NLP):** English
- **License:** apache-2.0
- **Finetuned from model:** Falcon3-1B-Instruct

## Bias, Risks, and Limitations

* Not a Substitute for Professional Care: This model is not a licensed mental health professional. Its responses may be incomplete, inaccurate, or unsuitable for serious conditions.
* Inherent Biases - May reflect biases in training data (e.g., cultural assumptions, stigmatizing language).
* Crisis Limitations - Not designed for crisis intervention (e.g., suicidal ideation, self-harm). Always direct users to human professionals or emergency services.
* Over-Reliance Risk - Outputs could inadvertently worsen symptoms if users interpret them as definitive advice.
* Intended Use - Assist with general emotional support, not diagnosis or treatment.

## Training Hyperparameters

| Hyperparameter  | Value |
| ------------- | ------------- |
| Precision  | float16  |
| Optimizer  | AdamW_32bit  |
| Learning rate  | 2e-4  |
| Weight decay  | 1e-2  |
| Batch size  | 2  |
| Training Epochs  | 3  |
| Quantization  | 8-Bit  |
| LoRA Dropout  | 0.1  |
| LoRA Rank  | 16  |
| Warmup Ratio  | 0.03  |

```