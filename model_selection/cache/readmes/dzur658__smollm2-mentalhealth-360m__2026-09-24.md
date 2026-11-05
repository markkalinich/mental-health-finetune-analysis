---
library_name: transformers
license: apache-2.0
datasets:
- Amod/mental_health_counseling_conversations
language:
- en
base_model:
- HuggingFaceTB/SmolLM2-360M-Instruct
---

# SmolLM2 360m for Mental Health

<img src="model_image.png" height="500px" width="500px" />

### Model Description

<!-- Provide a longer summary of what this model is. -->

**IMPORTANT: This model has been deprecated in favor of the <a href="https://huggingface.co/dzur658/smollm2-mentalhealth-360m-V2">V2 release</a> use V2 for purposes
other than testing/research.**

This is my first fine tune of a model being uploaded to the huggingface 🤗 hub! This model is based on SmolLm2-360M-Instruct from the hugging face team, the model
was fully fine tuned locally on a 3050 TI with only 4gb of VRAM. The model has decent knowledge of common mental health topics, ie explaining to the user what
anxiety, depression, PTSD, etc are. From my limited testing the model appears to excel at describing common mental health problems from a technical standpoint 
(such as explaining what depression is defined as from the American Psychiatry Association), and can provide high level advice to the user on how to better their
mental health. The model being only 360 million parameters is small enough to run on most devices and uses approximately 700 mb of memory for inference, and is therefore
intended for lower powered edge devices including most modern smartphones. 

**This Model should in no way be used to treat, diagnose, or otherwise prevent mental health disorders, and is simply a demonstration of full fine tuning
a small model on a consumer GPU. Be smart 😊**

- **Developed by:** Alex Dzurec
- **Model type:** Large Language Model
- **Language(s) (NLP):** English (tested)
- **License:** Apache 2.0
- **Finetuned from model:** HuggingFaceTB/SmolLM2-360M-Instruct

### Model Sources

- **Repository:** <a href="https://github.com/dzur658/smollm2-mentalhealth-360m">Github</a>

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
### Uses Discovered
- **User mental health learning:** Can teach the user symptoms, and definitions regarding standard mental health issues and provide examples
- **"Advice":** Model can give broad (albiet sometimes not great) advice to a user presenting with mental health conditions

### Direct Use (Inference)

- **System Prompt:** This model was not trained with a specific system prompt although V2's prompt has shown promise in testing.
  - **V2 System Prompt:** "You are an extremely empathetic and helpful AI assistant named SmolHealth designed to listen to the user and provide insight."
- **Temperature:** 1.1 Greater temperature between 1-1.1 have been found to be better for this model
- **top_p:** 0.9 (have not tested other top_p values)

#### Use With Transformers 🤗
```
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer
model_path = "C:/Users/dzure/ai_projects/smollm_mental_health/smollm2-mentalhealth-360m-fp16/checkpoint-60"
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", torch_dtype=torch.float16)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Ensure pad token is set if tokenizer doesn't have one (pipeline might need it)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Create a pipeline
# We will format the text *before* sending it to the pipeline's generator call
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

print("Model loaded and ready for interaction.")

# Define a more specific system prompt for your fine-tuned model
system_prompt_content = "You are an extremely empathetic and helpful AI assistant named SmolHealth designed to listen to the user and provide insight. You may ask follow up questions only before ending your turn."

while True:
    print("\nType 'quit' to leave the conversation.")
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break

    # 1. Construct the messages list with system and user prompts
    messages = [
        {"role": "system", "content": system_prompt_content},
        {"role": "user", "content": user_input}
    ]

    # 2. Apply the chat template
    # add_generation_prompt=True is crucial to add the cue for the assistant to start responding
    try:
        formatted_prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
    except Exception as e:
        print(f"Error applying chat template: {e}")
        print("Ensure your tokenizer has a chat_template attribute properly configured.")
        continue # Skip this turn if formatting fails

    # 3. Generate a response using the fully formatted prompt
    # Pass generation parameters directly here for more control
    response = generator(
        formatted_prompt,
        max_new_tokens=1024,          # Increased slightly
        num_return_sequences=1,
        return_full_text=False,      # Get only the newly generated text
        do_sample=True,              # Use sampling
        temperature=1.0,             # Adjust for creativity vs. focus
        top_p=0.9,                   # Nucleus sampling
        # repetition_penalty=1.1,    # Optionally try to reduce parroting further
    )

    print("Model:", response[0]['generated_text'].strip())

print("Exiting.")
```
#### Use with GGUF
<a href="https://huggingface.co/dzur658/smollm2-mentalhealth-360m-gguf">GGUF version of the model</a>

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
The model should not be used to treat mental health disorders, nor should this model be used as a substitute
for a licensed professional.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
Preliminary testing has revealed the model to sometimes output repeating text, or (rarely) attempt to finish the users thought. The more chat turns
passed into the pipeline the larger this effect seems to become.

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->
<a href="https://huggingface.co/datasets/Amod/mental_health_counseling_conversations">View the dataset here</a>
<p>*All credit for the dataset belongs to Amod</p>

### Training Procedure

Full fine tune of SmolLm2-360m in BF16 precision using the TRL library and Pytorch running on a 3050 ti laptop GPU for 60 steps.

#### Preprocessing

**The following function was used to clean the raw dataset and format the q/a into the chat template SmolLm2 expects:**
```
def format_example(data):
    prompt = data["Context"].strip()
    response = data["Response"].strip()

    formatted = tokenizer.apply_chat_template(
        [{"role": "user", "content": prompt}, {"role": "assistant", "content": response}],
        tokenize=False,
        add_generation_prompt=False # Important for training
    )
    return formatted
```

#### Training Hyperparameters

- **Training regime:** <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->
```
training_args = TrainingArguments(
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    warmup_steps=5,
    max_steps=60,
    learning_rate=2e-4,
    fp16=not use_bf16,
    bf16=use_bf16,
    logging_steps=1,
    optim="adamw_8bit",
    weight_decay=0.01,
    lr_scheduler_type="linear",
    seed=3407,
    output_dir="smollm2-mentalhealth-360m-fp16", # IMPORTANT: model save directory
)
```

## Environmental Impact
- **Hardware Type:** 3050 TI mobile GPU
- **Hours used:** 1.5 hours
- **Carbon Emitted:** ~121 g of CO2

## More Information
This model was primarily created as my first step towards fine tuning small LLMs capable of running on mobile devices, and proving (some) viabliity of local finetuning.

## Model Card Authors

Alex Dzurec

## Credit
If you use this model please credit me by name (Alex Dzurec) or by my HuggingFace 🤗 username (dzur658)